import pickle
import sys
import time

def decode(code, data):
    message = ""
    for i in range(0, len(data), 8):
        message += code[data[i:i+8]]

    return message

if __name__ == '__main__':
    start = time.perf_counter()
    if(len(sys.argv) != 2):
        print("Incorrect number of arguments. Input: python digr256D.py filename")

    else:
        filename = sys.argv[1]
        try:
            my_file = open(filename, 'rb')
            data = my_file.read()
        except FileNotFoundError:
            print("No file found with name: ", filename)
            print("Ensure correct arguments. Input: python digr256D.py filename")

        with open('digram_code256.pkl', 'rb') as f:
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

        print(time.perf_counter() - start)