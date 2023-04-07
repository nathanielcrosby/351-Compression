import pickle
import sys
import math

ascii_printable = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!"#$%&()*+,-./:;<>=?@[]\^_`}{|~ ' + "'" + "\n" + "\t"
utf_chars = {'‐':'-' ,"’":"'" , "‘":"'" , '”':'"' , '“':'"' , '—':'-', 'ñ':'n', 'é':'e', 'Á':'A', 'à': 'a', 'è':'e', 'ü':'u', 'á':'a', 'ê':'e', 'ä':'a', 
             'ó': 'o', 'û':'u', 'ú':'u', 'Ñ':'N', 'â':'a', 'À':'A', 'ï':'i', 'ô':'o', 'Ú':'U', 'í':'i', 'æ':'a', 'œ':'o', 'Æ':'A', 'î':'i', 'ç':'c', 'ë':'e', 
             'ù':'u', 'É':'E', 'Ç':'C', 'Ü':'U', 'È':'E', 'ö':'o', 'ā':'a', 'ò':'o', 'ο':'o'}

def read_text(files):
    all_text = ""
    for file in files:
        try:
            all_text += open(file,'r', encoding="utf8").read()
        except FileNotFoundError:
            print("No file found with name: ", file)
            print("Ensure correct arguments. Input: python digrCode.py size file1 file2 ...")

    return all_text


def find_digrams(text):
    ascii = {}
    for ch in ascii_printable:
        ascii[ch] = ch

    digram_count = {}

    for i in range(len(text) - 1):
        left = ascii.get(text[i])
        right = ascii.get(text[i+1])
        if (left is None):
            left = utf_chars.get(text[i])
        if (right is None):
            right = utf_chars.get(text[i+1])

        if (left is not None) and (right is not None):
            if digram_count.get(left+right) is None:
                digram_count[left+right] = 1
            else:
                digram_count[left+right] += 1


    sorted_digrams = dict_sort(digram_count)
    sorted_digrams.reverse()

    return sorted_digrams


# https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/
def dict_sort(dict):
    sorted_tuples = sorted(dict.items(), key=lambda item: item[1])
    sorted_dict = [k[0] for k in sorted_tuples]
    return sorted_dict

def Digram(freqs, size):
    len_code = math.ceil(math.log2(size))
    code = {}
    for i in range(len(ascii_printable)):
        code[ascii_printable[i]] = str(format(i, 'b')).zfill(len_code)
    for i in range(len(ascii_printable), size, 1):
        code[freqs[i-len(ascii_printable)]] = str(format(i, 'b')).zfill(len_code)

    return code
    

def can_cast(val):
    try:
        new_val = int(val)
    except ValueError:
        print("Size value must be an integer greater than 95. Input: python digrCode.py size file1 file2 ...")


if __name__ == "__main__":
    if(len(sys.argv) < 3):
        print("Incorrect number of arguments. Input: python digrCode.py size file1 file2 ...")
    elif (can_cast(sys.argv[1])) or (int(sys.argv[1]) < 96):
        print("Incorrect Dictionary size. Ensure size is an int greater than 95. Input: python digrCode.py size file1 file2 ...")
    else:
        size = int(sys.argv[1])
        text = read_text(sys.argv[2:])
        freqs = find_digrams(text)
        
        code = Digram(freqs, size)

        with open('digram_code'+str(size)+'.pkl', 'wb') as f:
            pickle.dump(code, f)
    