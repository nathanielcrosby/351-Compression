import pickle
import sys

def decode(code, data):
    message = ""
    for i in range(0, len(data), 10):
        message += code[data[i:i+10]]

    return message

def rejoin_vals(vals):
    new_vals = []
    for i in range(0, len(vals), 5):
        new_vals.append(vals[i] + vals[i + 1] + vals[i + 2] + vals[i + 3] + vals[i + 4])
    return new_vals

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Incorrect number of arguments. Input: python digr1024D.py filename")

    else:
        filename = sys.argv[1]
        try:
            my_file = open(filename, 'rb')
            data = my_file.read()
        except FileNotFoundError:
            print("No file found with name: ", filename)
            print("Ensure correct arguments. Input: python digr1024D.py filename")

        with open('digram_code1024.pkl', 'rb') as f:
            code = pickle.load(f)

        nums = rejoin_vals(list(bytearray(data)))

        vals = []
        for num in nums:
            vals.append('{0:010b}'.format(num))

        data = "".join(vals)

        inv_code = {v: k for k, v in code.items()}

        message = decode(inv_code, data)

        with open(filename+'.txt', 'w') as f:
            f.write(message)