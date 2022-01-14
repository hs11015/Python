import sys

length = 0
List = []

for line in open('.\seq.txt'):  #염기서열 List에 받기
    for x in line:
        if x == '\n':
            continue
        List.append(x)
        length += 1

count = 0

for i in range(0, len(List)):
    if List[i] == 'C':
        count += 1
    elif List[i] != 'C' and count != 0:
        print(count, end= ' ')
        count = 0

if count != 0:
    print(count, end=' ')

print()


