print("받고싶은 염기서열 txt를 입력하세요.")
fpath = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

dnaseq = ''
for line in open(fpath):
    dnaseq += line.rstrip().upper() #txt파일에 소문자가 있을 경우 대문자로 변

flag = 0
cnt = 0
finding = input("세고 싶은 염기 입력(A,T,G,C) : ")

for i in range(0, len(dnaseq)):
    nt = dnaseq[i]

    if nt == finding:
        if flag == 0:
            flag = 1
            cnt = 1
        else:
            cnt += 1
    else:
        if flag == 1 :
            print(cnt, end=' ')
            flag = 0

if flag == 1:
    print(cnt, end=' ')

print()

