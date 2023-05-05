from tkinter import *
import random as rd
from tkinter import messagebox as mb

def tetris():
    r = Tk()
    r.title("TETRIS!!")
    r.config(background='orange')
    c = Canvas(r,height='500',width='500',bg='#808080')
    lab_1 = Label(r,text='POINTS = 00',font=('Arial',20),background='orange')
    lab_1.pack()
    c.pack()
    spd = 300
    s = "shape_to_come"
    temp_ll = 0
    c.create_line(0,60,500,60,fill='white')
    c.create_line(0,61,500,61,fill='blue')

    points = 0

    present = []
    x0 = [i for i in range(0,481,20)]
    y0 = [i for i in range(0,481,20)]
    occupied = []
    for i in x0:
        occupied.append([i,480])
    for i in y0:
        if [0,i] not in occupied:
            occupied.append([0,i])
        if [480,i] not in occupied:
            occupied.append([480,i])

    lenx = len(occupied)

    c_s = []
    clrs = ['red','blue','orange','green','yellow','brown','purple','pink']
    cc = rd.choice(clrs)

    bdr_sqr = [c.create_rectangle(0,0,20,500,fill='black'),
            c.create_rectangle(480,0,500,500,fill='black'),
            c.create_rectangle(0,480,500,500,fill='black')]

    def check_line():
        nonlocal occupied,x0,present,lenx,points
        y = [i for i in range(20,461,20)]
        pt = 0
        count = 0
        done_x = 0
        done_y = 0
        for i in y:
            for j in occupied:
                if j[1] == i:
                    count+=1
            if count == len(x0):
                pt+=1
                for m in range(20,461,20):
                    for n in present:
                        if (n[0] == m) and (n[1] == i):
                            c.delete(n[2])
                            done_x = n[0]
                            done_y = n[1]
                            present.remove(n)
                            occupied.remove([n[0],n[1]])
                c.delete('all')
                c.create_line(0,60,500,60,fill='white')
                c.create_line(0,61,500,61,fill='blue')
                c.create_rectangle(0,0,20,500,fill='black'),
                c.create_rectangle(480,0,500,500,fill='black'),
                c.create_rectangle(0,480,500,500,fill='black')
                for i in occupied[lenx:]:
                    if i[1]<=done_y:
                        i[1]+=20
                for i in present:
                    if i[1]<=done_y:
                        i[1]+=20
                    i[2] = c.create_rectangle(i[0],i[1],i[0]+20,i[1]+20,fill=i[len(i)-1],width='2')
            count= 0
        points = points + 100*(pt)*(pt)
        lab_1.config(text = 'POINTS = '+str(points))

    def check_below():
        nonlocal c_s
        temp = 1
        for i in c_s:
            x1 = i[0]
            y1 = i[1]
            if [x1,y1+20] in occupied:
                temp = 0
        return temp

    def check_r():
        nonlocal c_s
        temp_r = 1
        for i in c_s:
            a = i[0]
            b = i[1]
            if [a+20,b] in occupied:
                temp_r = 0
        return temp_r

    def check_l():
        global c_s
        temp_l = 1
        for i in c_s:
            a = i[0]
            b = i[1]
            if [a-20,b] in occupied:
                temp_l = 0
        return temp_l

    def sqrr(x,y,st):
        nonlocal c_s,cc
        c_s.append([x,y,c.create_rectangle(int(x),int(y),int(x)+20,int(y)+20,fill=cc,width='2'),st,cc])

    def check_finish():
        nonlocal c_s,occupied
        for i in c_s:
            y = i[1]
            if y == 60:
                return 0
            else:
                return 1

    def shape(x,y):
        nonlocal c_s,s,cc,clrs,spd,temp_ll
        shapes = ['sqr','line','left_hump','right_hump','2_hump','mid_hump','s','z']
        s = rd.choice(shapes)
        #s = 'line'
        cc = clrs[shapes.index(s)]
        if temp_ll == 0:
            temp_ll = 1
        elif temp_ll == 1:
            check_line()
        if s == 'sqr':
            c_s = []
            sqrr(x,y,0)
            sqrr(x+20,y+20,0)
            sqrr(x,y+20,0)
            sqrr(x+20,y,0)
        elif s == 'line':
            c_s = []
            sqrr(x,y,0)
            sqrr(x+20,y,0)
            sqrr(x+40,y,0)
            sqrr(x+60,y,0)
        elif s == 'left_hump':
            c_s = []
            sqrr(x,y,1)
            sqrr(x+20,y+20,1)
            sqrr(x,y+20,1)
            sqrr(x+40,y+20,1)
        elif s == 'right_hump':
            c_s = []
            sqrr(x,y,1)
            sqrr(x-20,y+20,1)
            sqrr(x,y+20,1)
            sqrr(x-40,y+20,1)
        elif s == '2_hump':
            c_s = []
            sqrr(x,y,1)
            sqrr(x+20,y+20,1)
            sqrr(x,y+20,1)
            sqrr(x+40,y+20,1)
            sqrr(x+40,y,1)
        elif s == 'mid_hump':
            c_s = []
            sqrr(x,y,1)
            sqrr(x+20,y,1)
            sqrr(x,y-20,1)
            sqrr(x-20,y,1)
        elif s == 'z':
            c_s = []
            sqrr(x,y,0)
            sqrr(x+20,y,0)
            sqrr(x,y+20,0)
            sqrr(x-20,y+20,0)
        elif s == 's':
            c_s = []
            sqrr(x,y,0)
            sqrr(x-20,y,0)
            sqrr(x,y+20,0)
            sqrr(x+20,y+20,0)
        dwn_mov()

    def dwn_mov():
        nonlocal c_s,cc,spd,present
        for i in c_s:
            c.delete(i[2])
        for i in c_s:
            x1 = i[0]
            y1 = i[1]
            i[2] = c.create_rectangle(x1,y1+20,x1+20,y1+40,fill=cc,width='2')
            i[1]+=20
        temp = check_below() 
        if temp == 0:
            for i in c_s:
                if [i[0],i[1]] not in occupied:
                    occupied.append([i[0],i[1]])
                    present.append(i)
            mm = check_finish()
            if mm == 1:
                shape(200,0)
            elif mm == 0:
                 a = mb.showerror("Game Over","YOU LOST")
                 if a == "ok":
                    r.destroy()
                    tetris()

                
        else:
            r.after(spd,dwn_mov)

    def rgt_mov(event):
        nonlocal c_s,cc
        temp_r = check_r()
        if temp_r == 1:
            for i in c_s:
                c.delete(i[2])
            for i in c_s:
                a = i[0]
                b = i[1]
                i[2] = c.create_rectangle(a+20,b,a+40,b,fill=cc,width='2')
                i[0]+=20

    def lft_mov(event):
        nonlocal c_s,cc
        temp_l = check_l()
        if temp_l == 1:
            for i in c_s:
                c.delete(i[2])
            for i in c_s:
                a = i[0]
                b = i[1]
                i[2] = c.create_rectangle(a-20,b,a,b,fill=cc,width='2')
                i[0]-=20

    def rot(event):
        nonlocal c_s,s,cc
        for i in c_s:
            c.delete(i[2])
        if s == "sqr":
            pass
        elif s == "line":
            if c_s[0][1] == c_s[1][1]:
                if ([c_s[1][0],c_s[0][1]+20] not in occupied) and ([c_s[1][0],c_s[0][1]+40] not in occupied):
                    x11 = c_s[0][0]+20
                    y11 = c_s[0][1]-20
                    for i in c_s:
                        i[2] = c.create_rectangle(x11,y11,x11+20,y11+20,fill=cc,width='2')
                        i[0] = x11
                        i[1] = y11
                        y11+=20
                else:
                    pass
            else:
                if ([c_s[1][0]-20,c_s[1][1]] not in occupied) and ([c_s[1][0]+20,c_s[1][1]] not in occupied) and ([c_s[1][0]+40,c_s[1][1]] not in occupied):
                    x11 = c_s[0][0]-20
                    y11 = c_s[0][1]+20
                    for i in c_s:
                        i[2] = c.create_rectangle(x11,y11,x11+20,y11+20,fill=cc,width='2')
                        i[0] = x11
                        i[1] = y11
                        x11+=20
        elif s == "s":
            if c_s[0][1] == c_s[1][1]:
                if ([c_s[0][0]-20,c_s[0][1]+20] not in occupied):
                    x11 = c_s[0][0]
                    y11 = c_s[0][1]
                    c_s[0] = [x11,y11,c.create_rectangle(x11,y11,x11+20,y11+20,fill=cc,width='2'),cc]
                    c_s[1] = [x11,y11-20,c.create_rectangle(x11,y11-20,x11+20,y11,fill=cc,width='2'),cc]
                    c_s[2] = [x11-20,y11,c.create_rectangle(x11-20,y11,x11,y11+20,fill=cc,width='2'),cc]
                    c_s[3] = [x11-20,y11+20,c.create_rectangle(x11-20,y11+20,x11,y11+40,fill=cc,width='2'),cc]
            else:
                if ([c_s[0][0]+20,c_s[0][1]+20] not in occupied) and ([c_s[0][0],c_s[0][1]+20] not in occupied):
                    x11 = c_s[0][0]
                    y11 = c_s[0][1]
                    c_s[0] = [x11,y11,c.create_rectangle(x11,y11,x11+20,y11+20,fill=cc,width='2'),cc]
                    c_s[1] = [x11-20,y11,c.create_rectangle(x11-20,y11,x11,y11+20,fill=cc,width='2'),cc]
                    c_s[2] = [x11,y11+20,c.create_rectangle(x11,y11+20,x11+20,y11+40,fill=cc,width='2'),cc]
                    c_s[3] = [x11+20,y11+20,c.create_rectangle(x11+20,y11+20,x11+40,y11+40,fill=cc,width='2'),cc]
        elif s == "z":
            if c_s[0][1] == c_s[1][1]:
                if ([c_s[0][0]+20,c_s[0][1]+20] not in occupied):
                    x11 = c_s[0][0]
                    y11 = c_s[0][1]
                    c_s[0] = [x11,y11,c.create_rectangle(x11,y11,x11+20,y11+20,fill=cc,width='2'),cc]
                    c_s[1] = [x11,y11-20,c.create_rectangle(x11,y11-20,x11+20,y11,fill=cc,width='2'),cc]
                    c_s[2] = [x11+20,y11,c.create_rectangle(x11+20,y11,x11+40,y11+20,fill=cc,width='2'),cc]
                    c_s[3] = [x11+20,y11+20,c.create_rectangle(x11+20,y11+20,x11+40,y11+40,fill=cc,width='2'),cc]
            else:
                if ([c_s[0][0]-20,c_s[0][1]+20] not in occupied) and ([c_s[0][0],c_s[0][1]+20] not in occupied):
                    x11 = c_s[0][0]
                    y11 = c_s[0][1]
                    c_s[0] = [x11,y11,c.create_rectangle(x11,y11,x11+20,y11+20,fill=cc,width='2'),cc]
                    c_s[1] = [x11+20,y11,c.create_rectangle(x11+20,y11,x11+40,y11+20,fill=cc,width='2'),cc]
                    c_s[2] = [x11,y11+20,c.create_rectangle(x11,y11+20,x11+20,y11+40,fill=cc,width='2'),cc]
                    c_s[3] = [x11-20,y11+20,c.create_rectangle(x11-20,y11+20,x11,y11+40,fill=cc,width='2'),cc]
        elif s == "mid_hump":
            state = c_s[0][3]
            lst = []
            x = c_s[0][0]
            y = c_s[0][1]
            chk2 = 1
            if (state == 1) and ([x,y+20] in occupied):
                chk2 = 0
            elif (state == 2) and ([x+20,y] in occupied):
                chk2 = 0
            elif (state == 4) and ([x-20,y] in occupied):
                chk2 = 0        
            if chk2 == 1:
                if state<4:
                    state+=1
                else:
                    state = 1
                lst.insert(0,[x,y,c.create_rectangle(int(x),int(y),int(x)+20,int(y)+20,fill=cc,width='2'),state,cc])
                lst.insert(1,[x,y+20,c.create_rectangle(int(x),int(y),int(x)+20,int(y)+20,fill=cc,width='2'),state,cc])
                lst.insert(2,[x+20,y,c.create_rectangle(int(x),int(y),int(x)+20,int(y)+20,fill=cc,width='2'),state,cc])
                lst.insert(3,[x,y-20,c.create_rectangle(int(x),int(y),int(x)+20,int(y)+20,fill=cc,width='2'),state,cc])
                lst.insert(4,[x-20,y,c.create_rectangle(int(x),int(y),int(x)+20,int(y)+20,fill=cc,width='2'),state,cc])
                c.delete(lst[state][2])
                lst.pop(state)
                c_s = []
                for i in lst:
                    c_s.append(i)
                lst = []
        elif s == '2_hump':
            state = c_s[0][3]
            lst = []
            x = c_s[0][0]
            y = c_s[0][1]
            if (state == 1):
                c.delete(c_s[0][2])
                c.delete(c_s[2][2])
                c_s[0] = [x+20,y-20,c.create_rectangle(int(x+20),int(y-20),int(x)+40,int(y),fill=cc,width='2'),2,cc]
                c_s[1][3] = 2
                c_s[2] = [x+40,y-20,c.create_rectangle(int(x+40),int(y-20),int(x)+60,int(y),fill=cc,width='2'),2,cc]
                c_s[3][3] = 2
                c_s[4][3] = 2
            elif (state == 2) and ([x-20,y] not in occupied) and ([x-20,y+20] not in occupied):
                c.delete(c_s[1][2])
                c.delete(c_s[3][2])
                c_s[0][3] = 3
                c_s[1] = [x-20,y,c.create_rectangle(int(x-20),int(y),int(x),int(y)+20,fill=cc,width='2'),3,cc]
                c_s[2][3] = 3
                c_s[3] = [x-20,y+20,c.create_rectangle(int(x-20),int(y+20),int(x),int(y)+40,fill=cc,width='2'),3,cc]
                c_s[4][3] = 3
            elif (state == 3) and ([x-20,y+40] not in occupied) and ([x,y+40] not in occupied):
                c.delete(c_s[2][2])
                c.delete(c_s[4][2])
                c_s[0][3] = 4
                c_s[1][3] = 4
                c_s[2] = [x-20,y+40,c.create_rectangle(int(x-20),int(y+40),int(x),int(y)+60,fill=cc,width='2'),4,cc]
                c_s[3][3] = 4
                c_s[4] = [x,y+40,c.create_rectangle(int(x),int(y+40),int(x)+20,int(y)+60,fill=cc,width='2'),4,cc]
            elif (state == 4) and ([x+20,y+20] not in occupied) and ([x+20,y+40] not in occupied):
                c.delete(c_s[0][2])
                c.delete(c_s[1][2])
                c.delete(c_s[2][2])
                c.delete(c_s[3][2])
                c.delete(c_s[4][2])
                x = x-20
                y = y+20
                c_s = [[x,y,c.create_rectangle(int(x),int(y),int(x)+20,int(y)+20,fill=cc,width='2'),1,cc],
                    [x+20,y+20,c.create_rectangle(int(x+20),int(y+20),int(x+20)+20,int(y+20)+20,fill=cc,width='2'),1,cc],
                    [x,y+20,c.create_rectangle(int(x),int(y+20),int(x)+20,int(y+20)+20,fill=cc,width='2'),1,cc],
                    [x+40,y+20,c.create_rectangle(int(x+40),int(y+20),int(x+40)+20,int(y+20)+20,fill=cc,width='2'),1,cc],
                    [x+40,y,c.create_rectangle(int(x+40),int(y),int(x+40)+20,int(y)+20,fill=cc,width='2'),1,cc]]
        elif s == 'left_hump':
            state = c_s[0][3]
            if (state == 1):
                x = c_s[0][0]
                y = c_s[0][1]
                if ([x+40,y] not in occupied) and ([x+40,y-20] not in occupied):
                    c.delete(c_s[0][2])
                    c.delete(c_s[2][2])
                    c_s[0] = [x+40,y,c.create_rectangle(int(x+40),int(y),int(x)+60,int(y)+20,fill=cc,width='2'),2,cc]
                    c_s[1][3] = 2
                    c_s[2] = [x+40,y-20,c.create_rectangle(int(x+40),int(y-20),int(x)+60,int(y),fill=cc,width='2'),2,cc]
                    c_s[3][3] = 2
            elif (state == 2):
                x = c_s[0][0]
                y = c_s[0][1]
                if ([x-40,y] not in occupied) and ([x-20,y] not in occupied):
                    c.delete(c_s[2][2])
                    c.delete(c_s[1][2])
                    c_s[0][3] = 3
                    c_s[1] = [x-40,y,c.create_rectangle(int(x-40),int(y),int(x)-20,int(y)+20,fill=cc,width='2'),3,cc]
                    c_s[2] = [x-20,y,c.create_rectangle(int(x-20),int(y),int(x),int(y)+20,fill=cc,width='2'),4,cc]
                    c_s[3][3] = 3
            elif (state == 3):
                x = c_s[0][0]
                y = c_s[0][1]
                if ([x-40,y+20] not in occupied) and ([x-40,y-20] not in occupied):
                    c.delete(c_s[0][2])
                    c.delete(c_s[1][2])
                    c.delete(c_s[3][2])
                    c.delete(c_s[2][2])
                    c_s[0] =  [x-20,y-20,c.create_rectangle(int(x-20),int(y-20),int(x),int(y),fill=cc,width='2'),4,cc]
                    c_s[1] =  [x-40,y-20,c.create_rectangle(int(x-40),int(y-20),int(x)-20,int(y),fill=cc,width='2'),4,cc]
                    c_s[2] =  [x-40,y,c.create_rectangle(int(x-40),int(y),int(x)-20,int(y)+20,fill=cc,width='2'),4,cc]
                    c_s[3] =  [x-40,y+20,c.create_rectangle(int(x-40),int(y+20),int(x-20),int(y)+40,fill=cc,width='2'),4,cc]
            elif (state == 4):
                x = c_s[0][0]
                y = c_s[0][1]
                if ([x,y+40] not in occupied) and ([x+20,y+40] not in occupied):
                    c.delete(c_s[0][2])
                    c.delete(c_s[1][2])
                    c.delete(c_s[2][2])
                    c.delete(c_s[3][2])
                    x = x-20
                    y = y+20
                    c_s = [[x,y,c.create_rectangle(int(x),int(y),int(x)+20,int(y)+20,fill=cc,width='2'),1,cc],
                        [x+20,y+20,c.create_rectangle(int(x+20),int(y+20),int(x+20)+20,int(y+20)+20,fill=cc,width='2'),1,cc],
                        [x,y+20,c.create_rectangle(int(x),int(y+20),int(x)+20,int(y+20)+20,fill=cc,width='2'),1,cc],
                        [x+40,y+20,c.create_rectangle(int(x+40),int(y+20),int(x+40)+20,int(y+20)+20,fill=cc,width='2'),1,cc]]
        elif s == 'right_hump':
            state = c_s[0][3]
            if state == 1:
                x = c_s[0][0]
                y = c_s[0][1]
                if ([x,y-20] not in occupied) and ([x-20,y-20] not in occupied):
                    c.delete(c_s[1][2])
                    c.delete(c_s[3][2])
                    c_s[0][3] = 2
                    c_s[1] = [x,y-20,c.create_rectangle(int(x),int(y-20),int(x)+20,int(y),fill=cc,width='2'),2,cc]
                    c_s[2][3] = 2
                    c_s[3] = [x-20,y-20,c.create_rectangle(int(x-20),int(y-20),int(x),int(y),fill=cc,width='2'),2,cc]
            elif state == 2:
                x = c_s[0][0]
                y = c_s[0][1]
                if ([x-40,y] not in occupied) and ([x-40,y-20] not in occupied):
                    c.delete(c_s[0][2])
                    c.delete(c_s[2][2])
                    c_s[0] = [x-40,y,c.create_rectangle(int(x-40),int(y),int(x)-20,int(y)+20,fill=cc,width='2'),3,cc]
                    c_s[1][3] = 3
                    c_s[2] = [x-40,y-20,c.create_rectangle(int(x-40),int(y-20),int(x)-20,int(y),fill=cc,width='2'),3,cc]
            elif state == 3:
                x = c_s[0][0]
                y = c_s[0][1]
                if ([x,y+20] not in occupied) and ([x+20,y+20] not in occupied):
                    c.delete(c_s[1][2])
                    c.delete(c_s[3][2])
                    c_s[0][3] = 4
                    c_s[1] = [x,y+20,c.create_rectangle(int(x),int(y+20),int(x)+20,int(y)+40,fill=cc,width='2'),4,cc]
                    c_s[2][3] = 4
                    c_s[3] = [x+20,y+20,c.create_rectangle(int(x+20),int(y+20),int(x)+40,int(y)+40,fill=cc,width='2'),4,cc]
            elif state == 4:
                x = c_s[0][0]
                y = c_s[0][1]
                if ([x+40,y+20] not in occupied) and ([x+40,y] not in occupied):
                    x = x+40
                    c.delete(c_s[0][2])
                    c.delete(c_s[1][2])
                    c.delete(c_s[2][2])
                    c.delete(c_s[3][2])
                    c_s = [[x,y,c.create_rectangle(int(x),int(y),int(x)+20,int(y)+20,fill=cc,width='2'),1,cc],
                        [x-20,y+20,c.create_rectangle(int(x-20),int(y+20),int(x-20)+20,int(y+20)+20,fill=cc,width='2'),1,cc],
                        [x,y+20,c.create_rectangle(int(x),int(y+20),int(x)+20,int(y+20)+20,fill=cc,width='2'),1,cc],
                        [x-40,y+20,c.create_rectangle(int(x-40),int(y+20),int(x-40)+20,int(y+20)+20,fill=cc,width='2'),1,cc]]

    r.bind('<Right>',rgt_mov)
    r.bind('<Left>',lft_mov)
    r.bind('<space>',rot)
    shape(260,0)
    r.mainloop()

tetris()