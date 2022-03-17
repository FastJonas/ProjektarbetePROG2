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
                    if location.get_object() == 'Staircasekey' or location.get_object() == 'Officekey':
                        
                        rootwindow = turtle.getcanvas().winfo_toplevel()
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
                        turtle.tracer(False)
                        window1 = turtle.Screen()
                        t1 = turtle.Turtle()
                        
                        t1.hideturtle()
                        t1.speed(0)
                        

                        t1.fillcolor("gold")
                        t1.speed(0)
                        t1.penup()
                        #Cirkel
                        t1.pensize(5)
                        t1.goto(160,-20)
                        t1.pendown()
                        t1.begin_fill()
                        t1.circle(60)
                        t1.penup()
                        t1.goto(160,0)
                        t1.pendown()
                        t1.end_fill()
                        t1.fillcolor("white")
                        t1.begin_fill()
                        t1.circle(40)
                        t1.penup()
                        t1.end_fill()

                        t1.fillcolor("gold")

                        t1.goto(100,25)
                        t1.begin_fill()
                        t1.left(180)
                        t1.pendown()

                        t1.forward(160)
                        t1.penup()
                        t1.goto(100,50)

                        t1.pendown()
                        t1.forward(160)

                        t1.right(90)
                        t1.forward(10)
                        t1.left(90)
                        t1.forward(80)
                        t1.left(90)
                        t1.forward(10)
                        t1.left(90)
                        t1.forward(10)
                        t1.right(90)
                        t1.forward(60)
                        t1.left(90)
                        t1.forward(10)
                        t1.left(90)
                        t1.forward(30)
                        t1.right(90)
                        t1.forward(10)
                        t1.right(90)
                        t1.forward(20)
                        t1.left(90)
                        t1.forward(10)
                        t1.left(90)
                        t1.forward(20)
                        t1.right(90)
                        t1.forward(10)
                        t1.right(90)
                        t1.forward(20)
                        t1.left(90)
                        t1.forward(10)
                        t1.left(90)
                        t1.forward(20)
                        t1.right(90)
                        t1.forward(10)
                        t1.right(90)
                        t1.forward(30)
                        t1.left(90)
                        t1.forward(10)
                        t1.left(90)
                        t1.forward(35)
                        t1.right(90)
                        t1.forward(160)
                        t1.left(90)
                        t1.forward(25)
                        t1.left(90)
                        t1.forward(160)
                        t1.end_fill()
                        t1.goto(100,50)
                        t1.begin_fill()
                        t1.left(90)
                        t1.forward(25)
                        t1.right(90)
                        t1.forward(160)
                        t1.end_fill()
                        t1.penup()
                        t1.goto(-150,150)
                        t1.pendown()
                        t1.pensize(10)
                        t1.write("(Click on this window to close)",font=("Bodoni MT",20,"normal"))
                        t1.hideturtle()
                        window1.exitonclick()

                        try:
                            turtle.bye()
                        except Exception:
                            pass

                    elif location.get_object() == 'Note with number _ _ _ 1':
                        
                        rootwindow = turtle.getcanvas().winfo_toplevel()
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
                        turtle.tracer(False)
                        window2 = turtle.Screen()
                        t2 = turtle.Turtle()
                        t2.hideturtle()
                        t2.speed(0)

                        # Pappret
                        t2.goto(-200, -170)
                        t2.begin_fill()
                        t2.fillcolor('beige')
                        t2.width(5)
                        t2.fd(400)
                        t2.lt(90)
                        t2.fd(500)
                        t2.lt(90)
                        t2.fd(400)
                        t2.lt(90)
                        t2.fd(500)
                        t2.end_fill()

                        # Siffra
                        t2.penup()
                        t2.goto(0, 0)
                        t2.pendown()
                        t2.write(1, font=('arial', 100), align='center')

                        # Hålen
                        k = 0; n = 10; y = 355
                        while k < n:
                            k += 1; y -= 50
                            t2.penup()
                            t2.goto(-190, y)
                            t2.pendown()
                            t2.circle(5)

                        # lines
                        k = 0; n = 24; y = 330
                        while k < n:
                            k += 1; y -= 20
                            t2.width(1)
                            t2.penup()
                            t2.goto(-197, y)
                            t2.pendown()
                            t2.lt(90)
                            t2.fd(400)
                            t2.rt(90)

                        # redline
                        t2.penup()
                        t2.goto(-165, 327)
                        t2.pendown()
                        t2.color('red')
                        t2.fd(495)
                        t2.color('black')

                        t2.goto(-190,-200)
                        t2.write("(Click on this window to close)",font=("Bodoni MT",20,"normal"))

                        window2.exitonclick()

                        try:
                            turtle.bye()
                        except Exception:
                            pass

                    elif location.get_object() == 'Note with number _ 2 _ _':
                        
                        rootwindow = turtle.getcanvas().winfo_toplevel()
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
                        turtle.tracer(False)
                        window3 = turtle.Screen()
                        t3 = turtle.Turtle()
                        t3.hideturtle()
                        t3.speed(0)

                        # Pappret
                        t3.goto(-200, -170)
                        t3.begin_fill()
                        t3.fillcolor('beige')
                        t3.width(5)
                        t3.fd(400)
                        t3.lt(90)
                        t3.fd(500)
                        t3.lt(90)
                        t3.fd(400)
                        t3.lt(90)
                        t3.fd(500)
                        t3.end_fill()

                        # Siffra
                        t3.penup()
                        t3.goto(0, 0)
                        t3.pendown()
                        t3.write(2, font=('arial', 100), align='center')

                        # Hålen
                        k = 0; n = 10; y = 355
                        while k < n:
                            k += 1; y -= 50
                            t3.penup()
                            t3.goto(-190, y)
                            t3.pendown()
                            t3.circle(5)

                        # lines
                        k = 0; n = 24; y = 330
                        while k < n:
                            k += 1; y -= 20
                            t3.width(1)
                            t3.penup()
                            t3.goto(-197, y)
                            t3.pendown()
                            t3.lt(90)
                            t3.fd(400)
                            t3.rt(90)

                        # redline
                        t3.penup()
                        t3.goto(-165, 327)
                        t3.pendown()
                        t3.color('red')
                        t3.fd(495)
                        t3.color('black')

                        t3.goto(-190,-200)
                        t3.write("(Click on this window to close)",font=("Bodoni MT",20,"normal"))

                        window3.exitonclick()

                        try:
                            turtle.bye()
                        except Exception:
                            pass

                    if location.get_object() == 'Note with number _ _ 4 _':
                        
                        rootwindow = turtle.getcanvas().winfo_toplevel()
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
                        turtle.tracer(False)
                        window4 = turtle.Screen()
                        t4 = turtle.Turtle()
                        t4.hideturtle()
                        t4.speed(0)

                        # Pappret
                        t4.goto(-200, -170)
                        t4.begin_fill()
                        t4.fillcolor('beige')
                        t4.width(5)
                        t4.fd(400)
                        t4.lt(90)
                        t4.fd(500)
                        t4.lt(90)
                        t4.fd(400)
                        t4.lt(90)
                        t4.fd(500)
                        t4.end_fill()

                        # Siffra
                        t4.penup()
                        t4.goto(0, 0)
                        t4.pendown()
                        t4.write(4, font=('arial', 100), align='center')

                        # Hålen
                        k = 0; n = 10; y = 355
                        while k < n:
                            k += 1; y -= 50
                            t4.penup()
                            t4.goto(-190, y)
                            t4.pendown()
                            t4.circle(5)

                        # lines
                        k = 0; n = 24; y = 330
                        while k < n:
                            k += 1; y -= 20
                            t4.width(1)
                            t4.penup()
                            t4.goto(-197, y)
                            t4.pendown()
                            t4.lt(90)
                            t4.fd(400)
                            t4.rt(90)

                        # redline
                        t4.penup()
                        t4.goto(-165, 327)
                        t4.pendown()
                        t4.color('red')
                        t4.fd(495)
                        t4.color('black')
                        t4.goto(-190,-200)
                        t4.write("(Click on this window to close)",font=("Bodoni MT",20,"normal"))

                        window4.exitonclick()

                        try:
                            turtle.bye()
                        except Exception:
                            pass

                    elif location.get_object() == 'Note with number 7 _ _ _':
                        
                        rootwindow = turtle.getcanvas().winfo_toplevel()
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
                        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
                        turtle.tracer(False)
                        window5 = turtle.Screen()
                        t5 = turtle.Turtle()
                        t5.hideturtle()
                        t5.speed(0)

                        # Pappret
                        t5.goto(-200, -170)
                        t5.begin_fill()
                        t5.fillcolor('beige')
                        t5.width(5)
                        t5.fd(400)
                        t5.lt(90)
                        t5.fd(500)
                        t5.lt(90)
                        t5.fd(400)
                        t5.lt(90)
                        t5.fd(500)
                        t5.end_fill()

                        # Siffra
                        t5.penup()
                        t5.goto(0, 0)
                        t5.pendown()
                        t5.write(7, font=('arial', 100), align='center')

                        # Hålen
                        k = 0; n = 10; y = 355
                        while k < n:
                            k += 1; y -= 50
                            t5.penup()
                            t5.goto(-190, y)
                            t5.pendown()
                            t5.circle(5)

                        # lines
                        k = 0; n = 24; y = 330
                        while k < n:
                            k += 1; y -= 20
                            t5.width(1)
                            t5.penup()
                            t5.goto(-197, y)
                            t5.pendown()
                            t5.lt(90)
                            t5.fd(400)
                            t5.rt(90)

                        # redline
                        t5.penup()
                        t5.goto(-165, 327)
                        t5.pendown()
                        t5.color('red')
                        t5.fd(495)
                        t5.color('black')
                        t5.goto(-190,-190)
                        t5.write("(Click on this window to close)",font=("Bodoni MT",20,"normal"))

                        window5.exitonclick()

                        try:
                            turtle.bye()
                        except Exception:
                            pass


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
