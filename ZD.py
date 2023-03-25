import pickle
import sys

ascii_printable = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!"#$%&()*+,-./:;<>=?@[]\^_`}{|~ ' + "'" + "\n"


def longer_codes(codes, len_code):
    new_code = {k.zfill(len_code): v for k, v in codes.items()}
    return new_code


def decode(data):
    message = ""
    codes = {}
    counter = 0
    len_code = 9

    for char in ascii_printable:
        codes[str(format(counter, 'b')).zfill(len_code)] = char
        counter += 1

    i = 0
    while i < (len(data) - len_code):
        left = codes[data[i:i+len_code]]
        message += left
        i += len_code

        if (i + len_code) <= len(data):
            right = codes[data[i:i+len_code]]
            message += right
            i += len_code

            if counter < 2**16:
                codes[str(format(counter, 'b')).zfill(len_code)] = left + right
                
                if ('0' not in str(format(counter, 'b')).zfill(len_code)) and (len_code < 16):
                    len_code += 1
                    codes = longer_codes(codes, len_code)

                counter += 1

    return message


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Incorrect number of arguments. Input: python ZD.py filename")

    else:
        filename = sys.argv[1]
        try:
            my_file = open(filename, 'rb')
            data = my_file.read()
        except FileNotFoundError:
            print("No file found with name: ", filename)
            print("Ensure correct arguments. Input: python ZD.py filename")

        nums = list(bytearray(data))

        vals = []
        for num in nums:
            vals.append('{0:08b}'.format(num))

        data = "".join(vals)
        message = decode(data)

        with open(filename+'.txt', 'w') as f:
            f.write(message)