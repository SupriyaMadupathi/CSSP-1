def collectAllurl(data):
    text = data.split("</div>")
    strattag = "<img "
    endtag = "\""
    list1 = []
    for k in text:
        list1.append(k)
    for i in list1:
        if strattag in i:
            val = i.index(strattag)
            i = i[val +len(strattag)+5 :]
            end = i.index(endtag)
            print(i[:end])
    

def getAllcolors(data):
    text = data.split("\n")
    start = "background-color:"
    end = ";"
    list2 = []
    for k in text:
        list2.append(k)
    for i in list2:
        if start in i:
            # l1 = []
            val1 = i.index(start)
            i = i[val1 +len(start) :]
            tail = i.index(end)
            # new = i[:tail]
            # l1.append(new)
            # print(i[:tail])
def main():
    data = open("webpage5.html", encoding="utf8").read()
    #print(data)
    collectAllurl(data)
    getAllcolors(data)

if __name__ == '__main__':
    main()