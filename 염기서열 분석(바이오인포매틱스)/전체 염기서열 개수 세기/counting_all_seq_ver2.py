def count_nt(name, seq):
    nts = {nt : 0 for nt in 'ACGT'}
    for nt in seq:
        nts[nt] += 1

    print(name, ': ', seq, sep='')
    for nt in 'ACGT':
        cnt = nts[nt]
        print(nt, cnt)
    print()

print("받고싶은 염기서열 txt를 입력하세요.")
fpath = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

seqs = {}
seq = ''
name = ''
for line in open(fpath):
    if line[0] == '>':			#염기 이름과 염기서열 dictionary에 각각 저장
        if seq != '':
            seqs[name] = seq
            seq = ''
        name = line[1:].rstrip()
    else:
        seq += line.rstrip().upper()

if seq != '':
    seqs[name] = seq

for name in sorted(seqs):		#sorted(seqs)로 바로 sort 하고 들어감
    seq = seqs[name]
    count_nt(name, seq)
