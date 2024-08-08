#기본 사칙연산 함수 정의(이건 터미널 내에서 실행되는 거)
def add(x, y): #더하기 함수 정의(x,y를 인수로 가짐)
    return x + y #함수의 결과값(add 함수 사용했을 때의 결과값)

def subtract(x, y): #빼기 함수 정의(x,y를 인수로 가짐)
    return x - y #함수의 결과값

def multiply(x, y): #곱하기 함수 정의(x,y를 인수로 가짐)
    return x * y #함수의 결과값

def divide(x, y): #나누기 함수 정의(x,y를 인수로 가짐)
    return x / y #함수의 결과값

#사용자에게 사칙연산 선택 메뉴 출력
print("사칙연산을 선택 하세요. \n 1.더하기 \n 2.빼기 \n 3.곱하기 \n 4.나누기") #사용자가 어떤 것을 사용할 것인지 고르기 위해 보기 주는 것(\n은 줄바꿈 해주는 것)


choice = input("선택 하세요(1 or 2 or 3 or 4):") #사용자가 입력하는 값 받아서 choice 변수에 할당

num1 = int(input("첫 번째 숫자: ")) #첫 번째 숫자 입력 받아 num1 변수에 할당 
num2 = int(input("두 번째 숫자: ")) #두 번째 숫자 입력 받아 num2 변수에 할당

if choice == '1': #사용자가 입력한 값이 1이라면
    print(num1,"+",num2,"=", add(num1,num2)) #변수 num1, 문자열 +, 변수 num2, 문자열 =, 위에서 정의했던 add함수의 결과값을 출력

elif choice == '2': #사용자가 입력한 값이 2라면
    print(num1,"-",num2,"=", subtract(num1,num2)) #변수 num1, 문자열 -, 변수 num2, 문자열 =, 위에서 정의했던 subtract함수의 결과값을 출력

elif choice == '3': #사용자가 입력한 값이 3이라면
    print(num1,"*",num2,"=", multiply(num1,num2)) #변수 num1, 문자열 *, 변수 num2, 문자열 =, 위에서 정의했던 multiply함수의 결과값을 출력

elif choice == '4': #사용자가 입력한 값이 4라면
    print(num1,"/",num2,"=", divide(num1,num2)) #변수 num1, 문자열 /, 변수 num2, 문자열 =, 위에서 정의했던 divide함수의 결과값을 출력
else: #1,2,3,4 제외한 모든 다른 것을 입력했을 경우
    print("잘못된 선택")  #""안에 있는 문자열 출력
