print("받고싶은 염기서열 txt를 입력하세요.")
fpath = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

match = int(input("match하면 몇 점? [예) 2] : "))
mismatch = int(input("mismatch하면 몇 점? [예) -1] : "))
indel = int(input("둘 중 하나라도 비어있는 염기서열(-)이 있으면 몇 점? [예) 0] : "))

#print(match, mismatch, indel, fpath)

dic_seqs = {}
seq = ''
spc = ''
for line in open(fpath):
    if line[0] == '>':
        if len(seq) > 0:
            dic_seqs[spc] = seq

        spc = line.rstrip()[1:]
        seq = ''
    else:
        seq += line.rstrip().upper()

if len(seq) > 0:
    dic_seqs[spc] = seq

[seq1, seq2] = dic_seqs.values()

score = 0
for p in range(0, len(seq1)):
    nt1 = seq1[p]
    nt2 = seq2[p]
    if nt1 == '-' or nt2 == '-':
        score += indel
    elif nt1 == nt2:
        score += match
    else:
        score += mismatch

print("sum all score : ", score)
