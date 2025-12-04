#This file is for making player and enemy units via code.
#It's essentially a bunch of macros for generating a list of bytes.
#It contains many examples from my own FE1 hack, Time For Tom.



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

def define_enemy2(arg_name, arg_class, arg_level, arg_weapon, arg_drop, arg_pos, arg_ai, arg_dest=(0, 0)):
    enemy = dict();
    enemy[E_NAME] = arg_name;
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
thomas_head = (0x1, CLASS_ARCHER, 2, 10, 20, 10);
thomas_stats = (20, 7, 6, 9, 5, 4, 6, 6, 0);
thomas_items = ((0x5, 0), (0x13, 0), (0x40, 0), (0x0, 0));
thomas = define_unit(thomas_head, thomas_stats, thomas_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
jake_head = (0x2, CLASS_SHOOTER, 1, 20, 21, 9);
jake_stats = (20, 5, 1, 8, 3, 3, 10, 6, 0);
jake_items = ((0x17, 0), (0x19, 0), (0x0, 0), (0x0, 0));
jake = define_unit(jake_head, jake_stats, jake_items);

roger_head = (0x4, CLASS_ARMOR, 5, 0, 18, 5);
roger_stats = (22, 7, 5, 6, 5, 2, 13, 5, 0);
roger_items = ((0xc, 38), (0, 0), (0, 0), (0, 0));
roger = define_unit(roger_head, roger_stats, roger_items);

morodof_head = (0x3, CLASS_BISHOP, 3, 0, 13, 20);
morodof_stats = (16, 3, 5, 4, 4, 5, 6, 6, 3);
morodof_items = ((0x36, 20), (0, 0), (0, 0), (0, 0));
morodof = define_unit(morodof_head, morodof_stats, morodof_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
delmud_head = (0x1e, CLASS_SOCIAL, 4, 0, 13, 10);
delmud_stats = (20, 8, 6, 8, 6, 5, 6, 9, 7);
delmud_items = ((0x9, 60), (2, 42), (0, 0), (0, 0));
delmud = define_unit(delmud_head, delmud_stats, delmud_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
fin_head = (0x8, CLASS_SOCIAL, 10, 0, 4, 6);
fin_stats = (28, 11, 8, 10, 9, 2, 8, 9, 3);
fin_items = ((0xe, 0), (3, 0), (0, 0), (0, 0));
fin = define_unit(fin_head, fin_stats, fin_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
cain_head = (0xb, CLASS_SOCIAL, 6, 0, 3, 6);
cain_stats = (25, 12, 6, 9, 6, 1, 7, 9, 0);
cain_items = ((0x3, 0), (0xf, 0), (0, 0), (0, 0));
cain = define_unit(cain_head, cain_stats, cain_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
selfina_head = (0x9, CLASS_HORSEMAN, 6, 0, 9, 17);
selfina_stats = (22, 7, 12, 9, 12, 6, 6, 8, 3);
selfina_items = ((0x12, 0), (0x27, 0), (0x0, 0), (0, 0));
selfina = define_unit(selfina_head, selfina_stats, selfina_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
glade_head = (0xa, CLASS_SOCIAL, 5, 0, 3, 1);
glade_stats = (21, 8, 10, 12, 7, 0, 7, 9, 7);
glade_items = ((0xc, 0), (0xf, 0), (0, 0), (0, 0));
glade = define_unit(glade_head, glade_stats, glade_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
alba_head = (0xc, CLASS_SOCIAL, 5, 0, 3, 5);
alba_stats = (26, 9, 10, 9, 9, 2, 9, 9, 0);
alba_items = ((0x20, 0), (0xf, 0), (0, 0), (0, 0));
alba = define_unit(alba_head, alba_stats, alba_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
robert_head = (0xd, CLASS_HORSEMAN, 6, 0, 3, 4);
robert_stats = (24, 9, 12, 10, 10, 5, 7, 8, 3);
robert_items = ((0x14, 0), (0x13, 0), (0, 0), (0, 0));
robert = define_unit(robert_head, robert_stats, robert_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
claude_head = (0xf, CLASS_CLERIC, 10, 0, 0x19, 0xe);
claude_stats = (25, 1, 4, 15, 10, 9, 9, 6, 15);
claude_items = ((0x38, 0), (0x3e, 0), (0, 0), (0, 0));
claude = define_unit(claude_head, claude_stats, claude_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
mable_head = (0x13, CLASS_PEGASUS, 3, 0, 0x13, 0xe);
mable_stats = (20, 10, 12, 7, 15, 11, 7, 9, 9);
mable_items = ((0x2a, 40), (0xf, 30), (0x40, 7), (0, 0));
mable = define_unit(mable_head, mable_stats, mable_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
barnef_head = (0x16, CLASS_BISHOP, 15, 50, 0x19, 0xc);
barnef_stats = (30, 10, 9, 18, 9, 2, 12, 6, 20);
barnef_items = ((0x35, 20), (0x38, 25), (0x39, 3), (0x3a, 7));
barnef = define_unit(barnef_head, barnef_stats, barnef_items);

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
thomasplus1_head = (0x1, CLASS_ARCHER, 10, 0, 20, 10);
thomasplus1_stats = (26, 9, 8, 12, 8, 6, 8, 6, 2);
thomasplus1_items = ((0x5, 0), (0x12, 0), (0x40, 0), (0x0, 0));
thomasplus1 = define_unit(thomasplus1_head, thomasplus1_stats, thomasplus1_items);

thomasplus2_head = (0x1, CLASS_SNIPER, 1, 0, 20, 10);
thomasplus2_stats = (30, 11, 10, 15, 9, 7, 9, 7, 4);
thomasplus2_items = ((0x5, 0), (0x14, 0), (0x40, 0), (0x0, 0));
thomasplus2 = define_unit(thomasplus2_head, thomasplus2_stats, thomasplus2_items);

thomasplus3_head = (0x1, CLASS_SNIPER, 10, 0, 20, 10);
thomasplus3_stats = (40, 13, 16, 20, 11, 10, 10, 7, 7);
thomasplus3_items = ((0x15, 0), (0x5, 0), (0x58, 0), (0x0, 0));
thomasplus3 = define_unit(thomasplus3_head, thomasplus3_stats, thomasplus3_items);

#(Name, Class, Level, Exp, Y, X)
#(HP, STR, SKL, WLV, SPD, LCK, DEF, MOV, RES)
#((Item1, uses), (Item2, uses), (Item3, uses), (Item4, uses))
kirby_head = (0x1d, CLASS_COMMANDO, 1, 0, 0x3, 0x1b);
kirby_stats = (30, 10, 14, 15, 15, 20, 8, 7, 15);
kirby_items = ((0x26, 255), (0x0, 0), (0x0, 0), (0x0, 0));
kirby = define_unit(kirby_head, kirby_stats, kirby_items);



#(Name, Class, Level, Weapon, Drop, X, Y, AI, ?, Dest_Y, Dest_X)
ch1 = [];
ch1_boss = define_enemy(0x0, CLASS_HUNTER, 2, 0x11, 0x0, (2, 10), AI_GUARD, (2, 10)); ch1.append(ch1_boss);
ch1_e1 = define_enemy(0x0, CLASS_THIEF, 1, 0x2, 0x40, (3, 18), AI_CHARGE); ch1.append(ch1_e1);
ch1_e2 = define_enemy(0x0, CLASS_FIGHTER, 1, 0x1b, 0x0, (5, 17), AI_CHARGE); ch1.append(ch1_e2);
ch1_e3 = define_enemy(0x0, CLASS_PIRATE, 1, 0x1b, 0x0, (5, 12), AI_CHARGE); ch1.append(ch1_e3);
ch1_e4 = define_enemy(0x0, CLASS_ARCHER, 1, 0x11, 0x0, (3, 9), AI_GUARD, (3, 9)); ch1.append(ch1_e4);

ch1.append(define_enemy2(0x81, CLASS_THIEF, 1, 0x2, 0x0, (0x9, 0xc), AI_CHARGE));
ch1.append(define_enemy2(0x81, CLASS_FIGHTER, 1, 0x1b, 0x0, (0xe, 0x12), AI_GUARD));
ch1.append(define_enemy2(0x81, CLASS_MERCENARY, 1, 0x2, 0x0, (0x8, 0x6), AI_GUARD));

ch2 = [];
def ch2_enemies():
    ch2.append(define_enemy(0x1, CLASS_PIRATE, 3, 0x1f, 0x0, (2, 9), AI_GUARD, (1, 9)));
    ch2.append(define_enemy(0x29, CLASS_THIEF, 4, 0x7, 0x7, (2, 15), AI_CHARGE));
    ch2.append(define_enemy(0x29, CLASS_PIRATE, 1, 0x1b, 0x0, (7, 10), AI_CHARGE));
    ch2.append(define_enemy(0x29, CLASS_HUNTER, 1, 0x11, 0x0, (7, 11), AI_CHARGE));
    ch2.append(define_enemy(0x29, CLASS_PIRATE, 2, 0x1c, 0x0, (8, 12), AI_CHARGE));
    ch2.append(define_enemy(0x29, CLASS_THIEF, 1, 0x2, 0x0, (10, 16), AI_CHARGE));
    ch2.append(define_enemy(0x29, CLASS_THIEF, 1, 0x2, 0x0, (4, 5), AI_CHARGE));
    ch2.append(define_enemy(0x29, CLASS_FIGHTER, 1, 0x1f, 0x0, (3, 9), AI_GUARD, (3, 9)));
    ch2.append(define_enemy(0x29, CLASS_FIGHTER, 1, 0x1b, 0x0, (15, 13), AI_GUARD));
    ch2.append(define_enemy(0x29, CLASS_THIEF, 1, 0x2, 0x4a, (6, 1), AI_GUARD));
    ch2.append(define_enemy(0x2d, CLASS_MERCENARY, 1, 0x4, 0x0, (7, 8), AI_GUARD, (7, 8)));
    ch2.append(define_enemy(0x29, CLASS_HUNTER, 2, 0x13, 0x0, (0x0c, 0x02), AI_CHARGE));
    ch2.append(define_enemy(0x29, CLASS_PIRATE, 1, 0x1b, 0x0, (0x08, 0x04), AI_CHARGE));
    ch2.append(define_enemy(0x29, CLASS_THIEF, 3, 0x2, 0x40, (0x04, 0x0c), AI_CHARGE));
ch2_enemies();

ch3 = [];
def ch3_enemies():
    ch3.append(define_enemy(0x3, CLASS_PALADIN, 1, 0xe, 0xe, (6, 18), AI_GUARD, (6, 18)));
    ch3.append(define_enemy(0x2, CLASS_ARMOR, 1, 0xf, 0x0, (18, 18), AI_GUARD));
    ch3.append(define_enemy(0x2, CLASS_MERCENARY, 1, 0x2, 0x0, (21, 19), AI_GUARD));
    ch3.append(define_enemy(0x2, CLASS_ARCHER, 1, 0x11, 0x0, (13, 18), AI_GUARD));
    ch3.append(define_enemy(0x2, CLASS_ARCHER, 1, 0x11, 0x0, (13, 24), AI_GUARD));
    ch3.append(define_enemy(0x2, CLASS_ARMOR, 1, 0xc, 0x42, (13, 4), AI_GUARD, (13, 4)));
    ch3.append(define_enemy(0x2, CLASS_ARMOR, 1, 0xc, 0x42, (13, 28), AI_GUARD, (13, 28)));
    ch3.append(define_enemy(0x2, CLASS_SOCIAL, 6, 0x25, 0x0, (8, 4), AI_GUARD));
    ch3.append(define_enemy(0x2, CLASS_SOCIAL, 2, 0xc, 0x0, (2, 7), AI_GUARD));
    ch3.append(define_enemy(0x2, CLASS_SOCIAL, 2, 0xc, 0x0, (2, 25), AI_GUARD));
    ch3.append(define_enemy(0x2, CLASS_SOCIAL, 1, 0xf, 0x0, (3, 18), AI_GUARD));
    ch3.append(define_enemy(0x2, CLASS_ARMOR, 2, 0xf, 0x42, (3, 11), AI_GUARD, (3, 11)));
    ch3.append(define_enemy(0x2, CLASS_CLERIC, 1, 0x37, 0x37, (6, 19), AI_HEALER, (6, 19)));
    ch3.append(define_enemy(0x2, CLASS_ARMOR, 1, 0xf, 0x0, (6, 17), AI_GUARD, (6, 17)));
    ch3.append(define_enemy(0x2e, CLASS_THIEF, 3, 0x3, 0x44, (8, 28), AI_GUARD, (6, 17)));
    ch3.append(define_enemy(0x2, CLASS_SOCIAL, 1, 0xc, 0x0, (7, 18), AI_CHARGE));
    ch3.append(define_enemy(0x2, CLASS_MERCENARY, 1, 0x2, 0x42, (0xd, 2), AI_CHARGE));
    ch3.append(define_enemy(0x2, CLASS_MERCENARY, 2, 0x2, 0x42, (0xd, 0x1d), AI_CHARGE));
    ch3.append(define_enemy(0x2, CLASS_HUNTER, 2, 0x11, 0x0, (0x15, 0x1a), AI_GUARD));
    ch3.append(define_enemy(0x2, CLASS_MERCENARY, 1, 0x3, 0x0, (0x16, 0x1b), AI_GUARD));
ch3_enemies();

ch4 = [];
def ch4_enemies():
    ch4.append(define_enemy(0x7, CLASS_MAGE, 6, 0x2c, 0x37, (13, 1), AI_GUARD, (13, 1)));
    ch4.append(define_enemy(0x5, CLASS_MAGE, 3, 0x2b, 0x0, (13, 2), AI_GUARD));
    ch4.append(define_enemy(0x5, CLASS_MAGE, 2, 0x2b, 0x0, (4, 17), AI_CHARGE));
    ch4.append(define_enemy(0x5, CLASS_MAGE, 2, 0x2c, 0x0, (1, 15), AI_CHARGE));
    ch4.append(define_enemy(0x5, CLASS_MAGE, 3, 0x2b, 0x0, (5, 13), AI_CHARGE));
    ch4.append(define_enemy(0x5, CLASS_MAGE, 1, 0x2b, 0x0, (8, 13), AI_CHARGE));
    ch4.append(define_enemy(0x2f, CLASS_SOCIAL, 3, 0x20, 0x0, (4, 9), AI_GUARD));
    ch4.append(define_enemy(0x2f, CLASS_SOCIAL, 2, 0x20, 0x0, (5, 4), AI_GUARD));
    ch4.append(define_enemy(0x2f, CLASS_MERCENARY, 3, 0x3, 0x0, (6, 7), AI_GUARD));
    ch4.append(define_enemy(0x2f, CLASS_HUNTER, 3, 0x12, 0x0, (7, 3), AI_GUARD));
    ch4.append(define_enemy(0x2f, CLASS_HUNTER, 2, 0x13, 0x0, (9, 5), AI_GUARD));
    ch4.append(define_enemy(0x2f, CLASS_MERCENARY, 3, 0x2, 0x0, (9, 1), AI_GUARD));
    ch4.append(define_enemy(0x6, CLASS_MAGE, 4, 0x31, 0x2c, (10, 5), AI_GUARD));
    
    ch4.append(define_enemy(0x2f, CLASS_MERCENARY, 1, 0x3, 0x0, (0x9, 0x4), AI_CHARGE));
    ch4.append(define_enemy(0x5, CLASS_MAGE, 1, 0x2c, 0x0, (0xc, 0x7), AI_CHARGE));
ch4_enemies();

ch5 = [];
def ch5_enemies():
    ch5_boss = define_enemy(0x9, CLASS_DRAGON, 6, 0x25, 0x40, (20, 12), AI_GUARD); ch5.append(ch5_boss);
    ch5.append(define_enemy(0x8, CLASS_DRAGON, 7, 0x25, 0, (19, 13), AI_GUARD));
    ch5.append(define_enemy(0x8, CLASS_DRAGON, 6, 0x25, 0, (19, 11), AI_GUARD));
    ch5.append(define_enemy(0x8, CLASS_DRAGON, 7, 0x25, 0, (21, 13), AI_GUARD));
    ch5.append(define_enemy(0x8, CLASS_DRAGON, 7, 0x25, 0, (21, 11), AI_GUARD));
    
    ch5.append(define_enemy(0x8, CLASS_BISHOP, 7, 0x37, 0, (19, 15), AI_HEALER));
    ch5.append(define_enemy(0x8, CLASS_ARMOR, 8, 0x20, 0, (18, 15), AI_CHARGE));
    ch5.append(define_enemy(0x8, CLASS_ARMOR, 5, 0x20, 0, (18, 16), AI_CHARGE));
    ch5.append(define_enemy(0x8, CLASS_ARMOR, 5, 0x20, 0, (18, 14), AI_CHARGE));
    ch5.append(define_enemy(0x8, CLASS_ARMOR, 6, 0xf, 0, (19, 14), AI_CHARGE));
    ch5.append(define_enemy(0x8, CLASS_ARMOR, 6, 0xf, 0, (19, 16), AI_CHARGE));
    
    ch5.append(define_enemy(0x8, CLASS_ARCHER, 11, 0x11, 0, (20, 8), AI_CHARGE));
    ch5.append(define_enemy(0x8, CLASS_ARCHER, 11, 0x11, 0, (20, 9), AI_CHARGE));
    ch5.append(define_enemy(0x8, CLASS_ARCHER, 11, 0x11, 0, (20, 10), AI_CHARGE));
    ch5.append(define_enemy(0x8, CLASS_ARCHER, 11, 0x11, 0, (21, 9), AI_CHARGE));
    
    ch5.append(define_enemy(0x8, CLASS_ARMOR, 7, 0x20, 0, (22, 7), AI_CHARGE));
    ch5.append(define_enemy(0x8, CLASS_ARMOR, 7, 0x20, 0, (22, 8), AI_CHARGE));
    ch5.append(define_enemy(0x8, CLASS_ARMOR, 6, 0x20, 0, (22, 9), AI_CHARGE));
    ch5.append(define_enemy(0x8, CLASS_ARMOR, 5, 0x20, 0, (22, 10), AI_CHARGE));
ch5_enemies();

ch6 = [];
def ch6_enemies():
    ch6_boss = define_enemy(0x2c, CLASS_PALADIN, 5, 0x16, 0x46, (4, 0x13), AI_CHARGE); ch6.append(ch6_boss);
    ch6.append(define_enemy(0x28, CLASS_SOCIAL, 6, 0x20, 0, (6, 0x12), AI_CHARGE));
    ch6.append(define_enemy(0x28, CLASS_SOCIAL, 6, 0x3, 0, (6, 0x14), AI_CHARGE));
    ch6.append(define_enemy(0x28, CLASS_HORSEMAN, 3, 0x11, 0, (7, 0x11), AI_CHARGE));
    ch6.append(define_enemy(0x28, CLASS_HORSEMAN, 3, 0x11, 0, (8, 0x12), AI_CHARGE));
    ch6.append(define_enemy(0x28, CLASS_ARMOR, 5, 0xf, 0, (8, 0xb), AI_GUARD, (9, 0xb)));
    ch6.append(define_enemy(0x28, CLASS_ARMOR, 3, 0xf, 0xf, (8, 0xf), AI_GUARD, (9, 0xf)));
    
    ch6.append(define_enemy(0x28, CLASS_SOCIAL, 6, 0x3, 0, (0xa, 0x12), AI_CHARGE));
    ch6.append(define_enemy(0x28, CLASS_SOCIAL, 5, 0x3, 0, (0xc, 0x14), AI_CHARGE));
    ch6.append(define_enemy(0x28, CLASS_SOCIAL, 6, 0x3, 0, (0xd, 0x16), AI_CHARGE));
    
    ch6.append(define_enemy(0x28, CLASS_SNIPER, 1, 0x12, 0x0, (0xa, 0xe), AI_GUARD));
    ch6.append(define_enemy(0x28, CLASS_ARCHER, 2, 0x13, 0, (0xa, 0xc), AI_GUARD));
    ch6.append(define_enemy(0x28, CLASS_ARMOR, 3, 0x20, 0, (0x7, 0xd), AI_GUARD));
    ch6.append(define_enemy(0x28, CLASS_ARCHER, 3, 0x11, 0, (0x3, 0xe), AI_GUARD));
    ch6.append(define_enemy(0x28, CLASS_SNIPER, 1, 0x11, 0x14, (0x2, 0xc), AI_GUARD, (0x2, 0xd)));
    ch6.append(define_enemy(0x28, CLASS_SOCIAL, 4, 0xc, 0, (0xc, 0xe), AI_CHARGE));
    ch6.append(define_enemy(0x28, CLASS_HORSEMAN, 3, 0x27, 0, (0xd, 0xc), AI_CHARGE));
    
    ch6.append(define_enemy(0x32, CLASS_FIGHTER, 6, 0x1c, 0, (6, 9), AI_GUARD));
    ch6.append(define_enemy(0x32, CLASS_FIGHTER, 9, 0x1e, 0x51, (0xa, 3), AI_GUARD));
    ch6.append(define_enemy(0x32, CLASS_FIGHTER, 3, 0x1b, 0, (0xf, 0x6), AI_GUARD));
ch6_enemies();

ch7 = [];
def ch7_enemies():
    ch7.append(define_enemy(0xb, CLASS_BISHOP, 1, 0x2c, 0x0, (0xa, 0xf), AI_GUARD, (0xa, 0xf)));
    ch7.append(define_enemy(0x5, CLASS_ARMOR, 5, 0xc, 0, (0xc, 0x1), AI_GUARD, (0xc, 0x1)));
    ch7.append(define_enemy(0x5, CLASS_ARMOR, 5, 0xc, 0, (0xc, 0x2), AI_GUARD, (0xc, 0x2)));
    ch7.append(define_enemy(0x5, CLASS_MAGE, 5, 0x2d, 0, (0x4, 0x2), AI_GUARD));
    ch7.append(define_enemy(0x5, CLASS_MAGE, 7, 0x2b, 0, (0x2, 0x5), AI_GUARD));
    ch7.append(define_enemy(0x5, CLASS_MAGE, 6, 0x2c, 0, (0x2, 0x9), AI_GUARD));
    ch7.append(define_enemy(0x5, CLASS_BISHOP, 1, 0x2b, 0x2c, (0xa, 0x5), AI_GUARD));
    ch7.append(define_enemy(0x5, CLASS_MERCENARY, 5, 0x9, 0x0, (0xc, 0x6), AI_GUARD));
    ch7.append(define_enemy(0x5, CLASS_BISHOP, 1, 0x2c, 0x51, (0xe, 0x5), AI_GUARD));
    ch7.append(define_enemy(0x5, CLASS_BISHOP, 1, 0x2b, 0x0, (0xe, 0xd), AI_GUARD));
    ch7.append(define_enemy(0x5, CLASS_BISHOP, 5, 0x3e, 0x0, (0x9, 0x14), AI_HEALER));
    ch7.append(define_enemy(0x5, CLASS_MAGE, 7, 0x31, 0x47, (0xa, 0x14), AI_HEALER));
    ch7.append(define_enemy(0x5, CLASS_MERCENARY, 6, 0x7, 0x42, (0x5, 0x13), AI_GUARD, (0x5, 0x13)));
    ch7.append(define_enemy(0x5, CLASS_MAGE, 5, 0x2e, 0x0, (0x6, 0x12), AI_GUARD));
    ch7.append(define_enemy(0x5, CLASS_BISHOP, 1, 0x2d, 0x0, (0xa, 0xb), AI_GUARD));
    ch7.append(define_enemy(0x34, CLASS_THIEF, 9, 0xa, 0x4d, (0x11, 0x13), AI_THIEF));
    ch7.append(define_enemy(0x34, CLASS_MERCENARY, 12, 0x7, 0x0, (0x11, 0x14), AI_THIEF));
    ch7.append(define_enemy(0xa, CLASS_THIEF, 10, 0x0, 0x44, (0x2, 0xf), AI_FOLLOW_MARS));
ch7_enemies();
ch7_reinforcements = [];
ch7_reinforcements.append(define_enemy(0x5, CLASS_MAGE, 5, 0x2b, 0x0, (0xd, 0x11), AI_CHARGE));
ch7_reinforcements.append(define_enemy(0x5, CLASS_MERCENARY, 5, 0x3, 0x0, (0xd, 0x11), AI_CHARGE));
ch7_reinforcements.append(define_enemy(0x5, CLASS_BISHOP, 3, 0x2e, 0x0, (0xd, 0x11), AI_CHARGE));
ch7_reinforcements.append(define_enemy(0x5, CLASS_HERO, 8, 0x1, 0x0, (0xd, 0x11), AI_CHARGE));
ch7_reinforcements.append(define_enemy(0x5, CLASS_MAGE, 7, 0x2b, 0x0, (0x1, 0x2), AI_CHARGE));

ch7_reinforcements.append(define_enemy2(0xc3, CLASS_GENERAL, 1, 0x16, 0x27, (0xd, 0x11), AI_CHARGE));

ch8 = [];
def ch8_enemies():
    ch8.append(define_enemy(0xd, CLASS_LORD, 8, 0xb, 0, (0x3, 0xa), AI_GUARD));
    ch8.append(define_enemy(0xc, CLASS_MAGE, 7, 0x30, 0x9, (0x2, 0xa), AI_GUARD));
    ch8.append(define_enemy(0xc, CLASS_CLERIC, 3, 0x36, 0x0, (0x4, 0x9), AI_HEALER));
    ch8.append(define_enemy(0xc, CLASS_PALADIN, 2, 0xe, 0x0, (0x2, 0x8), AI_GUARD));
    
    ch8.append(define_enemy(0xc, CLASS_SOCIAL, 6, 0xc, 0x0, (0x6, 0x3), AI_GUARD));
    ch8.append(define_enemy(0xc, CLASS_ARCHER, 6, 0x11, 0x40, (0x7, 0x2), AI_GUARD));
    
    ch8.append(define_enemy(0xc, CLASS_SOCIAL, 8, 0x2, 0x0, (0x5, 0x13), AI_CHARGE));
    ch8.append(define_enemy(0xc, CLASS_FIGHTER, 3, 0x0, 0x0, (0x4, 0x14), AI_CUDDLE));
    ch8.append(define_enemy(0xc, CLASS_MAGE, 6, 0x2b, 0x0, (0x4, 0x12), AI_CHARGE));
    
    ch8.append(define_enemy(0xc, CLASS_PEGASUS, 4, 0xc, 0x40, (0x6, 0x7), AI_CHARGE));
    ch8.append(define_enemy(0xc, CLASS_ARMOR, 6, 0xf, 0x40, (0xb, 0x2), AI_GUARD));
    ch8.append(define_enemy(0xc, CLASS_MERCENARY, 9, 0x1, 0x40, (0xc, 0x2), AI_CHARGE));
    ch8.append(define_enemy(0xc, CLASS_MAGE, 3, 0x2d, 0x0, (0xb, 0x5), AI_CHARGE));
    ch8.append(define_enemy(0xc, CLASS_CLERIC, 7, 0x3e, 0x0, (0x1, 0x13), AI_HEALER));
    
    ch8.append(define_enemy(0x35, CLASS_LORD, 8, 0xb, 0x0, (0x7, 0xd), AI_GUARD));
    
    ch8.append(define_enemy(0x33, CLASS_MAGE, 10, 0x2e, 0x40, (0x10, 0x7), AI_FOLLOW_MARS));
    ch8.append(define_enemy(0x36, CLASS_THIEF, 5, 0x2, 0x0, (0x012, 0x1), AI_THIEF));
    ch8.append(define_enemy(0xe, CLASS_CLERIC, 15, 0x0, 0x3d, (0x2, 0xe), AI_GUARD, (0x2, 0xe)));
ch8_enemies();

ch8_reinforcements = [];
ch8_reinforcements.append(define_enemy(0x36, CLASS_FIGHTER, 6, 0x1c, 0x0, (0x12, 0x3), AI_CHARGE));

ch8_reinforcements.append(define_enemy(0x36, CLASS_FIGHTER, 9, 0x1c, 0x0, (0x12, 0x1), AI_CHARGE));
ch8_reinforcements.append(define_enemy(0x36, CLASS_FIGHTER, 9, 0x1c, 0x0, (0x12, 0x2), AI_CHARGE));
ch8_reinforcements.append(define_enemy(0x36, CLASS_FIGHTER, 9, 0x1c, 0x0, (0x12, 0x3), AI_CHARGE));
ch8_reinforcements.append(define_enemy(0x36, CLASS_SOCIAL, 11, 0x1f, 0x51, (0x12, 0x4), AI_CHARGE));

ch8_reinforcements.append(define_enemy(0x36, CLASS_MAGE, 7, 0x2d, 0x0, (0x11, 0x1), AI_CHARGE));
ch8_reinforcements.append(define_enemy(0x36, CLASS_MAGE, 8, 0x2d, 0x0, (0x11, 0x2), AI_CHARGE));
ch8_reinforcements.append(define_enemy(0x36, CLASS_THIEF, 13, 0x7, 0x0, (0x11, 0x3), AI_CHARGE));

ch9 = [];
def ch9_enemies():
    ch9.append(define_enemy(0x10, CLASS_CLERIC, 10, 0x3e, 0x0, (0x1, 0x8), AI_HEALER));
    ch9.append(define_enemy(0xf, CLASS_PALADIN, 1, 0x2, 0x0, (0x1, 0x6), AI_GUARD));
    ch9.append(define_enemy(0xf, CLASS_PALADIN, 1, 0x2, 0x0, (0x1, 0xa), AI_GUARD));
    ch9.append(define_enemy(0xf, CLASS_BISHOP, 1, 0x2b, 0x0, (0x3, 0x7), AI_GUARD));
    ch9.append(define_enemy(0xf, CLASS_BISHOP, 1, 0x37, 0x0, (0x3, 0x9), AI_HEALER));
    ch9.append(define_enemy(0xf, CLASS_SOCIAL, 8, 0xf, 0x0, (0x6, 0x6), AI_GUARD));
    ch9.append(define_enemy(0xf, CLASS_SOCIAL, 8, 0x20, 0x0, (0xa, 0x6), AI_GUARD));
    ch9.append(define_enemy(0xf, CLASS_MAGE, 9, 0x2c, 0x0, (0x6, 0x9), AI_GUARD));
    ch9.append(define_enemy(0xf, CLASS_SOCIAL, 10, 0x3, 0x0, (0x6, 0x1), AI_GUARD));
    ch9.append(define_enemy(0xf, CLASS_PALADIN, 1, 0x20, 0x0, (0x7, 0xd), AI_GUARD));
    ch9.append(define_enemy(0xf, CLASS_BISHOP, 1, 0x2c, 0x0, (0x6, 0xd), AI_CHARGE));
    ch9.append(define_enemy(0xf, CLASS_SOCIAL, 10, 0xf, 0xf, (0x7, 0xe), AI_CHARGE));
    ch9.append(define_enemy(0xf, CLASS_ARCHER, 7, 0x12, 0x0, (0x8, 0xe), AI_GUARD));
    ch9.append(define_enemy(0xf, CLASS_SOCIAL, 9, 0xf, 0x0, (0x9, 0xe), AI_CHARGE));
    ch9.append(define_enemy(0xf, CLASS_ARCHER, 7, 0x12, 0x0, (0x9, 0xf), AI_GUARD));
    ch9.append(define_enemy(0xf, CLASS_MERCENARY, 8, 0x1, 0x51, (0xe, 0xe), AI_CHARGE));
ch9_enemies();

ch10 = [];
def ch10_enemies():
    ch10.append(define_enemy(0x15, CLASS_GENERAL, 1, 0xf, 0x51, (0x4, 0x1c), AI_GUARD, (0x4, 0x1c)));
    ch10.append(define_enemy(0x14, CLASS_SOCIAL, 9, 0x3, 0x0, (0x5, 0x1a), AI_GUARD));
    ch10.append(define_enemy(0x14, CLASS_SOCIAL, 10, 0x3, 0x1, (0x5, 0x1e), AI_GUARD));
    ch10.append(define_enemy(0x14, CLASS_ARMOR, 9, 0x20, 0x0, (0x7, 0x19), AI_GUARD));
    
    ch10.append(define_enemy(0x14, CLASS_HUNTER, 7, 0x12, 0x0, (0x4, 0x11), AI_CHARGE));
    ch10.append(define_enemy(0x14, CLASS_HUNTER, 8, 0x13, 0x0, (0x5, 0x12), AI_CHARGE));
    ch10.append(define_enemy(0x14, CLASS_MERCENARY, 9, 0x3, 0x0, (0x3, 0x10), AI_CHARGE));
    
    ch10.append(define_enemy(0x14, CLASS_SOCIAL, 8, 0xc, 0x0, (0x2, 0x1), AI_CHARGE));
    ch10.append(define_enemy(0x14, CLASS_HORSEMAN, 6, 0x11, 0x0, (0x4, 0x1), AI_CHARGE));
    ch10.append(define_enemy(0x14, CLASS_SOCIAL, 10, 0xc, 0x0, (0x3, 0x2), AI_CHARGE));
    ch10.append(define_enemy(0x14, CLASS_HORSEMAN, 7, 0x12, 0x0, (0x4, 0x4), AI_CHARGE));
    
    ch10.append(define_enemy(0x14, CLASS_FIGHTER, 8, 0x1f, 0x0, (0xc, 0x1), AI_CHARGE));
    ch10.append(define_enemy(0x14, CLASS_FIGHTER, 9, 0x1c, 0x0, (0xb, 0x2), AI_CHARGE));
    
    ch10.append(define_enemy(0x14, CLASS_PEGASUS, 7, 0xf, 0x0, (0xf, 0x2), AI_CHARGE));
    ch10.append(define_enemy(0x14, CLASS_PEGASUS, 8, 0x3, 0x0, (0x10, 0x1), AI_CHARGE));
    ch10.append(define_enemy(0x14, CLASS_PEGASUS, 9, 0x20, 0x0, (0x10, 0x3), AI_CHARGE));
    
    ch10.append(define_enemy(0x14, CLASS_ARMOR, 9, 0x20, 0x20, (0x11, 0xa), AI_GUARD));
    ch10.append(define_enemy(0x14, CLASS_ARMOR, 9, 0x3, 0x0, (0x11, 0x10), AI_GUARD));
    
    ch10.append(define_enemy(0x14, CLASS_DRAGON, 3, 0x25, 0x0, (0x2, 0x1e), AI_CHARGE));
ch10_enemies();
ch10_reinforcements = [];
ch10_reinforcements.append(define_enemy(0x34, CLASS_THIEF, 9, 0x7, 0x0, (0x1b, 0x1d), AI_THIEF));
ch10_reinforcements.append(define_enemy(0x34, CLASS_THIEF, 18, 0xa, 0xa, (0x1c, 0x1b), AI_THIEF));

ch10_reinforcements.append(define_enemy2(0xa8, CLASS_PEGASUS, 60, 0x21, 0x0, (0x11, 0x0e), AI_CHARGE));
ch10_reinforcements.append(define_enemy2(0xa8, CLASS_PEGASUS, 60, 0x21, 0x0, (0x12, 0x0f), AI_CHARGE));
ch10_reinforcements.append(define_enemy2(0xa8, CLASS_PEGASUS, 60, 0x21, 0x0, (0x13, 0x0e), AI_CHARGE));
ch10_reinforcements.append(define_enemy2(0xa8, CLASS_PEGASUS, 60, 0x21, 0x0, (0x12, 0x0d), AI_CHARGE));

ch11 = [];
def ch11_enemies():
    ch11.append(define_enemy(0x14, CLASS_ARMOR, 11, 0x20, 0x0, (0x15, 0x3), AI_GUARD, (0x15, 0x3)));
    ch11.append(define_enemy(0x14, CLASS_ARMOR, 12, 0xf, 0x0, (0x10, 0x11), AI_GUARD, (0x10, 0x11)));
    ch11.append(define_enemy(0x37, CLASS_MAMKUTE, 12, 0x24, 0x0, (0x13, 0x13), AI_GUARD));
    ch11.append(define_enemy(0x37, CLASS_PALADIN, 5, 0xf, 0x0, (0x13, 0x11), AI_GUARD));
    ch11.append(define_enemy(0x17, CLASS_PALADIN, 1, 0xc, 0x0, (0xa, 0x5), AI_CHARGE));
    ch11.append(define_enemy(0x14, CLASS_HERO, 1, 0x2, 0x0, (0x9, 0x7), AI_CHARGE));
    ch11.append(define_enemy(0x14, CLASS_ARMOR, 12, 0x3, 0x0, (0x3, 0x6), AI_GUARD, (0x3, 0x6)));
    ch11.append(define_enemy(0x17, CLASS_SOCIAL, 12, 0x20, 0x0, (0x8, 0x12), AI_CHARGE));
    ch11.append(define_enemy(0x17, CLASS_SOCIAL, 11, 0x0f, 0x0, (0xa, 0x12), AI_CHARGE));
    ch11.append(define_enemy(0x17, CLASS_SOCIAL, 13, 0x03, 0x0, (0xc, 0x12), AI_CHARGE));
    ch11.append(define_enemy(0x37, CLASS_MAMKUTE, 3, 0x22, 0x0, (0xb, 0xe), AI_GUARD, (0xb, 0xe)));
    ch11.append(define_enemy(0x14, CLASS_ARCHER, 14, 0x12, 0x0, (0xa, 0x1), AI_GUARD));
    ch11.append(define_enemy(0x14, CLASS_ARCHER, 12, 0x12, 0x0, (0xe, 0x1), AI_GUARD));
    ch11.append(define_enemy(0x14, CLASS_ARMOR, 15, 0xf, 0x0, (0xd, 0x1), AI_GUARD));
    ch11.append(define_enemy(0x37, CLASS_BISHOP, 4, 0x2e, 0x0, (0x2, 0xb), AI_GUARD));
    ch11.append(define_enemy(0x17, CLASS_ARCHER, 7, 0x11, 0x0, (0x5, 0xb), AI_CHARGE));
    ch11.append(define_enemy(0x17, CLASS_MERCENARY, 9, 0x3, 0x0, (0x6, 0xa), AI_CHARGE));
    ch11.append(define_enemy(0x17, CLASS_SNIPER, 4, 0x27, 0x0, (0x7, 0xb), AI_CHARGE));
    ch11.append(define_enemy(0x37, CLASS_BISHOP, 7, 0x37, 0x37, (0x4, 0x12), AI_HEALER));
    ch11.append(define_enemy(0x16, CLASS_GENERAL, 7, 0xe, 0xe, (0x7, 0x11), AI_GUARD, (0x7, 0x11)));
ch11_enemies();

ch11_reinforcements = [];
ch11_reinforcements.append(define_enemy(0x17, CLASS_PALADIN, 1, 0xc, 0x0, (0x11, 0x13), AI_CHARGE));
ch11_reinforcements.append(define_enemy(0x17, CLASS_HERO, 1, 0x3, 0x0, (0x16, 0x15), AI_CHARGE));

ch12 = [];
def ch12_enemies():
    ch12.append(define_enemy(0x18, CLASS_LORD, 15, 0xa, 0x5c, (0x6, 0x18), AI_GUARD));
    ch12.append(define_enemy(0x13, CLASS_GENERAL, 10, 0x27, 0x27, (0x6, 0x19), AI_GUARD, (0x6, 0x19)));
    ch12.append(define_enemy(0x12, CLASS_DRAGON, 1, 0x20, 0xf, (0x5, 0x16), AI_GUARD));
    
    ch12.append(define_enemy(0x11, CLASS_HORSEMAN, 8, 0x12, 0x0, (0x8, 0xa), AI_GUARD, (0x10, 0xd)));
    ch12.append(define_enemy(0x11, CLASS_SNIPER, 6, 0x11, 0x5b, (0x9, 0xb), AI_GUARD, (0xf, 0xc)));
    ch12.append(define_enemy(0x11, CLASS_GENERAL, 3, 0xc, 0x0, (0xa, 0x8), AI_GUARD, (0xf, 0xd)));
    ch12.append(define_enemy(0x11, CLASS_BISHOP, 14, 0x33, 0x58, (0x9, 0xd), AI_GUARD, (0x7, 0xe)));
    
    ch12.append(define_enemy(0x11, CLASS_PALADIN, 1, 0xc, 0x0, (0x6, 0xf), AI_CHARGE));
    ch12.append(define_enemy(0x11, CLASS_SOCIAL, 12, 0xf, 0x0, (0x5, 0x10), AI_CHARGE));
    
    ch12.append(define_enemy(0x11, CLASS_HERO, 3, 0x3, 0x0, (0x9, 0xe), AI_CHARGE));
    ch12.append(define_enemy(0x11, CLASS_MERCENARY, 3, 0x7, 0x0, (0x8, 0xf), AI_CHARGE));
    ch12.append(define_enemy(0x11, CLASS_MAMKUTE, 4, 0x23, 0x0, (0x7, 0x11), AI_GUARD));
    
    ch12.append(define_enemy(0x11, CLASS_DRAGON, 6, 0x20, 0x0, (0x6, 0xb), AI_CHARGE));
    ch12.append(define_enemy(0x11, CLASS_CLERIC, 15, 0x37, 0x3a, (0x6, 0x14), AI_HEALER));
    
    ch12.append(define_enemy(0x11, CLASS_HORSEMAN, 10, 0x11, 0x0, (0xe, 0xa), AI_CHARGE));
    ch12.append(define_enemy(0x11, CLASS_HUNTER, 6, 0x11, 0x0, (0xd, 0x1e), AI_GUARD));
    ch12.append(define_enemy(0x11, CLASS_THIEF, 3, 0x2, 0x0, (0x5, 0x13), AI_GUARD, (0x3, 0x19)));
ch12_enemies();

ch13 = [];
def ch13_enemies():
    ch13.append(define_enemy(0x24, CLASS_FIGHTER, 20, 0x1e, 0x0, (0x1, 0x13), AI_GUARD, (0x2, 0x16)));
    ch13.append(define_enemy(0x25, CLASS_FIGHTER, 18, 0x1f, 0x1f, (0x3, 0x15), AI_GUARD, (0x4, 0x15)));
    ch13.append(define_enemy(0x25, CLASS_FIGHTER, 16, 0x1f, 0x0, (0x5, 0x16), AI_GUARD, (0x9, 0x16)));
    ch13.append(define_enemy(0x25, CLASS_FIGHTER, 19, 0x1d, 0x0, (0x4, 0x13), AI_GUARD, (0x1, 0x12)));
    
    ch13.append(define_enemy(0x19, CLASS_HUNTER, 14, 0x13, 0x0, (0xb, 0x15), AI_GUARD));
    ch13.append(define_enemy(0x19, CLASS_SNIPER, 4, 0x14, 0x0, (0xc, 0x16), AI_GUARD));
    ch13.append(define_enemy(0x19, CLASS_BISHOP, 6, 0x31, 0x0, (0x13, 0x13), AI_GUARD));
    ch13.append(define_enemy(0x19, CLASS_THIEF, 15, 0x1, 0x0, (0x15, 0x16), AI_GUARD));
    ch13.append(define_enemy(0x19, CLASS_MAGE, 16, 0x2d, 0x0, (0x16, 0x14), AI_GUARD));
    ch13.append(define_enemy(0x19, CLASS_PEGASUS, 15, 0xf, 0x0, (0xd, 0x11), AI_GUARD));
    ch13.append(define_enemy(0x19, CLASS_HERO, 8, 0x3, 0x0, (0x14, 0xd), AI_GUARD));
    ch13.append(define_enemy(0x19, CLASS_HUNTER, 15, 0x27, 0x0, (0x13, 0xd), AI_GUARD));
    ch13.append(define_enemy(0x19, CLASS_HUNTER, 13, 0x27, 0x0, (0x15, 0x10), AI_GUARD));
    
    ch13.append(define_enemy(0x19, CLASS_DRAGON, 9, 0xf, 0x0, (0x01, 0x3), AI_GUARD));
    ch13.append(define_enemy(0x19, CLASS_DRAGON, 9, 0x25, 0x0, (0x1, 0x5), AI_GUARD));
    ch13.append(define_enemy(0x19, CLASS_SNIPER, 5, 0x27, 0x0, (0x8, 0x2), AI_GUARD));
    ch13.append(define_enemy(0x1a, CLASS_HERO, 15, 0x16, 0x16, (0x2, 0x9), AI_GUARD, (0x2, 0x9)));
    ch13.append(define_enemy(0x19, CLASS_PEGASUS, 19, 0x25, 0x25, (0x3, 0xe), AI_CHARGE));
ch13_enemies();

ch14 = [];
def ch14_enemies():
    ch14.append(define_enemy(0x1d, CLASS_MAMKUTE, 15, 0x23, 0x47, (0x5, 0xe), AI_GUARD, (0x5, 0xe)));
    ch14.append(define_enemy(0x1b, CLASS_BISHOP, 5, 0x34, 0xb, (0x6, 0xd), AI_GUARD));
    ch14.append(define_enemy(0x1c, CLASS_HERO, 6, 0xa, 0x4f, (0x8, 0xf), AI_GUARD));
    ch14.append(define_enemy(0x1c, CLASS_HERO, 6, 0xa, 0x51, (0x8, 0xd), AI_GUARD));
    
    ch14.append(define_enemy(0x1c, CLASS_BISHOP, 8, 0x37, 0x0, (0x5, 0x15), AI_HEALER));
    ch14.append(define_enemy(0x1c, CLASS_BISHOP, 10, 0x3e, 0x0, (0x5, 0x7), AI_HEALER));
    ch14.append(define_enemy(0x1c, CLASS_BISHOP, 9, 0x31, 0x0, (0xe, 0xe), AI_GUARD, (0xe, 0xe)));
    ch14.append(define_enemy(0x1c, CLASS_MAMKUTE, 7, 0x22, 0x0, (0x12, 0xc), AI_GUARD));
    ch14.append(define_enemy(0x1c, CLASS_MAMKUTE, 9, 0x24, 0x0, (0x12, 0x10), AI_GUARD));
    ch14.append(define_enemy(0x1c, CLASS_HERO, 9, 0x1, 0x0, (0x13, 0xe), AI_GUARD));
    
    ch14.append(define_enemy(0x1c, CLASS_MAMKUTE, 8, 0x24, 0x51, (0x18, 0x4), AI_CHARGE));
    ch14.append(define_enemy(0x1c, CLASS_MAMKUTE, 9, 0x24, 0x0, (0x19, 0x3), AI_CHARGE));
    ch14.append(define_enemy(0x1c, CLASS_MAMKUTE, 12, 0x22, 0x0, (0x9, 0x1a), AI_CHARGE));
    ch14.append(define_enemy(0x38, CLASS_MAMKUTE, 7, 0x24, 0x22, (0x9, 0x19), AI_CHARGE));
    ch14.append(define_enemy(0x1c, CLASS_GENERAL, 7, 0xd, 0x51, (0x13, 0x6), AI_CHARGE));
    ch14.append(define_enemy(0x1c, CLASS_GENERAL, 9, 0x12, 0x0, (0x14, 0x17), AI_CHARGE));
    ch14.append(define_enemy(0x1c, CLASS_BISHOP, 8, 0x30, 0x0, (0x9, 0x7), AI_CHARGE));
    ch14.append(define_enemy(0x1c, CLASS_BISHOP, 9, 0x31, 0x0, (0xb, 0x3), AI_CHARGE));
ch14_enemies();

ch15 = [];
def ch15_enemies():
    ch15.append(define_enemy(0x1e, CLASS_DRAGON, 16, 0x1a, 0xd, (0x19, 0x18), AI_CHARGE));
    ch15.append(define_enemy(0x8, CLASS_DRAGON, 8, 0xe, 0x0, (0x1a, 0x17), AI_CHARGE));
    ch15.append(define_enemy(0x8, CLASS_DRAGON, 9, 0x25, 0x0, (0x1a, 0x18), AI_CHARGE));
    ch15.append(define_enemy(0x8, CLASS_DRAGON, 12, 0xf, 0x0, (0x1a, 0x19), AI_CHARGE));
    ch15.append(define_enemy(0x8, CLASS_DRAGON, 9, 0x25, 0x0, (0x1a, 0x1a), AI_CHARGE));
    ch15.append(define_enemy(0x8, CLASS_DRAGON, 8, 0xe, 0x0, (0x1a, 0x1b), AI_CHARGE));
    
    ch15.append(define_enemy(0x8, CLASS_DRAGON, 6, 0x20, 0x0, (0x1b, 0x17), AI_CHARGE));
    ch15.append(define_enemy(0x8, CLASS_DRAGON, 7, 0xf, 0x0, (0x1b, 0x18), AI_CHARGE));
    ch15.append(define_enemy(0x8, CLASS_DRAGON, 9, 0xd, 0x0, (0x1b, 0x19), AI_CHARGE));
    ch15.append(define_enemy(0x8, CLASS_DRAGON, 7, 0xf, 0x0, (0x1b, 0x1a), AI_CHARGE));
    ch15.append(define_enemy(0x8, CLASS_DRAGON, 6, 0x20, 0x0, (0x1b, 0x1b), AI_CHARGE));
    
    ch15.append(define_enemy(0x20, CLASS_MAGE, 16, 0x31, 0x0, (0xf, 0x12), AI_GUARD));
    ch15.append(define_enemy(0x20, CLASS_MAGE, 18, 0x31, 0x31, (0x9, 0x3), AI_GUARD));
    ch15.append(define_enemy(0x20, CLASS_MAGE, 19, 0x31, 0x0, (0x8, 0xb), AI_GUARD));
    ch15.append(define_enemy(0x20, CLASS_BISHOP, 15, 0x3e, 0x4b, (0x7, 0xc), AI_HEALER));
    
    ch15.append(define_enemy(0x20, CLASS_GENERAL, 16, 0xf, 0x51, (0x1, 0x5), AI_GUARD, (0x1, 0x5)));
    ch15.append(define_enemy(0x20, CLASS_ARMOR, 20, 0xd, 0x0, (0x2, 0x4), AI_GUARD));
    ch15.append(define_enemy(0x20, CLASS_ARMOR, 20, 0x1, 0x0, (0x3, 0x6), AI_GUARD));
    ch15.append(define_enemy(0x20, CLASS_THIEF, 20, 0xa, 0x48, (0x1, 0x16), AI_CHARGE));
ch15_enemies();


ch16 = [];
def ch16_enemies():
    ch16.append(define_enemy(0x21, CLASS_BISHOP, 20, 0x2f, 0x0, (0x11, 0x3), AI_GUARD, (0x11, 0x3)));
    ch16.append(define_enemy(0x20, CLASS_GENERAL, 18, 0x14, 0x0, (0x12, 0x4), AI_GUARD, (0x12, 0x4)));
    ch16.append(define_enemy(0x20, CLASS_GENERAL, 18, 0xf, 0x0, (0x12, 0x2), AI_GUARD, (0x12, 0x2)));
    ch16.append(define_enemy(0x20, CLASS_HERO, 15, 0x1, 0x0, (0x13, 0x5), AI_GUARD));
    ch16.append(define_enemy(0x20, CLASS_SNIPER, 18, 0x14, 0x0, (0x13, 0x9), AI_GUARD));
    ch16.append(define_enemy(0x20, CLASS_GENERAL, 15, 0x14, 0x0, (0x10, 0x1), AI_GUARD));
    ch16.append(define_enemy(0x20, CLASS_GENERAL, 16, 0xe, 0x0, (0xe, 0x4), AI_GUARD));
    ch16.append(define_enemy(0x20, CLASS_GENERAL, 16, 0x1, 0x0, (0xe, 0x6), AI_GUARD));
    
    ch16.append(define_enemy(0x20, CLASS_HERO, 18, 0x7, 0x0, (0xc, 0x9), AI_GUARD));
    ch16.append(define_enemy(0x20, CLASS_HORSEMAN, 20, 0x14, 0x0, (0xb, 0x1), AI_GUARD));
    ch16.append(define_enemy(0x20, CLASS_GENERAL, 14, 0x7, 0x0, (0x9, 0x4), AI_GUARD));
    ch16.append(define_enemy(0x20, CLASS_GENERAL, 13, 0x25, 0x0, (0x9, 0x7), AI_GUARD));
    
    ch16.append(define_enemy(0x20, CLASS_PALADIN, 13, 0xe, 0x0, (0x9, 0x6), AI_CHARGE));
    ch16.append(define_enemy(0x20, CLASS_PALADIN, 13, 0xd, 0x0, (0x8, 0x6), AI_CHARGE));
    ch16.append(define_enemy(0x20, CLASS_PALADIN, 16, 0xe, 0x0, (0x7, 0x6), AI_CHARGE));
    ch16.append(define_enemy(0x20, CLASS_PALADIN, 16, 0xd, 0x0, (0x6, 0x6), AI_CHARGE));
    ch16.append(define_enemy(0x20, CLASS_DRAGON, 19, 0xd, 0x0, (0x12, 0x5), AI_GUARD));
    
    ch16.append(define_enemy(0x20, CLASS_BISHOP, 18, 0x37, 0x0, (0x13, 0x1), AI_HEALER));
    ch16.append(define_enemy(0x20, CLASS_BISHOP, 18, 0x3e, 0x0, (0x13, 0x8), AI_HEALER));
ch16_enemies();

ch17 = [];
def ch17_enemies():
    ch17.append(define_enemy(0x23, CLASS_BISHOP, 25, 0x32, 0x55, (0x1, 0x2), AI_GUARD, (0x1, 0x2)));
    ch17.append(define_enemy(0x5, CLASS_GENERAL, 20, 0x14, 0x0, (0x3, 0x2), AI_GUARD, (0x3, 0x2)));
    ch17.append(define_enemy(0x5, CLASS_HERO, 19, 0xa, 0xa, (0x5, 0xb), AI_GUARD));
    ch17.append(define_enemy(0x5, CLASS_GENERAL, 18, 0xf, 0x0, (0x5, 0x7), AI_GUARD, (0x5, 0x7)));
    ch17.append(define_enemy(0x5, CLASS_SNIPER, 20, 0x15, 0x0, (0x2, 0x13), AI_GUARD));
    ch17.append(define_enemy(0x5, CLASS_GENERAL, 20, 0xe, 0x0, (0x8, 0x14), AI_GUARD));
    ch17.append(define_enemy(0x5, CLASS_PALADIN, 19, 0x1, 0x0, (0x9, 0x15), AI_GUARD));
    ch17.append(define_enemy(0x5, CLASS_PALADIN, 20, 0xd, 0x0, (0xb, 0x6), AI_CHARGE));
    
    ch17.append(define_enemy(0x5, CLASS_PALADIN, 20, 0xe, 0x0, (0x14, 0xb), AI_CHARGE));
    ch17.append(define_enemy(0x5, CLASS_PALADIN, 20, 0x1, 0x0, (0x16, 0xb), AI_CHARGE));
    ch17.append(define_enemy(0x5, CLASS_GENERAL, 21, 0xd, 0x0, (0x13, 0x14), AI_GUARD));
    
    ch17.append(define_enemy(0x5, CLASS_BISHOP, 19, 0x31, 0x0, (0x12, 0x8), AI_GUARD));
    ch17.append(define_enemy(0x5, CLASS_BISHOP, 19, 0x31, 0x0, (0x12, 0xe), AI_GUARD));
    ch17.append(define_enemy(0x5, CLASS_BISHOP, 19, 0x2e, 0x0, (0x12, 0x2), AI_GUARD));
    ch17.append(define_enemy(0x5, CLASS_BISHOP, 20, 0x34, 0x0, (0x1, 0x5), AI_GUARD));
    ch17.append(define_enemy(0x5, CLASS_BISHOP, 20, 0x34, 0x0, (0x3, 0x11), AI_GUARD));
    ch17.append(define_enemy(0x5, CLASS_BISHOP, 16, 0x2e, 0x0, (0x7, 0xb), AI_CHARGE));
    
    ch17.append(define_enemy(0x5, CLASS_BISHOP, 15, 0x3e, 0x4b, (0x1, 0x3), AI_HEALER));
    ch17.append(define_enemy(0x5, CLASS_BISHOP, 15, 0x3e, 0x48, (0x1, 0x1), AI_HEALER));
    ch17.append(define_enemy(0x5, CLASS_BISHOP, 15, 0x3e, 0x0, (0xc, 0x1), AI_HEALER));
ch17_enemies();

ch18 = [];
def ch18_enemies():
    ch18.append(define_enemy(0x3a, CLASS_BISHOP, 10, 0x2b, 0x0, (0x7, 0x9), AI_GUARD, (0x7, 0x9)));
    ch18.append(define_enemy(0x26, CLASS_LORD, 45, 0x21, 0x21, (0x8, 0x9), AI_GUARD));
    ch18.append(define_enemy(0x3b, CLASS_HERO, 15, 0x16, 0x0, (0xc, 0x10), AI_CHARGE));
    ch18.append(define_enemy(0x3c, CLASS_LORD, 15, 0x16, 0x0, (0x2, 0xc), AI_GUARD));
    ch18.append(define_enemy(0x3d, CLASS_LORD, 18, 0x7, 0x0, (0x2, 0x6), AI_CHARGE));
    ch18.append(define_enemy(0x3e, CLASS_LORD, 20, 0xb, 0x0, (0x1, 0x9), AI_CHARGE));
    ch18.append(define_enemy(0x3f, CLASS_MAGE, 25, 0x31, 0x0, (0xc, 0x2), AI_GUARD));
    ch18.append(define_enemy(0x35, CLASS_LORD, 30, 0xb, 0x0, (0x4, 0x9), AI_GUARD));
    ch18.append(define_enemy(0x40, CLASS_DRAGON, 25, 0x25, 0x0, (0x1, 0x1), AI_CHARGE));
    ch18.append(define_enemy(0x41, CLASS_LORD, 17, 0xb, 0x0, (0x2, 0x2), AI_CHARGE));
    ch18.append(define_enemy2(0xb6, CLASS_LORD, 26, 0xa, 0x0, (0x6, 0x1), AI_CHARGE));
    ch18.append(define_enemy(0x43, CLASS_BISHOP, 18, 0x34, 0x0, (0x6, 0x6), AI_GUARD));
    ch18.append(define_enemy(0x44, CLASS_BISHOP, 20, 0x30, 0x0, (0x6, 0xc), AI_GUARD));
    ch18.append(define_enemy(0x2a, CLASS_CLERIC, 25, 0x3e, 0x0, (0x6, 0x9), AI_HEALER));
    ch18.append(define_enemy(0x31, CLASS_CLERIC, 25, 0x37, 0x0, (0x6, 0x8), AI_HEALER));
    ch18.append(define_enemy(0x1f, CLASS_CLERIC, 25, 0x3e, 0x0, (0x6, 0xa), AI_HEALER));
    ch18.append(define_enemy(0x4, CLASS_GENERAL, 20, 0x8, 0x0, (0x6, 0x10), AI_CHARGE));
ch18_enemies();

ch13_reinforcements = [];
ch13_reinforcements.append(define_enemy(0x19, CLASS_MAGE, 15, 0x2c, 0x0, (0xd, 0x1), AI_CHARGE));
ch13_reinforcements.append(define_enemy(0x19, CLASS_MAGE, 15, 0x2c, 0x0, (0xf, 0x1), AI_CHARGE));
ch13_reinforcements.append(define_enemy(0x19, CLASS_MAGE, 15, 0x2c, 0x0, (0x16, 0xc), AI_CHARGE));
ch13_reinforcements.append(define_enemy(0x19, CLASS_MAGE, 15, 0x2c, 0x0, (0x6, 0xa), AI_CHARGE));
ch13_reinforcements.append(define_enemy(0x25, CLASS_FIGHTER, 5, 0x1b, 0x1b, (0x16, 0x1), AI_CHARGE));

ch14_reinforcements = [];
ch14_reinforcements.append(define_enemy(0x1c, CLASS_BISHOP, 7, 0x2e, 0x0, (0x1b, 0x2), AI_CHARGE));
ch14_reinforcements.append(define_enemy(0x1c, CLASS_BISHOP, 9, 0x3c, 0x0, (0x1c, 0x3), AI_HEALER));
ch14_reinforcements.append(define_enemy(0x1c, CLASS_MAMKUTE, 9, 0x24, 0x0, (0x1c, 0x19), AI_CHARGE));
ch14_reinforcements.append(define_enemy(0x1c, CLASS_GENERAL, 10, 0x16, 0x51, (0x1b, 0x17), AI_CHARGE));

ch14_reinforcements.append(define_enemy(0x39, CLASS_MAMKUTE, 13, 0x24, 0x0, (0x1c, 0xe), AI_CHARGE));


ch16_reinforcements = [];
ch16_reinforcements.append(define_enemy(0x20, CLASS_GENERAL, 15, 0x7, 0x0, (0x2, 0xd), AI_CHARGE));
ch16_reinforcements.append(define_enemy(0x20, CLASS_GENERAL, 15, 0x7, 0x0, (0x3, 0xd), AI_CHARGE));
ch16_reinforcements.append(define_enemy(0x20, CLASS_GENERAL, 15, 0x7, 0x0, (0x4, 0xd), AI_CHARGE));
ch16_reinforcements.append(define_enemy(0x20, CLASS_GENERAL, 17, 0xe, 0x0, (0x2, 0xe), AI_CHARGE));
ch16_reinforcements.append(define_enemy(0x20, CLASS_GENERAL, 17, 0xe, 0x0, (0x3, 0xe), AI_CHARGE));
ch16_reinforcements.append(define_enemy(0x20, CLASS_GENERAL, 17, 0xe, 0x0, (0x4, 0xe), AI_CHARGE));

ch16_reinforcements.append(define_enemy(0x20, CLASS_BISHOP, 20, 0x2e, 0x0, (0x2, 0xd), AI_CHARGE));
ch16_reinforcements.append(define_enemy(0x20, CLASS_BISHOP, 20, 0x2e, 0x0, (0x3, 0xd), AI_CHARGE));
ch16_reinforcements.append(define_enemy(0x20, CLASS_BISHOP, 20, 0x2e, 0x0, (0x4, 0xd), AI_CHARGE));
ch16_reinforcements.append(define_enemy(0x20, CLASS_BISHOP, 20, 0x30, 0x0, (0x2, 0xe), AI_CHARGE));
ch16_reinforcements.append(define_enemy(0x20, CLASS_BISHOP, 20, 0x30, 0x0, (0x3, 0xe), AI_CHARGE));
ch16_reinforcements.append(define_enemy(0x20, CLASS_BISHOP, 20, 0x30, 0x30, (0x4, 0xe), AI_CHARGE));

ch17_reinforcements = [];
ch17_reinforcements.append(define_enemy(0x5, CLASS_BISHOP, 25, 0x2b, 0x0, (0x1, 0xb), AI_CHARGE));
ch17_reinforcements.append(define_enemy(0x5, CLASS_BISHOP, 25, 0x31, 0x4f, (0x1, 0xc), AI_CHARGE));
ch17_reinforcements.append(define_enemy(0x5, CLASS_BISHOP, 25, 0x30, 0x0, (0x1, 0xd), AI_CHARGE));

ch17_reinforcements.append(define_enemy(0x5, CLASS_BISHOP, 19, 0x31, 0x0, (0x2, 0x5), AI_CHARGE));
ch17_reinforcements.append(define_enemy(0x5, CLASS_GENERAL, 20, 0xf, 0x0, (0x6, 0x5), AI_CHARGE));
ch17_reinforcements.append(define_enemy(0x5, CLASS_PALADIN, 19, 0xe, 0x0, (0xd, 0x13), AI_CHARGE));
ch17_reinforcements.append(define_enemy(0x5, CLASS_PALADIN, 19, 0x1, 0x0, (0xd, 0x16), AI_CHARGE));
ch17_reinforcements.append(define_enemy(0x5, CLASS_SNIPER, 20, 0x14, 0x0, (0x16, 0x16), AI_CHARGE));
ch17_reinforcements.append(define_enemy(0x5, CLASS_BISHOP, 17, 0x31, 0x0, (0x12, 0xb), AI_CHARGE));
ch17_reinforcements.append(define_enemy(0x5, CLASS_BISHOP, 20, 0x3e, 0x0, (0xc, 0x3), AI_CHARGE));
ch17_reinforcements.append(define_enemy(0x5, CLASS_DRAGON, 25, 0xe, 0x0, (0x9, 0x1), AI_CHARGE));

ch15_reinforcements = [];
ch15_reinforcements.append(define_enemy(0x8, CLASS_DRAGON, 6, 0x20, 0x0, (0x17, 0x1c), AI_CHARGE));
ch15_reinforcements.append(define_enemy(0x8, CLASS_DRAGON, 6, 0x20, 0x0, (0x16, 0x1b), AI_CHARGE));
ch15_reinforcements.append(define_enemy(0x8, CLASS_DRAGON, 6, 0x20, 0x0, (0x15, 0x1c), AI_CHARGE));
ch15_reinforcements.append(define_enemy(0x8, CLASS_DRAGON, 6, 0x20, 0x0, (0x14, 0x1b), AI_CHARGE));
ch15_reinforcements.append(define_enemy(0x8, CLASS_DRAGON, 6, 0x20, 0x0, (0x13, 0x1c), AI_CHARGE));

ch15_reinforcements.append(define_enemy(0x8, CLASS_SNIPER, 8, 0x11, 0x0, (0x6, 0x1), AI_CHARGE));
ch15_reinforcements.append(define_enemy(0x8, CLASS_MAGE, 15, 0x2c, 0x48, (0x1, 0xa), AI_CHARGE));

ch18_reinforcements = [];
ch18_reinforcements.append(define_enemy2(0xbe, CLASS_DRAGON, 23, 0x13, 0x0e, (0x13, 0x02), AI_CHARGE));
ch18_reinforcements.append(define_enemy2(0xbe, CLASS_DRAGON, 23, 0x13, 0x0e, (0x13, 0x10), AI_CHARGE));
ch18_reinforcements.append(define_enemy2(0xbe, CLASS_DRAGON, 25, 0x10, 0x0e, (0x19, 0x09), AI_CHARGE));
ch18_reinforcements.append(define_enemy2(0xbe, CLASS_DRAGON, 25, 0x10, 0x0e, (0x13, 0x02), AI_CHARGE));
ch18_reinforcements.append(define_enemy2(0xbe, CLASS_DRAGON, 25, 0x10, 0x0e, (0x13, 0x10), AI_CHARGE));
ch18_reinforcements.append(define_enemy2(0xbe, CLASS_DRAGON, 27, 0x1a, 0x0e, (0x19, 0x09), AI_CHARGE));

ch18_reinforcements.append(define_enemy2(0xbe, CLASS_DRAGON, 30, 0x1a, 0x0e, (0x13, 0x02), AI_CHARGE));
ch18_reinforcements.append(define_enemy2(0xbe, CLASS_DRAGON, 30, 0x1a, 0x0e, (0x13, 0x10), AI_CHARGE));

ch_moon = [];
ch_moon.append(define_enemy2(0xa3, CLASS_MAGE, 5, 0x3b, 0x4f, (0x1, 0x1), AI_GUARD));
#make_chapter(ch_moon);

#make_chapter(ch1);
#make_chapter(ch2);
#make_chapter(ch3);
#make_chapter(ch4);
#make_chapter(ch5);
#make_chapter(ch6);
#make_chapter(ch7);
#make_chapter(ch8);
#make_chapter(ch9);
#make_chapter(ch10);
#make_chapter(ch11);
#make_chapter(ch12);
#make_chapter(ch13);
#make_chapter(ch14);
#make_chapter(ch15);
#make_chapter(ch16);
#make_chapter(ch17);
#make_chapter(ch18);

#make_chapter(ch7_reinforcements);
#make_chapter(ch8_reinforcements);
#make_chapter(ch10_reinforcements);
#make_chapter(ch11_reinforcements);
#make_chapter(ch13_reinforcements);
#make_chapter(ch14_reinforcements);
#make_chapter(ch16_reinforcements);
#make_chapter(ch17_reinforcements);
#make_chapter(ch15_reinforcements);
#make_chapter(ch18_reinforcements);

#make_unit(thomas);
#make_unit(jake);
#make_unit(roger);
#make_unit(morodof);
#make_unit(delmud);

#make_unit(selfina);
#make_unit(fin);
#make_unit(cain);
#make_unit(glade);
#make_unit(robert);
#make_unit(alba);

#make_unit(claude);
#make_unit(mable);
#make_unit(elice);
#make_unit(barnef);

#make_unit(cuan);
#make_unit(ethlin);
#make_unit(sigurd);

#make_unit(dean);

#make_unit(kirby);