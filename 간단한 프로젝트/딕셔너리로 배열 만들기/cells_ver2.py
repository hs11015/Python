tableM = {}
for row in range(1, 7):
    tableM[row] = {}
    for col in range(1, 5):
        tableM[row][col] = row * col

for row in range(1, 7):
    for col in range(1, 5):
        val = tableM[row][col]
        print(val, end='\t')
    print()
