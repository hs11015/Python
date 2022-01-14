cnt_AA = 0
cnt_AC = 0
cnt_AG = 0
cnt_AT = 0
cnt_CA = 0
cnt_CC = 0
cnt_CG = 0
cnt_CT = 0
cnt_GA = 0
cnt_GC = 0
cnt_GG = 0
cnt_GT = 0
cnt_TA = 0
cnt_TC = 0
cnt_TG = 0
cnt_TT = 0

List = []
nucleotide = ['A', 'C', 'G', 'T']

for line in  open('.\seq.txt'):
    for x in line:
        if x == '\n':
            continue
        List.append(x)

for i in range(0, len(List)-1):
    if List[i] == 'A':
        if List[i+1] == 'A':
            cnt_AA += 1
        elif List[i+1] == 'C':
            cnt_AC += 1
        elif List[i+1] == 'G':
            cnt_AG += 1
        elif List[i+1] == 'T':
            cnt_AT += 1

    elif List[i] == 'C':
        if List[i+1] == 'A':
            cnt_CA += 1
        elif List[i+1] == 'C':
            cnt_CC += 1
        elif List[i+1] == 'G':
            cnt_CG += 1
        elif List[i+1] == 'T':
            cnt_CT += 1

    elif List[i] == 'G':
        if List[i+1] == 'A':
            cnt_GA += 1
        elif List[i+1] == 'C':
            cnt_GC += 1
        elif List[i+1] == 'G':
            cnt_GG += 1
        elif List[i+1] == 'T':
            cnt_GT += 1

    elif List[i] == 'T':
        if List[i+1] == 'A':
            cnt_TA += 1
        elif List[i+1] == 'C':
            cnt_TC += 1
        elif List[i+1] == 'G':
            cnt_TG += 1
        elif List[i+1] == 'T':
            cnt_TT += 1

cnt_dict = {'AA': int(cnt_AA), 'AC': int(cnt_AC), 'AG': int(cnt_AG), 'AT': int(cnt_AT),
    'CA': int(cnt_CA), 'CC': int(cnt_CC), 'CG': int(cnt_CG), 'CT': int(cnt_CT),
    'GA': int(cnt_GA), 'GC': int(cnt_GC), 'GG': int(cnt_GG), 'GT': int(cnt_GT),
    'TA': int(cnt_TA), 'TC': int(cnt_TC), 'TG': int(cnt_TG), 'TT': int(cnt_TT)}

for x in range(0, 4):
    for y in range(0,4):
        dinucleotide = nucleotide[x] + nucleotide[y]
        if cnt_dict[dinucleotide] != 0:     #0이 아닐 떄만 출력
            print(dinucleotide, cnt_dict[dinucleotide])


print()
