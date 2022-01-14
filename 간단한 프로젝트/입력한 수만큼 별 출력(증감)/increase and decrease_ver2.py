while True:
    ans = input("Enter a positive integer or 'q' for quit:")
    if ans == 'q':
        print('bye...')
        break

    if not ans.isdigit() or int(ans) <= 0:
        print('Only positive integer please...\n')
        continue

    num = int(ans)
    print('You entered', num)

    maxnum = num * 2 - 1;
    numdigit = len(str(maxnum))

    linecnt = 1
    outline = '{:<{}} {}'
    for i in range(1, num+1):
        print(outline.format(linecnt, numdigit, '*' * i))		#{:<numdigit} (마지막 숫자 길이, 왼쪽정렬)
        linecnt += 1

    for i in range(num-1, 0, -1):
        print(outline.format(linecnt, numdigit, '*' * i))
        linecnt += 1

    print()
