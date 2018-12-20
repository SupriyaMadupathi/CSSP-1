li_st = []
mat = []
for _ in range(int(input()) + 1):
            li = input().split(" ")
            li_st.append(li)
for i in range(len(li_st)):
        temp = []
        for j in range(len(li_st[i])):
                r = (int(li_st[i][j]) + 50) / 100
                temp.append(int(r * 100))
        mat.append(temp)
print(mat)

