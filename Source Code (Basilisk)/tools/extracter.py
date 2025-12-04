#from asm import asm_ref;
#from asm import assembler;
from tools import gen;
import os;
from sys import exit;
from wave import open as wave_open;
from pyaudio import PyAudio;

hex_format = gen.hex_format;
hex_format2 = gen.hex_format2;

unprotect_bits = "0123456789abcdef";
protect_bits = "０１２３４５６７８９ＡＢＣＤＥＦ";

chapter_count = 25;

def play_sound(file):
    wf = wave_open(file, 'rb')
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(1024)
    while data != b'':
        stream.write(data)
        data = wf.readframes(1024)
    stream.stop_stream()
    stream.close()
    p.terminate()

def get_chapter_count(arg_project):
    chapter_count = 0;
    i = 0; 
    base_path = arg_project + "chapters/ch_";
    while (True):
        i += 1;
        end_path = str(i);
        if (i < 10):
            end_path = "0" + end_path;
        if os.path.exists(base_path + end_path):
            chapter_count += 1;
            
def get_data_size(arg_data):
    tmp_len = 0;
    for e in arg_data:
        line = arg_data[e];
        tmp_len += len(line);
    return tmp_len;

def input_intro_config(arg_project):
    lst = [];
    with open(arg_project + "/gameplay/intro_config.txt") as file:
        for line in file:
            if (len(line) > 6) and (line[0] != "C"):
                line = line[3:-1].split(":");
                key = line[0];
                val = int(line[1].strip(), 16);
                match key:
                    case "Line":
                        lst.append(val);
                    case "BGM":
                        lst.append(val);
                    case _:
                        print("Error! Invalid argument in intro_config.txt: " + key);
    return lst;
    

def input_shoploc(arg_project):
    tmp_shops = dict();
    index = 0;
    for ch_i in range(0, chapter_count):
        nmb = str(ch_i + 1);
        if (ch_i < 9):
            nmb = "0" + nmb;
        tmp_i = hex_format(index);
        tmp_dir = arg_project + "/chapters/ch_" + nmb + "/";
        file = open(tmp_dir + "shops.txt", "r");
        tmp_shop = [];
        for line in file:
            line = line[:-1];
            if ":" in line:
                tmp = line.split(":", 1);
                data = tmp[0];
                val = tmp[1];
                tmp_shop.append(int(val[1:3], 16));
        tmp_shop.append(0xf0);
        tmp_shops[tmp_i] = list(tmp_shop);
        index += 1;
        file.close();
    return tmp_shops;

def input_ports(arg_project):
    ports = [];
    with open(arg_project + "/gameplay/unit_port_index.txt", "r") as file:
        for line in file:
            line = line[:-1];
            val = line.split("=")[1];
            if (val == "none"):
                ports.append(0xff);
            else:
                ports.append(int(val, 16));
    return ports;
            

def input_promotes(arg_project):
    tmp_p = [[0x0,], [0x0,]];
    base_dir = arg_project + "/gameplay/promote_";
    lbls = ("items.txt", "class.txt");
    i = 0;
    for lbl in lbls:
        lst = tmp_p[i];
        with open(base_dir + lbl) as file:
            for line in file:
                vals = line.split("->");
                lst.append(int(vals[1], 16));
        i += 1;
    return tmp_p;

def input_events(arg_project):
    tmp_shops = dict();
    index = 0;
    for ch_i in range(0, chapter_count):
        nmb = str(ch_i + 1);
        if (ch_i < 9):
            nmb = "0" + nmb;
        tmp_i = hex_format(index);
        tmp_dir = arg_project + "/chapters/ch_" + nmb + "/";
        file = open(tmp_dir + "events.txt", "r");
        tmp_shop = [];
        for line in file:
            line = line[:-1];
            if ":" in line:
                tmp = line.split(":", 1);
                data = tmp[0];
                val = tmp[1];
                tmp_shop.append(int(val[1:3], 16));
        tmp_shop.append(0x00);
        tmp_shops[tmp_i] = list(tmp_shop);
        index += 1;
        file.close();
    return tmp_shops;

def input_maps(arg_project):
    tmp_maps = dict();
    index = 0;
    for ch_i in range(0, chapter_count):
        tmp_map = [];
        nmb = str(ch_i + 1);
        if (ch_i < 9):
            nmb = "0" + nmb;
        tmp_i = hex_format(index);
        tmp_dir = arg_project + "/chapters/ch_" + nmb + "/";
        file = open(tmp_dir + "map_" + nmb + ".txt", "r");
        tmp_map = [];
        for line in file:
            if line == "\n":
                break;
            line = line[:-1];
            i = 0;
            while (i < (len(line))):
                tmp_map.append(int(line[i:i + 2], 16));
                i += 2;
        tmp_maps[tmp_i] = list(tmp_map);
        index += 1;
        file.close();
    return tmp_maps;

def compress_map(arg_map):
    tmp_map = arg_map;
    global new_map;
    new_map = [];
    new_map.append(tmp_map[0]);
    new_map.append(tmp_map[1]);
    new_map.append(tmp_map[2]);
    new_map.append(tmp_map[3]);
    global repeat_count;
    repeat_count = 0;
    global last_byte;
    last_byte = -1;
    byte = -1;
    last_byte = -1;
    i = 4; i_end = len(tmp_map);
    i2 = 0;
    while (i < i_end):
        byte = tmp_map[i];
        i2 = i + 1;
        repeat_count = 0;
        while (i2 < i_end):
            next_byte = tmp_map[i2];
            if (next_byte == byte):
                i2 += 1;
                repeat_count += 1;
                if (repeat_count > 0x35):
                    break;
            else:
                break;
        new_map.append(byte);
        if (repeat_count > 0):
            new_map.append(0xc8 + repeat_count);
            i = i2 - 1;
        i += 1;
    new_map.append(0x00);
    return new_map;

def load_dct_names(arg_project):
    tmp_dct = dict();
    with open(arg_project + "/text/dictionary/dictionary_names.txt", "r") as file:
        for line in file:
            if (len(line) > 3) and (line[3:-1] != " "):
                if line[-1] == "\n":
                    tmp_dct[line[0:2]] = line[3:-1];
                else:
                    tmp_dct[line[0:2]] = line[3:];
    return tmp_dct;

    
def get_bytestr(arg_dct, arg_index):
    txt = "";
    for i in arg_dct[hex_format(arg_index)]:
        txt += hex_format(i);
    return txt;

def input_script(arg_project, arg_name, arg_tbl, arg_bankbyte=0x80, arg_usedct=True):
    def get_cc(arg_line):
        tmp_cc = "";
        for c in arg_line:
            tmp_cc = tmp_cc + c;
            if c == "]":
                break;
        return tmp_cc;
    
    if (arg_usedct):
        tmp_dct = dict();
        with open(arg_project + "/text/dictionary/dictionary.txt", "r") as file:
            for line in file:
                if line[-1] == "\n":
                    tmp_dct[line[0:2]] = line[3:-1];
                else:
                    tmp_dct[line[0:2]] = line[3:];
        tmp_dct2 = dict();
        with open(arg_project + "/text/dictionary/dictionary2.txt", "r") as file:
            for line in file:
                if line[-1] == "\n":
                    tmp_dct2[line[0:2]] = line[3:-1];
                else:
                    tmp_dct2[line[0:2]] = line[3:];
    else:
        tmp_dct = {};
        tmp_dct2 = {};
    tmp_data = dict();
    line_nmb = "";
    with open(arg_project + "/text/script/" + arg_name + ".txt", "r") as file:
        scan_text = False;
        printed_text = False;
        tmp_lst = [];
        for line in file:
            end = False;
            if not scan_text:
                if line[0] == "{":
                    printed_text = False;
                    scan_text = True;
                    line_nmb = line[1:3];
                    #print(line_nmb);
            else:
                if (len(line) > 15) and ("[MSG SPD]" in line):
                    tmp_i = line.find("[MSG SPD]");
                    tmp_cc = line[tmp_i:tmp_i + 14];
                    tmp_lst.append(0xe9);
                    tmp_val = tmp_cc[11:13];
                    tmp_byte = int(tmp_val, 16);
                    tmp_lst.append(tmp_byte);
                    line = line.replace(tmp_cc, "");
                if line[0] == "=":
                    do_nothing = 0;
                elif line[0] == "[":
                    printed_text = False;
                    cc = get_cc(line);
                    cc2 = line[0:2];
                    if cc == "[TITLE]":
                        tmp_lst.append(0xe5);
                    elif cc == "[MESSAGE]":
                        do_nothing = 0;
                    elif cc == "[PORTRAIT]":
                        tmp_lst.append(0xe8);
                    elif cc == "[MSG SPD]":
                        tmp_lst.append(0xe9);
                        tmp_val = line[11:13];
                        tmp_byte = int(tmp_val, 16);
                        tmp_lst.append(tmp_byte);
                    elif cc == "[MUSIC]":
                        tmp_lst.append(0xdf);
                        tmp_val = line[9:11];
                        tmp_byte = int(tmp_val, 16);
                        tmp_lst.append(tmp_byte);
                    elif cc == "[KEEP_MUSIC]":
                        tmp_lst.append(0xe0);
                    elif cc == "[NEXT_EPILOGUE]":
                        tmp_lst.append(0xe1);
                        tmp_lst.append(0x01);
                        tmp_lst.append(0xe7);
                        end = True;
                    elif cc == "[GOTO]":
                        tmp_lst.append(0xe6);
                        
                        tmp_val = line[8:10];
                        tmp_byte = int(tmp_val, 16);
                        tmp_lst.append(tmp_byte);
                        
                        tmp_val = line[12:14];
                        tmp_byte = int(tmp_val, 16);
                        tmp_lst.append(tmp_byte);
                        end = True;
                    elif cc == "[JUMP]":
                        tmp_lst.append(0xe4);
                        
                        tmp_val = line[8:10];
                        tmp_byte = int(tmp_val, 16);
                        tmp_lst.append(tmp_byte);
                        
                        tmp_val = line[12:14];
                        tmp_byte = int(tmp_val, 16);
                        tmp_lst.append(tmp_byte);
                        end = True;
                    elif cc == "[YESNO]":
                        tmp_lst.append(0xe7);
                        end = True;
                    elif cc == "[TURN_OFF_BLIPS]":
                        tmp_lst.append(0xe2);
                    elif cc == "[BTL_WINDOW]":
                        tmp_lst.append(0x05);
                        tmp_lst.append(0x13);
                        tmp_lst.append(0x16);
                        tmp_lst.append(0x04);
                    elif cc2 == "[X":
                        tmp_val = line[4:5];
                        tmp_byte = int(tmp_val + "0", 16);
                        tmp_lst.append(tmp_byte);
                        tmp_val = line[10:11];
                        tmp_byte = int(tmp_val + "0", 16);
                        tmp_lst.append(tmp_byte);
                    elif cc2 == "[W":
                        tmp_val = line[4:6];
                        tmp_byte = int(tmp_val, 16);
                        tmp_lst.append(tmp_byte);
                        tmp_val = line[11:13];
                        tmp_byte = int(tmp_val, 16);
                        tmp_lst.append(tmp_byte);
                    elif cc2 == "[C":
                        tmp_val = line[4:6];
                        tmp_byte = int(tmp_val, 16);
                        tmp_lst.append(tmp_byte);
                    elif cc == "[NEXT]":
                        tmp_lst.append(0xee);
                    elif cc == "[END]":
                        tmp_lst.append(0xef);
                        end = True;
                    else:
                        print("*** Invalid Control Code: " + cc + " ***");
                elif line == "\n":
                    tmp_lst.append(0xed);
                    printed_text = False;
                elif len(line) < 2:
                    printed_text = False;
                    do_nothing = 1;
                else:
                    if printed_text:
                        printed_text = False;
                        tmp_lst.append(0xed);
                    if arg_usedct:
                        for i in tmp_dct:
                            if tmp_dct[i] in line:
                                line = line.replace(tmp_dct[i], "[8f][" + i + "]");
                        for i in tmp_dct2:
                            if tmp_dct2[i] in line:
                                line = line.replace(tmp_dct2[i], "[8e][" + i + "]");
                    tmp_line_lst = detableize(line, arg_tbl);
                    for i in tmp_line_lst:
                        tmp_lst.append(i);
                    printed_text = True;
                if end:
                    printed_text = False;
                    tmp_data[line_nmb] = list(tmp_lst);
                    tmp_lst = [];
                    scan_text = False;
                    end = False;
    return tmp_data;

def input_from_file(arg_project, arg_fname, arg_tbl, arg_endbyte, arg_fixln=-1, arg_dct={}):
    tmp_dct = dict();
    check = (arg_fname == "/text/names/names");
    ini = True;
    
    file = open(arg_project + arg_fname + ".txt", "r");
    for line in file:
        tmp_key = line[0:2].lower();
        tmp_word = line[3:(len(line))];
        if (check):
            if (ini):
                tmp_name = tmp_word[:-1].lower();
                if (tmp_name == "marth"):
                    print("Error! Invalid name for unit 01.");
                    play_sound("resource/data/cache.dat");
                    exit(0);
                ini = False;
        if (arg_dct):
            for key in arg_dct:
                dct_word = arg_dct[key];
                if dct_word in tmp_word:
                    tmp_word = tmp_word.replace(dct_word, "[8f][" + key + "]");
        tmp_val = detableize(tmp_word, arg_tbl);
        if arg_fixln != -1:
            while (len(tmp_val) < arg_fixln):
                tmp_val.append(arg_endbyte);
        else:
            tmp_val.append(arg_endbyte);
        tmp_dct[tmp_key] = tmp_val;
    file.close();
    return tmp_dct;

def input_growths(arg_project):
    dct = dict();
    key = "?";
    with open(arg_project + "/gameplay/growths.txt", "r") as file:
        for line in file:
            if line[0] == "{":
                key = line[1:3];
                dct[key] = [];
            elif ":" in line:
                sub = line[:-1].split(":", 1);
                val = sub[1][1:];
                dct[key].append(int(val, 16));
    return dct;

def input_bases(arg_project):
    dct = dict();
    key = "?";
    with open(arg_project + "/gameplay/class_bases.txt", "r") as file:
        for line in file:
            if line[0] == "{":
                key = line[1:3];
                dct[key] = [];
            elif ":" in line:
                sub = line[:-1].split(":", 1);
                val = sub[1][1:];
                dct[key].append(int(val));
    return dct;

def input_recruits(arg_project):
    lst1 = [];
    lst2 = [];
    lst3 = [];
    lst4 = [];
    with open(arg_project + "/gameplay/recruitment.txt") as file:
        for line in file:
            if (len(line) > 6):
                line = line[3:-1].split(":");
                key = line[0];
                val = int(line[1].strip(), 16);
                match key:
                    case "Recruiter":
                        lst1.append(val);
                    case "Enemy":
                        lst2.append(val);
                    case "New Player ID":
                        lst3.append(val);
                    case "Recruit Line":
                        lst4.append(val);
                    case _:
                        print("Error! Invalid argument in recruitment.txt: " + key);
    return (lst1, lst2, lst3, lst4);

range_table = {};
range_table["00"] = "none";  
range_table["01"] = "no_cmd";    
range_table["0a"] = "1";  
range_table["0c"] = "2";  
range_table["0e"] = "1-2";  
range_table["12"] = "1_staff";  
range_table["32"] = "long_staff";  
range_table["41"] = "item_cmd";  
range_table["4a"] = "1_item";  
range_table["4c"] = "2_item";  
range_table["4e"] = "1-2_item";  
tmp_keys = range_table.copy().keys();
for key in tmp_keys:
    val = range_table[key];
    range_table[val] = key;

effect_table = {};
effect_table["00"] = "none";
effect_table["01"] = "live";
effect_table["02"] = "relive";
effect_table["03"] = "recover";
effect_table["04"] = "unknown";
effect_table["05"] = "magic_proof";
effect_table["06"] = "falchion";
effect_table["07"] = "warp";
effect_table["08"] = "hammerne";
effect_table["09"] = "ohm";
effect_table["0a"] = "reserve";
effect_table["0b"] = "maph";
effect_table["0c"] = "mshield";
effect_table["0d"] = "helarn";
effect_table["0e"] = "2range_proof";
tmp_keys = effect_table.copy().keys();
for key in tmp_keys:
    val = effect_table[key];
    effect_table[val] = key;

type_table = {};
type_table["00"] = "sword";
type_table["01"] = "lance";
type_table["02"] = "bow";
type_table["03"] = "ballista";
type_table["04"] = "axe";
type_table["05"] = "dragonstone";
type_table["06"] = "tome";
type_table["07"] = "staff";
type_table["08"] = "staff_ohm";
type_table["0b"] = "lord_only";
type_table["fe"] = "no_equip";
type_table["a5"] = "no_equip";
tmp_keys = type_table.copy().keys();
for key in tmp_keys:
    val = type_table[key];
    type_table[val] = key;
    
    
#TODO
itemdata_ints = ("Might", "Weight", "Hit", "Crit", "Price", "Uses");

def input_itemdata(arg_project):
    dt = {};
    dt["Might"] = [];
    dt["WLevel"] = [];
    dt["Weight"] = [];
    dt["Hit"] = [];
    dt["Crit"] = [];
    dt["Price"] = [];
    dt["Uses"] = [];
    dt["Bonus"] = [];
    dt["Effect"] = [];
    dt["Range"] = [];
    dt["Type"] = [];
    with open(arg_project + "/gameplay/items/item_data.txt") as file:          
        byte = "";
        byte_val = 0x0;
        index = 0x0;
        for line in file:
            if (len(line) > 2):
                if line[2] == ":":
                    byte = line[0:2];
                else:
                    line = line[:-1].split(":", 1);
                    name = line[0].strip();
                    value = line[1].strip();
                    if (name in itemdata_ints):
                        byte_val = int(value);
                    elif name == "Bonus":
                        byte_val = int(value, 16);
                    elif name == "WLevel":
                        if (len(value) > 2) and (value[0:3] == "prf"):
                            byte_val = int(value[4:6], 16) + 0x80;
                        else:
                            byte_val =  int(value);
                    elif name == "Effect":
                        if not value in effect_table:
                            print("Error! Invalid effect (" + value + ")!");
                        byte_val = int(effect_table[value], 16);
                    elif name == "Range":
                        if not value in range_table:
                            print("Error! Invalid item range (" + value + ")!");
                        byte_val = int(range_table[value], 16);
                    elif name == "Type":
                        if not value in type_table:
                            print("Error! Invalid item type (" + value + ")!");
                        byte_val = int(type_table[value], 16);   
                    dt[name].append(byte_val);
                    byte_val = 0x0;      
    return dt;

def insert_itemtable(arg_project, arg_icount=0x5c):
    table_might = []; table_wlevel = [];
    table_weight = []; table_hit = [];
    table_crit = []; table_price = [];
    table_uses = []; table_bonus = [];
    table_effect = []; table_range = [];
    table_type = [];
    with open(arg_project + "/tables/items.txt") as file: 
        for line in file:
            if len(line) > 4:
                line = line[:-1].split(":", 1);
                arg = line[0].strip();
                val = line[1].strip();
                byte = 0;
                tmp_tbl = [];
                if arg == "might":
                    byte = int(val);
                    tmp_tbl = table_might;
                elif arg == "wlevel":
                    if (val[0] == "p"):
                        byte = int(val[3:5], 16);
                    else:
                        byte = int(val);
                    tmp_tbl = table_wlevel;
                elif arg == "weight":
                    byte = int(val);
                    tmp_tbl = table_weight;
                elif arg == "hit":
                    byte = int(val);
                    tmp_tbl = table_hit;
                elif arg == "crit":
                    byte = int(val);
                    tmp_tbl = table_crit;
                elif arg == "price":
                    byte = int(val);
                    tmp_tbl = table_price;
                elif arg == "uses":
                    byte = int(val);
                    tmp_tbl = table_uses;
                elif arg == "bonus":
                    byte = int(val[2:4], 16);
                    tmp_tbl = table_bonus;
                elif arg == "effect":
                    if byte in effect_table.keys():
                        byte = int(effect_table[byte], 16);
                    else:
                        print("Error!");
                    tmp_tbl = table_effect;
                elif arg == "range":
                    tmp_tbl = table_range;
                elif arg == "type":
                    tmp_tbl = table_type;
                tmp_tbl.append(byte);


def input_units(arg_project):
    super_lst = [];
    for ch_i in range(0, chapter_count):
        nmb = str(ch_i + 1);
        if (ch_i < 9):
            nmb = "0" + nmb;
        tmp_dir = arg_project + "/chapters/ch_" + nmb + "/";
        units = [];
        with open(tmp_dir + "units.txt", "r") as file:
            for line in file:
                if line[0:2] == "00":
                    break;
                else:
                    i = 0;
                    unit = [];
                    while (i < len(line) - 1):
                        byte = int(line[i:i + 2], 16);
                        unit.append(byte);
                        i += 2;
                    units.append(list(unit));
        super_lst.append(list(units));
    return super_lst;

def input_struct(arg_project, arg_name):
    super_lst = [];
    for ch_i in range(0, 25):
        nmb = str(ch_i + 1);
        if (ch_i < 9):
            nmb = "0" + nmb;
        tmp_dir = arg_project + "/chapters/ch_" + nmb + "/";
        units = [];
        with open(tmp_dir + arg_name + ".txt", "r") as file:
            for line in file:
                if line[0:2] == "00":
                    break;
                else:
                    i = 0;
                    unit = [];
                    while (i < len(line) - 1):
                        byte = int(line[i:i + 2], 16);
                        unit.append(byte);
                        i += 2;
                    units.append(list(unit));
        super_lst.append(list(units));
    return super_lst;

def input_spawns(arg_project):
    super_lst = dict();
    for ch_i in range(0, 25):
        nmb = str(ch_i + 1);
        if (ch_i < 9):
            nmb = "0" + nmb;
        tmp_dir = arg_project + "/chapters/ch_" + nmb + "/";
        ch = [];
        with open(tmp_dir + "spawns.txt", "r") as file:
            i2 = 0;
            for line in file:
                if i2 == 0:
                    ch.append(int(line[0:2], 16));
                    i2 += 1;
                else:
                    ch.append(int(line[0:2], 16));
                    ch.append(int(line[2:4], 16));
        super_lst[hex_format(ch_i)] = list(ch);
    return super_lst;

def struct_make_bank(arg_project, arg_name):
    tmp_data = -1;
    tmp_bank = dict();
    i = 0;
    if (arg_name == "units"):
        tmp_data = input_units(arg_project);
    else:
        tmp_data = input_struct(arg_project, arg_name);
    if tmp_data != -1:
        for ch in tmp_data:
            tmp_entry_index = hex_format(i);
            if ch == []:
                tmp_bank[tmp_entry_index] = [0];
            else:
                ch_units = [];
                for unit in ch:
                    for byte in unit:
                        ch_units.append(byte);
                ch_units.append(0);
                tmp_bank[tmp_entry_index] = list(ch_units);   
            i += 1;
    return tmp_bank;

def load_tbl(arg_filename):
    tmp_tbl = dict();
    for i in range(0xff):
        tmp_tbl[hex_format(i)] = "[" + hex_format(i) + "]";
    file = open(arg_filename + ".tbl", "r");
    for line in file:
        tmp_tbl[(line[0:2]).lower()] = line[3:(len(line) - 1)];
    file.close();
    return tmp_tbl;

def blank_tbl():
    tmp_tbl = dict();
    for i in range(0xff):
        tmp_tbl[hex_format(i)] = "[" + hex_format(i) + "]";
    return tmp_tbl;
    
def tableize(arg_bytelist, arg_tbl):
    tmp_str = "";
    for i in arg_bytelist:
        if hex_format(i) in arg_tbl:
            tmp_str = tmp_str + arg_tbl[hex_format(i)];
    return tmp_str;

def detableize(arg_str, arg_tbl):
    tmp_lst = [];
    for i in arg_tbl:
        tmp = arg_tbl[i];
        if (len(tmp) > 1):
            arg_str = arg_str.replace(tmp, "[" + i + "]");
    i = 0;
    while i < (len(arg_str) - 1):
        tmp = arg_str[i];
        if tmp == "[":
            tmp_lst.append(int(arg_str[(i + 1):(i + 3)], 16));
            i += 3;
            continue;
        for i2 in arg_tbl:
            if arg_tbl[i2] == tmp:
                tmp_lst.append(int(i2, 16));
                break;
        i += 1;
    return tmp_lst;

def protect(arg_str):
    for i in range(len(unprotect_bits) - 1):
        arg_str = arg_str.replace(unprotect_bits[i], protect_bits[i]);
    return arg_str;

def unprotect(arg_str):
    for i in range(len(unprotect_bits) - 1):
        arg_str = arg_str.replace(protect_bits[i], unprotect_bits[i]);
    return arg_str;

def rom_append(arg_file, arg_location, arg_byte):
    arg_file.seek(arg_location);
    arg_file.write(bytes([arg_byte]));

'''
def output_code(arg_rom, arg_bank_index, arg_ranges, arg_name = ""):
    bank_index_name = gen.hex_format(arg_bank_index)
    #base_name = "asm/bank_" + bank_index_name + "/asm_" + str(bank_index_name);
    if not (arg_name == ""):
        base_name += "_" + arg_name;
    fname = base_name + ".txt";
    line_nmb = 0;
    with open(fname, "w") as file:
        txt = "";
        for i in range(0, len(arg_ranges)):
            asm_range = arg_ranges[i];
            asm_pos = asm_range[0x0];
            asm_end = asm_range[0x1];
            txt += "///(Vanilla Range: " + hex(asm_pos) + " - " + hex(asm_end) + ")\n";
            while (True):
                if not (asm_pos < asm_end):
                    break;
                local_adr = gen.local_adr_str(asm_pos);
#   gen          txt += "[rtn_0f_" + local_adr + "]\n";
                results = assembler.disassemble(arg_rom, aassembler
                result = results[0x2];
                if (result):
                    print("Error in file " + gen.hex_format(i) + "!");
#     gen        cmds = results[0x0];
                for cmd in cmds:
                    txt += cmd + "\n";
                txt +="\n\n\n";
                asm_pos = results[0x1];
        file.write(txt);

def output_asm(arg_rom, arg_r):
    pos = arg_r[0x0];
    name = arg_r[0x1];
    routines = [arg_r,];
    fname = name + ".txt";
    cmds = assembler.disassemble(arg_rom, passembler txt = "";
    with open("asm_tnp/" + fname, "w") as file: 
        local_adr = gen.abs_to_ptr(pos); #0x3fd00
# gen    txt = "///" + name + " ($" + gen.hex_format2(local_adr) + ")\gen
        for cmd in cmds:
            txt += cmd + "\n";
        file.write(txt);
    print("Created file " + fname);
    
#compiles = assembler.assemble("exit_dct_cheassemblerompiles = assembler.assemble("exit_dct_cheassemblerdef print_assembled(arg_fname):
    compiles = assembler.assemble(arg_fname);
#assembleroutine in compiles:
        print("[" + routine[0x1] + "]");
        for inst_list in routine[:-1]:
            for inst in inst_list:
                txt = "(";
                for op in inst:
                    txt += gen.hex_format(op) + ", ";
    gen         txt += ")";
                print(txt);
                
def get_labels(arg_fname):
    with open(arg_fname + ".txt", "r") as file:
        labels = [];
        for line in file:
            if (len(line) > 0) and (line[0] == "["):
                labels.append(line[0:-1]);
    with open("tmp_labels.txt", "w") as file:
        txt = "";
        for label in labels:
            txt += "//" + label + "\n";
        file.write(txt);
        

routines = {};
routines["get_dct_cc"] = (0x3fd00, "get_dct_cc");
routines["get_dct_cc2"] = (0x3fd67, "get_dct_cc2");
routines["exit_dct_check"] = (0x3ff90, "exit_dct_check");

def add_routine(name, adr):
    routines[name] = (adr, name);

add_routine("b0f_01", 0x3c010);
add_routine("b0f_02", 0x3c01d);
add_routine("b0f_03", 0x3c02a);
add_routine("b0f_04", 0x3c037);
add_routine("b0f_05", 0x3c044);
add_routine("b0f_06", 0x3c051);
add_routine("b0f_07", 0x3c05e);
add_routine("b0f_08", 0x3c078);
add_routine("b0f_09", 0x3c085);
add_routine("b0f_10", 0x3c154);
add_routine("b0f_11", 0x3c16d);
add_routine("b0f_12", 0x3c173);
add_routine("b0f_13", 0x3c1d4);
add_routine("b0f_14", 0x3c1f4);
add_routine("b0f_15", 0x3c20b);
add_routine("b0f_16", 0x3c219);
add_routine("b0f_17", 0x3c235);
add_routine("b0f_18", 0x3c24d);

source = "resource/fe.nes";
rot = "b0f_18";

#output_asm(source, routines[rot]);
#print_assembled("asm/bank_0f");

#output_code(source, 0xf, vanilla.code_0f);
#output_code(source, 0xf, vanilla.code_0f_end, "tmp");

#get_labels("asm/bank_0f/asm_0f");

def dump_to_range(bank, arg_freespaces):
    tmp_blist = [];
    for key in bank:
        bytelist = bank[key];
'''









                    