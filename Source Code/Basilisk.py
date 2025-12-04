import main;
import os;
import tkinter as tk;
from tkinter import filedialog as fd;
from tkinter import PhotoImage as pi
from os.path import exists, join;
from os import makedirs
import sys as sys;
from sys import stdout, stderr
from random import randint;
from shutil import copy as file_copy;
from shutil import copytree;
from ui.umaker import Maker as UMaker;
from ui.patcher import Patcher;

class FEProject:
    def __init__(self):
        self.base_rom = "";
        self.name = "none";
        self.directory = "";

def rng(arg_min, arg_max):
    return randint(arg_min, arg_max);

day_msgs = [];
day_msgs.append("Let them all GO?\nBut MAAAAAAARS?");
day_msgs.append("His name is Mars! Deal with it! >:]");
day_msgs.append("Kaga Loyalists UNITE!");
day_msgs.append("Johnny was bad, even as a\nchild everybody could tell!");
day_msgs.append("FE3 is better.");
day_msgs.append("Go play Octo Vinctum\non Steam now!\nhttps://store.steampowered.com/app/1899110/Octo_Vinctum_Revenge_of_the_Czar/");
day_msgs.append("Some dude named Polinym wasted 3 years of his life on this.");
day_msgs.append("Are you... a real villain?");
day_msgs.append("This looks like a good spot\nto find ghosts at night.");
day_msgs.append("Engage and good writing are\nlike oil and water.");
day_msgs.append("Mystic Knights of\nthe Oingo Boingo!");
day_msgs.append("He's the leader of the bunch,\nyou know him well.");
day_msgs.append("Welcome to where time stands\nstill. No one leaves and no\none will.");
day_msgs.append("  AT FIRST.\n  THERE ARE\n DARK DRAGON,\nFALCION SWORD\n     AND");
day_msgs.append("Ah, superintendent Chalmers, welcome!\nI hope you're prepared for an unforgettable luncheon.");
day_msgs.append("Isn't this fun? Isn't this what life's all about?\nIsn't this a dream come true?\nIsn't this a nightmare too?");
day_msgs.append("In the middle of the night...\nI go walkin' in my sleep.");
day_msgs.append("Fighting evil by moonlight,\nwinning love by daylight,\nnever running from a real fight!\nHe is the one named Starlord Mars!");
day_msgs.append("A long long time ago,\nin the land of idiot boys.\nThere lived a cat, a phenomenal cat,\nwho loved to wallow all day!");
day_msgs.append("Not bad for a guy with ONE EYE!");
day_msgs.append("The blood of Meridia denies even DEATH!");

c_black = '#000000';
c_white = '#F0F0F0';
c_blue = '#2828A0';
c_blue2 = '#6868D0';
c_lblue = '#4848D0';
c_green = "#87CE67";



global base_rom;
base_rom = "";

global umaker_inst;
global patcher_inst;
umaker_inst = None;
patcher_inst = None;

class ConsoleText (tk.Text):
    # A Text widget that can display console output and error

    def __init__ (self, master, **kwargs):
        # Initialize the Text widget with some default options
        super ().__init__ (master, **kwargs)
        self.configure(state="disabled", bg="white", fg="black");
        self["width"] = 60;
        self["height"] = 8;

    def write (self, text):
        # Insert the text into the Text widget
        self.configure (state="normal")
        self.insert ("end", text)
        self.configure (state="disabled")
        self.see ("end") # Scroll to the end

    def flush (self):
        # Do nothing
        pass



def get_boolstr(arg_str):
    if (arg_str == "True"):
        return True;
    else:
        return False;

def include_dir(arg_dir):
    if not exists(join(arg_dir)):
        makedirs(join(arg_dir));
        
def dir_exists(arg_dir):
    return exists(join(arg_dir));

def file_exists(path):
    return os.path.isfile(path);


wnd_all = [];

wnd_main = tk.Tk();

wnd_main.title("Basilisk - FE1 Editor");
wnd_main.geometry("800x460+50+50");
wnd_main.resizable(False, False);
wnd_main.iconbitmap("resource/icon.ico");
wnd_main.iconbitmap(default="resource/icon.ico");
wnd_main["bg"] = c_blue;
#wnd_main["fg"] = c_white;
cp = FEProject();



def text_loadfrom(arg_textbox):
    return arg_textbox.get('1.0', 'end-1c');

def pos(thing, arg_row, arg_col):
    thing.grid(row=arg_row, column=arg_col, padx=(10, 10), pady=(10, 10));
    
def load_rom():
    global base_rom;
    file = fd.askopenfilename(title="Select a Fire Emblem 1 ROM!.", filetypes=(("FE1 ROMs","*.nes"),("all files","*.*")));
    if file != "":
        cp.base_rom = file;
        lbl_load_rom["text"] = "Base ROM: " + file;
        file_copy(file, "resource/fe1.nes");
        
def load_dir():
    global base_rom;
    dir = fd.askdirectory();
    if dir != "":
        cp.directory = dir;
        lbl_load_dir["text"] = "Path: " + dir;
    
def backup():    
    cp_dir = cp.directory;
    name = cp.name;
    if (cp_dir) and (name):
        proj_dir = cp_dir + "/" + name + "/";
        edit_rom = proj_dir + name + ".nes";
        fname = proj_dir + name + ".nes";
        backups_dir = proj_dir + "backups/";
        include_dir(backups_dir);
        base_name = backups_dir + name + "_backup";
        i = 1;
        while (True):
            str_i = str(i);
            fname = base_name + str_i + ".nes";
            if not file_exists(fname):
                file_copy(edit_rom, fname);
                print("Created backup #" + str_i);
                break;
            i += 1;
            

#2c1c2
def save_config():
    with open("resource/data/save.txt", "w") as save_file:
        cp.name = text_loadfrom(txt_pname);
        tmp_writestr = cp.base_rom + "\n";
        tmp_writestr += cp.directory + "\n";
        tmp_writestr += cp.name + "\n";
        tmp_writestr += "BASILISK TOOL BY POLINYM\n";
        save_file.write(tmp_writestr);
        print("Config file saved.");
    
def decompile():
    cp.name = text_loadfrom(txt_pname);
    if cp.name != "" and cp.base_rom != "" and cp.directory != "":
        dir = cp.directory + "/" + cp.name;
        if not (dir_exists(dir)):
            template = join("resource/project_template");
            if not os.path.exists(template):
                print("Error!\nNo template project exists in resource/project_template.\nOnly edit it if you know what you're doing.");
            else:
                copytree(template, dir);
                file_copy(cp.base_rom, dir + "/" + cp.name + ".nes");
                print("Created project folder \"" + cp.name + "\".");
        else:
            print("Error!\nA directory for project \"" + cp.name + "\" already exists.\nYou must delete it first.");
          
def browse_button():
    # Ask the user to select a directory
    dir = cp.directory + "/" + cp.name;
    if (dir):
        os.startfile(dir);
            
def project_compile():
    cp.name = text_loadfrom(txt_pname);
    project_name = cp.name;
    if cp.name != "":
        if cp.directory != "":
            if cp.base_rom != "":
                dir = cp.directory + "/" + cp.name;
                if dir_exists(dir):
                    main.compile(dir, cp.name);
                else:
                    print("Error!\nProject \"" + project_name + "\"not found.");
            else:
                print("Error!\nNo base ROM provided.");
        else:
            print("Error!\nNo project directory provided.");
          
          
def open_umaker():
    #global umaker_inst;
    #if umaker_inst:
    #    umaker_inst.lift(wnd_main);
    #else:
    cp_dir = cp.directory;
    name = cp.name;
    if (cp_dir) and (name):
        proj_dir = cp_dir + "/" + name + "/";
    else:
        print("(!) Opened Unit Maker with no project. (!)");
        proj_dir = "";
    umaker_inst = UMaker(proj_dir);
    
def open_patcher():
    #global umaker_inst;
    #if umaker_inst:
    #    umaker_inst.lift(wnd_main);
    #else:
    cp_dir = cp.directory;
    name = cp.name;
    if (cp_dir) and (name):
        proj_dir = cp_dir + "/" + name + "/";
    else:
        print("(!) Opened Pather with no project. (!)");
        proj_dir = "";
    patcher_inst = Patcher(proj_dir + name + ".nes", "resource/patches");
    
    
    
row = 0;
img = pi(file="resource/logo.png");
lbl_img = tk.Label(wnd_main, image=img);
pos(lbl_img, row, 0);

row += 1;
btn_load_rom = tk.Button(wnd_main, text="Load Base ROM");
btn_load_rom["command"] = load_rom;
btn_load_rom["bg"] = c_blue2;
btn_load_rom["fg"] = c_white;
pos(btn_load_rom, row, 0);

lbl_load_rom = tk.Label(wnd_main, text = "");
lbl_load_rom["bg"] = c_blue;
lbl_load_rom["fg"] = c_white;
pos(lbl_load_rom, row, 1);



row += 1;
btn_load_dir = tk.Button(wnd_main, text="Set Project Directory");
btn_load_dir["command"] = load_dir;
btn_load_dir["bg"] = c_blue2;
btn_load_dir["fg"] = c_white;
pos(btn_load_dir, row, 0);

lbl_load_dir = tk.Label(wnd_main, text = "");
lbl_load_dir["bg"] = c_blue;
lbl_load_dir["fg"] = c_white;
pos(lbl_load_dir, row, 1);

row += 1;
lbl_pname = tk.Label(wnd_main, text = "Project Name ");
lbl_pname["bg"] = c_blue;
lbl_pname["fg"] = c_white;
pos(lbl_pname, row, 0);

txt_pname = tk.Text(wnd_main, width=24, height=1);
txt_pname["bg"] = c_blue;
txt_pname["fg"] = c_white;
pos(txt_pname, row, 1);
row += 1;





btn_decomp = tk.Button(wnd_main, text="Generate Project from Template");
btn_decomp["bg"] = c_blue2;
btn_decomp["fg"] = c_white;
btn_decomp["command"] = decompile;
btn_decomp.grid(row=row, column=0, pady=10);

btn_save = tk.Button(wnd_main, text="Save Config");
btn_save["bg"] = c_blue2;
btn_save["fg"] = c_white;
btn_save["command"] = save_config;
btn_save.grid(row=row, column=1, pady=10);





row += 1;
btn_dir = tk.Button(text="Open Project", command=browse_button)
btn_dir.grid(row=row, column=0, pady=10);
btn_dir["bg"] = c_blue2;
btn_dir["fg"] = c_white;

btn_dir = tk.Button(text="Backup ROM", command=backup)
btn_dir.grid(row=row, column=1, pady=10);
btn_dir["bg"] = c_blue2;
btn_dir["fg"] = c_white;

row += 1;
btn_dir = tk.Button(text="Open Unit Maker", command=open_umaker)
btn_dir.grid(row=row, column=0);
btn_dir["bg"] = c_blue2;
btn_dir["fg"] = c_white;

row += 1;

btn_dir = tk.Button(text="Open Patcher", command=open_patcher)
btn_dir.grid(row=row, column=0);
btn_dir["bg"] = c_blue2;
btn_dir["fg"] = c_white;

btn_comp = tk.Button(wnd_main, text="Compile Project");
btn_comp["bg"] = c_green;
btn_comp["fg"] = c_black;
btn_comp["command"] = project_compile;
btn_comp.grid(row=row, column=1, pady=10);




console = ConsoleText(wnd_main)
pos(console, 0, 1);

sys.stdout = console
sys.stderr = console


row += 1;




def load_config():
    if exists("resource/data/save.txt"):
        with open("resource/data/save.txt", "r+") as file:
            def read():
                return file.readline()[:-1];
            cp.base_rom = read();
            lbl_load_rom["text"] = "" + cp.base_rom;
            
            cp.directory = read();
            lbl_load_dir["text"] = "" + cp.directory;
            
            cp.name = read();
            txt_pname.insert(tk.INSERT, cp.name);
        return True;
    else:
        return False;
            
if load_config():
    
    print("Loaded Project \"" + cp.name + "\".");
    print("Directory: " + cp.directory);
    print("Base ROM: " + cp.base_rom);
    print("\n" + day_msgs[rng(0, len(day_msgs)-1)] + "\n");
else:
    print("Welcome!\nThis is the Basilisk FE1 editor\ncreated by Polinym.\nPlease see the included README\nfile for instructions.\nHave fun making the FE1\nof your dreams!");

wnd_main.mainloop();