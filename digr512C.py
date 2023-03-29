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
    for i in range(0, len(value), 9):
        if (i < (len(value) - 8)):
            vals.append(int(value[i:i+9], 2))
        else:
            vals.append(int(value[i:], 2) * (2 ** (9 - (len(value) % 9))))

    return vals

def split_vals_in_list(vals):
    new_vals = []
    for num in vals:     
        a = num % 256
        new_vals.append(a)
        b = num - a
        new_vals.append(b % 255)
        new_vals.append(b - (b % 255))

    return new_vals

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
        new_vals = split_vals_in_list(vals)


        with open(filename+'.digr512', 'wb') as f:
            f.write(bytearray(new_vals))