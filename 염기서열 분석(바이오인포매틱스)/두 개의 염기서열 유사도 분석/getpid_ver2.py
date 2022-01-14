print("받고싶은 염기서열 txt를 입력하세요.")
fpath = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

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

match = 0
total = 0
for p in range(0, len(seq1)):
    nt1 = seq1[p]
    nt2 = seq2[p]
    if nt1 == nt2:
        match += 1

    if nt1 != '-' and nt2 != '-':
        total += 1

pid = match/total
print(pid)
