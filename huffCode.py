import pickle
import sys

ascii_printable = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!"#$%&()*+,-./:;<>=?@[]\^_`}{|~ ' + "'" + "\n" + "\t"


def read_text(files):
    all_text = ""
    for file in files:
        try:
            all_text += open(file,'r', encoding="utf8").read()
        except FileNotFoundError:
            print("No file found with name: ", file)
            print("Ensure correct arguments. Input: python huffCode.py file1 file2 ...")

    return all_text

def find_freq(text):
    counts = {}
    total = 0
    for char in ascii_printable:
        counts[char] = 0

    for char in text:
        if(counts.get(char) is not None):
            counts[char] += 1
            total += 1

    final_count = {}
    for key in list(counts.keys()):
        if counts[key] > 0:
            final_count[key] = counts[key] / total

    return final_count


# https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/
def dict_sort(dict):
    sorted_tuples = sorted(dict.items(), key=lambda item: item[1])
    sorted_dict = [k[0] for k in sorted_tuples]
    return sorted_dict

def Huffman(A, P, D=2):
    if (len(A) <= D):
        trivial_code = {}
        for i in range(D):
            trivial_code[A[i]] = str(i)
        return trivial_code
    
    m = 2
    A_sort = dict_sort(P)
    A_star = [(A_sort[0], A_sort[1])] + A_sort[2:]
    P_star = {}
    b_star = (A_sort[0], A_sort[1])
    P_star[b_star] = P[A_sort[0]]+P[A_sort[1]]
    
    for a in A_sort[2:]:
        P_star[a] = P[a]

    C_star = Huffman(A_star, P_star, D)

    C = {}
    for b in A_star[1:]:
        C[b] = C_star[b]
    for i in range(D):
        C[b_star[i]] = C_star[b_star] + str(i)

    return C


if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Incorrect number of arguments. Input: python huffCode.py file1 file2 ...")

    text = read_text(sys.argv[1:])
    freqs = find_freq(text)
    sorted_freqs = dict_sort(freqs)
    
    code = Huffman(sorted_freqs, freqs)

    with open('huffman_code.pkl', 'wb') as f:
        pickle.dump(code, f)
    