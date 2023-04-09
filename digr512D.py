import pickle
import sys

def decode(code, data):
    message = []
    for i in range(0, len(data)-8, 9):
        message.append(code[data[i:i+9]])

    return "".join(message)

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Incorrect number of arguments. Input: python digr512D.py filename")

    else:
        filename = sys.argv[1]
        try:
            my_file = open(filename, 'rb')
            data = my_file.read()
        except FileNotFoundError:
            print("No file found with name: ", filename)
            print("Ensure correct arguments. Input: python digr512D.py filename")

        with open('digram_code512.pkl', 'rb') as f:
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