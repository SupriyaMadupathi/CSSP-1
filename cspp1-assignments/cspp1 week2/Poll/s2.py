def count(x, option, options):
    # print(x)
    # print(option)
    # print(options)
    for i in range(len(options)):
        if i == x:
            if option in options[i]:
                options[i][option] += 1
                # print(options[i][option])
    return options



def main():
    num = int(input())
    # print(num)
    # quiz = Quiz()
    dic = {}
    for i in range(num):
        question = str(input())
        options = []
        for i in range(4):
            options.insert(i,str(input()))
        dic[question] = options
    # print(dic)
    options = []
    for key in dic:
        answers = {}
        for each in dic[key]:
            answers[each] = 0
        options.append(answers)
    # print(options)
    noofpart = int(input())
    for i in range(noofpart):
        partname = input()
        for i in range(num):
            string = input().split()
            print(string,"-----")
            options1 = count(int(string[0]) - 1, string[1], options)
    # print(options1)
    result = []
    for each in options1:
        maxnum = max(each.values())
        for each1 in each:
            if each[each1] == maxnum:
                result.append(each1)
    i = 0
    for key in dic:
        print("Highest number of votes for question : " + key + " : " + result[i])
        # print(result[i])
        i += 1
        if i == num:
            break


if __name__ == '__main__':
    main()