import turtle
import time
def pick_up_object(location, pocket):
    if location.get_object() != 'No objects':
        while True:
            if location.get_object() not in pocket:
                time.sleep(3)
                print((f'You find a {location.get_object()}.').center(170))
                time.sleep(2)
                choice_object = input(f'You have the following options:\n(1) Pick up \n(2) Do not pick up\n\nEnter your choice: ')

                if choice_object == str(1):
                    object_pocket = pocket.append(location.get_object())
                    if location.get_object() == 'Staircasekey' or location.get_object == 'Officekey':
                        rootwindow = turtle.getcanvas().winfo_toplevel()
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
                        turtle.tracer(False)
                        t = turtle.Turtle()
                        t.hideturtle()
                        t.speed(0)
                        t = turtle.Turtle()

                        t.fillcolor("gold")
                        t.speed(0)
                        t.penup()
                        #Cirkel
                        t.pensize(5)
                        t.goto(160,-20)
                        t.pendown()
                        t.begin_fill()
                        t.circle(60)
                        t.penup()
                        t.goto(160,0)
                        t.pendown()
                        t.end_fill()
                        t.fillcolor("white")
                        t.begin_fill()
                        t.circle(40)
                        t.penup()
                        t.end_fill()

                        t.fillcolor("gold")

                        t.goto(100,25)
                        t.begin_fill()
                        t.left(180)
                        t.pendown()

                        t.forward(160)
                        t.penup()
                        t.goto(100,50)

                        t.pendown()
                        t.forward(160)

                        t.right(90)
                        t.forward(10)
                        t.left(90)
                        t.forward(80)
                        t.left(90)
                        t.forward(10)
                        t.left(90)
                        t.forward(10)
                        t.right(90)
                        t.forward(60)
                        t.left(90)
                        t.forward(10)
                        t.left(90)
                        t.forward(30)
                        t.right(90)
                        t.forward(10)
                        t.right(90)
                        t.forward(20)
                        t.left(90)
                        t.forward(10)
                        t.left(90)
                        t.forward(20)
                        t.right(90)
                        t.forward(10)
                        t.right(90)
                        t.forward(20)
                        t.left(90)
                        t.forward(10)
                        t.left(90)
                        t.forward(20)
                        t.right(90)
                        t.forward(10)
                        t.right(90)
                        t.forward(30)
                        t.left(90)
                        t.forward(10)
                        t.left(90)
                        t.forward(35)
                        t.right(90)
                        t.forward(160)
                        t.left(90)
                        t.forward(25)
                        t.left(90)
                        t.forward(160)
                        t.end_fill()
                        t.goto(100,50)
                        t.begin_fill()
                        t.left(90)
                        t.forward(25)
                        t.right(90)
                        t.forward(160)
                        t.end_fill()
                        t.penup()
                        t.goto(-125,150)
                        t.pendown()
                        t.pensize(10)
                        t.write("woooow you found a key!",font=("Bauhaus 93",20,"normal"))
                        t.hideturtle()
                        turtle.exitonclick()

                    elif location.get_object() == 'Note with number _ _ _ 1':
                        rootwindow = turtle.getcanvas().winfo_toplevel()
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
                        turtle.tracer(False)
                        t = turtle.Turtle()
                        t.hideturtle()
                        t.speed(0)

                        # Pappret
                        t.goto(-200, -170)
                        t.begin_fill()
                        t.fillcolor('beige')
                        t.width(5)
                        t.fd(400)
                        t.lt(90)
                        t.fd(500)
                        t.lt(90)
                        t.fd(400)
                        t.lt(90)
                        t.fd(500)
                        t.end_fill()

                        # Siffra
                        t.penup()
                        t.goto(0, 0)
                        t.pendown()
                        t.write(1, font=('arial', 100), align='center')

                        # Hålen
                        k = 0; n = 10; y = 355
                        while k < n:
                            k += 1; y -= 50
                            t.penup()
                            t.goto(-190, y)
                            t.pendown()
                            t.circle(5)

                        # lines
                        k = 0; n = 24; y = 330
                        while k < n:
                            k += 1; y -= 20
                            t.width(1)
                            t.penup()
                            t.goto(-197, y)
                            t.pendown()
                            t.lt(90)
                            t.fd(400)
                            t.rt(90)

                        # redline
                        t.penup()
                        t.goto(-165, 327)
                        t.pendown()
                        t.color('red')
                        t.fd(495)
                        t.color('black')

                        turtle.exitonclick()

                    elif location.get_object() == 'Note with number _ 2 _ _':
                        rootwindow = turtle.getcanvas().winfo_toplevel()
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
                        turtle.tracer(False)
                        t = turtle.Turtle()
                        t.hideturtle()
                        t.speed(0)

                        # Pappret
                        t.goto(-200, -170)
                        t.begin_fill()
                        t.fillcolor('beige')
                        t.width(5)
                        t.fd(400)
                        t.lt(90)
                        t.fd(500)
                        t.lt(90)
                        t.fd(400)
                        t.lt(90)
                        t.fd(500)
                        t.end_fill()

                        # Siffra
                        t.penup()
                        t.goto(0, 0)
                        t.pendown()
                        t.write(2, font=('arial', 100), align='center')

                        # Hålen
                        k = 0; n = 10; y = 355
                        while k < n:
                            k += 1; y -= 50
                            t.penup()
                            t.goto(-190, y)
                            t.pendown()
                            t.circle(5)

                        # lines
                        k = 0; n = 24; y = 330
                        while k < n:
                            k += 1; y -= 20
                            t.width(1)
                            t.penup()
                            t.goto(-197, y)
                            t.pendown()
                            t.lt(90)
                            t.fd(400)
                            t.rt(90)

                        # redline
                        t.penup()
                        t.goto(-165, 327)
                        t.pendown()
                        t.color('red')
                        t.fd(495)
                        t.color('black')

                        turtle.exitonclick()

                    if location.get_object() == 'Note with number _ _ 4 _':
                        rootwindow = turtle.getcanvas().winfo_toplevel()
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
                        turtle.tracer(False)
                        t = turtle.Turtle()
                        t.hideturtle()
                        t.speed(0)

                        # Pappret
                        t.goto(-200, -170)
                        t.begin_fill()
                        t.fillcolor('beige')
                        t.width(5)
                        t.fd(400)
                        t.lt(90)
                        t.fd(500)
                        t.lt(90)
                        t.fd(400)
                        t.lt(90)
                        t.fd(500)
                        t.end_fill()

                        # Siffra
                        t.penup()
                        t.goto(0, 0)
                        t.pendown()
                        t.write(4, font=('arial', 100), align='center')

                        # Hålen
                        k = 0; n = 10; y = 355
                        while k < n:
                            k += 1; y -= 50
                            t.penup()
                            t.goto(-190, y)
                            t.pendown()
                            t.circle(5)

                        # lines
                        k = 0; n = 24; y = 330
                        while k < n:
                            k += 1; y -= 20
                            t.width(1)
                            t.penup()
                            t.goto(-197, y)
                            t.pendown()
                            t.lt(90)
                            t.fd(400)
                            t.rt(90)

                        # redline
                        t.penup()
                        t.goto(-165, 327)
                        t.pendown()
                        t.color('red')
                        t.fd(495)
                        t.color('black')

                        turtle.exitonclick()

                    elif location.get_object() == 'Note with number 7 _ _ _':
                        rootwindow = turtle.getcanvas().winfo_toplevel()
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
                        turtle.tracer(False)
                        t = turtle.Turtle()
                        t.hideturtle()
                        t.speed(0)

                        # Pappret
                        t.goto(-200, -170)
                        t.begin_fill()
                        t.fillcolor('beige')
                        t.width(5)
                        t.fd(400)
                        t.lt(90)
                        t.fd(500)
                        t.lt(90)
                        t.fd(400)
                        t.lt(90)
                        t.fd(500)
                        t.end_fill()

                        # Siffra
                        t.penup()
                        t.goto(0, 0)
                        t.pendown()
                        t.write(7, font=('arial', 100), align='center')

                        # Hålen
                        k = 0; n = 10; y = 355
                        while k < n:
                            k += 1; y -= 50
                            t.penup()
                            t.goto(-190, y)
                            t.pendown()
                            t.circle(5)

                        # lines
                        k = 0; n = 24; y = 330
                        while k < n:
                            k += 1; y -= 20
                            t.width(1)
                            t.penup()
                            t.goto(-197, y)
                            t.pendown()
                            t.lt(90)
                            t.fd(400)
                            t.rt(90)

                        # redline
                        t.penup()
                        t.goto(-165, 327)
                        t.pendown()
                        t.color('red')
                        t.fd(495)
                        t.color('black')

                        turtle.exitonclick()


                    print('\n' * 50)
                    print((f'You pick up the {location.get_object()} and put it in your pocket.').center(170))
                    print((f'You are still in the {location.get_platsname()}.').center(170))
                    return object_pocket
                    
                elif choice_object == str(2):
                    break
            
                else:
                    print("You did not enter any of the options... Try again:\n")
            else:
                break
