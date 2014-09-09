fout = open("sample_out.txt", "wt")
fin = open("mdown.txt", "rt")

def headers(line):
    if line[0:0] == "#":
        fout.write(line.replace(line[0:0], "<h1>"))
    
    
    
    
def main():
    for line in fin:
        headers(line)
    print "done"
    
    


if __name__ == "__main__":
    main()
