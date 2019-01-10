li = []
def loadquestions(data):
    print("|----------------|")
    print("| Load Questions |")
    print("|----------------|")
    inp = int(data[1])
    # print(inp)
    for i in range(0, inp):
        li.append(input().split(":"))
    if inp >= 1:
        print(inp, "are added to the quiz")
    else:
        print("Quiz does not have questions")

def startquiz(data):
    # li = []
    print("|------------|")
    print("| Start Quiz |")
    print("|------------|")
    # print("hi")
    inp1 = int(data[1])
    for x in li:
        # print("hooo")
        ans = input().split(" ")
        x.append(ans[1])
        print(x[0]+"("+ x[3]+")")
        choice = x[1].split(",")
        print(choice[0] + "\t"+choice[1]+"\t"+choice[2]+"\t"+choice[3]+ "\n")

    # print(inp1)
def score(data):
    print("|--------------|")
    print("| Score Report |")
    print("|--------------|")
    summ = 0
    for i in li:
        print(i[0])
        if i[2]== i[5]:
            print(" Correct Answer! - Marks Awarded:", i[3])
            summ = summ+int(i[3])
            # print(summ)
        else:
            print(" Wrong Answer! - Penalty:", i[4])
            summ = summ + int(i[4])
    print("Total Score:", summ)


    pass

def main():
        while True:
            try:
                # data = input()
                # if data:
                data = input().split()
                if data[0] == "LOAD_QUESTIONS":
                    loadquestions(data)
                if data[0] == "START_QUIZ":
                    startquiz(data)
                if data[0] == "SCORE_REPORT":
                    score(data)
            except EOFError:
                break
    # q = int(data[1])
    # loadquestions(data)
    # print(type(q))
    # print(data)
    # if data[0] == "LOAD_QUESTIONS":
        # print("|----------------|")
        # print("| Load Questions |")
        # print("|----------------|")




if __name__ == '__main__':
    main()