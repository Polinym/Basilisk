from os.path import exists as path_exists, join as path_join
from os import makedirs;
from tools import extracter as ex;
from tools import gen;
from tools.meow import dump;
import datetime;

def get_current_time():
    tmp_now = datetime.datetime.now();
    return tmp_now.strftime("%I:%M %p")

def include_dir(arg_project, arg_dir):
    if not path_exists(path_join(arg_project + "\\" + arg_dir)):
        makedirs(path_join(arg_project + "\\" + arg_dir));
        
convert_ptrstr = gen.convert_ptrstr
hex_format = gen.hex_format;
hex_format2 = gen.hex_format2;

def iff(arg_project, arg_tbl, arg_pathname, arg_terminator, arg_dct={}):
    return ex.input_from_file(arg_project, arg_pathname, arg_tbl, arg_terminator, -1, arg_dct);

def load_data(arg_project):
    all_data = {};
    tmp_tbl = ex.load_tbl(arg_project + "/tbl_eng");
    tmp_tbl_hex = ex.blank_tbl();
    tmp_dct_names = ex.load_dct_names(arg_project);
    
    all_data["tbl"] = tmp_tbl;
    all_data["tbl_hex"] = tmp_tbl_hex;
    '''Misc Text'''
    all_data["dct1"] = ex.input_from_file(arg_project, "/text/dictionary/dictionary", tmp_tbl, 0xef, -1);
    all_data["dct2"] = ex.input_from_file(arg_project, "/text/dictionary/dictionary2", tmp_tbl, 0xef, -1);
    all_data["dct_names"]  = ex.input_from_file(arg_project,"/text/dictionary/dictionary_names", tmp_tbl, 0xef, -1);
    
    
    all_data["names_chapters"] = iff(arg_project, tmp_tbl, "/text/names/chapters", 0xed, tmp_dct_names);
    all_data["names_classes"] = iff(arg_project, tmp_tbl, "/text/names/classes", 0xef, tmp_dct_names);
    all_data["names_enemies"] = iff(arg_project, tmp_tbl, "/text/names/enemy", 0xef, tmp_dct_names);
    all_data["names_locations"] = iff(arg_project, tmp_tbl, "/text/names/location", 0xed, tmp_dct_names);
    all_data["names_terrain"] = iff(arg_project, tmp_tbl, "/text/names/terrain", 0xef, tmp_dct_names);
    all_data["names_units"] = iff(arg_project, tmp_tbl, "/text/names/names", 0xef, tmp_dct_names);
        
    
    all_data["names_items"]  = iff(arg_project, tmp_tbl, "/text/names/items", 0xef, tmp_dct_names);
    all_data["promotes"] = ex.input_promotes(arg_project);
    
    '''Unit Data'''
    all_data["units"]  = ex.struct_make_bank(arg_project, "units");
    all_data["enemies"]  = ex.struct_make_bank(arg_project, "enemies");
    all_data["spawns"]  = ex.input_spawns(arg_project);
    all_data["village_recruits"]  = ex.struct_make_bank(arg_project, "village_recruits");
    all_data["reinforcements"]  = ex.struct_make_bank(arg_project, "reinforcements");
    
    
    all_data["growths"]  = ex.input_growths(arg_project);
    all_data["bases"]  = ex.input_bases(arg_project);
    all_data["ports"] = ex.input_ports(arg_project);
    all_data["recruit"] = ex.input_recruits(arg_project);
    all_data["intro_config"] = ex.input_intro_config(arg_project);
    
    data_item_stats = ex.input_itemdata(arg_project);
    for key in data_item_stats:
        bytelst = data_item_stats[key];
        new_key = "item_" + key.lower();
        new_dct = {};
        new_dct["00"] = bytelst;
        all_data[new_key] = new_dct;
    
    
    all_data["bonus_damage"] = iff(arg_project, tmp_tbl, "/gameplay/items/bonus_damage", 0xff);
    
    '''Maps and Events'''
    all_data["shops"] = ex.input_shoploc(arg_project);
    all_data["events"] = ex.input_events(arg_project);
    all_data["maps"] = ex.input_maps(arg_project);
    maps1 = {};
    maps2 = {};

    tmp_i = 0;
    maps = all_data["maps"];
    for i in range(13):
        maps1[hex_format(i)] = maps[hex_format(tmp_i)];
        tmp_i += 1;
    for i in range(12):
        maps2[hex_format(i)] = maps[hex_format(tmp_i)];
        tmp_i += 1;
        
    all_data["maps1"] = maps1;
    all_data["maps2"] = maps2;
    
    '''Introduction'''
    all_data["intro_desc"] = ex.input_from_file(arg_project, "/text/intro/intro_desc", tmp_tbl, 0xef, -1);
    all_data["intro_names"] = ex.input_from_file(arg_project, "/text/intro/intro_names", tmp_tbl, 0xed, -1);
    
    '''Menu Systems'''
    all_data["menus"] = ex.input_from_file(arg_project, "/text/menus/menus", tmp_tbl, 0xef, -1, tmp_dct_names);
    all_data["btl_cmds"] = ex.input_from_file(arg_project, "/text/menus/btl_cmds", tmp_tbl, 0xef);
    all_data["preparations"] = ex.input_from_file(arg_project, "/text/menus/preparations", tmp_tbl, 0xef);
    all_data["shop_inv"] = ex.input_from_file(arg_project, "/gameplay/shops_inv", tmp_tbl_hex, 0xf0);
    all_data["combat"] = ex.input_from_file(arg_project, "/text/menus/combat", tmp_tbl, 0xef);
    
    '''Game Script'''
    all_data["scr_intros"] = ex.input_script(arg_project, "intros", tmp_tbl, 0x80);
    all_data["scr_villages"] = ex.input_script(arg_project, "outros_and_villages", tmp_tbl, 0xc0);
    all_data["scr_recruits"] = ex.input_script(arg_project, "recruit", tmp_tbl, 0x71);
    all_data["scr_shops_items"] = ex.input_script(arg_project, "shops_items", tmp_tbl, 0xb1);
    all_data["scr_victory_defeat"] = ex.input_script(arg_project, "victory_defeat", tmp_tbl, 0xb1);
    all_data["scr_houses"] = ex.input_script(arg_project, "houses", tmp_tbl, 0xb1);
    all_data["scr_btl"] = ex.input_script(arg_project, "btl", tmp_tbl, 0xb1, False);
    all_data["scr_epilogue"] = ex.input_script(arg_project, "epilogue", tmp_tbl, 0x40);
    return all_data;

def compile_project(arg_project, arg_name):
    tmp_path = arg_project;
    #copy("resource/fe1.nes", tmp_path + "/" + arg_project + ".nes");
    data = load_data(tmp_path);
    errors = dump(arg_project, data, "", arg_name);
    print("Project \"" + arg_project + "\"\ncompiled at " + get_current_time());
    if (errors > 0):
        print("*** WARNING! ***");
        print("Freespace Errors: " + str(errors));
        print("See log ^");
'''
def compile_random(arg_seed):
    if (arg_seed != ""):
        seed = arg_seed;
    else:
        seed = random_seedname();
    data = generate({}, seed);
    copy("resource/fe1.nes", "rand/output/FE1 - " + seed + ".nes");
    dump("random", data, seed);
    print("Created random FE1 ROM '" + seed + "'!");
'''