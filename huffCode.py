ascii_printable = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!"#$%&()*+,-./:;<>=?@[]\^_`}{|~ ' + "'"


def read_text(files):
    all_text = ""
    for file in files:
        all_text += open(file,'r').read()

    return all_text

def find_freq(text):
    counts = {}
    total = 0
    for char in ascii_printable:
        counts[char] = 0

    for char in text:
        if(counts.get(char) is not None):
            #print(char)
            counts[char] += 1
            total += 1

    final_count = {}
    for key in list(counts.keys()):
        if counts[key] > 0:
            final_count[key] = counts[key] / total

    return final_count


if __name__ == "__main__":
    text = read_text(['books/ulysses.txt'])
    #print(ascii_printable)
    #print(len(ascii_printable))

    #print(text)
    print(find_freq(text))