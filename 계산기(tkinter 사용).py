
#tkinter 모듈 불러와서 계산기 GUI 생성하기 (GUI: 사용자 그래픽 인터페이스-전자 기기와 상호 작용할 수 있도록 하는 시각적 인터페이스)
import tkinter as tkt 

#루트 창 생성하고 설정
root = tkt.Tk()
root.title("계산기") #제목 설정
root.resizable(0, 0) #창 크기 조정할 수 없게 하기          
root.wm_attributes("-topmost", 1) #창을 항상 위에 표시하게 하기  

#계산식 저장할 문자열 변수 생성
equa = ""
equation = tkt.StringVar() #변수 선언(이 함수를 사용해야 GUI에서 tkinter가 변수값을 가져올 떄 문제 안 생김)

#계산식 입력 표시할 레이블 생성
calculation = tkt.Label(root, textvariable=equation) 
equation.set("계산식을 입력하세요 : ") #초기 메세지 설정
calculation.grid(row=2, columnspan=8) #레이블 배치

#버튼 눌렸을 때 숫자 or 연산자를 계산식에 추가하는 함수 정의 (num을 인수로 가짐)
def btnPress(num): 
     global equa #변수 equa를 전역 변수로 설정(전역 변수는 스크립트 전체에서 접근할 수 있는 변수)
     equa = equa + str(num) #num을 문자열로 바꿔주고 더함(equa가 문자열 변수이기 때문)
     equation.set(equa) #equa 값을 equation 변수에 설정 - 사용자 인터페이스에 계산식 표시하기 위함

#"=" 버튼 눌렸을 때 계산식 평가하는 함수 정의 
def EqualPress():
     global equa #위와 동일
     total = str(eval(equa)) #eval() 함수를 사용하여 계산하고 그 값을 문자열로 바꿔서 total변수에 저장
     equation.set(total) #위와 동일
     equa = "" #변수 equa를 다시 비운다고 생각
      
#"C" 버튼이 눌렸을 때 계산식 초기화하는 함수 정의
def ClearPress():
     global equa #위와 동일
     equa = "" #equa 비운다고 생각
     equation.set("") #위와 동일

# 숫자 및 연산자 버튼을 생성하고 배치(bg-배경색 설정, command=lambda는 한줄 함수를 구현할 때 사용-보통 잘 쓰지는 않지만 지금같은 경우 사용하기도 함)
#width-라벨의 너비, relief-라벨의 테두리 모양, borderwidth-라벨 테두리 두께, padx-라벨의 테두리와 내용의 가로 여백, pady-라벨의 테두리와 내용의 세로 여백
#row-행 위치, column-열 위치
Button0 = tkt.Button(root, text="0", bg='white',command=lambda: btnPress(0), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button0.grid(row=6, column=2, padx=10, pady=10)
Button1 = tkt.Button(root, text="1", bg='white',command=lambda: btnPress(1), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button1.grid(row=3, column=1, padx=10, pady=10)
Button2 = tkt.Button(root, text="2", bg='white',command=lambda: btnPress(2), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button2.grid(row=3, column=2, padx=10, pady=10)
Button3 = tkt.Button(root, text="3", bg='white',command=lambda: btnPress(3), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button3.grid(row=3, column=3, padx=10, pady=10)
Button4 = tkt.Button(root, text="4", bg='white',command=lambda: btnPress(4), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button4.grid(row=4, column=1, padx=10, pady=10)
Button5 = tkt.Button(root, text="5", bg='white',command=lambda: btnPress(5), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button5.grid(row=4, column=2, padx=10, pady=10)
Button6 = tkt.Button(root, text="6", bg='white',command=lambda: btnPress(6), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button6.grid(row=4, column=3, padx=10, pady=10)
Button7 = tkt.Button(root, text="7", bg='white',command=lambda: btnPress(7), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button7.grid(row=5, column=1, padx=10, pady=10)
Button8 = tkt.Button(root, text="8", bg='white',command=lambda: btnPress(8), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button8.grid(row=5, column=2, padx=10, pady=10)
Button9 = tkt.Button(root, text="9", bg='white',command=lambda: btnPress(9), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button9.grid(row=5, column=3, padx=10, pady=10)
Plus = tkt.Button(root, text="+", bg='white',command=lambda: btnPress("+"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Plus.grid(row=3, column=4, padx=10, pady=10)
Minus = tkt.Button(root, text="-", bg='white',command=lambda: btnPress("-"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Minus.grid(row=4, column=4, padx=10, pady=10)
Multiply = tkt.Button(root, text="*", bg='white',command=lambda: btnPress("*"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Multiply.grid(row=5, column=4, padx=10, pady=10)
Divide = tkt.Button(root, text="/", bg='white',command=lambda: btnPress("/"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Divide.grid(row=6, column=4, padx=10, pady=10)
Equal = tkt.Button(root, text="=", bg='white',command=EqualPress, height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Equal.grid(row=6, column=3, padx=10, pady=10)
Clear = tkt.Button(root, text="C", bg='white',command=ClearPress, height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Clear.grid(row=6, column=1, padx=10, pady=10)

# 루프를 시작하여 GUI를 실행
root.mainloop()