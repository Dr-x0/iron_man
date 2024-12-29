import turtle

# إعدادات الشاشة
turtle.hideturtle()
turtle.bgcolor("#000000")
turtle.setup(500, 600)
turtle.speed(2)

# إحداثيات الوجه
face_one = [
    [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],
    [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]
]
face_two = [
    [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210)],
    [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]
]
face_three = [
    [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],
    [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220), (0, -220)]
]

# نقاط البداية
face_one_start = (0, 120)
face_two_start = (0, -30)
face_three_start = (0, -220)

def draw_face(face_details, start_point, color="#FFFC33"):
    turtle.penup()
    turtle.goto(start_point)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()

    # رسم الوجه
    for i in range(len(face_details[0])):
        x, y = face_details[0][i]
        turtle.goto(x, y)

    for i in range(len(face_details[1])):
        x, y = face_details[1][i]
        turtle.goto(x, y)
    
    turtle.end_fill()

def draw_eye(x_offset, y_offset):
    turtle.penup()
    turtle.goto(x_offset, y_offset)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

def draw_mouth():
    turtle.penup()
    turtle.goto(-50, -220)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(100, 120)

def change_color(x, y):
    if -100 < x < 100 and -100 < y < 100:
        draw_face(face_one, face_one_start, color="red")
    else:
        draw_face(face_one, face_one_start)

# رسم الوجه
draw_face(face_one, face_one_start)
draw_face(face_two, face_two_start)
draw_face(face_three, face_three_start)

# إضافة العينين والفم
draw_eye(-30, 50)
draw_eye(30, 50)
draw_mouth()

# التفاعل مع النقر
turtle.onscreenclick(change_color)

turtle.done()
