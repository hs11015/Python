print("받고싶은 염기서열 txt를 입력하세요.")
fpath = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

myseq = ''
for line in open(fpath):
    myseq += line.rstrip().upper()	#upper 써줌으로써 모두 대문자로 만듦

mydic = {}
for nt1 in 'ACGT':			#염기서열 dictionary화
    mydic[nt1] = {}
    for nt2 in 'ACGT':
        mydic[nt1][nt2] = 0

for i in range(len(myseq)-1):		#myseq 안에 들어있는 거 1개씩 읽어들이면서 숫자 늘림
    nt1 = myseq[i]
    nt2 = myseq[i+1]
    mydic[nt1][nt2] += 1

for nt1 in 'ACGT':
    for nt2 in 'ACGT':
        cnt = mydic[nt1][nt2]
        if cnt > 0:
            print(nt1, nt2, ' ', cnt, sep='')
