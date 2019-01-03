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
                # count += 1
            # if count > 5:
                            # print(len(d))
                # print("All Rooms are reserved")
                # break
            else:
                for  j in range(1, 7):
                    if  j not in dic.keys():
                        if j >= int(capacity):
                            print("All Rooms are reserved")
                            break
                        dic[j] = data1[1]
                        break
                    # print(len(data1))
                # print(count)
            # count += 1
            # print(count)
        if data1[0] == "reserveN":
            if len(dic) >= capacity:
                print("All Rooms are reserved")
            elif int(data1[2]) in dic.keys():
                print("Room is already reserved")
            else:
                dic[int(data1[2])] = data1[1]
                print(data1[1], data1[2])
        i += 1
    for a in dic:
        print(dic[a], a)
    # print(dic)
    for x in sorted(dic):
        print(dic[x], x)
    # sort = sorted(dic)
    # print(sort)

        

if __name__ == '__main__':
    main()