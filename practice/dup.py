def main():
 arr = [2,2,2,3,4,4,5,5]
 dup = set(arr)
 #print(dup)
 res ={}
 for i in dup:
  res = arr.count(i)
  #print(arr.count(i))
  print(i , res)
if__name__="__main__";
main()