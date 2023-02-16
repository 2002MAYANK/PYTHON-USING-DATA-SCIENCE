from turtle import*
speed('fast')
bgcolor('black')
pencolor('green')
fillcolor('red')
pensize(5)
side=6
for i in range(side):
    fd(100)
    begin_fill()
    for i in range(side):
        fd(50)
        for i in range(side):
            fd(25)
            left(360/side)
            dot(10)
        rt(360/side)
    end_fill()
    lt(360/side)
mainloop()

