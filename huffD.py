import pickle
import sys

def decode(code, data):
    i, j = 0, 1
    message = ""
    while j <= len(data):
        sub = data[i:j]
        if (code.get(sub) is not None):
            message += code[sub]
            i = j
        j += 1

    return message

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Incorrect number of arguments. Input: python huffD.py filename")

    else:
        filename = sys.argv[1]
        try:
            my_file = open(filename, 'rb')
            data = my_file.read()
        except FileNotFoundError:
            print("No file found with name: ", filename)
            print("Ensure correct arguments. Input: python huffD.py filename")

        with open('huffman_code.pkl', 'rb') as f:
            code = pickle.load(f)

        nums = list(bytearray(data))

        vals = []
        for num in nums:
            vals.append('{0:08b}'.format(num))

        data = "".join(vals)

        inv_code = {v: k for k, v in code.items()}

        message = decode(inv_code, data)

        with open(filename+'.txt', 'w') as f:
            f.write(message)
