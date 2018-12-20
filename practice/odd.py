def main():
  s = "1234567"
  l = len(s)
  il = l//2
  il2 = l/2
  even = ""
  odd = ""
  if l%2 == 0:
    for i in range(0,il,1):
      a = (l - 1) - i
      res = int(s[i]) + int(s[a])
      even = even + str(res)
  else:
    for i in range(0,il,1):
      a = (l - 1) - i
      ores = int(s[i]) + int(s[a])
      odd = odd + str(ores)
      odd = odd + s[round(il2)]
    print(odd)
    print(even)
if __name__ == '__main__':
  main()