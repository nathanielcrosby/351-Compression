import pickle
import sys

utf_chars = {'‐':'-' ,"’":"'" , "‘":"'" , '”':'"' , '“':'"' , '—':'-', 'ñ':'n', 'é':'e', 'Á':'A', 'à': 'a', 'è':'e', 'ü':'u', 'á':'a', 'ê':'e', 'ä':'a', 
             'ó': 'o', 'û':'u', 'ú':'u', 'Ñ':'N', 'â':'a', 'À':'A', 'ï':'i', 'ô':'o', 'Ú':'U', 'í':'i', 'æ':'a', 'œ':'o', 'Æ':'A', 'î':'i', 'ç':'c', 'ë':'e', 
             'ù':'u', 'É':'E', 'Ç':'C', 'Ü':'U', 'È':'E', 'ö':'o', 'ā':'a', 'ò':'o', 'ο':'o'}

def encode(code, data):
    clean_data = ""
    for ch in data:
        if code.get(ch) is not None:
            clean_data += ch
        elif utf_chars.get(ch) is not None:
            clean_data += utf_chars[ch]
        else:
            clean_data += '?'
    data = clean_data

    value = ""
    i = 0
    while i < len(data):
        if (i == (len(data) - 1)) and (code.get(data[i]) is not None):
            value += code[data[i]]
            i += 1
        elif code.get(data[i:i+2]) is not None:
            value += code[data[i:i+2]]
            i += 2
        elif code.get(data[i]) is not None:
            value += code[data[i]]
            i += 1
        else:
            i += 1

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
        print("Incorrect number of arguments. Input: python digr512C.py filename")

    else:
        filename = sys.argv[1]
        try:
            my_file = open(filename, 'r', encoding="utf8")
            data = my_file.read()
        except FileNotFoundError:
            print("No file found with name: ", filename)
            print("Ensure correct arguments. Input: python digr512C.py filename")

        with open('digram_code512.pkl', 'rb') as f:
            code = pickle.load(f)

        value = encode(code, data)
        vals = str_to_list(value)

        with open(filename+'.digr512', 'wb') as f:
            f.write(bytearray(vals))
