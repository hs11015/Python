print("받고 싶은 score pattern txt를 입력하세요.")
pat_f = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

print("받고싶은 염기서열 txt를 입력하세요.")
seq_f = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

cutoff = float(input("최소 점수(cutoff)를 정해주세요 : "))

print('Pattern file:', pat_f)
print('Sequence file:', seq_f)
print('Cutoff:', cutoff)

# Reading sequence file
seq = ''
for line in open(seq_f):
    if line[0] == '>':
        continue
    seq += line.rstrip().upper()
print(seq)

# Reading pattern file
pat = {}
p = 0
for line in open(pat_f):
    prob = line.rstrip().split()
    pat[p] = {}
    for (i, nt) in list(enumerate('ACGT')):
        pat[p][nt] = float(prob[i])
    p += 1

psize = p
for p in range(0, psize):
    for nt in 'ACGT':
        val = pat[p][nt]
        print(val, '\t', sep='', end='')
    print()

# Traversing sequence
for i in range(0, len(seq) - (psize-1)):
    score = 1
    for j in range(0, psize):
        nt = seq[i + j]
        score *= pat[j][nt]

    if score >= cutoff:
        print(i + 1, score)
