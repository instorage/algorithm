def quicksort(arr):
  # return 'quicksort'
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    final = quicksort(less) + [pivot] + quicksort(greater)
    return final

print quicksort([10,5,2,3])