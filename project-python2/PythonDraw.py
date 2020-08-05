#蟒蛇绘制

import turtle  #导入了绘图库

turtle.setup(650,350,200,200);  #setup函数用于控制窗体的大小，参数分别是（高度、宽度、x，y）
turtle.penup();
turtle.fd(-250);
turtle.pendown();
turtle.pensize(25);
turtle.pencolor("purple");
turtle.seth(-40);
for i in range(4):
    turtle.circle(40,80);
    turtle.circle(-40,80);
turtle.circle(40,80/2);
turtle.fd(40);
turtle.circle(16,180);
turtle.fd(40 * 2/3);
turtle.done();