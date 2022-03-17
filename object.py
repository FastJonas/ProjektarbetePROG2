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
                    if location.get_object() == 'Staircasekey':
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
