while True:

    enter = input("Enter a positive integer or 'q' for quit:")

    if enter.isdigit()==False:  #enter가 숫자가 아닐 때
        if enter == 'q':
            print('bye...')
            break

        else:   #q가 아닌 문자일 때(실수float도 여기 포함)
            print("Only positive integer please...\n")


    else:   #enter.isdigit()==True, enter가 숫자일 때
        if int(enter) == 0:     #0은 양이 아닌 정수
            print("Only positive integer please...\n")

        elif int(enter) > 0:
            print("You entered %d" %int(enter))

            cnt = 0
            for i in range(1, int(enter)*2):
                if int(enter)*2-1 < 10:
                    print('%-2d' %i, end='')
                elif int(enter)*2-1 < 100:
                    print('%-3d' %i, end='')
                elif int(enter)*2-1 < 1000:
                    print('%-4d' %i, end='')
                elif int(enter)*2-1 < 10000:
                    print('%-5d' %i, end='')


                if i < int(enter)+1:
                    print('*' * i)

                else:   #i > =enter+1
                    cnt += 1
                    print('*' * (i-2*cnt))
            print()

