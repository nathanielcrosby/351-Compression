import pickle
import sys

ascii_printable = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!"#$%&()*+,-./:;<>=?@[]\^_`}{|~ ' + "'" + "\n"

def encode(data):
    codes = {}
    counter = 0
    len_code = 9
    for char in ascii_printable:
        codes[char] = str(format(counter, 'b')).zfill(len_code)
        counter += 1

    ascii = codes.copy()

    clean_data = ""
    for ch in data:
        if codes.get(ch) is not None:
            clean_data += ch
    data = clean_data

    value = ""
    comp_ratio = 1

    i = 0
    while i < len(data):

        j = i+1
        while (j < len(data)) and (codes.get(data[i:j+1]) is not None):
            j += 1
        
        value += codes[data[i:j]].zfill(len_code) 
        
        if (counter < 2**16) and (j < len(data)):
            value += codes[data[j]].zfill(len_code)
            codes[data[i:j+1]] = str(format(counter, 'b')).zfill(len_code)

            comp_ratio = 0.001 * ((2 * len_code) / (8*len(data[i:j+1]))) + (0.999 * comp_ratio)

            if '0' not in str(format(counter, 'b')).zfill(len_code) and (len_code < 16):
                len_code += 1

            counter += 1
            i = j + 1

        else:
            comp_ratio = 0.001 * ((len_code) / (8*len(data[i:j]))) + (0.999 * comp_ratio)
            i=j
            
            if (comp_ratio > 0.8):
                codes = ascii.copy()
                counter = len(ascii_printable)
                len_code = 9

    return value


def str_to_list(value):
    vals = []
    for i in range(0, len(value), 8):
        if (i < (len(value) - 7)):
            vals.append(int(value[i:i+8], 2))
        else:
            vals.append(int(value[i:], 2) * (2 ** (8 - (len(value) % 8))))

    return vals


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Incorrect number of arguments. Input: python ZC.py filename")

    else:
        filename = sys.argv[1]
        try:
            my_file = open(filename, 'r', encoding="utf8")
            data = my_file.read()
        except FileNotFoundError:
            print("No file found with name: ", filename)
            print("Ensure correct arguments. Input: python ZC.py filename")

        value = encode(data)
        vals = str_to_list(value)

        with open(filename+'.Z', 'wb') as f:
            f.write(bytearray(vals))