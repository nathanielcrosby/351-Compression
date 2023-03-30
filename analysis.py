import os
import sys
import time
from tabulate import tabulate

def filter_dir(dir_list):
    new_list = []
    for file in dir_list:
        if not ("all_concatenated_books" in file or  "total" in file or "Z" in file or "huff" in file or "digr" in file):
            new_list.append(file)
    return new_list 

def write_data_to_file(filename):
    dir_list = os.listdir(os.getcwd() + "/books/")
    dir_list = filter_dir(dir_list)
    #print(dir_list)

    books = ["./books/" + book for book in dir_list]
    algorithms = ["huff", "digr256", "digr512", "digr1024", "Z"]
    code_algorithms = algorithms[0:4]
    
    for code_algorithm in code_algorithms:
        if code_algorithm == "huff":
            cmd = "python " + code_algorithm + "Code.py" + " " + "./books/all_concatenated_books.txt"
            os.system(cmd)
        else:
            size = code_algorithm[4:len(code_algorithm)]
            cmd = "python " + code_algorithm[0:4] + "Code.py" + " " + size + " " + "./books/all_concatenated_books.txt"
            os.system(cmd)

    with open(filename, 'w') as f:
        f.write("")
        
    for algorithm in algorithms:
        with open(filename, 'a') as f:
            f.write(algorithm + ":" + "\n")
        for book in books:
            with open(filename, 'a') as f:
                f.write(book[8:len(book)] + ":" + "\n")

            cmd="python " + algorithm + "C.py" + " " + book
            start_time = time.time()
            os.system(cmd)
            end_time=time.time()
            compression_time=str(end_time - start_time)
            with open(filename, 'a') as f:
                f.write("Compression time: " + compression_time + " " + "seconds" "\n")

            compressed_file_size = os.path.getsize(book + '.' + algorithm)
            original_file_size = os.path.getsize(book)
            compression_ratio = float(compressed_file_size)/original_file_size

            with open(filename, 'a') as f:
                f.write("Compressed file size: " + str(compressed_file_size) + " " + "bytes" + "\n")
                f.write("Original file size: " + str(original_file_size) + " " + "bytes" + "\n")
                f.write("Compression Ratio: " + str(compression_ratio) + "\n")

            cmd="python " + algorithm + "D.py" + " " + book + "." + algorithm
            start_time = time.time()
            os.system(cmd)
            end_time=time.time()
            decompression_time=str(end_time - start_time)
            with open(filename, 'a') as f:
                f.write("Decompression time: " + decompression_time + " " + "seconds" "\n")
            
            with open(filename, 'a') as f:
                f.write("\n")
            
        with open(filename, 'a') as f:
            f.write("\n\n")

def write_data_in_latex(filename):
    dir_list = os.listdir(os.getcwd() + "/books/")
    dir_list = filter_dir(dir_list)
    #print(dir_list)

    books = ["./books/" + book for book in dir_list]
    algorithms = ["huff", "digr256", "digr512", "digr1024", "Z"]
    code_algorithms = algorithms[0:4]

    compression_ratio_data = [[""] + algorithms]
    compression_time_data =  [[""] + algorithms]
    decompression_time_data =  [[""] + algorithms]
    
    for code_algorithm in code_algorithms:
        if code_algorithm == "huff":
            cmd = "python " + code_algorithm + "Code.py" + " " + "./books/all_concatenated_books.txt"
            os.system(cmd)
        else:
            size = code_algorithm[4:len(code_algorithm)]
            cmd = "python " + code_algorithm[0:4] + "Code.py" + " " + size + " " + "./books/all_concatenated_books.txt"
            os.system(cmd)
    
    for book in books:
        compression_ratio_row = [book[8:len(book) - 4]]
        compression_time_row = [book[8:len(book) - 4]]
        decompression_time_row = [book[8:len(book) - 4]]

        for algorithm in algorithms:
            cmd="python " + algorithm + "C.py" + " " + book
            start_time = time.time()
            os.system(cmd)
            end_time=time.time()
            compression_time=str(end_time - start_time)

            compression_time_row.append(compression_time)


            compressed_file_size = os.path.getsize(book + '.' + algorithm)
            original_file_size = os.path.getsize(book)
            compression_ratio = float(compressed_file_size)/original_file_size

            compression_ratio_row.append(compression_ratio)

            cmd="python " + algorithm + "D.py" + " " + book + "." + algorithm
            start_time = time.time()
            os.system(cmd)
            end_time=time.time()
            decompression_time=str(end_time - start_time)

            decompression_time_row.append(decompression_time)

        compression_ratio_data.append(compression_ratio_row)
        compression_time_data.append(compression_time_row)
        decompression_time_data.append(decompression_time_row)
    
    compression_ratio_table = tabulate(compression_ratio_data, tablefmt="latex")
    compression_time_table = tabulate(compression_time_data, tablefmt="latex")
    decompression_time_table = tabulate(decompression_time_data, tablefmt="latex")

    with open(filename, 'w') as f:
        f.write("Compression Ratio Table:\n")
        f.write(compression_ratio_table + "\n\n")

        f.write("Compression Time Table:\n")
        f.write(compression_time_table + "\n\n")

        f.write("Decompression Time Table:\n")
        f.write(decompression_time_table + "\n\n")

    
if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Incorrect number of arguments. Input: python analysis.py filename")
    else:
        filename = sys.argv[1]
        try:
            my_file = open(filename, 'r', encoding="utf8")
            data = my_file.read()
        except FileNotFoundError:
            print("No file found with name: ", filename)
            print("Ensure correct arguments. Input: python anaylsis.py filename")
        
        # write_data_to_file(filename)
        write_data_in_latex(filename)
