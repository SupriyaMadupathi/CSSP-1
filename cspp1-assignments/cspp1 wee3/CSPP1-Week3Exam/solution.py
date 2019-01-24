def main():
    n = int(input())
    # print(n)
    d = {}
    d2 = {}
    for i in range(n):
        data = input().split("|")
        if data[4] == "a":
            print("Invalid Points")
            # break

        else:
            if data[0] not in d:
                d[data[0]] = int(data[4])
                d2[data[0]] = 0
            else:
                d[data[0]] += int(data[4])
            if data[2] == data[3]:
                d2[data[0]] += int(data[4])
            else:
                d2[data[0]] -= int(data[4])
    # print(d)
    # for x in range(n):
    #   if data[0] not in d2:
    # print(d2)
    for id1 in sorted(d):
        for id2 in d2:
            # print(type(id1))
            if id1 == id2:
                result = int((int(d2[id1])/ int(d[id2]))*100)
                if result < 0:
                    result = 0.0
        print(id1+": "+str(float(result))+"%" )



if __name__ == '__main__':
    main()
