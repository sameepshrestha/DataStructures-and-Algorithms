def mergesort(arr):
  if len(arr)<=1: return arr
  mid = len(arr)//2
  left = mergesort(arr[:mid])
  right = mergesort(arr[mid:])
  return merger(left,right) #havee to return the merger so that we have the right as the right as the sorted array


def merger(left, right):
  result=[]
  i,j =0,0
  # print(left,right)
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1
    # print(result)
  result+=left[i:]
  result+=right[j:]
  return result 
mergesort([2,5,1,7,9,4])