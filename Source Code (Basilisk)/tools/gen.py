bank_size = 0x4000;

def do_nothing():
    return -1;

def convert_ptrstr(ptr_str, to_type):
    if (to_type == "address"):
        byte1 = ptr_str[0:2];
        byte2 = ptr_str[2:4];
        byte = int(byte2 + byte1, 16);
        if (byte < 0xfff0):
            byte += 0x10;
        else:
            bit = byte1[3:4];
            byte = int("000" + bit);
    elif (to_type == "stored"):
        byte1 = ptr_str[0:2];
        byte2 = ptr_str[2:4];
        byte = int(byte2 + byte1, 16);
        if (byte > 0x0fff):
            byte += -0x1000;
        else:
            bit = byte2[1:2]; 
            byte1 = hex_format(int(byte1, 16) - 0x1);
            byte = int("f" + bit + byte1, 16);
    return byte;

def hex_format(arg_val):
    tmp = hex(arg_val)[2:];
    if ((len(tmp) % 2) != 0):
        tmp = "0" + tmp;
    return tmp;

def hex_format2(arg_val):
    tmp = hex(arg_val)[2:];
    for i in range(0, 4 - len(tmp)):
        tmp = "0" + tmp;
    return tmp;

def hex_format3(arg_val):
    tmp = hex(arg_val)[2:];
    for i in range(0, 6 - len(tmp)):
        tmp = "0" + tmp;
    return tmp;

def abs_to_ptr(arg_val):
    if (arg_val > 0x3c00f):
        return arg_val - 0x30010;
    else:
        while (arg_val > 0xc00f):
            arg_val += -0x4000;
        return arg_val;
    
def local_adr_str(arg_pos):
    return hex_format2(abs_to_ptr(arg_pos));

def get_bank(arg_adr):
    adr = arg_adr; 
    threshold = bank_size;
    bank_index = 0x0;
    while (adr < threshold):
        threshold += bank_size;
        bank_index += 1;
    return bank_index;