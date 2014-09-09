text = ""

with open("sample_out.txt", "wt") as fout:
    with open("mdown.txt", "rt") as fin:
        for line in fin:
            for i in line:
                if i == "#":
                    tag = "h1"
                    fout.write(line.replace(line, ""))
                    text += "<" + tag + ">" + line + "</" + tag + ">"
                    line = text
                    fout.write(line.replace("#", ""))
            