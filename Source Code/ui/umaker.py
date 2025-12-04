import tkinter as tk;
from tkinter import ttk;
from random import randint, seed;
import time;

def rng(arg_min, arg_max):
    return randint(arg_min, arg_max);

class Maker():
    def __init__(self, arg_dir):
        seed(int(time.time() * 1000) % (2**32 - 1));
        self.wnd = tk.Toplevel()
        self.wnd.title("Unit Maker");
        self.wnd.geometry("600x550+64+64")
        self.unit = {};
        self.labels = {};
        self.istats = {};
        
        self.rows = 0;
        self.cols = 0;
        
        self.dir = arg_dir;
        self.ini = False;
        self.grow = tk.BooleanVar();
        self.grow.set(True);
        
        self.bbox = tk.Text(self.wnd, width=60, height=1);
        self.bbox.grid(row=0, column=0, columnspan=4, sticky=tk.W, padx=8,pady=6);
        self.rows += 1;
        
        self.btn_load = tk.Button(self.wnd, text="Load", width=10, command=self.load_unit);
        self.btn_load.grid(row=9, column=2, sticky=tk.W, padx=8, pady=6);
        
        self.btn_make = tk.Button(self.wnd, text="Generate", width=10, command=self.generate);
        self.btn_make.grid(row=9, column=3, sticky=tk.W, padx=8, pady=6);
        
        self.btn_bases = tk.Button(self.wnd, text="Set Stats to Class Bases", width=20, command=self.update_bases);
        self.btn_bases.grid(row=10, column=2, sticky=tk.W, padx=8, pady=6);
        
        self.check_grow = tk.Checkbutton(self.wnd, text="Scale by Level/Growths", variable=self.grow);
        self.check_grow.grid(row=10, column=3, sticky=tk.W, padx=8, pady=6);
        
        
        self.load_labels();
        self.bases = self.load_bases(arg_dir + "gameplay/class_bases.txt");
        self.growths = self.load_bases(arg_dir + "gameplay/growths.txt");
        
        self.add_vals();
        
        #self.btn_load = tk.Button(self.wnd, text="Reload Names", width=20, command=self.load_labels);
        #self.btn_load.grid(row=10, column=2, columnspan=2, sticky=tk.W, padx=8, pady=6);
        
        self.wnd.mainloop();
        
    
    def load_names(self, arg_dir):
        tmp_lbl = {};
        with open(arg_dir, "r") as file:
            for line in file:
                if (len(line) > 1):
                    tmp_lbl[line[0:2]] = line[3:-1];
        return tmp_lbl;
    
    def load_bases(self, arg_dir):
        tmp_bases = {};
        index = "";
        tmp_stats = {};
        with open(arg_dir, "r") as file:
            for line in file:
                if (len(line) > 2):
                    if (line[0] == "{"):
                        if (index != ""):
                            tmp_bases[index] = tmp_stats;
                            tmp_stats = {};
                        index = line[1:3];
                    else:
                        tmp_stats[line[1:4]] = line[6:-1];
        if (index != ""):
            tmp_bases[index] = tmp_stats;
            tmp_stats = {};
        return tmp_bases;
        
                        
    
    def hex_format(self, arg_val):
        tmp_byteval = "";
        if (arg_val < 0x10):
            tmp_byteval = "0";
        tmp = str(hex(arg_val));
        tmp_byteval = tmp_byteval + tmp[2:len(tmp)];
        return tmp_byteval.lower();
    
    def hex_format2(self, arg_val):
        tmp_byteval = "";
        if (arg_val < 0x1000):
            tmp_byteval = tmp_byteval + "0";
        if (arg_val < 0x0100):
            tmp_byteval = tmp_byteval + "0";
        if (arg_val < 0x0010):
            tmp_byteval = tmp_byteval + "0";
        tmp = str(hex(arg_val));
        tmp_byteval = tmp_byteval + tmp[2:len(tmp)];
        return tmp_byteval.lower();
    
    def get_label(self, arg_type, arg_val):
        labels = self.labels;
        tmp_lbls = labels[arg_type];
        if not arg_val in tmp_lbls.keys():
            return " ";
        return labels[arg_type][arg_val];
    
    
    def get_val(self, arg_lbl):
        unit = self.unit;
        tmp_val = unit[arg_lbl].get();
        val_ln = len(tmp_val);
        if (val_ln > 4):
            tmp_val = tmp_val[0:4];
        hx = False;
        if (val_ln > 1):
            if (tmp_val[0:2] == "0x"):
                hx = True;
        if not hx:
            return int(tmp_val);
        else:
            return int(tmp_val, 16);
        
    def get_val_hex2(self, arg_lbl):
        unit = self.unit;
        return unit[arg_lbl].get();
        
    def get_val_hex(self, arg_val):
        return self.hex_format(self.get_val(arg_val));
    
    def get_blist(self, arg_start, arg_end):
        #return [hex(i) for i in range(arg_start, arg_end + 1)];
        tmp_lst = [];
        hf = self.hex_format;
        for i in range(arg_start, arg_end+1):
            tmp_lst.append(hf(i));
        return tmp_lst
    
    def update_iusage1(self, arg_e):
        self.update_iusage(1);
    def update_iusage2(self, arg_e):
        self.update_iusage(2);
    def update_iusage3(self, arg_e):
        self.update_iusage(3);
    def update_iusage4(self, arg_e):
        self.update_iusage(4);
        
            
    def update_iusage(self, arg_i):
        lbl_name1 = "Item" + str(arg_i);
        lbl_name2 = lbl_name1 + " Uses";
        lbl = self.unit[lbl_name1].get()[2:4];
        lbl2 = self.unit[lbl_name2];
        if (lbl == "00"):
            lbl2.set("0");
        else:
            istats = self.istats;
            lbl2.set(istats[lbl]["Uses"]);
            
    def get_level_stat(self, arg_stat, arg_lvl, arg_class, arg_id):
        val = int(self.bases[arg_class][arg_stat]);
        growths = self.growths[arg_id];
        if (self.grow.get()):
            for i in range(arg_lvl-1):
                if (rng(0,10) < int(growths[arg_stat], 16)):
                    val += 1;
        return val; 
            
    def update_bases(self):
        lbls = self.unit;
        tmp_id = lbls["Name"].get()[2:4];
        tmp_class = lbls["Class"].get()[2:4];
        tmp_lvl = int(lbls["Level"].get());
        
        lbls["Strength"].set(self.get_level_stat("STR", tmp_lvl, tmp_class, tmp_id));
        lbls["Skill"].set(self.get_level_stat("SKL", tmp_lvl, tmp_class, tmp_id));
        lbls["Weapon Lv."].set(self.get_level_stat("WLV", tmp_lvl, tmp_class, tmp_id));
        lbls["Speed"].set(self.get_level_stat("SPD", tmp_lvl, tmp_class, tmp_id));
        lbls["Luck"].set(self.get_level_stat("LCK", tmp_lvl, tmp_class, tmp_id));
        lbls["Defense"].set(self.get_level_stat("DEF", tmp_lvl, tmp_class, tmp_id));
        lbls["Movement"].set(self.bases[tmp_class]["MOV"]);
        
        hp = self.get_level_stat("MHP", tmp_lvl, tmp_class, tmp_id);
        lbls["HP"].set(hp);
        lbls["Max HP"].set(hp);
        
        
            
    
    def get_ilist(self, arg_start, arg_end):
        return [str(i) for i in range(arg_start, arg_end + 1)]
    
    def add_val(self, arg_lbl, arg_min, arg_max, arg_hex=True, arg_lbls="", arg_cmd=None):
        rows = self.rows;
        cols = self.cols;
        tmp_lbl = tk.Label(self.wnd, text=arg_lbl + ": ");
        tmp_lbl.grid(row=rows, column=cols, sticky=tk.W, padx=8, pady=4);
        
        tmp_vals2 = [];
        
        if (arg_hex):
            tmp_vals = self.get_blist(arg_min, arg_max);
            if (arg_lbls != ""):
                for i in range(len(tmp_vals)):
                    val = tmp_vals[i];
                    b = val[0:2];
                    #if (len(b) < 4):
                    #    b = "0" + b;
                    tmp_vals2.append("0x" + b + " - " + self.get_label(arg_lbls, b));
            else:
                for i in range(len(tmp_vals)):
                    b = tmp_vals[i][0:2];
                    #if (len(b) < 4):
                    #    b = "0" + b;
                    tmp_vals2.append(b);
                
        else:
            tmp_vals2 = self.get_ilist(arg_min, arg_max);
        selected = tk.StringVar();
        selected.set(tmp_vals2[0]);
        unit = self.unit;
        unit[arg_lbl] = selected;
        tmp_val = ttk.Combobox(self.wnd, values=tmp_vals2, textvariable=selected)
        tmp_val.grid(row=rows, column=cols+1, sticky=tk.W, padx=8, pady=4);
        if (arg_cmd):
            tmp_val.bind("<<ComboboxSelected>>", arg_cmd);
        rows += 1;
        if (rows > 17):
            rows = 1;
            cols += 2;
        self.rows = rows;
        self.cols = cols;
        return tmp_val;
    
    
    
    def load_unit(self):
        unit = self.unit;
        labels = self.labels;
        current = self.get_bbox();
        cur_ln = len(current);
        if (cur_ln > 1) and (cur_ln < 0x38):
            tmp_unit = current;
            bytelist = [];
            for i in range(0x1b):
                i2 = i * 2;
                bytelist.append(int(tmp_unit[i2:i2+2], 16));
            def set_lbl(arg_lbl, arg_index):
                unit[arg_lbl].set(bytelist[arg_index]);
                
            def set_lbl_hex(arg_lbl, arg_index, arg_lbls=""):
                if (arg_lbls != ""):
                    tmp = "0x" + self.hex_format(bytelist[arg_index]);
                    tmp = tmp + " - " + self.get_label(arg_lbls, self.hex_format(bytelist[arg_index]));
                else:
                    tmp = self.hex_format(bytelist[arg_index]);
                unit[arg_lbl].set(tmp);
                
            set_lbl_hex("Name", 0, "names");
            set_lbl_hex("Class", 1, "classes");
            set_lbl("Level", 2);
            set_lbl("HP", 3);
            set_lbl("Max HP", 4);
            set_lbl("EXP", 5);
            
            set_lbl("Strength", 7);
            set_lbl("Skill", 8);
            set_lbl("Weapon Lv.", 9);
            set_lbl("Speed", 10);
            set_lbl("Luck", 11);
            set_lbl("Defense", 12);
            set_lbl("Movement", 13);
            set_lbl("Visibility", 0xe);
            res = bytelist[0xf];
            if (res > 0x80):
                res += -0x80;
            unit["Resistance"].set(res);
            
            set_lbl_hex("Y", 0x10);
            set_lbl_hex("X", 0x11);
            
            set_lbl_hex("Item1", 0x13, "item_names");
            set_lbl_hex("Item2", 0x14, "item_names");
            set_lbl_hex("Item3", 0x15, "item_names");
            set_lbl_hex("Item4", 0x16, "item_names");
            
            set_lbl("Item1 Uses", 0x17);
            set_lbl("Item2 Uses", 0x18);
            set_lbl("Item3 Uses", 0x19);
            set_lbl("Item4 Uses", 0x1a);
            
        self.unit = unit;
            
    
    def get_bbox(self):
        return self.bbox.get("1.0", "end");
        
    def set_bbox(self, arg_str):
        self.bbox.delete("1.0", "end");
        self.bbox.insert("1.0", arg_str);
        
    
    
    def generate(self):
        tmp_unit = "";
        get_val_hex = self.get_val_hex;
        
        tmp_unit += get_val_hex("Name");
        tmp_unit += get_val_hex("Class");
        tmp_unit += get_val_hex("Level");
        tmp_unit += get_val_hex("HP");
        tmp_unit += get_val_hex("Max HP");
        tmp_unit += get_val_hex("EXP");
        
        tmp_unit += "00";
        
        tmp_unit += get_val_hex("Strength");
        tmp_unit += get_val_hex("Skill");
        tmp_unit += get_val_hex("Weapon Lv.");
        tmp_unit += get_val_hex("Speed");
        tmp_unit += get_val_hex("Luck");
        tmp_unit += get_val_hex("Defense");
        tmp_unit += get_val_hex("Movement");
        tmp_unit += get_val_hex("Visibility");
        
        tmp_val = self.get_val("Resistance");
        if (tmp_val > 0):
            tmp_val += 0x80;
        else:
            tmp_val = 0;
        tmp_unit += self.hex_format(tmp_val);
        
        tmp_unit += self.get_val_hex2("Y");
        tmp_unit += self.get_val_hex2("X");
        
        tmp_unit += "00";
        
        tmp_unit += get_val_hex("Item1");
        tmp_unit += get_val_hex("Item2");
        tmp_unit += get_val_hex("Item3");
        tmp_unit += get_val_hex("Item4");
        
        tmp_unit += get_val_hex("Item1 Uses");
        tmp_unit += get_val_hex("Item2 Uses");
        tmp_unit += get_val_hex("Item3 Uses");
        tmp_unit += get_val_hex("Item4 Uses");
        
        self.set_bbox(tmp_unit);
    
    def add_vals(self):
        rows = self.rows; cols = self.cols;
        rows = 1; cols = 0;
        add_val = self.add_val;
        
        add_val("Name", 0x1, 0x35, True, "names");
        add_val("Class", 0x1, 0x16, True, "classes");
        add_val("Level", 0x1, 99, False);
        add_val("HP", 0x1, 52, False);
        add_val("Max HP", 0x1, 52, False);
        add_val("EXP", 0x0, 99, False);
        
        add_val("Strength", 0x0, 99, False);
        add_val("Skill", 0x0, 99, False);
        add_val("Weapon Lv.", 0x0, 99, False);
        add_val("Speed", 0x0, 99, False);
        add_val("Luck", 0x0, 99, False);
        add_val("Defense", 0x0, 99, False);
        add_val("Movement", 0x0, 99, False);
        add_val("Visibility", 0x0, 99, False);
        add_val("Resistance", 0x0, 99, False);
        
        add_val("Y", 0x1, 0x20, True);
        add_val("X", 0x1, 0x20, True);
        
        add_val("Item1", 0x0, 0x5C, True, "item_names", self.update_iusage1);
        add_val("Item2", 0x0, 0x5C, True, "item_names", self.update_iusage2);
        add_val("Item3", 0x0, 0x5C, True, "item_names", self.update_iusage3);
        add_val("Item4", 0x0, 0x5C, True, "item_names", self.update_iusage4);
        
        add_val("Item1 Uses", 0x0, 0xff, False);
        add_val("Item2 Uses", 0x0, 0xff, False);
        add_val("Item3 Uses", 0x0, 0xff, False);
        add_val("Item4 Uses", 0x0, 0xff, False);
        
        self.rows = rows;
        self.cols = cols;
        
    def load_itemstats(self):
        proj_dir = self.dir;
        base_dir = proj_dir + "gameplay/items/item_data.txt";
        item_data = {};
        with open(base_dir, "r") as file:
            key = "";
            tmp_dct = {};
            for line in file:
                ln = len(line);
                if (ln > 1):
                    if (line[2] == ":"):
                        if (key != ""):
                            item_data[key] = tmp_dct.copy();
                        key = line[0:2];
                    else:
                        line = line.replace(" ", "");
                        vals = line.strip().split(":");
                        tmp_dct[vals[0]] = vals[1];
            if (key != ""):
                item_data[key] = tmp_dct.copy();
        return item_data;
    
    def load_labels(self):
        proj_dir = self.dir;
        if (proj_dir):
            labels = self.labels;
            base_dir = proj_dir + "text/names/";
            item_names_dir = proj_dir + "text/names/";
            #base_dir = "resource/names/";
            labels["names"] = self.load_names(base_dir + "names.txt");
            labels["item_names"] = self.load_names(item_names_dir + "items.txt");
            labels["classes"] = self.load_names(base_dir + "classes.txt");
            self.istats = self.load_itemstats();
            
            labels["item_names"]["00"] = "NO ITEM";
            self.add_vals();
            
            
            
            
            
            
            