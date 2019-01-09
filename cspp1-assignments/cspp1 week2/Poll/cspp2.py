from sys import stdin
from collections import Counter
# def questions(n):
# def participants(n):
def count(x, y, choice):
    # print(x)
    # print(y)
    # print(choice)
    for i in range(len(choice)):
        if i == x:
            if y in choice[i]:
                choice[i][y] += 1
    return choice


def main():
    n = int(input())
    # count = 0
    dic = {}
    for i in range(n):
        li = []
        # options = []
        question = input()
        # print(question)
        for j in range(4):
            # options = input()
            li.insert(j, str(input()))
            dic[question] = li
    # print(dic)
    li = []

        # for i in range(1, n+1):
    for keys in dic:
        ans  = {}
        for x in dic[keys]:
            ans[x] = 0
        li.append(ans)
    # print(li)   
    participants = int(input())
    # count = 0
    # dic2 = {}
    # survey = []
    for i in range(participants):
        name = input()
        # print(name)
        for x in range(n):
            data = input()
            survey = count(int(data[0]) - 1, data[1], li)
            # survey.append(data)

    res = []
    for each in survey:
        maximum = max(each.values())
        if x in each:
            if each[x] == maximum:
                res.append(x)
    # print(Counter(survey))
    i = 0
    for key in dic:
        print("Highest number of votes for question : " + key + " : " + res[i])
        # print(result[i])
        i += 1
        if i == n:
            break

    # print(dic2)
    


if __name__ == '__main__':
    main()