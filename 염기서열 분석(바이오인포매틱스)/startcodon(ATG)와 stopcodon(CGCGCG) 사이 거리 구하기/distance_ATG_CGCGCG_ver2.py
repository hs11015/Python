print("받고싶은 염기서열 txt를 입력하세요.")
seq_f = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

bs = 'CGCGCG'
sc = 'ATG'

######################################
def find_positions(seq, pattern):
    pos = []
    psize = 0
    while True:
        i = seq.find(pattern)
        if i == -1: break
        pos.append(i + psize)
        seq = seq[i + len(pattern):]
        psize += i + len(pattern)
    return pos
######################################

seq = ''
for line in open(seq_f):
    if line[0] == '>': continue
    seq += line.rstrip().upper()

# finding binding site positions (starting from 0)
bspos = find_positions(seq, bs)

# finding start codon positions (starting from 0)
scpos = find_positions(seq, sc)

for bs_value in bspos:

    found_index = -1
    for (sc_index, sc_value) in list(enumerate(scpos)):
        if sc_value >= bs_value:
            found_index = sc_index
            break

    dist = -1
    if found_index == 0:
        dist = scpos[found_index] - bs_value
    elif found_index == -1:
        dist = bs_value - scpos[-1]
    else:
        dist1 = scpos[found_index] - bs_value
        dist2 = bs_value - scpos[found_index-1]
        dist = dist1
        if dist2 < dist:
            dist = dist2

    print(bs_value + 1, '\t', dist, sep='')
