from turtle import*
def polygon(side,dis):
    for i in range(side):
        fd(dis)
        lt(360/side)
bgcolor("black")
for i in range(3,11):
    color('red')
    polygon(i,-100)
    polygon(i,100)


hideturtle()
mainloop()