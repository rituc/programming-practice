def magic_index(a):
  for i in range(len(a)):
    if i == a[i]:
     return i

  return -1

a = [1,2,3,5,5,5,6,6]

print magic_index(a)

def magic_index2(a):
 start = 0
 end = len(a) -1
 mid = start+(end-start)/2
 while(start<end):
  if a[mid] == mid:
   return mid
  elif a[mid] > mid:
   end = mid - 1
  else:
   start = mid+1

print magic_index2(a)

