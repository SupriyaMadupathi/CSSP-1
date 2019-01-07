def depth(data):
    c = 0
    s = " "
    li = []
    s = " ".join(str(x) for x in data)
    for i in range(len(s)):
        if s[i]=="[":
            c += 1
        if s[i] == "]":
            li.append(c)
    print(li)




    
    # for each in data:
    #     # for i in :
    #         if type(each) == type([]):
    #             c += 1
        # if each == "]":
            # li.append(c)
    # li.append(c)
    # print(c)
def count(data):
    c = 0
    s = " "
    s = " ".join(str(x) for x in data)
    for i in range(len(s)):
        if s[i]=="[":
            c += 1
    print(c)
def nested_sum(data):
    li = []
    li.append(data)
    summ = 0
    while li:
        item = li.pop()
        if isinstance(item, list):
            for x in item:
                # print(x)
                li.append(x)
        elif str != type(item):
            summ += item
        
    print(summ)

def main():
    data = eval(input())
    nested_sum(data)
    count(data)
    depth(data)
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