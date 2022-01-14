L = []      #Create an empty list

for x in range(0, 100):
    L.append(x*3)   #insert the 100 integers(3의 배수)


line_num = 1
count = 0

#1번째 줄은 1개, 2번째 줄 2개, ...,  줄의 수와 출력되는 수 동일

for x in range(0, 100):
    print('%03d' %L[x], end=' ')    #세 자리 수로 출력(앞에 0 붙여서 채움)
    count += 1                      #숫자 하나 입력될 때마다 count 하나씩 늘려주기

    if line_num == count:           #line_num(줄 수)와 count(출력된 수)가 같다면
        print()                     #다음 for문 실행될 때 다음 줄에 수가 출력되>게 만듦
        count = 0                   #빈 줄이기 떄문에 count는 0으로 재정의
        line_num += 1               #한 줄 추가했기 떄문에 line_num은 +1하기

print()
