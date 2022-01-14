print("받고싶은 염기서열 txt를 입력하세요.")
fpath = input("(현재 파일 안에 있으면 '.\파일명.txt' 형식) : ")

List = []

for line in open(fpath):
    for x in line:
        if x == '>':
            break
        if x =='\n':
            continue
        List.append(x)


ATG_loc_1 = 1
ATG_loc_2 = 1
CGCGCG_loc = 1


temp = 0

for x in range(0, len(List)-5):
    if List[x] == 'C':
        if List[x+1] == 'G':
            if List[x+2] == 'C':
                if List[x+3] == 'G':
                    if List[x+4] == 'C':
                        if List[x+5] == 'G':
                            CGCGCG_loc = int(x+1)   #새로 입력된 CGCGCG 시작 위>치

                            if x+5 > len(List)-5 :
                                print(CGCGCG_loc, end='\t')
                                print(CGCGCG_loc, ATG_loc_1)

    elif List[x] == 'A':
        if List[x+1] == 'T':
            if List[x+2] == 'G':
                ATG_loc_2 = int(x+1)    #새로 입력된 ATG 시작 위치

                if ATG_loc_2 != 1:

                    if ATG_loc_1 == 1:
                        print(CGCGCG_loc, end='\t')
                        print(ATG_loc_2 - CGCGCG_loc)

                    elif (CGCGCG_loc - ATG_loc_1) > (ATG_loc_2 - CGCGCG_loc) > 0:
                        print(CGCGCG_loc, end='\t')
                        print(ATG_loc_2 - CGCGCG_loc)

                    elif 0 < (CGCGCG_loc - ATG_loc_1) < (ATG_loc_2 - CGCGCG_loc):
                        print(CGCGCG_loc, end='\t')
                        print(CGCGCG_loc - ATG_loc_1)

                ATG_loc_1 = ATG_loc_2   #이전 ATG 시작 위치 바꾸기

print()
