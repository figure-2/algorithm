import sys
sys.stdin = open('input.txt')

#stdin 의 뜻 standard in /  표준

# N = int(input()) #  input 되는 값이 숫자지만 문자로 인식하기 때문에 int()로 숫자로 변환해줌

# #print(N)

# if N % 2 == 1:
#     print('홀수')
# else:
#     print('짝수')

# N = int(input()) 

# if N % 2 == 1:
#     print('홀수')
# else:
#     print('짝수')

TC = int(input())

for i in range(TC):
    N =  int(input())
    #print(N)

    if N % 2 == 1:
        print('홀수')
    else:
        print('짝수')


# 1차원 리스트 input 받기

number = input().split()

for number in numbers:
    int_num = int(number)

    if int_num % 2 == 1:
        print(f'{int_num}은 홀수 입니다.')



numbers = list(map(int, input().split()))

for number in number:
    if number % 2










