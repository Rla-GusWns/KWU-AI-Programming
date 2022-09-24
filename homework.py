import turtle as  t

#1번 모양으로 진행

t.speed("fastest")

#캔버스 크기 정하고 칠하기

t.color('gray')

t.penup()
t.goto(-250,-250)
t.pendown()
t.begin_fill()
for i in range(4) :
    t.forward(500)
    t.left(90)
t.end_fill()

#얼굴모양 만들기

t.color('white')
t.penup()
t.pensize(4)
t.fillcolor('orange')
t.goto(0,-230)
t.pendown()
t.begin_fill()
t.circle(220)
t.end_fill()

# 입 만들기

t.color('red')
t.penup()
t.goto(0,-170)
t.pendown()
t.begin_fill()
t.circle(90)
t.end_fill()

t.color('orange')
t.penup()
t.goto(0,-150)
t.pendown()
t.begin_fill()
t.circle(95)
t.end_fill()

#왼쪽 눈 만들기

t.color('white')
t.pensize(4)
t.penup()
t.goto(-160,50)
t.right(90)
t.fillcolor('darkblue')
t.begin_fill()

a=0.7
b=0.14

for i in range(120):
  
    if 0<= i <10 or 60<= i <70 :
        t.pendown()
        a = a+0.000007
        t.left(4) #   3 
        t.forward(a) #   a   
        t.penup()
    if 10<= i < 30 or 70<= i< 90:
        t.pendown()
        b=b+0.35
        t.left(2.5)
        t.forward(b)
        t.penup()
    if 30<= i < 50 or 90<= i < 110:
        t.pendown()
        b=b-0.35
        t.left(2.5)
        t.forward(b)
        t.penup()
    if 50<= i < 60 or 110<=i <120:
        t.pendown()
        a = a-0.000007
        t.left(4) #   3 
        t.forward(a) #   a   
        t.penup()

t.end_fill()

#오른쪽 눈 만들기

t.color('white')
t.goto(130,40)
t.right(45)
t.pendown()
t.pensize(9)
t.fillcolor('darkblue')
t.begin_fill()
t.circle(-55,90)
t.circle(-30,90)
t.circle(-55,90)
t.circle(-30,90)
t.end_fill()

#코 만들기

t.penup()
t.color('yellow')
t.goto(-10,0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

t.hideturtle()

t.done()

