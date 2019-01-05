# 
def add_all(t):
    total = 0
    for i in t:
        if type(i) == list: # check whether i is list or not
            total = total + add_all(i)
        else:
            total += i
    return total

def main():
    data = eval(input())
    add_all(data)
    # summ = 0
    # li = []
    # x =list(sum(data, []))
    # print(x)
    # li.append(data)
    # for each in data:
    #     #
    #     for i1 in each:
    #         x =""
    #     #   # for i2 in i1:
    #         li.append(i1)
    #         for a in li:
    #             if type(x) != type(each):
    #                 summ += each
    #     #   # li.append(i1)
        #   for x in li:
        #       if y != type(x):
        #           summ += x

    # print(summ)
    # count = 0
    # for each in data:
    #     if list in each:
    #         print("hi")
    #         count += 1
        # print(count)


            

if __name__ == '__main__':
    main()