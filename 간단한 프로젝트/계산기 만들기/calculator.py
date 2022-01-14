print('\n##### My Calculator #####\n')
print("Enter 'stop' as the first number to quit\n")

while True:     #반복문으로 stop 입력 전까지는 계속 계산 기능 함

    a = input('Enter the first number:')    #1번쨰 숫자 입력
    if a == 'stop':
        print('Bye')    #stop 입력 시 Bye 출력 후 종료
        break
    oper = input('Enter operator:')         #연산자 입력
    b = input('Enter the second number:')   #2번째 숫자 입력

    if a.isdigit() == 1  and b.isdigit() == 1:  #a와 b가 모두 숫자일 때

        if oper == '+' or oper == '-' or oper == '*' or oper == '/':
            if oper == '+':                 #연산자가 +일 때(덧셈)
                result = int(a) + int(b)    #result에 a+b 값 저장
            elif oper == '-':               #연산자가 -일 때(뺄셈)
                result = int(a) - int(b)    #result에 a-b  값 저장
            elif oper == '*':               #연산자가 *일 때(곱셈)
                result = int(a) * int(b)    #result에 a*b 값 저장
            elif oper == '/':               #연산자가 /일 때(나눗셈)
                result = int(a) / int(b)    #result에 a/b 값 저장

            print(a, oper, b, '=', result, '\n')            #결과값 출력

        else:   #주어진 사칙 연산자(+, -, *, /)가 아닌 것을 입력했을 때
            print('Error: Wrong operator. Try again\n')     #오류 알림

    else:       #a와 b 중 하나라도 숫자가 아닐 때
        print('Error: Only numbers are allowed. Try again\n')
