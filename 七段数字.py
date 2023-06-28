#七段数码管，带小数
from ast import Str
from tkinter import Y
import turtle,time,random

from pip import main
#画笔颜色随机
def color():
    r=random.random()
    g=random.random()
    b=random.random()
    return r,g,b
#线条
def drawline(s):
    if s==1: 
        grap()
        turtle.pendown()       
        turtle.fd(30)
        grap()
        turtle.right(90)        
    else:
        turtle.penup()
        grap()
        turtle.fd(30)
        grap()
        turtle.right(90)
        turtle.pendown()

#间隔
def grap():
    turtle.penup()
    turtle.fd(8)
    #turtle.pendown()

#画数字
def drawnum(n):
    drawline(1) if n in [2,3,4,5,6,8,9] else drawline(0) 
    drawline(1) if n in [1,3,4,5,6,7,8,9,0] else drawline(0) 
    drawline(1) if n in [2,3,5,6,8,9,0] else drawline(0) 
    drawline(1) if n in [2,6,8,0] else drawline(0) 
    turtle.left(90)
    drawline(1) if n in [4,5,6,8,9,0] else drawline(0) 
    drawline(1) if n in [2,3,5,6,7,8,9,0] else drawline(0) 
    drawline(1) if n in [1,2,3,4,7,8,9,0] else drawline(0) 
    turtle.penup()
    turtle.left(180)
    turtle.fd(26)
    turtle.pendown()

k=0 #计数用
def drawnums(str):
    global k
    for i in str:
        if i in '-: ':
            turtle.write("年月日：：：    "[k],font=("微软雅黑",20,"normal"))
            grap()
            grap()
            grap()
            grap()
            grap()
            turtle.pencolor(color())
            k+=1
        else:
            drawnum(eval(i))

#main
def main():
    turtle.setup(1280,270)
    turtle.penup()
    turtle.pensize(5)
    turtle.pencolor(color())
    turtle.speed(10)
    turtle.delay(5)
    turtle.goto(-600,0)
    turtle.pendown()
    #获取时间
    t=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    drawnums(t)
    turtle.hideturtle()
    turtle.done()

main()

