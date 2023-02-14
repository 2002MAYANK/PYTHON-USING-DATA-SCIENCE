from turtle import*
speed('fast')
bgcolor('black')
pencolor('yellow')
fillcolor('red')
pensize(5)
side=6
for i in range(side):
    fd(150)
    begin_fill()
    for i in range(side):
        fd(100)
        left(360/side)
    lt(360/side)
    end_fill()
    lt(360/side)
mainloop()

