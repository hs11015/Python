print("받고 싶은 score pattern txt를 입력하세요.")
pat_f = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

print("받고싶은 염기서열 txt를 입력하세요.")
seq_f = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

print('Pattern file:', pat_f)
print('Sequence file:', seq_f)

# Reading sequence file
seq = ''
for line in open(seq_f):
    if line[0] == '>':
        continue

    seq += line.rstrip().upper()

# Reading pattern file
pat = {}
p = 0
for line in open(pat_f):
    prob = line.rstrip().split()	#split() : ‘ ’ 공백 기준으로 split한 리스트 생성

    pat[p] = {}
    for (i, nt) in list(enumerate('ACGT')):	# line마다 하나씩
        pat[p][nt] = float(prob[i])

    p += 1
psize = p

# Traversing sequence
max_p = -1
max_score = -1;

for i in range(0, len(seq) - (psize-1)):
    score = 1
    for j in range(0, psize):
        nt = seq[i + j]
        score *= pat[j][nt]

    if score >= max_score:
        max_score = score
        max_p = i

max_seq = seq[max_p:max_p + psize]
print(max_p+1, max_score, max_seq)
