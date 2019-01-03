def main():
    data = int(input())
    dic = {}
    i = 0
    capacity = 6
    # count = 1
    while i < data:
        # print(i)
        data1 = input().split(" ")
        # print(data1[0])

        if data1[0] == "reserve":
            if dic == {}:
                dic[1] = data1[1]
                print(data1[1], 1)
                # count += 1
            else:
                for  j in range(1, 6):
                    if  j not in dic.keys():
                        if j > 6:
                            print("All Rooms are reserved")
                            break
                        dic[j] = data1[1]
                        break
                    # print(len(data1))
                # print(count)
            # count += 1
            # print(count)
        if data1[0] == "reserveN":
            if len(dic) >= 6:
                print("All Rooms are reserved")
            elif int(data1[2]) in dic.keys():
                print("Room is already reserved")
            else:
                dic[int(data1[2])] = data1[1]
                # print(data1[1], data1[2])
        if data1[0] == "build":
            capacity += int(data1[1])
            print("Added" + " " + data1[1] + " " + "more rooms")
        if data1[0] == "print":
            for x in sorted(dic):
                print(dic[x], x)
            
        i += 1
    # for a in dic:
        # print(dic[a], a)
    # print(dic)

    # sort = sorted(dic)
    # print(sort)

        

if __name__ == '__main__':
    main()