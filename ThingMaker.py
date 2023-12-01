NAME = 0x0;
CLASS = 0x1;
LEVEL = 0x2;
HP = 0x3; MAX_HP = 0x4;
EXP = 0x5;
TILE = 0x6;
STR = 0x7; SKL = 0x8;
WLV = 0x9; SPD = 0xa;
LCK = 0xb; DEF = 0xc;
MOV = 0xd; VIS = 0xe;
RES = 0xf;
START_Y = 0x10;
START_X = 0x11;
MOVED = 0x12;
ITEM1 = 0x13; ITEM2 = 0x14;
ITEM3 = 0x15; ITEM4 = 0x16;
ITEM1_USES = 0x17; ITEM2_USES = 0x18;
ITEM3_USES = 0x19; ITEM4_USES = 0x1a;

E_NAME = 0x0; E_CLASS = 0x1; E_LEVEL = 0x2;
E_WEAPON = 0x3; E_DROP = 0x4; E_X = 0x5; E_Y = 0x6;
E_AI = 0x7; E_UNKNOWN = 0x8; E_DEST_X = 0x9; E_DEST_Y = 0xa;

CLASS_SOCIAL = 0x1; CLASS_ARMOR = 0x2;
CLASS_PEGASUS = 0x3; CLASS_PALADIN = 0x4;
CLASS_DRAGON = 0x5; CLASS_MERCENARY = 0x6;
CLASS_FIGHTER = 0x7; CLASS_PIRATE = 0x8;
CLASS_THIEF = 0x9; CLASS_HERO = 0xa;
CLASS_ARCHER = 0xb; CLASS_HUNTER = 0xc;
CLASS_SHOOTER = 0xd; CLASS_HORSEMAN = 0xe;
CLASS_SNIPER = 0xf; CLASS_COMMANDO = 0x10;
CLASS_MAMKUTE = 0x11; CLASS_MAGE = 0x12;
CLASS_CLERIC = 0x13; CLASS_BISHOP = 0x14;
CLASS_LORD = 0x15; CLASS_GENERAL = 0x16;


AI_GUARD = 0x1d;
AI_THIEF = 0x38;
AI_APPROACH_ATTACK = 0x15;
AI_FOLLOW_MARS = 0x4;
AI_GUARD_POS = 0x3d;
AI_CHARGE = 0x35;
AI_HEALER = 0x2e;
AI_CUDDLE = 0x50;


def hex_format(arg_val):
    tmp_byteval = "";
    if (arg_val < 0x10):
        tmp_byteval = "0";
    tmp = str(hex(arg_val));
    tmp_byteval = tmp_byteval + tmp[2:len(tmp)];
    return tmp_byteval.lower();

def define_unit(arg_head, arg_stats, arg_items):
    unit = dict();
    unit[NAME] = arg_head[0];
    unit[CLASS] = arg_head[1];
    unit[LEVEL] = arg_head[2];
    unit[HP] = arg_stats[0]; unit[MAX_HP] = unit[HP];
    unit[EXP] = arg_head[3];
    unit[TILE] = 0x0;
    unit[STR] = arg_stats[1]; unit[SKL] = arg_stats[2];
    unit[WLV] = arg_stats[3]; unit[SPD] = arg_stats[4];
    unit[LCK] = arg_stats[5]; unit[DEF] = arg_stats[6];
    unit[MOV] = arg_stats[7]; unit[VIS] = 0x0;
    tmp_res = arg_stats[8];
    if tmp_res > 0:
        tmp_res += 0x80;
    unit[RES] = tmp_res;
    unit[START_Y] = arg_head[4];
    unit[START_X] = arg_head[5];
    unit[MOVED] = 0x0;
    unit[ITEM1] = arg_items[0][0];
    unit[ITEM2] = arg_items[1][0];
    unit[ITEM3] = arg_items[2][0];
    unit[ITEM4] = arg_items[3][0];
    
    unit[ITEM1_USES] = arg_items[0][1];
    unit[ITEM2_USES] = arg_items[1][1];
    unit[ITEM3_USES] = arg_items[2][1];
    unit[ITEM4_USES] = arg_items[3][1];
    return unit.copy();


#(Name, Class, Level, Weapon, Drop, Y, X, AI, ?, Dest_Y, Dest_X)
def define_enemy(arg_name, arg_class, arg_level, arg_weapon, arg_drop, arg_pos, arg_ai, arg_dest=(0, 0)):
    enemy = dict();
    enemy[E_NAME] = arg_name + 0x81;
    enemy[E_CLASS] = arg_class; enemy[E_LEVEL] = arg_level;
    enemy[E_WEAPON] = arg_weapon; enemy[E_DROP] = arg_drop;
    enemy[E_Y] = arg_pos[0]; enemy[E_X] = arg_pos[1];
    enemy[E_AI] = arg_ai;
    enemy[E_UNKNOWN] = 0x0;
    enemy[E_DEST_Y] = arg_dest[0]; enemy[E_DEST_X] = arg_dest[1];
    return enemy;

def make_unit(arg_unit):
    tmp_str = "";
    for stat in arg_unit:
        tmp_str += hex_format(arg_unit[stat]);
    print(tmp_str);
    
def make_chapter(arg):
    for i in arg:
        make_unit(i);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
elice_head = (0x12, CLASS_LORD, 12, 0, 0x18, 0x10);
elice_stats = (24, 12, 9, 10, 14, 7, 8, 7, 5);
elice_items = ((0x1, 20), (0x9, 20), (0x40, 3), (0x0, 0));
elice = define_unit(elice_head, elice_stats, elice_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
cuan_head = (0x18, CLASS_PALADIN, 14, 0, 0xf, 0xb);
cuan_stats = (32, 16, 20, 18, 13, 9, 17, 8, 8);
cuan_items = ((0x10, 0), (0xf, 0), (0x0, 0), (0x0, 0));
cuan= define_unit(cuan_head, cuan_stats, cuan_items);

ethlin_head = (0x19, CLASS_CLERIC, 14, 0, 0xf, 0xc);
ethlin_stats = (35, 8, 20, 19, 8, 18, 12, 9, 18);
ethlin_items = ((0x37, 0), (0x3c, 0), (0x0, 0), (0x0, 0));
ethlin = define_unit(ethlin_head, ethlin_stats, ethlin_items);

sigurd_head = (0x1a, CLASS_PALADIN, 18, 50, 0x1, 0x7);
sigurd_stats = (40, 26, 14, 20, 18, 2, 18, 8, 0);
sigurd_items = ((0x8, 0), (0x2a, 0), (0x0, 0), (0x0, 0));
sigurd = define_unit(sigurd_head, sigurd_stats, sigurd_items);

dean_head = (0x11, CLASS_DRAGON, 3, 0, 0x15, 0x10);
dean_stats = (26, 12, 10, 12, 16, 6, 12, 9, 2);
dean_items = ((0x18, 60), (0xd, 14), (0x40, 3), (0x0, 0));
dean = define_unit(dean_head, dean_stats, dean_items);


#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
kirby_head = (0x1, CLASS_COMMANDO, 1, 0, 0x6, 0x19);
kirby_stats = (25, 7, 9, 6, 7, 7, 5, 7, 5);
kirby_items = ((0x26, 255), (0x40, 1), (0x0, 0), (0x0, 0));
kirby = define_unit(kirby_head, kirby_stats, kirby_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
new_samto_head = (0x5, CLASS_MAGE, 1, 0, 0x2, 0xf);
new_samto_stats = (21, 3, 9, 8, 7, 9, 5, 7, 5);
new_samto_items = ((0x2b, 40), (0x33, 10), (0x0, 0), (0x0, 0));
new_samto = define_unit(new_samto_head, new_samto_stats, new_samto_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
glade_x_head = (0xa, CLASS_PEGASUS, 1, 0, 0x6, 0x16);
glade_x_stats = (25, 7, 9, 10, 9, 0, 8, 10, 7);
glade_x_items = ((0x8, 60), (0x18, 60), (0x2, 99), (0x28, 255));
glade_x = define_unit(glade_x_head, glade_x_stats, glade_x_items);



#(Name, Class, Level, Weapon, Drop, X, Y, AI, ?, Dest_Y, Dest_X)
'''
ch1 = [];
ch1_boss = define_enemy(0x0, CLASS_HUNTER, 2, 0x11, 0x0, (2, 10), AI_GUARD, (2, 10)); ch1.append(ch1_boss);
ch1_e1 = define_enemy(0x0, CLASS_THIEF, 1, 0x2, 0x40, (3, 18), AI_CHARGE); ch1.append(ch1_e1);
ch1_e2 = define_enemy(0x0, CLASS_FIGHTER, 1, 0x1b, 0x0, (5, 17), AI_CHARGE); ch1.append(ch1_e2);
ch1_e3 = define_enemy(0x0, CLASS_PIRATE, 1, 0x1b, 0x0, (5, 12), AI_CHARGE); ch1.append(ch1_e3);
ch1_e4 = define_enemy(0x0, CLASS_ARCHER, 1, 0x11, 0x0, (3, 9), AI_GUARD, (3, 9)); ch1.append(ch1_e4);
ch2 = [];
'''
#make_unit(cuan);
#make_unit(ethlin);
#make_unit(sigurd);

#make_unit(dean);

#make_unit(kirby);
#make_unit(new_samto);
make_unit(glade_x);
        
