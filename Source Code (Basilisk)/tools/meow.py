from tools.gen import hex_format, hex_format2, convert_ptrstr;
from tools import extracter as ex;
from tools.maph import *;


global errors;

def dump(arg_project, arg_data, arg_seed="", arg_name=""):
    if (arg_seed != ""):
        dump_rom = "rand/output/FE1 - " + arg_seed + ".nes";
    else:
        dump_rom = arg_project + "/" + arg_name + ".nes";
    data = arg_data;
    global errors;
    errors = 0;
    
    maps1 = data["maps1"];
    maps2 = data["maps2"];
    for key in maps1:
        maps1[key] = ex.compress_map(maps1[key]);
    for key in maps2:
        maps2[key] = ex.compress_map(maps2[key]);
    
    added_dct = {};
    
    def dump_data(arg_name, arg_maph):
        global errors;
        tmp_data = [];
        print("\n - " + arg_name + " - ");
        tmp_added = added_dct.copy();
        for key in arg_maph:
            if (key != "free") and (key != "offset"):
                #tmp = tools.input_from_file("dictionary", tbl, 0xef, 8);
                tmp_data.append(data[key]);
            

        tmp_ptrs = [];
        for key in arg_maph:
            if (key != "free") and (key != "offset"):
                tmp_ptrs.append(arg_maph[key][1]);
            
        
        tmp_free = arg_maph["free"];
        offsets = arg_maph["offset"];
    
        dump_space = freebank.copy();
        result = dump_to_rom(dump_rom, tmp_data, tmp_free, tmp_ptrs, offsets[0], offsets[1], tmp_added);
        if not (result):
            errors += 1;
        return tmp_added;
    
    if (arg_seed != ""):
        added = {};
        dump_data("Units/Enemies/Spawns", maph_8_random);
    else:
        added = dump_data("Misc", maph_misc);
        dump_data("Units / Enemies / Intro", maph_8);
        dump_data("Dictionary #2", maph_bank_0);
        dump_data("Villages / Outros", maph_bank_c);
        dump_data("Combat / Recruiment", maph_bank_7);
        dump_data("Menus / Shops / Item Usage", maph_bank_b);
        dump_data("Houses", maph_bank_3);
        dump_data("Recruits / Reinforcements / Events", maph_bank_3_other);
        dump_data("Endings / Death Quotes", maph_bank_4);
        dump_data("Opening", maph_bank_d);
        
    print("\n* Data Tables *\n");
        
        
    with open(dump_rom, "rb+") as file:
        for key in item_keys:
            tmp_data = data["item_" + key]["00"];
            pos = item_starts[key];
            for i in range(0, len(tmp_data)):
                file.seek(pos);
                file.write(bytes([tmp_data[i]]));
                pos += 1;
            
    print("Updated item data in ROM.");
    
    insert_promotes(dump_rom, data["promotes"]);
    print("Updated promotion data in ROM.");
    
    insert_ports(dump_rom, data["ports"]);
    print("Updated unit portrait index table in ROM.");
    
    insert_recruits(dump_rom, data["recruit"]);
    print("Updated recruitment table in ROM.");
    
    insert_intro_config(dump_rom, data["intro_config"]);
    print("Updated intro config table in ROM.");
    
    print("\n***************\n");
    
    dump_ptrs = [];
    added = added_dct.copy();
    dump_data = [];

    print("Maps (1-13)");
    dump_ptrs = [];
    added = added_dct.copy();
    dump_data = [];
    dump_space = freebank_maps.copy();
    
    dump_ptrs.append(0x8010);
    dump_data.append(data["maps1"]);
    dump_to_rom(dump_rom, dump_data, dump_space, dump_ptrs, 0x0, 0x0, added);
    
    print("Maps (14-25)");
    dump_ptrs = [];
    added = added_dct.copy();
    dump_data = [];
    dump_space = freebank_maps2.copy();
    
    dump_ptrs.append(0x24010);
    dump_data.append(data["maps2"]);
    dump_to_rom(dump_rom, dump_data, dump_space, dump_ptrs, -0x20000, 0x4000, added);
    
    return errors;


def dump_to_rom(arg_rom, arg_data, arg_space, arg_ptrs, offset=0x0, offset2=0x0, added=False):
    ext = False;
    
    with open(arg_rom, "rb") as file:
        content = list(file.read());
    file = content;
        
    space_index = 0;
    ptrs_index = 0;
    tmp_pos = 0;
    
    ptr_pos = -1;
    ptr_value = 0;
    space_pos = arg_space[space_index][0];
    tmp_tbl = ex.load_tbl("resource/tbl_eng");
    
    tmp_unique = {};
    
    tmp_size_data = 0x0;
    for bank in arg_data:
        for key in bank:
            lst = bank[key];
            key2 = str(lst);
            if not (key2 in tmp_unique):
                tmp_unique[key2] = lst;
                tmp_size_data += len(lst);
            
    tmp_size_free = 0x0;
    for tmp_space in arg_space:
        tmp_size_free += tmp_space[1] - tmp_space[0];
        
    file_pos = 0x0;
    
    #print("Data Size:  " + str(tmp_size_data));
    #print("Free Space: " + str(tmp_size_free));
    
    print("Free Space Remaining: " + str(tmp_size_free - tmp_size_data) + " bytes.");
        
    
    bank_index = 0;
    
    for bank in arg_data:
        bank_index += 1;
        ptr_pos = arg_ptrs[ptrs_index];
        ptrs_index += 1;
        file_pos = ptr_pos;
        start = 0;
        for index in range(0, 0xff):
            tmp = hex_format(index);
            if tmp in bank:
                entry = bank[hex_format(index)];
                
                #Find space for entry.
                #print(space_index);
                
                if (added) and (entry in added.values()):
                    for tmp_key in added:
                        if added[tmp_key] == entry:
                            #print(ex.tableize(entry, tmp_tbl));
                            ptr_value = tmp_key;
                            ptr_str = hex_format2(ptr_value);
                            
                            val1 = int(ptr_str[0:2], 16);
                            file[ptr_pos] = val1;
                            #file.write(bytes([val1]));
                            ptr_pos += 1;
                            
                            #file.seek(ptr_pos);
                            val1 = int(ptr_str[2:4], 16);
                            file[ptr_pos] = val1;
                            #file.write(bytes([val1]));
                            ptr_pos += 1;
                            break;
                else:
                    if (space_index > (len(arg_space) + 1)):
                        print("Error! Out of space. (1)");
                        return False;
                        ext = True;
                    while ((space_pos + len(entry)) > (arg_space[space_index][1] + 1)):
                        #print(len(entry));
                        #print(hex(space_pos));
                        space_index += 1;
                        if (space_index == (len(arg_space))):
                            print("#: " + tmp + " in " + str(bank_index));
                            print(ex.tableize(entry, tmp_tbl));
                            print("Error! Out of space. (2)");
                            return False;
                            ext = True;
                            break;
                        space_pos = arg_space[space_index][0];
                    if ext:
                        break;
                    #Write the pointer
                    ptr_value = convert_ptrstr(hex_format2(space_pos + offset + offset2), 'stored');
                    added[ptr_value] = entry;
                    file_pos = ptr_pos;
                    ptr_str = hex_format2(ptr_value);
                    
                    val1 = int(ptr_str[0:2], 16);
                    #print(val1);
                    file[file_pos] = val1;
                    
                    file_pos += 1;
                    
                    val1 = int(ptr_str[2:4], 16);
                    file[file_pos] = val1;
                    ptr_pos += 0x02;
                
                    #Write the entry
                    tmp_lst = [];
                    for byte in entry:
                        tmp_lst.append(byte);
                    tmp_len = len(tmp_lst);
                        
                    #file.seek(space_pos);
                    #file.write(bytes(tmp_lst));
                    
                    file[space_pos:space_pos+tmp_len] = tmp_lst;
                    
                    space_pos += tmp_len;
        if ext:
            break;
    with open(arg_rom, "rb+") as f:
        f.write(bytes(file));
    return True;
    print("ROM sucessfully modified.");
    
def insert_promotes(arg_rom, arg_prm):
    with open(arg_rom, "rb+") as file:
        for i in range(2):
            file.seek(maph_promotes[i]);
            file.write(bytes(arg_prm[i]));
    return True;

def insert_ports(arg_rom, arg_ports):
    pos = 0x2BD80;
    with open(arg_rom, "rb+") as file:
        rom = list(file.read());
    for port in arg_ports:
        rom[pos] = port;
        pos += 1;
    with open(arg_rom, "rb+") as file:
        rom = bytes(rom);
        file.write(rom);
    return True;
    
def insert_recruits(arg_rom, arg_recs):
    tmp_maphs = maph_recruits;
    with open(arg_rom, "rb+") as file:
        rom = list(file.read());
    pos = 0;
    for i in range(4):
        pos = tmp_maphs[i];
        tmp_recs = arg_recs[i];
        for tmp_rec in tmp_recs:
            rom[pos] = tmp_rec;
            pos += 1;
    with open(arg_rom, "rb+") as file:
        rom = bytes(rom);
        file.write(rom);
    return True;

def insert_intro_config(arg_rom, arg_lst):
    with open(arg_rom, "rb+") as file:
        rom = list(file.read());
    pos = maph_intro_config;
    for tmp_byte in arg_lst:
        rom[pos] = tmp_byte;
        pos += 1;
    with open(arg_rom, "rb+") as file:
        rom = bytes(rom);
        file.write(rom);
    return True;
    

        