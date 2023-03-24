import pickle
import sys

def encode(code, data):
    value = ""
    for char in data:
        if code.get(char) is not None:
            value += code[char]

    return value

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Incorrect number of arguments. Input: python huffC.py filename")

    else:
        filename = sys.argv[1]
        try:
            my_file = open(filename, 'r', encoding="utf8")
            data = my_file.read()
        except FileNotFoundError:
            print("No file found with name: ", filename)
            print("Ensure correct arguments. Input: python huffC.py filename")

        with open('huffman_code.pkl', 'rb') as f:
            code = pickle.load(f)

        value = encode(code, data)

        vals = []
        for i in range(0, len(value), 8):
            if (i < (len(value) - 7)):
                vals.append(int(value[i:i+8], 2))
            else:
                vals.append(int(value[i:], 2) * (2 ** (8 - (len(value) % 8))))

        with open(filename+'.huff', 'wb') as f:
            f.write(bytearray(vals))