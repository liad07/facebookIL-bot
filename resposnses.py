def sample_res(txt):
    print(txt)
    file = open("all.txt", "r", encoding="utf8")
    x = file.read().split("\n")
    b = ""
    for i in range(len(x)):
        if txt in x[i]:
            b = x[i].replace(",", "\n")
            print(b)
            return b
        if txt in x[i]:
            break
