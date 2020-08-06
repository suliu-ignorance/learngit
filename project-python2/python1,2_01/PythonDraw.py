#蟒蛇绘制

import turtle  #导入了绘图库

turtle.setup(650,350,200,200);  #setup函数用于控制窗体的大小，参数分别是（高度、宽度、x，y）
turtle.penup();
turtle.fd(-250);
turtle.pendown();
turtle.pensize(25);
turtle.pencolor("purple");
turtle.seth(-40);   #绝对角度
for i in range(4):
    turtle.circle(40,80);
    turtle.circle(-40,80);
turtle.circle(40,80/2);
turtle.fd(40);
turtle.circle(16,180);
turtle.fd(40 * 2/3);
turtle.done();


print("---------------------------------")
#知识点

'''
    1、库引用与import
        from和import保留字共同完成
            ①from <库名>import<函数名>
            
            ②from<库名>import*
            <函数名>(<函数参数>)
            
            ③import和as保留字共同完成。
                import<库名>as<库别名>
                <库别名>.<函数名>(<函数参数>)
                
  2、turtle画笔控制函数
    penup():画笔抬起
    pendown():画笔落下
    pensize(width):画笔宽度，海龟的腰围
    pencolor(color):color为颜色字符串或r，g，b值
        三种形式：
                    颜色字符串
                    RGB小数值
                    RGB元组值
  3、turtle运动控制函数
     fd(d):海龟走直线
        d为负数的话，海龟倒退走
     circle(r,extend):海龟走曲线
     r:圆心默认在海龟左侧的r处
     extend:绘制半径 
     
  4、turtle方向控制函数 
    
    
    绘制海龟面对的方向:绝对角度&海龟角度
        绝对角度: seth()
        海龟角度:right/left()
'''