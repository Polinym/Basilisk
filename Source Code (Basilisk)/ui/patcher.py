import tkinter as tk
from tkinter import messagebox
from os import listdir;
from ips_util import Patch as IPS;


def set_text(arg_entry, arg_txt):
    arg_entry["state"] = "normal";
    arg_entry.delete("1.0", "end");
    arg_entry.insert("1.0", arg_txt);
    arg_entry["state"] = "disabled";

class Patcher:
    def __init__(self, arg_rom, arg_path_patch):
        wnd = tk.Toplevel();
        self.wnd = wnd;
        self.wnd.title("Patcher");
        self.wnd.geometry("600x450+64+64");
        self.rom = arg_rom;
        self.path = arg_path_patch;
        
        self.patch_files = [];
        self.text_files = [];
        self.load_files();
        self.patches = [];
        self.name_ref = [];
        
        self.current_patch = False;

        tmp_row = 0;
        self.entries = tk.Listbox(wnd, width=40, height=10)
        self.entries.grid(row=tmp_row, column=0, columnspan=2, padx=8,pady=6);
        self.entries.bind('<<ListboxSelect>>', self.select_patch);
        
        tmp_row += 1;
        
        self.lbl_name = tk.Label(wnd, text="Patch Name:");
        self.lbl_name.grid(row=tmp_row, column=0, columnspan=1, padx=8,pady=6);
        self.txt_name = tk.Text(wnd, width=32, height=1, state="disabled");
        self.txt_name.grid(row=tmp_row, column=1, columnspan=1, padx=8,pady=6);
        
        tmp_row += 1;
        
        self.lbl_name = tk.Label(wnd, text="Description:");
        self.lbl_name.grid(row=tmp_row, column=0, columnspan=1, padx=8,pady=6);
        self.txt_desc = tk.Text(wnd, width=48, height=4, state="disabled", wrap=tk.WORD);
        self.txt_desc.grid(row=tmp_row, column=1, columnspan=2, padx=8,pady=6);
        
        tmp_row += 1;
        
        self.lbl_name = tk.Label(wnd, text="Credit:");
        self.lbl_name.grid(row=tmp_row, column=0, columnspan=1, padx=8,pady=6);
        self.txt_cred = tk.Text(wnd, width=64, height=2, state="disabled");
        self.txt_cred.grid(row=tmp_row, column=1, columnspan=2, padx=8,pady=6);
        
        tmp_row += 1;
        
        self.txt_warn = tk.Text(wnd, width=40, height=5, wrap=tk.WORD);
        self.txt_warn.grid(row=tmp_row, column=1, columnspan=2, padx=8,pady=6);
        set_text(self.txt_warn, "Warning!\n It's highly reccommended that you BACK UP YOUR PROJECT'S ROM first by pressing \"Backup ROM\"!\n Patches cannot be un-applied!");
        self.txt_warn.tag_configure('center', justify='center');
        self.txt_warn.tag_add('center', '1.0', 'end');
        self.txt_warn.tag_configure("red", foreground="red");
        self.txt_warn.tag_add("red", "1.0", "1.end");
        
        tmp_row += 1;

        self.patch_button = tk.Button(wnd, text="Apply Patch", command=self.apply_patch)
        self.patch_button.grid(row=tmp_row, column=1, columnspan=1, padx=8,pady=6);

        self.load_patches();

    def load_patches(self):
        #sample_data = [("Item 1", "Description 1"), ("Item 2", "Description 2"), ("Item 3", "Description 3")];
        #for item in sample_data:
        #    self.entries.insert(tk.END, item[0]);
        patches = [];
        name_ref = [];
        for fname in self.patch_files:
            patch = {};
            patch["file"] = fname;
            with open(self.path + "/" + fname + ".txt") as file:
                for line in file:
                    if (line[:-1] == "\n"):
                        line = line[:-1];
                    vals = line.split(":", 1);
                    if (vals):
                        patch[vals[0]] = vals[1][1:];
            patches.append(patch);
            name_ref.append(patch);
        self.patches = patches;
        
        for i in range(len(name_ref)):
            patch = name_ref[i];
            self.entries.insert(tk.END, patch["Name"]);
        self.name_ref = name_ref;
                
    def select_patch(self, e):
        index = self.entries.curselection();
        if (index):
            patch = self.name_ref[index[0]];
            set_text(self.txt_name, patch["Name"]);
            set_text(self.txt_desc, patch["Desc"]);
            set_text(self.txt_cred, patch["Credit"]);
            self.current_patch = patch;
        else:
            set_text(self.txt_name, "");
            set_text(self.txt_desc, "");
            set_text(self.txt_cred, "");
            self.current_patch = False;

    def apply_patch(self):
        patch = self.current_patch;
        if (patch):
            rom = self.rom;
            patch_file = self.path + "/" + patch["file"] + ".ips";
            apply_ips_patch(rom, patch_file);
            txt = "Success! Applied patch \"" + patch["Name"] + "\" to ROM \"" + rom + ".";
            messagebox.showinfo("Patch Successful", txt);
        else:
            messagebox.showwarning("Error!", "Select a patch to apply first!");
        #messagebox.showinfo("Entry Patched", f"Updated entry to: {name} - {desc}");
        #messagebox.showwarning("No selection", "Please select an entry first.")
        
    def load_files(self):
        ips_files = [];
        
        for filename in listdir(self.path):
            if filename.endswith('.ips'):
                ips_files.append(filename[:-4]);
        self.patch_files = ips_files;

def apply_ips_patch(arg_rom, arg_ips):
    patch = IPS.load(arg_ips);
    with open(arg_rom, 'rb+') as f_in:
        with open(arg_rom, 'rb+') as f_out:
            f_out.write(patch.apply(f_in.read()))
        



