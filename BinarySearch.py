import array

def BinarySearch(arr, min, max, n):
  mid = int((min + max)/2)
  print(mid, end = " ")
  if(min > max):
    return False
  if(arr[mid] == n):
    return True
  elif(arr[mid] > n):
    return(BinarySearch(arr, min, mid-1, n))
  else:
    return(BinarySearch(arr, mid+1, max, n))


def main():
  print("Binary Search Implementation")
  arr = array.array('i', [ 4,6,9,12,15,26,36,38,45,56,66,78,99,145,167,222,678])
  #search for 12
  if(BinarySearch(arr, 0, arr.__len__()-1, 12)):
    print("Element found")
  else:
    print("Element not found")

if (__name__ == "__main__"):
  main()