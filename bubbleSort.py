def bubble_sort(v):
  for i in range(len(v)-1):
    for j in range(len(v)-i-1):
      if (v[j] > v[j+1]):
        v[j], v[j + 1] = v[j + 1], v[j]
  return v

l = [5, 4, 6, 8, 1, 3, 10, 84, 13, 1, 8, 3]
print(bubble_sort(l))
