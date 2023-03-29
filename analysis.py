import os
import time

def filter_dir(dir_list):
    new_list = []
    for file in dir_list:
        if not ("Z" in file or "huff" in file or "digr" in file):
            new_list.append(file)
    return new_list 

if __name__ == '__main__':
    dir_list = os.listdir(os.getcwd() + "/books/")
    dir_list = filter_dir(dir_list)
    #print(dir_list)

    books = ["./books/" + book for book in dir_list]
    algorithms = ["huff", "digr256", "digr512", "digr1024", "Z"]
    #algorithms = ["Z"]
        
    for algorithm in algorithms:
        with open("data.txt", 'a') as f:
            f.write(algorithm + ":" + "\n")
        for book in books:
            with open("data.txt", 'a') as f:
                f.write(book[8:len(book)] + ":" + "\n")
            if algorithm != "Z":
                if algorithm == "huff":
                    cmd = "python " + algorithm + "Code.py" + " " + book
                    os.system(cmd)
                else:
                    size = algorithm[4:len(algorithm)]
                    cmd = "python " + algorithm + "Code.py" + " " + size + " " + book
                    os.system(cmd)

            cmd="python " + algorithm + "C.py" + " " + book
            start_time = time.time()
            os.system(cmd)
            end_time=time.time()
            compression_time=str(end_time - start_time)
            with open("data.txt", 'a') as f:
                f.write("Compression time: " + compression_time + " " + "seconds" "\n")

            original_file_size = os.path.getsize(book)
            compressed_file_size = os.path.getsize(book + '.' + algorithm)
            compression_ratio = float(original_file_size)/compressed_file_size
            with open("data.txt", 'a') as f:
                f.write("Original file size (in terms of bytes): " + str(original_file_size) + "\n")
                f.write("Compressed file size (in terms of bytes): " + str(compressed_file_size) + "\n")
                f.write("Compression Ratio: " + str(compression_ratio) + "\n")

            cmd="python " + algorithm + "D.py" + " " + book + "." + algorithm
            start_time = time.time()
            os.system(cmd)
            end_time=time.time()
            decompression_time=str(end_time - start_time)
            with open("data.txt", 'a') as f:
                f.write("Decompression time: " + decompression_time + " " + "seconds" "\n")
            

            with open("data.txt", 'a') as f:
                f.write("\n")
            
        with open("data.txt", 'a') as f:
            f.write("\n\n\n")