def max_index(arr,start,end):
  if start==end: return start
  k= max_index(arr,start+1,end)
  print(k)
  return start if arr[start]<arr[k] else k

def recursive_selection(arr,start=0):
  if start == len(arr)-1:
    return arr
  max_id = max_index(arr,start,end=len(arr)-1)
  # print(max_id)
  arr[start],arr[max_id]= arr[max_id],arr[start]
  return recursive_selection(arr,start+1)
  
recursive_selection([2,9,7])