def insertion_sort(v):
  for i in range(1, len(v)):
    x = v[i]
    j = i-1
    while j >= 0 and x < v[j]:
      v[j+1] = v[j]
      j -= 1
    v[j+1] = x
  return v

l = [5, 4, 6, 8, 1, 3, 10, 84, 13, 1, 8, 3]
print(insertion_sort(l))
