import pickle
import sys

def encode(code, data):
    value = ""
    i = 0
    while i < len(data):
        if i == (len(data) - 1):
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
        print("Incorrect number of arguments. Input: python digr1024C.py filename")

    else:
        filename = sys.argv[1]
        try:
            my_file = open(filename, 'r', encoding="utf8")
            data = my_file.read()
        except FileNotFoundError:
            print("No file found with name: ", filename)
            print("Ensure correct arguments. Input: python digr1024C.py filename")

        with open('digram_code1024.pkl', 'rb') as f:
            code = pickle.load(f)

        value = encode(code, data)
        vals = str_to_list(value)

        with open(filename+'.digr1024', 'wb') as f:
            f.write(bytearray(vals))