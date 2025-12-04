maph_misc = dict();
#(Pointer Address, Count, End Byte(s), Fix Length?)
maph_misc["bonus_damage"] = ("bytes", 0x3D947, 0xc, 0xff, -1);
maph_misc["dct1"] = ("normal", 0x3deb0, 0x7f, 0xef, -1);
maph_misc["names_classes"] = ("names", 0x3da2f, 0x17, 0xef, -1);
maph_misc["names_items"] = ("names", 0x3dae5, 0x5b, 0xef, -1);
maph_misc["names_units"] = ("names", 0x3DE3B, 0x34, 0xef, -1);
maph_misc["names_enemies"] = ("names", 0x3DFB4, 0x44, 0xef, -1);
maph_misc["growths"] = ("sandwiches", 0x3E1F0, 0x34, -1, -1);
maph_misc["names_terrain"] = ("names", 0x3E601, 0xf, 0xef, -1);
maph_misc["bases"] = ("sandwiches", 0x3EC14, 24, 0xed, -1);
maph_misc["names_locations"] = ("names", 0x3EFC7, 0x18, 0xed, -1);
maph_misc["names_chapters"] = ("names", 0x3EE18, 24, 0xed, -1);
#Bank 0f

freebank = [];
freebank.append((0x3da5f, 0x3dae4));
freebank.append((0x3dba0, 0x3de36));
freebank.append((0x3e03e, 0x3e1ef)); #Enemy names
freebank.append((0x3E25A, 0x3E3BE)); #Growth rates
freebank.append((0x3e621, 0x3e66b)); #Terrain names
freebank.append((0x3EC40, 0x3ED05)); #Class bases
freebank.append((0x3ee4b, 0x3efc6)); 
freebank.append((0x3effa, 0x3f0ad));
freebank.append((0x3f351, 0x3f80f));
freebank.append((0x3f990, 0x3fa7d));
maph_misc["free"] = freebank;
maph_misc["offset"] = (-0x30000, 0x0);

maph_8 = dict();
maph_8["units"] = ("struct_plr", 0x204A0, 0x18, 0x1b);
maph_8["enemies"] = ("struct_enm", 0x20AB3, 0x18, 0xb);
maph_8["scr_intros"] = ("script", 0x21F3B, 50)
maph_8["spawns"] = ("spawns", 0x207A0, 0x18);
freebank_struct = [];
freebank_struct.append((0x204D2, 0x2079F));
freebank_struct.append((0x207D2, 0x20AB2));
freebank_struct.append((0x20AE5, 0x21F3A));
freebank_struct.append((0x21FA1, 0x23A89));
freebank_struct.append((0x23C91, 0x23FAF));
maph_8["free"] = freebank_struct;
maph_8["offset"] = (-0x20000, 0x8000);

maph_8_random = dict();
maph_8_random["units"] = ("struct_plr", 0x204A0, 0x18, 0x1b);
maph_8_random["enemies"] = ("struct_enm", 0x20AB3, 0x18, 0xb);
#maph_8_random["scr_intros"] = ("script", 0x21F3B, 50)
maph_8_random["spawns"] = ("spawns", 0x207A0, 0x17);
free8 = [];
free8.append((0x204D2, 0x2079F));
free8.append((0x207D2, 0x20AB2));
free8.append((0x20AE5, 0x21F3A));
free8.append((0x21FA1, 0x23A89));
free8.append((0x23C91, 0x23FAF));
maph_8_random["free"] = free8;
maph_8_random["offset"] = (-0x20000, 0x8000);

maph_bank_0 = dict();
maph_bank_0["dct2"] = ("names", 0x35b0, 0x7f, 0xef, -1);
maph_bank_0["dct_names"] = ("names", 0x36b0, 0x2f, 0xef, -1);
freebank_0 = [];
freebank_0.append((0x3730, 0x3faf));
maph_bank_0["free"] = freebank_0;
maph_bank_0["offset"] = (0x0, 0x8000);

maph_bank_c = {};
maph_bank_c["scr_villages"] = ("script", 0x30010, 93, 0x8000, 0x30000);
freebank_villages = [];
freebank_villages.append((0x300CC, 0x3347E));
freebank_villages.append((0x33824, 0x33978));
freebank_villages.append((0x33D92, 0x33FAF));
maph_bank_c["free"] = freebank_villages;
maph_bank_c["offset"] = (-0x30000, 0x8000);

maph_bank_7 = dict();
maph_bank_7["combat"] = ("names", 0x1c2fd, 21, 0xef, -1, 0x4000, 0x10000);
maph_bank_7["scr_recruits"] = ("script", 0x1c863, 108, 0x4000, 0x10000);
freebank_7 = [];
freebank_7.append((0x1c329, 0x1c433)); #Combat messages
freebank_7.append((0x1c520, 0x1c85f));
freebank_7.append((0x1c93d, 0x1ea33));
freebank_7.append((0x1ee40, 0x1ffff));
maph_bank_7["free"] = freebank_7;
maph_bank_7["offset"] = (-0x10000, -0x4000);


maph_bank_b = dict();
maph_bank_b["btl_cmds"] = ("names", 0x2c1b5, 0, 0xef, -1, 0x4000, 0x20000);
maph_bank_b["preparations"] = ("names",0x2C201, 0, 0xef, -1, 0x4000, 0x20000);
maph_bank_b["menus"] = ("names", 0x2CFD2, 71, (0xed, 0xef), -1,  0x4000, 0x20000);
maph_bank_b["shops"] = ("bytes", 0x2E50F, 24, 0xf0, -1, 0x4000, 0x20000);
maph_bank_b["shop_inv"] = ("bytes", 0x2E6D2, 0x13, 0xf0, -1, 0x4000, 0x20000);
maph_bank_b["offset"] = (-0x20000, -0x4000);

maph_bank_b["scr_victory_defeat"] = ("script", 0x2dd95, 10, -0x4000, 0x20000);
maph_bank_b["scr_shops_items"] = ("script", 0x2E776, 87, -0x4000, 0x20000);
freebank_b = [];
freebank_b.append((0x2C1C2, 0x2C1EA)); #System menu
freebank_b.append((0x2C20E, 0x2C27B)); #Battle preps
freebank_b.append((0x2D062, 0x2D260)); #Menu stuff
freebank_b.append((0x2DDAB, 0x2DE6B)); #Outros
freebank_b.append((0x2E111, 0x2E290)); #Game over
freebank_b.append((0x2E541, 0x2E6D1)); #Shop locations
freebank_b.append((0x2E6FA, 0x2E775)); #Shop inventory
freebank_b.append((0x2E826, 0x2F048)); #Shops/item usage
freebank_b.append((0x2F43C, 0x2F484)); #Unused
freebank_b.append((0x2F485, 0x2F6DF)); #Unused
freebank_b.append((0x2F6E0, 0x2FFAF)); #Free
maph_bank_b["free"] = freebank_b;
maph_bank_b["offset"] = (-0x20000, -0x4000);


maph_menus = {};
maph_menus["menus"] = ("names", 0x2CFD2, 72, 0x4000, 0x20000);
maph_menus["offset"] = (-0x20000, -0x4000);

maph_bank_3 = dict();
#data_bank_3["houses"] = (0xE477, 50, -0x4000, 0x0);
maph_bank_3["scr_houses"] = ("script", 0xE477, 0x31, -0x4000, 0x0);
freebank_3 = [];
freebank_3.append((0xe4db, 0xf6df));
freebank_3.append((0xf6e0, 0xffaf));
maph_bank_3["free"] = freebank_3;
maph_bank_3["offset"] = (0x0, -0x4000);

maph_bank_3_other = dict();
maph_bank_3_other["village_recruits"] = ("struct_plr", 0xD476, 0x18, 0x1b);
maph_bank_3_other["reinforcements"] = ("struct_enm", 0xD5AC, 0x18, 0xb);
maph_bank_3_other["events"] = ("events", 0xE101, 0x18, 0x05);
freebank_3_other = [];
freebank_3_other.append((0xD4A8, 0xD5A9));
freebank_3_other.append((0xD5DE, 0xD9F4));
freebank_3_other.append((0xE133, 0xE3E9));
maph_bank_3_other["free"] = freebank_3_other;
maph_bank_3_other["offset"] = (-0x0000, -0x4000);

maph_bank_4 = dict();
maph_bank_4["scr_btl"] = ("script", 0x1046b, 64, 0x8000, 0x10000);
maph_bank_4["scr_epilogue"] = ("script", 0x12DFD, 0x41, 0x8000, 0x10000);
freebank_4 = [];
freebank_4.append((0x104ED, 0x1097C));
freebank_4.append((0x12E81, 0x1397B));
freebank_4.append((0x13D92, 0x13faf));
maph_bank_4["free"] = freebank_4;
maph_bank_4["offset"] = (-0x10000, 0x8000);

maph_bank_d = dict();
maph_bank_d["intro_names"] = ("names", 0x34CA8, 0x15, 0xed, -1, -0x4000, 0x30000);
maph_bank_d["intro_desc"] = ("names", 0x34DDC, 0x15, 0xef, -1, -0x4000, 0x30000);
freebank_d = [];
freebank_d.append((0x34CD4, 0x34DDB));
freebank_d.append((0x34E08, 0x353ED));
freebank_d.append((0x37e50, 0x37fae));
maph_bank_d["free"] = freebank_d;
maph_bank_d["offset"] = (-0x30000, 0x4000);


dct_pos = 0x3deb0;
dct_ptr = [];
dct_count = 0x7f;
dct = dict();

ptrs = [];

data = [];

#freebank.append((0x3fd70, 0x3fee0));

freebank_maps = [];
freebank_maps.append((0x802a, 0xa65d));
freebank_maps.append((0xabeb, 0xbf9f));

freebank_maps2 = [];
freebank_maps2.append((0x24028, 0x26b77));
freebank_maps2.append((0x27D70, 0x27f9f));

space_units = [];
space_units.append((0x204d2, 0x2079f));

item_keys = ("might", "wlevel", "weight", "hit", "crit", "price", "uses", "bonus", "effect", "range", "type");
item_starts = {};
item_starts["might"] = 0x3d667;
item_starts["wlevel"] = 0x3D6C3;
item_starts["weight"] = 0x3D71F;
item_starts["hit"] = 0x3D77B;
item_starts["crit"] = 0x3D7D7;
item_starts["price"] = 0x3D833;
item_starts["uses"] = 0x3D88F;
item_starts["bonus"] = 0x3D8EB;
item_starts["effect"] = 0x3D977;
item_starts["range"] = 0x3D9D3;
item_starts["type"] = 0x3fe69;

maph_promotes = (0x3ff40, 0x3ff60);
maph_intro_config = 0xE0CF;

maph_recruits = (0x3edc5, 0x3edd4, 0x3ede2, 0x3edf0);