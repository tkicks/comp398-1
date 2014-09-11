## global data
path = raw_input("Enter a path to an input file\n>> ")
#fin = open(path, "rt")
fout = open("readmeout.txt", "wt")
#searchfile = open(path, "r")




def htag(line):
    y = line[0:6]
    x = y.count("#")
    if x == 1:
        rline = line.translate(None, "#")
        newline = "<h1> " + rline.strip() + "</h1>\n"
        #fout.write(newline)
        ptag(newline)
        
    elif x == 2:
        rline = line.translate(None, "#")
        newline = "<h2>" + rline.strip() + "</h2>\n"
        #fout.write(newline)
        ptag(newline)
    
    elif x == 3:
        rline = line.translate(None, "#")
        newline = "<h3>" + rline.strip() + "</h3>\n"
        #fout.write(newline)
        ptag(newline)

    elif x == 4:
        rline = line.translate(None, "#")
        newline = "<h4>" + rline.strip() + "</h4>\n"
        #fout.write(newline) 
        ptag(newline)
    
    elif x == 5:
        rline = line.translate(None, "#")
        newline = "<h5>" + rline.strip() + "</h5>\n"
        #fout.write(newline) 
        ptag(newline)
        
    elif x == 6:
        rline = line.translate(None, "#")
        newline = "<h6>" + rline.strip() + "</h6>\n"
        #fout.write(newline) 
        ptag(newline)
    
    else:
        #fout.write(line)
        ptag(line)

def ptag(line):
    if len(line) > 1:
        if "\n" in line:
            newline = "<p>" + line.strip() + "</p>\n"
            quote(newline)
            #fout.write(newline)
        else:
            quote(line)
            
def quote(line):
    if line.count(">") % 2 == 1:
        if line.count(">") == 1:
            temp = line.translate(None, ">")
            newline = "<blockquote>" + temp.strip() + "</blockquote>\n"
            fout.write(newline)
        else:
            for i in range(0, len(line)):
                if list(line)[i] == list(line)[i-1]:
                    list(line).pop(i)
            newline = "<blockquote>" + line.strip() + "</blockquote>\n"
            fout.write(newline)
    else:
        fout.write(line)
    
        


def main():
    with open(path, "r") as fin:
        for line in fin:
            htag(line)
    fout.close()  







if __name__ == "__main__":
    main()
    
    