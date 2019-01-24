def check_response(data):
    total_score = 0
    scored = {}
    # print(scored)
    global flag
    flag = 0
    full_Score = {}
    for item in data:
        try:
            if int(item[4]) == type(int):
                print("OKOK")
        except ValueError:
            print("Invalid Points")
            flag = 1
            break
        if item[0] not in scored:
                full_Score[item[0]] = int(item[4])
                scored[item[0]] = 0
                # print(scored)
        else:
            full_Score[item[0]] += int(item[4])
        if item[2] == item[3]:
            scored[item[0]] += int(item[4])
        else:
            scored[item[0]] -= int(item[4])

    for got in sorted(scored):
        for total in sorted(full_Score):
            if flag == 0:
                if got == total:
                    final = int((scored[got]/full_Score[total]) * 100)
                    if final <= 0:
                        final = 0.0
                        print(got + ": " + str(final) + "%")
                    else:
                        print(got + ": " + str(float(final)) + "%")



def main():
    number = int(input())
    global questions
    questions = []
    for i in range(number):
        questions.append(input().split("|"))
    check_response(questions)

if __name__ == '__main__':
    main()
