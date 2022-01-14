print("받고싶은 염기서열 txt를 입력하세요.")
fpath = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

D = []
name = ''
seq = ''

for line in open(fpath):
    if line[0] == '>':
        if seq != '':
            D.append(name + ': ' + seq)
            seq = ''
        name = line[1:-1]
    else:
        seq += line.rstrip().upper()

if seq != '':
    D.append(name + ': ' + seq)

D.sort()    #1,2,3 등 Seq 순서 맞추기

def cnt_DNA_seq(x):
    A = 0
    C = 0
    G = 0
    T = 0
    start = 0

    for i in range(0, len(D[x])):
        print(D[x][i], end='')

        if D[x][i] == ':':
            start = 1
        elif D[x][i] == 'A' and start == 1:
            A += 1
        elif D[x][i] == 'C' and start == 1:
            C += 1
        elif D[x][i] == 'G' and start == 1:
            G += 1
        elif D[x][i] == 'T' and start == 1:
            T += 1

    print()
    print('A %d\n' %A, end='')
    print('C %d\n' %C, end='')
    print('G %d\n' %G, end='')
    print('T %d\n' %T, end='\n')


for j in range(0, len(D)):
    cnt_DNA_seq(j)
