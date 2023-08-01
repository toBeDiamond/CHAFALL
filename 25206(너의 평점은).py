import sys;
sys.stdin = open('ppp.txt')

# 등급에 따른 과목 평점
tier ={
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
}

T= 20
total = 0
credit = 0
for tc in range(T):
    data = input().split() # [과목명, 학점, 평점]

    if data[2] != 'P': #P인 경우 제외시키기
        total += float(data[1]) * tier[data[2]] # 학점 숫자형으로 전환 후 평점으로 곱
        credit+= float(data[1]) # 학점만
print(f'{total/credit: .6f}') # 총합/ 전체 학점


