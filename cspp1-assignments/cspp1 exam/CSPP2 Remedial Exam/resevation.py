def main():
    data = int(input())
    dic = {}
    i = 0
    capacity = 5
    count = 0
    while i < data:
        # print(i)
        data1 = input().split(" ")
        # print(data1[0])

        if data1[0] == "reserve":
            if len(dic) == capacity:
                print("All Rooms are reserved")
            elif dic == {}:
                dic[1] = data1[1]
                # print("hi")
                print(data1[1], 1)
                # count += 1
            else:
                for  j in range(1, capacity+1):
                    if  j not in dic.keys():
                        # if j == capacity - 1:
                            # break
                        dic[j] = data1[1]
                        # count += 1
                        print(data1[1], j)
                        break
                    # print(len(data1))
                # print(count)
            # count += 1
            # print(count)
        if data1[0] == "reserveN":
            if len(dic) == capacity:
            # print(len(dic))
            # if len(dic) >= 6:
                # print(len(dic))
                print("All Rooms are reserved")
            elif int(data1[2]) in dic.keys():
                print("Room is already reserved")
            else:
                dic[int(data1[2])] = data1[1]
                # count += 1
                print(data1[1], data1[2])
        if data1[0] == "build":
            capacity += int(data1[1])
            print("Added" + " " + data1[1] + " " + "more rooms")
        if data1[0] == "print":
            for x in sorted(dic):
                print(dic[x], x)
        if data1[0] == "cancel":
            dic2 = dic.copy()
            for k,v in dic2.items():
                if v == data1[1]:
                    dic.pop(k)
            print(data1[1], "now has no reserva2tions.")

            
    # for a in dic:
        # print(dic[a], a)
        i += 1
    # print(dic)

    # sort = sorted(dic)
    # print(sort)

        

if __name__ == '__main__':
    main()