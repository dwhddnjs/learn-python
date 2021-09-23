//출력 명령
print(111)

print('이종원')

print(1234+1234)

print('이종원'*10)

//변수

이름 = '이종원'

//인덱싱

print('파이썬 배우고 있음'[0]) //파

print('파이썬 배우고 있음'[0:2]) //파이

//list
자동차 = ['k5', 'white', 5000]

자동차 = ['k5', 'white', [5000, 600]]

print(자동차[0]) //k5

자동차[1] = 'black' //['k5', 'black', 5000]
자동차.sort() //정렬
자동차.reverse() // 뒤집기

//Dictionary 
중고차 = {
    'brand':'bmw',
    'model':'520d'
    }

print(중고차['brand']) //bmw

중고차['brand'] = 123

print(중고차['brand']) //123


// if문 조건문

재고량 = 20

// == 비교 연산자

if 재고량 > 0 : 
    print('지금 주문 가능합니다')

중고차재고 = ['k5', 'bmw', 'tico']

if 'k5' in 중고차재고 : 
    print('지금 주문 가능합니다')
  else : 
    print('주문 불가능 합니다')
  elif 재고량 > 0 :
    print('주문 가능 합니다')

//어떤 코드를 조건이 맞을 때만 실행시키고 싶은 경우 쓰자

//for반복문
 for 변수 in 범위

for i in range(0,10):
    print('차')

중고차들 = ['k5', 'bmw', 'tico']

for i in 중고차들 :
    print(i)

    i는 중고차 하나 하나의 데이터 

print()

//1.코드 단순 반복할때
//2.list에서 자료 하나씩 뽑을떄













