count = 0
for i in range(1, 101):
 if i % 5 == 0 or i % 7 == 0:
  print(i, end=" ")
  count += 1
print("\nCount = ", count)