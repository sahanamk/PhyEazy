from tkinter import*
import tkinter
import os

phy=Tk()
phy.title('PhyEazy - Physics Tutorials')
canvas=Canvas(phy, width=1500, height=900, bg='grey12')
canvas.pack(expand=YES,fill=BOTH)

icon=PhotoImage(file="icon1.png")
piclabel=Label(canvas, bg='grey12', image=icon, height=427, width=377)
piclabel.image=icon
piclabel.pack()

#Home page
def Start1():
    #classses
    phy_start=Tk()
    canvas_start=Canvas(phy_start, width=1500, height=900, bg='grey12')
    canvas_start.pack(expand=YES,fill=BOTH)
    
    def Back_Start():
        phy_start.destroy()
    
    def Class7():
        phy_class7=Tk()
        phy_class7.title('Class 7')
        canvas_class7=Canvas(phy_class7, width=1500, height=900, bg='grey12')
        canvas_class7.pack(expand=YES,fill=BOTH)
        
        def Back7():
            phy_class7.destroy()
        
        def Quiz7():
            phy_Quiz7=Tk()
            phy_Quiz7.title('Quiz')
            canvas_Quiz7=Canvas(phy_Quiz7, width=1500, height=900, bg='grey12')
            canvas_Quiz7.pack(expand=YES,fill=BOTH)
            
            def play():
                import PlayQuiz7
                PlayQuiz7.PlayQuiz()
                
            play7=Button(phy_Quiz7, bg='coral2',font=('Castellar',30), text='Play Quiz', command=play)
            play7.pack()
            play7.place(relx=.40,rely=.35)
            
            def add():
                import Quiz7
                
            quiz7=Button(phy_Quiz7, bg='coral2', font=('Castellar',30),text='Add Questions', command=add)
            quiz7.pack()
            quiz7.place(relx=.36,rely=.55)
            
            def Back_Quiz7():
                phy_Quiz7.destroy()
            
            Back_Quiz7=Button(phy_Quiz7, bg='coral2', text='<--', command=Back_Quiz7)
            Back_Quiz7.pack()
            Back_Quiz7.place(relx=.0,rely=.0)
                    
        #chapters of class 7
        def Light7():
            phy_Light7=Tk()
            phy_Light7.title('Light')
            canvas_Light7=Canvas(phy_Light7, width=1500, height=900, bg='white')
            canvas_Light7.pack(expand=YES,fill=BOTH)
            
            canvas_Light7.create_text(720,40,text='LIGHT', font=('Times New Roman',27), fill = 'black')
            canvas_Light7.create_rectangle(182,170,202,270, fill='lavender')
            canvas_Light7.create_oval(186,148,198,170, fill='orange')
            canvas_Light7.create_polygon(220,148,417,126,420,148,222,170 , fill='gray64', outline='black')
            canvas_Light7.create_oval(208,147,224,170,fill='gray58')
            canvas_Light7.create_text(260,100,text='Side view', font=('courier',14), fill = 'black')
            canvas_Light7.create_text(770,100,text='Front view', font=('courier',14), fill = 'black')
            canvas_Light7.create_oval(770,175,782,198, fill='orange')
            canvas_Light7.create_oval(750,150,800,200, outline='black')
            canvas_Light7.create_text(500,320,text='(i) Light passing through a straight pipe', font=('courier',14), fill = 'black')
            
            canvas_Light7.create_rectangle(182,600,202,700, fill='lavender')
            canvas_Light7.create_oval(186,600,198,578, fill='orange')
            canvas_Light7.create_polygon(220,570,305,550,344,585,375,530,460,510,464,530,382,550,346,610,302,570,224,590 , fill='gray64', outline='black')
            canvas_Light7.create_oval(208,569,225,593,fill='gray58')
            canvas_Light7.create_text(260,485,text='Side view', font=('courier',14), fill = 'black')
            canvas_Light7.create_text(770,485,text='Front view', font=('courier',14), fill = 'black')
            canvas_Light7.create_oval(750,540,800,590, fill='grey17')
            
            canvas_Light7.create_text(500,700,text='(ii) Light passing through a bent pipe', font=('courier',14), fill = 'black')
            canvas_Light7.create_text(1000,250,text='''\t\t\t\t      In fig(i) the candle light is seen 
                                      through the straight pipe whereas 
                                      in fig(ii) the candle light cannot 
                                      be seen through the bent pipe.''', font=('courier',14), fill = 'black')
            canvas_Light7.create_text(1000,450,text='''\t\t\tTherefore we can say that, 
                                     \tLight travels in a straight line.''', font=('Bookman Old Style',22,'bold'), fill = 'black')

            def Back_Light7():
                phy_Light7.destroy()
            
            Back_Light7=Button(phy_Light7, bg='coral2', text='<--', command=Back_Light7)
            Back_Light7.pack()
            Back_Light7.place(relx=.0,rely=.0)
            
            def page2_Light7():
                phy_page2_Light7=Tk()
                phy_page2_Light7.title('Light')
                canvas_page2_Light7=Canvas(phy_page2_Light7, width=1500, height=900, bg='white')
                canvas_page2_Light7.pack(expand=YES,fill=BOTH)
                
                canvas_page2_Light7.create_text(750,60,text='Reflection of light on a plane mirror', font=('Yu Gothic UI Semibold',22), fill = 'black')
                canvas_page2_Light7.create_rectangle(180,150,350,340, fill='brown2')
                canvas_page2_Light7.create_rectangle(200,170,330,320, fill='mint cream')
                canvas_page2_Light7.create_rectangle(290,300,310,400, fill='lavender')
                canvas_page2_Light7.create_oval(294,278,306,300,fill='orange')
                canvas_page2_Light7.create_rectangle(250,240,270,320, fill='lavender')
                canvas_page2_Light7.create_oval(254,218,266,240,fill='orange')
                
                canvas_page2_Light7.create_text(280,440,text='(i)Reflection of a candle in a plane mirror', font=('courier',14), fill = 'black')
                canvas_page2_Light7.create_text(30,550,text='''\t\t\t\t\t\tThe image formed by a plane mirrior 
                                                is always virtual, upright, and
                                                of the same shape and size as 
                                                that of the object it is reflecting 
                                                as seen in fig(i).''', font=('courier',14), fill = 'black')
                canvas_page2_Light7.create_line(1100,200,1100,600)
                
                for i in range(0,420,20):
                    canvas_page2_Light7.create_line(1100,i+200,1115,i+200+10)
                
                canvas_page2_Light7.create_rectangle(1390,300,1410,400, fill='lavender', outline='grey70')
                canvas_page2_Light7.create_oval(1394,278,1406,300,fill='orange', outline='grey70')
                canvas_page2_Light7.create_rectangle(790,300,810,400, fill='lavender')
                canvas_page2_Light7.create_oval(794,278,806,300,fill='orange')
                
                canvas_page2_Light7.create_line(799,278,1100,450)
                canvas_page2_Light7.create_line(790,400,1100,515)
                canvas_page2_Light7.create_line(1401,278,1100,450, fill='gray67')
                canvas_page2_Light7.create_line(1410,400,1100,515, fill='gray67')
                canvas_page2_Light7.create_line(760,630,1100,450)
                canvas_page2_Light7.create_line(760,630,1100,515)
                
                canvas_page2_Light7.create_polygon(904,325,910,340,895,345, fill='black')
                canvas_page2_Light7.create_polygon(904,430,910,445,895,450, fill='black')
                canvas_page2_Light7.create_polygon(990,520,973,516,981,497, fill='black')
                canvas_page2_Light7.create_polygon(1006,557,990,551,1000,535, fill='black')
                canvas_page2_Light7.create_polygon(1285,357,1270,352,1280,337, fill='grey70')
                canvas_page2_Light7.create_polygon(1305,450,1290,445,1300,430, fill='grey70')
                
                canvas_page2_Light7.create_text(810,460,text='Object', font=('courier',16), fill = 'black')
                canvas_page2_Light7.create_text(1410,460,text='Image', font=('courier',16), fill = 'black')
                canvas_page2_Light7.create_text(1100,660,text='Plane mirror', font=('courier',16), fill = 'black')
                canvas_page2_Light7.create_text(740,670,text='Eye', font=('courier',16), fill = 'black')
                
                def Back_page2_Light7():
                    phy_page2_Light7.destroy()
                
                Back_page2_Light7=Button(phy_page2_Light7, bg='coral2', text='<--', command=Back_page2_Light7)
                Back_page2_Light7.pack()
                Back_page2_Light7.place(relx=.0,rely=.0)
                
                def page3_Light7():
                    phy_page3_Light7=Tk()
                    phy_page3_Light7.title('Light')
                    canvas_page3_Light7=Canvas(phy_page3_Light7, width=1500, height=900, bg='white')
                    canvas_page3_Light7.pack(expand=YES,fill=BOTH)
                    
                    canvas_page3_Light7.create_text(750,40, text='Laws of Reflection', font=('Yu Gothic UI Semibold',22), fill = 'black')
                    canvas_page3_Light7.create_line(500,350,1000,350)
                    
                    for i in range(500,1001,20):
                        canvas_page3_Light7.create_line(i,350,i+10,360)
                    
                    canvas_page3_Light7.create_line(500,200,750,350)
                    canvas_page3_Light7.create_line(1000,200,750,350)

                    for i in range(180,350,15):
                        canvas_page3_Light7.create_line(750,i,750,i+10)
                    
                    canvas_page3_Light7.create_text(400,600, text='''\t\t\t\t\t\t     The laws of reflection of light are;
                                                    
                                                    (i)The incident ray, the reflected ray and 
                                                    the normal to the mirror at the point of
                                                    incidence all lie in the same plane.
                                                    
                                                    (ii)The angle of incidence is equal to the 
                                                    angle of reflection.''', font=('courier',16), fill='black')
                    
                    canvas_page3_Light7.create_arc(715,310,760,340, style=ARC, start=60, extent=140)
                    canvas_page3_Light7.create_arc(785,310,740,340, style=ARC,start=340, extent=140)
                    
                    canvas_page3_Light7.create_text(370,230, text='''\t\t\t\t\t\t     angle of 
                                                    incidence''', font=('courier',14), fill = 'black')
                    canvas_page3_Light7.create_text(550,230, text='''\t\t\t\t\t\t     angle of 
                                                    reflection''', font=('courier',14), fill = 'black')
                   
                    canvas_page3_Light7.create_text(750,330, text='i  r', font=('courier',14), fill = 'black')
                    canvas_page3_Light7.create_text(750,160, text='normal', font=('courier',14), fill = 'black')
                    canvas_page3_Light7.create_text(750,380, text='mirror', font=('courier',14), fill = 'black')
                    canvas_page3_Light7.create_text(430,220, text='incident ray', font=('courier',14), fill = 'black')
                    canvas_page3_Light7.create_text(1070,220, text='reflected ray', font=('courier',14), fill = 'black')
                    
                    canvas_page3_Light7.create_polygon(560,220,570,243,540,240, fill = 'black')
                    canvas_page3_Light7.create_polygon(943,235,930,257,910,240, fill = 'black')
                    
                    canvas_page3_Light7.create_rectangle(650,730,750,770, fill = 'PaleTurquoise1')
                    canvas_page3_Light7.create_text(700,750, text='i=r', font=('courier',14), fill = 'black')

                    def Back_page3_Light7():
                        phy_page3_Light7.destroy()
                
                    Back_page3_Light7=Button(phy_page3_Light7, bg='coral2', text='<--', command=Back_page3_Light7)
                    Back_page3_Light7.pack()
                    Back_page3_Light7.place(relx=.0,rely=.0)
                    
                    def page4_Light7():
                        phy_page4_Light7=Tk()
                        phy_page4_Light7.title('Light')
                        canvas_page4_Light7=Canvas(phy_page4_Light7, width=1500, height=900, bg='white')
                        canvas_page4_Light7.pack(expand=YES,fill=BOTH)
                        
                        canvas_page4_Light7.create_text(700,40,text='Spherical mirrors', font=('Yu Gothic UI Semibold',22), fill = 'black')
                        
                        canvas_page4_Light7.create_arc(200,100,300,240, style=ARC, start=270, extent=180)
                        canvas_page4_Light7.create_text(300,360, text='Concave mirror', font=('courier',16), fill = 'black')
                        
                        canvas_page4_Light7.create_arc(950,100,1050,240, style=ARC, start=90, extent=180)
                        canvas_page4_Light7.create_text(1000,360, text='Convex mirror', font=('courier',16), fill = 'black')
                        
                        canvas_page4_Light7.create_text(800,560,text='''\t\t\t\t\t\t        Image formed by a convex mirror is erect, virtual and
                                                        smaller in size than the object.
                                                        
                                                        The mirrors used as side mirrors in scooters are convex
                                                        mirrors. Convex mirrors can form images of objects spread
                                                        over a large area. So, these help the drivers to see the
                                                        traffic behind them.''',font=('courier',14), fill = 'black')
                                                        
                        canvas_page4_Light7.create_text(100,600,text='''\t\t\t\t\t\t        A concave mirror can form a real and inverted image. 
                                                        When the object is placed very close to the mirror, 
                                                        the image formed is virtual, erect and magnified.
                                                        
                                                        Concave mirrors are used for many purposes. You might
                                                        have seen doctors using concave mirrors for examining
                                                        eyes, ears, nose and throat. Concave mirrors are also
                                                        used by dentists to see an enlarged image of the teeth.
                                                        The reflectors of torches, headlights of cars and 
                                                        scooters are concave in shape''', font=('courier',14), fill = 'black')
                        
                        j=260
                        k=0
                        for i in range(100,240,15):
                            canvas_page4_Light7.create_line(j,i,j+15,i+4, fill='black')
                            j=j+15-k
                            k+=3.5
                        j=990
                        k=0
                        for i in range(100,240,15):
                            canvas_page4_Light7.create_line(j,i,j+15,i+7, fill='black')
                            j=j-15+k
                            k+=3.5
                            
                        def Back_page4_Light7():
                            phy_page4_Light7.destroy()
                            
                        Back_page4_Light7=Button(phy_page4_Light7, bg='coral2', text='<--', command=Back_page4_Light7)
                        Back_page4_Light7.pack()
                        Back_page4_Light7.place(relx=.0,rely=.0)
                        
                        def page5_Light7():
                            phy_page5_Light7=Tk()
                            phy_page5_Light7.title('Light')
                            canvas_page5_Light7=Canvas(phy_page5_Light7, width=1500, height=900, bg='white')
                            canvas_page5_Light7.pack(expand=YES,fill=BOTH)
                            
                            canvas_page5_Light7.create_text(700,40,text='Lenses', font=('Yu Gothic UI Semibold',22), fill = 'black')
                            canvas_page5_Light7.create_arc(250,100,300,300, style=ARC, start=295, extent=133)
                            canvas_page5_Light7.create_arc(270,100,320,300, style=ARC, start=112, extent=135)
                            canvas_page5_Light7.create_text(300,360, text='Convex lens', font=('courier',16), fill = 'black')
                            canvas_page5_Light7.create_arc(1020,100,1120,300, style=ARC, start=110, extent=140)
                            canvas_page5_Light7.create_arc(900,100,1000,300, style=ARC, start=290, extent=140)
                            canvas_page5_Light7.create_line(968,106,1053,106, fill='black')                            
                            canvas_page5_Light7.create_line(968,294,1053,294, fill='black')
                            canvas_page5_Light7.create_text(1000,360, text='Concave lens', font=('courier',16), fill = 'black')
                            
                            canvas_page5_Light7.create_line(100,108,287,108, fill='black')                            
                            canvas_page5_Light7.create_line(100,292,287,292, fill='black')
                            canvas_page5_Light7.create_line(287,108,450,170, fill='black')                            
                            canvas_page5_Light7.create_line(287,292,450,240, fill='black')
                            
                            canvas_page5_Light7.create_line(800,106,1015,106, fill='black')                            
                            canvas_page5_Light7.create_line(800,294,1015,294, fill='black')
                            canvas_page5_Light7.create_line(1015,106,1115,56, fill='black')                            
                            canvas_page5_Light7.create_line(1015,294,1115,344, fill='black')
                            
                            canvas_page5_Light7.create_text(100,600, text='''
                                                            A convex lens is curved outwards.It is thicker in the 
                                                            centre and narrows down at the edges. It merges the light 
                                                            rays passing through it at a certain point. Therefore,
                                                            it is also called a Converging Lens.
                                                            
                                                            A convex lens can forms real and inverted image. When
                                                            the object is placed very close to the lens, the image 
                                                            formed is virtual, erect and magnified. When used to see
                                                            objects magnified, the convex lens is called a magnifying 
                                                            glass.
                                                            
                                                            A convex lens converges (bends inward) the light generally
                                                            falling on it. Therefore, it is called the converging lens.''', font=('courier',14), fill = 'black')
                            
                            canvas_page5_Light7.create_text(850,560, text='''
                                                            A concave lens is curved inwards. It has wider edges and
                                                            a thinner centre. It reflects back the light that travels
                                                            through it is different directions. Therefore, it is also 
                                                            called a Diverging Lens.
                                                            
                                                            A concave lens always forms erect, virtual and smaller
                                                            image than the object.
                                                            
                                                            A concave lens diverges (bends outward) the light and 
                                                            is called a diverging lens.''', font=('courier',14), fill = 'black')
                        
                            def Back_page5_Light7():
                                phy_page5_Light7.destroy()
                                   
                            Back_page5_Light7=Button(phy_page5_Light7, bg='coral2', text='<--', command=Back_page5_Light7)
                            Back_page5_Light7.pack()
                            Back_page5_Light7.place(relx=.0,rely=.0)
                            
                            def page6_Light7():
                                phy_page6_Light7=Tk()
                                phy_page6_Light7.title('Light')
                                canvas_page6_Light7=Canvas(phy_page6_Light7, width=1500, height=900, bg='white')
                                canvas_page6_Light7.pack(expand=YES,fill=BOTH)
                                canvas_page6_Light7.create_text(750,40,text='Sunlight-White or Coloured?', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                
                                xy = 300,100,1200,840
                                canvas_page6_Light7.create_arc(xy, start=0, extent=180, fill="red")
                                xy = 350,140,1150,800
                                canvas_page6_Light7.create_arc(xy, start=0, extent=180, fill="orange")
                                xy = 400,180,1100,760
                                canvas_page6_Light7.create_arc(xy, start=0, extent=180, fill="yellow")
                                xy = 450,220,1050,720
                                canvas_page6_Light7.create_arc(xy, start=0, extent=180, fill="green2")
                                xy = 500,260,1000,680
                                canvas_page6_Light7.create_arc(xy, start=0, extent=180, fill="dodger blue")
                                xy = 550,300,950,640
                                canvas_page6_Light7.create_arc(xy, start=0, extent=180, fill="blue2")
                                xy = 600,340,900,600
                                canvas_page6_Light7.create_arc(xy, start=0, extent=180, fill="violet red")
                                xy = 650,380,850,560
                                canvas_page6_Light7.create_arc(xy, start=0, extent=180, fill="white", outline='white')
                                
                                canvas_page6_Light7.create_arc(650,380,850,560, style=ARC, start=0, extent=180, outline='black')
                                canvas_page6_Light7.create_text(750,520,text='Rainbow', font=('Yu Gothic UI Semibold',20), fill = 'black')
                                
                                canvas_page6_Light7.create_text(450,650,text='''
                                                                •A rainbow is a natural phenomenon in which the light rays of the sun are reflected and refracted by
                                                                the water droplets present in the atmosphere.
                                                                
                                                                •The white light of the sun contains seven coloured lights in it that separate out due to refraction 
                                                                 (called a Spectrum of Lights). This spectrum of white light can be seen in the following:
                                                                    o	Rainbows
                                                                    o	Soap bubbles
                                                                    o	Surface of a CD
                                                                    o	Prisms''', font=('Courier',14), fill = 'black')
                                
                                def Back_page6_Light7():
                                    phy_page6_Light7.destroy()
                                   
                                Back_page6_Light7=Button(phy_page6_Light7, bg='coral2', text='<--', command=Back_page6_Light7)
                                Back_page6_Light7.pack()
                                Back_page6_Light7.place(relx=.0,rely=.0)
                                
                                def page7_Light7():
                                    phy_page7_Light7=Tk()
                                    phy_page7_Light7.title('Light')
                                    canvas_page7_Light7=Canvas(phy_page7_Light7, width=1500, height=900, bg='white')
                                    canvas_page7_Light7.pack(expand=YES,fill=BOTH)
                                    
                                    canvas_page7_Light7.create_polygon(750,150,950,550,550,550, fill='lightblue1')
                                    canvas_page7_Light7.create_polygon(605,440,810,260,1100,300,1100,320,825,280, fill='red')
                                    canvas_page7_Light7.create_polygon(605,440,825,280,1100,320,1100,340,830,300, fill='orange')
                                    canvas_page7_Light7.create_polygon(605,440,830,300,1100,340,1100,360,835,320, fill='yellow')
                                    canvas_page7_Light7.create_polygon(605,440,835,320,1100,360,1100,380,840,340, fill='green')
                                    canvas_page7_Light7.create_polygon(605,440,840,340,1100,380,1100,400,845,360, fill='dodger blue')
                                    canvas_page7_Light7.create_polygon(605,440,845,360,1100,400,1100,420,850,380, fill='blue2')
                                    canvas_page7_Light7.create_polygon(605,440,850,380,1100,420,1100,440,860,400, fill='violet red')
                                    
                                    canvas_page7_Light7.create_line(605,440,400,600)
                                    canvas_page7_Light7.create_text(420,500, text='White light', font=('courier',14))
                                    
                                    canvas_page7_Light7.create_text(750,620, text='Spectrum of White Light through a Prism', font=('courier',14))

                                    def Back_page7_Light7():
                                        phy_page7_Light7.destroy()
                                   
                                    Back_page7_Light7=Button(phy_page7_Light7, bg='coral2', text='<--', command=Back_page7_Light7)
                                    Back_page7_Light7.pack()
                                    Back_page7_Light7.place(relx=.0,rely=.0)
                                    
                                    def page8_Light7():
                                        phy_page8_Light7=Tk()
                                        phy_page8_Light7.title('Light')
                                        canvas_page8_Light7=Canvas(phy_page8_Light7, width=1500, height=900, bg='white')
                                        canvas_page8_Light7.pack(expand=YES,fill=BOTH)
                                        
                                        canvas_page8_Light7.create_text(700,80, text='Newton\'s disk',font=('Yu Gothic UI Semibold',22))
                                        xy=300,200,500,300
                                        colour=['Violet red','blue2','dodger blue','green2','yellow','orange','red']
                                        for i in range(7):
                                            canvas_page8_Light7.create_arc(xy, start=i*(360/7), extent=360/7, fill=colour[i])
                                       
                                        canvas_page8_Light7.create_rectangle(395,300,405,500, fill='black')
                                        canvas_page8_Light7.create_oval(900,200,1100,300, fill='seashell')
                                        canvas_page8_Light7.create_rectangle(995,300,1005,500, fill='black')
                                        canvas_page8_Light7.create_arc(1000,248,1004,252, style=ARC, start=0, extent=359)
                                        
                                        canvas_page8_Light7.create_arc(950,220,1050,280, style=ARC, start=230, extent=80)
                                        canvas_page8_Light7.create_line(1015,264,1033,273)
                                        canvas_page8_Light7.create_line(1027,288,1033,273)
                                        
                                        canvas_page8_Light7.create_text(750,560, text='(a) A disc with seven colours \t\t\t\t (b) It appears white on rotating',font=('courier',14))
                                        canvas_page8_Light7.create_text(350,700, text='''
                                                                        •The Newton’s disc can be obtained by dividing a disk into 7 partitions and painting
                                                                         each of them with the seven colours of the rainbow.
                                                                        •When the disc is rotated at a fast pace in daylight all the colours tend to mix 
                                                                         together and the disc appears whitish in colour.''',font=('courier',14))

                                        def Back_page8_Light7():
                                            phy_page8_Light7.destroy()
                                   
                                        Back_page8_Light7=Button(phy_page8_Light7, bg='coral2', text='<--', command=Back_page8_Light7)
                                        Back_page8_Light7.pack()
                                        Back_page8_Light7.place(relx=.0,rely=.0)
                                        
                                        def Back_to_class7_Light():
                                            phy_Light7.destroy()
                                            phy_page2_Light7.destroy()
                                            phy_page3_Light7.destroy()
                                            phy_page4_Light7.destroy()
                                            phy_page5_Light7.destroy()
                                            phy_page6_Light7.destroy()
                                            phy_page7_Light7.destroy()
                                            phy_page8_Light7.destroy()
                                            
                                        Back_to_class7_Light=Button(phy_page8_Light7,bg='coral2', text='Class 7',font=('Castellar',18), command=Back_to_class7_Light)
                                        Back_to_class7_Light.pack()
                                        Back_to_class7_Light.place(relx=.87,rely=.85)
                                    
                                    page8_Light7=Button(phy_page7_Light7, bg='coral2', text='-->', command=page8_Light7)
                                    page8_Light7.pack()
                                    page8_Light7.place(relx=.98,rely=.0)
                                
                                page7_Light7=Button(phy_page6_Light7, bg='coral2', text='-->', command=page7_Light7)
                                page7_Light7.pack()
                                page7_Light7.place(relx=.98,rely=.0)
                            
                            page6_Light7=Button(phy_page5_Light7, bg='coral2', text='-->', command=page6_Light7)
                            page6_Light7.pack()
                            page6_Light7.place(relx=.98,rely=.0)
                        
                        page5_Light7=Button(phy_page4_Light7, bg='coral2', text='-->', command=page5_Light7)
                        page5_Light7.pack()
                        page5_Light7.place(relx=.98,rely=.0)
                
                    page4_Light7=Button(phy_page3_Light7, bg='coral2', text='-->', command=page4_Light7)
                    page4_Light7.pack()
                    page4_Light7.place(relx=.98,rely=.0)
                    
                page3_Light7=Button(phy_page2_Light7, bg='coral2', text='-->', command=page3_Light7)
                page3_Light7.pack()
                page3_Light7.place(relx=.98,rely=.0)
                
            page2_Light7=Button(phy_Light7, bg='coral2', text='-->', command=page2_Light7)
            page2_Light7.pack()
            page2_Light7.place(relx=.98,rely=.0)
            
        def Electric_current_and_its_effects():
            global phy_Electric
            phy_Electric=Toplevel()
            phy_Electric.title('Electric current and its effects')
            canvas_Electric=Canvas(phy_Electric, width=1500, height=900, bg='white')
            canvas_Electric.pack(expand=YES,fill=BOTH)
            
            canvas_Electric.create_text(750,70,text='ELECTRIC CURRENT AND ITS EFFECTS', font=('Times New Roman',27), fill = 'black')
            canvas_Electric.create_text(450,240,text='''
                                        •  An electronic component can be an element of an electric circuit that helps in its functioning.
                                        
                                        •  The electric circuit allows electricity to flow through it and is used to provide electricity 
                                           for various purposes such as running electric motors, providing electricity to a bulb or a fan,
                                           generating heat.
                                        
                                        •  A battery is defined as a combination of two or more cells. In a battery, the negative terminal 
                                           of one cell is connected to the positive terminal of the next cell and so on. .
                                        
                                        •  Batteries are used in several devices such as toys, remote control, torches and transistors.''', font=('courier',16), fill = 'black')
            
            canvas_Electric.create_text(700,680,text='Batteries', font=('courier',12), fill = 'black')
            
            global batteries
            batteries = tkinter.PhotoImage(file="batteries.png")
            button = Button(phy_Electric, image = batteries,width=686,height=206,font=("Courier",20,"bold"),bg='#94ffe2') 
            button.configure(image = batteries)
            button.place(relx = 0.5, rely = 0.65, anchor = CENTER)
            
            def Back_Electric():
                phy_Electric.destroy()
            
            Back_Electric=Button(phy_Electric, bg='coral2', text='<--', command=Back_Electric)
            Back_Electric.pack()
            Back_Electric.place(relx=.0,rely=.0)
            
            def ecaie_page2():
                phy_ecaie_page2=Tk()
                phy_ecaie_page2.title('Electric Current and its Effects')
                canvas_ecaie_page2=Canvas(phy_ecaie_page2, width=1500, height=900, bg='white')
                canvas_ecaie_page2.pack(expand=YES, fill=BOTH)
                canvas_ecaie_page2.create_text(700,100,text='Symbols of Electric Components',font=('Yu Gothic UI Semibold',22),fill='black')
                
                def wire():
                    phy_wire=Tk()
                    phy_wire.title('Electric Current and its Effects')
                    canvas_wire=Canvas(phy_wire, width=600, height=500, bg='white')
                    canvas_wire.pack(expand=YES, fill=BOTH)
                    canvas_wire.create_rectangle(200,250,350,252, fill='black')
                    
                def Electric_Cell():
                    phy_cell=Tk()
                    phy_cell.title('Electric Current and its Effects')
                    canvas_cell=Canvas(phy_cell, width=600, height=500, bg='white')
                    canvas_cell.pack(expand=YES, fill=BOTH)

                    canvas_cell.create_rectangle(200,250,280,252, fill='black')
                    canvas_cell.create_rectangle(280,170,282,330, fill='black')
                    
                    canvas_cell.create_rectangle(300,220,310,280, fill='black')
                    canvas_cell.create_rectangle(310,250,390,252, fill='black')
    
                def switch_off():
                    phy_switch_off=Tk()
                    phy_switch_off.title('Electric Current and its Effects')
                    canvas_switch_off=Canvas(phy_switch_off, width=600, height=500, bg='white')
                    canvas_switch_off.pack(expand=YES, fill=BOTH)
                    
                    canvas_switch_off.create_line(200,250,280,250, fill='black')
                    canvas_switch_off.create_oval(277,247,283,253, fill='black')
                    canvas_switch_off.create_line(280,250,330,200, fill='black')
                    canvas_switch_off.create_line(340,250,420,250, fill='black')
                    canvas_switch_off.create_oval(337,247,343,253, fill='black')
                    
                def switch_on():
                    phy_switch_on=Tk()
                    phy_switch_on.title('Electric Current and its Effects')
                    canvas_switch_on=Canvas(phy_switch_on, width=600, height=500, bg='white')
                    canvas_switch_on.pack(expand=YES, fill=BOTH)
                    
                    canvas_switch_on.create_line(200,250,280,250, fill='black')
                    canvas_switch_on.create_oval(277,247,283,253, fill='black')
                    canvas_switch_on.create_line(340,250,420,250, fill='black')
                    canvas_switch_on.create_oval(337,247,343,253, fill='black')
                    canvas_switch_on.create_line(277,247,337,247, fill='black')
                
                def battery():
                    phy_battery=Tk()
                    phy_battery.title('Electric Current and its Effects')
                    canvas_battery=Canvas(phy_battery, width=700, height=500, bg='white')
                    canvas_battery.pack(expand=YES, fill=BOTH)
                    
                    canvas_battery.create_rectangle(200,250,280,252, fill='black')
                    canvas_battery.create_rectangle(280,170,282,330, fill='black')
                    
                    canvas_battery.create_rectangle(300,220,310,280, fill='black')
                    canvas_battery.create_rectangle(310,250,350,252, fill='black')
                    
                    canvas_battery.create_rectangle(350,170,352,330, fill='black')
                    canvas_battery.create_rectangle(370,220,380,280, fill='black')
                    canvas_battery.create_rectangle(380,250,420,252, fill='black')
                    
                    canvas_battery.create_rectangle(420,170,422,330, fill='black')
                    canvas_battery.create_rectangle(440,220,450,280, fill='black')
                    canvas_battery.create_rectangle(450,250,530,252, fill='black')
                    
                Wire=Button(phy_ecaie_page2, height=1, width=20, bg='coral2', text='Connecting Wire',font=('Castellar', 27), command=wire)
                cell=Button(phy_ecaie_page2, height=1, width=15, bg='coral2', text='Electric Cell', font=('Castellar',27), command=Electric_Cell)
                Switch_off=Button(phy_ecaie_page2, height=1, width=20, bg='coral2', text='Switch in Off Position', font=('Castellar', 27), command=switch_off)
                Switch_on=Button(phy_ecaie_page2, height=1, width=20, bg='coral2', text='Switch in On Postition', font=('Castellar', 27),command=switch_on)
                Battery=Button(phy_ecaie_page2, height=1, width=8, bg='coral2', text='Battery', font=('Castellar', 27), command=battery)
                Wire.pack()
                Wire.place(relx=.25, rely=.20)
                cell.pack()
                cell.place(relx=.25,rely=.32)
                Switch_off.pack()
                Switch_off.place(relx=.25, rely=.44)
                Switch_on.pack()
                Switch_on.place(relx=.25, rely=.56)
                Battery.pack()
                Battery.place(relx=.25, rely=.68)
                
                def Back_ecaie_page2():
                    phy_ecaie_page2.destroy()
            
                Back_ecaie_page2=Button(phy_ecaie_page2, bg='coral2', text='<--', command=Back_ecaie_page2)
                Back_ecaie_page2.pack()
                Back_ecaie_page2.place(relx=.0,rely=.0)
                
                def ecaie_page3():
                    phy_ecaie_page3=Tk()
                    phy_ecaie_page3.title('Electric Current and its Effects')
                    canvas_ecaie_page3=Canvas(phy_ecaie_page3, width=1500, height=900, bg='white')
                    canvas_ecaie_page3.pack(expand=YES, fill=BOTH)
                    
                    canvas_ecaie_page3.create_text(750,60,text='Circuit Diagram',font=('Yu Gothic UI Semibold',22),fill='black')
                    canvas_ecaie_page3.create_line(600,280,600,200)
                    canvas_ecaie_page3.create_line(600,200,718,200)
                    canvas_ecaie_page3.create_rectangle(590,280,610,285, fill='black')
                    canvas_ecaie_page3.create_rectangle(580,290,620,292, fill='black')
                    canvas_ecaie_page3.create_line(600,292,600,342)
                    canvas_ecaie_page3.create_line(600,342,750,342)
                    canvas_ecaie_page3.create_oval(750,340,755,345, fill='black')
                    canvas_ecaie_page3.create_oval(775,340,780,345, fill='black')
                    canvas_ecaie_page3.create_line(755,340,775,340)
                    canvas_ecaie_page3.create_line(780,342,850,342)
                    canvas_ecaie_page3.create_line(850,342,850,200)
                    canvas_ecaie_page3.create_line(850,200,760,200)
                    canvas_ecaie_page3.create_arc(736,150,773,202, style=ARC, start=290, extent=285)
                    canvas_ecaie_page3.create_arc(706,150,743,202, style=ARC, start=325, extent=282)
                    canvas_ecaie_page3.create_oval(690,130,790,230)
                    
                    canvas_ecaie_page3.create_line(660,168,680,174)
                    canvas_ecaie_page3.create_line(670,138,690,147)
                    canvas_ecaie_page3.create_line(693,112,712,127)
                    canvas_ecaie_page3.create_line(740,98,740,119)
                    canvas_ecaie_page3.create_line(789,112,770,127)
                    canvas_ecaie_page3.create_line(810,138,790,147)
                    canvas_ecaie_page3.create_line(817,168,797,174)

                    canvas_ecaie_page3.create_text(500,570,text='''
                                        •  An electric circuit can be drawn on a paper with the help of the symbols that are used for
                                           representing the electronic components. Such a representation of an electric circuit using
                                           its symbols is called an Electric Circuit Diagram.
                                        
                                        •  The electric circuit diagram consists of a key that acts as a switch for the circuit. The 
                                           key can be placed anywhere in the circuit.
                                        
                                        •  Open Circuit - When the key is switched off or opened the circuit is said to be an open circuit
                                           as it is incomplete.
                                        
                                        •  Closed Circuit - When the key is switched on or closed the circuit is said to be a closed
                                           circuit as it is complete.
                                        
                                        •  The electric circuit shown here consists of a bulb. The bulb has a wire present inside it called
                                           the Filament. When the electric current passes through the filament it closed. The filament 
                                           breaks when the bulb gets fused.''', font=('courier',16), fill = 'black')
                    
                    def Back_ecaie_page3():
                        phy_ecaie_page3.destroy()
            
                    Back_ecaie_page3=Button(phy_ecaie_page3, bg='coral2', text='<--', command=Back_ecaie_page3)
                    Back_ecaie_page3.pack()
                    Back_ecaie_page3.place(relx=.0,rely=.0)

                    def ecaie_page4():
                        global phy_ecaie_page4
                        phy_ecaie_page4=Toplevel()
                        phy_ecaie_page4.title('Electric Current and its Effects')
                        canvas_ecaie_page4=Canvas(phy_ecaie_page4, width=1500, height=900, bg='white')
                        canvas_ecaie_page4.pack(expand=YES, fill=BOTH)
                        
                        canvas_ecaie_page4.create_text(700,60,text='Light Bulb',font=('Yu Gothic UI Semibold',22),fill='black')
                        canvas_ecaie_page4.create_text(390,600,text='''
                                                       The bulb glows only when the switch is in the ‘ON’ position and the electric circuit is closed.
                                                       In the bulb there is a coiled wire, called the filament that gets hot when electricity is passed
                                                       through it. This makes the filament glow and as a result, light is produced from the bulb.
                                                       When the filament of a bulb breaks, the circuit of the bulb becomes incomplete. Hence the bulb does 
                                                       not glow as it does not receive any electricity.''',font=('Courier',16),fill='black')
                        
                        canvas_ecaie_page4.create_rectangle(1120,175,1490,215,fill='navajo white')
                        canvas_ecaie_page4.create_rectangle(1120,215,1490,405,fill='antiquewhite1')
                        canvas_ecaie_page4.create_text(1300,200,text='CAUTION',font=('Baskerville Old Face',17),fill='black')
                        canvas_ecaie_page4.create_text(1035,300,text='''
                                                       Never touch a lighted electric
                                                       bulb connected to the mains. It
                                                       may be very hot and your hand 
                                                       may get burnt badly. Do not 
                                                       experiment with the electric 
                                                       supply from the mains or 
                                                       agenerator or an inverter. You
                                                       may get an electric shock, which
                                                       may bedangerous.''',font=('Courier',12),fill='black')
                                                       
                        canvas_ecaie_page4.create_text(740,460,text='A Light bulb', font=('courier',12), fill = 'black')                  
                        global bulb
                        bulb = tkinter.PhotoImage(file="bulb.png")
                        button = Button(phy_ecaie_page4, image = bulb,width=251,height=263,font=("Courier",20,"bold"),bg='#94ffe2') 
                        button.configure(image = bulb)
                        button.place(relx = 0.5, rely = 0.35, anchor = CENTER)
                        
                        canvas_ecaie_page4.create_text(380,460,text='Bulb filament', font=('courier',12), fill = 'black')                  
                        global filament
                        filament = tkinter.PhotoImage(file="filament.png")
                        button = Button(phy_ecaie_page4, image = filament ,width=201,height=265,font=("Courier",20,"bold"),bg='#94ffe2') 
                        button.configure(image = filament)
                        button.place(relx = 0.25, rely = 0.35, anchor = CENTER)

                        def Back_ecaie_page4():
                            phy_ecaie_page4.destroy()
            
                        Back_ecaie_page4=Button(phy_ecaie_page4, bg='coral2', text='<--', command=Back_ecaie_page4)
                        Back_ecaie_page4.pack()
                        Back_ecaie_page4.place(relx=.0,rely=.0)
                        
                        def ecaie_page5():
                            global phy_ecaie_page5
                            phy_ecaie_page5=Toplevel()
                            phy_ecaie_page5.title('Electric Current and its Effects')
                            canvas_ecaie_page5=Canvas(phy_ecaie_page5, width=1500, height=900, bg='white')
                            canvas_ecaie_page5.pack(expand=YES, fill=BOTH)
                            
                            canvas_ecaie_page5.create_text(700,60,text='The Heating Effect of Electric Current',font=('Yu Gothic UI Semibold',22),fill='black')
                            canvas_ecaie_page5.create_text(300,300,text='''
                                                           When an electric current passes through a wire the wire gets heated up. This is known as the 
                                                           heating effect of electric current.
                                                           
                                                           The heat that is produced in the wire depends upon the following factors:
                                                               •   the material of the wire
                                                               •   the length of the wire
                                                               •   the thickness of the wire
                                                               
                                                           Many appliances work on the heating effect of electric current such as:
                                                               •   electric heater
                                                               •   electric iron
                                                               •   electric stove
                                                               •   geysers
                                                               •   electric coffee maker
                                                               •   toaster
                                                               •   hair dryer''',font=('courier',14),fill='black')
                                                               
                            canvas_ecaie_page5.create_text(740,710,text='Appliances that work on the heating effect of electric current', font=('courier',12), fill = 'black')
                            global appliances
                            appliances = tkinter.PhotoImage(file="appliances.png")
                            button = Button(phy_ecaie_page5, image = appliances,width=733,height=206,font=("Courier",20,"bold"),bg='#94ffe2') 
                            button.configure(image = appliances)
                            button.place(relx = 0.5, rely = 0.7, anchor = CENTER)
                        
                            def Back_ecaie_page5():
                                phy_ecaie_page5.destroy()
            
                            Back_ecaie_page5=Button(phy_ecaie_page5, bg='coral2', text='<--', command=Back_ecaie_page5)
                            Back_ecaie_page5.pack()
                            Back_ecaie_page5.place(relx=.0,rely=.0)
                            
                            def ecaie_page6():
                                global phy_ecaie_page6
                                phy_ecaie_page6=Toplevel()
                                phy_ecaie_page6.title('Electric Current and its Effects')
                                canvas_ecaie_page6=Canvas(phy_ecaie_page6, width=1500, height=900, bg='white')
                                canvas_ecaie_page6.pack(expand=YES, fill=BOTH)                           
                                
                                canvas_ecaie_page6.create_text(700,60,text='Electric Fuse',font=('Yu Gothic UI Semibold',22),fill='black')
                                
                                canvas_ecaie_page6.create_text(380,570,text='''
                                                               •  An electric fuse is a device that is used to prevent the damage that can be caused by an excess of electric current. 
                                                                  According to the heating effect of the electric current, a wire becomes hot as current is passed through it. 
                                                                  However, if an excess of current is passed through a wire it can melt or break.
                                                               
                                                               •  The electric fuse consists of a wire which is made up of a metal or an alloy which has a low melting point. As a 
                                                                  result, the wire breaks down easily as high current passes through it. As the wire breaks the circuit of the fuse 
                                                                  opens and hence no for the current passes through it.
                                                               
                                                               •  This can prevent a short circuit for fire due to high electric current.
                                                               
                                                               •  Different types of fuses are used for different devices and some are also available for houses as well.''',font=('courier',14),fill='black')
                                
                                canvas_ecaie_page6.create_text(740,420,text='Different types of Fuses', font=('courier',12), fill = 'black')
                                global fuse
                                fuse = tkinter.PhotoImage(file="fuse.png")
                                button = Button(phy_ecaie_page6, image = fuse ,width=555,height=291,font=("Courier",20,"bold"),bg='#94ffe2') 
                                button.configure(image = fuse)
                                button.place(relx = 0.5, rely = 0.3, anchor = CENTER)
                            
                                def Back_ecaie_page6():
                                    phy_ecaie_page6.destroy()
                                    
                                Back_ecaie_page6=Button(phy_ecaie_page6, bg='coral2', text='<--', command=Back_ecaie_page6)
                                Back_ecaie_page6.pack()
                                Back_ecaie_page6.place(relx=.0,rely=.0)
                                
                                def ecaie_page7():
                                    phy_ecaie_page7=Tk()
                                    phy_ecaie_page7.title('Electric Current and its Effects')
                                    canvas_ecaie_page7=Canvas(phy_ecaie_page7, width=1500, height=900, bg='white')
                                    canvas_ecaie_page7.pack(expand=YES, fill=BOTH)
                                    
                                    canvas_ecaie_page7.create_text(410,100,text='How can excessive current pass through a circuit?',font=('Yu Gothic UI Semibold',22),fill='black')

                                    canvas_ecaie_page7.create_text(350,200,text='''
                                                                   •  Sometimes we connect different devices to the same socket which results in drawing of more current from that socket.
                                                                      As a result, the load on the circuit increases and it can lead to a short circuit or fire.
                                                                   
                                                                   •  When the insulation of wires gets torn away, the wires can come in contact with
                                                                      each other which cause a spark or may lead to a fire (short circuit). This is why
                                                                      fuses are used to prevent any kind of short circuit and overloading''',font=('courier',14),fill='black')
                                                                       
                                    canvas_ecaie_page7.create_text(290,390,text='CFL (Compact Fluorescent Lamp)',font=('Yu Gothic UI Semibold',22),fill='black')
                                    canvas_ecaie_page7.create_text(180,520,text='''
                                                                   •  CFLs do not work on the heating effect of electric current.
                                                                     
                                                                   •  They do not have a filament inside them instead they contain two electrodes that 
                                                                      produce light.
                                                                    
                                                                   •  These bulbs have a fluorescent coating inside them which makes the light brighter.
                                                                       
                                                                   •  CFLs thus save energy as they do not produce heat along with the light.
                                                                       
                                                                   •   Ordinary bulbs on the other hand waste energy as they get heated while lighting up.''',font=('Courier',14),fill='black')
                                        
                                    
                                    canvas_ecaie_page7.create_rectangle(1080,215,1460,255,fill='navajo white')
                                    canvas_ecaie_page7.create_rectangle(1080,255,1460,385,fill='antiquewhite1')
                                    canvas_ecaie_page7.create_text(1260,240,text='CAUTION',font=('Baskerville Old Face',17),fill='black')
                                    canvas_ecaie_page7.create_text(1000,310,text='''
                                                       Never try to investigate an 
                                                       electric fuse connected to mains
                                                       circuit on your own. You may, 
                                                       however, visit an electric repair
                                                       shop and compare the burnt out 
                                                       fuses with the new ones''',font=('Courier',12),fill='black')
                                    
                                    canvas_ecaie_page7.create_rectangle(1080,410,1460,640,fill='lightcyan2')
                                    canvas_ecaie_page7.create_text(1000,510,text='''
                                                       One reason for excessive currents
                                                       in electrical circuits is the 
                                                       direct touching of wires. This 
                                                       may happen if the insulation on 
                                                       the wires has come off due to wear
                                                       and tear. This may cause a short 
                                                       circuit. Another reason for 
                                                       excessive current can be the
                                                       connection of many devices to a
                                                       single socket. This may cause 
                                                       overload in the circuit.''',font=('Courier',12),fill='black')

                                    def Back_ecaie_page7():
                                        phy_ecaie_page7.destroy()
                                    
                                    Back_ecaie_page7=Button(phy_ecaie_page7, bg='coral2', text='<--', command=Back_ecaie_page7)
                                    Back_ecaie_page7.pack()
                                    Back_ecaie_page7.place(relx=.0,rely=.0)
                                    
                                    def ecaie_page8():
                                        global phy_ecaie_page8
                                        phy_ecaie_page8=Toplevel()
                                        phy_ecaie_page8.title('Electric Current and its Effects')
                                        canvas_ecaie_page8=Canvas(phy_ecaie_page8, width=1500, height=900, bg='white')
                                        canvas_ecaie_page8.pack(expand=YES, fill=BOTH)
                                
                                        canvas_ecaie_page8.create_text(220,110,text='What is an ISI mark?',font=('Yu Gothic UI Semibold',22),fill='black')
                                        canvas_ecaie_page8.create_text(140,250,text='''
                                                                       •   ISI stands for Indian Standards Institute which standardizes all electrical 
                                                                           appliances.
                                                                       
                                                                       •   Hence if any appliance does not have an ISI mark over it, it means that this 
                                                                           appliance does not conform to the standard guidelines of ISI and hence it is
                                                                           not safe to use.
                                                                       
                                                                       •   On the other hand, if any appliance holds such a mark, it means that it is 
                                                                           safe to use, it is a quality product and it will not lead to wastage of 
                                                                           electricity.''',font=('Courier',14),fill='black')
                                        
                                        canvas_ecaie_page8.create_text(370,470,text='What are miniature circuit breakers (MCB)?',font=('Yu Gothic UI Semibold',22),fill='black')
                                        canvas_ecaie_page8.create_text(140,600,text='''
                                                                       •   A miniature circuit breaker or MCB is generally used instead of fuses.
                                                                       
                                                                       •   A fuse breaks due to excessive current so that the circuit opens up and the 
                                                                           damage can be prevented. However, once a fuse breaks down it cannot be used 
                                                                           again.
                                                                       
                                                                       •   MCB, on the other hand, is a switch which turns OFF on its own when a circuit
                                                                           overloads. Once the problem the circuit is rectified we can switch ON the MCB 
                                                                           once again.''',font=('Courier',14),fill='black')
                                        
                                        canvas_ecaie_page8.create_text(1210,400,text='ISI Mark on Electric Geyser', font=('courier',12), fill = 'black')
                                        global ISI
                                        ISI = tkinter.PhotoImage(file="ISI.png")
                                        button = Button(phy_ecaie_page8, image = ISI ,width=245,height=343,font=("Courier",20,"bold"),bg='#94ffe2') 
                                        button.configure(image = ISI)
                                        button.place(relx = 0.8, rely = 0.25, anchor = CENTER)
                                        
                                        canvas_ecaie_page8.create_text(1210,770,text='Miniature Circuit Breaker (MCB)', font=('courier',12), fill = 'black')
                                        global MCB
                                        MCB = tkinter.PhotoImage(file="MCB.png")
                                        button = Button(phy_ecaie_page8, image = ISI ,width=232,height=329,font=("Courier",20,"bold"),bg='#94ffe2') 
                                        button.configure(image = MCB)
                                        button.place(relx = 0.8, rely = 0.7, anchor = CENTER)
                                        
                                        def Back_ecaie_page8():
                                            phy_ecaie_page8.destroy()
                                    
                                        Back_ecaie_page8=Button(phy_ecaie_page8, bg='coral2', text='<--', command=Back_ecaie_page8)
                                        Back_ecaie_page8.pack()
                                        Back_ecaie_page8.place(relx=.0,rely=.0)
                                        
                                        def ecaie_page9():
                                            global phy_ecaie_page9
                                            phy_ecaie_page9=Toplevel()
                                            phy_ecaie_page9.title('Electric Current and its Effects')
                                            canvas_ecaie_page9=Canvas(phy_ecaie_page9, width=1500, height=900, bg='white')
                                            canvas_ecaie_page9.pack(expand=YES, fill=BOTH)
                                            canvas_ecaie_page9.create_text(700,60,text='Magnetic Effect of Electric Current',font=('Yu Gothic UI Semibold',22),fill='black')
                                            canvas_ecaie_page9.create_text(350,160,text='''
                                                                       When an electric current is passed through a wire it behaves like a magnet. This is called the magnetic effect of the 
                                                                       electric current which was discovered by a scientist, Hans Christian Oersted.  
                                                                       
                                                                       He discovered that the needle of a compass deflects when an electric current is passed through a wire placed near the 
                                                                       compass. This indicates that a magnetic field is created near the wire that deflects the needle.''',font=('Courier',14),fill='black')
                                            
                                            canvas_ecaie_page9.create_text(650,650,text='Deflection in Compass Needle due to Electric Current', font=('courier',12), fill = 'black')
                                            global deflection
                                            deflection = tkinter.PhotoImage(file="deflection.png")
                                            button = Button(phy_ecaie_page9, image = deflection ,width=612,height=324,font=("Courier",20,"bold"),bg='#94ffe2') 
                                            button.configure(image = deflection)
                                            button.place(relx = 0.45, rely = 0.53, anchor = CENTER)
                                        
                                            def Back_ecaie_page9():
                                                phy_ecaie_page9.destroy()
                                    
                                            Back_ecaie_page9=Button(phy_ecaie_page9, bg='coral2', text='<--', command=Back_ecaie_page9)
                                            Back_ecaie_page9.pack()
                                            Back_ecaie_page9.place(relx=.0,rely=.0)
                                            
                                            def ecaie_page10():
                                                global phy_ecaie_page10
                                                phy_ecaie_page10=Toplevel()
                                                phy_ecaie_page10.title('Electric Current and its Effects')
                                                canvas_ecaie_page10=Canvas(phy_ecaie_page10, width=1500, height=900, bg='white')
                                                canvas_ecaie_page10.pack(expand=YES, fill=BOTH)
                                                canvas_ecaie_page10.create_text(700,60,text='Electromagnet',font=('Yu Gothic UI Semibold',22),fill='black')
                                                canvas_ecaie_page10.create_text(280,160,text='''
                                                                               •   Every magnetic material has a magnetic field up to which the influence of its magnetism can be experienced.
                                                                               
                                                                               •   A magnet whose magnetic field is generated with the help of electric current is called an Electromagnet.
                                                                               
                                                                               •   The Electromagnet is formed because of the magnetic effect of the electric current.''',font=('Courier',14),fill='black')
                                                
                                                canvas_ecaie_page10.create_text(740,720,text='Electromagnet', font=('courier',12), fill = 'black')
                                                global Electromagnet
                                                Electromagnet = tkinter.PhotoImage(file="electromagnet.png")
                                                button = Button(phy_ecaie_page10, image = Electromagnet ,width=607,height=393,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                button.configure(image = Electromagnet)
                                                button.place(relx = 0.5, rely = 0.6, anchor = CENTER)
                                                
                                                def Back_ecaie_page10():
                                                    phy_ecaie_page10.destroy()
                                    
                                                Back_ecaie_page10=Button(phy_ecaie_page10, bg='coral2', text='<--', command=Back_ecaie_page10)
                                                Back_ecaie_page10.pack()
                                                Back_ecaie_page10.place(relx=.0,rely=.0)
                                                
                                                def ecaie_page11():
                                                    phy_ecaie_page11=Tk()
                                                    phy_ecaie_page11.title('Electric Current and its Effects')
                                                    canvas_ecaie_page11=Canvas(phy_ecaie_page11, width=1500, height=900, bg='white')
                                                    canvas_ecaie_page11.pack(expand=YES, fill=BOTH)
                                                    
                                                    canvas_ecaie_page11.create_text(350,120,text='Applications of Electromagnets',font=('Yu Gothic UI Semibold',22),fill='black')
                                                    canvas_ecaie_page11.create_text(200,420,text='''
                                                                                    •   Electromagnets are used in domestic appliances such as electric bells.
                                                                                    
                                                                                    •   They are used in toys.
                                                                                    
                                                                                    •   They are used in all kinds of telecommunication equipment.
                                                                                    
                                                                                    •   They are used in cranes to separate magnetic materials from junk and to lift heavy objects.
                                                                                    
                                                                                    •   They are used by doctors to remove any magnetic materials that we have fallen in the eye.
                                                                                    
                                                                                    •	Motors and generators.
                                                                                    
                                                                                    •	Transformers.
                                                                                    
                                                                                    •	Pickups.
                                                                                    
                                                                                    •	Relays.
                                                                                    
                                                                                    •	Loudspeakers and headphones.
                                                                                    
                                                                                    •	Actuators such as valves.
                                                                                    
                                                                                    •	Magnetic recording and data storage equipment: tape recorders, VCRs, hard disks.''',font=('Courier',16),fill='black')
                                        
                                                    
                                                    def Back_ecaie_page11():
                                                        phy_ecaie_page11.destroy()
                                    
                                                    Back_ecaie_page11=Button(phy_ecaie_page11, bg='coral2', text='<--', command=Back_ecaie_page11)
                                                    Back_ecaie_page11.pack()
                                                    Back_ecaie_page11.place(relx=.0,rely=.0)
                                                    
                                                    def ecaie_page12():
                                                        global phy_ecaie_page12
                                                        phy_ecaie_page12=Toplevel()
                                                        phy_ecaie_page12.title('Electric Current and its Effects')
                                                        canvas_ecaie_page12=Canvas(phy_ecaie_page12, width=1500, height=900, bg='white')
                                                        canvas_ecaie_page12.pack(expand=YES, fill=BOTH)
                                                        
                                                        canvas_ecaie_page12.create_text(700,40,text='Electric Bell',font=('Yu Gothic UI Semibold',22),fill='black')
                                                        canvas_ecaie_page12.create_text(350,510,text='Components of an Electric Bell',font=('Yu Gothic UI Semibold',22),fill='black')
                                                        canvas_ecaie_page12.create_text(280,650,text='''
                                                                                        •   A coil of wire wound over an iron piece that forms the Electromagnet.
                                                                                        
                                                                                        •   An iron strip (soft iron armature) which has a hammer attached to it which is joined to the wire coil.
                                                                                        
                                                                                        •   A contact screw through which is attached to the iron strip.
                                                                                        
                                                                                        •   A battery which connects the wire coil and the contact screw.
                                                                                        
                                                                                        •   A switch in the middle of the circuit.''',font=('Courier',14),fill='black')
                                                        
                                                        canvas_ecaie_page12.create_text(700,460,text='Electric bell', font=('courier',12), fill = 'black')
                                                        global Electricbell
                                                        Electricbell = tkinter.PhotoImage(file="electric bell.png")
                                                        button = Button(phy_ecaie_page12, image = Electricbell ,width=471,height=380,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                        button.configure(image = Electricbell)
                                                        button.place(relx = 0.43, rely = 0.3, anchor = CENTER)
                                                
                                                        def Back_ecaie_page12():
                                                            phy_ecaie_page12.destroy()
                                    
                                                        Back_ecaie_page12=Button(phy_ecaie_page12, bg='coral2', text='<--', command=Back_ecaie_page12)
                                                        Back_ecaie_page12.pack()
                                                        Back_ecaie_page12.place(relx=.0,rely=.0)
                                                        
                                                        def ecaie_page13():
                                                            phy_ecaie_page13=Tk()
                                                            phy_ecaie_page13.title('Electric Current and its Effects')
                                                            canvas_ecaie_page13=Canvas(phy_ecaie_page13, width=1500, height=900, bg='white')
                                                            canvas_ecaie_page13.pack(expand=YES, fill=BOTH)
                                                            
                                                            canvas_ecaie_page13.create_text(270,120,text='Working of an Electric Bell',font=('Yu Gothic UI Semibold',22),fill='black')
                                                            canvas_ecaie_page13.create_text(180,380,text='''
                                                                                            •   When the switch of the Bell is ON, an electric current flows through the coil of wire which makes 
                                                                                                the iron piece attached to it act as an Electromagnet.
                                                                                                
                                                                                            •   As a result, the iron piece attracts the hammer towards itself. The hammer thus hits the bell and 
                                                                                                a sound isproduced.
                                                                                                
                                                                                            •   As the hammer move towards the iron piece, it moves away from the contact screw which breaks down 
                                                                                                the circuit.
                                                                                            
                                                                                            •   As the circuit breaks the wire coil stops receiving any current which makes the electromagnet lose 
                                                                                                its magnetic effect.
                                                                                                
                                                                                            •   As a result, the hammer falls back to its original position.
                                                                                            
                                                                                            •   Then as the hammer falls back the iron strip again comes in contact with the contact screw and the 
                                                                                                circuit gets completed.
                                                                                                
                                                                                            •   This again turns the iron piece into an electromagnet and the whole process continues until the bell 
                                                                                                is switched OFF. This results in the continuous ringing of the bell.''',font=('Courier',16),fill='black')
                                                        
                                                            def Back_ecaie_page13():
                                                                phy_ecaie_page13.destroy()
                                                            
                                                            Back_ecaie_page13=Button(phy_ecaie_page13, bg='coral2', text='<--', command=Back_ecaie_page13)
                                                            Back_ecaie_page13.pack()
                                                            Back_ecaie_page13.place(relx=.0,rely=.0)
                                                                
                                                            def Back_to_class7_ecaie():
                                                                phy_Electric.destroy()
                                                                phy_ecaie_page2.destroy()
                                                                phy_ecaie_page3.destroy()
                                                                phy_ecaie_page4.destroy()
                                                                phy_ecaie_page5.destroy()
                                                                phy_ecaie_page6.destroy()
                                                                phy_ecaie_page7.destroy()
                                                                phy_ecaie_page8.destroy()
                                                                phy_ecaie_page9.destroy()
                                                                phy_ecaie_page10.destroy()
                                                                phy_ecaie_page11.destroy()
                                                                phy_ecaie_page12.destroy()
                                                                phy_ecaie_page13.destroy()
                                                                
                                                            Back_to_class7_ecaie=Button(phy_ecaie_page13,bg='coral2', text='Class 7',font=('Castellar',18), command=Back_to_class7_ecaie)
                                                            Back_to_class7_ecaie.pack()
                                                            Back_to_class7_ecaie.place(relx=.87,rely=.85)
                                                        
                                                        ecaie_page13=Button(phy_ecaie_page12, bg='coral2',text='-->', command=ecaie_page13)
                                                        ecaie_page13.pack()
                                                        ecaie_page13.place(relx=.98, rely=.0)
                                                        
                                                    ecaie_page12=Button(phy_ecaie_page11, bg='coral2',text='-->', command=ecaie_page12)
                                                    ecaie_page12.pack()
                                                    ecaie_page12.place(relx=.98, rely=.0)
                                                
                                                ecaie_page11=Button(phy_ecaie_page10, bg='coral2',text='-->', command=ecaie_page11)
                                                ecaie_page11.pack()
                                                ecaie_page11.place(relx=.98, rely=.0)
                                        
                                            ecaie_page10=Button(phy_ecaie_page9, bg='coral2',text='-->', command=ecaie_page10)
                                            ecaie_page10.pack()
                                            ecaie_page10.place(relx=.98, rely=.0)
                                        
                                        ecaie_page9=Button(phy_ecaie_page8, bg='coral2',text='-->', command=ecaie_page9)
                                        ecaie_page9.pack()
                                        ecaie_page9.place(relx=.98, rely=.0)
                                        
                                    ecaie_page8=Button(phy_ecaie_page7, bg='coral2',text='-->', command=ecaie_page8)
                                    ecaie_page8.pack()
                                    ecaie_page8.place(relx=.98, rely=.0)
                                    
                                ecaie_page7=Button(phy_ecaie_page6, bg='coral2',text='-->', command=ecaie_page7)
                                ecaie_page7.pack()
                                ecaie_page7.place(relx=.98, rely=.0)
                            
                            ecaie_page6=Button(phy_ecaie_page5, bg='coral2',text='-->', command=ecaie_page6)
                            ecaie_page6.pack()
                            ecaie_page6.place(relx=.98, rely=.0)
                        
                        ecaie_page5=Button(phy_ecaie_page4, bg='coral2',text='-->', command=ecaie_page5)
                        ecaie_page5.pack()
                        ecaie_page5.place(relx=.98, rely=.0)
                    
                    ecaie_page4=Button(phy_ecaie_page3, bg='coral2',text='-->', command=ecaie_page4)
                    ecaie_page4.pack()
                    ecaie_page4.place(relx=.98, rely=.0)
                
                ecaie_page3=Button(phy_ecaie_page2, bg='coral2',text='-->', command=ecaie_page3)
                ecaie_page3.pack()
                ecaie_page3.place(relx=.98, rely=.0)
            
            ecaie_page2=Button(phy_Electric, bg='coral2',text='-->',command=ecaie_page2)
            ecaie_page2.pack()
            ecaie_page2.place(relx=.98,rely=.0)

        Light7=Button(phy_class7, height=1, width=8, bg='coral2', text='Light', font=('Castellar',27), command=Light7)
        Electric=Button(phy_class7, height=2, width=20, bg='coral2', text='Electric current and\nit\'s effects', font=('Castellar',27), command=Electric_current_and_its_effects)
        Quiz7=Button(phy_class7, height=1, width=8, bg='coral2', text='Quiz', font=('Castellar',27), command=Quiz7)
        Light7.pack()
        Light7.place(relx=.43,rely=.25)
        Electric.pack()
        Electric.place(relx=.33,rely=.43)
        Quiz7.pack()
        Quiz7.place(relx=.43,rely=.65)
        
        Back_class7=Button(phy_class7, bg='coral2', text='<--', command=Back7 )
        Back_class7.pack()
        Back_class7.place(relx=.0,rely=.0)
                
    def Class8():
        phy_class8=Tk()
        phy_class8.title('Class 8')
        canvas_class8=Canvas(phy_class8, width=1500, height=900, bg='grey12')
        canvas_class8.pack(expand=YES,fill=BOTH)
        
        def Back8():
            phy_class8.destroy()
        
        def Quiz8():
            phy_Quiz8=Tk()
            phy_Quiz8.title('Quiz')
            canvas_Quiz8=Canvas(phy_Quiz8, width=1500, height=900, bg='grey12')
            canvas_Quiz8.pack(expand=YES,fill=BOTH)
            
            def play():
                import PlayQuiz8
                PlayQuiz8.PlayQuiz()
                
            play8=Button(phy_Quiz8, bg='coral2',font=('Castellar',30), text='Play Quiz', command=play)
            play8.pack()
            play8.place(relx=.40,rely=.35)
            
            def add():
                import Quiz8
                
            quiz8=Button(phy_Quiz8, bg='coral2', font=('Castellar',30),text='Add Questions', command=add)
            quiz8.pack()
            quiz8.place(relx=.36,rely=.55)
            
            def Back_Quiz8():
                phy_Quiz8.destroy()
            
            Back_Quiz8=Button(phy_Quiz8, bg='coral2', text='<--', command=Back_Quiz8)
            Back_Quiz8.pack()
            Back_Quiz8.place(relx=.0,rely=.0)
                    
        #chapters of class 8
        def Force_and_Pressure():
            phy_ForcePressure=Tk()
            phy_ForcePressure.title('Force and Pressure')
            canvas_ForcePressure=Canvas(phy_ForcePressure, width=1500, height=900, bg='grey12')
            canvas_ForcePressure.pack(expand=YES,fill=BOTH)
            canvas_ForcePressure.create_text(700,50,text='What is Force', font=('Times New Roman',17), fill='white')
            canvas_ForcePressure.create_text(700,200, text='''
1)  When a push or pull is applied to an object it is called force.
    
2)  A force can change the state of an object from rest to motion or vice versa.

3)  To let a force come into play, two or more objects must interact with each other.
\n We know that a magnet can attract a piece of iron. Hence, we can say that the magnet pulls the iron piece towards
itself due to its magnetic force. Similarly, when opposite poles of a magnet repel each other we can say that they are
pushing each other away.''', font=('Times New Roman',14), fill='white')
            canvas_ForcePressure.create_text(700,330,text='Characteristics of Forces', font=('Times New Roman',18), fill='white')
            canvas_ForcePressure.create_text(700,500, text='''
-> When two forces act in the same direction, the net resultant force on an object is the sum of these two forces.

-> When two forces act in opposite directions the net resultant force is the difference of these two forces.
        The force has a magnitude which describes its strength.
        
-> The force always has a direction in which it is applied and a measure of its strength or magnitude.

-> The effects of a force may alter when the direction of the magnitude of the force is changed.

->The effect of more than one forces being applied on an object is calculated by evaluating the net force acting on that object.
''', font=('Times New Roman',14), fill='white')

            def Back_ForcePressure():
                phy_ForcePressure.destroy()
            
            Back_ForcePressure=Button(phy_ForcePressure, bg='coral2', text='<--', command=Back_ForcePressure)
            Back_ForcePressure.pack()
            Back_ForcePressure.place(relx=.0,rely=.0)
            
            def fp8_page1():
                phy_FP8_page1=Tk()
                phy_FP8_page1.title('Force and Pressure')                
                canvas_FP8_page1=Canvas(phy_FP8_page1, width=1500,height=900, bg='grey12')
                canvas_FP8_page1.pack(expand=YES,fill=BOTH)

                canvas_FP8_page1.create_text(680,100,text='ACTIVITY',font=('courier',20),fill='white')

                canvas_FP8_page1.create_rectangle(300,300,400,400, fill='orange')
                canvas_FP8_page1.create_polygon(300,300,350,200,400,300, fill='brown')
                canvas_FP8_page1.create_rectangle(250,180,450,450, outline='white')

                canvas_FP8_page1.create_rectangle(900,300,1000,400, fill='orange')
                canvas_FP8_page1.create_polygon(900,300,950,200,1000,300, fill='brown') 
                canvas_FP8_page1.create_rectangle(780,180,1150,420, outline='white')

                canvas_FP8_page1.create_rectangle(800,210,880,215, fill='white')
                canvas_FP8_page1.create_rectangle(800,245,880,250, fill='white')


                canvas_FP8_page1.create_polygon(875,200,895,213,875,225, fill='white')
                canvas_FP8_page1.create_polygon(875,235,895,247,875,260, fill='white')

                canvas_FP8_page1.create_text(865,190,text='high velocity',font=('courier',12), fill = 'white')
                canvas_FP8_page1.create_text(945,345, text='Pressure\n inside\n is high',font=('courier',10), fill = 'white')
                canvas_FP8_page1.create_text(1050,345, text='Pressure\n outside\n is low',font=('courier',10), fill = 'white')

                canvas_FP8_page1.create_rectangle(600,500,700,600, fill='orange')
                canvas_FP8_page1.create_polygon(600,400,650,300,700,400, fill='brown')
                canvas_FP8_page1.create_rectangle(580,280,730,620, outline='white')

                canvas_FP8_page1.create_rectangle(610,410,615,485 , fill='white')
                canvas_FP8_page1.create_polygon(600,415,613,400,626,415,fill='white')

                canvas_FP8_page1.create_rectangle(645,410,650,485, fill='white')
                canvas_FP8_page1.create_rectangle(682,410,687,485, fill='white')

                def fp8_page2():
                    phy_FP8_page2=Tk()
                    phy_FP8_page2.title('Force and Pressure')                
                    canvas_FP8_page2=Canvas(phy_FP8_page2, width=1500,height=900, bg='white')
                    canvas_FP8_page2.pack(expand=YES,fill=BOTH)
                    canvas_FP8_page2.create_text(700, 200, text='''
-> If two forces are acting upon each other having equal magnitudes (strength) and in opposite directions
    then the net force acting on the object will be zero.

-> Force can bring different effects to an object’s position, size and shape.

 F = m * a
  F = Force
  m = Mass
  a = acceleration

-> The SI unit of force is Newton (N).''', font=('Times New Roman',14), fill='black')
                    canvas_FP8_page2.create_text(700,350,text='Force can change the state of motion of an object', font=('Times New Roman',22), fill='black')
                    canvas_FP8_page2.create_text(700,400, text='The motion of an object', font=('Times New Roman',18), fill='black')
                    canvas_FP8_page2.create_text(700,500, text='''
->  An object is said to be in motion if it is moving by a certain speed in a particular direction.

->  If the object is at rest, it means that it is not changing its position with respect to an observing point. Hence it has zero speed.

->  When the object starts moving it means that its position is being changed with respect to an observation point.

->  In order to move an object from one place to another, a force is required to bring that object in motion.''', font=('Times New Roman',14),fill='black')

                    def Back_fp8_page2():
                        phy_FP8_page2.destroy()
            
                    Back_fp8_page2=Button(phy_FP8_page2, bg='coral2', text='<--', command=Back_fp8_page2)
                    Back_fp8_page2.pack()
                    Back_fp8_page2.place(relx=.0,rely=.0)

                    def fp8_page3():
                        phy_FP8_page3=Tk()
                        phy_FP8_page3.title('Force and Pressure')                
                        canvas_FP8_page3=Canvas(phy_FP8_page3, width=1500,height=900, bg='white')
                        canvas_FP8_page3.pack(expand=YES,fill=BOTH)
                        canvas_FP8_page3.create_text(700,200, text='''
->  Not only this, a force applied on to an object can change its speed, bring it to rest or even change the direction of its motion.

->  It may bring a combination of these effects as well such as a change in direction of motion and change in the speed of the motion altogether.

->  Hence we can say that force can change the state of motion of an object.

->  Any object cannot move by itself or change its state of motion on its own without the application of a force.

->  However, it is not a case that this change of state of motion will take place every time with every kind of object.
    For instance, if a person tries to push a very heavy object such as a wall, it would not at all.''', font=('Times New Roman',14), fill='black')
                        canvas_FP8_page3.create_text(700,400, text='Force can change the shape of an object', font=('Times New Roman',18), fill='black')
                        canvas_FP8_page3.create_text(700,450, text='''
The shape of an object can be altered if some force is applied on to it. Depending upon the magnitude of the force that is being
applied and the rigidity of the object, the effect on its shape and size can be observed.''', font=('Times New Roman',14), fill='black')
                        def shape():
                            global phy_shape
                            phy_shape=Toplevel()
                            phy_shape.title('Force and Pressure')                
                            canvas_shape=Canvas(phy_shape, width=1500,height=900, bg='white')
                            canvas_shape.pack(expand=YES, fill=BOTH)
                            canvas_shape.create_text(700,100,text='FORCE CAN CHANGE THE SHAPE OF AN OBJECT', font=('Times New Roman',20),fill='black')
                            
                            global shape
                            shape = tkinter.PhotoImage(file="shape.png")
                            button = Button(canvas_shape,image = shape, width=683,height=445,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                            button.configure(image = shape)
                            button.place(relx=0.50,rely=0.50,anchor = CENTER)


                        def Back_fp8_page3():
                            phy_FP8_page3.destroy()
                            
                        Shape=Button(phy_FP8_page3, bg='cyan4', text='FORCE CAN CHANGE SHAPE OF OBJECT', font=('Times New Roman',20), command=shape)
                        Shape.pack()
                        Shape.place(relx=.30,rely=.70)
            
                        Back_fp8_page3=Button(phy_FP8_page3, bg='coral2', text='<--', command=Back_fp8_page3)
                        Back_fp8_page3.pack()
                        Back_fp8_page3.place(relx=.0,rely=.0)
                        
                        def fp8_page4():
                            phy_FP8_page4=Tk()
                            phy_FP8_page4.title('Force and Pressure')                
                            canvas_FP8_page4=Canvas(phy_FP8_page4, width=1500,height=900, bg='white')
                            canvas_FP8_page4.pack(expand=YES,fill=BOTH)
                            canvas_FP8_page4.create_rectangle(100,130,620,180, fill='orange')
                            canvas_FP8_page4.create_rectangle(630,130,1250,180, fill='orange')
                            canvas_FP8_page4.create_rectangle(100,185,620,350, fill='burlywood1')
                            canvas_FP8_page4.create_rectangle(630,185,1250,350, fill='burlywood1')
                            canvas_FP8_page4.create_text(700, 50, text='''
Types of Forces: On the basis of the nature of the interaction between two or more objects, forces can be classified as:''', font=('Times New Roman',16), fill='black')
                            canvas_FP8_page4.create_text(700,200, text='''
Contact forces               	                                                                    Non-contact forces

These kinds of forces are applied only when two or                    These kinds of forces are applied when the objects do not come in contact
more objects come in contact with each other.                         with each other and yet are exerting a force upon each other.

Example: Muscular Force, Frictional Force                             Example: Magnetic Force, Gravitational Force, Electrostatic Force''', font=('Times New Roman',14), fill='black')
                            canvas_FP8_page4.create_text(700,400, text='Contact Forces', font=('Times New Roman',20), fill='black')
                            canvas_FP8_page4.create_text(700, 430,text='1. Muscular Force', font=('Times New Roman',18), fill='black')
                            canvas_FP8_page4.create_text(700,550, text='''
The force that comes into play because of the action of muscles is called muscular force. For example:
    
->   Human beings use muscular force in order to walk.

->   The expansion and contraction of lungs is because of muscular force	

->   Movement of food along the food pipe	
 	
->   Animals can also exit muscular forces; that's why they can move from one place to another''', font=('Times New Roman',14), fill='black')
                                
                            def Back_fp8_page4():
                                phy_FP8_page4.destroy()
            
                            Back_fp8_page4=Button(phy_FP8_page4, bg='coral2', text='<--', command=Back_fp8_page4)
                            Back_fp8_page4.pack()
                            Back_fp8_page4.place(relx=.0,rely=.0)
                            
                            def fp8_page5():
                                global phy_FP8_page5
                                phy_FP8_page5=Toplevel()
                                phy_FP8_page5.title('Force and Pressure')                
                                canvas_FP8_page5=Canvas(phy_FP8_page5, width=1500,height=900, bg='white')
                                canvas_FP8_page5.pack(expand=YES,fill=BOTH)
                                canvas_FP8_page5.create_text(700,100, text='2. Fricional Force', font=('Times New Roman',18),fill='black')
                                canvas_FP8_page5.create_text(700,300,text='''
It is the force that is exerted by the surface over an object whenever the object moves on the surface. 
Force of friction has the following characteristics:
    
    • The force of friction always acts in the opposite direction of the motion of the object.

    • It leads to generation of heat as two surfaces come in contact with  each other. For example, 
        when we rub our hands together, heat is produced as a result of friction between our hands.
        
    • Frictional force also leads to wear and tear of the surfaces of  objects that come in contact 
        with each other. For example, sole of shoes often gets worn-out due to friction force 
        that acts between them and the ground as we walk.''', font=('Times New Roman',14), fill='black')
                                canvas_FP8_page5.create_text(700,450, text='3. Air Resistance',font=('Times New Roman',18), fill='black')
                                canvas_FP8_page5.create_text(700,480,text='''
Whenever an object moves or flies in the air, it experiences a force called air resistance.''', font=('Times New Roman',14), fill='black')

                                global air
                                air = tkinter.PhotoImage(file="air.png")
                                button = Button(canvas_FP8_page5,image = air, width=413,height=274,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                                button.configure(image = air)
                                button.place(relx=0.50,rely=0.80,anchor = CENTER)

                                def Back_fp8_page5():
                                    phy_FP8_page5.destroy()
            
                                Back_fp8_page5=Button(phy_FP8_page5, bg='coral2', text='<--', command=Back_fp8_page5)
                                Back_fp8_page5.pack()
                                Back_fp8_page5.place(relx=.0,rely=.0)
                                
                                def fp8_page6():
                                    global phy_FP8_page6
                                    phy_FP8_page6=Toplevel()
                                    phy_FP8_page6.title('Force and Pressure')                
                                    canvas_FP8_page6=Canvas(phy_FP8_page6, width=1500,height=900, bg='white')
                                    canvas_FP8_page6.pack(expand=YES,fill=BOTH)
                                    canvas_FP8_page6.create_text(700,50,text='Non Contact Forces', font=('Times New Roman',20), fill='black')
                                    canvas_FP8_page6.create_text(700,130,text='1. Magnetic Force', font=('Times New Roman',18), fill='black')
                                    canvas_FP8_page6.create_text(700,200,text='''
-> The force exerted by any magnetic object is called magnetic force.
 	
-> We know that like magnetic poles always repel each other, that is, they push each other away.
	
-> Also, opposite magnetic poles always attract each other, that is, they pull each other towards themselves.''', font=('Times New Roman',14), fill='black')

                                    def magimg():
                                        global phy_mag
                                        phy_mag=Toplevel()
                                        phy_mag.title('Force and Pressure')                
                                        canvas_mag=Canvas(phy_mag, width=1500,height=900, bg='white')
                                        canvas_mag.pack(expand=YES, fill=BOTH)
                                        canvas_mag.create_text(700,100,text='MAGNETIC FORCE', font=('Times New Roman',20),fill='black')

                                        global mag
                                        mag = tkinter.PhotoImage(file="mag.png")
                                        button = Button(canvas_mag,image = mag, width=400,height=225,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                                        button.configure(image = mag)
                                        button.place(relx=0.50,rely=0.50,anchor = CENTER)

                                    canvas_FP8_page6.create_text(700,350,text='2. Electrostatic Force', font=('Times New Roman',18), fill='black')
                                    canvas_FP8_page6.create_text(700,450,text='''
-> The force exerted by a charged particle is called electrostatic force.
	
-> We know that like charges always repel or push each other away.
 	
-> Similarly, opposite charges always attract or pull each other towards themselves.''', font=('Times New Roman',14), fill='black')

                                    def elimg():
                                        global phy_ele
                                        phy_ele=Toplevel()
                                        phy_ele.title('Force and Pressure')                
                                        canvas_ele=Canvas(phy_ele, width=1500,height=900, bg='white')
                                        canvas_ele.pack(expand=YES, fill=BOTH)
                                        canvas_ele.create_text(700,100,text='ELECTROSTATIC FORCE', font=('Times New Roman',20),fill='black')

                                        global elec
                                        elec = tkinter.PhotoImage(file="elec.png")
                                        button = Button(canvas_ele,image = elec, width=705,height=191,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                                        button.configure(image = elec)
                                        button.place(relx=0.50,rely=0.50,anchor = CENTER)

                                    canvas_FP8_page6.create_text(700,550,text='3. Gravitational Force', font=('Times New Roman',14), fill='black')
                                    canvas_FP8_page6.create_text(700,650, text='''
-> It is an attractive force that is applied by the earth on all the objects.

-> It is also called the force of gravity or gravity that acts upon all the objects 
    that are present on or near the Earth's surface.''', font=('Times New Roman',14), fill='black')
                                    
                                    def Back_fp8_page6():
                                        phy_FP8_page6.destroy()
                                        
                                    Elec=Button(phy_FP8_page6, bg='cyan4', text='ELECTROSTATIC FORCE', font=('Times New Roman',20), command=elimg)
                                    Elec.pack()
                                    Elec.place(relx=.80,rely=.50)
                                        
                                    Mag=Button(phy_FP8_page6, bg='cyan4', text='MAGNETIC FORCE', font=('Times New Roman',20), command=magimg)
                                    Mag.pack()
                                    Mag.place(relx=.80,rely=.20)
                                        
                                    Back_fp8_page6=Button(phy_FP8_page6, bg='coral2', text='<--', command=Back_fp8_page6)
                                    Back_fp8_page6.pack()
                                    Back_fp8_page6.place(relx=.0,rely=.0)
                                    
                                    def fp8_page7():
                                        phy_FP8_page7=Tk()
                                        phy_FP8_page7.title('Force and Pressure')                
                                        canvas_FP8_page7=Canvas(phy_FP8_page7, width=1500,height=900, bg='white')
                                        canvas_FP8_page7.pack(expand=YES,fill=BOTH)
                                        canvas_FP8_page7.create_text(700,100,text='''
    • Gravity is a property exhibited by every object present in the universe and not only the earth. 
        Hence, all the planets, the moons and even the sun have a gravitational force of their own.''', font=('Times New Roman',14), fill='black')
                                        canvas_FP8_page7.create_text(700,200,text='Pressure',font=('Times New Roman',20), fill='black')
                                        canvas_FP8_page7.create_text(700,500, text='''
Not only the magnitude of the force but the area upon which it acts also affects the changes it may bring upon an object.
The force acting upon a unit area is called pressure.
	
Hence, the pressure exerted by an object depends upon its surface area. If the surface is small, the amount of 
pressure applied is large, and vice-versa.

    -> The SI unit of Pressure is Pascal (Pa) or N/m2
    
    1. A needle has a pointed end that has a very small surface area. Hence  when a large force is 
       exerted upon the needle with a hammer the pressure on the needle increases and it easily 
       moves inside the wall. 
	
    2. Shoulder bags always have broad straps rather than thin straps in order to minimize the pressure 
       that would be exerted on the shoulders of the career due to the gravitational force acting upon the bag.
       
    3. Tools that are used for cutting and piercing always have sharp edges because as a person would apply a 
       force on the tool, its sharp edges would exert more pressure due to less surface area and the object wood 
       cut down easily.
       
    4. The two tyres of a tractor are wider because it minimizes the pressure exerted by the tractor on the ground. 
       As a result, it becomes easier to move the tractor on a muddy field.
       
    5. Camel can walk easily over the sand because it has wide feet which allow them to walk on sand easily. 
       Human beings, on the other hand, cannot as walk easily on sand as their feet have less surface area and 
       therefore our feet sink in the sand.''', font=('Times New Roman',14), fill='black')
       
                                        def Back_fp8_page7():
                                            phy_FP8_page7.destroy()
            
                                        Back_fp8_page7=Button(phy_FP8_page7, bg='coral2', text='<--', command=Back_fp8_page7)
                                        Back_fp8_page7.pack()
                                        Back_fp8_page7.place(relx=.0,rely=.0)
       
                                        def fp8_page8():
                                            phy_FP8_page8=Tk()
                                            phy_FP8_page8.title('Force and Pressure')                
                                            canvas_FP8_page8=Canvas(phy_FP8_page8, width=1500,height=900, bg='white')
                                            canvas_FP8_page8.pack(expand=YES,fill=BOTH)
                                            canvas_FP8_page8.create_text(700,100,text='The Pressure Exerted by Liquids and Gases', font=('Times New Roman',18), fill='black')
                                            canvas_FP8_page8.create_text(700,200,text='''
-> Liquids exert a pressure on the walls of the container in which they are put in. The pressure that a liquid 
    exerts on the bottom of the container is dependent upon the height of the liquid in the container.
-> The liquid exerts equal pressure on different points on the walls of the container having the same depth.

->Similarly, gases also exert pressure on the walls of the container.The molecules of a gas of higher 
  kinetic energy collide with walls applying large force, and as a result these molecules apply pressure on 
the walls of the container''', font=('Times New Roman',14), fill='black')
                                            canvas_FP8_page8.create_text(700,300,text='Atmospheric Pressure', font=('Times New Roman',20), fill='black')
                                            canvas_FP8_page8.create_text(700,500,text='''
    -> A layer of gases is present around the earth’s surface. The air present in the atmosphere exerts 
       a pressure on the earth which is called atmospheric pressure.	
    -> The value of atmospheric pressure at the sea level is 101325 Pascal.
    -> The atmospheric pressure keeps on increasing as we move towards the Earth’s surface.
    
    -> The amount of atmospheric pressure upon us is quite large due to the large surface area of the atmosphere 
      around the earth but we do not experience any of its effects.
      
        ◦ This is so because the pressure of the air inside our body is equal to the atmospheric pressure. 
          There are also fluids present in our body that exert a pressure inside our body. Hence, our bodies easily obtain a
          balance with the atmospheric pressure.'
          
    • However sometimes at higher altitudes where the atmospheric pressure is low as compared to that at the Earth’s 
    surface (low altitudes), nose bleeding occurs.
        -> This is so because at that time the blood pressure in our body becomes higher than the atmospheric pressure outside us.''', font=('Times New Roman',14),fill='black')
        
                                            def Back_fp8_page8():
                                                phy_FP8_page8.destroy()
            
                                            Back_fp8_page8=Button(phy_FP8_page8, bg='coral2', text='<--', command=Back_fp8_page8)
                                            Back_fp8_page8.pack()
                                            Back_fp8_page8.place(relx=.0,rely=.0)
                                            
                                            def Back_to_class8_fp():
                                                phy_ForcePressure.destroy()
                                                phy_FP8_page1.destroy()
                                                phy_FP8_page2.destroy()
                                                phy_FP8_page3.destroy()
                                                phy_FP8_page4.destroy()
                                                phy_FP8_page5.destroy()
                                                phy_FP8_page6.destroy()
                                                phy_FP8_page7.destroy()
                                                phy_FP8_page8.destroy()
                                            
                                            Back_to_class8_fp=Button(phy_FP8_page8,bg='coral2', text='Class 8',font=('Castellar',18), command=Back_to_class8_fp)
                                            Back_to_class8_fp.pack()
                                            Back_to_class8_fp.place(relx=.87,rely=.85)
                                            
                                        fppg8=Button(phy_FP8_page7,bg='coral2', text='-->', command=fp8_page8)
                                        fppg8.pack()
                                        fppg8.place(relx=.98, rely=.0)
                                       
                                    fppg7=Button(phy_FP8_page6,bg='coral2', text='-->', command=fp8_page7)
                                    fppg7.pack()
                                    fppg7.place(relx=.98, rely=.0)
                                    
                                fppg6=Button(phy_FP8_page5,bg='coral2', text='-->', command=fp8_page6)
                                fppg6.pack()
                                fppg6.place(relx=.98, rely=.0)
        
                            fppg5=Button(phy_FP8_page4,bg='coral2', text='-->', command=fp8_page5)
                            fppg5.pack()
                            fppg5.place(relx=.98, rely=.0)

                        fppg4=Button(phy_FP8_page3,bg='coral2', text='-->', command=fp8_page4)
                        fppg4.pack()
                        fppg4.place(relx=.98, rely=.0)
	
                    fppg3=Button(phy_FP8_page2,bg='coral2', text='-->', command=fp8_page3)
                    fppg3.pack()
                    fppg3.place(relx=.98, rely=.0)

                def Back_fp8_page1():
                    phy_FP8_page1.destroy()
            
                Back_fp8_page1=Button(phy_FP8_page1, bg='coral2', text='<--', command=Back_fp8_page1)
                Back_fp8_page1.pack()
                Back_fp8_page1.place(relx=.0,rely=.0)
                
                fppg2=Button(phy_FP8_page1,bg='coral2', text='-->', command=fp8_page2)
                fppg2.pack()
                fppg2.place(relx=.98, rely=.0)
            
            fppg1=Button(phy_ForcePressure,bg='coral2', text='-->', command=fp8_page1)
            fppg1.pack()
            fppg1.place(relx=.98, rely=.0)
                        
        def Friction():
            phy_Friction=Tk()
            phy_Friction.title('Friction')
            canvas_Friction=Canvas(phy_Friction, width=1500, height=900, bg='grey12')
            canvas_Friction.pack(expand=YES,fill=BOTH)
            
            canvas_Friction.create_text(650,100 ,text='FRICTION', font=('courier', 30), fill='white')
            
            canvas_Friction.create_text(500,200, text='''Factors that can affect Friction''', font=('courier', 20), fill='white')
            canvas_Friction.create_text(500,300, text='''

    1. The irregularities of a surface: If we move an object\n with has an irregular or rough surface on another surface which is also irregular,\n the force of Friction will be high in this case and the movement of the object would be restricted.

    2. The regularity of a surface or its smoothness: If the surfaces\n of either the objects or are smooth, the force of Friction would be less and\n the object would move easily over the surface. Even smooth surfaces have a certain irregularity.

    3. If two surfaces are pressed hard: the force of Friction increases \nbetween two surfaces if they are pressed hard and hence the movement of the\n object becomes restricted. However, if there is no pressure the object can easily move.
''', font=('courier',12), fill='white')
            
            canvas_Friction.create_text(650,500, text='Types of Friction',font=('courier',20), fill='white')
            canvas_Friction.create_text(650,620, text='''

    1. Static Friction: The Frictional force that comes into play until an object starts moving is called static Friction.\n An object has to overcome the static Friction force in order to start its movement.

    2. Sliding Friction: Sliding Friction comes into play whenever an object moves along the surface of another object. \nSuch a movement is called ‘slide’. Hence, sliding Friction is the force that opposes the movement or slide of an object. 

    3. Rolling Friction: When an object is rolling on a surface the force of Friction which acts upon\n it is called rolling Friction.

    4. Fluid Friction: When an object moves in a fluid, the fluid exerts a fluid Friction upon the object.\n It is also called air Friction (when the medium of travel is air) and viscous Friction (when the medium of travel is water).
''', font=('courier', 12), fill='white')
            canvas_Friction.create_rectangle(1050,200,1250,230, outline='black', fill='brown')
            canvas_Friction.create_rectangle(1080,200,1220,100, outline='black', fill='yellow')
            canvas_Friction.create_text(1100,234, text='Smooth Surface', font=('courier',12), fill='white')
            canvas_Friction.create_rectangle(1080,110,1105,120, fill='blue')
            canvas_Friction.create_polygon(1105,105,1110,115,1105,125, fill='blue')
            canvas_Friction.create_text(1140,110, text='Small Push', fill='black')
            canvas_Friction.create_rectangle(1180,203,1155,193, fill='blue')
            canvas_Friction.create_polygon(1155,188,1150,198,1155,208 , fill='blue')
            canvas_Friction.create_text(1130, 210, text='Low Friction',fill= 'white')
            
            canvas_Friction.create_rectangle(1050,350,1250,380, outline='black', fill='brown')
            canvas_Friction.create_rectangle(1080,350,1220,250, outline='black', fill='yellow')
            canvas_Friction.create_text(1100,387, text='Rough Surface', font=('courier',12), fill='white')
            
            canvas_Friction.create_rectangle(1050,260,1105,270, fill='blue')
            canvas_Friction.create_polygon(1105,255,1110,265,1105,275, fill='blue')
            canvas_Friction.create_text(1140,265, text='Big Push', fill='black')
            canvas_Friction.create_rectangle(1200,365,1155,355, fill='blue')
            canvas_Friction.create_polygon(1155,350,1150,360,1155,370 , fill='blue')
            canvas_Friction.create_text(1130, 360, text='High Friction', fill='white')
            
            def Back_Friction():
                    phy_Friction.destroy()
            
            Back_Friction=Button(phy_Friction, bg='coral2', text='<--', command=Back_Friction)
            Back_Friction.pack()
            Back_Friction.place(relx=.0,rely=.0)
        
            def friction_page1():
               phy_friction_page1=Tk()
               phy_friction_page1.title('Friction')
               canvas_friction_page1=Canvas(phy_friction_page1, width=1500, height=900, bg='white')
               canvas_friction_page1.pack(expand=YES, fill=BOTH)
               
               canvas_friction_page1.create_text(350,50,text='Advantages of Frictional Force', font=('courier',20), fill='black')
               canvas_friction_page1.create_text(350,220, text='''                                                                  Frictional force is necessary for various purposes in our daily lives such as:

                                                                   1. It allows us to walk on the earth surface.

                                                                   2. It allows us to write with a pen on a surface or a paper.
                                                                   
                                                                   3. It allows us to fix a nail in the wall.
                                                                   
                                                                   4. A moving object would never be able to come to the state of rest without the Frictional force.
                                                                   
                                                                   5. It would not be possible to drive any automobiles on the road without the Friction force.
                                                                   
                                                                   6. It would not be possible to construct any buildings without the Frictional force.
                                                                   ''', font=('courier', 12), fill='black')
               canvas_friction_page1.create_text(350,400, text='Disadvantages of Frictional Force', font=('courier',20), fill='black')
               canvas_friction_page1.create_text(350,550, text='''

                                                                    1. Frictional force results in wear and tear of objects such as the moving 
                                                                    parts of a machine, the tyres of a vehicle, sole of the shoes etc.
                                                                    
                                                                    2. It also results in the production of heat. In the case of machines,
                                                                    the production of heat leads to wastage of energy.
                                                                    
                                                                    3. The Frictional force also leads to a decrease in
                                                                    the speed of a moving object or some time stops it.
                                                                    
                                                                    4. It can lead to noise pollution in certain cases. For instance, aircrafts
                                                                    produce loud sound due to the resistance of the air.
                                                                    ''', font=('courier', 12), fill='black')
            
               def Back_friction_page1():
                   phy_friction_page1.destroy()
                   
               Back_friction_page1=Button(phy_friction_page1, bg='coral2', text='<--', command=Back_friction_page1)
               Back_friction_page1.pack()
               Back_friction_page1.place(relx=.0,rely=.0)
                    
               def friction_page2():
                   phy_friction_page2=Tk()
                   phy_friction_page2.title('Friction')
                   canvas_friction_page2=Canvas(phy_friction_page2, width=1500, height=900, bg='white')
                   canvas_friction_page2.pack(expand=YES, fill=BOTH)
                   canvas_friction_page2.create_text(700,100, text='How can we reduce or increase Friction?', font=('courier',16), fill='black')    
                   canvas_friction_page2.create_text(700,400,text='''
Increasing Friction: Sometimes we need to increase Friction so as to avoid slipping of objects, for example:
 1)  The sole of the shoes is grooved so that the Friction between our feet and ground increases and we can walk safely
 2)  The tyres are treaded so that they can have a better grip over the ground and allow the smooth movement of the vehicles.
 3)  Brake pads are used in bikes to stop them suddenly from moving by increasing the amount of Friction.
 4)  Kabaddi players rub their hands with soil which helps in increasing the Friction between the hands and allows them to have 
        an easy grip of the opponent.
 5)  Gymnasts also apply a coarse substance so that they can have a better grip due to increased Friction in their hands.
    
    Reducing Friction: Sometimes in order to have a smooth movement of an object we need to reduce Friction. For example,

 ->  The powder is sprinkled over the carrom board to decrease the Friction between the board’s surface and the striker. 
     In this way, the surface of the carrom board becomes smooth.
 ->  Grease is used in bicycles and other motors or different parts of a machine to reduce Friction and increase their efficiency.
 ->  Oil is applied on the hinges of the door so that they can move easily.
 
 Applying substances like oil, grease or powder allows in smooth movement as they block the irregularities of a surface. The 
 substances that can reduce the amount of Friction between different objects are called lubricants. However, we can never reduce 
 Friction to a level of zero. There are always some irregularities present on the surface.''', font=('Times New Roman',14), fill='black')
                    
                   def Back_friction_page2():
                       phy_friction_page2.destroy()
                   
                   Back_friction_page2=Button(phy_friction_page2, bg='coral2', text='<--', command=Back_friction_page2)
                   Back_friction_page2.pack()
                   Back_friction_page2.place(relx=.0,rely=.0)
                   
                   def Back_to_class8_friction():
                       phy_Friction.destroy()
                       phy_friction_page1.destroy()
                       phy_friction_page2.destroy()

                   Back_to_class8_friction=Button(phy_friction_page2,bg='coral2', text='Class 8',font=('Castellar',18), command=Back_to_class8_friction)
                   Back_to_class8_friction.pack()
                   Back_to_class8_friction.place(relx=.87,rely=.85)
                   
               Friction_page2=Button(phy_friction_page1, bg='coral2', text='-->', command=friction_page2)
               Friction_page2.pack()
               Friction_page2.place(relx=.98, rely=.0)
               
            Friction_page1=Button(phy_Friction, bg='coral2', text='-->', command=friction_page1)
            Friction_page1.pack()
            Friction_page1.place(relx=.98, rely=.0)
                
        ForcePressure=Button(phy_class8, height=1, width=18, bg='coral2', text='Force and Pressure', font=('Castellar',27), command=Force_and_Pressure)
        Friction=Button(phy_class8, height=1, width=8, bg='coral2', text='Friction', font=('Castellar',27), command=Friction)
        Quiz8=Button(phy_class8, height=1, width=8, bg='coral2', text='Quiz', font=('Castellar',27), command=Quiz8)        
        ForcePressure.pack()
        ForcePressure.place(relx=.33,rely=.33)
        Friction.pack()
        Friction.place(relx=.41,rely=.50)
        Quiz8.pack()
        Quiz8.place(relx=.41,rely=.65)
        
        Back_class8=Button(phy_class8, bg='coral2', text='<--', command=Back8 )
        Back_class8.pack()
        Back_class8.place(relx=.0,rely=.0)
                
    def Class9():
        phy_class9=Tk()
        phy_class9.title('Class 9')
        canvas_class9=Canvas(phy_class9, width=1500, height=900, bg='grey12')
        canvas_class9.pack(expand=YES,fill=BOTH)
        
        def Back9():
            phy_class9.destroy()        
        
        def Quiz9():
            phy_Quiz9=Tk()
            phy_Quiz9.title('Quiz')
            canvas_Quiz9=Canvas(phy_Quiz9, width=1500, height=900, bg='grey12')
            canvas_Quiz9.pack(expand=YES,fill=BOTH)
            
            def play():
                import PlayQuiz9
                PlayQuiz9.PlayQuiz()
                
            play9=Button(phy_Quiz9, bg='coral2',font=('Castellar',30), text='Play Quiz', command=play)
            play9.pack()
            play9.place(relx=.40,rely=.35)
            
            def add():
                import Quiz9
                
            quiz9=Button(phy_Quiz9, bg='coral2', font=('Castellar',30),text='Add Questions', command=add)
            quiz9.pack()
            quiz9.place(relx=.36,rely=.55)
            
            def Back_Quiz9():
                phy_Quiz9.destroy()
            
            Back_Quiz9=Button(phy_Quiz9, bg='coral2', text='<--', command=Back_Quiz9)
            Back_Quiz9.pack()
            Back_Quiz9.place(relx=.0,rely=.0)
                    
        #chapters of class 9
        def Force_and_Laws_of_motion():
            global phy_ForceLawsofmotion
            phy_ForceLawsofmotion=Toplevel()
            phy_ForceLawsofmotion.title('Force and Laws of motion')
            canvas_ForceLawsofmotion=Canvas(phy_ForceLawsofmotion, width=1500, height=900, bg='white')
            canvas_ForceLawsofmotion.pack(expand=YES,fill=BOTH)
            
            canvas_ForceLawsofmotion.create_text(750,70,text='FORCE AND LAWS OF MOTION', font=('Times New Roman',27), fill = 'black')
            canvas_ForceLawsofmotion.create_text(230,460,text='What is a force?', font=('Yu Gothic UI Semibold',22), fill = 'black')
            canvas_ForceLawsofmotion.create_text(360,600,text='''
                                                 Whenever we push or pull an object a force acts upon them and makes them move from one place
                                                 to another. Hence, force can –
                                                 
                                                 •  initiate motion in a motionless object
                                                 
                                                 •  change (increase or decrease) the velocity of the moving object
                                                 
                                                 •  alter the direction of a moving object
                                                 
                                                 •  change the shape and size of an object''', font=('Adobe Fangsong Std R',14), fill = 'black')
            
            global force
            force = tkinter.PhotoImage(file="force.png")
            button = Button(phy_ForceLawsofmotion, image = force ,width=811,height=333,font=("Courier",20,"bold"),bg='#94ffe2') 
            button.configure(image = force)
            button.place(relx = 0.43, rely = 0.3, anchor = CENTER)
            
            def Back_ForceLawsofmotion():
                phy_ForceLawsofmotion.destroy()
            
            Back_ForceLawsofmotion=Button(phy_ForceLawsofmotion, bg='coral2', text='<--', command=Back_ForceLawsofmotion)
            Back_ForceLawsofmotion.pack()
            Back_ForceLawsofmotion.place(relx=.0,rely=.0)
            
            def Forcemotion_page2():
                phy_Forcemotion_page2=Tk()
                phy_Forcemotion_page2.title('Force and Laws of motion')
                canvas_Forcemotion_page2=Canvas(phy_Forcemotion_page2, width=1500, height=900, bg='white')
                canvas_Forcemotion_page2.pack(expand=YES,fill=BOTH)
                
                canvas_Forcemotion_page2.create_text(760,50,text='Effects of Force', font=('Yu Gothic UI Semibold',23), fill = 'black')
                canvas_Forcemotion_page2.create_text(280,120,text='Initiating motion in a motionless body', font=('Adobe Garamond Pro Bold',18), fill = 'black')
                canvas_Forcemotion_page2.create_text(360,160,text='Eg: •  A man uses a force to move a stationary lawnmower', font=('Adobe Fangsong Std R',16), fill = 'black')
                canvas_Forcemotion_page2.create_text(280,290,text='Changing the velocity of a moving body', font=('Adobe Garamond Pro Bold',18), fill = 'black')
                canvas_Forcemotion_page2.create_text(440,330,text='Eg: •  a cyclist uses a bigger force to pedal his bicycle and increase its speed', font=('Adobe Fangsong Std R',16), fill = 'black')
                canvas_Forcemotion_page2.create_text(280,470,text='Altering the direction of a moving body', font=('Adobe Garamond Pro Bold',18), fill = 'black')
                canvas_Forcemotion_page2.create_text(430,510,text='Eg: •  A footballer uses a force to change the diretion of motion of the ball', font=('Adobe Fangsong Std R',16), fill = 'black')
                canvas_Forcemotion_page2.create_text(280,650,text='Changing the shape and size of an object', font=('Adobe Garamond Pro Bold',18), fill = 'black')
                canvas_Forcemotion_page2.create_text(400,690,text='Eg: •  A baker uses a force on his dough to shape it into a curry puff', font=('Adobe Fangsong Std R',16), fill = 'black')

            
                def Back_Forcemotion_page2():
                    phy_Forcemotion_page2.destroy()
            
                Back_Forcemotion_page2=Button(phy_Forcemotion_page2, bg='coral2', text='<--', command=Back_Forcemotion_page2)
                Back_Forcemotion_page2.pack()
                Back_Forcemotion_page2.place(relx=.0,rely=.0)
                
                def Forcemotion_page3():
                    phy_Forcemotion_page3=Tk()
                    phy_Forcemotion_page3.title('Force and Laws of motion')
                    canvas_Forcemotion_page3=Canvas(phy_Forcemotion_page3, width=1500, height=900, bg='white')
                    canvas_Forcemotion_page3.pack(expand=YES,fill=BOTH)
                    
                    canvas_Forcemotion_page3.create_text(200,80,text='Balanced Forces', font=('Yu Gothic UI Semibold',22), fill = 'black')
                    canvas_Forcemotion_page3.create_text(470,170,text='''
                                                         •  When equal amount of forces are applied on an object from different directions such that they cancel out each other
                                                         
                                                         •  They do not change the state of rest or motion of an object
                                                         
                                                         •  They may change the shape and size of an object''', font=('Adobe Fangsong Std R',16), fill = 'black')
                    
                    canvas_Forcemotion_page3.create_rectangle(800,360,785,450, fill='brown', outline='black')
                    canvas_Forcemotion_page3.create_rectangle(600,360,615,450, fill='brown', outline='black')
                    canvas_Forcemotion_page3.create_polygon(600,350,800,350,750,400,550,400, fill='brown', outline='black')
                    canvas_Forcemotion_page3.create_rectangle(550,400,750,410, fill='brown', outline='black')
                    canvas_Forcemotion_page3.create_polygon(750,410,750,400,800,350,800,360, fill='brown', outline='black')
                    canvas_Forcemotion_page3.create_rectangle(550,410,565,500, fill='brown', outline='black')
                    canvas_Forcemotion_page3.create_rectangle(750,410,735,500, fill='brown', outline='black')
                    
                    canvas_Forcemotion_page3.create_rectangle(670,370,700,340, fill='salmon', outline='salmon')
                    canvas_Forcemotion_page3.create_oval(670,375,700,365, fill='salmon', outline='salmon')
                    canvas_Forcemotion_page3.create_oval(670,345,700,335, fill='brown4', outline='salmon')
                    canvas_Forcemotion_page3.create_oval(695,365,715,345, fill='salmon', outline='salmon')
                    canvas_Forcemotion_page3.create_oval(700,360,710,350, fill='brown', outline='salmon')

                    canvas_Forcemotion_page3.create_line(685,290,685,320)
                    canvas_Forcemotion_page3.create_line(685,290,675,300)
                    canvas_Forcemotion_page3.create_line(685,290,695,300)
                    canvas_Forcemotion_page3.create_text(730,270,text='Force exerted by table on the cup', font=('calibri',14), fill = 'black')

                    canvas_Forcemotion_page3.create_line(685,430,685,460)
                    canvas_Forcemotion_page3.create_line(685,460,675,450)
                    canvas_Forcemotion_page3.create_line(685,460,695,450)
                    canvas_Forcemotion_page3.create_text(680,480,text='Weight', font=('calibri',14), fill = 'black')

                    canvas_Forcemotion_page3.create_text(210,550,text='Unbalanced Forces', font=('Yu Gothic UI Semibold',22), fill = 'black')
                    canvas_Forcemotion_page3.create_text(400,670,text='''
                                                         •  When forces applied to an object are of different magnitude (or not in opposite directions so as to cancel)
                                                         
                                                         •  They can alter state of rest or motion of an object
                                                         
                                                         •  They can cause acceleration in an object
                                                         
                                                         •  They can change the shape and size of an object''', font=('Adobe Fangsong Std R',16), fill = 'black')
                    
                    def Back_Forcemotion_page3():
                        phy_Forcemotion_page3.destroy()
            
                    Back_Forcemotion_page3=Button(phy_Forcemotion_page3, bg='coral2', text='<--', command=Back_Forcemotion_page3)
                    Back_Forcemotion_page3.pack()
                    Back_Forcemotion_page3.place(relx=.0,rely=.0)
                    
                    def Forcemotion_page4():
                        phy_Forcemotion_page4=Tk()
                        phy_Forcemotion_page4.title('Force and Laws of motion')
                        canvas_Forcemotion_page4=Canvas(phy_Forcemotion_page4, width=1500, height=900, bg='white')
                        canvas_Forcemotion_page4.pack(expand=YES,fill=BOTH)
                        
                        canvas_Forcemotion_page4.create_text(700,80,text='What is the force of friction?', font=('Yu Gothic UI Semibold',22), fill = 'black')
                        canvas_Forcemotion_page4.create_text(440,170,text='''
                                                             It is a force extended when two surfaces are in contact with each other. It always acts in a direction
                                                             opposite to the direction of motion of the object.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                        
                        canvas_Forcemotion_page4.create_rectangle(500,550,1000,700, fill='Plum3', outline='black')
                        canvas_Forcemotion_page4.create_rectangle(650,550,850,400, fill='Plum1', outline='black')

                        canvas_Forcemotion_page4.create_line(880,400,950,400, fill = 'black')
                        canvas_Forcemotion_page4.create_line(940,390,950,400, fill = 'black')
                        canvas_Forcemotion_page4.create_line(940,410,950,400, fill = 'black')
                        canvas_Forcemotion_page4.create_text(920,420,text='Motion', font=('calibri',14), fill = 'black')

                        canvas_Forcemotion_page4.create_line(720,549,790,549, fill = 'black')
                        canvas_Forcemotion_page4.create_line(720,549,730,539, fill = 'black')
                        canvas_Forcemotion_page4.create_line(720,549,730,559, fill = 'black')
                        canvas_Forcemotion_page4.create_text(760,570,text='Friction', font=('calibri',14), fill = 'black')
                        
                        canvas_Forcemotion_page4.create_line(630,475,560,475, fill = 'black')
                        canvas_Forcemotion_page4.create_line(630,475,620,465, fill = 'black')
                        canvas_Forcemotion_page4.create_line(630,475,620,485, fill = 'black')
                        canvas_Forcemotion_page4.create_text(580,450,text='Pulling force', font=('calibri',14), fill = 'black')
            
                        def Back_Forcemotion_page4():
                            phy_Forcemotion_page4.destroy()
            
                        Back_Forcemotion_page4=Button(phy_Forcemotion_page4, bg='coral2', text='<--', command=Back_Forcemotion_page4)
                        Back_Forcemotion_page4.pack()
                        Back_Forcemotion_page4.place(relx=.0,rely=.0)
                        
                        def Forcemotion_page5():
                            phy_Forcemotion_page5=Tk()
                            phy_Forcemotion_page5.title('Force and Laws of motion')
                            canvas_Forcemotion_page5=Canvas(phy_Forcemotion_page5, width=1500, height=900, bg='white')
                            canvas_Forcemotion_page5.pack(expand=YES,fill=BOTH)
                            
                            canvas_Forcemotion_page5.create_text(180,150,text='Galileo’s Observation:', font=('Yu Gothic UI Semibold',18), fill = 'black')
                            canvas_Forcemotion_page5.create_text(260,190,text='''
                                                                 •  He observed the motion of objects on an inclined plane.
                                                                 •  When a marble is rolled down an inclined plane its velocity increases.''', font=('Adobe Fangsong Std R',15), fill = 'black')

                            canvas_Forcemotion_page5.create_text(170,280,text='Galileo’s Arguments:', font=('Yu Gothic UI Semibold',18), fill = 'black')
                            canvas_Forcemotion_page5.create_text(410,420,text='''
                                                                •   When a marble is rolled down from the left – It will go up on the opposite side up to the same
                                                                       height at which it is dropped down.
                                                                
                                                                •   If the inclination of planes is equal – The marble would travel equal distances while climbing up 
                                                                       as travelled while rolling down. 
                                                                
                                                                •   If we decrease the angle of inclination of the right plane – The marble would travel further until
                                                                       it reaches its original height.
                                                                
                                                                •   If the right side plane is made flat – Marble would travel forever to achieve the same height.''', font=('Adobe Fangsong Std R',16), fill = 'black')
                            
                            canvas_Forcemotion_page5.create_text(160,610,text='Galileo\'s Inference:', font=('Yu Gothic UI Semibold',18), fill = 'black')
                            canvas_Forcemotion_page5.create_text(260,650,text='''
                                                                 •  He observed the motion of objects on an inclined plane.
                                                                 •  When a marble is rolled down an inclined plane its velocity increases.''', font=('Adobe Fangsong Std R',15), fill = 'black')
                            
                            def galileo1_page5():
                                phy_galileo1_page5=Tk()
                                canvas_galileo1_page5=Canvas(phy_galileo1_page5, width=1000, height=500, bg='white')
                                canvas_galileo1_page5.pack(expand=YES,fill=BOTH)
                                   
                            galileo1_page5=Button(phy_Forcemotion_page5, bg='coral2', text='Demo 1', command=galileo1_page5)
                            galileo1_page5.pack()
                            galileo1_page5.place(relx=.8,rely=.35)
                            
                            def galileo2_page5():
                                phy_galileo2_page5=Tk()
                                canvas_galileo2_page5=Canvas(phy_galileo2_page5, width=1000, height=500, bg='white')
                                canvas_galileo2_page5.pack(expand=YES,fill=BOTH)
                                   
                            galileo2_page5=Button(phy_Forcemotion_page5, bg='coral2', text='Demo 2', command=galileo2_page5)
                            galileo2_page5.pack()
                            galileo2_page5.place(relx=.8,rely=.45)
                            
                            def galileo3_page5():
                                phy_galileo3_page5=Tk()
                                canvas_galileo3_page5=Canvas(phy_galileo3_page5, width=1000, height=500, bg='white')
                                canvas_galileo3_page5.pack(expand=YES,fill=BOTH)
                                   
                            galileo3_page5=Button(phy_Forcemotion_page5, bg='coral2', text='Demo 3', command=galileo3_page5)
                            galileo3_page5.pack()
                            galileo3_page5.place(relx=.8,rely=.55)
                            
                            def galileo4_page5():
                                phy_galileo4_page5=Tk()
                                canvas_galileo4_page5=Canvas(phy_galileo4_page5, width=1000, height=500, bg='white')
                                canvas_galileo4_page5.pack(expand=YES,fill=BOTH)
                                   
                            galileo4_page5=Button(phy_Forcemotion_page5, bg='coral2', text='Demo 4', command=galileo4_page5)
                            galileo4_page5.pack()
                            galileo4_page5.place(relx=.8,rely=.65)
                            
                            def Back_Forcemotion_page5():
                                phy_Forcemotion_page5.destroy()
                                
                            Back_Forcemotion_page5=Button(phy_Forcemotion_page5, bg='coral2', text='<--', command=Back_Forcemotion_page5)
                            Back_Forcemotion_page5.pack()
                            Back_Forcemotion_page5.place(relx=.0,rely=.0)
                            
                            def Forcemotion_page6():
                                global phy_Forcemotion_page6
                                phy_Forcemotion_page6=Toplevel()
                                phy_Forcemotion_page6.title('Force and Laws of motion')
                                canvas_Forcemotion_page6=Canvas(phy_Forcemotion_page6, width=1500, height=900, bg='white')
                                canvas_Forcemotion_page6.pack(expand=YES,fill=BOTH)
                                
                                canvas_Forcemotion_page6.create_text(700,60,text='First Law of Motion/The law of Inertia', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                canvas_Forcemotion_page6.create_text(400,150,text='''
                                                                     Whether an object is moving uniformly on a straight path or is at rest, its state would not change until and unless 
                                                                     an external force is applied on to it.''', font=('Adobe Fangsong Std R',16), fill = 'black')
                                canvas_Forcemotion_page6.create_text(400,470,text='''
                                                                     Hence, we can say that objects oppose a change in their state of motion or rest. This tendency of objects to remain 
                                                                     in the state of rest or to keep moving uniformly is called Inertia.''', font=('Adobe Fangsong Std R',16), fill = 'black')
                            
                                canvas_Forcemotion_page6.create_text(170,600,text='Examples of Inertia', font=('Yu Gothic UI Semibold',18), fill = 'black')
                                canvas_Forcemotion_page6.create_text(430,680,text='''
                                                                     •  We fall back when a vehicle starts moving in the forward direction because our body is in the rest state and it 
                                                                          opposes the motion of the vehicle.
                                                                        
                                                                     •  We fall forward when brakes are applied in a car because our body opposite the change of state of motion to rest''', font=('Adobe Fangsong Std R',16), fill = 'black')
                                
                                global firstlaw
                                firstlaw = tkinter.PhotoImage(file="firstlaw.png")
                                button = Button(phy_Forcemotion_page6, image = firstlaw ,width=359,height=265,font=("Courier",20,"bold"),bg='#94ffe2') 
                                button.configure(image = firstlaw)
                                button.place(relx = 0.43, rely = 0.3, anchor = CENTER)
            
                                def Back_Forcemotion_page6():
                                    phy_Forcemotion_page6.destroy()
            
                                Back_Forcemotion_page6=Button(phy_Forcemotion_page6, bg='coral2', text='<--', command=Back_Forcemotion_page6)
                                Back_Forcemotion_page6.pack()
                                Back_Forcemotion_page6.place(relx=.0,rely=.0)
                                
                                def Forcemotion_page7():
                                    phy_Forcemotion_page7=Tk()
                                    phy_Forcemotion_page7.title('Force and Laws of motion')
                                    canvas_Forcemotion_page7=Canvas(phy_Forcemotion_page7, width=1500, height=900, bg='white')
                                    canvas_Forcemotion_page7.pack(expand=YES,fill=BOTH)
                                    
                                    canvas_Forcemotion_page7.create_text(170,70,text='Inertia and Mass', font=('Yu Gothic UI Semibold',18), fill = 'black')
                                    canvas_Forcemotion_page7.create_text(340,200,text='''
                                                                         •  The inertia of an object is dependent upon its mass.
                                                                         
                                                                         •  Lighter objects have less inertia, that is, they can easily change their state of rest or motion.
                                                                         
                                                                         •  Heavier objects have large inertia and therefore they show more resistance.
                                                                         
                                                                         •  Hence ‘Mass’ is called a measure of the inertia of an object.''', font=('Adobe Fangsong Std R',16), fill = 'black')
            
                                    canvas_Forcemotion_page7.create_rectangle(500,400,510,700, outline='black', fill = 'sienna3')
                                    canvas_Forcemotion_page7.create_rectangle(900,400,910,700, outline='black', fill = 'sienna3')
                                    canvas_Forcemotion_page7.create_rectangle(510,420,900,423, outline='black', fill = 'sienna3')
                                    canvas_Forcemotion_page7.create_line(600,420,600,530)
                                    canvas_Forcemotion_page7.create_line(800,420,800,530)
                                    canvas_Forcemotion_page7.create_arc(550,530,650,630, style=ARC, start=0, extent= 180)
                                    canvas_Forcemotion_page7.create_arc(750,530,850,630, style=ARC, start=0, extent= 180)
                                    canvas_Forcemotion_page7.create_polygon(550,580,650,580,620,660,580,660, outline='black', fill = 'grey')
                                    canvas_Forcemotion_page7.create_polygon(750,580,850,580,820,660,780,660, outline='black', fill = 'grey')
                                    canvas_Forcemotion_page7.create_arc(750,560,850,600, start=0, extent= 180, fill='tan1')
                                    canvas_Forcemotion_page7.create_text(600,700, text='Empty bucket', font=('calibri',14), fill='black')
                                    canvas_Forcemotion_page7.create_text(800,700, text='Bucket with sand', font=('calibri',14), fill='black')
                                    canvas_Forcemotion_page7.create_text(1020,500, text='''
                                                                         It is easier for a person to push the bucket 
                                                                         that is empty rather than the one that is 
                                                                         filled with sand. This is because the mass of
                                                                         an empty bucket is less than that of the bucket
                                                                         filled with sand.''', font=('Adobe Fangsong Std R',16), fill='black')
            
                                    def Back_Forcemotion_page7():
                                        phy_Forcemotion_page7.destroy()
            
                                    Back_Forcemotion_page7=Button(phy_Forcemotion_page7, bg='coral2', text='<--', command=Back_Forcemotion_page7)
                                    Back_Forcemotion_page7.pack()
                                    Back_Forcemotion_page7.place(relx=.0,rely=.0)
                                    
                                    def Forcemotion_page8():
                                        phy_Forcemotion_page8=Tk()
                                        phy_Forcemotion_page8.title('Force and Laws of motion')
                                        canvas_Forcemotion_page8=Canvas(phy_Forcemotion_page8, width=1500, height=900, bg='white')
                                        canvas_Forcemotion_page8.pack(expand=YES,fill=BOTH)
                                        canvas_Forcemotion_page8.create_text(700,60,text='Second Law of Motion', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                        canvas_Forcemotion_page8.create_text(300,250,text='''
                                                                             •  The impact produced by a moving object depends upon its mass and velocity.
                                                                             
                                                                             •  For Example, a small bullet fired at a high velocity can kill a person.
                                                                             
                                                                             •  Momentum – The product of mass and velocity is called Momentum.
                                                                             
                                                                             •  It is a vector quantity. Its direction is same as that of the object’s velocity. 
                                                                             
                                                                             •  Denoted by – p
                                                                             
                                                                             •  SI unit – kg metre per second''', font=('Adobe Fangsong Std R',16), fill = 'black')
                                        
                                        canvas_Forcemotion_page8.create_rectangle(200,500,650,700, outline='black', fill = 'PaleTurquoise1')
                                        canvas_Forcemotion_page8.create_text(160,580,text='''
                                                                             •  p = mv,
                                                                                     
                                                                                 where m is the mass of the object, 
                                                                             
                                                                                 v is the velocity of the object''', font=('Adobe Fangsong Std R',18), fill = 'RoyalBlue3')
                                        
                                        canvas_Forcemotion_page8.create_rectangle(750,400,1400,775, outline='black', fill = 'lemon chiffon')
                                        canvas_Forcemotion_page8.create_text(800,550,text='''
                                                                             •  The momentum of a stationary object –
                                                                                     
                                                                                 Let the mass of a stationary object be ‘m’,
                                                                             
                                                                                 Let the velocity of a stationary object be ‘v’,
                                                                             
                                                                                 The stationary object has no velocity, so v = 0,
                                                                             
                                                                                 Therefore, p = m*v = m*0 = 0''', font=('Adobe Fangsong Std R',18), fill = 'Springgreen4')
                                        canvas_Forcemotion_page8.create_text(790,720,text='''
                                                                                 So, the momentum of a stationary object is zero''', font=('Adobe Fangsong Std R',18,'bold'), fill = 'Springgreen4')
                                        
            
                                        def Back_Forcemotion_page8():
                                            phy_Forcemotion_page8.destroy()
            
                                        Back_Forcemotion_page8=Button(phy_Forcemotion_page8, bg='coral2', text='<--', command=Back_Forcemotion_page8)
                                        Back_Forcemotion_page8.pack()
                                        Back_Forcemotion_page8.place(relx=.0,rely=.0)
                                        
                                        def Forcemotion_page9():
                                            global phy_Forcemotion_page9
                                            phy_Forcemotion_page9=Toplevel()
                                            phy_Forcemotion_page9.title('Force and Laws of motion')
                                            canvas_Forcemotion_page9=Canvas(phy_Forcemotion_page9, width=1500, height=900, bg='white')
                                            canvas_Forcemotion_page9.pack(expand=YES,fill=BOTH)
                                            
                                            canvas_Forcemotion_page9.create_text(270,90,text='According to the second law of motion,', font=('Yu Gothic UI Semibold',18,'bold'), fill = 'black')
                                            canvas_Forcemotion_page9.create_text(380,140,text='''
                                                                                 The rate of change of momentum of an object is directly proportional to the applied unbalanced force on
                                                                                 the object in the direction of the force.''', font=('Adobe Fangsong Std R',16), fill = 'black')
                                            canvas_Forcemotion_page9.create_text(140,260,text='For Example:- ', font=('Yu Gothic UI Semibold',18,'bold'), fill = 'black')
                                            canvas_Forcemotion_page9.create_text(340,320,text='''
                                                                                 A cricketer when catches a ball pulls his hands in the backward direction to give some time to decrease
                                                                                 the velocity of the ball. As the acceleration of the ball decreases the force exerted on catching the 
                                                                                 moving ball also decreases. If the cricketer would try to stop a moving ball suddenly he would have to
                                                                                 apply larger force.''', font=('Adobe Fangsong Std R',16), fill = 'black')
                                            
                                            global cricketer
                                            cricketer = tkinter.PhotoImage(file="cricketer.png")
                                            button = Button(phy_Forcemotion_page9, image = cricketer ,width=407,height=401,font=("Courier",20,"bold"),bg='#94ffe2') 
                                            button.configure(image = cricketer)
                                            button.place(relx = 0.43, rely = 0.3, anchor = CENTER)
                                            
                                            def Back_Forcemotion_page9():
                                                phy_Forcemotion_page9.destroy()
            
                                            Back_Forcemotion_page9=Button(phy_Forcemotion_page9, bg='coral2', text='<--', command=Back_Forcemotion_page9)
                                            Back_Forcemotion_page9.pack()
                                            Back_Forcemotion_page9.place(relx=.0,rely=.0)
                                            
                                            def Forcemotion_page10():
                                                global phy_Forcemotion_page10
                                                phy_Forcemotion_page10=Toplevel()
                                                phy_Forcemotion_page10.title('Force and Laws of motion')
                                                canvas_Forcemotion_page10=Canvas(phy_Forcemotion_page10, width=1500, height=900, bg='white')
                                                canvas_Forcemotion_page10.pack(expand=YES,fill=BOTH)
                                                
                                                canvas_Forcemotion_page10.create_text(370,70,text='Mathematical Formulation of the Second Law of Motion', font=('Yu Gothic UI Semibold',18,'bold'), fill = 'black')
                                                canvas_Forcemotion_page10.create_text(170,120,text='''
                                                                                      Based on the definition of the second law of motion, we can infer that -''', font=('Adobe Fangsong Std R',16), fill = 'black')
                                            
                                                canvas_Forcemotion_page10.create_text(430,610,text='''
                                                                                     Therefore, with help of the second law of motion we can evaluate the amount of force that is being exerted on any object.
                                                                                     From the formula stated above, we can see that the force is directly proportional to acceleration. So the acceleration of
                                                                                     an object can change depending upon the change in force applied.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                canvas_Forcemotion_page10.create_text(400,720,text='''
                                                                                     Force = ma
                                                                                     SI Unit: kg-ms-2 or N (Newton)''', font=('Adobe Fangsong Std R',18,'bold'), fill = 'black')
                                                
                                                global secondlaw
                                                secondlaw = tkinter.PhotoImage(file="secondlaw.png")
                                                button = Button(phy_Forcemotion_page10, image = secondlaw ,width=617,height=261,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                button.configure(image = secondlaw)
                                                button.place(relx = 0.43, rely = 0.3, anchor = CENTER)
            
                                                def Back_Forcemotion_page10():
                                                    phy_Forcemotion_page10.destroy()
            
                                                Back_Forcemotion_page10=Button(phy_Forcemotion_page10, bg='coral2', text='<--', command=Back_Forcemotion_page10)
                                                Back_Forcemotion_page10.pack()
                                                Back_Forcemotion_page10.place(relx=.0,rely=.0)
                                                
                                                def Forcemotion_page11():
                                                    phy_Forcemotion_page11=Tk()
                                                    phy_Forcemotion_page11.title('Force and Laws of motion')
                                                    canvas_Forcemotion_page11=Canvas(phy_Forcemotion_page11, width=1500, height=900, bg='white')
                                                    canvas_Forcemotion_page11.pack(expand=YES,fill=BOTH)
                                                    canvas_Forcemotion_page11.create_text(700,60,text='Third Law of Motion - Action and Reaction Forces', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                    canvas_Forcemotion_page11.create_text(370,130,text='''
                                                                                          Two forces acting from opposite directions are called Action and Reaction Forces.For Example, a ball when hits the 
                                                                                          ground (action) bounces back with a certain force reaction.''', font=('Adobe Fangsong Std R',16), fill = 'black')
                                                    
                                                    canvas_Forcemotion_page11.create_oval(530,350,580,400, fill='blue')
                                                    canvas_Forcemotion_page11.create_line(300,500,800,500)
                                                    
                                                    canvas_Forcemotion_page11.create_line(575,405,615,495)
                                                    canvas_Forcemotion_page11.create_line(615,495,600,485)
                                                    canvas_Forcemotion_page11.create_line(615,495,620,480)
                                                    canvas_Forcemotion_page11.create_text(555,450, text='Action', font=('Adobe Fangsong Std R',12))

                                                    canvas_Forcemotion_page11.create_line(630,495,700,305)
                                                    canvas_Forcemotion_page11.create_line(700,305,685,315)
                                                    canvas_Forcemotion_page11.create_line(700,305,705,315)
                                                    canvas_Forcemotion_page11.create_text(710,400, text='Reaction', font=('Adobe Fangsong Std R',12))
                                                    
                                                    canvas_Forcemotion_page11.create_text(760,520, text='Ground', font=('Adobe Fangsong Std R',12))

                                                    canvas_Forcemotion_page11.create_text(300,590,text='The Third Law of Motion States that –', font=('Yu Gothic UI Semibold',18), fill = 'black')
                                                    canvas_Forcemotion_page11.create_text(400,650,text='''
                                                                                          When an object exerts a force on another object, the second object instantly exerts a force back onto the first object. 
                                                                                          These forces are always equal in magnitude but opposite in direction. These forces act on two different objects always.
                                                                                          Or in other words, every action has an equal and opposite reaction.''', font=('Adobe Fangsong Std R',16), fill = 'black')

                                                    
            
                                                    def Back_Forcemotion_page11():
                                                        phy_Forcemotion_page11.destroy()
            
                                                    Back_Forcemotion_page11=Button(phy_Forcemotion_page11, bg='coral2', text='<--', command=Back_Forcemotion_page11)
                                                    Back_Forcemotion_page11.pack()
                                                    Back_Forcemotion_page11.place(relx=.0,rely=.0)
                                                    
                                                    def Forcemotion_page12():
                                                        phy_Forcemotion_page12=Tk()
                                                        phy_Forcemotion_page12.title('Force and Laws of motion')
                                                        canvas_Forcemotion_page12=Canvas(phy_Forcemotion_page12, width=1500, height=900, bg='white')
                                                        canvas_Forcemotion_page12.pack(expand=YES,fill=BOTH)
                                                        
                                                        canvas_Forcemotion_page12.create_text(700,60,text='Conservation of Momentum', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                        canvas_Forcemotion_page12.create_text(400,180,text='''
                                                                                              As per the law of conservation of momentum, the sum of momenta of two objects before the collision and after collision remains the same
                                                                                              given that no external unbalanced force acts upon them. In another way, collision conserves the total momentum of two objects.''', font=('Adobe Fangsong Std R',16), fill = 'black')
                                                        
                                                        canvas_Forcemotion_page12.create_oval(150,350,250,450, fill='steelblue1')
                                                        canvas_Forcemotion_page12.create_oval(325,375,375,425, fill='steelblue1')
                                                        
                                                        canvas_Forcemotion_page12.create_oval(650,350,750,450, fill='steelblue1')
                                                        canvas_Forcemotion_page12.create_oval(750,375,800,425, fill='steelblue1')
                                                        
                                                        canvas_Forcemotion_page12.create_oval(1050,350,1150,450, fill='steelblue1')
                                                        canvas_Forcemotion_page12.create_oval(1225,375,1275,425, fill='steelblue1')
                                                        
                                                        canvas_Forcemotion_page12.create_text(700,460,text='Before Collision \t\t\t\t During Collision \t\t\t\t After Collision', font=('calibri',18), fill = 'black')

                                                        
                                                        canvas_Forcemotion_page12.create_text(400,650,text='''
                                                                                              Consider the figure given above. Two balls A and B having a certain initial velocities collide with each other. Conditions before the collision-
                                                                                              • There is no unbalanced force acting upon them
                                                                                              • The initial velocity of A is greater than initial velocity of B''', font=('Adobe Fangsong Std R',16), fill = 'black')

            
                                                        def Back_Forcemotion_page12():
                                                            phy_Forcemotion_page12.destroy()
            
                                                        Back_Forcemotion_page12=Button(phy_Forcemotion_page12, bg='coral2', text='<--', command=Back_Forcemotion_page12)
                                                        Back_Forcemotion_page12.pack()
                                                        Back_Forcemotion_page12.place(relx=.0,rely=.0)
                                                        
                                                        def Forcemotion_page13():
                                                            global phy_Forcemotion_page13
                                                            phy_Forcemotion_page13=Toplevel()
                                                            phy_Forcemotion_page13.title('Force and Laws of motion')
                                                            canvas_Forcemotion_page13=Canvas(phy_Forcemotion_page13, width=1500, height=900, bg='white')
                                                            canvas_Forcemotion_page13.pack(expand=YES,fill=BOTH)
                                                            
                                                            canvas_Forcemotion_page13.create_text(700,260,text='The figure below explains how the momentum of the balls is conserved after the collision.', font=('calibri',18), fill = 'black')
                                                            
                                                            global collision
                                                            collision = tkinter.PhotoImage(file="collision.png")
                                                            button = Button(phy_Forcemotion_page13, image = collision ,width=802,height=266,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                            button.configure(image = collision)
                                                            button.place(relx = 0.43, rely = 0.3, anchor = CENTER)
                                                            
                                                            def Back_Forcemotion_page13():
                                                                phy_Forcemotion_page13.destroy()
            
                                                            Back_Forcemotion_page13=Button(phy_Forcemotion_page13, bg='coral2', text='<--', command=Back_Forcemotion_page13)
                                                            Back_Forcemotion_page13.pack()
                                                            Back_Forcemotion_page13.place(relx=.0,rely=.0)
                                                            
                                                            def Forcemotion_page14():
                                                                phy_Forcemotion_page14=Tk()
                                                                phy_Forcemotion_page14.title('Force and Laws of motion')
                                                                canvas_Forcemotion_page14=Canvas(phy_Forcemotion_page14, width=1500, height=900, bg='white')
                                                                canvas_Forcemotion_page14.pack(expand=YES,fill=BOTH)
                                                                
                                                                canvas_Forcemotion_page14.create_text(700,60,text='Facts about Conservation Laws', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                canvas_Forcemotion_page14.create_text(500,330,text='''
                                                                                                      •  They are considered as the fundamental laws in physics.
                                                                                                      
                                                                                                      •  They are based on observations and experiments.
                                                                                                      
                                                                                                      •  They cannot be proved but can be verified or disproved with the help of experiments.
                                                                                                      
                                                                                                      •  A single experiment is enough to disprove a law, while a single experiment is not enough to prove the same.
                                                                                                      
                                                                                                      •  It requires a large number of experiments to prove the law.
                                                                                                      
                                                                                                      •  The law of conservation of momentum was formulated 300 years ago.
                                                                                                      
                                                                                                      •  There is no single situation present until now that disproves this law.
                                                                                                      
                                                                                                      •  Other laws of conservation are – law of conservation of energy, the law of conservation of angular momentum, the law of conservation of charge.''', font=('Adobe Fangsong Std R',16), fill = 'black')
                                                                                            
                                                                def Back_Forcemotion_page14():
                                                                    phy_Forcemotion_page14.destroy()
                                                                    
                                                                Back_Forcemotion_page14=Button(phy_Forcemotion_page14, bg='coral2', text='<--', command=Back_Forcemotion_page14)
                                                                Back_Forcemotion_page14.pack()
                                                                Back_Forcemotion_page14.place(relx=.0,rely=.0)
                                                                
                                                                def Back_to_class9_Forcemotion():
                                                                    phy_ForceLawsofmotion.destroy()
                                                                    phy_Forcemotion_page2.destroy()
                                                                    phy_Forcemotion_page3.destroy()
                                                                    phy_Forcemotion_page4.destroy()
                                                                    phy_Forcemotion_page5.destroy()
                                                                    phy_Forcemotion_page6.destroy()
                                                                    phy_Forcemotion_page7.destroy()
                                                                    phy_Forcemotion_page8.destroy()
                                                                    phy_Forcemotion_page9.destroy()
                                                                    phy_Forcemotion_page10.destroy()
                                                                    phy_Forcemotion_page11.destroy()
                                                                    phy_Forcemotion_page12.destroy()
                                                                    phy_Forcemotion_page13.destroy()
                                                                    phy_Forcemotion_page14.destroy()
                                                                
                                                                Back_to_class9_Forcemotion = Button(phy_Forcemotion_page14,bg='coral2', text='Class 9',font=('Castellar',18), command=Back_to_class9_Forcemotion)
                                                                Back_to_class9_Forcemotion.pack()
                                                                Back_to_class9_Forcemotion.place(relx=.87,rely=.85)
                                                            
                                                            Forcemotion_page14=Button(phy_Forcemotion_page13, bg='coral2', text='-->', command=Forcemotion_page14)
                                                            Forcemotion_page14.pack()
                                                            Forcemotion_page14.place(relx=.98, rely=.0)
                                                            
                                                        Forcemotion_page13=Button(phy_Forcemotion_page12, bg='coral2', text='-->', command=Forcemotion_page13)
                                                        Forcemotion_page13.pack()
                                                        Forcemotion_page13.place(relx=.98, rely=.0)
                
                                                    Forcemotion_page12=Button(phy_Forcemotion_page11, bg='coral2', text='-->', command=Forcemotion_page12)
                                                    Forcemotion_page12.pack()
                                                    Forcemotion_page12.place(relx=.98, rely=.0)
                
                                                Forcemotion_page11=Button(phy_Forcemotion_page10, bg='coral2', text='-->', command=Forcemotion_page11)
                                                Forcemotion_page11.pack()
                                                Forcemotion_page11.place(relx=.98, rely=.0)
                
                                            Forcemotion_page10=Button(phy_Forcemotion_page9, bg='coral2', text='-->', command=Forcemotion_page10)
                                            Forcemotion_page10.pack()
                                            Forcemotion_page10.place(relx=.98, rely=.0)
                
                                        Forcemotion_page9=Button(phy_Forcemotion_page8, bg='coral2', text='-->', command=Forcemotion_page9)
                                        Forcemotion_page9.pack()
                                        Forcemotion_page9.place(relx=.98, rely=.0)
                
                                    Forcemotion_page8=Button(phy_Forcemotion_page7, bg='coral2', text='-->', command=Forcemotion_page8)
                                    Forcemotion_page8.pack()
                                    Forcemotion_page8.place(relx=.98, rely=.0)
                
                                Forcemotion_page7=Button(phy_Forcemotion_page6, bg='coral2', text='-->', command=Forcemotion_page7)
                                Forcemotion_page7.pack()
                                Forcemotion_page7.place(relx=.98, rely=.0)
                
                            Forcemotion_page6=Button(phy_Forcemotion_page5, bg='coral2', text='-->', command=Forcemotion_page6)
                            Forcemotion_page6.pack()
                            Forcemotion_page6.place(relx=.98, rely=.0)
                
                        Forcemotion_page5=Button(phy_Forcemotion_page4, bg='coral2', text='-->', command=Forcemotion_page5)
                        Forcemotion_page5.pack()
                        Forcemotion_page5.place(relx=.98, rely=.0)
                
                    Forcemotion_page4=Button(phy_Forcemotion_page3, bg='coral2', text='-->', command=Forcemotion_page4)
                    Forcemotion_page4.pack()
                    Forcemotion_page4.place(relx=.98, rely=.0)
                
                Forcemotion_page3=Button(phy_Forcemotion_page2, bg='coral2', text='-->', command=Forcemotion_page3)
                Forcemotion_page3.pack()
                Forcemotion_page3.place(relx=.98, rely=.0)
                
            Forcemotion_page2=Button(phy_ForceLawsofmotion, bg='coral2', text='-->', command=Forcemotion_page2)
            Forcemotion_page2.pack()
            Forcemotion_page2.place(relx=.98, rely=.0)
                              
        def Gravitation9():
            phy_Gravitation9=Tk()
            phy_Gravitation9.title('Gravitation')
            canvas_Gravitation9=Canvas(phy_Gravitation9, width=1500, height=900, bg='grey12')
            canvas_Gravitation9.pack(expand=YES,fill=BOTH)
            
            canvas_Gravitation9.create_oval(300,300,700,700, fill='orange')
            canvas_Gravitation9.create_oval(800,300,900,400,fill='white')
            canvas_Gravitation9.create_oval(100,100,900,900,outline='white')
            canvas_Gravitation9.create_oval(0,0,1000,1000,outline='white')
            canvas_Gravitation9.create_oval(200,150,300,250, fill='royalblue2')
            canvas_Gravitation9.create_text(500,600,text='GRAVITATION',font=('Backlash BRK',50), fill = 'white')
            
            def Back_Gravitation9():
                phy_Gravitation9.destroy()
            
            Back_Gravitation9=Button(phy_Gravitation9, bg='coral2', text='<--', command=Back_Gravitation9)
            Back_Gravitation9.pack()
            Back_Gravitation9.place(relx=.0,rely=.0)
                        
            def grav_page1():
                phy_grav_page1=Tk()
                phy_grav_page1.title('Gravitation')
                canvas_grav_page1=Canvas(phy_grav_page1, width=1500, height=900, bg='grey12')
                canvas_grav_page1.pack(expand=YES, fill=BOTH)
                canvas_grav_page1.create_text(500,50, text='CENTRIPETAL FORCE', font=('courier', 40), fill='white')
                canvas_grav_page1.create_text(500,200, text='TANGENT', font=('courier', 20), fill='white')
                canvas_grav_page1.create_arc(400, 300, 600,500, style=ARC, start=0, extent=359, outline='white')                
                canvas_grav_page1.create_line(300,300,700, 300, fill='white')
                canvas_grav_page1.create_text(300, 520, text='Tangent to a circle', font=('courier',14), fill='white')                
                canvas_grav_page1.create_text(800,300,text='''
                A straight line that 
                meets the circle at one
                and only one point is called a
                tangent to the circle. Straight
                line ABC is a tangent
                to the circle at B.''', font=('courier', 14), fill='white')
                canvas_grav_page1.create_text(800,550, text='WHAT IS CENTRIPETAL FORCE?', font=('courier',18), fill='white')
                canvas_grav_page1.create_text(600,620, text='''

    We know that an object in circular motion keeps on changing its direction.
    Due to this, the velocity of the object also changes.
    A force called Centripetal Force acts upon the object that keeps it moving in a circular path.
    The centripetal force is exerted from the centre of the path.
    Without the Centripetal Force objects cannot move in circular paths, they would always travel straight.
    For Example, The rotation of Moon around the Earth is possible because of the centripetal force exerted by Earth.
''', font=('courier',12), fill='white')
                
                def Back_grav_page1():
                    phy_grav_page1.destroy()
            
                Back_grav_page1=Button(phy_grav_page1, bg='coral2', text='<--', command=Back_grav_page1)
                Back_grav_page1.pack()
                Back_grav_page1.place(relx=.0,rely=.0)
                
                def grav_page2():
                    phy_grav_page2=Tk()
                    phy_grav_page2.title('Gravitation')
                    canvas_grav_page2=Canvas(phy_grav_page2, width=1500, height=900, bg='grey12')
                    canvas_grav_page2.pack(expand=YES, fill=BOTH)
                    xy=300,300,500,500
                    canvas_grav_page2.create_arc(xy, style=ARC, start=0, extent=359, outline='white', fill='snow4')
                    xy1=750,350,850,450                    
                    canvas_grav_page2.create_arc(xy1, style=ARC, start=0, extent=359, outline='grey', fill='snow4')
                    canvas_grav_page2.create_line(400,400,800,400, fill='white')
                    canvas_grav_page2.create_line(400,430,580,430, fill='white')
                    canvas_grav_page2.create_line(620,430,800,430, fill='white')
                    canvas_grav_page2.create_line(407,420,400,430, fill='white')
                    canvas_grav_page2.create_line(400,430,407,440, fill='white')
                    canvas_grav_page2.create_line(793,420,800,430, fill='white')
                    canvas_grav_page2.create_line(793,440,800,430, fill='white')
                    canvas_grav_page2.create_text(600,430, text='d', font=('courier',14), fill='white')
                    
                    canvas_grav_page2.create_rectangle(500,498,650,545, fill='cyan', outline='white')
                    canvas_grav_page2.create_text(590,515,text='F=________', font=('courier',14), fill='black')
                    canvas_grav_page2.create_text(593,505, text='GMm', font=('courier',14), fill='black')                    
                    canvas_grav_page2.create_text(602,528, text='2', font=('courier',10), fill='black')
                    canvas_grav_page2.create_text(593,535, text='d', font=('courier',14), fill='black')
                    
                    canvas_grav_page2.create_text(700,50, text='NEWTON\'S OBSERVATIONS', font=('courier',18), fill='white')
                    canvas_grav_page2.create_text(650,100, text='''
Why does Apple fall on Earth from a tree? – Because the earth attracts it towards itself.
Can Apple attract the earth?  - Yes. It also attracts the earth as per Newton's third law (every action has an equal and opposite reaction).
But the mass of the earth is much larger than Apple's mass thus the force applied by Apple appears negligible and Earth never moves towards it.
Newton thus suggested that all objects in this universe attract each other. This force of attraction is called Gravitational Force.
''', font=('courier',12), fill='white')
                    canvas_grav_page2.create_text(700,170, text='UNIVERSAL LAW OF GRAVITATION BY NEWTON', font=('courier',18 ), fill='white')
                    canvas_grav_page2.create_text(700,240, text='''
According to the universal law of gravitation, every object attracts every other object with a force.
This force is directly proportional to the product of their masses.
This force is inversely proportional to the square of distances between them.
Consider the figure given below. It depicts the force of attraction between two objects with masses m1 and m2
respectively that are ‘d’ distance apart.
''', font=('courier',12), fill='white')
                    canvas_grav_page2.create_text(700,620, text='''
From the definition,
F ∝ m1m2
F ∝ 1/d^2
Combining, F ∝ m1m2/d^2
Therefore, F = Gm1m2/d^2, where G is Universal Grvitational Constant
G = 6.67 x 10^-11 Nm^2 kg^-2 
''', font=('courier',12), fill='white')
                    
                    def Back_grav_page2():
                        phy_grav_page2.destroy()
            
                    Back_grav_page2=Button(phy_grav_page2, bg='coral2', text='<--', command=Back_grav_page2)
                    Back_grav_page2.pack()
                    Back_grav_page2.place(relx=.0,rely=.0)
                    
                    def grav_page3():
                        phy_grav_page3=Tk()
                        phy_grav_page3.title('Gravitation')
                        canvas_grav_page3=Canvas(phy_grav_page3, width=1500, height=900, bg='grey12')
                        canvas_grav_page3.pack(expand=YES, fill=BOTH)
                        canvas_grav_page3.create_text(700,100,text='Why we study the universal law of gravitation?', font=('courier',20), fill='white')
                        canvas_grav_page3.create_text(700,150, text='''

It explains many important phenomena of the universe –
    1.Earth’s gravitational force
    2.Why the moon always moves in a circular motion around the earth and the sun
    3.Why all planets revolve around the sun
    4.How the sun and moon can cause tides
''',font=('courier',12), fill='white')
                        canvas_grav_page3.create_text(700,250, text='Free Fall', font=('courier',20), fill='white')
                        canvas_grav_page3.create_text(700,500, text='''
    Acceleration due to gravity – Whenever an object falls towards the Earth there is an acceleration associated 
    with the movement of the object. This acceleration is called acceleration due to gravity.
    Denoted by: g
    SI Unit: m s^-2
    We know that, F= ma (Newton's Second Law )
    Therefore, F = mg  ---(1)
    
    Also, F = GMm/R^2  (Universal Law of Gravitation)  ---(2)
    
    From (1) and (2)
    mg = GMm/R^2
    Therefore, g = GM / R^2
    
    
    Value of ‘g' may vary at different parts of the earth –

    From the equation g = GM/ r2 it is clear that the value of ‘g' depends upon the distance 
    of the object from the earth's centre.This is because the shape of the earth is not a perfect sphere.
    It is rather flattened at poles and bulged out at the equator. Hence, the value of ‘g' is greater at the
    poles and lesser at the equator. However, for our convenience, we take a constant value of ‘g' throughout.

''', font=('courier',12), fill='white')
                        def Fg():
                            import tkinter as tk
                            
                            def show_entry_fields():
                                #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
                                f=(6.67*10**-11 *int(e1.get())*int(e2.get()))/6400 *10**-3
                                tk.Label(master, text='Gravitational force on earth=').grid(row=2,column=0)
                                tk.Label(master, text=(f,'N')).grid(row=2, column=1)

                            master = tk.Tk()
                            tk.Label(master, text="Mass of Object").grid(row=0)
#                            tk.Label(master, 
 #                                    text="Charge").grid(row=1)
                                     
                            e1 = tk.Entry(master)
  #                          e2 = tk.Entry(master)
                                     
                            e1.grid(row=0, column=1)
   #                         e2.grid(row=1, column=1)
                                     
                            tk.Button(master, 
                                     text='Quit', 
                                     command=master.quit).grid(row=3, 
                                                                column=0, 
                                                                sticky=tk.W, 
                                                                pady=4)
                            tk.Button(master, 
                                      text='Show', command=show_entry_fields).grid(row=3, 
                                                                        column=1, 
                                                                        sticky=tk.W, 
                                                                        pady=4)
                            tk.mainloop()  
                        
                        def Back_grav_page3():
                            phy_grav_page3.destroy()
            
                        Back_grav_page3=Button(phy_grav_page3, bg='coral2', text='<--', command=Back_grav_page3)
                        Back_grav_page3.pack()
                        Back_grav_page3.place(relx=.0,rely=.0)
                        
                        def grav_page4():
                            phy_grav_page4=Tk()
                            phy_grav_page4.title('Gravitation')
                            canvas_grav_page4=Canvas(phy_grav_page4, width=1500, height=900, bg='grey12')
                            canvas_grav_page4.pack(expand=YES, fill=BOTH)
                            
                            canvas_grav_page4.create_rectangle(20,400,620,440, fill='orange')
                            canvas_grav_page4.create_rectangle(623,400,1350,440, fill='orange')
                            canvas_grav_page4.create_rectangle(20,443,620,700, fill='white')
                            canvas_grav_page4.create_rectangle(623,443,1350,700, fill='white')
                            
                            canvas_grav_page4.create_text(700,50, text='What is Free Fall?', font=('courier',20),fill='white')
                            canvas_grav_page4.create_text(700,200, text='''
When an object falls towards the earth due to earth’s gravity and no other force is acting upon it, 
the object is said to be in free fall state. Free falling objects are not even resisted by the air.
g = 9.8 m/s^2 is also called the Free-fall Acceleration.

Value of ‘g' is same on the earth, so the equations of motion for an object with uniform motion are valid 
where acceleration ‘a' is replaced by ‘g', as given under:
    
v = u + gt

s = ut + (1/2) gt^2

2 g s = v^2 – u^2
    
    ''', font=('courier',12), fill='white')
                            canvas_grav_page4.create_text(700,350, text='Difference between Universal gravitational Constant and Acceleration due to Gravity', font=('courier',20),fill='white' )
                            canvas_grav_page4.create_text(700,550, text='''
Mass 	                                                          Weight 

Mass is defined as the quantity                                The weight of an object is the force by which
of matter in an object.                                        the gravitational pull of earth attracts the object.

Mass is a scalar quantity                                      Weight is a vector quantity 

The mass of an object is always constant as                    The weight of an object can vary at different 
it depends upon the inertia of the object                      locations because of change in gravitational force of the earth

Mass can never be zero                                         Weight can be zero at places there is no gravitational force

Denoted as: m                                                  Denoted  as W

SI Unit: kg                                                    SI unit: N 
''', font=('courier',12), fill='black')
                            
                        
                                
                            def Back_grav_page4():
                                phy_grav_page4.destroy()
                                
                            def grav_page5():
                                phy_grav_page5=Tk()
                                phy_grav_page5.title('Gravitation')
                                canvas_grav_page5=Canvas(phy_grav_page5, width=1500, height=900, bg='grey12')
                                canvas_grav_page5.pack(expand=YES, fill=BOTH)
                                canvas_grav_page5.create_text(700,100, text='Weight of an object on the Moon', font=('courier new',16), fill='white')
                                
                                canvas_grav_page5.create_text(700,200,text='''
Just like the Earth, the Moon also exerts a force upon objects. Hence, objects on moon also have 
some weight. The weight willnot be same as than on the earth. So, weight on the Moon can be calculated as -''', font=('courier',14), fill='white')
                                
                                def grav_page6():
                                    phy_grav_page6=Tk()
                                    phy_grav_page6.title('Gravitation')
                                    canvas_grav_page6=Canvas(phy_grav_page6, width=1500, height=900, bg='grey12')
                                    canvas_grav_page6.pack(expand=YES, fill=BOTH)
                                    
                                    canvas_grav_page6.create_text(700,100, text='Thrust', font=('courier new',16), fill='white')
                                    canvas_grav_page6.create_text(700,200, text='''
•	The force that acts in the perpendicular direction is called thrust.

•	It is similar to force applied to an object

•	It is a vector quantity.
                                                                  ''', font=('courier new',12), fill='white')
                                    canvas_grav_page6.create_text(700,300, text='Pressure', font=('courier new',16), fill='white')
                                    canvas_grav_page6.create_text(700,400, text='''
•	The force that acts per unit area of the object is pressure.

•	It is the thrust per unit area.

•	Pressure is denoted by ‘P'

•	P = thrust/ area = force/ area = F/A

•	SI unit: N/m2 or Pa (Pascal)                                                                  ''', font=('courier new',12), fill='white')
                                
                                    def grav_page7():
                                        phy_grav_page7=Tk()
                                        phy_grav_page7.title('Gravitation')
                                        canvas_grav_page7=Canvas(phy_grav_page7, width=1500, height=900, bg='grey12')
                                        canvas_grav_page7.pack(expand=YES, fill=BOTH)
                                        
                                        canvas_grav_page7.create_text(700,100, text='Why do nails have sharp edges?', font=('courier new',18), fill='white')
                                        canvas_grav_page7.create_text(700,250, text='''
We know that pressure is inversely proportional to area. As area increases, pressure decreases and vice versa. 
So, nails' sharp edges make it easier for them to get into the wall because more pressure is exerted on the wall 
from a single point.

•	Solids - They exert pressure on the surface because of their weight.

•	Fluids (gases and liquids) - They also have weight, therefore, they exert pressure on the surface and the

                                 walls of the container in which they are put in.
                                                                      ''', font=('courier new',14), fill='white')
                                        canvas_grav_page7.create_text(700,400, text='Buoyancy', font=('courier new',18), fill='white')
                                        canvas_grav_page7.create_text(700,550, text='''
•	Whenever an object is immersed in a liquid, the liquid exerts a buoyant force or upthrust in the opposite 
    direction of the gravitational force. This is also called the Force of Buoyancy.
    
•	It depends upon the density of the fluid.

•	Therefore an object is able to float in water when the gravitational force is less than the buoyant force.

•	Similarly, an object sinks into the water when the gravitational force is larger than the buoyant force.
                                                                      ''', font=('courier new',14), fill='white')
                                                                      
                                        def grav_page8():
                                            phy_grav_page8=Tk()
                                            phy_grav_page8.title('Gravitation')
                                            canvas_grav_page8=Canvas(phy_grav_page8, width=1500, height=900, bg='grey12')
                                            canvas_grav_page8.pack(expand=YES, fill=BOTH)
                                            canvas_grav_page8.create_text(700,100, text='Why does an object sink or float on water', font=('courier new',18), fill='white')
                                            canvas_grav_page8.create_text(700,250, text='''
•	An object can sink or float on water based on its density with respect to water. The density is defined as mass per unit volume.
•	Objects having a density less than water float in it. For Example, Cork flows in water because its density is lower
 than that of water. 
•	Objects that have a density higher than water sink in it. For Example, Iron nail sinks in water
 because the density of iron is more than water's density.

•	Thus, we can conclude that buoyancy depends upon:
o	The density of the liquid
o	The volume of the object (as the volume of object increases, its density decreases and vice-versa)

                                                                          ''', font=('courier new',14), fill='white')
                                            canvas_grav_page8.create_text(700,400, text='Archimedes Principle', font=('courier new',18), fill='white')
                                            canvas_grav_page8.create_text(700,550, text='''
According to the Archimedes principle, whenever an object is immersed in a liquid (fully or partially), the liquid 
exerts an upward force upon the object. The amount of that force is equivalent to the weight of the liquid displaced by the object.
This means that if the weight of an object is greater than the amount of liquid it displaces, the object will sink into the liquid.
 However, if the weight of an object is less than the amount of water it displaces, the object will sink.
 
•	Submarines have a tank called Buoyancy Tank. Whenever the submarine needs to be taken inside water the tank 
is filled which thus increases the weight of the submarine. Similarly, when the submarine is to appear above water 
the tank is emptied and the weight of the submarine becomes lighter and it rises above the water.

•	Ships are heavier than water but their unique shape gives them a large volume. Their volume is larger than 
their weight and hence the water displaced by a ship provides it with the right upthrust so that it can float on water.

                                                                          ''', font=('courier new',14), fill='white')
                                            
                                            def grav_page9():
                                                phy_grav_page9=Tk()
                                                phy_grav_page9.title('Gravitation')
                                                canvas_grav_page9=Canvas(phy_grav_page9, width=1500, height=900, bg='grey12')
                                                canvas_grav_page9.pack(expand=YES, fill=BOTH)
                                                
                                                canvas_grav_page9.create_text(700,50, text='Applications of Archimedes Principle', font=('courier new',18), fill='white')
                                                canvas_grav_page9.create_text(700,150, text='''
•	In evaluating relative density

•	In designing ships and submarines

•	In making lactometers and hydrometers
                                                                          ''', font=('courier new',14), fill='white')
                                                canvas_grav_page9.create_text(700,250, text='What is relative density?', font=('courier new',18), fill='white')
                                                canvas_grav_page9.create_text(700,350, text='''
When density can be expressed in comparison with water's density it is called Relative Density. It has no unit
 because it is a ratio of two similar quantities. 
 
 Density = Mass / Volume
 
 Relative Density = Density of Substance / Density of Water
                                                                        ''', font=('courier new',14), fill='white')
                                                canvas_grav_page9.create_text(700,500, text='Why Water is chosen as a Reference ?', font=('courier new',18), fill='white')
                                                canvas_grav_page9.create_text(700,600, text='''
Water is present everywhere on earth so it becomes easier to evaluate the 
density of a substance in relation to water.
                                                                        ''', font=('courier new',14), fill='white')
                                                                        
                                                def Back_to_class9_grav():
                                                    phy_Gravitation9.destroy()
                                                    phy_grav_page1.destroy()
                                                    phy_grav_page2.destroy()
                                                    phy_grav_page3.destroy()
                                                    phy_grav_page4.destroy()
                                                    phy_grav_page5.destroy()
                                                    phy_grav_page6.destroy()
                                                    phy_grav_page7.destroy()
                                                    phy_grav_page8.destroy()
                                                    phy_grav_page9.destroy()
                                                
                                                Back_to_class9_grav=Button(phy_grav_page9,bg='coral2', text='Class 9',font=('Castellar',18), command=Back_to_class9_grav)
                                                Back_to_class9_grav.pack()
                                                Back_to_class9_grav.place(relx=.87,rely=.85)
                                                
                                            Grav_page9=Button(phy_grav_page8, bg='coral2', text='-->', command=grav_page9)
                                            Grav_page9.pack()
                                            Grav_page9.place(relx=.98,rely=.0)
                                               
                                        Grav_page8=Button(phy_grav_page7, bg='coral2', text='-->', command=grav_page8)
                                        Grav_page8.pack()
                                        Grav_page8.place(relx=.98,rely=.0)
                                
                                    Grav_page7=Button(phy_grav_page6, bg='coral2', text='-->', command=grav_page7)
                                    Grav_page7.pack()
                                    Grav_page7.place(relx=.98,rely=.0)
                                
                                def Back_grav_page5():
                                    phy_grav_page5.destroy()
                                
                                Grav_page6=Button(phy_grav_page5, bg='coral2', text='-->', command=grav_page6)
                                Grav_page6.pack()
                                Grav_page6.place(relx=.98,rely=.0)
                                
                                Back_grav_page5=Button(phy_grav_page5, bg='coral2', text='<--', command=Back_grav_page5)
                                Back_grav_page5.pack()
                                Back_grav_page5.place(relx=.0,rely=.0)
                                
                                phy_grav_page5.mainloop()
                            
                            Grav_page5=Button(phy_grav_page4, bg='coral2', text='-->', command=grav_page5)
                            Grav_page5.pack()
                            Grav_page5.place(relx=.98,rely=.0)
                            
                            Back_grav_page4=Button(phy_grav_page4, bg='coral2', text='<--', command=Back_grav_page4)
                            Back_grav_page4.pack()
                            Back_grav_page4.place(relx=.0,rely=.0)
                
                        Grav_page4=Button(phy_grav_page3, bg='coral2', text='-->', command=grav_page4)
                        Grav_page4.pack()
                        Grav_page4.place(relx=.98, rely=.0)
                        
                    Grav_page3=Button(phy_grav_page2, bg='coral2', text='-->', command=grav_page3)
                    Grav_page3.pack()
                    Grav_page3.place(relx=.98, rely=.0)
                    
                Grav_page2=Button(phy_grav_page1, bg='coral2', text='-->', command=grav_page2)
                Grav_page2.pack()
                Grav_page2.place(relx=.98, rely=.0)
            
            Grav_page1=Button(phy_Gravitation9, bg='coral2', text='-->', command=grav_page1)
            Grav_page1.pack()
            Grav_page1.place(relx=.98, rely=.0)
                        
        def Work_and_Energy():
            phy_WorkEnergy=Tk()
            phy_WorkEnergy.title('Work and Energy')
            canvas_WorkEnergy=Canvas(phy_WorkEnergy, width=1500, height=900, bg='grey12')
            canvas_WorkEnergy.pack(expand=YES,fill=BOTH)
            
            canvas_WorkEnergy.create_text(600,100, text='WORK', font=('courier',40), fill='white')
            canvas_WorkEnergy.create_text(300,400,text='''
                                          The definition of work done may vary in real life and scientifically. For Example, We may 
                                          consider studying, talking, singing, reading as work but it is not so in the case of science.
                                          Examples of Scientific Work Done are:
                                              
                                          1)Moving a chair from one location to another
                                          
                                          2)Lifting a book from the shelf and placing it on a table
                                          
                                          3)Pushing a pebble lying on the ground.
                                          
                                          4)In all these situations we are applying a force on 
                                            an object which is then changing the state of rest or motion of the object.
                                          
                                         So, we can conclude that work is done if and only if:
                                             1)A force is applied to an object.
                                              
                                             2)If the object is displaced from one point to another point.
                                          
                                         These are also called ‘Conditions of Work Done'.

''',font=('courier',12),fill='white' )
                
            def Back_WorkEnergy():
                phy_WorkEnergy.destroy()
            
            Back_WorkEnergy=Button(phy_WorkEnergy, bg='coral2', text='<--', command=Back_WorkEnergy)
            Back_WorkEnergy.pack()
            Back_WorkEnergy.place(relx=.0,rely=.0)
            
            def workenergy_page1():
                phy_workenergy_page1=Tk()
                phy_workenergy_page1.title('Work and Energy')
                canvas_workenergy_page1=Canvas(phy_workenergy_page1, width=1500, height=900, bg='white')
                canvas_workenergy_page1.pack(expand=YES, fill=BOTH)
                canvas_workenergy_page1.create_text(600,200,text='Work done by a constant force',font=('courier',20), fill='black')

                canvas_workenergy_page1.create_rectangle(840,100,1300,240,outline='black', fill='yellow')
                canvas_workenergy_page1.create_rectangle(840,250,1300,400,outline='black', fill='orange')
                canvas_workenergy_page1.create_rectangle(840,405,1300,540,outline='black', fill='yellow')
                canvas_workenergy_page1.create_rectangle(0,440,325,580,outline='black', fill='orange')
                
                canvas_workenergy_page1.create_rectangle(400,350,800,370, outline='black')
                canvas_workenergy_page1.create_polygon(400,350,800,350,775,335,425,335)
                canvas_workenergy_page1.create_rectangle(400,370,415,500,outline='black')
                canvas_workenergy_page1.create_rectangle(785,370,800,500,outline='black')
                canvas_workenergy_page1.create_rectangle(450,335, 490, 300, outline='black', fill='yellow')
                canvas_workenergy_page1.create_line(440,320,390, 320)
                canvas_workenergy_page1.create_line(425,310, 440,320)
                canvas_workenergy_page1.create_line(440,320, 425,330)
                canvas_workenergy_page1.create_text(415,290, text='Force', font=('courier',14), fill='black')
                canvas_workenergy_page1.create_rectangle(700,335,740,300, outline='black', fill='yellow')
                canvas_workenergy_page1.create_line(500,320, 680, 320)
                canvas_workenergy_page1.create_line(665,310,680,320)
                canvas_workenergy_page1.create_line(680,320,665,330)
                canvas_workenergy_page1.create_text(590,290,text='displacement',font=('courier',14), fill='black')
                
                canvas_workenergy_page1.create_line(350,20,350,880)
                canvas_workenergy_page1.create_line(840,20,840,880)
                canvas_workenergy_page1.create_text(170,100, text='''
When you play a certain force 
‘F Newton’ on an object
and the object moves a distance
of ‘ d meters’ in the 
direction where you applied
the force then, the amount 
of work done can be calculated as:''', font=('courier',11), fill='black')
                canvas_workenergy_page1.create_rectangle(10,200,320,400, outline='black')
                canvas_workenergy_page1.create_text(160,220,text='Work done = Force x Displacement', font=('courier',11), fill='black')
                canvas_workenergy_page1.create_rectangle(70,250, 300, 290, outline='black', fill='cyan')
                canvas_workenergy_page1.create_text(160, 265, text='W = F x d', font=('courier',20), fill='black')
                canvas_workenergy_page1.create_rectangle(20, 300, 300, 350, outline='black', fill='cyan')
                canvas_workenergy_page1.create_text(160,330, text='W=F.d\n  =F x d cos(theta)', font=('courier',16), fill='black')
                canvas_workenergy_page1.create_text(160, 370, text='where theta is the angle between\n the direction of force\n and displacement', font=('courier',10), fill='black')
                canvas_workenergy_page1.create_text(170,420, text='SI unit of Work: N-m or J (Joule)', font=('courier',11),fill='black')
                canvas_workenergy_page1.create_text(170,450, text='What is 1 Joule Work?', font=('courier',14),fill='black')
                canvas_workenergy_page1.create_text(170,510, text='''
A situation where 1 Newton force is
applied on an object that can move 
the object by a distance of 1m in 
the direction of the applied force,
 then 1 joule of work is said to
 be done.''', font=('courier',11),fill='black')
                
                canvas_workenergy_page1.create_text(860,300, text='''
                                                    ->If direction of displacement is 
                                                    same as the direction of force:
                                                    
                                                    1) W= F.d = F x d
                                                    2)Nature of Work Done : Positive
                                                    3)Angle between Force applied and Displacement
                                                      occurred (degrees) : 0
                                                      
                                                      
                                                      
                                                    ->If direction of displacement is
                                                    opposite to the direction of force :
                                                        
                                                    1) W = F.d = - F x d
                                                    2)Nature of Work Done : Negative
                                                    3)Angle between Force applied and Displacement
                                                      occured( degrees ) : 180
                                                      
                                                      
                                                      
                                                    ->If direction of displacement is
                                                      perpendicular to the direction of force :
                                                    1) W= F.d = 0
                                                    2)Nature of work done : Zero
                                                    3)Angle between Force applied and Displacement
                                                       occured ( degrees ) : 90
                                                    ''', font=('courier',10), fill='black')
                    
                def W():
                    import tkinter as tk
                    
                    def show_entry_fields():
                        #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
                        wo=int(e1.get())*int(e2.get())
                        tk.Label(master, text='Work=').grid(row=2,column=0)
                        tk.Label(master, text=(wo,'J')).grid(row=2, column=1)
                        
                    master = tk.Tk()
                    tk.Label(master, text="Force(N)").grid(row=0)
                    tk.Label(master, 
                             text="Displacement(m)").grid(row=1)
                    
                    e1 = tk.Entry(master)
                    e2 = tk.Entry(master)
                    
                    e1.grid(row=0, column=1)
                    e2.grid(row=1, column=1)
                    
                    tk.Button(master, 
                              text='Quit', 
                              command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
                    tk.Button(master, 
                              text='Show', command=show_entry_fields).grid(row=3, 
                                                                                            column=1, 
                                                                                            sticky=tk.W, 
                                                                                            pady=4)
                    tk.mainloop()
                    
                def Back_workenergy_page1():
                    phy_workenergy_page1.destroy()
            
                Back_workenergy_page1=Button(phy_workenergy_page1, bg='coral2', text='<--', command=Back_workenergy_page1)
                Back_workenergy_page1.pack()
                Back_workenergy_page1.place(relx=.0,rely=.0)
                
                def WorkEnergy_page2():
                    phy_workenergy_page2=Tk()
                    phy_workenergy_page2.title('Work and Energy')
                    canvas_workenergy_page2=Canvas(phy_workenergy_page2,width=1500, height=900, bg='white')
                    canvas_workenergy_page2.pack(expand=YES, fill=BOTH)
                    canvas_workenergy_page2.create_text(300,50,text='ENERGY',font=('courier',40), fill='black')
                    canvas_workenergy_page2.create_rectangle(20,170,1350,240, outline='black', fill='cyan')
                    canvas_workenergy_page2.create_rectangle(20,250,1350,290, outline='black', fill='orange')
                    canvas_workenergy_page2.create_rectangle(20,300,1350,360, outline='black', fill='cyan')
                    canvas_workenergy_page2.create_rectangle(20,365,1350,440, outline='black', fill='orange')
                    canvas_workenergy_page2.create_rectangle(20,445,1350,490, outline='black', fill='cyan')
                    canvas_workenergy_page2.create_rectangle(20,495,1350,545, outline='black', fill='orange')
                    canvas_workenergy_page2.create_rectangle(20,550,1350,590, outline='black', fill='cyan')
                    canvas_workenergy_page2.create_rectangle(20,595,1350,670, outline='black', fill='orange')
                    canvas_workenergy_page2.create_text(300, 100, text='''
                                                                Any object that is capable of doing work processes some energy. The object can gain or lose energy depending upon 
                                                                the work done. If an object does some work it loses its energy and if some work is done on an object it gains energy.''', font=('courier',12), fill='black')
                    canvas_workenergy_page2.create_text(300,150, text='Different forms of Energy', font=('courier',20), fill='black')
                    canvas_workenergy_page2.create_text(500,420, text='''
                                                        1.Mechanical Energy – It is the sum of kinetic and 
                                                                                potential energy of an object. Therefore, it is the energy obtained by 
                                                                                an object due to motion or by the virtue of its location. Example, a bicycle climbing
                                                                                a hill possesses kinetic energy as well as potential energy.
                                                        
                                                        2.  Heat Energy – It is the energy obtained by an object due to its temperature. It is
                                                                          also called Thermal Energy. Example, energy possessed by a hot cup
                                                        
                                                        3.  Chemical Energy – It is the energy accumulated in 
                                                                              bonds of chemical compounds. Chemical energy is released at the time
                                                                              of chemical reactions. Example, energy possessed by natural gas and biomass.	
                                                        
                                                        4.  Electrical Energy – It is kind of kinetic energy 
                                                                                caused due to the motion of electrons. It depends upon the speed of 
                                                                                electrons. As the speed increases so does the electrical energy. 
                                                                                Example, electricity produced by a battery, lightning at thunderstorms	
                                                        
                                                        5.  Light Energy – It is the energy due to light or electromagnetic waves. It is also called as Radiant Energy
                                                                            or Electromagnetic Energy. Example, energy from the sun
                                                        
                                                        6.  Nuclear Energy – It is the energy present in the nucleus of an atom. Nuclear energy releases when the nucleus combines or 
                                                                             separate. Therefore, we can say that every atom in this universe comprises of nucleus energy. Example, 
                                                                             uranium is a radioactive metal capable of producing nuclear energy in nuclear power plants
                                                        
                                                        7.  Sonic Energy – It is the energy produced by a substance as it vibrates. This energy flows through the substance in the form of sound waves.
                                                                            Example, music instruments produce sound energy
                                                        
                                                        8.  Ionization Energy – It is the energy that binds 
                                                                                electrons with its nucleus. It is thus the amount of energy required to 
                                                                                remove one electron completely from its atom (called First Ionization Energy).
                                                                                Subsequently, the ionization energy increases as we remove the second electron from the atom ( called Second Ionization Energy).
                                                                                ''', font=('courier',10), fill='black')
                        
                    def Back_workenergy_page2():
                        phy_workenergy_page2.destroy()
            
                    Back_workenergy_page2=Button(phy_workenergy_page2, bg='coral2', text='<--', command=Back_workenergy_page2)
                    Back_workenergy_page2.pack()
                    Back_workenergy_page2.place(relx=.0,rely=.0)
                    
                    def workenergy_page3():
                        phy_workenergy_page3=Tk()
                        phy_workenergy_page3.title('Work and Energy')
                        canvas_workenergy_page3=Canvas(phy_workenergy_page3,width=1500, height=900, bg='white')
                        canvas_workenergy_page3.pack(expand=YES, fill=BOTH)
                        canvas_workenergy_page3.create_text(300,100,text='KINETIC ENERGY',font=('courier',40), fill='black')
                        canvas_workenergy_page3.create_text(300, 120, text='''
                                                            Every moving object possesses some energy called Kinetic Energy. As the speed of the object increases so is its 
                                                            kinetic energy.''',font=('courier',12), fill='black')
                        canvas_workenergy_page3.create_rectangle(200,450,600,480, outline='black', fill='orange')
                        canvas_workenergy_page3.create_text(300,300,text=''' 
                                                            Work Done  W= F x s                      ---(i)
                                                            Due to the force, the velocity changes to v and the acceleration produced is a
                                                            Therefore, Relationship between v, u and s is given by 
                                                            2as = v - u
                                                            
                                                            s = ______                          ----(ii)
                                                            
                                                            F=ma                                   ---(iii)
                                                            Substitute (ii) and (iii) in (i) we get
                                                            W = F x s
                                                              = ma x __________
                                                              
                                                              = ____ m ( v - u )
                                                              
                                                            If u = 0
                                                            
                                                            W = ____ mv
                                                            
                                                            Work Done = Change in Kinetic Energy
                                                              ''',font=('courier',12), fill='black')
                        canvas_workenergy_page3.create_text(287,185, text='2', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_text(323,185, text='2', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_text(265,225, text='2', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_text(284,245, text='2a', font=('courier',12), fill='black')
                        canvas_workenergy_page3.create_text(295,225, text='2', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_text(270,230, text='v - u', font=('courier',12), fill='black')
                        canvas_workenergy_page3.create_text(335,320, text='v - u', font=('courier',12), fill='black')
                        canvas_workenergy_page3.create_text(322,315, text='2', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_text(360,315, text='2', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_text(340,337, text='2a', font=('courier',12), fill='black')
                        canvas_workenergy_page3.create_text(277,350, text='1', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_text(277,370, text='2', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_text(355,350, text='2', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_text(390,350, text='2', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_rectangle(200,400,340,450, outline='black', fill='cyan')
                        canvas_workenergy_page3.create_text(260,423, text='W = _____mv', font=('courier',12), fill='black')
                        canvas_workenergy_page3.create_text(325,420, text='2', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_text(277,420, text='1', font=('courier',10), fill='black')
                        canvas_workenergy_page3.create_text(277,440, text='2', font=('courier',10), fill='black')
                        
                        def KE():
                            import tkinter as tk

                            def show_entry_fields():
                                #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
                                ke=0.5*int(e1.get()) *int(e2.get())**2
                                tk.Label(master, text='Kinetic Energy=').grid(row=2,column=0)
                                tk.Label(master, text=(ke,'J')).grid(row=2, column=1)
                                
                            master = tk.Tk()
                            tk.Label(master, text="Mass").grid(row=0)
                            tk.Label(master, 
                                     text="Velocity").grid(row=1)
                    
                            e1 = tk.Entry(master)
                            e2 = tk.Entry(master)
                            
                            e1.grid(row=0, column=1)
                            e2.grid(row=1, column=1)
                            
                            tk.Button(master, 
                                      text='Quit', 
                                      command=master.quit).grid(row=3, 
                                                         column=0, 
                                                         sticky=tk.W, 
                                                         pady=4)
                            tk.Button(master, 
                                      text='Show', command=show_entry_fields).grid(row=3, 
                                                                            column=1, )
                        
                            tk.mainloop()  
                        
                        def Back_workenergy_page3():
                            phy_workenergy_page3.destroy()
            
                        Back_workenergy_page3=Button(phy_workenergy_page3, bg='coral2', text='<--', command=Back_workenergy_page3)
                        Back_workenergy_page3.pack()
                        Back_workenergy_page3.place(relx=.0,rely=.0)
                    
                        def workenergy_page4():
                            phy_workenergy_page4=Tk()
                            phy_workenergy_page4.title('Work and Energy')
                            canvas_workenergy_page4=Canvas(phy_workenergy_page4,width=1500, height=900, bg='white')
                            canvas_workenergy_page4.pack(expand=YES, fill=BOTH)
                            canvas_workenergy_page4.create_text(300,100,text='POTENTIAL ENERGY',font=('courier',40), fill='black')
                            canvas_workenergy_page4.create_text(300,400, text='''
                                                                Every object possesses some energy called Potential Energy. 
                                                                An object when gains energy may store it in itself as potential energy.
                                                                
                                                                
                                                                We know that when an object rises above the ground some work is done 
                                                                against gravity. Since work is done on the object, the object would gain
                                                                some energy. The energy that the object gains at a height is called Gravitational Potential Energy.
                                                                It is defined as the amount of work done required in raising an object 
                                                                above the ground up to a certain point against the gravity
                                                                
                                                                
                                                                
                                                                An object ‘A’ having mass ‘m’ is raised by height ‘h’ above the 
                                                                ground. Let us calculate the potential energy of object A at height ‘h’:
                                                                    
                                                                    We know that
                                                                            W = F x d = F x h (height)
                                                                            F = m x g (because the force is applied against gravity)
                                                                            Therefore, W = m x g x h
                                                                            Hence, Potential Energy of an object PE = mgh

''', font=('courier',12), fill='black')
                            canvas_workenergy_page4.create_rectangle(200,580, 380,630, outline='black', fill='cyan')
                            canvas_workenergy_page4.create_text(300,600, text='PE = mgh', font=('courier', 20), fill='black')
                            canvas_workenergy_page4.create_text(700,650, text='Gravitational potential energy does not get affected due to the path taken by the object to reach a certain height.', font=('courier',12), fill='black')
                            
                            def PE():
                                import tkinter as tk
                                
                                def show_entry_fields():
                                    #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
                                    pe=9.8*int(e1.get()) *int(e2.get())
                                    tk.Label(master, text='Potential Energy=').grid(row=2,column=0)
                                    tk.Label(master, text=(pe,'J')).grid(row=2, column=1)
                                    
                                master = tk.Tk()
                                tk.Label(master, text="Mass").grid(row=0)
                                tk.Label(master, 
                                         text="Height").grid(row=1)
                                
                                e1 = tk.Entry(master)
                                e2 = tk.Entry(master)
                                
                                e1.grid(row=0, column=1)
                                e2.grid(row=1, column=1)
                                
                                tk.Button(master, 
                                          text='Quit', 
                                          command=master.quit).grid(row=3, 
                                                             column=0, 
                                                             sticky=tk.W, 
                                                             pady=4)
                                tk.Button(master, 
                                          text='Show', command=show_entry_fields).grid(row=3, 
                                                                                column=1, 
                                                                                sticky=tk.W, 
                                                                                pady=4)
                                
                                tk.mainloop()
                            
                            def Back_workenergy_page4():
                                phy_workenergy_page4.destroy()
            
                            Back_workenergy_page4=Button(phy_workenergy_page4, bg='coral2', text='<--', command=Back_workenergy_page4)
                            Back_workenergy_page4.pack()
                            Back_workenergy_page4.place(relx=.0,rely=.0)
                            
                            def workenergy_page5():
                                phy_workenergy_page5=Tk()
                                phy_workenergy_page5.title('Work and Energy')
                                canvas_workenergy_page5=Canvas(phy_workenergy_page5,width=1500, height=900, bg='white')
                                canvas_workenergy_page5.pack(expand=YES, fill=BOTH)
                                
                                canvas_workenergy_page5.create_text(700,50, text='Law of Conservation of Energy', font=('courier',30), fill='black')
                                canvas_workenergy_page5.create_text(700,100, text='''Law: According to the law of conservation of energy, the total amount of energy before and after transformation remains the same.
                                                                    
Consider the following example where an object of mass ‘m’ is made to fall freely from a height ‘h’. ''', font=('courier',12), fill='black')
                                canvas_workenergy_page5.create_rectangle(100,200, 130, 400, outline='black', fill='brown')
                                canvas_workenergy_page5.create_line(160,200,160,400)
                                canvas_workenergy_page5.create_line(160,200,170,210)
                                canvas_workenergy_page5.create_line(160,200,150,210)
                                canvas_workenergy_page5.create_line(170,390,160,400)
                                canvas_workenergy_page5.create_line(150,390,160,400)
                                canvas_workenergy_page5.create_text(180,300,text='h', font=('courier',14), fill='black')
                                canvas_workenergy_page5.create_oval(120,160,160,200, fill='black')
                                canvas_workenergy_page5.create_text(160,150, text='A', font=('courier',14), fill='black')
                                canvas_workenergy_page5.create_text(300,440, text='''Object is at the top of a
building of a
height 'h' above the 
ground at postion A''', font=('courier',10), fill='black')
                                
                                canvas_workenergy_page5.create_rectangle(700,200,730,400, outline='black', fill='brown')
                                canvas_workenergy_page5.create_line(800,200,800,245)
                                canvas_workenergy_page5.create_line(800,255,800,400)
                                canvas_workenergy_page5.create_line(800,200,810,210)
                                canvas_workenergy_page5.create_line(800,200,790,210)
                                canvas_workenergy_page5.create_line(810,235,800,245)
                                canvas_workenergy_page5.create_line(790,235,800,245)
                                canvas_workenergy_page5.create_line(800,255,810,265)
                                canvas_workenergy_page5.create_line(800,255,790,265)
                                canvas_workenergy_page5.create_line(810,390,800,400)
                                canvas_workenergy_page5.create_line(790,390,800,400)
                                canvas_workenergy_page5.create_text(820,222,text='x', font=('courier',14), fill='black')
                                canvas_workenergy_page5.create_text(820,320,text='h-x', font=('courier',14), fill='black')
                                canvas_workenergy_page5.create_oval(740,230,780,270, fill='black')
                                canvas_workenergy_page5.create_text(780,220, text='B', font=('courier',14), fill='black')
                                canvas_workenergy_page5.create_text(1000,440, text='''Object is at position B which is
a distance x metre
from the top of the building                                                                    
''', font=('courier',10), fill='black')
                                canvas_workenergy_page5.create_rectangle(1200,200,1230,400, outline='black', fill='brown')
                                canvas_workenergy_page5.create_oval(1240,360,1280,400, fill='black')
                                canvas_workenergy_page5.create_text(1280,350, text='C', font=('courier',14), fill='black')
                                canvas_workenergy_page5.create_text(1200,440, text='''Object is at position C which is 
on the ground''', font=('courier',10), fill='black')
                                canvas_workenergy_page5.create_text(700,600, text=''' -> At point A,

PE= mgh           KE=0 (since v=0 at point A)
   Therefore, TE= PE + KE
                = mgh + 0
              TE = mgh          ---(1)
              
''', font=('courier', 12), fill='black')
                                
                                def Back_workenergy_page5():
                                    phy_workenergy_page5.destroy()
            
                                Back_workenergy_page5=Button(phy_workenergy_page5, bg='coral2', text='<--', command=Back_workenergy_page5)
                                Back_workenergy_page5.pack()
                                Back_workenergy_page5.place(relx=.0,rely=.0)
                                
                                def workenergy_page6():
                                    phy_workenergy_page6=Tk()
                                    phy_workenergy_page6.title('Work and Energy')
                                    canvas_workenergy_page6=Canvas(phy_workenergy_page6,width=1500, height=900, bg='white')
                                    canvas_workenergy_page6.pack(expand=YES, fill=BOTH)
                                    canvas_workenergy_page6.create_text(700,300, text='''-> At point B,
                                                                        
PE = mg( h - x )= mgh - mgx
KE = 1/2 mv
v  = u   + 2gx (Equations of Motion)
    = 2gx
Therfore, KE = 1/2 x m x 2gx
             = mgx
Therefore, TE = PE + KE = mgh -mgx + mgx
           TE = mgh          ---(2)
        
-> At point C,

PE = 0
KE = 1/2 mv^2
v^2 = u^2 +2gh
v^2 = 2gh
TE = PE + KE = 1/2 x m x 2gh
TE = mgh                    ---(3)

From (1),(2) and (3), Total Energy is conserved  
        ''', font=('courier', 12), fill = 'black')
                                    canvas_workenergy_page6.create_text(450, 160, text='2', font=('courier',10),fill='black')
                                    canvas_workenergy_page6.create_text(350, 180, text='2', font=('courier',10),fill='black')
                                    canvas_workenergy_page6.create_text(415, 180, text='2', font=('courier',10),fill='black')
                                    
                                    def Back_workenergy_page6():
                                        phy_workenergy_page6.destroy()
            
                                    Back_workenergy_page6=Button(phy_workenergy_page6, bg='coral2', text='<--', command=Back_workenergy_page6)
                                    Back_workenergy_page6.pack()
                                    Back_workenergy_page6.place(relx=.0,rely=.0)
                                    
                                    def workenergy_page7():
                                        phy_workenergy_page7=Tk()
                                        phy_workenergy_page7.title('Work and Energy')
                                        canvas_workenergy_page7=Canvas(phy_workenergy_page7,width=1500, height=900, bg='white')
                                        canvas_workenergy_page7.pack(expand=YES, fill=BOTH)
                                        canvas_workenergy_page7.create_rectangle(300,10,1200,300, outline='black', fill='yellow')
                                        canvas_workenergy_page7.create_rectangle(100,330,1350,700, outline='black', fill='orange')
                                        canvas_workenergy_page7.create_text(700,50, text='POWER', font=('courier',30), fill='black')
                                        canvas_workenergy_page7.create_text(700,100,text='Power – The rate of doing work is defined as Power.',font=('courier',12), fill='black')
                                        canvas_workenergy_page7.create_text(700,200,text='''Power = Work Done / Time
P = W/ t
SI Unit: W (Watt) or J/s
1 kilowatt = 1000 watts
1 kW = 1000 W
1 W = 1000 J s-1
Average Power = Total Energy Consumed / Total Time taken
''',font=('courier',12), fill='black')
                                        canvas_workenergy_page7.create_text(700,350, text='Commercial Unit of Power', font=('courier',20), fill='black')
                                        canvas_workenergy_page7.create_text(700,500, text='''We cannot use Joule to measure power commercially. Instead, we use kilowatt-hour (kWh).
Commercial unit of energy = 1 kilowatt hour (kwh)

∴ 1 kWh = 1 kilowatt × 1 hour
= 1000 watt × 3600 seconds
= 3600000 Joule (watt × second)
1 kWh = 3.6 × 106 J.
∴ 1 kWh = 1 unit

The energy used in one hour at the rate of 1 kW is called 1 kWh.
''', font=('courier',12), fill='black')
                                        
                                        def P():
                                            import tkinter as tk
                                            
                                            def show_entry_fields():
                                                #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
                                                P=int(e1.get())/int(e2.get())
                                                tk.Label(master, text='Power=').grid(row=2,column=0)
                                                tk.Label(master, text=(P,'W')).grid(row=2, column=1)
                                                
                                            master = tk.Tk()
                                            tk.Label(master, text="Energy(J)").grid(row=0)
                                            tk.Label(master, 
                                                     text="time(s)").grid(row=1)
                    
                                            e1 = tk.Entry(master)
                                            e2 = tk.Entry(master)
                                            
                                            e1.grid(row=0, column=1)
                                            e2.grid(row=1, column=1)
                                            
                                            tk.Button(master, 
                                                      text='Quit', 
                                                      command=master.quit).grid(row=3, 
                                                                         column=0, 
                                                                         sticky=tk.W, 
                                                                         pady=4)
                                            tk.Button(master, 
                                                      text='Show', command=show_entry_fields).grid(row=3, 
                                                                                            column=1, 
                                                                                            sticky=tk.W, 
                                                                                            pady=4)
                                            
                                            tk.mainloop()
                                            
                                        def com():
                                            import tkinter as tk
                                            
                                            def show_entry_fields():
                                                
                                                comm=int(e1.get())*3.6*10**6
                                                tk.Label(master, text='Energy in J=').grid(row=2,column=0)
                                                tk.Label(master, text=(comm,'J')).grid(row=2, column=1)
                                                
                                            master = tk.Tk()
                                            tk.Label(master, text="Energy in kWh:").grid(row=0)
                    
                                            e1 = tk.Entry(master)
                                            
                                            e1.grid(row=0, column=1)

                                            tk.Button(master, 
                                                      text='Quit', 
                                                      command=master.quit).grid(row=3, 
                                                                         column=0, 
                                                                         sticky=tk.W, 
                                                                         pady=4)
                                            tk.Button(master, 
                                                      text='Show', command=show_entry_fields).grid(row=3, 
                                                                                            column=1, 
                                                                                            sticky=tk.W, 
                                                                                            pady=4)
                                            
                                            tk.mainloop()
                                            
                                        p=Button(phy_workenergy_page7, bg='coral2', text='FIND POWER', command=P)
                                        p.pack()
                                        p.place(relx=.75, rely=.25)
                                        c=Button(phy_workenergy_page7, bg='coral2', text='CONVERT COMMERCIAL UNIT OF ENERGY TO SI UNIT', command=com)
                                        c.pack()
                                        c.place(relx=.75, rely=.75)
                                        
                                        def Back_workenergy_page7():
                                            phy_workenergy_page7.destroy()
                                        
                                        def Back_to_class9():
                                            phy_WorkEnergy.destroy()
                                            phy_workenergy_page1.destroy()
                                            phy_workenergy_page2.destroy()
                                            phy_workenergy_page3.destroy()
                                            phy_workenergy_page4.destroy()
                                            phy_workenergy_page5.destroy()
                                            phy_workenergy_page6.destroy()
                                            phy_workenergy_page7.destroy()
                                        
                                        Back_to_class9=Button(phy_workenergy_page7,bg='coral2', text='Class 9',font=('Castellar',18), command=Back_to_class9)
                                        Back_to_class9.pack()
                                        Back_to_class9.place(relx=.87,rely=.85)
            
                                        Back_workenergy_page7=Button(phy_workenergy_page7, bg='coral2', text='<--', command=Back_workenergy_page7)
                                        Back_workenergy_page7.pack()
                                        Back_workenergy_page7.place(relx=.0,rely=.0)
                                        
                                    WorkEnergy_page7=Button(phy_workenergy_page6, bg='coral2', text='-->', command=workenergy_page7)
                                    WorkEnergy_page7.pack()
                                    WorkEnergy_page7.place(relx=.98, rely=.0)
                                
                                WorkEnergy_page6=Button(phy_workenergy_page5, bg='coral2', text='-->', command=workenergy_page6)
                                WorkEnergy_page6.pack()
                                WorkEnergy_page6.place(relx=.98, rely=.0)
                                
                            p=Button(phy_workenergy_page4, bg='coral2', text='FIND POTENTIAL ENERGY', command=PE )
                            p.pack()
                            p.place(relx=.75, rely=.75)
                            
                            WorkEnergy_page5=Button(phy_workenergy_page4, bg='coral2', text='-->', command=workenergy_page5)
                            WorkEnergy_page5.pack()
                            WorkEnergy_page5.place(relx=.98, rely=.0)
                        
                        k=Button(phy_workenergy_page3, bg='coral2', text='FIND KINETIC ENERGY', command=KE )
                        k.pack()
                        k.place(relx=.75, rely=.75)
                        
                        WorkEnergy_page4=Button(phy_workenergy_page3, bg='coral2', text='-->', command=workenergy_page4 )
                        WorkEnergy_page4.pack()
                        WorkEnergy_page4.place(relx=.98, rely=.0)
                    
                    WorkEnergy_page3=Button(phy_workenergy_page2, bg='coral2', text='-->', command=workenergy_page3)
                    WorkEnergy_page3.pack()
                    WorkEnergy_page3.place(relx=.98, rely=.0)
                
                w=Button(phy_workenergy_page1, bg='coral2', text='FIND WORK DONE', command=W)
                w.pack()
                w.place(relx=.75, rely=.75)
                
                workenergy_page2=Button(phy_workenergy_page1, bg='coral2', text='-->', command=WorkEnergy_page2 )
                workenergy_page2.pack()
                workenergy_page2.place(relx=.98, rely=.0)
                
            Workenergy_page1=Button(phy_WorkEnergy, bg='coral2', text='-->', command=workenergy_page1)            
            Workenergy_page1.pack()
            Workenergy_page1.place(relx=.98,rely=.0)
            
            def Back_WorkEnergy():
                phy_WorkEnergy.destroy()
            
            Back_WorkEnergy=Button(phy_WorkEnergy, bg='coral2', text='<--', command=Back_WorkEnergy)
            Back_WorkEnergy.pack()
            Back_WorkEnergy.place(relx=.0,rely=.0)
                        
        def Sound9():
            phy_Sound9=Tk()
            phy_Sound9.title('Sound')
            canvas_Sound9=Canvas(phy_Sound9, width=1500, height=900, bg='white')
            canvas_Sound9.pack(expand=YES,fill=BOTH)
            
            canvas_Sound9.create_text(750,70,text='SOUND', font=('Times New Roman',27), fill = 'black')
            canvas_Sound9.create_text(550,330,text='''
                                      •  Sound energy is a form of energy because of which our ears are able to hear something.
                                      
                                      •  One cannot create sound or destroy it. But one can transform one form of energy into sound energy. For instance, 
                                         when a cell phone rings, the sound is produced by converting electrical energy into sound energy.
                                      
                                      •  A sound is produced when an object vibrates, that is they move in a ‘to-and-fro’ motion.
                                      
                                         For instance,
                                         •  When we strike a tuning fork or a stretched rubber band, it vibrates and produces sound.
                                         
                                         •  The human voice is produced because of the vibration of the vocal cords.
                                         
                                         •  String instruments produce sound as their strings vibrate.
                                         
                                         •  When a bird flaps its wings a sound is produced.
                                         
                                         •  A flute produces sound because the air column of the flute vibrates as air passes through it.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                
            def Back_Sound9():
                phy_Sound9.destroy()
            
            Back_Sound9=Button(phy_Sound9, bg='coral2', text='<--', command=Back_Sound9)
            Back_Sound9.pack()
            Back_Sound9.place(relx=.0,rely=.0)
            
            def page2_Sound9():
                phy_page2_Sound9=Tk()
                phy_page2_Sound9.title('Sound')
                canvas_page2_Sound9=Canvas(phy_page2_Sound9, width=1500, height=900, bg='white')
                canvas_page2_Sound9.pack(expand=YES,fill=BOTH)
                
                canvas_page2_Sound9.create_text(270,100,text='How does sound travel?', font=('Yu Gothic UI Semibold',24), fill = 'black')
                canvas_page2_Sound9.create_text(550,330,text='''
                                                •  In order to propagate, sound requires a medium through which it can travel. This medium could be a gas,
                                                   liquid or solid.
                                                
                                                •  Sound propagates in a medium as the particles of the medium vibrate from a starting point. This means that 
                                                   sound always has a starting point and an ending point.
                                                
                                                •  For instance, while you talk to a friend, as you speak, the particles in the air get displaced due to the 
                                                   pressure caused by the sound you produce. They then displace the adjacent particles and so on. In this way, 
                                                   sound travels from your place to your friend’s ears.
                                                   
                                                •  Therefore, we can say that the particles of a medium do not travel from one point one another in order to 
                                                   propagate sound. Sound propagates because of the disturbance caused by a source of sound in the medium.
                                                   
                                                •  A wave is a disturbance produced in a medium as the particles of the medium vibrate. The particles produce 
                                                   motion in each other without moving forward or backwards. This leads to the propagation of sound. Hence sound
                                                   is often called a Wave.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                
                def Back_page2_Sound9():
                    phy_page2_Sound9.destroy()
            
                Back_page2_Sound9=Button(phy_page2_Sound9, bg='coral2', text='<--', command=Back_page2_Sound9)
                Back_page2_Sound9.pack()
                Back_page2_Sound9.place(relx=.0,rely=.0)
                
                def page3_Sound9():
                    phy_page3_Sound9=Tk()
                    phy_page3_Sound9.title('Sound')
                    canvas_page3_Sound9=Canvas(phy_page3_Sound9, width=1500, height=900, bg='white')
                    canvas_page3_Sound9.pack(expand=YES,fill=BOTH)
                    
                    canvas_page3_Sound9.create_text(330,120,text='How can sound travel through air?', font=('Yu Gothic UI Semibold',24), fill = 'black')
                    canvas_page3_Sound9.create_text(550,330,text='''
                                                    •  When an object vibrates in the air or produces a sound, some regions of high pressure are created in front 
                                                       of it. These are called the Regions of Compression. These regions of compression move forward in the medium as 
                                                       particles exert pressure on their adjacent particles.
                                                    
                                                    •  With alternate regions of compression, there are also regions of low pressure that are in its front. Thes are 
                                                       called Regions of Rarefaction.
                                                    
                                                    •  As the object would move forwards and backwards consecutively producing sound, the series of compressions and 
                                                       rarefactions will be created. This will allow sound to move through air or any other medium as well.
                                                    
                                                    •  If the medium is dense the pressure exerted on the particles will be more in order to propagate the sound and 
                                                       vice versa.
                                                    
                                                    •  Therefore, we can also say that propagation of sound is all about change in the pressure of the medium.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                       
                    def Back_page3_Sound9():
                        phy_page3_Sound9.destroy()
            
                    Back_page3_Sound9=Button(phy_page3_Sound9, bg='coral2', text='<--', command=Back_page3_Sound9)
                    Back_page3_Sound9.pack()
                    Back_page3_Sound9.place(relx=.0,rely=.0)
                    
                    def page4_Sound9():
                        global phy_page4_Sound9
                        phy_page4_Sound9=Toplevel()
                        phy_page4_Sound9.title('Sound')
                        canvas_page4_Sound9=Canvas(phy_page4_Sound9, width=1500, height=900, bg='white')
                        canvas_page4_Sound9.pack(expand=YES,fill=BOTH)
                        
                        canvas_page4_Sound9.create_text(750,600,text='''Sound wave causing compression (C) and refraction (R)''', font=('Adobe Fangsong Std R',14), fill = 'black')
                        global soundwave
                        soundwave = tkinter.PhotoImage(file="soundwave.png")
                        button = Button(phy_page4_Sound9, image = soundwave ,width=604,height=295,font=("Courier",20,"bold"),bg='#94ffe2') 
                        button.configure(image = soundwave)
                        button.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            
                        def Back_page4_Sound9():
                            phy_page4_Sound9.destroy()
            
                        Back_page4_Sound9=Button(phy_page4_Sound9, bg='coral2', text='<--', command=Back_page4_Sound9)
                        Back_page4_Sound9.pack()
                        Back_page4_Sound9.place(relx=.0,rely=.0)
                        
                        def page5_Sound9():
                            global phy_page5_Sound9
                            phy_page5_Sound9=Toplevel()
                            phy_page5_Sound9.title('Sound')
                            canvas_page5_Sound9=Canvas(phy_page5_Sound9, width=1500, height=900, bg='white')
                            canvas_page5_Sound9.pack(expand=YES,fill=BOTH)
                            
                            canvas_page5_Sound9.create_text(290,130,text='What are mechanical waves?', font=('Yu Gothic UI Semibold',24), fill = 'black')
                            canvas_page5_Sound9.create_text(560,230,text='''
                                                            A wave that is produced when objects of the medium oscillate is called Mechanical Wave. The sound waves are therefore,
                                                            mechanical waves.
                                                            
                                                            •  Sound cannot travel through the vacuum as it always needs a medium to propagate. The vacuum contains no air hence no 
                                                               particles can propagate sound.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                            
                            global waves
                            waves = tkinter.PhotoImage(file="waves.png")
                            button = Button(phy_page5_Sound9, image = waves ,width=786,height=322,font=("Courier",20,"bold"),bg='#94ffe2') 
                            button.configure(image = waves)
                            button.place(relx = 0.5, rely = 0.65, anchor = CENTER)
            
                            def Back_page5_Sound9():
                                phy_page5_Sound9.destroy()
            
                            Back_page5_Sound9=Button(phy_page5_Sound9, bg='coral2', text='<--', command=Back_page5_Sound9)
                            Back_page5_Sound9.pack()
                            Back_page5_Sound9.place(relx=.0,rely=.0)
                            
                            def page6_Sound9():
                                global phy_page6_Sound9
                                phy_page6_Sound9=Toplevel()
                                phy_page6_Sound9.title('Sound')
                                canvas_page6_Sound9=Canvas(phy_page6_Sound9, width=1500, height=900, bg='white')
                                canvas_page6_Sound9.pack(expand=YES,fill=BOTH)
                                
                                canvas_page6_Sound9.create_text(220,90,text='Longitudinal waves:', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                canvas_page6_Sound9.create_text(530,150,text='''
                                                                Any wave that vibrates in the direction of the motion is called a Longitudinal Wave. Sound waves are longitudinal because the
                                                                particles of the medium vibrate in the direction which is parallel to the direction of the propagation of the sound waves.The 
                                                                particles in the medium oscillate to and fro in the case of longitudinal waves.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                canvas_page6_Sound9.create_text(220,280,text='Transverse Waves:', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                canvas_page6_Sound9.create_text(550,340,text='''
                                                                A transverse wave is produced when the particles of the medium oscillate in a direction which is perpendicular to the direction
                                                                of the propagation of the wave. The particles in a transverse wave oscillate in an up and down motion. For Example, light waves 
                                                                are transverse in nature.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                
                                global longitudewave
                                longitudewave = tkinter.PhotoImage(file="longitudewave.png")
                                button = Button(phy_page6_Sound9, image = longitudewave ,width=700,height=297,font=("Courier",20,"bold"),bg='#94ffe2') 
                                button.configure(image = longitudewave)
                                button.place(relx = 0.5, rely = 0.7, anchor = CENTER)
                            
                                def Back_page6_Sound9():
                                    phy_page6_Sound9.destroy()
            
                                Back_page6_Sound9=Button(phy_page6_Sound9, bg='coral2', text='<--', command=Back_page6_Sound9)
                                Back_page6_Sound9.pack()
                                Back_page6_Sound9.place(relx=.0,rely=.0)
                                
                                def page7_Sound9():
                                    global phy_page7_Sound9
                                    phy_page7_Sound9=Toplevel()
                                    phy_page7_Sound9.title('Sound')
                                    canvas_page7_Sound9=Canvas(phy_page7_Sound9, width=1500, height=900, bg='white')
                                    canvas_page7_Sound9.pack(expand=YES,fill=BOTH)
                                    
                                    canvas_page7_Sound9.create_text(170,80,text='''
                                                                    •  A sound wave is characterized by three factors:
                                                                        o  Amplitude
                                                                        o  Frequency
                                                                        o  Speed''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                    
                                    global soundwaves
                                    soundwaves = tkinter.PhotoImage(file="soundwaves.png")
                                    button = Button(phy_page7_Sound9, image = soundwaves ,width=811,height=511,font=("Courier",20,"bold"),bg='#94ffe2') 
                                    button.configure(image = soundwaves)
                                    button.place(relx = 0.5, rely = 0.55, anchor = CENTER)
                                    
                                    def Back_page7_Sound9():
                                        phy_page7_Sound9.destroy()
            
                                    Back_page7_Sound9=Button(phy_page7_Sound9, bg='coral2', text='<--', command=Back_page7_Sound9)
                                    Back_page7_Sound9.pack()
                                    Back_page7_Sound9.place(relx=.0,rely=.0)
                                    
                                    def page8_Sound9():
                                        phy_page8_Sound9=Tk()
                                        phy_page8_Sound9.title('Sound')
                                        canvas_page8_Sound9=Canvas(phy_page8_Sound9, width=1500, height=900, bg='white')
                                        canvas_page8_Sound9.pack(expand=YES,fill=BOTH)
                                        
                                        canvas_page8_Sound9.create_text(700,60,text='Characteristics of Sound', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                        canvas_page8_Sound9.create_text(530,420,text='''
                                                                        Compression (C):
                                                                            The compression region is represented by the upper part of the wave curve.
                                                                            It is a region where particles cluster together.
                                                                            The density, as well as pressure, is always high in this region. 
                                                                        
                                                                        Refraction (R):
                                                                            A refraction is represented by the lower part of the wave curve.
                                                                            It is a region where the particles separate out.
                                                                            Refraction region always has lower pressure.
                                                                        
                                                                        Time Period (T):
                                                                                The time taken between two consecutive compressions or refractions to cross a fixed point is called Time Period of the Wave.
                                                                                In other words, the time taken for one complete oscillation through a medium is called a Time Period.
                                                                                SI unit: second (s)
                                                                        
                                                                        Frequency (f):
                                                                            The number of oscillations per unit time is called the Frequency of a Wave (Number of compressions + the number of 
                                                                            refractions per unit time).
                                                                            SI unit: Hertz (Hz)
                                                                            
                                                                        The relationship between frequency and time period:
                                                                                f = 1/T''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                        
                                        def Back_page8_Sound9():
                                            phy_page8_Sound9.destroy()
            
                                        Back_page8_Sound9=Button(phy_page8_Sound9, bg='coral2', text='<--', command=Back_page8_Sound9)
                                        Back_page8_Sound9.pack()
                                        Back_page8_Sound9.place(relx=.0,rely=.0)
                                        
                                        def page9_Sound9():
                                            phy_page9_Sound9=Tk()
                                            phy_page9_Sound9.title('Sound')
                                            canvas_page9_Sound9=Canvas(phy_page9_Sound9, width=1500, height=900, bg='white')
                                            canvas_page9_Sound9.pack(expand=YES,fill=BOTH)
                                            
                                            canvas_page9_Sound9.create_text(480,370,text='''
                                                                            Crest:
                                                                                It is the peak of the curve.
                                                                        
                                                                            Trough:
                                                                                It is the crust of the curve.
                                                                                
                                                                            Wavelength (λ):
                                                                                The distance between two consecutive compressions or refractions is called Wavelength.
                                                                                SI unit: metre (m)
                                                                            
                                                                            The Speed of sound (v):
                                                                                The distance by which a compression or refraction of a wave travels per unit time is called as Sound’s Speed.
                                                                                SI unit: metres/seconds
                                                                                v = wavelength / time = λ/T = λ*F 
                                                                                Speed of Sound in air = 333 m/s
                                                                                        
                                                                            Loudness:
                                                                                It is how our ears respond to a sound.
                                                                                Two sounds with same intensity can vary in loudness only because we can detect one sound easier than the other.
                                                                            
                                                                            Intensity:
                                                                                The amount of sound energy that passes through a unit area per second is called its intensity''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                
                                            
                                            def Back_page9_Sound9():
                                                phy_page9_Sound9.destroy()
            
                                            Back_page9_Sound9=Button(phy_page9_Sound9, bg='coral2', text='<--', command=Back_page9_Sound9)
                                            Back_page9_Sound9.pack()
                                            Back_page9_Sound9.place(relx=.0,rely=.0)
                                            
                                            def page10_Sound9():
                                                global phy_page10_Sound9
                                                phy_page10_Sound9=Toplevel()
                                                phy_page10_Sound9.title('Sound')
                                                canvas_page10_Sound9=Canvas(phy_page10_Sound9, width=1500, height=900, bg='white')
                                                canvas_page10_Sound9.pack(expand=YES,fill=BOTH)
                                                
                                                canvas_page10_Sound9.create_text(440,280,text='''
                                                                                 Pitch:
                                                                                     Pitch of a sound depends upon:
                                                                                        1. the frequency of the sound
                                                                                        2. size of the object producing the sound
                                                                                        3. type of the object producing the sound
                                                                                        \n
                                                                                        
                                                                                 Amplitude:
                                                                                     The value of the maximum or minimum disturbance caused in the medium is called the Amplitude of the Sound.
                                                                                     Amplitude defines if the sound is loud or soft.
                                                                                     \n''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                
                                                global pitch
                                                pitch = tkinter.PhotoImage(file="pitch.png")
                                                button = Button(phy_page10_Sound9, image = pitch ,width=369,height=268,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                button.configure(image = pitch)
                                                button.place(relx = 0.55, rely = 0.2, anchor = CENTER)
                                                
                                                global amplitude
                                                amplitude = tkinter.PhotoImage(file="amplitude.png")
                                                button = Button(phy_page10_Sound9, image = amplitude ,width=482,height=211,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                button.configure(image = amplitude)
                                                button.place(relx = 0.25, rely = 0.7, anchor = CENTER)
                                        
                                                def Back_page10_Sound9():
                                                    phy_page10_Sound9.destroy()
            
                                                Back_page10_Sound9=Button(phy_page10_Sound9, bg='coral2', text='<--', command=Back_page10_Sound9)
                                                Back_page10_Sound9.pack()
                                                Back_page10_Sound9.place(relx=.0,rely=.0)
                                                
                                                def page11_Sound9():
                                                    global phy_page11_Sound9
                                                    phy_page11_Sound9=Toplevel()
                                                    phy_page11_Sound9.title('Sound')
                                                    canvas_page11_Sound9=Canvas(phy_page11_Sound9, width=1500, height=900, bg='white')
                                                    canvas_page11_Sound9.pack(expand=YES,fill=BOTH)
                                                    
                                                    canvas_page11_Sound9.create_text(470,280,text='''
                                                                                     Timber:
                                                                                         The timbre or quality of sound is a characteristic with which we can differentiate between different sounds even if they have
                                                                                         same pitch and amplitude.
                                                                                    
                                                                                     Tone:
                                                                                         The sound which has single frequency throughout is called a Tone.
                                                                                         
                                                                                     Note:
                                                                                         A sound with more than one frequency is called a Note. It is pleasant to listen
                                                                                    
                                                                                     Music:
                                                                                         It is a sound which is pleasant and has rich quality.
                                                                                     
                                                                                     Noise:
                                                                                         It is an unpleasant sound.
                                                                                         \n''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                    
                                                    global noise
                                                    noise = tkinter.PhotoImage(file="noise.png")
                                                    button = Button(phy_page11_Sound9, image = noise ,width=326,height=206,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                    button.configure(image = noise)
                                                    button.place(relx = 0.2, rely = 0.75, anchor = CENTER)
                                                    
                                                    def Back_page11_Sound9():
                                                        phy_page11_Sound9.destroy()
                                                        
                                                    Back_page11_Sound9=Button(phy_page11_Sound9, bg='coral2', text='<--', command=Back_page11_Sound9)
                                                    Back_page11_Sound9.pack()
                                                    Back_page11_Sound9.place(relx=.0,rely=.0)
                                                    
                                                    def page12_Sound9():
                                                        global phy_page12_Sound9
                                                        phy_page12_Sound9=Toplevel()
                                                        phy_page12_Sound9.title('Sound')
                                                        canvas_page12_Sound9=Canvas(phy_page12_Sound9, width=1500, height=900, bg='white')
                                                        canvas_page12_Sound9.pack(expand=YES,fill=BOTH)
                                                        
                                                        global speedofsound
                                                        speedofsound = tkinter.PhotoImage(file="speedofsound.png")
                                                        button = Button(phy_page12_Sound9, image = speedofsound ,width=554,height=300,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                        button.configure(image = speedofsound)
                                                        button.place(relx = 0.5, rely = 0.2, anchor = CENTER)
                                                        
                                                        canvas_page12_Sound9.create_text(430,420,text='''
                                                                                         •  Sound cannot travel at the same speed in different mediums. The speed of sound in a medium is affected by three things:
                                                                                             o  The density of the medium. For instance, speed of sound is the maximum through solids 
                                                                                             o  The temperature of the medium. As the temperature increases, the sound propagates easily.
                                                                                             o  Humidity in the air also affects the travel of sound. As the humidity increases, so does the propagation of sound.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                        
                                                        canvas_page12_Sound9.create_text(240,550,text='What is a sonic boom?', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                        canvas_page12_Sound9.create_text(410,660,text='''
                                                                                         When an object travels in the air with a speed greater than that of the sound, it produces a sound with high energy.
                                                                                         This energy is loud enough that it can break glasses or damage the buildings. The sound produced is similar to the 
                                                                                         sound of an explosion or thunderclap.
                                                                                         
                                                                                         These objects exert a large amount of pressure on the air which causes the production of shock waves in the air. 
                                                                                         These shock waves produce extremely large and loud sound waves which are called Sonic booms.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                        
                                                        def Back_page12_Sound9():
                                                            phy_page12_Sound9.destroy()
            
                                                        Back_page12_Sound9=Button(phy_page12_Sound9, bg='coral2', text='<--', command=Back_page12_Sound9)
                                                        Back_page12_Sound9.pack()
                                                        Back_page12_Sound9.place(relx=.0,rely=.0)
                                                        
                                                        def page13_Sound9():
                                                            global phy_page13_Sound9
                                                            phy_page13_Sound9=Toplevel()
                                                            phy_page13_Sound9.title('Sound')
                                                            canvas_page13_Sound9=Canvas(phy_page13_Sound9, width=1500, height=900, bg='white')
                                                            canvas_page13_Sound9.pack(expand=YES,fill=BOTH)
                                                            
                                                            global sonicboom
                                                            sonicboom = tkinter.PhotoImage(file="sonicboom.png")
                                                            button = Button(phy_page13_Sound9, image = sonicboom ,width=450,height=229,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                            button.configure(image = sonicboom)
                                                            button.place(relx = 0.5, rely = 0.25, anchor = CENTER)
                                                            
                                                            canvas_page13_Sound9.create_text(430,530,text='''
                                                                                             •  Speed of light in air = 3 * 108 m/s
                                                                                         
                                                                                             •  Speed of sound in air = 333 m/s
                                                                                         
                                                                                             This clearly states that sound travels a lower speed than that of light in air. This is a reason why at the time of
                                                                                             lightening, the light is visible instantly while the sound of the thunder reaches our ears after a few seconds.
                                                                                         
                                                                                             •  Sound can bounce off a solid or a liquid. Some materials like metals and walls are called Good Reflectors of Sound
                                                                                                as they do not absorb the sound while others like clothes and sponge are called Bad Reflectors of Sound as they absorb 
                                                                                                the sound easily.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                        
                                                            def Back_page13_Sound9():
                                                                phy_page13_Sound9.destroy()
            
                                                            Back_page13_Sound9=Button(phy_page13_Sound9, bg='coral2', text='<--', command=Back_page13_Sound9)
                                                            Back_page13_Sound9.pack()
                                                            Back_page13_Sound9.place(relx=.0,rely=.0)
                                                            
                                                            def page14_Sound9():
                                                                phy_page14_Sound9=Tk()
                                                                phy_page14_Sound9.title('Sound')
                                                                canvas_page14_Sound9=Canvas(phy_page14_Sound9, width=1500, height=900, bg='white')
                                                                canvas_page14_Sound9.pack(expand=YES,fill=BOTH)
                                                                
                                                                canvas_page14_Sound9.create_text(750,40, text='Laws of Reflection of Sound', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                canvas_page14_Sound9.create_line(500,350,1000,350)
                    
                                                                canvas_page14_Sound9.create_line(500,200,750,350)
                                                                canvas_page14_Sound9.create_line(1000,200,750,350)
                                                                                    
                                                                for i in range(180,350,15):
                                                                    canvas_page14_Sound9.create_line(750,i,750,i+10)
                    
                    
                                                                canvas_page14_Sound9.create_text(180,600, text='''
                                                                                                     The laws of reflection of sound are;
                                                                                                
                                                                                                (i)The incident sound wave, the reflected sound wave
                                                                                                   and the normal, all lie in the same plane.
                                                    
                                                                                                (ii)The angle of incident of incident sound wave
                                                                                                    is equal to the angle of reflection formed by
                                                                                                    the reflected sound wave, that is, i = r''', font=('courier',16), fill='black')
                    
                                                                canvas_page14_Sound9.create_arc(715,310,760,340, style=ARC, start=60, extent=140)
                                                                canvas_page14_Sound9.create_arc(785,310,740,340, style=ARC,start=340, extent=140)
                                                                        
                                                                canvas_page14_Sound9.create_text(750,330, text='i  r', font=('courier',14), fill = 'black')
                                                                canvas_page14_Sound9.create_text(750,160, text='normal', font=('courier',14), fill = 'black')
                                                                canvas_page14_Sound9.create_text(750,370, text='reflecting surface', font=('courier',14), fill = 'black')
                                                                canvas_page14_Sound9.create_text(420,220, text='incident sound wave', font=('courier',14), fill = 'black')
                                                                canvas_page14_Sound9.create_text(1080,220, text='reflected sound wave', font=('courier',14), fill = 'black')
                                                                
                                                                canvas_page14_Sound9.create_polygon(560,220,570,243,540,240, fill = 'black')
                                                                canvas_page14_Sound9.create_polygon(943,235,930,257,910,240, fill = 'black')
                                                                
                                                                def Back_page14_Sound9():
                                                                    phy_page14_Sound9.destroy()
            
                                                                Back_page14_Sound9=Button(phy_page14_Sound9, bg='coral2', text='<--', command=Back_page14_Sound9)
                                                                Back_page14_Sound9.pack()
                                                                Back_page14_Sound9.place(relx=.0,rely=.0)
                                                                
                                                                def page15_Sound9():
                                                                    global phy_page15_Sound9
                                                                    phy_page15_Sound9=Toplevel()
                                                                    phy_page15_Sound9.title('Sound')
                                                                    canvas_page15_Sound9=Canvas(phy_page15_Sound9, width=1500, height=900, bg='white')
                                                                    canvas_page15_Sound9.pack(expand=YES,fill=BOTH)
                                                                    
                                                                    canvas_page15_Sound9.create_text(150,100,text='Echo', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                    canvas_page15_Sound9.create_text(390,190,text='''
                                                                                                     When we hear the same sound again and again in a medium it is called Echo. The sound or echo persists in our brain
                                                                                                     for 0.1 seconds. This means that the difference between sound and its echo should be at least 0.1 seconds. It is 
                                                                                                     produced as a result of reflection of sound through a medium. If sound reflects more than once we may hear multiple 
                                                                                                     echoes.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                                    
                                                                    global echo
                                                                    echo = tkinter.PhotoImage(file="echo.png")
                                                                    button = Button(phy_page15_Sound9, image = echo ,width=473,height=332,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                    button.configure(image = echo)
                                                                    button.place(relx = 0.5, rely = 0.65, anchor = CENTER)
                                                                    
                                                                    def Back_page15_Sound9():
                                                                        phy_page15_Sound9.destroy()
                                                                    
                                                                    Back_page15_Sound9=Button(phy_page15_Sound9, bg='coral2', text='<--', command=Back_page15_Sound9)
                                                                    Back_page15_Sound9.pack()
                                                                    Back_page15_Sound9.place(relx=.0,rely=.0)
                                                                    
                                                                    def page16_Sound9():
                                                                        global phy_page16_Sound9
                                                                        phy_page16_Sound9=Toplevel()
                                                                        phy_page16_Sound9.title('Sound')
                                                                        canvas_page16_Sound9=Canvas(phy_page16_Sound9, width=1500, height=900, bg='white')
                                                                        canvas_page16_Sound9.pack(expand=YES,fill=BOTH)
                                                                        
                                                                        canvas_page16_Sound9.create_text(200,110,text='Reverberation', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                        canvas_page16_Sound9.create_text(390,200,text='''
                                                                                                         It is the persistence of a sound after a sound is produced. A reverberation is created when a sound signal is reflected 
                                                                                                         multiple of times until it reaches a sound wave that cannot be heard by human ears. Auditoriums and big halls often have 
                                                                                                         to deal with reverberation. That is why the roofs are made up of soundproof materials like Flipboard and the chairs in 
                                                                                                         the halls are also made up of fabrics that can absorb sound.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                                        
                                                                        global Reverberation
                                                                        Reverberation = tkinter.PhotoImage(file="Reverberation.png")
                                                                        button = Button(phy_page16_Sound9, image = Reverberation ,width=593,height=236,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                        button.configure(image = Reverberation)
                                                                        button.place(relx = 0.5, rely = 0.65, anchor = CENTER)
                                                                        
                                                                        def Back_page16_Sound9():
                                                                            phy_page16_Sound9.destroy()
                                                                    
                                                                        Back_page16_Sound9=Button(phy_page16_Sound9, bg='coral2', text='<--', command=Back_page16_Sound9)
                                                                        Back_page16_Sound9.pack()
                                                                        Back_page16_Sound9.place(relx=.0,rely=.0)
                                                                        
                                                                        def page17_Sound9():
                                                                            global phy_page17_Sound9
                                                                            phy_page17_Sound9=Toplevel()
                                                                            phy_page17_Sound9.title('Sound')
                                                                            canvas_page17_Sound9=Canvas(phy_page17_Sound9, width=1500, height=900, bg='white')
                                                                            canvas_page17_Sound9.pack(expand=YES,fill=BOTH)
                                                                            
                                                                            canvas_page17_Sound9.create_text(390,90,text='Advantages of Multiple Reflection of Sound', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                            canvas_page17_Sound9.create_text(400,230,text='''
                                                                                                             •  Horns, trumpets, loudhailers or megaphones are designed in such a way that sound can travel in a particular direction only 
                                                                                                                without spreading out everywhere. This makes it easier for the audience to listen to the speaker. All these instruments work 
                                                                                                                on the phenomena of multiple reflections of sound.
                                                                                                             
                                                                                                             •  The multiple reflections in a stethoscope tube make it possible for the doctors to listen to a patient’s heartbeat.
                                                                                                             
                                                                                                             •  Concert halls are generally covered so that sound can reflect through it and reach the wider audience.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                                            
                                                                            global multiplereflections
                                                                            multiplereflections = tkinter.PhotoImage(file="multiplereflections.png")
                                                                            button = Button(phy_page17_Sound9, image = multiplereflections ,width=360,height=232,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                            button.configure(image = multiplereflections)
                                                                            button.place(relx = 0.5, rely = 0.7, anchor = CENTER)
                                                                            
                                                                            def Back_page17_Sound9():
                                                                                phy_page17_Sound9.destroy()
                                                                                
                                                                            Back_page17_Sound9=Button(phy_page17_Sound9, bg='coral2', text='<--', command=Back_page17_Sound9)
                                                                            Back_page17_Sound9.pack()
                                                                            Back_page17_Sound9.place(relx=.0,rely=.0)
                                                                            
                                                                            def page18_Sound9():
                                                                                phy_page18_Sound9=Tk()
                                                                                phy_page18_Sound9.title('Sound')
                                                                                canvas_page18_Sound9=Canvas(phy_page18_Sound9, width=1500, height=900, bg='white')
                                                                                canvas_page18_Sound9.pack(expand=YES,fill=BOTH)
                                                                                
                                                                                canvas_page18_Sound9.create_text(360,70,text='''
                                                                                                                 •  The range of sound – on the basis of the range of frequency of a sound, it is categorized into ultrasound and infrasound.
                                                                                                                 
                                                                                                                 Human auditory range is between 20 Hz and 20000 Hz.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                                                
                                                                                canvas_page18_Sound9.create_text(680,210,text='Infrasound                                                                       Ultrasound', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                                canvas_page18_Sound9.create_text(370,490,text='''
                                                                                                                 Infrasound refers to the sound with frequency lower                            Ultrasound refers to the sound with frequency higher 
                                                                                                                 than 20 Hz which can’t be heard by humans.	                           than the upper limit (20 kHz) of frequencies audible 
                                                                                                                                                                                                                            to normal human ears.
                                                                                                                                                                                                
                                                                                                                 Infrasound is used to stabilize myopia in young kids.	            Ultrasound is commonly used to find flaws in materials 
                                                                                                                                                                                                                            to measure the thickness of objects, to fund physical 
                                                                                                                                                                                                                            abnormalities in various parts of human body, as well 
                                                                                                                                                                                                                            as in the form of a sound ranging device called Sonar.
                                                                                                                 
                                                                                                                 Infrasound is influenced by the atmosphere so it can                           Ultrasound is not influenced by any such factors.
                                                                                                                 be used to monitor the activities of the atmosphere.	
                                                                                                                 
                                                                                                                 In particular, natural disasters such as volcanic                                   In particular, ultrasound is also used in micro welding. 
                                                                                                                 eruptions, earthquakes etc can be forecasted by                                 The weld is produced by the application of higher 
                                                                                                                 monitoring the infrasonic waves.	                                                         frequency vibratory energy as the parts are held together 
                                                                                                                                                                                                                            with force.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                                                
                                                                                def Back_page18_Sound9():
                                                                                    phy_page18_Sound9.destroy()
                                                                                
                                                                                Back_page18_Sound9=Button(phy_page18_Sound9, bg='coral2', text='<--', command=Back_page18_Sound9)
                                                                                Back_page18_Sound9.pack()
                                                                                Back_page18_Sound9.place(relx=.0,rely=.0)
                                                                                
                                                                                def page19_Sound9():
                                                                                    global phy_page19_Sound9
                                                                                    phy_page19_Sound9=Toplevel()
                                                                                    phy_page19_Sound9.title('Sound')
                                                                                    canvas_page19_Sound9=Canvas(phy_page19_Sound9, width=1500, height=900, bg='white')
                                                                                    canvas_page19_Sound9.pack(expand=YES,fill=BOTH)
                                                                                    
                                                                                    canvas_page19_Sound9.create_text(220,450,text='Hearing Aid:', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                                    canvas_page19_Sound9.create_text(350,540,text='''
                                                                                                                     The Hearing Aid contains a microphone which receives the sound from the outer atmosphere and converts it into 
                                                                                                                     electrical energy. This electrical energy is passed through an amplifier which amplifies the sound and then moves
                                                                                                                     it to a speaker. The speaker then converts the electrical signal into sound waves and sends it to the ear and
                                                                                                                     provides a clear hearing.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                                                    
                                                                                    global ultrasound
                                                                                    ultrasound = tkinter.PhotoImage(file="ultrasound.png")
                                                                                    button = Button(phy_page19_Sound9, image = ultrasound ,width=602,height=205,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                                    button.configure(image = ultrasound)
                                                                                    button.place(relx = 0.5, rely = 0.3, anchor = CENTER)
                                                                                    
                                                                                    def Back_page19_Sound9():
                                                                                        phy_page19_Sound9.destroy()
                                                                                
                                                                                    Back_page19_Sound9=Button(phy_page19_Sound9, bg='coral2', text='<--', command=Back_page19_Sound9)
                                                                                    Back_page19_Sound9.pack()
                                                                                    Back_page19_Sound9.place(relx=.0,rely=.0)
                                                                                    
                                                                                    def page20_Sound9():
                                                                                        global phy_page20_Sound9
                                                                                        phy_page20_Sound9=Toplevel()
                                                                                        phy_page20_Sound9.title('Sound')
                                                                                        canvas_page20_Sound9=Canvas(phy_page20_Sound9, width=1500, height=900, bg='white')
                                                                                        canvas_page20_Sound9.pack(expand=YES,fill=BOTH)
                                                                                        
                                                                                        canvas_page20_Sound9.create_text(250,80,text='Applications of Ultrasound', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                                        canvas_page20_Sound9.create_text(300,250,text='''
                                                                                                                         The ultrasound waves are the sound waves with high frequency. Due to this, they can travel long distances despite any 
                                                                                                                         obstacles between their paths.
                                                                                                                         
                                                                                                                         •  The ultrasound waves are used in clearing parts of objects that are hard to reach such as a spiral tube or electronic 
                                                                                                                            components. In order to clean the objects, they are put in a solution, then the ultrasonic waves are passed through 
                                                                                                                            the solution. As a result, the dust particles on the object get detached and fall off them.
                                                                                                                         
                                                                                                                         •  Ultrasound waves can recognize tiny cracks in metallic objects that are used in the manufacture of large structures, 
                                                                                                                            buildings and scientific equipment. The presence of such cracks can lower the strength of these structures and machines.
                                                                                                                            Hence, the ultrasound waves are passed through the metallic objects and detectors are used to detect the waves that pass
                                                                                                                            through the cracks. If a crack is present the ultrasound waves would reflect back.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                                                        
                                                                                        global ultrasoundwaves
                                                                                        ultrasoundwaves = tkinter.PhotoImage(file="ultrasoundwaves.png")
                                                                                        button = Button(phy_page20_Sound9, image = ultrasoundwaves ,width=424,height=260,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                                        button.configure(image = ultrasoundwaves)
                                                                                        button.place(relx = 0.5, rely = 0.7, anchor = CENTER)
                                                                                        
                                                                                        def Back_page20_Sound9():
                                                                                            phy_page20_Sound9.destroy()
                                                                                
                                                                                        Back_page20_Sound9=Button(phy_page20_Sound9, bg='coral2', text='<--', command=Back_page20_Sound9)
                                                                                        Back_page20_Sound9.pack()
                                                                                        Back_page20_Sound9.place(relx=.0,rely=.0)
                                                                                        
                                                                                        def page21_Sound9():
                                                                                            phy_page21_Sound9=Tk()
                                                                                            phy_page21_Sound9.title('Sound')
                                                                                            canvas_page21_Sound9=Canvas(phy_page21_Sound9, width=1500, height=900, bg='white')
                                                                                            canvas_page21_Sound9.pack(expand=YES,fill=BOTH)
                                                                                            
                                                                                            canvas_page21_Sound9.create_text(320,400,text='''
                                                                                                                             •  Ultrasonic waves are also used in a medical process called Echocardiography. In this process, the ultrasound waves are 
                                                                                                                                passed through various parts of the heart in order to form the images of the organ.
                                                                                                                             
                                                                                                                             •  Ultrasonic waves are also used in a procedure called Ultrasonography. In this procedure, the ultrasonic waves are passed 
                                                                                                                                through the internal organs of the body in order to get their image. In this way, the doctors can find out the cause of a 
                                                                                                                                disease or any abnormalities in the organs. The ultrasound waves travel through the tissues of the body and as soon as the 
                                                                                                                                density of the tissue changes they reflect back. The reflected waves are then converted into electrical signals which form
                                                                                                                                the images of the internal organs.
                                                                                                                             
                                                                                                                             •  Ultrasound waves are also used to break the kidney stones. 
                                                                                                                             
                                                                                                                             •  This device is used to find the distance, direction and speed of objects that are present under the water. It uses Ultrasonic
                                                                                                                                waves to do so.
                                                                                                                             
                                                                                                                             •  The Sonar consists of two main devices – The transmitter and the detector (or receiver). The main function of the transmitter 
                                                                                                                                is the production and transmission of the Ultrasonic waves in water.
                                                                                                                             
                                                                                                                             •  As these waves travel underwater, they, when hit by an object, reflect back to the detector. The detector then converts these 
                                                                                                                                sound waves into electrical signals which are then interpreted.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                                                
                                                                                            def Back_page21_Sound9():
                                                                                                phy_page21_Sound9.destroy()
                                                                                                
                                                                                            Back_page21_Sound9=Button(phy_page21_Sound9, bg='coral2', text='<--', command=Back_page21_Sound9)
                                                                                            Back_page21_Sound9.pack()
                                                                                            Back_page21_Sound9.place(relx=.0,rely=.0)
                                                                                            
                                                                                            def page22_Sound9():
                                                                                                global phy_page22_Sound9
                                                                                                phy_page22_Sound9=Toplevel()
                                                                                                phy_page22_Sound9.title('Sound')
                                                                                                canvas_page22_Sound9=Canvas(phy_page22_Sound9, width=1500, height=900, bg='white')
                                                                                                canvas_page22_Sound9.pack(expand=YES,fill=BOTH)
                                                                                                
                                                                                                canvas_page22_Sound9.create_text(750,675,text='''SONAR – Sound Navigation and Ranging''', font=('Adobe Fangsong Std R',14), fill = 'black')
                                                                                                
                                                                                                global sonar
                                                                                                sonar = tkinter.PhotoImage(file="sonar.png")
                                                                                                button = Button(phy_page22_Sound9, image = sonar ,width=721,height=551,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                                                button.configure(image = sonar)
                                                                                                button.place(relx = 0.5, rely = 0.45, anchor = CENTER)
                                                                                                
                                                                                                def Back_page22_Sound9():
                                                                                                    phy_page22_Sound9.destroy()
                                                                                                
                                                                                                Back_page22_Sound9=Button(phy_page22_Sound9, bg='coral2', text='<--', command=Back_page22_Sound9)
                                                                                                Back_page22_Sound9.pack()
                                                                                                Back_page22_Sound9.place(relx=.0,rely=.0)
                                                                                                
                                                                                                def page23_Sound9():
                                                                                                    global phy_page23_Sound9
                                                                                                    phy_page23_Sound9=Toplevel()
                                                                                                    phy_page23_Sound9.title('Sound')
                                                                                                    canvas_page23_Sound9=Canvas(phy_page23_Sound9, width=1500, height=900, bg='white')
                                                                                                    canvas_page23_Sound9.pack(expand=YES,fill=BOTH)
                                                                                                    
                                                                                                    canvas_page23_Sound9.create_text(300,140,text='''
                                                                                                                                     •  The distance of the object is calculated with the help of the speed of sound in water and time taken by the way to reach the 
                                                                                                                                        detector. This process is called Echo Ranging.
                                                                                                                                     
                                                                                                                                     •  Uses of Sonar
                                                                                                                                        o  Finding the depth of a water body such as sea
                                                                                                                                        o  Detecting the presence of underwater objects like submarines, hills, icebergs and ships''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                                                                    
                                                                                                    canvas_page23_Sound9.create_text(280,310,text='How do bats search their prey?', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                                                    canvas_page23_Sound9.create_text(310,370,text='''
                                                                                                                                     Bats generate Ultrasonic waves. As these waves hit an object, they get reflected back to the bat’s ears. The bats can understand 
                                                                                                                                     the nature of reflection of these waves and then can decide the position of the object over their prey.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                                                                                                     
                                                                                                    canvas_page23_Sound9.create_text(750,750,text='''Ultrasonic waves generated by bats''', font=('Adobe Fangsong Std R',14), fill = 'black')
                                                                                                    global bats
                                                                                                    bats = tkinter.PhotoImage(file="bats.png")
                                                                                                    button = Button(phy_page23_Sound9, image = bats ,width=335,height=282,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                                                    button.configure(image = bats)
                                                                                                    button.place(relx = 0.5, rely = 0.7, anchor = CENTER)
                                                                                                    
                                                                                                    def Back_page23_Sound9():
                                                                                                        phy_page23_Sound9.destroy()
                                                                                                
                                                                                                    Back_page23_Sound9=Button(phy_page23_Sound9, bg='coral2', text='<--', command=Back_page23_Sound9)
                                                                                                    Back_page23_Sound9.pack()
                                                                                                    Back_page23_Sound9.place(relx=.0,rely=.0)
                                                                                                    
                                                                                                    def page24_Sound9():
                                                                                                        global phy_page24_Sound9
                                                                                                        phy_page24_Sound9=Toplevel()
                                                                                                        phy_page24_Sound9.title('Sound')
                                                                                                        canvas_page24_Sound9=Canvas(phy_page24_Sound9, width=1500, height=900, bg='white')
                                                                                                        canvas_page24_Sound9.pack(expand=YES,fill=BOTH)
                                                                                                        
                                                                                                        canvas_page24_Sound9.create_text(180,110,text='Human Ear', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                                                        canvas_page24_Sound9.create_text(750,500,text='Structure of Human Ear', font=('Adobe Fangsong Std R',14), fill = 'black')
                                                                                                        canvas_page24_Sound9.create_text(310,630,text='''
                                                                                                                                         Our ears allow us to receive audible frequencies in our surroundings. They then convert these sounds into electrical signals 
                                                                                                                                         which are then passed through a special nerve called the auditory nerve to our brain. The brain that interprets these signals
                                                                                                                                         and responds accordingly.''', font=('Adobe Fangsong Std R',18), fill = 'black')
                                                                                                        
                                                                                                        global ear
                                                                                                        ear = tkinter.PhotoImage(file="ear.png")
                                                                                                        button = Button(phy_page24_Sound9, image = ear ,width=353,height=292,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                                                        button.configure(image = ear)
                                                                                                        button.place(relx = 0.5, rely = 0.4, anchor = CENTER)
                                                                                                        
                                                                                                        def Back_page24_Sound9():
                                                                                                            phy_page24_Sound9.destroy()
                                                                                                
                                                                                                        Back_page24_Sound9=Button(phy_page24_Sound9, bg='coral2', text='<--', command=Back_page24_Sound9)
                                                                                                        Back_page24_Sound9.pack()
                                                                                                        Back_page24_Sound9.place(relx=.0,rely=.0)
                                                                                                        
                                                                                                        def page25_Sound9():
                                                                                                            phy_page25_Sound9=Tk()
                                                                                                            phy_page25_Sound9.title('Sound')
                                                                                                            canvas_page25_Sound9=Canvas(phy_page25_Sound9, width=1500, height=900, bg='white')
                                                                                                            canvas_page25_Sound9.pack(expand=YES,fill=BOTH)
                                                                                                            
                                                                                                            canvas_page25_Sound9.create_text(300,350,text='''
                                                                                                                                             •  Pinna:
                                                                                                                                                 The outer part of the ear that gathers sound from the environment.
                                                                                                                                             
                                                                                                                                             •  Auditory Canal:
                                                                                                                                                 Sound collected from the surroundings passes through the Auditory Canal.
                                                                                                                                             
                                                                                                                                             •  Eardrum or Tympanic Membrane:
                                                                                                                                                 It is located at the end of the auditory canal. The eardrum when receives a compression moves inwards because of 
                                                                                                                                                 increased pressure. Similarly, when it receives refraction it moves outwards due to a decrease in pressure. As a 
                                                                                                                                                 result, it starts to vibrate inwards and outwards on receiving a sound wave.
                                                                                                                                             
                                                                                                                                             •  The Middle Ear
                                                                                                                                                 It consists of three bones (hammer, anvil and stirrup). These bones amplify the vibrations produced by the eardrum.
                                                                                                                                                 These vibrations are then passed onto the inner ear by the middle ear.
                                                                                                                                             
                                                                                                                                             •  Cochlea:
                                                                                                                                                 It is located in the inner ear. It converts the vibrations into electrical signals which are then carried to the brain 
                                                                                                                                                 by the auditory nerve.''', font=('Adobe Fangsong Std R',18), fill = 'black')                                                                                                       
                                                                                                    
                                                                                                            def Back_page25_Sound9():
                                                                                                                phy_page25_Sound9.destroy()
                                                                                                
                                                                                                            Back_page25_Sound9=Button(phy_page25_Sound9, bg='coral2', text='<--', command=Back_page25_Sound9)
                                                                                                            Back_page25_Sound9.pack()
                                                                                                            Back_page25_Sound9.place(relx=.0,rely=.0)
                                                                                                            
                                                                                                            def Back_to_class9_Sound9():
                                                                                                                phy_Sound9.destroy()
                                                                                                                phy_page2_Sound9.destroy()
                                                                                                                phy_page3_Sound9.destroy()
                                                                                                                phy_page4_Sound9.destroy()
                                                                                                                phy_page5_Sound9.destroy()
                                                                                                                phy_page6_Sound9.destroy()
                                                                                                                phy_page7_Sound9.destroy()
                                                                                                                phy_page8_Sound9.destroy()
                                                                                                                phy_page9_Sound9.destroy()
                                                                                                                phy_page10_Sound9.destroy()
                                                                                                                phy_page11_Sound9.destroy()
                                                                                                                phy_page12_Sound9.destroy()
                                                                                                                phy_page13_Sound9.destroy()
                                                                                                                phy_page14_Sound9.destroy()
                                                                                                                phy_page15_Sound9.destroy()
                                                                                                                phy_page16_Sound9.destroy()
                                                                                                                phy_page17_Sound9.destroy()
                                                                                                                phy_page18_Sound9.destroy()
                                                                                                                phy_page19_Sound9.destroy()
                                                                                                                phy_page20_Sound9.destroy()
                                                                                                                phy_page21_Sound9.destroy()
                                                                                                                phy_page22_Sound9.destroy()
                                                                                                                phy_page23_Sound9.destroy()
                                                                                                                phy_page24_Sound9.destroy()
                                                                                                                phy_page25_Sound9.destroy()
                                                                                                                
                                                                                                            Back_to_class9_Sound9= Button(phy_page25_Sound9,bg='coral2', text='Class 9',font=('Castellar',18), command=Back_to_class9_Sound9)
                                                                                                            Back_to_class9_Sound9.pack()
                                                                                                            Back_to_class9_Sound9.place(relx=.87,rely=.85)
            
                                                                                                        page25_Sound9=Button(phy_page24_Sound9, bg='coral2', text='-->', command=page25_Sound9)
                                                                                                        page25_Sound9.pack()
                                                                                                        page25_Sound9.place(relx=.98,rely=.0)
            
                                                                                                    page24_Sound9=Button(phy_page23_Sound9, bg='coral2', text='-->', command=page24_Sound9)
                                                                                                    page24_Sound9.pack()
                                                                                                    page24_Sound9.place(relx=.98,rely=.0)
            
                                                                                                page23_Sound9=Button(phy_page22_Sound9, bg='coral2', text='-->', command=page23_Sound9)
                                                                                                page23_Sound9.pack()
                                                                                                page23_Sound9.place(relx=.98,rely=.0)
            
                                                                                            page22_Sound9=Button(phy_page21_Sound9, bg='coral2', text='-->', command=page22_Sound9)
                                                                                            page22_Sound9.pack()
                                                                                            page22_Sound9.place(relx=.98,rely=.0)
            
                                                                                        page21_Sound9=Button(phy_page20_Sound9, bg='coral2', text='-->', command=page21_Sound9)
                                                                                        page21_Sound9.pack()
                                                                                        page21_Sound9.place(relx=.98,rely=.0)
            
                                                                                    page20_Sound9=Button(phy_page19_Sound9, bg='coral2', text='-->', command=page20_Sound9)
                                                                                    page20_Sound9.pack()
                                                                                    page20_Sound9.place(relx=.98,rely=.0)
            
                                                                                page19_Sound9=Button(phy_page18_Sound9, bg='coral2', text='-->', command=page19_Sound9)
                                                                                page19_Sound9.pack()
                                                                                page19_Sound9.place(relx=.98,rely=.0)
            
                                                                            page18_Sound9=Button(phy_page17_Sound9, bg='coral2', text='-->', command=page18_Sound9)
                                                                            page18_Sound9.pack()
                                                                            page18_Sound9.place(relx=.98,rely=.0)
            
                                                                        page17_Sound9=Button(phy_page16_Sound9, bg='coral2', text='-->', command=page17_Sound9)
                                                                        page17_Sound9.pack()
                                                                        page17_Sound9.place(relx=.98,rely=.0)
            
                                                                    page16_Sound9=Button(phy_page15_Sound9, bg='coral2', text='-->', command=page16_Sound9)
                                                                    page16_Sound9.pack()
                                                                    page16_Sound9.place(relx=.98,rely=.0)
            
                                                                page15_Sound9=Button(phy_page14_Sound9, bg='coral2', text='-->', command=page15_Sound9)
                                                                page15_Sound9.pack()
                                                                page15_Sound9.place(relx=.98,rely=.0)
            
                                                            page14_Sound9=Button(phy_page13_Sound9, bg='coral2', text='-->', command=page14_Sound9)
                                                            page14_Sound9.pack()
                                                            page14_Sound9.place(relx=.98,rely=.0)
            
                                                        page13_Sound9=Button(phy_page12_Sound9, bg='coral2', text='-->', command=page13_Sound9)
                                                        page13_Sound9.pack()
                                                        page13_Sound9.place(relx=.98,rely=.0)
            
                                                    page12_Sound9=Button(phy_page11_Sound9, bg='coral2', text='-->', command=page12_Sound9)
                                                    page12_Sound9.pack()
                                                    page12_Sound9.place(relx=.98,rely=.0)
            
                                                page11_Sound9=Button(phy_page10_Sound9, bg='coral2', text='-->', command=page11_Sound9)
                                                page11_Sound9.pack()
                                                page11_Sound9.place(relx=.98,rely=.0)
            
                                            page10_Sound9=Button(phy_page9_Sound9, bg='coral2', text='-->', command=page10_Sound9)
                                            page10_Sound9.pack()
                                            page10_Sound9.place(relx=.98,rely=.0)
            
                                        page9_Sound9=Button(phy_page8_Sound9, bg='coral2', text='-->', command=page9_Sound9)
                                        page9_Sound9.pack()
                                        page9_Sound9.place(relx=.98,rely=.0)
            
                                    page8_Sound9=Button(phy_page7_Sound9, bg='coral2', text='-->', command=page8_Sound9)
                                    page8_Sound9.pack()
                                    page8_Sound9.place(relx=.98,rely=.0)
            
                                page7_Sound9=Button(phy_page6_Sound9, bg='coral2', text='-->', command=page7_Sound9)
                                page7_Sound9.pack()
                                page7_Sound9.place(relx=.98,rely=.0)
            
                            page6_Sound9=Button(phy_page5_Sound9, bg='coral2', text='-->', command=page6_Sound9)
                            page6_Sound9.pack()
                            page6_Sound9.place(relx=.98,rely=.0)
            
                        page5_Sound9=Button(phy_page4_Sound9, bg='coral2', text='-->', command=page5_Sound9)
                        page5_Sound9.pack()
                        page5_Sound9.place(relx=.98,rely=.0)
            
                    page4_Sound9=Button(phy_page3_Sound9, bg='coral2', text='-->', command=page4_Sound9)
                    page4_Sound9.pack()
                    page4_Sound9.place(relx=.98,rely=.0)
            
                page3_Sound9=Button(phy_page2_Sound9, bg='coral2', text='-->', command=page3_Sound9)
                page3_Sound9.pack()
                page3_Sound9.place(relx=.98,rely=.0)
            
            page2_Sound9=Button(phy_Sound9, bg='coral2', text='-->', command=page2_Sound9)
            page2_Sound9.pack()
            page2_Sound9.place(relx=.98,rely=.0)
                        
        ForceLawsofmotion=Button(phy_class9, height=1, width=23, bg='coral2', text='Force and Laws of motion', font=('Castellar',27), command=Force_and_Laws_of_motion)
        Gravitation9=Button(phy_class9, height=1, width=11, bg='coral2', text='Gravitation', font=('Castellar',27), command=Gravitation9)
        WorkEnergy=Button(phy_class9, height=1, width=16, bg='coral2', text='Work and Energy', font=('Castellar',27), command=Work_and_Energy)
        Sound9=Button(phy_class9, height=1, width=8, bg='coral2', text='Sound', font=('Castellar',27), command=Sound9)
        Quiz9=Button(phy_class9, height=1, width=8, bg='coral2', text='Quiz', font=('Castellar',27), command=Quiz9)
        ForceLawsofmotion.pack()
        ForceLawsofmotion.place(relx=.29,rely=.20)
        Gravitation9.pack()
        Gravitation9.place(relx=.39,rely=.35)
        WorkEnergy.pack()
        WorkEnergy.place(relx=.35,rely=.50)
        Sound9.pack()
        Sound9.place(relx=.41,rely=.65)
        Quiz9.pack()
        Quiz9.place(relx=.41,rely=.80)
        
        Back_class9=Button(phy_class9, bg='coral2', text='<--', command=Back9 )
        Back_class9.pack()
        Back_class9.place(relx=.0,rely=.0)
                
    def Class10():
        phy_class10=Tk()
        phy_class10.title('Class 10')
        canvas_class10=Canvas(phy_class10, width=1500, height=900, bg='grey12')
        canvas_class10.pack(expand=YES,fill=BOTH)
        
        def Back10():
            phy_class10.destroy()
        
        def Quiz10():
            phy_Quiz10=Tk()
            phy_Quiz10.title('Quiz')
            canvas_Quiz10=Canvas(phy_Quiz10, width=1500, height=900, bg='grey12')
            canvas_Quiz10.pack(expand=YES,fill=BOTH)
            
            def play():
                import PlayQuiz10
                PlayQuiz10.PlayQuiz()
                
            play10=Button(phy_Quiz10, bg='coral2',font=('Castellar',30), text='Play Quiz', command=play)
            play10.pack()
            play10.place(relx=.40,rely=.35)
            
            def add():
                import Quiz10
                
            quiz10=Button(phy_Quiz10, bg='coral2', font=('Castellar',30),text='Add Questions', command=add)
            quiz10.pack()
            quiz10.place(relx=.36,rely=.55)
            
            def Back_Quiz10():
                phy_Quiz10.destroy()
            
            Back_Quiz10=Button(phy_Quiz10, bg='coral2', text='<--', command=Back_Quiz10)
            Back_Quiz10.pack()
            Back_Quiz10.place(relx=.0,rely=.0)
                    
        #chapters of class 10
        def Electricity():
            phy_Electricity=Tk()
            phy_Electricity.title('Electricity')
            canvas_Electricity=Canvas(phy_Electricity, width=1500, height=900, bg='grey12')
            canvas_Electricity.pack(expand=YES,fill=BOTH)
            
            canvas_Electricity.create_text(700,100,text='''
We are familiar with air current and water current. We know that flowing water constitute water current in rivers. Similarly,
if the electric charge flows through a conductor (for example, through a metallic wire), wesay that there is an electric current in the
conductor. In a torch, weknow that the cells (or a battery, when placed in proper order) provideflow of charges or an electric current
through the torch bulb to glow. Wehave also seen that the torch gives light only when its switch is on. What does a switch do? A switch makes
a conducting link between the cell andthe bulb. A continuous and closed path of an electric current is called anelectric circuit. Now, if the circuit
is broken anywhere (or the switch of thetorch is turned off),\n the current stops flowing and the bulb does not glow.''',font=('Times New Roman',14), fill='white')
            canvas_Electricity.create_text(700,250, text='Electric Current', font=('Times New Roman',20),fill='white')
            canvas_Electricity.create_text(700,320,text='''
How do we express electric current? Electric current is expressed bythe amount of charge flowing through a particular area in unit time.
In other words, it is the rate of flow of electric charges. In circuits usingmetallic wires, electrons constitute the flow of charges.
However, electronswere not known at the time when the phenomenon of electricity was firstobserved. So, electric current was considered to be the
flow of positive charges and the direction of flow of positive charges was taken to be thedirection of electric current. Conventionally, in an
electric circuit thedirection of electric current is taken as opposite to the direction of the flow of electrons, which are negative charges.''', font=('Times New Roman',14),fill='white')
            canvas_Electricity.create_text(700,500, text='''
If a net charge Q, flows across any cross-section of a conductor intime t, then the current I, through the cross-section is
  I=Q/t
The SI unit of electric charge is coulomb (C), which is equivalent to the charge contained  in nearly 6 × 1018 electrons. (We know thatan electron
possesses a negative charge of 1.6 × 10–19 C.)
The electriccurrent is expressed by a unit called ampere (A), named after theFrench scientist, Andre-Marie Ampere (1775–1836). One ampere is
constituted by the flow of one coulomb of charge per second, that is, 1 A = 1 C/1 s. Small quantities of current are expressed inmilliampere
(1 mA = 10–3 A) or in microampere(1 μA = 10–6 A). An instrument called ammetermeasures electric current in a circuit.
It is always connected in series in a circuit through whichthe current is to be measured. Figure 12.1 showsthe schematic diagram of a typical
electric circuitcomprising a cell, an electric bulb, an ammeter and a plug key. Note that the electric currentflows in the circuit from the
positive terminal ofthe cell to the negative terminal of the cell throughthe bulb and ammeter.''',font=('Times New Roman',14),fill='white')
            
            def Back_Electricity():
                phy_Electricity.destroy()
            
            Back_Electricity=Button(phy_Electricity, bg='coral2', text='<--', command=Back_Electricity)
            Back_Electricity.pack()
            Back_Electricity.place(relx=.0,rely=.0)
            
            def Elec_page1():
                phy_Elec_page1=Tk()
                phy_Elec_page1.title('Electricity')
                canvas_Elec_page1=Canvas(phy_Elec_page1, width=1500,height=900, bg='grey12')
                canvas_Elec_page1.pack(expand=YES, fill=BOTH)
                
                canvas_Elec_page1.create_text(550,350, text='''
Potential Difference

 Work done per unit charge in taking charge from one point to another is known as Potential Difference. The unit of potential
 difference is volt (V). 1V is defined as the potential difference between two points if 1 Joule of work is done to move 1 coulomb charge
 from one point to another.
 
Ohm’s law                                                               
Potential difference between two points is directly proportional to the current, provided temperature is constant.
      V ∝ I
    ⇒ V = IR
                                                                
R is a constant known as Resistance. The SI unit of resistance is ohm (Ω)
                                                                
Factors on which resistance of a conductor depends-
                                                                
 1.It is directly proportional to length of conductor.
 2.Inversely proportional to the area of cross-section.
 3.Directly proportional to the temperature.
 4.Depends on nature of material.
                                                                
Resistivity:                                                              
-> Resistivity is the property of the material. The SI unit of resistivity is ohm-metre.                                                              
-> Resistivity of metals varies from 10-8 to 10-6.                                                              
-> Resistivity of insulators varies from 1012 to 1017                                                            
-> Copper and aluminium are used in electrical transmission due to their low resistivity.                                                               
-> Resistance = Resistivity * Length of Conductor/Cross Sectional Area
                                                                
Resistors in series
When two or more resistors are joined in series, then their total resistance is given by the formula-''', font=('Times New Roman',14), fill='white')
                    
                def V():
                    import tkinter as tk

                    def show_entry_fields():
                        #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
                        V=int(e1.get())/int(e2.get())
                        tk.Label(master, text='Potential Difference=').grid(row=2,column=0)
                        tk.Label(master, text=(V,'V')).grid(row=2, column=1)

                    master = tk.Tk()
                    tk.Label(master, text="Work Done").grid(row=0)
                    tk.Label(master, 
                             text="Charge").grid(row=1)
                    
                    e1 = tk.Entry(master)
                    e2 = tk.Entry(master)

                    e1.grid(row=0, column=1)
                    e2.grid(row=1, column=1)
                    
                    tk.Button(master, 
                              text='Quit', 
                              command=master.quit).grid(row=3, 
                                                 column=0, 
                                                 sticky=tk.W, 
                                                 pady=4)
                    tk.Button(master, 
                              text='Show', command=show_entry_fields).grid(row=3, 
                                                                    column=1, 
                                                                    sticky=tk.W, 
                                                                    pady=4)
                    
                    tk.mainloop()  
                    
                def I():
                    import tkinter as tk

                    def show_entry_fields():
                        #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
                        I=int(e1.get())/int(e2.get())
                        tk.Label(master, text='Current=').grid(row=2,column=0)
                        tk.Label(master, text=(I,'A')).grid(row=2, column=1)

                    master = tk.Tk()
                    tk.Label(master, text="Charge(Q)").grid(row=0)
                    tk.Label(master, 
                             text="time(t)").grid(row=1)
                    
                    e1 = tk.Entry(master)
                    e2 = tk.Entry(master)

                    e1.grid(row=0, column=1)
                    e2.grid(row=1, column=1)
                    
                    tk.Button(master, 
                              text='Quit', 
                              command=master.quit).grid(row=3, 
                                                 column=0, 
                                                 sticky=tk.W, 
                                                 pady=4)
                    tk.Button(master, 
                              text='Show', command=show_entry_fields).grid(row=3, 
                                                                    column=1, 
                                                                    sticky=tk.W, 
                                                                    pady=4)
                    
                    tk.mainloop()

                vo=Button(phy_Elec_page1, bg='coral2', text='Find Potential Difference', font=('Castellar',10), command=V)
                i=Button(phy_Elec_page1, bg='coral2', text='Find Current', font=('Castellar',10), command=I)
                vo.pack()
                vo.place(relx=.80, rely=.14)
                i.pack()
                i.place(relx=.80, rely=.20)
                    
                def Elec_page2():
                    global phy_Elec_page2
                    phy_Elec_page2=Toplevel()
                    phy_Elec_page2.title('Electricity')
                    canvas_Elec_page2=Canvas(phy_Elec_page2, width=1500,height=900, bg='grey12')
                    canvas_Elec_page2.pack(expand=YES, fill=BOTH)
                    canvas_Elec_page2.create_text(700,50,text='Resistors in series',font=('Times New Roman',18), fill='white')
                    canvas_Elec_page2.create_text(700,100,text='When two or more resistors are joined in series, then their total resistance is given by the formula-',font=('Times New Roman',14),fill='white')
                    canvas_Elec_page2.create_text(700,500,text='''
RS = R1 + R2 + R3
The current will remain same through all resistor. Total voltage is given by-
V = V1 + V2 + V3
Voltage across each resistor is given as –
V1 = lR1
V2 = lR2 [V1 + V2 + V3 = V]
V3 = lR3V = lR
⇒ V = lR1 + lR2 + lR3
lR = l(R1+ R2 + R3)
R = R1 + R2 + R3''',font=('Times New Roman',14),fill='white')
                    global series
                    series = tkinter.PhotoImage(file="series.png")
                    button = Button(canvas_Elec_page2,image = series,width=363,height=206,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                    button.configure(image = series)
                    button.place(relx=0.50,rely=0.35,anchor = CENTER)

                    def Elec_page3():
                        global phy_Elec_page3
                        phy_Elec_page3=Toplevel()
                        phy_Elec_page3.title('Electricity')
                        canvas_Elec_page3=Canvas(phy_Elec_page3, width=1500,height=900, bg='grey12')
                        canvas_Elec_page3.pack(expand=YES, fill=BOTH)
                        canvas_Elec_page3.create_text(700,100,text='Resistors in Parallel',font=('Times New Roman',18),fill='white')
                        canvas_Elec_page3.create_text(700,150,text='In this case, voltage is same across each resistor and is equal to applied voltage. Total current is given as-',font=('Times new Roman',14),fill='white')
                        canvas_Elec_page3.create_text(700,600,text='''
V/R = V/R1 + V/R2 + V/R3
1/Rp = 1/R1 + 1/R2 + 1/R3

Advantages of Parallel Combination over Series Combination

If one component fails in series combination, then complete circuit is broken and no component can work properly. Different appliances need
different current, this can be met through parallel.''',font=('Times New Roman',14),fill='white')

                        global parallel
                        parallel = tkinter.PhotoImage(file="parallel.png")
                        button = Button(canvas_Elec_page3,image = parallel,width=380,height=245,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                        button.configure(image = parallel)
                        button.place(relx=0.50,rely=0.45,anchor = CENTER)

                        def Elec_page4():
                            phy_Elec_page4=Tk()
                            phy_Elec_page4.title('Electricity')
                            canvas_Elec_page4=Canvas(phy_Elec_page4, width=1500,height=900, bg='grey12')
                            canvas_Elec_page4.pack(expand=YES, fill=BOTH)
                            canvas_Elec_page4.create_text(700,100,text='Heating effects of Electric Current',font=('Times New Roman',20),fill='white')
                            canvas_Elec_page4.create_text(700,200,text='''
When charge Q moves against the potential difference V in time t, the amount of work is given by-
W = Q x V
W = V x (Q / t) x t
W = Vit''',font=('Times New Roman',14),fill='white')
                            canvas_Elec_page4.create_text(700,300,text='Joule\'s Law of Heating',font=('Times New Roman',18), fill='white')
                            canvas_Elec_page4.create_text(700,400,text='''
•	Heat produced in a resistor is directly proportional to square root of current.
•	It is also directly proportional to resistance for a given current.
•	Also, directly proportional to time
H = I^2 x Rt
Filament of electric bulb is made up of tungsten because it has a very high melting point and also does not oxidize readily at a high temperature.
Electric fuse is a safety device to protect the electrical appliance from short circuit''',font=('Times New Roman',14),fill='white')
                            canvas_Elec_page4.create_text(700,520,text='Electric Power',font=('Times New Roman',18), fill='white')
                            canvas_Elec_page4.create_text(700,600,text='''
The rate at which electric energy is dissipated or consumed in an electric current. The SI unit of power is Watt.
P = Vl
⇒ P = I^2 R = V^2 / R
The commercial unit of electric energy is kilowatt hour (KWh).''',font=('Times New Roman',14),fill='white')

                            def Back_to_class10_Elec():
                                phy_Electricity.destroy()
                                phy_Elec_page1.destroy()
                                phy_Elec_page2.destroy()
                                phy_Elec_page3.destroy()
                                phy_Elec_page4.destroy()

                            Back_to_class10_Elec=Button(phy_Elec_page4,bg='coral2', text='Class 10',font=('Castellar',18), command=Back_to_class10_Elec)
                            Back_to_class10_Elec.pack()
                            Back_to_class10_Elec.place(relx=.87,rely=.85)
                        
                        def Back_elec_page4():
                            phy_Elec_page4.destroy() 
                            
                        elec_page4=Button(phy_Elec_page3, bg='coral2', text='-->', command=Elec_page4)            
                        elec_page4.pack()
                        elec_page4.place(relx=.98, rely=.0)
                           
                        def Back_elec_page3():
                            phy_Elec_page3.destroy()
                        
                    def Back_elec_page2():
                        phy_Elec_page2.destroy()

                    elec_page3=Button(phy_Elec_page2, bg='coral2', text='-->', command=Elec_page3)            
                    elec_page3.pack()
                    elec_page3.place(relx=.98, rely=.0)
                        
                    '''Back_Elec_page2=Button(phy_Elec_page2, bg='coral2', text='<--', command=Back_Elec_page2)
                    Back_Elec_page2.pack()
                    Back_Elec_page2.place(relx=.0,rely=.0)'''
                
                
                def Back_Elec_page1():
                    phy_Elec_page1.destroy()

                elec_page2=Button(phy_Elec_page1, bg='coral2', text='-->', command=Elec_page2)            
                elec_page2.pack()
                elec_page2.place(relx=.98, rely=.0)
            
                Back_Elec_page1=Button(phy_Elec_page1, bg='coral2', text='<--', command=Back_Elec_page1)
                Back_Elec_page1.pack()
                Back_Elec_page1.place(relx=.0,rely=.0)

            elec_page1=Button(phy_Electricity, bg='coral2', text='-->', command=Elec_page1)            
            elec_page1.pack()
            elec_page1.place(relx=.98, rely=.0)
                        
        def Magnetic_effects_of_electric_current():
            global phy_Magneticeffects
            phy_Magneticeffects=Toplevel()
            phy_Magneticeffects.title('Magnetic effects of electric current')
            canvas_Magneticeffects=Canvas(phy_Magneticeffects, width=1500, height=900, bg='white')
            canvas_Magneticeffects.pack(expand=YES,fill=BOTH)
            canvas_Magneticeffects.create_text(700,200, text='''
Any substance that attracts iron and iron like objects is defined as magnet. When a wire 
carries an electric current, it behaves as a magnet.

Properties of Magnet

1)Every magnet has north and south poles.
2)Same poles repel each other and unlike poles attract each other.
3)A freely suspended magnet will align itself in north south direction, north
  facing north of the magnet and south facing south of the magnet.
''',font=('courier',14), fill='black')
            
            canvas_Magneticeffects.create_text(700,400, text='''Characteristics of Field Lines
''',font=('courier',14), fill='black')
            global mag
            mag = tkinter.PhotoImage(file="linemag.png")
            button = Button(canvas_Magneticeffects,image = mag,width=355,height=248,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
            button.configure(image = mag)
            button.place(relx=0.50,rely=0.75,anchor = CENTER)
            
            def mag_page1():
                global phy_mag_page1
                phy_mag_page1=Toplevel()
                phy_mag_page1.title('Magnetic effects of electric current')
                canvas_mag_page1=Canvas(phy_mag_page1, width=1500, height=900, bg='white')
                canvas_mag_page1.pack(expand=YES,fill=BOTH)
                canvas_mag_page1.create_text(700,100, text='''Magnetic Field of a Bar Magnet
''',font=('courier',14), fill='black')
                canvas_mag_page1.create_text(700,150, text='''
Hold the thumb, forefinger and middle finger of right hand at right angles to each other.
 If the forefinger is in direction of magnetic field and the thumb points in the direction 
 of motion of conductor, than the direction of induced current is indicated by middle finger
''',font=('courier',14), fill='black')
                canvas_mag_page1.create_text(700,200,text='''
 Magnetic Field due to current through a Straight Conductor''', font=('courier',14), fill='black')
                canvas_mag_page1.create_text(700,250,text='''
They are represented in the form of concentric circles at every point on conductor. ''', font=('courier',14), fill='black')
                canvas_mag_page1.create_text(700,650,text='''
Direction of the field is given by compass or right-hand thumb rule. 
Circles are always closer near the conductor. ''', font=('courier',14), fill='black')
                global straight
                straight = tkinter.PhotoImage(file="straight.png")
                button = Button(canvas_mag_page1,image = straight,width=500,height=261,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                button.configure(image = straight)
                button.place(relx=0.50,rely=0.60,anchor = CENTER)
                
                def mag_page2():
                    global phy_mag_page2
                    phy_mag_page2=Toplevel()
                    phy_mag_page2.title('Magnetic Effects of Electric Current')
                    canvas_mag_page2=Canvas(phy_mag_page2, width=1500, height=900, bg='white')
                    canvas_mag_page2.pack(expand=YES, fill=BOTH)
                    canvas_mag_page2.create_text(700,50,text='''
Magnetic field due to current through a circular loop. ''', font=('Times New Roman',16), fill='black')
                    canvas_mag_page2.create_text(700,100,text='''
It is represented by concentric circle at every point. Circle will become larger and larger as one move away.
Magnetic field ''', font=('Times New Roman',14), fill='black')
                    
                    canvas_mag_page2.create_text(700,530, text='Factors affecting magnetic field of a circular current carrying conductor',font=('Times New Roman',16),fill='black')
                    canvas_mag_page2.create_text(700,600, text='''


-> Magnetic field is directly proportional to the current passing through the conductor.

->  Magnetic field is inversely proportional to the distance from the conductor.

->  Magnetic field is directly proportional to number of turns in coil.
''', font=('Times New Roman',14),fill='black')
                    global circle
                    circle = tkinter.PhotoImage(file="circle.png")
                    button = Button(canvas_mag_page2,image = circle,width=500,height=342,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                    button.configure(image = circle)
                    button.place(relx=0.50,rely=0.42,anchor = CENTER)
                    
                    def mag_page3():
                        global phy_mag_page3
                        phy_mag_page3=Toplevel()
                        phy_mag_page3.title('Magnetic Effects of Electric Current')
                        canvas_mag_page3=Canvas(phy_mag_page3, width=1500, height=900, bg='white')
                        canvas_mag_page3.pack(expand=YES, fill=BOTH)
                        canvas_mag_page3.create_text(700,100, text='Solenoid',font=('Times New Roman',18),fill='black')
                        canvas_mag_page3.create_text(700,150,text='''
Solenoid is defined as coil of many circular turns of insulated copper wire wrapped closely 
in a cylindrical form. Magnetic field of solenoid is similar to bar magnet.''', font=('Times New Roman',14), fill='black')
                        canvas_mag_page3.create_text(700,450, text='Electromagnet', font=('Times New Roman',18), fill='black')
                        canvas_mag_page3.create_text(700,500, text='''
It is temporary magnet that can be easily demagnetized. In this type of magnet,
polarity can be reversed and strength can be varied. They are very strong magnet.''', font=('Times New Roman',14), fill='black')
                        canvas_mag_page3.create_text(700,600, text='Permanent Magnet', font=('Times New Roman',18), fill='black')
                        canvas_mag_page3.create_text(700,630, text='''
These types of magnet cannot be easily demagnetized. They are weak magnets in which polarity cannot be reversed.''',font=('Times New Roman',14), fill='black')

                        global sol
                        sol = tkinter.PhotoImage(file="solenoid1.png")
                        button = Button(canvas_mag_page3,image = sol,width=253,height=264,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                        button.configure(image = sol)
                        button.place(relx=0.50,rely=0.45,anchor = CENTER)
                        
                        def mag_page4():
                            phy_mag_page4=Tk()
                            phy_mag_page4.title('Magnetic Effects of Electric Current')
                            canvas_mag_page4=Canvas(phy_mag_page4, width=1500, height=900, bg='white')
                            canvas_mag_page4.pack(expand=YES, fill=BOTH)
                            canvas_mag_page4.create_text(700,100, text='Force on a current carrying conductor in a magnetic field',font=('Times New Roman',18),fill='black')
                            canvas_mag_page4.create_text(700,130,text='''
The displacement in the conductor is the maximum when the direction of current is at right 
angle to the direction of magnetic field.''', font=('Times New Roman',14), fill='black')
                            canvas_mag_page4.create_text(700,200, text='Flemings Left Hand Rule', font=('Times New Roman',18), fill='black')
                            canvas_mag_page4.create_text(700,270,text='''
Stretch the thumb, forefinger and middle finger of the left hand such that they are mutually perpendicular.
 If the forefingers is in the direction of the magnetic field, middle finger in the direction of current 
 then thumb will point in the direction of motion or force.''', font=('Times New Roman',14), fill='black')
                            canvas_mag_page4.create_line(700,400,700,320)
                            canvas_mag_page4.create_line(700,400,600,400)
                            canvas_mag_page4.create_line(700,400,670,480)
                            
                            def mag_page5():
                                phy_mag_page5=Tk()
                                phy_mag_page5.title('Magnetic Effects of Electric Current')
                                canvas_mag_page5=Canvas(phy_mag_page5, width=1500, height=900, bg='white')
                                canvas_mag_page5.pack(expand=YES, fill=BOTH)
                                canvas_mag_page5.create_text(700,50, text='Electric Motor',font=('Times New Roman',18),fill='black')
                                canvas_mag_page5.create_text(700,100,text='''
A rotating device that converts electrical energy to mechanical energy.''', font=('Times New Roman',14), fill='black')
                                canvas_mag_page5.create_text(700,400,text='''
It consists of rectangular coil ABCD made up of insulated copper wire. The coil is placed perpendicular to magnetic field.
 There are two conducting brushes X and Y. Current in coil ABCD enters through a source battery through conducting brush X 
 and flows back to the battery through brush Y. The split ring acts as commutator. It reverses the direction of flow of 
 current in a commutator.

They are used in electromagnets, as soft iron core on which coil is wound. Armature enhances the power of the motor.''', font=('Times New Roman',14), fill='black')
                                canvas_mag_page5.pack(expand=YES, fill=BOTH)
                                canvas_mag_page5.create_text(700,550,text='''Electromagnetic Induction''', font=('Times New Roman',16), fill='black')
                                canvas_mag_page5.create_text(700,600,text='''
When we place a conductor in a changing magnetic field, some current is induced in it. This current is known
 as Induced Current and the phenomenon is known as Electromagnetic Induction''', font=('Times New Roman',14), fill='black')
                                
                                def mag_page6():
                                    phy_mag_page6=Tk()
                                    phy_mag_page6.title('Magnetic Effects of Electric Current')
                                    canvas_mag_page6=Canvas(phy_mag_page6, width=1500, height=900, bg='white')
                                    canvas_mag_page6.pack(expand=YES, fill=BOTH)
                                    canvas_mag_page6.create_text(700,50, text='Fleming Right Hand Rule', font=('Times New Roman',18), fill='black')
                                    canvas_mag_page6.create_text(700,120, text='''
Hold the forefinger, middle finger and thumb of right hand at right angles to each other. Forefinger points towards the 
direction of magnetic field, thumb points in the direction of motion of conductor and middle finger
 shows direction of induced current.''', font=('Times New Roman',14), fill='black')
                                    canvas_mag_page6.create_text(700,200, text='Electric Generator', font=('Times New Roman',20),fill='black')
                                    canvas_mag_page6.create_text(700,250, text='''
Electric Energy is a device used to convert mechanical energy into alternating form of electrical energy. It consists 
of insulated copper wire, magnetic poles, split rings, axle, brushes and galvanometer.''', font=('Times New Roman',14), fill='black')
                                    canvas_mag_page6.create_text(700,550, text='''
The axle is rotated so that it moves clockwise direction that is AB moves up and CD moves down. After half rotation, 
CD starts to move up and AB moves down. After every half rotation current changes its direction, this is called AC current.''', font=('Times New Roman',14), fill='black')

                                    def mag_page7():
                                        phy_mag_page7=Tk()
                                        phy_mag_page7.title('Magnetic Effects of Electric Current')
                                        canvas_mag_page7=Canvas(phy_mag_page7, width=1500, height=900, bg='white')
                                        canvas_mag_page7.pack(expand=YES, fill=BOTH)
                                        canvas_mag_page7.create_text(700,50, text='Domestic Electric Circuits', font=('Times New Roman',16), fill='black')
                                        canvas_mag_page7.create_text(700,150, text='''
Three kinds of wires are used in domestic electric circuits.

    1) Live wire red in colour
    2) Neutral wire with black insulation cover
    3) Earth wire with green insulation cover.
The potential difference between live and neutral wire in India is 220V.''', font=('Times New Roman',14), fill='black')
                                        canvas_mag_page7.create_text(700,300, text='Electric Fuse', font=('Times New Roman',16), fill='black')
                                        canvas_mag_page7.create_text(700,350, text='''


   -> It is a safety device to limit the current in an electric circuit.
   -> It prevents the electric appliances from damage.
   -> It is made up of material which has high resistivity and low melting point.
''', font=('Times New Roman',14), fill='black')
                
                                        def Back_to_class10_mag():
                                            phy_Magneticeffects.destroy()
                                            phy_mag_page1.destroy()
                                            phy_mag_page2.destroy()
                                            phy_mag_page3.destroy()
                                            phy_mag_page4.destroy()
                                            phy_mag_page5.destroy()
                                            phy_mag_page6.destroy()
                                            phy_mag_page7.destroy()

                                        Back_to_class10_mag=Button(phy_mag_page7,bg='coral2', text='Class 10',font=('Castellar',18), command=Back_to_class10_mag)
                                        Back_to_class10_mag.pack()
                                        Back_to_class10_mag.place(relx=.87,rely=.85)

                                    Mag_page7=Button(phy_mag_page6, bg='coral2', text='-->', command=mag_page7)
                                    Mag_page7.pack()
                                    Mag_page7.place(relx=.98,rely=.0)
                                    
                                Mag_page6=Button(phy_mag_page5, bg='coral2', text='-->', command=mag_page6)
                                Mag_page6.pack()
                                Mag_page6.place(relx=.98,rely=.0)
                                
                            Mag_page5=Button(phy_mag_page4, bg='coral2', text='-->', command=mag_page5)
                            Mag_page5.pack()
                            Mag_page5.place(relx=.98,rely=.0)
                            
                        Mag_page4=Button(phy_mag_page3, bg='coral2', text='-->', command=mag_page4)
                        Mag_page4.pack()
                        Mag_page4.place(relx=.98,rely=.0)
                            
                    Mag_page3=Button(phy_mag_page2, bg='coral2', text='-->', command=mag_page3)
                    Mag_page3.pack()
                    Mag_page3.place(relx=.98,rely=.0)
                
                Mag_page2=Button(phy_mag_page1, bg='coral2', text='-->', command=mag_page2)
                Mag_page2.pack()
                Mag_page2.place(relx=.98,rely=.0)
            
            def Back_Magneticeffects():
                phy_Magneticeffects.destroy()
            
            Mag_page1=Button(phy_Magneticeffects, bg='coral2', text='-->', command=mag_page1)
            Mag_page1.pack()
            Mag_page1.place(relx=.97,rely=.0)
                        
            Back_Magneticeffects=Button(phy_Magneticeffects, bg='coral2', text='<--', command=Back_Magneticeffects)
            Back_Magneticeffects.pack()
            Back_Magneticeffects.place(relx=.0,rely=.0)
                        
        def Light10():
            phy_Light10=Tk()
            phy_Light10.title('Light')
            canvas_Light10=Canvas(phy_Light10, width=1500, height=900, bg='white')
            canvas_Light10.pack(expand=YES,fill=BOTH)
            
            canvas_Light10.create_text(700,100, text='Laws of Reflection', font=('Times New Roman',18), fill='black')
            canvas_Light10.create_text(700,150, text='''
 ->   The angle of incidence is equal to angle of reflection
 ->   Incident ray, reflected ray and normal all lie in the same plane.
''', font=('Times New Roman',14), fill='black') 
            canvas_Light10.create_text(700,200,text='Spherical Mirrors', font=('Times New Roman',18), fill='black')
            canvas_Light10.create_text(700,230, text='''
Most common type of curved mirrors are spherical mirrors. Mirrors in which reflecting surface are spherical in shape, is known 
as spherical mirrors. Reflecting surface of a mirror can be curved inwards or curved outwards. The one which is curved inward
 is known as concave mirror and the one which curved outwards is known as convex mirror.''', font=('Times New Roman',14), fill='black')
            canvas_Light10.create_arc(200,400,300,540, style=ARC, start=270, extent=180)
            canvas_Light10.create_text(300,360, text='Concave mirror', font=('Times New Roman',16), fill = 'black')
                        
            canvas_Light10.create_arc(950,400,1050,540, style=ARC, start=90, extent=180)
            canvas_Light10.create_text(1000,360, text='Convex mirror', font=('Times New Roman',16), fill = 'black')
            j=260
            k=0
            for i in range(400,540,15):
                canvas_Light10.create_line(j,i,j+15,i+4, fill='black')
                j=j+15-k
                k+=3.5
            j=990
            k=0
            for i in range(400,540,15):
                canvas_Light10.create_line(j,i,j+15,i+7, fill='black')
                j=j-15+k
                k+=3.5
                
            def light10_page1():
                global phy_light10_page1
                phy_light10_page1=Toplevel()
                phy_light10_page1.title('Light')
                canvas_light10_page1=Canvas(phy_light10_page1, width=1500, height=900, bg='white')
                canvas_light10_page1.pack(expand=YES,fill=BOTH)
                canvas_light10_page1.create_text(700,100, text='Some Important Terms', font=('Times New Roman',18), fill='black')
                canvas_light10_page1.create_text(700,300, text='''


    1) Pole- The centre of the reflecting surface in a spherical mirror is a pole. It is represented by P.
                
    2) Centre of curvature- Reflecting surface in a spherical mirror has a centre, this is known as centre of curvature. Centre of 
                         curvature in convex mirror lies behind the mirror whereas in concave mirror, it lies in front of the mirror.
                         
    3) Radius of curvature- The radius of the reflecting surface of the spherical mirror is known as radius of curvature. It is represented by R.
                
    4) Principal axis- Straight line passing through the pole and centre of curvature in a spherical mirror is known as principal axis.
                
    5) Principal focus- The reflected rays appear to come from a point on the principal axis, this is known as principal focus.
                
    6) Focal length- The distance between the pole and the principal focus in a spherical mirror is known as focal length and it is represented by f.
                
    7) Aperture- The diameter of the reflecting surface is defined as aperture.
                

Note: Radius of curvature is twice the focal length (R=2f).''', font=('Times New Roman',14), fill='black')
                global m
                m = tkinter.PhotoImage(file="mirror1.png")
                button = Button(canvas_light10_page1,image = m,width=403,height=300,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                button.configure(image = m)
                button.place(relx=0.50,rely=0.75,anchor = CENTER)
                
                def Back_light10_page1():
                    phy_light10_page1.destroy()
                    
                Back_light10_page1=Button(phy_light10_page1, bg='coral2', text='<--', command=Back_light10_page1)
                Back_light10_page1.pack()
                Back_light10_page1.place(relx=.0,rely=.0)                                          

                def light10_page2():
                    global phy_light10_page2
                    phy_light10_page2=Toplevel()
                    phy_light10_page2.title('Light')
                    canvas_light10_page2=Canvas(phy_light10_page2, width=1500, height=900, bg='white')
                    canvas_light10_page2.pack(expand=YES,fill=BOTH)
                    
                    canvas_light10_page2.create_text(700,100, text='Representations of the images formed by Spherical Mirrors using Ray Diagrams', font=('Times New Roman',18), fill='black')
                    canvas_light10_page2.create_text(700,200,text='''
We draw the ray diagram to locate the image of an object formed. The intersection point of at least 
two reflected will give the position of image of the point object. The two rays that can be used to draw 
the ray diagram are-
   -> A ray parallel to the principal axis should pass through the focus after reflection in case of concave mirror, or appear to diverge
       in case of convex mirror.
''', font=('Times New Roman',18), fill='black')
                
                    global m1
                    m1 = tkinter.PhotoImage(file="mirror2.png")
                    button = Button(canvas_light10_page2,image = m1,width=750,height=365,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                    button.configure(image = m1)
                    button.place(relx=0.50,rely=0.60,anchor = CENTER)
                    
                    def Back_light10_page2():
                        phy_light10_page2.destroy()
                    
                    Back_light10_page2=Button(phy_light10_page2, bg='coral2', text='<--', command=Back_light10_page2)
                    Back_light10_page2.pack()
                    Back_light10_page2.place(relx=.0,rely=.0)
                    
                    def light10_page3():
                        global phy_light10_page3
                        phy_light10_page3=Toplevel()
                        phy_light10_page3.title('Light')
                        canvas_light10_page3=Canvas(phy_light10_page3, width=1500, height=900, bg='white')
                        canvas_light10_page3.pack(expand=YES,fill=BOTH)
                        canvas_light10_page3.create_text(700,100, text='''
   -> A ray passing through the focus of the concave mirror or directed towards the focus in case of 
   convex mirror, should appear parallel to the principal axis after reflection.''', font=('Times New Roman',18), fill='black')
                        global m2
                        m2 = tkinter.PhotoImage(file="mirror3.png")
                        button = Button(canvas_light10_page3,image = m2,width=807,height=346,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                        button.configure(image = m2)
                        button.place(relx=0.50,rely=0.60,anchor = CENTER)
                        
                        def Back_light10_page3():
                            phy_light10_page3.destroy()
                    
                        Back_light10_page3=Button(phy_light10_page3, bg='coral2', text='<--', command=Back_light10_page3)
                        Back_light10_page3.pack()
                        Back_light10_page3.place(relx=.0,rely=.0)
                        
                        def light10_page4():
                            global phy_light10_page4
                            phy_light10_page4=Toplevel()
                            phy_light10_page4.title('Light')
                            canvas_light10_page4=Canvas(phy_light10_page4, width=1500, height=900, bg='white')
                            canvas_light10_page4.pack(expand=YES,fill=BOTH)
                            canvas_light10_page4.create_text(700,100, text='''
   -> A ray which is passing through the centre of curvature in a concave mirror or directed in case of 
   convex mirror, should reflect along the same path.''', font=('Times New Roman',18), fill='black')
                            global m3
                            m3 = tkinter.PhotoImage(file="mirror4.png")
                            button = Button(canvas_light10_page4,image = m3,width=716,height=313,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                            button.configure(image = m3)
                            button.place(relx=0.50,rely=0.60,anchor = CENTER)
                            
                            def Back_light10_page4():
                                phy_light10_page4.destroy()
                    
                            Back_light10_page4=Button(phy_light10_page4, bg='coral2', text='<--', command=Back_light10_page4)
                            Back_light10_page4.pack()
                            Back_light10_page4.place(relx=.0,rely=.0)
                    
                            def light10_page5():
                                global phy_light10_page5
                                phy_light10_page5=Toplevel()
                                phy_light10_page5.title('Light')
                                canvas_light10_page5=Canvas(phy_light10_page5, width=1500, height=900, bg='white')
                                canvas_light10_page5.pack(expand=YES,fill=BOTH)
                                canvas_light10_page5.create_text(700,100, text='''
   -> A ray when incident obliquely to principal axis on a concave or convex mirror is also reflected 
       obliquely.''', font=('Times New Roman',18), fill='black' )
                                global m4
                                m4 = tkinter.PhotoImage(file="mirror5.png")
                                button = Button(canvas_light10_page5,image = m4,width=729,height=300,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                                button.configure(image = m4)
                                button.place(relx=0.50,rely=0.60,anchor = CENTER)
                                
                                def Back_light10_page5():
                                    phy_light10_page5.destroy()
                    
                                Back_light10_page5=Button(phy_light10_page5, bg='coral2', text='<--', command=Back_light10_page5)
                                Back_light10_page5.pack()
                                Back_light10_page5.place(relx=.0,rely=.0)
                    
                                def light10_page6():
                                    global phy_light10_page6
                                    phy_light10_page6=Toplevel()
                                    phy_light10_page6.title('Light')
                                    canvas_light10_page6=Canvas(phy_light10_page6, width=1500, height=900, bg='white')
                                    canvas_light10_page6.pack(expand=YES,fill=BOTH)
                                    canvas_light10_page6.create_text(700,50, text='Image formation by Convex Mirror', font=('Castellar',24), fill='black' )
                                    global m5
                                    m5 = tkinter.PhotoImage(file="mirrors7.png")
                                    button = Button(canvas_light10_page6,image = m5,width=682,height=550,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                                    button.configure(image = m5)
                                    button.place(relx=0.50,rely=0.60,anchor = CENTER)
                                    
                                    def Back_to_class10_Light():
                                        phy_Light10.destroy()
                                        phy_light10_page1.destroy()
                                        phy_light10_page2.destroy()
                                        phy_light10_page3.destroy()
                                        phy_light10_page4.destroy()
                                        phy_light10_page5.destroy()
                                        phy_light10_page6.destroy()
                                                                    
                                    Back_to_class10_Light= Button(phy_light10_page6,bg='coral2', text='Class 11',font=('Castellar',18), command=Back_to_class10_Light)
                                    Back_to_class10_Light.pack()
                                    Back_to_class10_Light.place(relx=.87,rely=.85)
                                    
                                    def Back_light10_page6():
                                        phy_light10_page6.destroy()
                    
                                    Back_light10_page6=Button(phy_light10_page6, bg='coral2', text='<--', command=Back_light10_page6)
                                    Back_light10_page6.pack()
                                    Back_light10_page6.place(relx=.0,rely=.0)
   
                                Light10_page6=Button(phy_light10_page5, bg='coral2', text='-->', command=light10_page6)
                                Light10_page6.pack()
                                Light10_page6.place(relx=.97,rely=.0) 
    
                            Light10_page5=Button(phy_light10_page4, bg='coral2', text='-->', command=light10_page5)
                            Light10_page5.pack()
                            Light10_page5.place(relx=.97,rely=.0) 
                        
                        Light10_page4=Button(phy_light10_page3, bg='coral2', text='-->', command=light10_page4)
                        Light10_page4.pack()
                        Light10_page4.place(relx=.97,rely=.0) 
                        
                    Light10_page3=Button(phy_light10_page2, bg='coral2', text='-->', command=light10_page3)
                    Light10_page3.pack()
                    Light10_page3.place(relx=.97,rely=.0) 
                
                    
                Light10_page2=Button(phy_light10_page1, bg='coral2', text='-->', command=light10_page2)
                Light10_page2.pack()
                Light10_page2.place(relx=.97,rely=.0) 
                
            def Back_Light10():
                phy_Light10.destroy()
            
            Light10_page1=Button(phy_Light10, bg='coral2', text='-->', command=light10_page1)
            Light10_page1.pack()
            Light10_page1.place(relx=.97,rely=.0) 
            Back_Light10=Button(phy_Light10, bg='coral2', text='<--', command=Back_Light10)
            Back_Light10.pack()
            Back_Light10.place(relx=.0,rely=.0)
                        
        Electricity=Button(phy_class10, height=1, width=11, bg='coral2', text='Electricity', font=('Castellar',27), command=Electricity)
        Magneticeffects=Button(phy_class10, height=2, width=18, bg='coral2', text='Magnetic effects of\nelectric current', font=('Castellar',27), command=Magnetic_effects_of_electric_current)
        Light10=Button(phy_class10, height=1, width=7, bg='coral2', text='Light', font=('Castellar',27), command=Light10)
        Quiz10=Button(phy_class10, height=1, width=8, bg='coral2', text='Quiz', font=('Castellar',27), command=Quiz10)
        Electricity.pack()
        Electricity.place(relx=.38,rely=.25)
        Magneticeffects.pack()
        Magneticeffects.place(relx=.32,rely=.40)
        Light10.pack()
        Light10.place(relx=.42,rely=.60)
        Quiz10.pack()
        Quiz10.place(relx=.41,rely=.75)
        
        Back_class10=Button(phy_class10, bg='coral2', text='<--', command=Back10 )
        Back_class10.pack()
        Back_class10.place(relx=.0,rely=.0)
                
    def Class11():
        phy_class11=Tk()
        phy_class11.title('Class 11')
        canvas_class11=Canvas(phy_class11, width=1500, height=900, bg='grey12')
        canvas_class11.pack(expand=YES,fill=BOTH)
        
        def Back11():
            phy_class11.destroy()
        
        def Quiz11():
            phy_Quiz11=Tk()
            phy_Quiz11.title('Quiz')
            canvas_Quiz11=Canvas(phy_Quiz11, width=1500, height=900, bg='grey12')
            canvas_Quiz11.pack(expand=YES,fill=BOTH)
            
            def play():
                import PlayQuiz11
                PlayQuiz11.PlayQuiz()
                
            play11=Button(phy_Quiz11, bg='coral2',font=('Castellar',30), text='Play Quiz', command=play)
            play11.pack()
            play11.place(relx=.40,rely=.35)
            
            def add():
                import Quiz11
                
            quiz11=Button(phy_Quiz11, bg='coral2', font=('Castellar',30),text='Add Questions', command=add)
            quiz11.pack()
            quiz11.place(relx=.36,rely=.55)
            
            def Back_Quiz11():
                phy_Quiz11.destroy()
            
            Back_Quiz11=Button(phy_Quiz11, bg='coral2', text='<--', command=Back_Quiz11)
            Back_Quiz11.pack()
            Back_Quiz11.place(relx=.0,rely=.0)
                    
        #chapters of class 11
        def Kinematics_and_laws_of_motion():
            import time
            import math

            tk=Tk()
            canvas = Canvas(tk, width = 1500, height=900, bg = 'white')
            canvas.pack(expand=YES, fill=BOTH)
            canvas.create_text(750,70,text='KINEMATICS AND LAWS OF MOTION', font=('Times New Roman',27), fill = 'black')

            def Play_Game():
                def P():
                    import tkinter as tk
                                            
                    def show_entry_fields():
                        #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
                        global v,angle
                        v=int(e1.get())
                        angle=int(e2.get())
                        
                        master.quit()
                                                
                    master = tk.Tk()
                    tk.Label(master, text="Enter Initial Velocity(m/s)").grid(row=0)
                    tk.Label(master, text="Enter Angle").grid(row=1)
                    
                
                    e1 = tk.Entry(master)
                    e2 = tk.Entry(master)
                    
                                            
                    e1.grid(row=0, column=1)
                    e2.grid(row=1,column=1)
                    
                                            
                    '''tk.Button(master, 
                              text='Quit', 
                              command=master.quit).grid(row=3, 
                                                 column=0, 
                                                 sticky=tk.W, 
                                                 pady=4)'''
                    tk.Button(master, 
                              text='Show', command=show_entry_fields).grid(row=3, 
                                                                    column=1, 
                                                                    sticky=tk.W, 
                                                                    pady=4)
                                            
                    tk.mainloop()
                P()
                global y, x 
                y=0
                x=0
                Angle = angle
                Velocity = v
                H=(Velocity**2*math.sin(math.radians(Angle)))/(2*9.8)
                t = 0.1
                a=1
                #time.sleep(0.45)
                while y<=2*H :
                    theta = math.radians( Angle)
                    x = Velocity * math.cos( theta) * t
                    
                    vy = Velocity * math.sin(theta)
                    a = t * t 
                    y = vy * t - (1.0/2 * 9.8  * a )
                    if a==1:
                        y+=20
                        
                    x += 20
                    canvas.create_oval( x+360, 500-y, x+400, 500-y+40, fill='red')
                    tk.update()
                    time.sleep(0.1)
                    canvas.create_oval(x+360, 500-y, x+400, 500-y+40, fill='white', outline='white')
                    tk.update()
                    if 500-y+40>850:
                        break
                    t += 0.5
                    a+=1
                    
            playgame=Button(tk, bg='pink', text='Projectile Motion Demonstration',font=('Castellar',20), command=Play_Game)
            playgame.pack()
            playgame.place(relx=.30,rely=.35)

            def Back_KinematicsLawsofmotion():
                tk.destroy()
            
            back_KinematicsLawsofmotion=Button(tk, bg='coral2', text='<--', command=Back_KinematicsLawsofmotion)
            back_KinematicsLawsofmotion.pack()
            back_KinematicsLawsofmotion.place(relx=.0,rely=.0)
            
            def page2_Kinematics():
                phy_page2_Kinematics=Tk()
                phy_page2_Kinematics.title('Kinematics and Law of Motion')
                canvas_page2_Kinematics=Canvas(phy_page2_Kinematics, width=1500, height=900, bg='white')
                canvas_page2_Kinematics.pack(expand=YES,fill=BOTH)
                
                canvas_page2_Kinematics.create_text(160,90,text='Motion', font=('Yu Gothic UI Semibold',24), fill = 'black')
                canvas_page2_Kinematics.create_text(430,120,text='''
                                                    Rest and Motion are relative terms, nobody can exist in a state of absolute rest or of absolute motion''', font=('Yu Gothic UI Light',18), fill = 'black')
                
                canvas_page2_Kinematics.create_text(270,230,text='One dimensional motion:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                canvas_page2_Kinematics.create_text(560,280,text='''
                                                    The motion of an object is said to be one dimensional motion if only one out of three coordinates specifying the position of the
                                                    object change with time. In such a motion an object move along a straight line path.''', font=('Yu Gothic UI Light',18), fill = 'black')
                
                canvas_page2_Kinematics.create_text(270,410,text='Two dimensional motion:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                canvas_page2_Kinematics.create_text(570,460,text='''
                                                    The motion of an object is said to be two dimensional motion if two out of three coordinates specifying the position of the object
                                                    change with time. In such motion the object moves in a plane.''', font=('Yu Gothic UI Light',18), fill = 'black')
                
                canvas_page2_Kinematics.create_text(280,600,text='Three dimensional motion:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                canvas_page2_Kinematics.create_text(560,650,text='''
                                                    The motion is said to be three dimensional motion if all the three coordinates specifying the position of an object change with 
                                                    respect to time ,in such a motion an object moves in space.''', font=('Yu Gothic UI Light',18), fill = 'black')
    
                def Back_page2_Kinematics():
                    phy_page2_Kinematics.destroy()
            
                Back_page2_Kinematics=Button(phy_page2_Kinematics, bg='coral2', text='<--', command=Back_page2_Kinematics)
                Back_page2_Kinematics.pack()
                Back_page2_Kinematics.place(relx=.0,rely=.0)
                
                def page3_Kinematics():
                    phy_page3_Kinematics=Tk()
                    phy_page3_Kinematics.title('Kinematics and Law of Motion')
                    canvas_page3_Kinematics=Canvas(phy_page3_Kinematics, width=1500, height=900, bg='white')
                    canvas_page3_Kinematics.pack(expand=YES,fill=BOTH)
                
                    canvas_page3_Kinematics.create_text(170,100,text='Path length:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                    canvas_page3_Kinematics.create_text(580,180,text='''
                                                        The path length traversed by an object between two points is not the same as the magnitude of displacement always. The displacement 
                                                        depends only on the end points; whereas the path length depends on the actual path. The two quantities are equal only if the object 
                                                        does not change its direction during the course of its motion. In all other cases, the path length is greater than the magnitude of 
                                                        displacement.''', font=('Yu Gothic UI Light',18), fill = 'black')
                    
                    canvas_page3_Kinematics.create_text(180,300,text='Displacement:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                    canvas_page3_Kinematics.create_text(520,380,text='''
                                                        A displacement is the shortest distance from the initial to the final position of a point P.
                                                        
                                                        •  The magnitude of displacement is less than or equal to the actual distance travelled by the object in the given time interval.
                                                        •  Displacement ≤ Actual distance''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                        
                    canvas_page3_Kinematics.create_text(130,500,text='Speed:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                    canvas_page3_Kinematics.create_text(260,620,text='''
                                                        It is rate of change of distance covered by the body with respect to time.
                                                        
                                                        •  Speed = Distance travelled /time taken
                                                        •  Speed is a scalar quantity .
                                                        •  Its unit is meter /sec.
                                                        •  Dimensional formula of speed is [M0L1 T -1 ] .
                                                        •  It is positive or zero but never negative.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                        
                    def Back_page3_Kinematics():
                        phy_page3_Kinematics.destroy()
                        
                    Back_page3_Kinematics=Button(phy_page3_Kinematics, bg='coral2', text='<--', command=Back_page3_Kinematics)
                    Back_page3_Kinematics.pack()
                    Back_page3_Kinematics.place(relx=.0,rely=.0)
                    
                    def page4_Kinematics():
                        global phy_page4_Kinematics
                        phy_page4_Kinematics=Toplevel()
                        phy_page4_Kinematics.title('Kinematics and Law of Motion')
                        canvas_page4_Kinematics=Canvas(phy_page4_Kinematics, width=1500, height=900, bg='white')
                        canvas_page4_Kinematics.pack(expand=YES,fill=BOTH)
                
                        canvas_page4_Kinematics.create_text(190,110,text='Average speed:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                        canvas_page4_Kinematics.create_text(510,140,text='''
                                                            The average speed of an object is greater than or equal to the magnitude of the averagevelocity over a given interval of time.''', font=('Yu Gothic UI Light',18), fill = 'black')
                        
                        canvas_page4_Kinematics.create_text(190,270,text='Uniform Speed:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                        canvas_page4_Kinematics.create_text(500,320,text='''
                                                            If an object covers equal distances in equal intervals of time than the speed of the moving object is called uniform speed. In 
                                                            this type of motion, position – time graph is always a straight line.''', font=('Yu Gothic UI Light',18), fill = 'black')
                        
                        global uniformspeed
                        uniformspeed = tkinter.PhotoImage(file="uniform speed.png")
                        button = Button(phy_page4_Kinematics, image = uniformspeed ,width=389,height=324,font=("Courier",20,"bold"),bg='#94ffe2') 
                        button.configure(image = uniformspeed)
                        button.place(relx = 0.5, rely = 0.7, anchor = CENTER)
                         
                        def Back_page4_Kinematics():
                            phy_page4_Kinematics.destroy()
                        
                        Back_page4_Kinematics=Button(phy_page4_Kinematics, bg='coral2', text='<--', command=Back_page4_Kinematics)
                        Back_page4_Kinematics.pack()
                        Back_page4_Kinematics.place(relx=.0,rely=.0)
                        
                        def page5_Kinematics():
                            phy_page5_Kinematics=Tk()
                            phy_page5_Kinematics.title('Kinematics and Law of Motion')
                            canvas_page5_Kinematics=Canvas(phy_page5_Kinematics, width=1500, height=900, bg='white')
                            canvas_page5_Kinematics.pack(expand=YES,fill=BOTH)
                
                            canvas_page5_Kinematics.create_text(240,70,text='Instantaneous speed:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                            canvas_page5_Kinematics.create_text(530,120,text='''
                                                                The speed of an object at any particular instant of time is called instantaneous speed. In this measurement, the time ∆t→0. When 
                                                                a body is moving with uniform speed its instantaneous speed = Average speed = uniform speed''', font=('Yu Gothic UI Light',18), fill = 'black')
                            
                            canvas_page5_Kinematics.create_text(160,210,text='Velocity:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                            canvas_page5_Kinematics.create_text(490,350,text='''
                                                                The rate of change of position of an object in a particular direction with respect to time is called velocity. It is equal to the 
                                                                displacement covered by an object per unit time.
                                                                •  Velocity =Displacement /Time
                                                                •  Velocity is a vector quantity
                                                                •  Its SI unit is meter per sec.
                                                                •  Its dimensional formula is [M0L1 T -1 ].
                                                                •  It may be negative, positive or zero.
                                                                •  When a body moves in a straight line then the average speed and average velocity are equal.''', font=('Yu Gothic UI Light',18), fill = 'black')
                            
                            canvas_page5_Kinematics.create_text(190,540,text='Acceleration:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                            canvas_page5_Kinematics.create_text(320,650,text='''
                                                                The rate of change of velocity of an object with respect to time is called its acceleration.
                                                                •  Acceleration = Change in velocity /time taken
                                                                •  It is a vector quantity,
                                                                •  Its SI unit is meter/ sec2
                                                                •  Its dimension is [M0L1 T -2 ].
                                                                •  It may be positive ,negative or zero.''', font=('Yu Gothic UI Light',18), fill = 'black')
                            
                            def Back_page5_Kinematics():
                                phy_page5_Kinematics.destroy()
                        
                            Back_page5_Kinematics=Button(phy_page5_Kinematics, bg='coral2', text='<--', command=Back_page5_Kinematics)
                            Back_page5_Kinematics.pack()
                            Back_page5_Kinematics.place(relx=.0,rely=.0)
                            
                            def page6_Kinematics():
                                global phy_page6_Kinematics
                                phy_page6_Kinematics=Toplevel()
                                phy_page6_Kinematics.title('Kinematics and Law of Motion')
                                canvas_page6_Kinematics=Canvas(phy_page6_Kinematics, width=1500, height=900, bg='white')
                                canvas_page6_Kinematics.pack(expand=YES,fill=BOTH)
                                
                                global acceleration
                                acceleration = tkinter.PhotoImage(file="acceleration.png")
                                button = Button(phy_page6_Kinematics, image = acceleration ,width=1004,height=700,font=("Courier",20,"bold"),bg='#94ffe2') 
                                button.configure(image = acceleration)
                                button.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                                
                                def Back_page6_Kinematics():
                                    phy_page6_Kinematics.destroy()
                        
                                Back_page6_Kinematics=Button(phy_page6_Kinematics, bg='coral2', text='<--', command=Back_page6_Kinematics)
                                Back_page6_Kinematics.pack()
                                Back_page6_Kinematics.place(relx=.0,rely=.0)
                                
                                def page7_Kinematics():
                                    phy_page7_Kinematics=Tk()
                                    phy_page7_Kinematics.title('Kinematics and Law of Motion')
                                    canvas_page7_Kinematics=Canvas(phy_page7_Kinematics, width=1500, height=900, bg='white')
                                    canvas_page7_Kinematics.pack(expand=YES,fill=BOTH)
                
                                    canvas_page7_Kinematics.create_text(180,80,text='Free fall:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                    canvas_page7_Kinematics.create_text(500,180,text='''
                                                                        In the absence of the air resistance all bodies fall with the same acceleration towards earth from a small height. This is called 
                                                                        free fall.
                                                                        
                                                                        •  The acceleration with which a body falls is called gravitational acceleration (g).
                                                                        •  Its value is 9.8 m/sec2 .''', font=('Yu Gothic UI Light',18), fill = 'black')
                                    
                                    canvas_page7_Kinematics.create_text(230,340,text='Relative Motion:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                    canvas_page7_Kinematics.create_text(500,550,text='''
                                                                        The rate of change of distance of one object with respect to the other is called relative velocity. The relative velocity of an 
                                                                        object B with respect to the object A when both are in motion is the rate of change of position of object B with respect to the 
                                                                        object A.
                                                                        
                                                                        •  Relative velocity of object A with respect to object B, 
                                                                           VAB = VA - VB
                                                                        
                                                                        •  When both objects are move in same direction, then the relative velocity of object B with respect to the object A,
                                                                           VBA = VB - VA
                                                                        
                                                                        •  When the object B moves in opposite direction of object A .
                                                                           VBA = VB + VA''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                     
                                    def Back_page7_Kinematics():
                                        phy_page7_Kinematics.destroy()
                        
                                    Back_page7_Kinematics=Button(phy_page7_Kinematics, bg='coral2', text='<--', command=Back_page7_Kinematics)
                                    Back_page7_Kinematics.pack()
                                    Back_page7_Kinematics.place(relx=.0,rely=.0)
                                    
                                    def page8_Kinematics():
                                        global phy_page8_Kinematics
                                        phy_page8_Kinematics=Toplevel()
                                        phy_page8_Kinematics.title('Kinematics and Law of Motion')
                                        canvas_page8_Kinematics=Canvas(phy_page8_Kinematics, width=1500, height=900, bg='white')
                                        canvas_page8_Kinematics.pack(expand=YES,fill=BOTH)
                                        
                                        canvas_page8_Kinematics.create_text(150,100,text='Inertia:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                        canvas_page8_Kinematics.create_text(520,160,text='''
                                                                        The property by virtue of which a body opposes any change in its state of rest or of uniform motion is known as inertia. Greater the 
                                                                        mass of the body greater is the inertia. That is mass is the measure of the inertia of the body.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                        
                                        canvas_page8_Kinematics.create_text(300,280,text='Inertia when car stops', font=('courier',12), fill = 'black')                  
                                        global inertia
                                        inertia = tkinter.PhotoImage(file="inertia.png")
                                        button = Button(phy_page8_Kinematics, image = inertia ,width=306,height=165,font=("Courier",20,"bold"),bg='#94ffe2') 
                                        button.configure(image = inertia)
                                        button.place(relx = 0.2, rely = 0.45, anchor = CENTER)
                                        
                                        canvas_page8_Kinematics.create_text(450,530,text='Physical Application of inertia or newtons’s first law:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                        canvas_page8_Kinematics.create_text(550,650,text='''
                                                                            1. When a moving bus suddenly stops, passenger’s head gets jerked in the forward direction.
                                                                            
                                                                            2. On hitting used mattress by a stick, dust particles come out of it.
                                                                            
                                                                            3. Whenever it is required to jump off a moving bus, we must always run for a short distance after jumping on road to prevent us from 
                                                                               falling in the forward direction.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                        
                                        def Back_page8_Kinematics():
                                            phy_page8_Kinematics.destroy()
                        
                                        Back_page8_Kinematics=Button(phy_page8_Kinematics, bg='coral2', text='<--', command=Back_page8_Kinematics)
                                        Back_page8_Kinematics.pack()
                                        Back_page8_Kinematics.place(relx=.0,rely=.0)
                                        
                                        def page9_Kinematics():
                                            global phy_page9_Kinematics
                                            phy_page9_Kinematics=Toplevel()
                                            phy_page9_Kinematics.title('Kinematics and Law of Motion')
                                            canvas_page9_Kinematics=Canvas(phy_page9_Kinematics, width=1500, height=900, bg='white')
                                            canvas_page9_Kinematics.pack(expand=YES,fill=BOTH)
                                            
                                            canvas_page9_Kinematics.create_text(330,80,text='Newton’s Second law of motion', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                            canvas_page9_Kinematics.create_text(500,150,text='''
                                                                                It states that the rate of change of momentum of a body is proportional to the applied force and takes place in the direction in which 
                                                                                force acts. Thus F= k dp/dt= k ma''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                            
                                            canvas_page9_Kinematics.create_text(750,720,text='Derivative of second law of motion', font=('courier',16), fill = 'black')                  
                                            global derivativeofsecondlaw
                                            derivativeofsecondlaw = tkinter.PhotoImage(file="derivative of second law.png")
                                            button = Button(phy_page9_Kinematics, image = derivativeofsecondlaw ,width=407,height=434,font=("Courier",20,"bold"),bg='#94ffe2') 
                                            button.configure(image = derivativeofsecondlaw)
                                            button.place(relx = 0.5, rely = 0.55, anchor = CENTER)
                                            
                                            def Back_page9_Kinematics():
                                                phy_page9_Kinematics.destroy()
                        
                                            Back_page9_Kinematics=Button(phy_page9_Kinematics, bg='coral2', text='<--', command=Back_page9_Kinematics)
                                            Back_page9_Kinematics.pack()
                                            Back_page9_Kinematics.place(relx=.0,rely=.0)
                                            
                                            def page10_Kinematics():
                                                global phy_page10_Kinematics
                                                phy_page10_Kinematics=Toplevel()
                                                phy_page10_Kinematics.title('Kinematics and Law of Motion')
                                                canvas_page10_Kinematics=Canvas(phy_page10_Kinematics, width=1500, height=900, bg='white')
                                                canvas_page10_Kinematics.pack(expand=YES,fill=BOTH)
                
                                                canvas_page10_Kinematics.create_text(460,170,text='''
                                                                                     •  It is applicable to a particle, and also to a body or a system of particles, provided F the total external force on the system 
                                                                                        and a is the acceleration of the system as a whole.
                                                                                     
                                                                                     •  Force is not always in the direction of motion .Depending on the situation F may be along V, opposite to v, normal to v, or may 
                                                                                        make some other angle with v. In every case it is parallel to acceleration.
                                                                                     
                                                                                     •  If v=0 at an instant, i.e., if a body is momentarily at rest, it does not mean that force or acceleration are necessarily zero 
                                                                                        at that instant. For ex: When a ball thrown upward reaches its maximum height, but the force continues to be its weight ‘mg‘ and
                                                                                        the acceleration is ‘g’ the acceleration due to gravity.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                
                                                canvas_page10_Kinematics.create_text(250,380,text='Numerical Application:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                canvas_page10_Kinematics.create_text(170,420,text='''
                                                                                     acceleration, a = FNet / M
                                                                                     where FNet is the vector resultant of all the forces acting on the body''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                
                                                global numericalapplication
                                                numericalapplication = tkinter.PhotoImage(file="numerical application.png")
                                                button = Button(phy_page10_Kinematics, image = numericalapplication ,width=407,height=272,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                button.configure(image = numericalapplication)
                                                button.place(relx = 0.5, rely = 0.75, anchor = CENTER)
                                            
                                                def Back_page10_Kinematics():
                                                    phy_page10_Kinematics.destroy()
                                                    
                                                Back_page10_Kinematics=Button(phy_page10_Kinematics, bg='coral2', text='<--', command=Back_page10_Kinematics)
                                                Back_page10_Kinematics.pack()
                                                Back_page10_Kinematics.place(relx=.0,rely=.0)
                                                
                                                def page11_Kinematics():
                                                    phy_page11_Kinematics=Tk()
                                                    phy_page11_Kinematics.title('Kinematics and Law of Motion')
                                                    canvas_page11_Kinematics=Canvas(phy_page11_Kinematics, width=1500, height=900, bg='white')
                                                    canvas_page11_Kinematics.pack(expand=YES,fill=BOTH)
                
                                                    canvas_page11_Kinematics.create_text(240,70,text='Physical Application:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                    canvas_page11_Kinematics.create_text(380,330,text='''
                                                                                         i) Body kept on horizontal plane is at rest.
                                                                                            For vertical direction
                                                                                            N = mg(since body is at rest)
                                                                                        
                                                                                        ii) Body kept on horizontal plane is accelerating horizontally under single horizontal force.
                                                                                            For vertical direction
                                                                                            N = mg (since body is at rest)
                                                                                            For horizontal direction
                                                                                            F = ma
                                                                                       
                                                                                       iii) Body kept on horizontal plane is accelerating horizontally towards right under two horizontal forces. (F1> F2)
                                                                                            For vertical direction
                                                                                            N = mg (since body is at rest)
                                                                                            For horizontal direction 
                                                                                            F1 - F2= ma''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                            
                                                    canvas_page11_Kinematics.create_text(160,640,text='Tension', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                    canvas_page11_Kinematics.create_text(430,700,text='''
                                                                                         Tension In A Light String Force applied by any linear object such as string, rope, chain, rod etc. is known as it’s tension. Since 
                                                                                         string is a highly flexible object so it can only pull the object and can never push. Hence tension of the string always acts away 
                                                                                         from the body to which it is attached irrespective of the direction.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                    def Back_page11_Kinematics():
                                                        phy_page11_Kinematics.destroy()
                        
                                                    Back_page11_Kinematics=Button(phy_page11_Kinematics, bg='coral2', text='<--', command=Back_page11_Kinematics)
                                                    Back_page11_Kinematics.pack()
                                                    Back_page11_Kinematics.place(relx=.0,rely=.0)
                                                    
                                                    def page12_Kinematics():
                                                        global phy_page12_Kinematics
                                                        phy_page12_Kinematics=Toplevel()
                                                        phy_page12_Kinematics.title('Kinematics and Law of Motion')
                                                        canvas_page12_Kinematics=Canvas(phy_page12_Kinematics, width=1500, height=900, bg='white')
                                                        canvas_page12_Kinematics.pack(expand=YES,fill=BOTH)
                                                        
                                                        global tension
                                                        tension = tkinter.PhotoImage(file="tension.png")
                                                        button = Button(phy_page12_Kinematics, image = tension ,width=886,height=378,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                        button.configure(image =tension)
                                                        button.place(relx = 0.5, rely = 0.3, anchor = CENTER)
                                                        
                                                        canvas_page12_Kinematics.create_text(300,550,text='Physical Application of Tension:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                        canvas_page12_Kinematics.create_text(400,650,text='''
                                                                                             i) Rope holding the bucket in the well pulls the bucket in the upward direction and the pulley in the downward direction.
                                                                                            
                                                                                            ii) When a block is pulled by the chain, the chain pulls the block in forward direction and the person holding the chain in 
                                                                                                reverse direction. In case of light string, rope, chain, rod etc. tension is same all along their lengths.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                            
                                                        def Back_page12_Kinematics():
                                                            phy_page12_Kinematics.destroy()
                        
                                                        Back_page12_Kinematics=Button(phy_page12_Kinematics, bg='coral2', text='<--', command=Back_page12_Kinematics)
                                                        Back_page12_Kinematics.pack()
                                                        Back_page12_Kinematics.place(relx=.0,rely=.0)
                                                        
                                                        def page13_Kinematics():
                                                            global phy_page13_Kinematics
                                                            phy_page13_Kinematics=Toplevel()
                                                            phy_page13_Kinematics.title('Kinematics and Law of Motion')
                                                            canvas_page13_Kinematics=Canvas(phy_page13_Kinematics, width=1500, height=900, bg='white')
                                                            canvas_page13_Kinematics.pack(expand=YES,fill=BOTH)
                                                            
                                                            canvas_page13_Kinematics.create_text(270,100,text='Tension of A light Rigid Rod:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                            canvas_page13_Kinematics.create_text(400,330,text='''
                                                                                                 Force applied by rod is also known as its tension. Since rod is rigid, it cannot bend like string. Hence rod can pull as well as
                                                                                                 push. Tension of rod can be of pulling as well as pushing nature but one at a time. Tension of a rod attached to the body may be 
                                                                                                 directed towards as well as away from the body.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                            
                                                            global tensionrod
                                                            tensionrod = tkinter.PhotoImage(file="tensionrod.png")
                                                            button = Button(phy_page13_Kinematics, image = tensionrod ,width=540,height=83,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                            button.configure(image =tensionrod)
                                                            button.place(relx = 0.5, rely = 0.25, anchor = CENTER)
                                                            
                                                            canvas_page13_Kinematics.create_text(280,460,text='Physical Application of tension:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                            canvas_page13_Kinematics.create_text(400,600,text='''
                                                                                                 i) Pillars supporting the house pushes the house in the upward direction and pushes the ground in the downward direction.
                                                                                                
                                                                                                ii) Rod holding the ceiling fan pulls the fan in the upward direction and pulls the hook attached to the ceiling in the downward 
                                                                                                    direction.
                                                            
                                                                                               iii) Parallel rods attached between the cart and the bull pulls the cart in the forward direction and pulls the bull in the backward 
                                                                                                    direction''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                            
                                                            def Back_page13_Kinematics():
                                                                phy_page13_Kinematics.destroy()
                                                                
                                                            Back_page13_Kinematics=Button(phy_page13_Kinematics, bg='coral2', text='<--', command=Back_page13_Kinematics)
                                                            Back_page13_Kinematics.pack()
                                                            Back_page13_Kinematics.place(relx=.0,rely=.0)
                                                            
                                                            def page14_Kinematics():
                                                                global phy_page14_Kinematics
                                                                phy_page14_Kinematics=Toplevel()
                                                                phy_page14_Kinematics.title('Kinematics and Law of Motion')
                                                                canvas_page14_Kinematics=Canvas(phy_page14_Kinematics, width=1500, height=900, bg='white')
                                                                canvas_page14_Kinematics.pack(expand=YES,fill=BOTH)
                                                                
                                                                canvas_page14_Kinematics.create_text(160,120,text='Fixed Pulley:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                canvas_page14_Kinematics.create_text(340,170,text='''
                                                                                                    It is a simple machine in the form of a circular disc or rim supported by spokes having groove at its periphery. It is free to 
                                                                                                    rotate about an axis passing through its center and perpendicular to its plane.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                                canvas_page14_Kinematics.create_text(150,300,text='Key Point:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                canvas_page14_Kinematics.create_text(350,330,text='''
                                                                                                    In case of light pulley, tension in the rope on both the sides of the pulley is same (to be proved in the rotational mechanics)''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                
                                                                global keypoint
                                                                keypoint = tkinter.PhotoImage(file="keypoint.png")
                                                                button = Button(phy_page14_Kinematics, image = keypoint ,width=498,height=316,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                button.configure(image = keypoint)
                                                                button.place(relx = 0.5, rely = 0.7, anchor = CENTER)

                                                                def Back_page14_Kinematics():
                                                                    phy_page14_Kinematics.destroy()
                                                                    
                                                                Back_page14_Kinematics=Button(phy_page14_Kinematics, bg='coral2', text='<--', command=Back_page14_Kinematics)
                                                                Back_page14_Kinematics.pack()
                                                                Back_page14_Kinematics.place(relx=.0,rely=.0)
                                                                
                                                                def page15_Kinematics():
                                                                    global phy_page15_Kinematics
                                                                    phy_page15_Kinematics=Toplevel()
                                                                    phy_page15_Kinematics.title('Kinematics and Law of Motion')
                                                                    canvas_page15_Kinematics=Canvas(phy_page15_Kinematics, width=1500, height=900, bg='white')
                                                                    canvas_page15_Kinematics.pack(expand=YES,fill=BOTH)
                                                                
                                                                    canvas_page15_Kinematics.create_text(440,100,text='Newton’s 3rd law or Law of Action and Reaction', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                    canvas_page15_Kinematics.create_text(30,170,text='''
                                                                                                         Every action is opposed by an equal and opposite reaction.
                                                                                                                                     or
                                                                                                         For every action there is an equal and opposite reaction''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                    
                                                                    global thirdlaw
                                                                    thirdlaw = tkinter.PhotoImage(file="third law.png")
                                                                    button = Button(phy_page15_Kinematics, image = thirdlaw ,width=384,height=75,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                    button.configure(image = thirdlaw)
                                                                    button.place(relx = 0.3, rely = 0.35, anchor = CENTER)
                                                                    
                                                                    canvas_page15_Kinematics.create_text(80,380,text='''
                                                                                                         F12 is the force on the first body (m1 ) due to second body (m2 )
                                                                                                         F21 is the force on the second body (m2) due to first body (m1)
                                                                                                         If F12 is action then F21 reaction and if F21 is action then F12 reaction.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                    
                                                                    canvas_page15_Kinematics.create_text(240,480,text='Numerical Application:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                    canvas_page15_Kinematics.create_text(370,530,text='''
                                                                                                         Force on the first body due to second body (F12 ) is equal and opposite to the force on the second body due to first body (F21 ).
                                                                                                                                                                 F21 = - F12''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                    canvas_page15_Kinematics.create_text(230,600,text='Physical Application:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                    canvas_page15_Kinematics.create_text(390,680,text='''
                                                                                                         i) Earth pulls the body on its surface in vertically downward direction and the body pulls the earth with the same force in 
                                                                                                            vertically  upward direction.
                                                                                                        ii) While walking we push the ground in the backward direction using static frictional force and the ground pushes us in the 
                                                                                                            forward direction using static frictional force.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                    
                                                                    def Back_page15_Kinematics():
                                                                        phy_page15_Kinematics.destroy()
                                                                    
                                                                    Back_page15_Kinematics=Button(phy_page15_Kinematics, bg='coral2', text='<--', command=Back_page15_Kinematics)
                                                                    Back_page15_Kinematics.pack()
                                                                    Back_page15_Kinematics.place(relx=.0,rely=.0)
                                                                    
                                                                    def page16_Kinematics():
                                                                        global phy_page16_Kinematics
                                                                        phy_page16_Kinematics=Toplevel()
                                                                        phy_page16_Kinematics.title('Kinematics and Law of Motion')
                                                                        canvas_page16_Kinematics=Canvas(phy_page16_Kinematics, width=1500, height=900, bg='white')
                                                                        canvas_page16_Kinematics.pack(expand=YES,fill=BOTH)
                                                                
                                                                        canvas_page16_Kinematics.create_text(220,70,text='Linear Momentum', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                        canvas_page16_Kinematics.create_text(330,160,text='''
                                                                                                             It is defined as the quantity of motion contained in the body. Mathematically it is given by the product of mass and velocity. 
                                                                                                             It is a vector quantity represented by p.
                                                                                                             
                                                                                                             p = mv''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                                        canvas_page16_Kinematics.create_text(400,300,text='Principle Of Conservation Of Linear Momentum:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                        canvas_page16_Kinematics.create_text(370,330,text='''
                                                                                                             It states that in the absence of any external applied force total momentum of a system remains conserved. Proof- We know that,''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                        
                                                                        global momentum
                                                                        momentum = tkinter.PhotoImage(file="momentum.png")
                                                                        button = Button(phy_page16_Kinematics, image = momentum ,width=523,height=333,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                        button.configure(image = momentum)
                                                                        button.place(relx = 0.5, rely = 0.7, anchor = CENTER)
                                                                
                                                                        def Back_page16_Kinematics():
                                                                            phy_page16_Kinematics.destroy()
                                                                    
                                                                        Back_page16_Kinematics=Button(phy_page16_Kinematics, bg='coral2', text='<--', command=Back_page16_Kinematics)
                                                                        Back_page16_Kinematics.pack()
                                                                        Back_page16_Kinematics.place(relx=.0,rely=.0)
                                                                        
                                                                        def page17_Kinematics():
                                                                            global phy_page17_Kinematics
                                                                            phy_page17_Kinematics=Toplevel()
                                                                            phy_page17_Kinematics.title('Kinematics and Law of Motion')
                                                                            canvas_page17_Kinematics=Canvas(phy_page17_Kinematics, width=1500, height=900, bg='white')
                                                                            canvas_page17_Kinematics.pack(expand=YES,fill=BOTH)
                                                                
                                                                            canvas_page17_Kinematics.create_text(470,80,text='Physical Application of law of conservation of momentum:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                            canvas_page17_Kinematics.create_text(340,170,text='''
                                                                                                                 i) Recoil of gun – when bullet is fired in the forward direction gun recoils in the backward direction.
                                                                                                            
                                                                                                                ii) In rocket propulsion fuel is ejected out in the downward direction due to which rocket is propelled up in vertically upward
                                                                                                                    direction.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                                                                                        
                                                                            global recoil
                                                                            recoil = tkinter.PhotoImage(file="recoil.png")
                                                                            button = Button(phy_page17_Kinematics, image = recoil ,width=371,height=194,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                            button.configure(image = recoil)
                                                                            button.place(relx = 0.5, rely = 0.42, anchor = CENTER)
                                                                            
                                                                            canvas_page17_Kinematics.create_text(470,500,text='Physical Application of law of conservation of momentum:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                            canvas_page17_Kinematics.create_text(270,650,text='''
                                                                                                                 Let mass of gun be mg and that of bullet be m . Initially both are at rest, hence their initial momentum is zero.
                                                                                                                 pi = mgug + mbub = 0
                                                                                                                 
                                                                                                                 Finally when bullet rushes out with velocity vg, gun recoils with velocity vb, hence their final momentum is
                                                                                                                 pf = mgvg + mb vb
                                                                                                                 
                                                                                                                 Since there is no external applied force, from the principal of conservation of linear momentum
                                                                                                                 pi = pf''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                                            def Back_page17_Kinematics():
                                                                                phy_page17_Kinematics.destroy()
                                                                    
                                                                            Back_page17_Kinematics=Button(phy_page17_Kinematics, bg='coral2', text='<--', command=Back_page17_Kinematics)
                                                                            Back_page17_Kinematics.pack()
                                                                            Back_page17_Kinematics.place(relx=.0,rely=.0)
                                                                            
                                                                            def page18_Kinematics():
                                                                                global phy_page18_Kinematics
                                                                                phy_page18_Kinematics=Toplevel()
                                                                                phy_page18_Kinematics.title('Kinematics and Law of Motion')
                                                                                canvas_page18_Kinematics=Canvas(phy_page18_Kinematics, width=1500, height=900, bg='white')
                                                                                canvas_page18_Kinematics.pack(expand=YES,fill=BOTH)
                                                                                
                                                                                global recoilformula
                                                                                recoilformula = tkinter.PhotoImage(file="recoilformula.png")
                                                                                button = Button(phy_page18_Kinematics, image = recoilformula ,width=238,height=98,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                                button.configure(image = recoilformula)
                                                                                button.place(relx = 0.5, rely = 0.1, anchor = CENTER)

                                                                                canvas_page18_Kinematics.create_text(150,200,text='''
                                                                                                                     From above expression it must be clear that
                                                                                                                        1. Gun recoils opposite to the direction of motion of bullet.
                                                                                                                        2. Greater is the mass of mullet mb or velocity of bullet vb greater is the recoil of the gun.
                                                                                                                        3. Greater is the mass of gun mg , smaller is the recoil of gun.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                                        
                                                                                canvas_page18_Kinematics.create_text(300,320,text='Impulse and Impulsive Force', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                                canvas_page18_Kinematics.create_text(200,380,text='Impulsive Force:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                canvas_page18_Kinematics.create_text(290,470,text='''
                                                                                                                     The force which acts on a body for very short duration of time but is still capable of changing the position, velocity and 
                                                                                                                     direction of motion of the body up to large extent is known as impulsive force.
                                                                                                                     Example -
                                                                                                                     1. Force applied by foot on hitting a football.
                                                                                                                     2. Force applied by boxer on a punching bag.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                                                canvas_page18_Kinematics.create_text(150,620,text='Impulse:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                canvas_page18_Kinematics.create_text(330,680,text='''
                                                                                                                     Impulse received by the body during an impact is defined as the product of average impulsive force and the short time duration 
                                                                                                                     for which it acts.
                                                                                                                     I = Favg× t''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                                                def Back_page18_Kinematics():
                                                                                    phy_page18_Kinematics.destroy()
                                                                    
                                                                                Back_page18_Kinematics=Button(phy_page18_Kinematics, bg='coral2', text='<--', command=Back_page18_Kinematics)
                                                                                Back_page18_Kinematics.pack()
                                                                                Back_page18_Kinematics.place(relx=.0,rely=.0)
                                                                                
                                                                                def page19_Kinematics():
                                                                                    global phy_page19_Kinematics
                                                                                    phy_page19_Kinematics=Toplevel()
                                                                                    phy_page19_Kinematics.title('Kinematics and Law of Motion')
                                                                                    canvas_page19_Kinematics=Canvas(phy_page19_Kinematics, width=1500, height=900, bg='white')
                                                                                    canvas_page19_Kinematics.pack(expand=YES,fill=BOTH)
                                                                
                                                                                    canvas_page19_Kinematics.create_text(430,130,text='Relation Between Impulse and Linear Momentum:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                    canvas_page19_Kinematics.create_text(330,180,text='''
                                                                                                                         Consider a body being acted upon by an impulsive force, this force changes its magnitude rapidly with the time. At any instant if
                                                                                                                         impulsive force is F then elementary impulse imparted to the body in the elementary time dt is given by''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                    
                                                                                    global impulse
                                                                                    impulse = tkinter.PhotoImage(file="impulse.png")
                                                                                    button = Button(phy_page19_Kinematics, image = impulse ,width=441,height=353,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                                    button.configure(image = impulse)
                                                                                    button.place(relx = 0.5, rely = 0.6, anchor = CENTER)

                                                                                    def Back_page19_Kinematics():
                                                                                        phy_page19_Kinematics.destroy()
                                                                                        
                                                                                    Back_page19_Kinematics=Button(phy_page19_Kinematics, bg='coral2', text='<--', command=Back_page19_Kinematics)
                                                                                    Back_page19_Kinematics.pack()
                                                                                    Back_page19_Kinematics.place(relx=.0,rely=.0)
                                                                                    
                                                                                    def page20_Kinematics():
                                                                                        phy_page20_Kinematics=Tk()
                                                                                        phy_page20_Kinematics.title('Kinematics and Law of Motion')
                                                                                        canvas_page20_Kinematics=Canvas(phy_page20_Kinematics, width=1500, height=900, bg='white')
                                                                                        canvas_page20_Kinematics.pack(expand=YES,fill=BOTH)
                                                                
                                                                                        canvas_page20_Kinematics.create_text(150,100,text='FRICTION', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                                                                        canvas_page20_Kinematics.create_text(230,140,text='''
                                                                                                                             The property by virtue of which the relative motion between two surfaces in contact is opposed is known as friction.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                        
                                                                                        canvas_page20_Kinematics.create_text(180,270,text='Frictional Force:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                        canvas_page20_Kinematics.create_text(240,320,text='''
                                                                                                                             Tangential forces developed between the two surfaces in contact, so as to oppose their relative motion are known as 
                                                                                                                             frictional forces or commonly friction.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                        
                                                                                        canvas_page20_Kinematics.create_text(250,450,text='Types of Frictional Forces:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                        canvas_page20_Kinematics.create_text(-170,580,text='''
                                                                                                                             Frictional forces are of three types :-

                                                                                                                                1. Static frictional force
                                                                                                                                
                                                                                                                                2. Kinetic frictional force
                                                                                                                                
                                                                                                                                3. Rolling frictional force''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                        
                                                                                        def Back_page20_Kinematics():
                                                                                            phy_page20_Kinematics.destroy()
                                                                                        
                                                                                        Back_page20_Kinematics=Button(phy_page20_Kinematics, bg='coral2', text='<--', command=Back_page20_Kinematics)
                                                                                        Back_page20_Kinematics.pack()
                                                                                        Back_page20_Kinematics.place(relx=.0,rely=.0)
                                                                                        
                                                                                        def page21_Kinematics():
                                                                                            global phy_page21_Kinematics
                                                                                            phy_page21_Kinematics=Toplevel()
                                                                                            phy_page21_Kinematics.title('Kinematics and Law of Motion')
                                                                                            canvas_page21_Kinematics=Canvas(phy_page21_Kinematics, width=1500, height=900, bg='white')
                                                                                            canvas_page21_Kinematics.pack(expand=YES,fill=BOTH)
                                                                                            
                                                                                            canvas_page21_Kinematics.create_text(250,60,text='Static Frictional Force:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                            canvas_page21_Kinematics.create_text(270,120,text='''
                                                                                                                                 Frictional force acting between the two surfaces in contact which are relatively at rest, so as to oppose their relative
                                                                                                                                 motion, when they tend to move relatively under the effect of any external force is known as static frictional force. 
                                                                                                                                 Static frictional force is a self adjusting force and its value lies between its minimum value up to its maximum value.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                           
                                                                                            global staticfriction
                                                                                            staticfriction = tkinter.PhotoImage(file="static friction.png")
                                                                                            button = Button(phy_page21_Kinematics, image = staticfriction ,width=1000,height=562,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                                            button.configure(image = staticfriction)
                                                                                            button.place(relx = 0.5, rely = 0.6, anchor = CENTER)
                                                                                            
                                                                                            def Back_page21_Kinematics():
                                                                                                phy_page21_Kinematics.destroy()
                                                                                        
                                                                                            Back_page21_Kinematics=Button(phy_page21_Kinematics, bg='coral2', text='<--', command=Back_page21_Kinematics)
                                                                                            Back_page21_Kinematics.pack()
                                                                                            Back_page21_Kinematics.place(relx=.0,rely=.0)
                                                                                            
                                                                                            def page22_Kinematics():
                                                                                                global phy_page22_Kinematics
                                                                                                phy_page22_Kinematics=Toplevel()
                                                                                                phy_page22_Kinematics.title('Kinematics and Law of Motion')
                                                                                                canvas_page22_Kinematics=Canvas(phy_page22_Kinematics, width=1500, height=900, bg='white')
                                                                                                canvas_page22_Kinematics.pack(expand=YES,fill=BOTH)
                                                                                            
                                                                                                canvas_page22_Kinematics.create_text(250,80,text='Kinetic  Frictional  Force:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                                canvas_page22_Kinematics.create_text(250,220,text='''
                                                                                                                                     Frictional  force  acting  between  the  two  surfaces  in contact which are moving relatively, so as to oppose their relative
                                                                                                                                     motion, is known as kinetic frictional force. It’s magnitude is almost constant and is equal to µkN where µk is the coefficient 
                                                                                                                                     of kinetic friction for the given pair of surface and N is the normal reaction acting between the two surfaces in contact. It is 
                                                                                                                                     always less than maximum value of static frictional force.
                                                                                                                                     fk = µkN Since,
                                                                                                                                     fk < fs(max) = µsN
                                                                                                                                     Therefore, µkN < µsN
                                                                                                                                     or, µk < µs''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                                
                                                                                                canvas_page22_Kinematics.create_text(240,420,text='Rolling Frictional Force:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                                canvas_page22_Kinematics.create_text(270,480,text='''
                                                                                                                                     Frictional force which opposes the rolling of bodies (like cylinder, sphere, ring etc.) over any surface is called rolling frictional 
                                                                                                                                     force. Rolling frictional force acting between any rolling body and the surface is almost constant and is given by µr N. Where µ is 
                                                                                                                                     coefficient of rolling friction and N is the normal reaction between the rolling body and the surface. ''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                                
                                                                                                global rollingfriction
                                                                                                rollingfriction = tkinter.PhotoImage(file="rolling friction.png")
                                                                                                button = Button(phy_page22_Kinematics, image = rollingfriction ,width=420,height=182,font=("Courier",20,"bold"),bg='#94ffe2') 
                                                                                                button.configure(image = rollingfriction)
                                                                                                button.place(relx = 0.5, rely = 0.8, anchor = CENTER)
                                                                                            
                                                                                                def Back_page22_Kinematics():
                                                                                                    phy_page22_Kinematics.destroy()
                                                                                        
                                                                                                Back_page22_Kinematics=Button(phy_page22_Kinematics, bg='coral2', text='<--', command=Back_page22_Kinematics)
                                                                                                Back_page22_Kinematics.pack()
                                                                                                Back_page22_Kinematics.place(relx=.0,rely=.0)
                                                                                                
                                                                                                def page23_Kinematics():
                                                                                                    phy_page23_Kinematics=Tk()
                                                                                                    phy_page23_Kinematics.title('Kinematics and Law of Motion')
                                                                                                    canvas_page23_Kinematics=Canvas(phy_page23_Kinematics, width=1500, height=900, bg='white')
                                                                                                    canvas_page23_Kinematics.pack(expand=YES,fill=BOTH)
                                                                                                    
                                                                                                    canvas_page23_Kinematics.create_text(230,120,text='''
                                                                                                                                         Although frictional force is a non-conservative force and causes lots of wastage of energy in the form of heat yet it is very 
                                                                                                                                         useful to us in many ways. That is why it is considered as a necessary evil.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                                    
                                                                                                    canvas_page23_Kinematics.create_text(250,250,text='Advantages of Friction:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                                    canvas_page23_Kinematics.create_text(280,360,text='''
                                                                                                                                         i) Friction is necessary in walking. Without friction it would have been impossible for us to walk.
                                                                                                                        
                                                                                                                                        ii) Friction is necessary for the movement of vehicles on the road. It is the static frictional force which makes the acceleration 
                                                                                                                                            and retardation of vehicles possible on the road.
                                                                                                    
                                                                                                                                       iii) We are able to hold anything with our hands by the help of friction only.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                                    
                                                                                                    canvas_page23_Kinematics.create_text(270,550,text='Disadvantages of Friction:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                                    canvas_page23_Kinematics.create_text(210,650,text='''
                                                                                                                                         i) Friction causes wear and tear in the machinery parts.

                                                                                                                                        ii) Kinetic friction wastes energy in the form of heat, light and sound.
                                                                                                    
                                                                                                                                       iii) A part of fuel energy is consumed in overcoming the friction operating within the various parts of machinery.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                                                                    def Back_page23_Kinematics():
                                                                                                        phy_page23_Kinematics.destroy()
                                                                                        
                                                                                                    Back_page23_Kinematics=Button(phy_page23_Kinematics, bg='coral2', text='<--', command=Back_page23_Kinematics)
                                                                                                    Back_page23_Kinematics.pack()
                                                                                                    Back_page23_Kinematics.place(relx=.0,rely=.0)
                                                                                                    
                                                                                                    def page24_Kinematics():
                                                                                                        phy_page24_Kinematics=Tk()
                                                                                                        phy_page24_Kinematics.title('Kinematics and Law of Motion')
                                                                                                        canvas_page24_Kinematics=Canvas(phy_page24_Kinematics, width=1500, height=900, bg='white')
                                                                                                        canvas_page24_Kinematics.pack(expand=YES,fill=BOTH)
                                                                                                    
                                                                                                        canvas_page24_Kinematics.create_text(270,100,text='Methods to Reduce Friction:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                                        canvas_page24_Kinematics.create_text(250,250,text='''
                                                                                                                                             i) By polishing – Polishing makes the surface smooth by filling the space between the depressions and projections present in the
                                                                                                                                                surface of the bodies at microscopic level and there by reduces friction.
                                                                                                        
                                                                                                                                            ii) By proper selection of material – Since friction depends upon the nature of material used hence it can be largely reduced by 
                                                                                                                                                proper selection of materials.
                                                                                            
                                                                                                                                           iii) By lubricating – When oil or grease is placed between the two surfaces in contact, it prevents the surface from coming in actual 
                                                                                                                                                contact with each other. This converts solid friction into liquid friction which is very small.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                                                                        canvas_page24_Kinematics.create_text(200,480,text='Banking of Roads:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                                                        canvas_page24_Kinematics.create_text(260,580,text='''
                                                                                                                                             In case of horizontal road necessary centripetal force mv2/r is provided by static frictional force. When heavy vehicles move with 
                                                                                                                                             high speed on a sharp turn (small radius) then all the factors contribute to huge centripetal force which if provided by the static 
                                                                                                                                             frictional force may result in the fatal accident. To prevent this roads are banked by lifting their outer edge.Due to this, normal 
                                                                                                                                             reaction of road on the vehicle gets tilted inwards such that it’s vertical component balances the weight of the body and the horizontal
                                                                                                                                             component provides the necessary centripetal force.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                                                                        def Back_page24_Kinematics():
                                                                                                            phy_page24_Kinematics.destroy()
                                                                                        
                                                                                                        Back_page24_Kinematics=Button(phy_page24_Kinematics, bg='coral2', text='<--', command=Back_page24_Kinematics)
                                                                                                        Back_page24_Kinematics.pack()
                                                                                                        Back_page24_Kinematics.place(relx=.0,rely=.0)
                                                                                                        
                                                                                                        def Back_to_class11_Kinematics():
                                                                                                                tk.destroy()
                                                                                                                phy_page2_Kinematics.destroy()
                                                                                                                phy_page3_Kinematics.destroy()
                                                                                                                phy_page4_Kinematics.destroy()
                                                                                                                phy_page5_Kinematics.destroy()
                                                                                                                phy_page6_Kinematics.destroy()
                                                                                                                phy_page7_Kinematics.destroy()
                                                                                                                phy_page8_Kinematics.destroy()
                                                                                                                phy_page9_Kinematics.destroy()
                                                                                                                phy_page10_Kinematics.destroy()
                                                                                                                phy_page11_Kinematics.destroy()
                                                                                                                phy_page12_Kinematics.destroy()
                                                                                                                phy_page13_Kinematics.destroy()
                                                                                                                phy_page14_Kinematics.destroy()
                                                                                                                phy_page15_Kinematics.destroy()
                                                                                                                phy_page16_Kinematics.destroy()
                                                                                                                phy_page17_Kinematics.destroy()
                                                                                                                phy_page18_Kinematics.destroy()
                                                                                                                phy_page19_Kinematics.destroy()
                                                                                                                phy_page20_Kinematics.destroy()
                                                                                                                phy_page21_Kinematics.destroy()
                                                                                                                phy_page22_Kinematics.destroy()
                                                                                                                phy_page23_Kinematics.destroy()
                                                                                                                phy_page24_Kinematics.destroy()
                                                                                                                
                                                                                                        Back_to_class11_Kinematics= Button(phy_page24_Kinematics,bg='coral2', text='Class 11',font=('Castellar',18), command=Back_to_class11_Kinematics)
                                                                                                        Back_to_class11_Kinematics.pack()
                                                                                                        Back_to_class11_Kinematics.place(relx=.87,rely=.85)
                                                                                                       
                                                                                                    page24_Kinematics=Button(phy_page23_Kinematics, bg='coral2', text='-->', command=page24_Kinematics)
                                                                                                    page24_Kinematics.pack()
                                                                                                    page24_Kinematics.place(relx=.98,rely=.0)
                                                                                        
                                                                                                page23_Kinematics=Button(phy_page22_Kinematics, bg='coral2', text='-->', command=page23_Kinematics)
                                                                                                page23_Kinematics.pack()
                                                                                                page23_Kinematics.place(relx=.98,rely=.0)
                                                                                        
                                                                                            page22_Kinematics=Button(phy_page21_Kinematics, bg='coral2', text='-->', command=page22_Kinematics)
                                                                                            page22_Kinematics.pack()
                                                                                            page22_Kinematics.place(relx=.98,rely=.0)
                                                                                        
                                                                                        page21_Kinematics=Button(phy_page20_Kinematics, bg='coral2', text='-->', command=page21_Kinematics)
                                                                                        page21_Kinematics.pack()
                                                                                        page21_Kinematics.place(relx=.98,rely=.0)
                                                                                        
                                                                                    page20_Kinematics=Button(phy_page19_Kinematics, bg='coral2', text='-->', command=page20_Kinematics)
                                                                                    page20_Kinematics.pack()
                                                                                    page20_Kinematics.place(relx=.98,rely=.0)
                                                                
                                                                                page19_Kinematics=Button(phy_page18_Kinematics, bg='coral2', text='-->', command=page19_Kinematics)
                                                                                page19_Kinematics.pack()
                                                                                page19_Kinematics.place(relx=.98,rely=.0)
                                                                
                                                                            page18_Kinematics=Button(phy_page17_Kinematics, bg='coral2', text='-->', command=page18_Kinematics)
                                                                            page18_Kinematics.pack()
                                                                            page18_Kinematics.place(relx=.98,rely=.0)
                                                                
                                                                        page17_Kinematics=Button(phy_page16_Kinematics, bg='coral2', text='-->', command=page17_Kinematics)
                                                                        page17_Kinematics.pack()
                                                                        page17_Kinematics.place(relx=.98,rely=.0)
                                                                
                                                                    page16_Kinematics=Button(phy_page15_Kinematics, bg='coral2', text='-->', command=page16_Kinematics)
                                                                    page16_Kinematics.pack()
                                                                    page16_Kinematics.place(relx=.98,rely=.0)
                                                                    
                                                                page15_Kinematics=Button(phy_page14_Kinematics, bg='coral2', text='-->', command=page15_Kinematics)
                                                                page15_Kinematics.pack()
                                                                page15_Kinematics.place(relx=.98,rely=.0)
                                                                
                                                            page14_Kinematics=Button(phy_page13_Kinematics, bg='coral2', text='-->', command=page14_Kinematics)
                                                            page14_Kinematics.pack()
                                                            page14_Kinematics.place(relx=.98,rely=.0)
                                                            
                                                        page13_Kinematics=Button(phy_page12_Kinematics, bg='coral2', text='-->', command=page13_Kinematics)
                                                        page13_Kinematics.pack()
                                                        page13_Kinematics.place(relx=.98,rely=.0)
                                                        
                                                    page12_Kinematics=Button(phy_page11_Kinematics, bg='coral2', text='-->', command=page12_Kinematics)
                                                    page12_Kinematics.pack()
                                                    page12_Kinematics.place(relx=.98,rely=.0)
                            
                                                page11_Kinematics=Button(phy_page10_Kinematics, bg='coral2', text='-->', command=page11_Kinematics)
                                                page11_Kinematics.pack()
                                                page11_Kinematics.place(relx=.98,rely=.0)
                            
                                            page10_Kinematics=Button(phy_page9_Kinematics, bg='coral2', text='-->', command=page10_Kinematics)
                                            page10_Kinematics.pack()
                                            page10_Kinematics.place(relx=.98,rely=.0)
                            
                                        page9_Kinematics=Button(phy_page8_Kinematics, bg='coral2', text='-->', command=page9_Kinematics)
                                        page9_Kinematics.pack()
                                        page9_Kinematics.place(relx=.98,rely=.0)
                            
                                    page8_Kinematics=Button(phy_page7_Kinematics, bg='coral2', text='-->', command=page8_Kinematics)
                                    page8_Kinematics.pack()
                                    page8_Kinematics.place(relx=.98,rely=.0)
                            
                                page7_Kinematics=Button(phy_page6_Kinematics, bg='coral2', text='-->', command=page7_Kinematics)
                                page7_Kinematics.pack()
                                page7_Kinematics.place(relx=.98,rely=.0)
                            
                            page6_Kinematics=Button(phy_page5_Kinematics, bg='coral2', text='-->', command=page6_Kinematics)
                            page6_Kinematics.pack()
                            page6_Kinematics.place(relx=.98,rely=.0)
                            
                        page5_Kinematics=Button(phy_page4_Kinematics, bg='coral2', text='-->', command=page5_Kinematics)
                        page5_Kinematics.pack()
                        page5_Kinematics.place(relx=.98,rely=.0)
                
                    page4_Kinematics=Button(phy_page3_Kinematics, bg='coral2', text='-->', command=page4_Kinematics)
                    page4_Kinematics.pack()
                    page4_Kinematics.place(relx=.98,rely=.0)
                
                page3_Kinematics=Button(phy_page2_Kinematics, bg='coral2', text='-->', command=page3_Kinematics)
                page3_Kinematics.pack()
                page3_Kinematics.place(relx=.98,rely=.0)
                
            page2_Kinematics=Button(tk, bg='coral2', text='-->', command=page2_Kinematics)
            page2_Kinematics.pack()
            page2_Kinematics.place(relx=.98,rely=.0)
                     
        def Gravitation11():
            phy_Gravitation11=Tk()
            phy_Gravitation11.title('Gravitation')
            canvas_Gravitation11=Canvas(phy_Gravitation11, width=1500, height=900, bg='white')
            canvas_Gravitation11.pack(expand=YES,fill=BOTH)
            
            canvas_Gravitation11.create_text(750,70,text='GRAVITATION', font=('Times New Roman',27), fill = 'black')
            
            canvas_Gravitation11.create_text(580,220,text='''
                                             Every object in the universe attracts every other object with a force which is called the force of gravitation. Gravitation is 
                                             one of the four classes of interactions found in nature.
                                             
                                             These are
                                             i) the gravitational force
                                            ii) the electromagnetic force
                                           iii) the strong nuclear force (also called the hadronic force).
                                            iv) the weak nuclear forces.''', font=('Yu Gothic UI Light',18), fill = 'black')
            
            canvas_Gravitation11.create_text(320,420,text='Newton’s Law of Gravitation', font=('Yu Gothic UI Semibold',24), fill = 'black')
            canvas_Gravitation11.create_text(450,460,text='''
                                             Gravitational force is a attractive force between two masses m1 and m2 separated by a distance r.''', font=('Yu Gothic UI Light',18), fill = 'black')
            
            canvas_Gravitation11.create_text(250,550,text='Gravitational force:', font=('Yu Gothic UI Semibold',22), fill = 'black')              
            canvas_Gravitation11.create_text(550,620,text='''
                                             •  The value of G is 6.67 X 10-11 Nm2 kg-2 and is same throughout the universe.
                                             
                                             •  The value of G is independent of the nature and size of the bodies well as the nature of the medium between them.
                                                Dimensional formula of G is [M-1L3].''', font=('Yu Gothic UI Light',18), fill = 'black')
            
            def Back_Gravitation11():
                phy_Gravitation11.destroy()
            
            Back_Gravitation11=Button(phy_Gravitation11, bg='coral2', text='<--', command=Back_Gravitation11)
            Back_Gravitation11.pack()
            Back_Gravitation11.place(relx=.0,rely=.0)
            
            def page2_Gravitation11():
                phy_page2_Gravitation11=Tk()
                phy_page2_Gravitation11.title('Gravitation')
                canvas_page2_Gravitation11=Canvas(phy_page2_Gravitation11, width=1500, height=900, bg='white')
                canvas_page2_Gravitation11.pack(expand=YES,fill=BOTH)
                
                canvas_page2_Gravitation11.create_text(400,50,text='Important Points about Gravitation Force:', font=('Yu Gothic UI Semibold',22), fill = 'black')              
                canvas_page2_Gravitation11.create_text(550,420,text='''
                                                       i) Gravitational force is a central as well as conservative force.
                                                       
                                                      ii) It is the weakest force in nature.
                                                       
                                                     iii) It is 1036 times smaller than electrostatic force and 10’l8times smaller than nuclear force.
                                                       
                                                      iv) The law of gravitational is applicable for all bodies, irrespective of their size, shape and position.
                                                    
                                                       v) Gravitational force acting between sun and planet provide it centripetal force for orbital motion.
                                                    
                                                      vi) Gravitational pull of the earth is called gravity.
                                                    
                                                     vii) Newton’s third law of motion holds good for the force of gravitation.
                                                          It means the gravitation forces between two bodies are action-reaction pairs.
                                                           
                                                    Following three points are important regarding the gravitational force
                                                           
                                                         (i) Unlike the electrostatic force, it is independent of the medium between the particles.
                                                         (ii) It is conservative in nature.
                                                        (iii) It expresses the force between two point masses (of negligible volume).
                                                             However, for external points of spherical bodies the whole mass can be assumed to be concentrated at its centre of
                                                             mass.''', font=('Yu Gothic UI Light',18), fill = 'black')
                
                def Back_page2_Gravitation11():
                    phy_page2_Gravitation11.destroy()
            
                Back_page2_Gravitation11=Button(phy_page2_Gravitation11, bg='coral2', text='<--', command=Back_page2_Gravitation11)
                Back_page2_Gravitation11.pack()
                Back_page2_Gravitation11.place(relx=.0,rely=.0)
                
                def page3_Gravitation11():
                    phy_page3_Gravitation11=Tk()
                    phy_page3_Gravitation11.title('Gravitation')
                    canvas_page3_Gravitation11=Canvas(phy_page3_Gravitation11, width=1500, height=900, bg='white')
                    canvas_page3_Gravitation11.pack(expand=YES,fill=BOTH)
                
                    canvas_page3_Gravitation11.create_text(320,50,text='Acceleration Due to Gravity:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                    canvas_page3_Gravitation11.create_text(550,410,text='''
                                                           The uniform acceleration produced in a freely falling object due to the gravitational pull of the earth is known as 
                                                           acceleration due to gravity.

                                                           •  It is denoted by g and its unit is m/s2. 
                                                           
                                                           •  It is a vector quantity and its direction is towards the centre of the earth.
                                                           
                                                           •  The value of g is independent of the mass of the object which is falling freely under gravity.
                                                           
                                                           •  The value of g changes slightly from place to place. The value of g is taken to be 9.8 m/s2 for all practical purposes.
                                                           
                                                           •  The value of acceleration due to gravity on the moon is about one sixth of that on the earth and on the sun is about 27 
                                                              times of that on the earth.
                                                           
                                                           •  Among the planets, the acceleration due to gravity is minimum on the mercury.
                                                           
                                                           •  Relation between g and a is given by
                                                              g = Gm / R2
                                                              where M = mass of the earth = 6.0 * 1024 kg and R = radius of the earth = 6.38 * 106 m.
                                                           
                                                           •  Acceleration due to gravity at a height h above the surface of the earth is given by
                                                              gh = Gm / (R+h)2 = g (1 – 2h / R)''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                    def Back_page3_Gravitation11():
                        phy_page3_Gravitation11.destroy()
                        
                    Back_page3_Gravitation11=Button(phy_page3_Gravitation11, bg='coral2', text='<--', command=Back_page3_Gravitation11)
                    Back_page3_Gravitation11.pack()
                    Back_page3_Gravitation11.place(relx=.0,rely=.0)
                    
                    def page4_Gravitation11():
                        phy_page4_Gravitation11=Tk()
                        phy_page4_Gravitation11.title('Gravitation')
                        canvas_page4_Gravitation11=Canvas(phy_page4_Gravitation11, width=1500, height=900, bg='white')
                        canvas_page4_Gravitation11.pack(expand=YES,fill=BOTH)
                
                        canvas_page4_Gravitation11.create_text(420,100,text='Factors Affecting Acceleration Due to Gravity:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                        canvas_page4_Gravitation11.create_text(530,400,text='''
                                                               i) Shape of Earth Acceleration due to gravity g &infi; 1 / R2 Earth is elliptical in shape.
                                                                  Its diameter at poles is approximately 42 km less than its diameter at equator.
                                                                  Therefore, g is minimum at equator and maximum at poles.
                                                            
                                                              ii) Rotation of Earth about Its Own Axis If ω is the angular velocity of rotation of earth about its own axis, then acceleration
                                                                  due to gravity at a place having latitude λ is given by
                                                                  g’ = g – Rω2 cos2 λ
                                                                  At poles λ = 90° and g’ = g
                                                                  Therefore, there is no effect of rotation of earth about its own axis at poles.
                                                                  At equator λ = 0° and g’ = g – Rω2
                                                                    
                                                                  The value of g is minimum at equator. If earth stopes its rotation about its own axis, then g will remain unchanged at poles 
                                                                  but increases by Rω2at equator.
                                                                    
                                                             iii) Effect of Altitude The value of g at height h from earth’s surface
                                                                  g’ = g / (1 + h / R)2
                                                                  Therefore g decreases with altitude.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                        def Back_page4_Gravitation11():
                            phy_page4_Gravitation11.destroy()
                        
                        Back_page4_Gravitation11=Button(phy_page4_Gravitation11, bg='coral2', text='<--', command=Back_page4_Gravitation11)
                        Back_page4_Gravitation11.pack()
                        Back_page4_Gravitation11.place(relx=.0,rely=.0)
                        
                        def page5_Gravitation11():
                            global phy_page5_Gravitation11
                            phy_page5_Gravitation11=Toplevel()
                            phy_page5_Gravitation11.title('Gravitation')
                            canvas_page5_Gravitation11=Canvas(phy_page5_Gravitation11, width=1500, height=900, bg='white')
                            canvas_page5_Gravitation11.pack(expand=YES,fill=BOTH)
                
                            canvas_page5_Gravitation11.create_text(200,110,text='''
                                                                   (iv) Effect of Depth The value of gat depth h A from earth’s surface
                                                                        g’ = g * (1 – h / R)
                                                                        Therefore g decreases with depth from earth’s surface.
                                                                        The value of g becomes zero at earth’s centre.''', font=('Yu Gothic UI Light',18), fill = 'black')
                            
                            global accelerationgravity
                            accelerationgravity = tkinter.PhotoImage(file="acceleration due to gravity.png")
                            button = Button(phy_page5_Gravitation11, image = accelerationgravity ,width=486, height=364, font=("Courier",20,"bold"), bg='#94ffe2') 
                            button.configure(image = accelerationgravity)
                            button.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                            
                            canvas_page5_Gravitation11.create_text(240,650,text='Gravitational Field:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                            canvas_page5_Gravitation11.create_text(550,700,text='''
                                                                   The space in the surrounding of any body in which its gravitational pull can be experienced by other bodies is called gravitational 
                                                                   field''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                         
                            def Back_page5_Gravitation11():
                                phy_page5_Gravitation11.destroy()
                        
                            Back_page5_Gravitation11=Button(phy_page5_Gravitation11, bg='coral2', text='<--', command=Back_page5_Gravitation11)
                            Back_page5_Gravitation11.pack()
                            Back_page5_Gravitation11.place(relx=.0,rely=.0)
                            
                            def page6_Gravitation11():
                                phy_page6_Gravitation11=Tk()
                                phy_page6_Gravitation11.title('Gravitation')
                                canvas_page6_Gravitation11=Canvas(phy_page6_Gravitation11, width=1500, height=900, bg='white')
                                canvas_page6_Gravitation11.pack(expand=YES,fill=BOTH)
                
                                canvas_page6_Gravitation11.create_text(320,60,text='Intensity of Gravitational Field:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                canvas_page6_Gravitation11.create_text(500,250,text='''
                                                                       The gravitational force acting per unit mass at Earth any point in gravitational field is called intensity of gravitational field 
                                                                       at that point.
                                                                       •  It is denoted by Eg or I.
                                                                          Eg or I = F / m
                                                                       •  Intensity of gravitational field at a distance r from a body of mass M is given by
                                                                          Eg or I = GM / r2 
                                                                       •  It is a vector quantity and its direction is towards the centre of gravity of the body.
                                                                       •  Its S1 unit is N/m and its dimensional formula is [LT-2].
                                                                       •  Gravitational mass Mg is defined by Newton’s law of gravitation.
                                                                          Mg = Fg / g = W / g = Weight of body / Acceleration due to gravity
                                                                          ∴ (M1)g / (M2)g = Fg1g2 / Fg2g1''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                canvas_page6_Gravitation11.create_text(260,500,text='Gravitational Potential:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                canvas_page6_Gravitation11.create_text(520,620,text='''
                                                                       Gravitational potential at any point in gravitational field is equal the work done per unit mass in bringing a very light body from
                                                                       infinity to that point.
                                                                       •  It is denoted by Vg.
                                                                       •  Gravitational potential, Vg = W / m = – GM / r
                                                                       •  Its SI unit is J / kg and it is a scalar quantity. 
                                                                       •  Its dimensional formula is [L3r-2].
                                                                       •  Since work W is obtained, that is, it is negative, the gravitational potential is always negative.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                def Back_page6_Gravitation11():
                                    phy_page6_Gravitation11.destroy()
                        
                                Back_page6_Gravitation11=Button(phy_page6_Gravitation11, bg='coral2', text='<--', command=Back_page6_Gravitation11)
                                Back_page6_Gravitation11.pack()
                                Back_page6_Gravitation11.place(relx=.0,rely=.0)
                                
                                def page7_Gravitation11():
                                    phy_page7_Gravitation11=Tk()
                                    phy_page7_Gravitation11.title('Gravitation')
                                    canvas_page7_Gravitation11=Canvas(phy_page7_Gravitation11, width=1500, height=900, bg='white')
                                    canvas_page7_Gravitation11.pack(expand=YES,fill=BOTH)
                
                                    canvas_page7_Gravitation11.create_text(310,60,text='Gravitational Potential Energy:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                    canvas_page7_Gravitation11.create_text(500,210,text='''
                                                                           Gravitational potential energy of any object at any point in gravitational field is equal to the work done in bringing it from infinity
                                                                           to that point. 
                                                                           •  It is denoted by U.
                                                                           •  Gravitational potential energy U = – GMm / r
                                                                           •  The negative sign shows that the gravitational potential energy decreases with increase in distance.
                                                                           •  Gravitational potential energy at height h from surface of earth
                                                                              Uh = – GMm / R + h = mgR / 1 + h/R''', font=('Yu Gothic UI Light',18), fill = 'black')
                                   
                                    canvas_page7_Gravitation11.create_text(170,370,text='Satellite', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                    canvas_page7_Gravitation11.create_text(540,430,text='''
                                                                           A heavenly object which revolves around a planet is called a satellite. Natural satellites are those heavenly objects which are not man
                                                                           made and revolve around the earth. Artificial satellites are those heavenly objects which are man made and launched for some purposes 
                                                                           revolve around the earth''', font=('Yu Gothic UI Light',18), fill = 'black')
                                    
                                    canvas_page7_Gravitation11.create_text(270,530,text='Time period of satellite:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                    canvas_page7_Gravitation11.create_text(100,650,text='''
                                                                           T = 2π √r3 / GM
                                                                             = 2π √(R + h)3 / g [ g = GM / R2
                                                                           Near the earth surface, time period of the satellite
                                                                           T = 2π √R3 / GM = √3π / Gp
                                                                           T = 2π √R / g = 5.08 * 103 s = 84 min.
                                                                           here p is the average density of earth.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                    
                                    def Back_page7_Gravitation11():
                                        phy_page7_Gravitation11.destroy()
                        
                                    Back_page7_Gravitation11=Button(phy_page7_Gravitation11, bg='coral2', text='<--', command=Back_page7_Gravitation11)
                                    Back_page7_Gravitation11.pack()
                                    Back_page7_Gravitation11.place(relx=.0,rely=.0)
                                    
                                    def page8_Gravitation11():
                                        global phy_page8_Gravitation11
                                        phy_page8_Gravitation11=Toplevel()
                                        phy_page8_Gravitation11.title('Gravitation')
                                        canvas_page8_Gravitation11=Canvas(phy_page8_Gravitation11, width=1500, height=900, bg='white')
                                        canvas_page8_Gravitation11.pack(expand=YES,fill=BOTH)
                                        
                                        global satellites
                                        satellites = tkinter.PhotoImage(file="satellites.png")
                                        button = Button(phy_page8_Gravitation11, image = satellites ,width=627, height=300, font=("Courier",20,"bold"), bg='#94ffe2') 
                                        button.configure(image = satellites)
                                        button.place(relx = 0.5, rely = 0.2, anchor = CENTER)
                
                                        canvas_page8_Gravitation11.create_text(340,360,text='Artificial satellites are of two types :', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                        canvas_page8_Gravitation11.create_text(340,410,text='1. Geostationary or Parking Satellites', font=('Yu Gothic UI Semibold',20), fill = 'black')
                                        canvas_page8_Gravitation11.create_text(500,590,text='''
                                                                               A satellite which appears to be at a fixed position at a definite height to an observer on earth is called geostationary or parking
                                                                               satellite.
                                                                               Height from earth’s surface = 36000 km
                                                                               Radius of orbit = 42400 km
                                                                               Time period = 24 h
                                                                               Orbital velocity = 3.1 km/s
                                                                               Angular velocity = 2π / 24 = π / 12 rad / h
                                                                               There satellites revolve around the earth in equatorial orbits.
                                                                               These satellites are used in communication purpose.
                                                                               INSAT 2B and INSAT 2C are geostationary satellites of India.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                        def Back_page8_Gravitation11():
                                            phy_page8_Gravitation11.destroy()
                        
                                        Back_page8_Gravitation11=Button(phy_page8_Gravitation11, bg='coral2', text='<--', command=Back_page8_Gravitation11)
                                        Back_page8_Gravitation11.pack()
                                        Back_page8_Gravitation11.place(relx=.0,rely=.0)
                                        
                                        def page9_Gravitation11():
                                            global phy_page9_Gravitation11
                                            phy_page9_Gravitation11=Toplevel()
                                            phy_page9_Gravitation11.title('Gravitation')
                                            canvas_page9_Gravitation11=Canvas(phy_page9_Gravitation11, width=1500, height=900, bg='white')
                                            canvas_page9_Gravitation11.pack(expand=YES,fill=BOTH)
                
                                            canvas_page9_Gravitation11.create_text(250,100,text='2. Polar Satellites', font=('Yu Gothic UI Semibold',20), fill = 'black')
                                            canvas_page9_Gravitation11.create_text(500,280,text='''
                                                                                   These are those satellites which revolve in polar orbits around earth. A polar orbit is that orbit whose angle of inclination with 
                                                                                   equatorial plane of earth is 90°.
                                                                                   
                                                                                   Height from earth’s surface = 880 km
                                                                                   Time period = 84 min
                                                                                   Orbital velocity = 8 km / s
                                                                                   Angular velocity = 2π / 84 = π / 42 rad / min.
                                                                                   There satellites revolve around the earth in polar orbits.
                                                                                   These satellites are used in forecasting weather, studying the upper region of the atmosphere, in mapping, etc.
                                                                                   PSLV series satellites are polar satellites of India.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                            
                                            global geopolar
                                            geopolar = tkinter.PhotoImage(file="geo and Polar Satellites.png")
                                            button = Button(phy_page9_Gravitation11, image = geopolar ,width=500, height=250, font=("Courier",20,"bold"), bg='#94ffe2') 
                                            button.configure(image = geopolar)
                                            button.place(relx = 0.5, rely = 0.75, anchor = CENTER)
                
                                            def Back_page9_Gravitation11():
                                                phy_page9_Gravitation11.destroy()
                        
                                            Back_page9_Gravitation11=Button(phy_page9_Gravitation11, bg='coral2', text='<--', command=Back_page9_Gravitation11)
                                            Back_page9_Gravitation11.pack()
                                            Back_page9_Gravitation11.place(relx=.0,rely=.0)
                                            
                                            def page10_Gravitation11():
                                                phy_page10_Gravitation11=Tk()
                                                phy_page10_Gravitation11.title('Gravitation')
                                                canvas_page10_Gravitation11=Canvas(phy_page10_Gravitation11, width=1500, height=900, bg='white')
                                                canvas_page10_Gravitation11.pack(expand=YES,fill=BOTH)
                
                                                canvas_page10_Gravitation11.create_text(220,100,text='Orbital Velocity:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                canvas_page10_Gravitation11.create_text(370,230,text='''
                                                                                        Orbital velocity of a satellite is the minimum velocity required to the satellite into a given orbit around earth
                                                                                        .
                                                                                        •  Orbital velocity of a satellite is given by
                                                                                           vo = √GM / r = R √g / R + h
                                                                                           where, M = mass of the planet, R = radius of the planet and h = height of the satellite from planet’s surface.
                                                                                        •  If satellite is revolving near the earth’s surface, then r = (R + h) =- R
                                                                                           Now orbital velocity, vo = √gR = 7.92km / h''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                
                                                canvas_page10_Gravitation11.create_text(300,400,text='Energy of a Satellite in Orbit:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                canvas_page10_Gravitation11.create_text(-50,480,text='''
                                                                                        Total energy of a satellite,
                                                                                        E = KE + PE
                                                                                          = GMm / 2r + (- GMm / r)
                                                                                          = – GMm / 2r''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                
                                                canvas_page10_Gravitation11.create_text(220,600,text='Binding Energy:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                canvas_page10_Gravitation11.create_text(470,680,text='''
                                                                                        The energy required to remove a satellite from its orbit around the earth (planet) to infinity is called binding energy of the satellite.
                                                                                        
                                                                                        •  Binding energy of the satellite of mass m is given by
                                                                                           BE = + GMm / 2r''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                def Back_page10_Gravitation11():
                                                    phy_page10_Gravitation11.destroy()
                                                    
                                                Back_page10_Gravitation11=Button(phy_page10_Gravitation11, bg='coral2', text='<--', command=Back_page10_Gravitation11)
                                                Back_page10_Gravitation11.pack()
                                                Back_page10_Gravitation11.place(relx=.0,rely=.0)
                                                
                                                def page11_Gravitation11():
                                                    global phy_page11_Gravitation11
                                                    phy_page11_Gravitation11=Toplevel()
                                                    phy_page11_Gravitation11.title('Gravitation')
                                                    canvas_page11_Gravitation11=Canvas(phy_page11_Gravitation11, width=1500, height=900, bg='white')
                                                    canvas_page11_Gravitation11.pack(expand=YES,fill=BOTH)
                
                                                    canvas_page11_Gravitation11.create_text(220,50,text='Escape Velocity:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                    canvas_page11_Gravitation11.create_text(470,150,text='''
                                                                                            Escape velocity on earth is the minimum velocity with which a body has to be projected vertically upwards from the earth’s surface so 
                                                                                            that it just crosses the earth’s gravitational field and never returns.
                                                                                            
                                                                                            ve = √2GM / R
                                                                                               = √2gR = √8πp GR2 / 3
                                                                                            •   Escape velocity at earth is 11.2 km / s.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                    
                                                    canvas_page11_Gravitation11.create_text(340,300,text='Some Important Escape Velocities:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                    canvas_page11_Gravitation11.create_text(450,370,text='''
                                                                                            Relation between escape velocity and orbital velocity of the satellite
                                                                                            ve = √2 vo
                                                                                            •  If velocity of projection u of satellite is greater than the escape velocity ( v > ve), then the satellite will escape away following a 
                                                                                               hyperbolic path.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                    
                                                    global Escapevelocity
                                                    Escapevelocity = tkinter.PhotoImage(file="Escapevelocity.png")
                                                    button = Button(phy_page11_Gravitation11, image = Escapevelocity ,width=480, height=349, font=("Courier",20,"bold"), bg='#94ffe2') 
                                                    button.configure(image = Escapevelocity)
                                                    button.place(relx = 0.5, rely = 0.76, anchor = CENTER)
                                                    
                                                    def Back_page11_Gravitation11():
                                                        phy_page11_Gravitation11.destroy()
                        
                                                    Back_page11_Gravitation11=Button(phy_page11_Gravitation11, bg='coral2', text='<--', command=Back_page11_Gravitation11)
                                                    Back_page11_Gravitation11.pack()
                                                    Back_page11_Gravitation11.place(relx=.0,rely=.0)
                                                    
                                                    def page12_Gravitation11():
                                                        global phy_page12_Gravitation11
                                                        phy_page12_Gravitation11=Toplevel()
                                                        phy_page12_Gravitation11.title('Gravitation')
                                                        canvas_page12_Gravitation11=Canvas(phy_page12_Gravitation11, width=1500, height=900, bg='white')
                                                        canvas_page12_Gravitation11.pack(expand=YES,fill=BOTH)
                                                        
                                                        canvas_page12_Gravitation11.create_text(270,80,text='Weightlessness:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                        canvas_page12_Gravitation11.create_text(190,200,text='''
                                                                                                It is a situation in which the effective weight of the body becomes zero
                                                                                                Weightlessness is achieved
                                                                                                i) during freely falling under gravity
                                                                                                ii) inside a space craft or satellite
                                                                                               iii) at the centre of the earth
                                                                                              iv) when a body is lying in a freely falling lift''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                        
                                                        global weightlessness
                                                        weightlessness = tkinter.PhotoImage(file="weightlessness.png")
                                                        button = Button(phy_page12_Gravitation11, image = weightlessness ,width=650, height=431, font=("Courier",20,"bold"), bg='#94ffe2') 
                                                        button.configure(image = weightlessness)
                                                        button.place(relx = 0.5, rely = 0.65, anchor = CENTER)
                                                    
                                                        def Back_page12_Gravitation11():
                                                            phy_page12_Gravitation11.destroy()
                        
                                                        Back_page12_Gravitation11=Button(phy_page12_Gravitation11, bg='coral2', text='<--', command=Back_page12_Gravitation11)
                                                        Back_page12_Gravitation11.pack()
                                                        Back_page12_Gravitation11.place(relx=.0,rely=.0)
                                                        
                                                        def page13_Gravitation11():
                                                            global phy_page13_Gravitation11
                                                            phy_page13_Gravitation11=Toplevel()
                                                            phy_page13_Gravitation11.title('Gravitation')
                                                            canvas_page13_Gravitation11=Canvas(phy_page13_Gravitation11, width=1500, height=900, bg='white')
                                                            canvas_page13_Gravitation11.pack(expand=YES,fill=BOTH)
                                                            
                                                            canvas_page13_Gravitation11.create_text(350,70,text='Kepler’s Laws of Planetary Motion:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                            canvas_page13_Gravitation11.create_text(450,250,text='''
                                                                                                    i) Law of orbit Every planet revolve around the sun in elliptical orbit and sun is at its one focus.
                                                                                                   ii) Law of area The radius vector drawn from the sun to a planet sweeps out equal areas in equal intervals of time, i.e., the areal 
                                                                                                       velocity of the planet around the sun is constant.
                                                                                                       Areal velocity of a planet
                                                                                                       dA / dt = L / 2m = constant
                                                                                                       where L = angular momentum and m = mass of the planet.
                                                                                                  iii) Law of period The square of the time period of revolution of planet around the sun is directly proportional to the cube semi-major 
                                                                                                       axis of its elliptical orbit.
                                                                                                       T2 &infi; a3 or (T1 / T2)2 = (a1 / a2)3
                                                                                                       where, a = semi-major axis of the elliptical orbit.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                                    
                                                            global keplerslaw
                                                            keplerslaw = tkinter.PhotoImage(file="keplerslaw.png")
                                                            button = Button(phy_page13_Gravitation11, image = keplerslaw ,width=685, height=268, font=("Courier",20,"bold"), bg='#94ffe2') 
                                                            button.configure(image = keplerslaw)
                                                            button.place(relx = 0.5, rely = 0.7, anchor = CENTER)
                                                    
                                                            def Back_page13_Gravitation11():
                                                                phy_page13_Gravitation11.destroy()
                                                                
                                                            Back_page13_Gravitation11=Button(phy_page13_Gravitation11, bg='coral2', text='<--', command=Back_page13_Gravitation11)
                                                            Back_page13_Gravitation11.pack()
                                                            Back_page13_Gravitation11.place(relx=.0,rely=.0)
                                                            
                                                            def page14_Gravitation11():
                                                                phy_page14_Gravitation11=Tk()
                                                                phy_page14_Gravitation11.title('Gravitation')
                                                                canvas_page14_Gravitation11=Canvas(phy_page14_Gravitation11, width=1500, height=900, bg='white')
                                                                canvas_page14_Gravitation11.pack(expand=YES,fill=BOTH)
                                                                
                                                                canvas_page14_Gravitation11.create_text(230,70,text='Important Points:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                                canvas_page14_Gravitation11.create_text(400,420,text='''
                                                                                                        i) A missile is launched with a velocity less than the escape velocity. The sum of its kinetic energy and potential energy is negative.
                                                                
                                                                                                       ii) The orbital speed of jupiter is less than the orbital speed of earth.
                                                
                                                                                                      iii) A bomb explodes on the moon. You cannot hear the sound of the explosion on earth.
                                                                                                        
                                                                                                       iv) A bottle filled with water at 30°C and fitted with a cork is taken to the moon. If the cork is opened at the surface of the moon 
                                                                                                           then water will boil.
                                                                                                        
                                                                                                        v) For a satellite orbiting near earth’s surface
                                                                                                            (a) Orbital velocity = 8 km/s
                                                                                                            (b) Time period = 84 min approximately
                                                                                                            (c) Angular speed ω = 2π/84 rad/min = 0.00125 rad/s
                                                                                                        
                                                                                                      vi) Inertial mass and gravitational mass
                                                                                                            (a) Inertial mass = force /acceleration
                                                                                                            (b) Gravitational mass = weight of body/acceleration due to gravity
                                                                                                            (c) They are equal to each other in magnitude.
                                                                                                            (d) Gravitational mass of a body is affected by the presence of other bodies near it.
                                                                                                                Inertial mass of a body remains unaffected by the presence of other bodies near it.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                                                def Back_page14_Gravitation11():
                                                                    phy_page14_Gravitation11.destroy()
                                                                    
                                                                Back_page14_Gravitation11=Button(phy_page14_Gravitation11, bg='coral2', text='<--', command=Back_page14_Gravitation11)
                                                                Back_page14_Gravitation11.pack()
                                                                Back_page14_Gravitation11.place(relx=.0,rely=.0)
                                                                
                                                                def Back_to_class11_Gravitation11():
                                                                    phy_Gravitation11.destroy()
                                                                    phy_page2_Gravitation11.destroy()
                                                                    phy_page3_Gravitation11.destroy()
                                                                    phy_page4_Gravitation11.destroy()
                                                                    phy_page5_Gravitation11.destroy()
                                                                    phy_page6_Gravitation11.destroy()
                                                                    phy_page7_Gravitation11.destroy()
                                                                    phy_page8_Gravitation11.destroy()
                                                                    phy_page9_Gravitation11.destroy()
                                                                    phy_page10_Gravitation11.destroy()
                                                                    phy_page11_Gravitation11.destroy()
                                                                    phy_page12_Gravitation11.destroy()
                                                                    phy_page13_Gravitation11.destroy()
                                                                    phy_page14_Gravitation11.destroy()
                                                                    
                                                                Back_to_class11_Gravitation11= Button(phy_page14_Gravitation11,bg='coral2', text='Class 11',font=('Castellar',18), command=Back_to_class11_Gravitation11)
                                                                Back_to_class11_Gravitation11.pack()
                                                                Back_to_class11_Gravitation11.place(relx=.87,rely=.85)
                                                               
                                                            page14_Gravitation11=Button(phy_page13_Gravitation11, bg='coral2', text='-->', command=page14_Gravitation11)
                                                            page14_Gravitation11.pack()
                                                            page14_Gravitation11.place(relx=.98,rely=.0)
                                                            
                                                        page13_Gravitation11=Button(phy_page12_Gravitation11, bg='coral2', text='-->', command=page13_Gravitation11)
                                                        page13_Gravitation11.pack()
                                                        page13_Gravitation11.place(relx=.98,rely=.0)
                                                        
                                                    page12_Gravitation11=Button(phy_page11_Gravitation11, bg='coral2', text='-->', command=page12_Gravitation11)
                                                    page12_Gravitation11.pack()
                                                    page12_Gravitation11.place(relx=.98,rely=.0)
                            
                                                page11_Gravitation11=Button(phy_page10_Gravitation11, bg='coral2', text='-->', command=page11_Gravitation11)
                                                page11_Gravitation11.pack()
                                                page11_Gravitation11.place(relx=.98,rely=.0)
                            
                                            page10_Gravitation11=Button(phy_page9_Gravitation11, bg='coral2', text='-->', command=page10_Gravitation11)
                                            page10_Gravitation11.pack()
                                            page10_Gravitation11.place(relx=.98,rely=.0)
                            
                                        page9_Gravitation11=Button(phy_page8_Gravitation11, bg='coral2', text='-->', command=page9_Gravitation11)
                                        page9_Gravitation11.pack()
                                        page9_Gravitation11.place(relx=.98,rely=.0)
                            
                                    page8_Gravitation11=Button(phy_page7_Gravitation11, bg='coral2', text='-->', command=page8_Gravitation11)
                                    page8_Gravitation11.pack()
                                    page8_Gravitation11.place(relx=.98,rely=.0)
                            
                                page7_Gravitation11=Button(phy_page6_Gravitation11, bg='coral2', text='-->', command=page7_Gravitation11)
                                page7_Gravitation11.pack()
                                page7_Gravitation11.place(relx=.98,rely=.0)
                            
                            page6_Gravitation11=Button(phy_page5_Gravitation11, bg='coral2', text='-->', command=page6_Gravitation11)
                            page6_Gravitation11.pack()
                            page6_Gravitation11.place(relx=.98,rely=.0)
                            
                        page5_Gravitation11=Button(phy_page4_Gravitation11, bg='coral2', text='-->', command=page5_Gravitation11)
                        page5_Gravitation11.pack()
                        page5_Gravitation11.place(relx=.98,rely=.0)
                
                    page4_Gravitation11=Button(phy_page3_Gravitation11, bg='coral2', text='-->', command=page4_Gravitation11)
                    page4_Gravitation11.pack()
                    page4_Gravitation11.place(relx=.98,rely=.0)
                
                page3_Gravitation11=Button(phy_page2_Gravitation11, bg='coral2', text='-->', command=page3_Gravitation11)
                page3_Gravitation11.pack()
                page3_Gravitation11.place(relx=.98,rely=.0)
                
            page2_Gravitation11=Button(phy_Gravitation11, bg='coral2', text='-->', command=page2_Gravitation11)
            page2_Gravitation11.pack()
            page2_Gravitation11.place(relx=.98,rely=.0)
                        
        def Oscillations():
            global phy_Oscillations
            phy_Oscillations=Toplevel()
            phy_Oscillations.title('Oscillations')
            canvas_Oscillations=Canvas(phy_Oscillations, width=1500, height=900, bg='white')
            canvas_Oscillations.pack(expand=YES,fill=BOTH)
            
            canvas_Oscillations.create_text(750,70,text='OSCILLATIONS', font=('Times New Roman',27), fill = 'black')
            
            canvas_Oscillations.create_text(260,150,text='Periodic Motion:', font=('Yu Gothic UI Semibold',22), fill = 'black')
            canvas_Oscillations.create_text(550,200,text='''
                                            A motion which repeats itself identically after a fixed interval of time is called periodic motion. 
                                            e.g., orbital motion of the earth around the sun, motion of arms of a clock, motion of a simple pendulum etc.''', font=('Yu Gothic UI Light',18), fill = 'black')
             
            canvas_Oscillations.create_text(275,300,text='Oscillatory Motion:', font=('Yu Gothic UI Semibold',22), fill = 'black')
            canvas_Oscillations.create_text(540,350,text='''
                                            A periodic motion taking place to and fro or back and forth about a fixed point, is called oscillatory motion,
                                            e.g., motion of a simple pendulum, motion of a loaded ''', font=('Yu Gothic UI Light',18), fill = 'black')
            
            canvas_Oscillations.create_text(290,450,text='Harmonic Oscillation:', font=('Yu Gothic UI Semibold',22), fill = 'black')
            canvas_Oscillations.create_text(520,500,text='''
                                            The oscillation which can be expressed in terms of single harmonic function, i.e., sine or cosine function,
                                            is called harmonic oscillation.''', font=('Yu Gothic UI Light',18), fill = 'black')
            
            canvas_Oscillations.create_text(320,600,text='Simple Harmonic Motion:', font=('Yu Gothic UI Semibold',22), fill = 'black')
            canvas_Oscillations.create_text(350,670,text='''
                                            A harmonic oscillation of constant amplitude and of single frequency
                                            under a restoring force whose magnitude is proportional to the 
                                            displacement and always acts tvowards mean Position is called Simple
                                            Harmonic Motion (SHM).''', font=('Yu Gothic UI Light',18), fill = 'black')
            global SMH
            SMH = tkinter.PhotoImage(file="SMH.png")
            button = Button(phy_Oscillations, image = SMH ,width=207, height=206, font=("Courier",20,"bold"), bg='#94ffe2') 
            button.configure(image = SMH)
            button.place(relx = 0.7 , rely = 0.77, anchor = CENTER)
            
            def Back_Oscillations():
                phy_Oscillations.destroy()
            
            Back_Oscillations=Button(phy_Oscillations, bg='coral2', text='<--', command=Back_Oscillations)
            Back_Oscillations.pack()
            Back_Oscillations.place(relx=.0,rely=.0)
            
            def page2_Oscillations():
                phy_page2_Oscillations=Tk()
                phy_page2_Oscillations.title('Oscillations')
                canvas_page2_Oscillations=Canvas(phy_page2_Oscillations, width=1500, height=900, bg='white')
                canvas_page2_Oscillations.pack(expand=YES,fill=BOTH)
                
                canvas_page2_Oscillations.create_text(180,130,text='''
                                                      A simple harmonic oscillation can be expressed as
                                                      y = a sin ωt
                                                      or y = a cos ωt
                                                      Where a = amplitude of oscillation.''', font=('Yu Gothic UI Light',18), fill = 'black')
                
                canvas_page2_Oscillations.create_text(290,270,text='Non-harmonic Oscillation:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                canvas_page2_Oscillations.create_text(390,320,text='''
                                                      A non-harmonic oscillation is a combination of two or more than two harmonic oscillations.
                                                      It can be expressed as y = a sin ωt + b sin 2ωt''', font=('Yu Gothic UI Light',18), fill = 'black')
                
                canvas_page2_Oscillations.create_text(300,420,text='Some Terms Related to SHM:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                canvas_page2_Oscillations.create_text(500,580,text='''
                                                      i) Time Period Time taken by the body to complete one oscillation is known as time period. It is denoted by T.
                                                      
                                                     ii) Frequency The number of oscillations completed by the body in one second is called frequency. It is denoted by v.
                                                         Its SI unit is ‘hertz’ or ‘second-1‘.
                                                         Frequency = 1 / Time period
                                                      
                                                    iii) Angular Frequency The product of frequency with factor 2π is called angular frequency. It is denoted by ω.
                                                         Angular frequency (ω) = 2πv
                                                         Its SI unit is ‘hertz’ or ‘second-1‘.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                      
                def Back_page2_Oscillations():
                    phy_page2_Oscillations.destroy()
            
                Back_page2_Oscillations=Button(phy_page2_Oscillations, bg='coral2', text='<--', command=Back_page2_Oscillations)
                Back_page2_Oscillations.pack()
                Back_page2_Oscillations.place(relx=.0,rely=.0)
                
                def page3_Oscillations():
                    phy_page3_Oscillations=Tk()
                    phy_page3_Oscillations.title('Oscillations')
                    canvas_page3_Oscillations=Canvas(phy_page3_Oscillations, width=1500, height=900, bg='white')
                    canvas_page3_Oscillations.pack(expand=YES,fill=BOTH)
                    
                    canvas_page3_Oscillations.create_text(550,170,text='''
                                                          iv) Displacement A physical quantity which changes uniformly with time in a periodic motion. is called displacement. 
                                                              It is denoted by y.
                                                         
                                                           v) Amplitude The maximum displacement in any direction from mean position is called amplitude. It is denoted by a.
                                                          
                                                          vi) Phase A physical quantity which express the position and direction of motion of an oscillating particle, is called phase. 
                                                              It is denoted by φ.
                                                              Simple harmonic motion is defined as the projection of a uniform circular motion on any diameter of a circle of reference.''', font=('Yu Gothic UI Light',18), fill = 'black')
                    
                    canvas_page3_Oscillations.create_text(350,370,text='Some Important Formulae of SHM:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                    canvas_page3_Oscillations.create_text(250,570,text='''
                                                          i) Displacement in SHM at any instant is given by
                                                             y = a sin ωt
                                                             or y = a cos ωt
                                                             where a = amplitude and
                                                             ω = angular frequency.
                                                          
                                                         ii) Velocity of a particle executing SHM at any instant is given by
                                                             v = ω √(a2 – y2)
                                                             At mean position y = 0 and v is maximum
                                                             vmax = aω
                                                             At extreme position y = a and v is zero.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                    
                    def Back_page3_Oscillations():
                        phy_page3_Oscillations.destroy()
                        
                    Back_page3_Oscillations=Button(phy_page3_Oscillations, bg='coral2', text='<--', command=Back_page3_Oscillations)
                    Back_page3_Oscillations.pack()
                    Back_page3_Oscillations.place(relx=.0,rely=.0)
                    
                    def page4_Oscillations():
                        global phy_page4_Oscillations
                        phy_page4_Oscillations=Toplevel()
                        phy_page4_Oscillations.title('Oscillations')
                        canvas_page4_Oscillations=Canvas(phy_page4_Oscillations, width=1500, height=900, bg='white')
                        canvas_page4_Oscillations.pack(expand=YES,fill=BOTH)
                        
                        canvas_page4_Oscillations.create_text(520,200,text='''
                                                              iii) Acceleration of a particle executing SHM at any instant is given by
                                                                   A or α = – ω2 y
                                                                   Negative sign indicates that the direction of acceleration is opposite to the direction in which displacement increases, i.e., 
                                                                   towards mean position.
                                                                   At mean position y = 0 and acceleration is also zero.
                                                                   At extreme position y = a and acceleration is maximum
                                                                   Amax = – aω2
                                                              
                                                               iv) Time period in SHM is given by
                                                                   T = 2π √Displacement / Acceleration''', font=('Yu Gothic UI Light',18), fill = 'black')
                        
                        canvas_page4_Oscillations.create_text(280,430,text='Graphical Representation', font=('Yu Gothic UI Semibold',22), fill = 'black')
                        canvas_page4_Oscillations.create_text(230,490,text='''
                                                              (i) Displacement – Time Graph''', font=('Yu Gothic UI Light',18), fill = 'black')
                        global displacementgraph
                        displacementgraph = tkinter.PhotoImage(file="displacementgraph.png")
                        button = Button(phy_page4_Oscillations, image = displacementgraph ,width=368, height=171, font=("Courier",20,"bold"), bg='#94ffe2') 
                        button.configure(image = displacementgraph)
                        button.place(relx = 0.3, rely = 0.75, anchor = CENTER)
                        
                        canvas_page4_Oscillations.create_text(820,490,text='''
                                                              (ii) Velocity – Time Graph''', font=('Yu Gothic UI Light',18), fill = 'black')
                        global velocitygraph
                        velocitygraph = tkinter.PhotoImage(file="velocitygraph.png")
                        button = Button(phy_page4_Oscillations, image = velocitygraph ,width=372, height=173, font=("Courier",20,"bold"), bg='#94ffe2') 
                        button.configure(image = velocitygraph)
                        button.place(relx = 0.7, rely = 0.75, anchor = CENTER)
            
                        def Back_page4_Oscillations():
                            phy_page4_Oscillations.destroy()
                        
                        Back_page4_Oscillations=Button(phy_page4_Oscillations, bg='coral2', text='<--', command=Back_page4_Oscillations)
                        Back_page4_Oscillations.pack()
                        Back_page4_Oscillations.place(relx=.0,rely=.0)
                        
                        def page5_Oscillations():
                            global phy_page5_Oscillations
                            phy_page5_Oscillations=Toplevel()
                            phy_page5_Oscillations.title('Oscillations')
                            canvas_page5_Oscillations=Canvas(phy_page5_Oscillations, width=1500, height=900, bg='white')
                            canvas_page5_Oscillations.pack(expand=YES,fill=BOTH)
                
                            canvas_page5_Oscillations.create_text(130,100,text='''
                                                                  (iii) Acceleration – Time Graph''', font=('Yu Gothic UI Light',18), fill = 'black')
                            
                            global accelerationgraph
                            accelerationgraph = tkinter.PhotoImage(file="accelerationgraph.png")
                            button = Button(phy_page5_Oscillations, image = accelerationgraph ,width=376, height=181, font=("Courier",20,"bold"), bg='#94ffe2') 
                            button.configure(image = accelerationgraph)
                            button.place(relx = 0.25, rely = 0.3, anchor = CENTER)
                            
                            canvas_page5_Oscillations.create_text(800,270,text='''
                                                                  For a particle executing SHM. the phase difference between
                                                                  
                                                                  i) Instantaneous displacement and instantaneous velocity
                                                                      = (π / 2) rad
                                                                 ii) Instantaneous velocity and instantaneous acceleration
                                                                      = (π / 2) rad
                                                                iii) Instantaneous acceleration and instantaneous displacement
                                                                      = π rad
                                                                
                                                                    The graph between velocity and displacement for a particle 
                                                                    executing SHM is elliptical.''', font=('Yu Gothic UI Light',18), fill = 'black')
                            
                            canvas_page5_Oscillations.create_text(230,520,text='Force in SHM:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                            canvas_page5_Oscillations.create_text(380,640,text='''
                                                                  We know that, the acceleration of body in SlIM is α = -ω2 x
                                                                  Applying the equation of motion F = ma,
                                                                  We have, F = – mω2 x = -kx
                                                                  Where, ω = √k / m and k = mω2 is a constant and sometimes it is called the elastic constant.
                                                                  
                                                                  In SHM, the force is proportional and opposite to the displacement''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                  
                            def Back_page5_Oscillations():
                                phy_page5_Oscillations.destroy()
                        
                            Back_page5_Oscillations=Button(phy_page5_Oscillations, bg='coral2', text='<--', command=Back_page5_Oscillations)
                            Back_page5_Oscillations.pack()
                            Back_page5_Oscillations.place(relx=.0,rely=.0)
                            
                            def page6_Oscillations():
                                phy_page6_Oscillations=Tk()
                                phy_page6_Oscillations.title('Oscillations')
                                canvas_page6_Oscillations=Canvas(phy_page6_Oscillations, width=1500, height=900, bg='white')
                                canvas_page6_Oscillations.pack(expand=YES,fill=BOTH)
                
                                canvas_page6_Oscillations.create_text(230,80,text='Energy in SHM:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                canvas_page6_Oscillations.create_text(500,400,text='''
                                                                      The kinetic energy of the particle is K = 1 / 2 mω2 (A2 – x2)
                                                                      
                                                                      From this expression we can see that, the kinetic energy is maximum at the centre (x = 0) and zero at the extremes of 
                                                                      oscillation (x ± A).
                                                                      
                                                                      The potential energy of the particle is U = 1 / 2 mω2 x2
                                                                      
                                                                      From this expression we can see that, the potential energy has a minimum value at the centre (x = 0) and increases as the 
                                                                      particle approaches either extreme of the oscillation (x ± A).
                                                                      
                                                                      Total energy can be obtained by adding potential and kinetic energies. Therefore,
                                                                      E = K + U
                                                                        = 1 / 2 mω2 (A2 – x2) + 1 / 2 mω2 x2
                                                                        = 1 / 2 mω2 A2
                                                                      
                                                                      where A = amplitude
                                                                      m = mass of particle executing SHM.
                                                                      ω = angular frequency and
                                                                      v = frequency''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                def Back_page6_Oscillations():
                                    phy_page6_Oscillations.destroy()
                        
                                Back_page6_Oscillations=Button(phy_page6_Oscillations, bg='coral2', text='<--', command=Back_page6_Oscillations)
                                Back_page6_Oscillations.pack()
                                Back_page6_Oscillations.place(relx=.0,rely=.0)
                                
                                def page7_Oscillations():
                                    global phy_page7_Oscillations
                                    phy_page7_Oscillations=Toplevel()
                                    phy_page7_Oscillations.title('Oscillations')
                                    canvas_page7_Oscillations=Canvas(phy_page7_Oscillations, width=1500, height=900, bg='white')
                                    canvas_page7_Oscillations.pack(expand=YES,fill=BOTH)
                
                                    canvas_page7_Oscillations.create_text(500,80,text='Changes of kinetic and potential energies during oscillations:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                    
                                    global PEKEgraph
                                    PEKEgraph = tkinter.PhotoImage(file="PEKEgraph.png")
                                    button = Button(phy_page7_Oscillations, image = PEKEgraph ,width=382, height=222, font=("Courier",20,"bold"), bg='#94ffe2') 
                                    button.configure(image = PEKEgraph)
                                    button.place(relx = 0.5, rely = 0.3, anchor = CENTER)
                                    
                                    canvas_page7_Oscillations.create_text(500,550,text='''
                                                                          •  The frequency of kinetic energy or potential energy of a particle executing SHM is double than that of the frequency in SHM.
                                                                          
                                                                          •  The frequency of total energy of particles executing SHM is zero as total energy in SHM remains constant at all positions.
                                                                          
                                                                          •  When a particle of mass m executes SHM with a constant angular frequency (I), then time period of oscillation
                                                                             T = 2π √Inertia factor / Spring factor
                                                                          
                                                                          •  In general, inertia factor = m, (mass of the particle)
                                                                          
                                                                          •  Spring factor = k (force constant)''', font=('Yu Gothic UI Light',18), fill = 'black')
                                
                                    def Back_page7_Oscillations():
                                        phy_page7_Oscillations.destroy()
                        
                                    Back_page7_Oscillations=Button(phy_page7_Oscillations, bg='coral2', text='<--', command=Back_page7_Oscillations)
                                    Back_page7_Oscillations.pack()
                                    Back_page7_Oscillations.place(relx=.0,rely=.0)
                                    
                                    def page8_Oscillations():
                                        global phy_page8_Oscillations
                                        phy_page8_Oscillations=Toplevel()
                                        phy_page8_Oscillations.title('Oscillations')
                                        canvas_page8_Oscillations=Canvas(phy_page8_Oscillations, width=1500, height=900, bg='white')
                                        canvas_page8_Oscillations.pack(expand=YES,fill=BOTH)
                
                                        canvas_page8_Oscillations.create_text(270,60,text='Simple Pendulum', font=('Yu Gothic UI Semibold',24), fill = 'black')
                                        canvas_page8_Oscillations.create_text(500,130,text='''
                                                                              A simple pendulum consists of a heavy point mass suspended from a rigid support by means of an elastic inextensible string.
                                                                              The time period of the simple pendulum is given by :
                                                                              T = 2π √l / g''', font=('Yu Gothic UI Light',18), fill = 'black')
                                        
                                        global simplependulum
                                        simplependulum = tkinter.PhotoImage(file="simplependulum.png")
                                        button = Button(phy_page8_Oscillations, image = simplependulum ,width=107, height=138, font=("Courier",20,"bold"), bg='#94ffe2') 
                                        button.configure(image = simplependulum)
                                        button.place(relx = 0.15, rely = 0.35, anchor = CENTER)
                                        
                                        canvas_page8_Oscillations.create_text(500,550,text='''
                                                                              where l = effective length of the pendulum and g = acceleration due to gravity.
                                                                              
                                                                              If the effective length l of simple pendulum is very large and comparable with the radius of earth (R), then its time period is 
                                                                              given by:
                                                                              T = 2π √Rl / (l + R)g
                                                                              
                                                                              For a simple pendulum of infinite length (l >> R)
                                                                              T = 2π √R / g = 84.6 min
                                                                              For a simple pendulum of length equal to radius of earth,
                                                                              T = 2π √R / g = 60 min''', font=('Yu Gothic UI Light',18), fill = 'black')
                                        
                                        def Back_page8_Oscillations():
                                            phy_page8_Oscillations.destroy()
                        
                                        Back_page8_Oscillations=Button(phy_page8_Oscillations, bg='coral2', text='<--', command=Back_page8_Oscillations)
                                        Back_page8_Oscillations.pack()
                                        Back_page8_Oscillations.place(relx=.0,rely=.0)
                                        
                                        def page9_Oscillations():
                                            phy_page9_Oscillations=Tk()
                                            phy_page9_Oscillations.title('Oscillations')
                                            canvas_page9_Oscillations=Canvas(phy_page9_Oscillations, width=1500, height=900, bg='white')
                                            canvas_page9_Oscillations.pack(expand=YES,fill=BOTH)
                                            
                                            canvas_page9_Oscillations.create_text(460,300,text='''
                                                                                  If the bob of the simple pendulum is suspended by a metallic wire of length l, having coefficient of linear expansion α, then
                                                                                  due to increase in temperature by dθ, then
                                                                                  Effective length l’ = l (1 + α dθ)
                                                                              
                                                                                  When a bob of simple pendulum of density ρ oscillates in a fluid of density ρo (ρo < p), then time period get increased.
                                                                                  Increased time period T’ = T √ρ / ρ – ρo
                                                                                  
                                                                                  When simple pendulum is in a horizontally accelerated vehicle, then its time period is given by
                                                                                  T = 2π √1 / √(a2 + g2)
                                                                                  where a = horizontal acceleration of the vehicle.
                                                                                  
                                                                                  When simple pendulum is in a vehicle sliding down an inclined plane, then its time period is given by
                                                                                  T = 2π √l / g cos θ
                                                                                  Where θ = inclination of plane.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                
                                            canvas_page9_Oscillations.create_text(270,600,text='Second’s Pendulum:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                            canvas_page9_Oscillations.create_text(330,670,text='''
                                                                                  A simple pendulum having time period of 2 second is called second’s Pendulum.
                                                                                  
                                                                                  •  The effective length of a second’s pendulum is 99.992 em of approximately 1 metre on earth.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                
                                            def Back_page9_Oscillations():
                                                phy_page9_Oscillations.destroy()
                        
                                            Back_page9_Oscillations=Button(phy_page9_Oscillations, bg='coral2', text='<--', command=Back_page9_Oscillations)
                                            Back_page9_Oscillations.pack()
                                            Back_page9_Oscillations.place(relx=.0,rely=.0)
                                            
                                            def page10_Oscillations():
                                                global phy_page10_Oscillations
                                                phy_page10_Oscillations=Toplevel()
                                                phy_page10_Oscillations.title('Oscillations')
                                                canvas_page10_Oscillations=Canvas(phy_page10_Oscillations, width=1500, height=900, bg='white')
                                                canvas_page10_Oscillations.pack(expand=YES,fill=BOTH)
                
                                                canvas_page10_Oscillations.create_text(260,70,text='Torsional Pendulum:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                canvas_page10_Oscillations.create_text(60,120,text='''
                                                                                       Time period of torsional pendulum is given by
                                                                                       T = 2π √I / C''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                
                                                global torsional
                                                torsional = tkinter.PhotoImage(file="torsional.png")
                                                button = Button(phy_page10_Oscillations, image = torsional ,width=70, height=117, font=("Courier",20,"bold"), bg='#94ffe2') 
                                                button.configure(image = torsional)
                                                button.place(relx = 0.2, rely = 0.28, anchor = CENTER)
                                                
                                                canvas_page10_Oscillations.create_text(190,330,text='''
                                                                                       where, I = moment of inertia of the body about the axis of rotation and
                                                                                       C = restoring couple per unit twist.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                
                                                canvas_page10_Oscillations.create_text(250,420,text='Spring Pendulum:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                canvas_page10_Oscillations.create_text(200,600,text='''
                                                                                       A point mass suspended from a massless (or light) spring constitutes
                                                                                       a spring pendulum. If the mass is once pulled downwards so as to stretch 
                                                                                       the spring and then released the system oscillated up and down about its 
                                                                                       mean position simple harmonically. 
                                                                                       Time period and frequency of oscillations are given by:
                                                                                       T = 2π √m / k or v = 1 / 2π √k / m
                                                                                       
                                                                                       If the spring is not light but has a definite mass ms, then it can be easily
                                                                                       shown that period of oscillation will be
                                                                                       T = 2π √(m + ms / 3) / k''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                
                                                global spring
                                                spring = tkinter.PhotoImage(file="spring.png")
                                                button = Button(phy_page10_Oscillations, image = spring ,width=71, height=226, font=("Courier",20,"bold"), bg='#94ffe2') 
                                                button.configure(image = spring)
                                                button.place(relx = 0.7, rely = 0.72, anchor = CENTER)
                                                
                                                def Back_page10_Oscillations():
                                                    phy_page10_Oscillations.destroy()
                                                    
                                                Back_page10_Oscillations=Button(phy_page10_Oscillations, bg='coral2', text='<--', command=Back_page10_Oscillations)
                                                Back_page10_Oscillations.pack()
                                                Back_page10_Oscillations.place(relx=.0,rely=.0)
                                                
                                                def page11_Oscillations():
                                                    global phy_page11_Oscillations
                                                    phy_page11_Oscillations=Toplevel()
                                                    phy_page11_Oscillations.title('Oscillations')
                                                    canvas_page11_Oscillations=Canvas(phy_page11_Oscillations, width=1500, height=900, bg='white')
                                                    canvas_page11_Oscillations.pack(expand=YES,fill=BOTH)
                
                                                    canvas_page11_Oscillations.create_text(310,100,text='Vibrations of a Loaded Spring:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                    canvas_page11_Oscillations.create_text(390,260,text='''
                                                                                           When a spring is compressed or stretched through a small distance y from mean position, a restoring force acts on it.
                                                                                           
                                                                                           Restoring force (F) = – ky
                                                                                           where k = force constant of spring.
                                                                                           This is also called Hooke’s law.
                                                                                           
                                                                                           Time period of a loaded spring is given by
                                                                                           T = 2π √m / k''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                    
                                                    global loadedspring
                                                    loadedspring = tkinter.PhotoImage(file="loadedspring.png")
                                                    button = Button(phy_page11_Oscillations, image = loadedspring ,width=207, height=207, font=("Courier",20,"bold"), bg='#94ffe2') 
                                                    button.configure(image = loadedspring)
                                                    button.place(relx = 0.52, rely = 0.37, anchor = CENTER)
                                                    
                                                    canvas_page11_Oscillations.create_text(340,600,text='''
                                                                                           When two springs of force constants k1 and k2 are connected in parallel to mass m as shown in figure, then
                                                                                           
                                                                                           i) Effective force constant of the spring combination
                                                                                              k = k1 + k2
                                                                                              
                                                                                          ii) Time period T = 2π √m / (k1 + k2)''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                    
                                                    def Back_page11_Oscillations():
                                                        phy_page11_Oscillations.destroy()
                        
                                                    Back_page11_Oscillations=Button(phy_page11_Oscillations, bg='coral2', text='<--', command=Back_page11_Oscillations)
                                                    Back_page11_Oscillations.pack()
                                                    Back_page11_Oscillations.place(relx=.0,rely=.0)
                                                    
                                                    def page12_Oscillations():
                                                        global phy_page12_Oscillations
                                                        phy_page12_Oscillations=Toplevel()
                                                        phy_page12_Oscillations.title('Oscillations')
                                                        canvas_page12_Oscillations=Canvas(phy_page12_Oscillations, width=1500, height=900, bg='white')
                                                        canvas_page12_Oscillations.pack(expand=YES,fill=BOTH)
                                                        
                                                        canvas_page12_Oscillations.create_text(300,150,text='''
                                                                                               When two springs of force constant k1 and k2 are connected in series to mass m as shown in figure, then
                                                                                               
                                                                                               i) Effective force constant of the spring combination
                                                                                                  1 / k = 1 / k1 + 1 / k2
                                                                                                  
                                                                                              ii) Time period T = 2π √m(k1 + k2) / k1k2''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                                                                  
                                                        global loadedspring2
                                                        loadedspring2 = tkinter.PhotoImage(file="loadedspring2.png")
                                                        button = Button(phy_page12_Oscillations, image = loadedspring2 ,width=70, height=224, font=("Courier",20,"bold"), bg='#94ffe2') 
                                                        button.configure(image = loadedspring2)
                                                        button.place(relx = 0.5, rely = 0.3, anchor = CENTER)
                                                        
                                                        canvas_page12_Oscillations.create_text(220,410,text='Free Oscillations:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                        canvas_page12_Oscillations.create_text(380,480,text='''
                                                                                               When a body which can oscillate about its mean position is displaced from mean position and then released, it oscillates
                                                                                               about its mean position. These oscillations are called free oscillations and the frequency of oscillations is called natural 
                                                                                               frequency''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                        
                                                        canvas_page12_Oscillations.create_text(240,580,text='Damped Oscillations:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                        canvas_page12_Oscillations.create_text(180,610,text='''
                                                                                               Oscillations with a decreasing amplitude with time are called damped oscillations.''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                        
                                                        canvas_page12_Oscillations.create_text(265,680,text='Un-damped Oscillations:', font=('Yu Gothic UI Semibold',22), fill = 'black')
                                                        canvas_page12_Oscillations.create_text(185,710,text='''
                                                                                               Oscillations with a constant amplitude with time are called un-damped oscillations''', font=('Yu Gothic UI Light',18), fill = 'black')
                                                        
                                                        def Back_page12_Oscillations():
                                                            phy_page12_Oscillations.destroy()
                        
                                                        Back_page12_Oscillations=Button(phy_page12_Oscillations, bg='coral2', text='<--', command=Back_page12_Oscillations)
                                                        Back_page12_Oscillations.pack()
                                                        Back_page12_Oscillations.place(relx=.0,rely=.0)
                                                        
                                                        def Back_to_class11_Oscillations():
                                                            phy_Oscillations.destroy()
                                                            phy_page2_Oscillations.destroy()
                                                            phy_page3_Oscillations.destroy()
                                                            phy_page4_Oscillations.destroy()
                                                            phy_page5_Oscillations.destroy()
                                                            phy_page6_Oscillations.destroy()
                                                            phy_page7_Oscillations.destroy()
                                                            phy_page8_Oscillations.destroy()
                                                            phy_page9_Oscillations.destroy()
                                                            phy_page10_Oscillations.destroy()
                                                            phy_page11_Oscillations.destroy()
                                                            phy_page12_Oscillations.destroy()
                                                            
                                                        Back_to_class11_Oscillations= Button(phy_page12_Oscillations,bg='coral2', text='Class 11',font=('Castellar',18), command=Back_to_class11_Oscillations)
                                                        Back_to_class11_Oscillations.pack()
                                                        Back_to_class11_Oscillations.place(relx=.87,rely=.85)
                                                                
                                                    page12_Oscillations=Button(phy_page11_Oscillations, bg='coral2', text='-->', command=page12_Oscillations)
                                                    page12_Oscillations.pack()
                                                    page12_Oscillations.place(relx=.98,rely=.0)
                            
                                                page11_Oscillations=Button(phy_page10_Oscillations, bg='coral2', text='-->', command=page11_Oscillations)
                                                page11_Oscillations.pack()
                                                page11_Oscillations.place(relx=.98,rely=.0)
                            
                                            page10_Oscillations=Button(phy_page9_Oscillations, bg='coral2', text='-->', command=page10_Oscillations)
                                            page10_Oscillations.pack()
                                            page10_Oscillations.place(relx=.98,rely=.0)
                            
                                        page9_Oscillations=Button(phy_page8_Oscillations, bg='coral2', text='-->', command=page9_Oscillations)
                                        page9_Oscillations.pack()
                                        page9_Oscillations.place(relx=.98,rely=.0)
                            
                                    page8_Oscillations=Button(phy_page7_Oscillations, bg='coral2', text='-->', command=page8_Oscillations)
                                    page8_Oscillations.pack()
                                    page8_Oscillations.place(relx=.98,rely=.0)
                            
                                page7_Oscillations=Button(phy_page6_Oscillations, bg='coral2', text='-->', command=page7_Oscillations)
                                page7_Oscillations.pack()
                                page7_Oscillations.place(relx=.98,rely=.0)
                            
                            page6_Oscillations=Button(phy_page5_Oscillations, bg='coral2', text='-->', command=page6_Oscillations)
                            page6_Oscillations.pack()
                            page6_Oscillations.place(relx=.98,rely=.0)
                            
                        page5_Oscillations=Button(phy_page4_Oscillations, bg='coral2', text='-->', command=page5_Oscillations)
                        page5_Oscillations.pack()
                        page5_Oscillations.place(relx=.98,rely=.0)
                
                    page4_Oscillations=Button(phy_page3_Oscillations, bg='coral2', text='-->', command=page4_Oscillations)
                    page4_Oscillations.pack()
                    page4_Oscillations.place(relx=.98,rely=.0)
                
                page3_Oscillations=Button(phy_page2_Oscillations, bg='coral2', text='-->', command=page3_Oscillations)
                page3_Oscillations.pack()
                page3_Oscillations.place(relx=.98,rely=.0)
                
            page2_Oscillations=Button(phy_Oscillations, bg='coral2', text='-->', command=page2_Oscillations)
            page2_Oscillations.pack()
            page2_Oscillations.place(relx=.98,rely=.0)
                        
        KinematicsLawsofmotion=Button(phy_class11, height=1, width=29, bg='coral2', text='Kinematics and Laws of motion', font=('Castellar',27), command=Kinematics_and_laws_of_motion)
        Gravitation11=Button(phy_class11, height=1, width=12, bg='coral2', text='Gravitation', font=('Castellar',27), command=Gravitation11)
        Oscillations=Button(phy_class11, height=1, width=12, bg='coral2', text='Oscillations', font=('Castellar',27), command=Oscillations)
        Quiz11=Button(phy_class11, height=1, width=8, bg='coral2', text='Quiz', font=('Castellar',27), command=Quiz11)        
        KinematicsLawsofmotion.pack()
        KinematicsLawsofmotion.place(relx=.24,rely=.25)
        Gravitation11.pack()
        Gravitation11.place(relx=.38,rely=.40)
        Oscillations.pack()
        Oscillations.place(relx=.38,rely=.55)
        Quiz11.pack()
        Quiz11.place(relx=.42,rely=.70)
        
        Back_class11=Button(phy_class11, bg='coral2', text='<--', command=Back11 )
        Back_class11.pack()
        Back_class11.place(relx=.0,rely=.0)
                
    def Class12():
        phy_class12=Tk()
        phy_class12.title('Class 12')
        canvas_class12=Canvas(phy_class12, width=1500, height=900, bg='grey12')
        canvas_class12.pack(expand=YES,fill=BOTH)
        
        def Back12():
            phy_class12.destroy()
        
        def Quiz12():
            phy_Quiz12=Tk()
            phy_Quiz12.title('Quiz')
            canvas_Quiz12=Canvas(phy_Quiz12, width=1500, height=900, bg='grey12')
            canvas_Quiz12.pack(expand=YES,fill=BOTH)
            
            def play():
                import PlayQuiz12
                PlayQuiz12.PlayQuiz()
                
            play12=Button(phy_Quiz12, bg='coral2',font=('Castellar',30), text='Play Quiz', command=play)
            play12.pack()
            play12.place(relx=.40,rely=.35)
            
            def add():
                import Quiz12
                
            quiz12=Button(phy_Quiz12, bg='coral2', font=('Castellar',30),text='Add Questions', command=add)
            quiz12.pack()
            quiz12.place(relx=.36,rely=.55)
            
            def Back_Quiz12():
                phy_Quiz12.destroy()
            
            Back_Quiz12=Button(phy_Quiz12, bg='coral2', text='<--', command=Back_Quiz12)
            Back_Quiz12.pack()
            Back_Quiz12.place(relx=.0,rely=.0)
                    
        #chapters of class 12
        def Electrostatics():
            phy_Electrostatics=Tk()
            phy_Electrostatics.title('Electrostatics')
            canvas_Electrostatics=Canvas(phy_Electrostatics, width=1500, height=900, bg='white')
            canvas_Electrostatics.pack(expand=YES,fill=BOTH)
            
            canvas_Electrostatics.create_text(700,300, text='''
Electrostatics is the study of electric charges at rest. Coulomb's Law explains the Relationship between two or more electric charges.
 In electrostatics, we do not concern with the movement of charges.

    Electrostatics involves electric charges, the forces acting on them, and their behavior in substances.

Electrostatics, as we study today, depends on the nature of electric charges. Nature of charges depends on the models of 
atom proposed by Ernest Rutherford and Niels Bohr. According to their theories, an atom consists of two types of charges: 
    positively charged protons in a nucleus surrounded by negatively charged electrons. A neutral atom has equal numbers of electrons and protons.

What we study under electrostatics is static electricity. The charges at rest develop due to friction when we rub two insulating 
bodies against each other.

Some industrial applications of electrostatics are:

  ->  In designing electrostatics generators like Van de Graff generator
  ->  In electrostatic spraying of paints, powders etc.
  ->  In the design of cathode ray tubes for radar, television etc.
  ->  Ink-jet printing
  ->  Understanding lightning that strikes from the cloud base to the ground.
  ->  Adhesive forces of glue associated with surface tension, all are electric in nature
''', font=('Times New Roman',14), fill='black')
                
            def electro_page1():
                phy_electro_page1=Tk()
                phy_electro_page1.title('Electrostatics')
                canvas_electro_page1=Canvas(phy_electro_page1, width=1500, height=900, bg='white')
                canvas_electro_page1.pack(expand=YES,fill=BOTH)
                canvas_electro_page1.create_text(700, 100, text='Electric Charge', font=('Times New Roman',18), fill='black')
                canvas_electro_page1.create_text(700,200, text='''
Electric charge is a fundamental property associated with elementary particles. It accompanies fundamental particles whenever 
that exists. Electron, proton, neutrons are a few examples of fundamental particles.

The charge is something possessed by material objects that make it possible for them to exert electrical forces and 
to respond to electrical force.''', font=('Times New Roman',14), fill='black')
                canvas_electro_page1.create_text(700,300, text='Understand the concept of charge', font=('Times New Roman',16), fill='black')
                canvas_electro_page1.create_text(700,500, text='''
Often times students are unable to visualize electric charge. We know electric charge to be a fundamental property associated 
with elementary particles. This fundamental property is like characteristics or properties of other substances or objects. For 
example, you have a fountain pen. If you lift it in your hand you are able to feel its weight. Now we know that,
Weight W=m×g
where m is the mass of pen and g is acceleration due to the gravity of earth.
Now start thinking about mass. What is mass? It is nothing but a characteristic that the pen in question has. 
Can you see this mass? No, it is the material of the pen what you are able to see which might be plastic or metallic.
Again does the mass of the pen change when you move it to the moon or another planet. The answer is again no. The 
mass of the pen does not change. It is the wight of the pen that change because acceleration due to gravity g is 
different for both moon and earth. So mass is nothing but the fundamental property associated with different objects. We can now say
 that any object in the universe can have any number of characteristics or properties.

''', font=('Times New Roman',14), fill='black' )

                def electro_page2():
                    phy_electro_page2=Tk()
                    phy_electro_page2.title('Electrostatics')
                    canvas_electro_page2=Canvas(phy_electro_page2, width=1500, height=900, bg='white')
                    canvas_electro_page2.pack(expand=YES,fill=BOTH)
                    canvas_electro_page2.create_text(700,150, text='''
Now coming back to the question of charge let us try to understand with the example of an electron. For ease let us assume electron
 is static or is at rest. The electron is a particle and has certain characteristics or properties. Two properties of electrons are
1. It has mass
2. It has a negative charge.
Like the electron, we have another fundamental particle called a proton. Protons also have properties like
1. It has mass
2. It has a positive charge
So, the negative charge on the electron and a positive charge on a proton is a property of both electron and proton. We call a charge 
positive or negative only by convention to distinguish between two types of charges. We should never mistake negative and positive 
charges with additive or subtractive sign.''', font=('Times New Roman',14), fill='black' )
                    canvas_electro_page2.create_text(700,300, text='Where does charge come from?', font=('Times New Roman',16), fill='black')
                    canvas_electro_page2.create_text(700,400, text='''
The electric charge on a body comes as a result of transferring of electrons from one body to another. This way one body has an excess 
and the other a deficiency of electrons. Electrons are very small particles that have a negative charge. Sir J.J. Thomson discovered electrons.
    To give a body an excess negative charge, we may add some electrons. And to give an excess of positive charge, we may remove the 
    electrons from the body.
It is important to note here that the “Charge” of a body refers to its excess charge only. The excess charge is always a very small fraction 
of the total positive or negative charge in the body as a whole.
Electric Charge is a property of the material of a given body like mass in mechanics.
Note:- symbol 'Q' or 'q' represents the electric charge''', font=('Times New Roman',14), fill='black')
                    canvas_electro_page2.create_text(700,580, text='''
We know that in an atom electrons revolve around a nucleus which has a positive charge. Electric charge is the property responsible 
for electric forces acting between nucleus and electrons in an atom. This electric force between the nucleus and electrons bind the atom together.
Charges are of two kinds
(i) negative charge
(ii) positive charge''', font=('Times New Roman',14), fill='black')

                    def electro_page3():
                        phy_electro_page3=Tk()
                        phy_electro_page3.title('Electrostatics')
                        canvas_electro_page3=Canvas(phy_electro_page3, width=1500, height=900, bg='white')
                        canvas_electro_page3.pack(expand=YES,fill=BOTH)
                        canvas_electro_page3.create_text(700,100, text='''
In an atom electron are particles having a negative charge? The nucleus consists of protons and neutrons. In a nucleus of an atom, 
protons have a positive charge and neutrons are neutral. The experiments lead to the fundamental results that''', font=('Times New Roman',14), fill='black')
                        canvas_electro_page3.create_text(700,250, text='LIKE CHARGES REPEL', font=('Times New Roman',14), fill='black')
                        canvas_electro_page3.create_text(700,550, text='UNLIKE CHARGES ATTRACT',font=('Times New Roman',14), fill='black'  )
                        canvas_electro_page3.create_oval(560,290,600,330, outline='black', fill='orange')
                        canvas_electro_page3.create_oval(800,290,840,330, outline='black', fill='orange')
                        canvas_electro_page3.create_text(580,310, text='+', font=('Times New Roman',14), fill='black')
                        canvas_electro_page3.create_text(820,310, text='+', font=('Times New Roman',14), fill='black')
                        
                        
                        
                        canvas_electro_page3.create_oval(560,410,600,450, outline='black', fill='orange')
                        canvas_electro_page3.create_oval(800,410,840,450, outline='black', fill='orange')
                        canvas_electro_page3.create_text(580,430, text='+', font=('Times New Roman',14), fill='black')
                        canvas_electro_page3.create_text(820,430, text='+', font=('Times New Roman',14), fill='black')
                        canvas_electro_page3.create_line(620,430,660,430, fill='black')
                        canvas_electro_page3.create_line(740,430,780,430, fill='black')
                        canvas_electro_page3.create_polygon(640,420,660,430,640,440, fill='black')
                        canvas_electro_page3.create_polygon(760,420,740,430,760,440, fill='black')
                        
                        canvas_electro_page3.create_oval(560,600,600,640, outline='black', fill='orange')
                        canvas_electro_page3.create_oval(800,600,840,640, outline='black', fill='orange')
                        canvas_electro_page3.create_text(580,620, text='+', font=('Times New Roman',14), fill='black')
                        canvas_electro_page3.create_text(820,610, text='_', font=('Times New Roman',14), fill='black')
                        canvas_electro_page3.create_line(620,620,780,620, fill='black')
                        canvas_electro_page3.create_polygon(760,610,780,620,760,630, fill='black')
                        
                        def electro_page4():
                            phy_electro_page4=Tk()
                            phy_electro_page4.title('Electrostatics')
                            canvas_electro_page4=Canvas(phy_electro_page4, width=1500, height=900, bg='white')
                            canvas_electro_page4.pack(expand=YES,fill=BOTH)
                            canvas_electro_page4.create_text(700,100,text='''
The electric force between two electrons is the same as the electric force between two protons kept at the 
same distance apart. That is both sets repel each other.
The electric force between an electron and proton placed at the same distance apart is not repulsive but attractive in nature.
Assignment of a negative charge on the electron and a positive charge on a proton is only a convention. It does not mean that 
charge on an electron is less than that on the proton. Importance of electric forces is that it encompasses almost every field 
associated with our life. It is important because all matter around us consists of atoms or molecules in which 
electric charges are exactly balanced.''', font=('Times New Roman',14), fill='black' )
                            canvas_electro_page4.create_text(700,300, text='Unit of Charge', font=('Times New Roman',16), fill='black')
                            canvas_electro_page4.create_text(700,400, text='''
-> The charge on a system can be measured by comparing it with the charge on a standard body.
-> SI unit of charge is Coulomb written as C.
-> Coulomb is the charge flowing through the wire in 1 second if the electric current in it is 1A.
-> Charge on electron is e=−1.602×10−19C
    and charge on proton is positive of this value.''', font=('Times New Roman',14), fill='black')
                            
                            def electro_page5():
                                phy_electro_page5=Tk()
                                phy_electro_page5.title('Electrostatics')
                                canvas_electro_page5=Canvas(phy_electro_page5, width=1500, height=900, bg='white')
                                canvas_electro_page5.pack(expand=YES,fill=BOTH)
                                canvas_electro_page5.create_text(700,100, text='Conductors and Insulators', font=('Times New Roman',18), fill='black')
                                canvas_electro_page5.create_text(700,400, text='''
There is a category of materials in which electric charges can flow easily while in other materials charges cannot flow easily. 
Substances through which electric charges can flow easily are called conductors. All metals like copper, aluminium etc. are good 
conductors of electricity.
Substances through which electric charges cannot flow are called insulators. Few examples of insulating materials are glass, rubber, 
mica, plastic, dry wood etc.
Presence or absence of free electrons in a material makes it a conductor or insulator. Conductors have free electrons which are 
loosely held by nuclei of their atoms. Insulators do not have free electrons. In insulators, electrons are strongly held by nuclei of their atoms.

It is important to note that
1. The charge transferred to a conductor gets distributed over the entire surface.
2. The charge transferred to an insulator stays at the same place.

Semiconductors are the third class of materials. Electrical properties of semiconductors are somewhat between insulators 
and conductors. Silicon and germanium are examples of semiconductors.


Question 1. Why do metals conduct electricity?

Answer. Atoms of metals have outer electrons which are not tied to any one atom. These electrons can move freely within the 
structure of a metal when an electric current is applied. That is why metals conduct electricity.''', font=('Times New Roman',14), fill='black')
                                
                                def electro_page6():
                                    phy_electro_page6=Tk()
                                    phy_electro_page6.title('Electrostatics')
                                    canvas_electro_page6=Canvas(phy_electro_page6, width=1500, height=900, bg='white')
                                    canvas_electro_page6.pack(expand=YES,fill=BOTH)
                                    canvas_electro_page6.create_text(700, 100, text='What happens when a body is charged?', font=('Times New Roman',18), fill='black')
                                    canvas_electro_page6.create_text(700, 200, text='''
Case 1: Body has a positive charge
When the body has a positive charge, it means electrons are somehow removed from the body. This results also in a decrease of mass of 
the body. The decrease in the mass of the body equals the total mass of electrons removed from the body.

Case 2: Body has a negative charge
When the body has a negative charge, it means electrons are somehow added to the body. This results in an increase of mass of the body. 
Increase in the mass of the body equals the total mass of electrons added to the body.''', font=('Times New Roman',14), fill='black')
                                    canvas_electro_page6.create_text(700,350, text='METHODS OF CHARGING ', font=('Times New Roman',18), fill='black')
                                    canvas_electro_page6.create_text(700,400, text='There are three main methods for charging of a body', font=('Times New Roman',14), fill='black')
                                    canvas_electro_page6.create_text(700,450, text='(i) Charging by rubbing and Fractional electricity:-',font=('Times New Roman',16), fill='black')
                                    canvas_electro_page6.create_text(700,550, text='''
Rubbing as the term suggest is moving two things back and forth against each other. The simplest way to experience electric charge 
is to rub certain bodies among each other. Rubbing or friction makes electrons move. This gives one material a positive charge and 
the other a negative charge. The charges stay on the surfaces of the materials until they can flow or they discharge.
If we pass a comb through hairs, comb becomes charged and can attract small pieces of paper. This is because the comb might have 
lost its electrons or acquired some electrons when we rub it with hairs. Now, this comb is a charged body. The net charge on the 
comb interacts with the net charge on small pieces of paper which results in attraction. Many such solid materials are known which 
on rubbing attract light objects like a light feather, bits of papers, straw etc.''', font=('Times New Roman',14), fill='black')
                    
                                    def electro_page7():
                                        global phy_electro_page7
                                        phy_electro_page7=Toplevel()
                                        phy_electro_page7.title('Electrostatics')
                                        canvas_electro_page7=Canvas(phy_electro_page7, width=1500, height=900, bg='white')
                                        canvas_electro_page7.pack(expand=YES,fill=BOTH)
                                        canvas_electro_page7.create_text(700,300, text='''
Explanation of appearance of electric charge on rubbing is simple. Material bodies consist of a large number of electrons and 
protons in equal number and hence is in neutral in their normal state. But when a glass rod is rubbed with a silk cloth, electrons 
are transferred from glass rod to silk cloth. The glass rod becomes positively charged and the silk cloth becomes negatively charged 
as it receives extra electrons from the glass rod. In this case rod after rubbing, comb after passing through dry hairs becomes 
electrified and these are the example of frictional electricity.''', font=('Times New Roman',14), fill='black')
                                        canvas_electro_page7.create_text(700, 450, text='(ii) Charging by induction (Electrostatic Induction):-', font=('Times New Roman',16), fill='black')
                                        canvas_electro_page7.create_text(700,500, text='''The temporary electrification of a conductor, when a charged body is brought near it is called electrostatic induction.''', font=('Times New Roman',14), fill='black')
                                        global img1
                                        img1 = tkinter.PhotoImage(file="chargingbyfriction.png")
                                        button = Button(canvas_electro_page7,image = img1,width=500,height=220,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                                        button.configure(image = img1)
                                        button.place(relx=0.50,rely=0.18,anchor = CENTER)
                                        
                                        def electro_page8():
                                            global phy_electro_page8
                                            phy_electro_page8=Toplevel()
                                            phy_electro_page8.title('Electrostatics')
                                            canvas_electro_page8=Canvas(phy_electro_page8, width=1500, height=900, bg='white')
                                            canvas_electro_page8.pack(expand=YES,fill=BOTH)
                                            canvas_electro_page8.create_text(700,400, text='''
When a body is charged this way there is no transfer of electrons from one body to other. This happens because there is no physical 
contact taking place between charging body and conductor being charged.
If a charged body is brought near an uncharged body, then the neutral body becomes oppositely charged. By induction method, we can 
charge any type of material body.''', font=('Times New Roman',14), fill='black')
                                            canvas_electro_page8.create_text(700,500, text='(iii) By conduction (by touch without rubbing):-', font=('Times New Roman',16), fill='black')
                                            canvas_electro_page8.create_text(700,550, text='''
Because of having excess free electrons in metals they can be charged by conduction. When we bring two conductors, one charged and 
other uncharged in contact, the same type of charge will appear on both the conductors.''', font=('Times New Roman',14), fill='black')
                                            global inductimg
                                            inductimg = tkinter.PhotoImage(file="induct.gif")
                                            button = Button(canvas_electro_page8,image = inductimg,width=650,height=350,font=("Courier",20,"bold"),bg='#94ffe2')#,command=lambda:back(canvas2) 
                                            button.configure(image = inductimg)
                                            button.place(relx=0.50,rely=0.25,anchor = CENTER)
                                            
                                            def electro_page9():
                                                phy_electro_page9=Tk()
                                                phy_electro_page9.title('Electrostatics')
                                                canvas_electro_page9=Canvas(phy_electro_page9, width=1500, height=900, bg='white')
                                                canvas_electro_page9.pack(expand=YES,fill=BOTH)
                                                canvas_electro_page9.create_text(700,100, text='Basic properties of electric charge', font=('Times New Roman',20), fill='black')
                                                canvas_electro_page9.create_text(700,150, text='(i) Additivity of charges', font=('Times New Roman',16), fill='black')
                                                canvas_electro_page9.create_text(700,250, text='''
Charges adds up like real numbers i. e., they are Scalars more clearly if any system has n number of charges q1, q2, q3, qn then 
total charge of the system is q=q1+q+2+q3+................qn.
Proper sign have to be used while adding the charges for example if
q1=+1C, q2=−2C and q3=+4C
then total charge of the system is
q=q1+q2+q3
or
q=(+1)+(−2)+(+4)C=(+3)C''', font=('Times New Roman',14), fill='black')
                                                canvas_electro_page9.create_text(700,370, text='(ii) conservation of charge :', font=('Times New Roman',16), fill='black')
                                                canvas_electro_page9.create_text(700, 420, text='''
Charge is conserved Charge of an isolated system is conserved. Charge can not be created or destroyed but charged particles can 
be created or destroyed.''', font=('Times New Roman',14), fill='black')
                                                canvas_electro_page9.create_text(700,480, text='(iii) Quantization of charge', font=('Times New Roman',16), fill='black')
                                                canvas_electro_page9.create_text(700, 550, text='''
All free charges are integral multiples of a unit of charge ‘e’, where e=−1.602×10−19C i. e., charge on an electron or proton. 
Thus charge q on a body is always denoted by
q = one where n = any integer positive or negative''', font=('Times New Roman',14), fill='black')
                                                
                                                def electro_page10():
                                                    phy_electro_page10=Tk()
                                                    phy_electro_page10.title('Electrostatics')
                                                    canvas_electro_page10=Canvas(phy_electro_page10, width=1500, height=900, bg='white')
                                                    canvas_electro_page10.pack(expand=YES,fill=BOTH)
                                                    canvas_electro_page10.create_text(700,100, text='Electrical Force', font=('Times New Roman',18), fill='black')
                                                    canvas_electro_page10.create_text(700, 400, text='''
Electric force is one of the interactions among particles we observe in nature. The very nature of matter depends on these electrical 
forces. Four basic interactions occurring between elementary particles are
  1.  The gravitational force
  2.  The electromagnetic force
  3.  The strong nuclear forces
  4.  The weak nuclear forces.
At this present level, you are familiar with gravitational forces. We will explore what are electric forces. It is the force of 
attraction that acts between all particles(or bodies) having mass. So, if we have two bodies of mass m1and m2 kept at a distance r
from each other then from Newton's law of gravitation,
F=Gm1m2/r^2
where G is Universal Gravitational Constant. Above equation gives the magnitude of force exerted by m1 on m2. Mass m2 also exert 
an equal and opposite force mass m1. From the above equation, we can see that Gravitational forces are inverse square in nature. 
It decreases inversely as the square of the distance between the two masses.

The electric force also varies inversely as the square of the distance between charge. It is billions of time stronger than the 
gravitational force. From the description of electric charges, we know that there are two kinds of charged matter. One is positive 
and another one is negative. We also know that like charges repel and unlike charges attract each other. Gravitational interaction 
in contrast only attract masses which are kept at a distance from each other. On atomic and molecular level gravitational forces 
play no role. This is because electric forces are very strong. The electric repulsion between two protons is 10^35 times stronger 
than the gravitational interaction between them.''', font=('Times New Roman',14), fill='black')
                                                    
                                                    def electro_page11():
                                                        phy_electro_page11=Tk()
                                                        phy_electro_page11.title('Electrostatics')
                                                        canvas_electro_page11=Canvas(phy_electro_page11, width=1500, height=900, bg='white')
                                                        canvas_electro_page11.pack(expand=YES,fill=BOTH)
                                                        canvas_electro_page11.create_text(700,100, text='''
Now if you try to bring a bunch of positive charges together they would repel with an enormous force. They will then spread out 
in all directions. The same thing happens with negative charges.
What if you try to bring even mixture of positive and negative charges? The answer is they would be pulled together by an 
enormous force of attraction. If the net amount of positive and negative charges in the mixture is equal then these forces 
would balance and mixture becomes neutral.''',font=('Times New Roman',14), fill='black')
                                                        canvas_electro_page11.create_text(700,250, text='Electrical force definition', font=('Times New Roman',18), fill='black')
                                                        canvas_electro_page11.create_text(700,400, text='''
These forces (explained above) acting between charges are Electrical forces. The force on a charged particle due to the electric 
field in its vicinity is the electric force.
All matter we see around us consists of positive protons and negative electrons. They are attracting and repelling each other 
with electric force. In matter around us, these electrical forces balance out so perfectly that we did not feel any force at all. 
The electric field - and hence the electric force - can change over time, if the charge particles generating the field are moving. 
An electric field does not have to be static.
Electromagnetic interactions involve moving charges. It includes both electric and magnetic forces. We already learned about 
electric forces. Magnetic forces are forces acting between magnets. It occurs between a magnet and a piece of iron. These are 
the result of electric charges in motion. So, both electric and magnetic phenomenon can be derived from charged particles.

Strong interactions are responsible for holding the nucleus of an atom target. It counters the repulsion between protons in a 
nucleus. The range of weak interactions is very short. Weak interaction between sub-atomic particles causes radioactive decay 
and thus plays an important role in nuclear fission''', font=('Times New Roman',14), fill='black')
                                                        
                                                        def electro_page12():
                                                            phy_electro_page12=Tk()
                                                            phy_electro_page12.title('Electrostatics')
                                                            canvas_electro_page12=Canvas(phy_electro_page12, width=1500, height=900, bg='white')
                                                            canvas_electro_page12.pack(expand=YES,fill=BOTH)
                                                            canvas_electro_page12.create_text(700,100, text='Electrical force examples', font=('Times New Roman',18), fill='black')
                                                            canvas_electro_page12.create_text(700,200, text='''
There is much electric force example that we came across in our day to day life. Some are
(a) Woolen clothing:-
When taking off woollen clothing rubbing of woollens against other clothing items makes it negatively charged. A noise and slight 
zap occur when wool neutralises this excess charge.
(b) Adhesive forces of glue associated with surface tension, all are electric in nature
(c) Forces behind lightning that strikes from the cloud base to the ground are electric in nature.''', font=('Times New Roman',14), fill='black')
                                                            canvas_electro_page12.create_text(700,350, text='Electrostatic Force', font=('Times New Roman',18), fill='black')
                                                            canvas_electro_page12.create_text(700,400, text='''
If all the charged particles under observation are stationary, then the corresponding force on the charged particles is an 
electrostatic force. If certain electrical insulator materials are rubbed electrostatic charge is developed on them. We 
discussed it under topic charging by rubbing.''', font=('Times New Roman',14), fill='black')
                                                            
                                                            def electro_page13():
                                                                 phy_electro_page13=Tk()
                                                                 phy_electro_page13.title('Electrostatics')
                                                                 canvas_electro_page13=Canvas(phy_electro_page13, width=1500, height=900, bg='white')
                                                                 canvas_electro_page13.pack(expand=YES,fill=BOTH)
                                                                 canvas_electro_page13.create_text(700, 100, text="Coulomb's Law", font=('Times New Roman',20), fill='black')
                                                                 canvas_electro_page13.create_text(700,400, text='''
In 1785 the French physicist Charles Augustin Coulomb measured the electric force between small charged spheres using a torsion 
balance. He then formulated his observations in the form of Coulomb's Law. Coulomb's Law is an electrical analog of Newton's 
Universal Law of Gravitation. It states that
    The force of attraction or repulsion between two stationary point charges is
    (i) directly proportional to the product of the magnitude of two charges.
    (ii) inversely proportional to the square of the distance between them.
    This force acts along the line joining the two charges. 
    
Two charges are separated by a distance r. Then according to Coulomb's Law the force F of attraction or repulsion between them is,
F∝q1q2 and F∝1/r2
Therefore,
F∝q1q2/r^2                                      ---(1)
or,
F=kq1q2/r^2
where, k
is the constant of proportionality. The value of k depends on the nature of the medium between two charges and the system of 
units we choose to measure F, q1, q2 and r.''', font=('Times New Roman',14), fill='black')
                                                                 
                                                                 def electro_page14():
                                                                     phy_electro_page14=Tk()
                                                                     phy_electro_page14.title('Electrostatics')
                                                                     canvas_electro_page14=Canvas(phy_electro_page14, width=1500, height=900, bg='white')
                                                                     canvas_electro_page14.pack(expand=YES,fill=BOTH)
                                                                     canvas_electro_page14.create_text(700,200, text='''
In SI units system, when two charges are in vacuum or air
k=1/4πε0
where ε0 is absolute permittivity of free space. Value of this constant in vacuum is 8.85×10−12C2/Nm2. If we put the value of 
ε0 in above equation for k
we find
k=1/4πε0=1/4×π×8.85×10−12C^2/Nm^2=9×10^9Nm^2C^−2

So, from above equation (1) the force between two charges located in air or vacuum is given by,

F=1/4πε0 x q1q2/r^2=9×10^9 × q1q2/r^2
(in Newton)

Now if the charges are in a medium (glass, water etc.) other then air and vacuum then electric force between these two charges is
F=1/4πε x q1q2/r^2
where, ε is a constant and is the the permittivity of the medium in which charges are present. Since the value of ε depends 
on the medium, the magnitude of force on a charge also depends on the medium.

NOTE:-

    1. The direction of the force is along the line joining two charges. It can be inward or outward depending on attraction 
        or repulsion between the charges.
    2. Coulomb's Law of electrostatics holds for two or more point charges at rest.
    3. SI unit of permittivity is C^2/Nm^2. It can also be expressed as farad per meter (F/m).''', font=('Times New Roman',14), fill='black')
                                                                     
                                                                     def electro_page15():
                                                                         phy_electro_page15=Tk()
                                                                         phy_electro_page15.title('Electrostatics')
                                                                         canvas_electro_page15=Canvas(phy_electro_page15, width=1500, height=900, bg='white')
                                                                         canvas_electro_page15.pack(expand=YES,fill=BOTH)
                                                                         canvas_electro_page15.create_text(700,100, text='Unit of electric charge', font=('Times New Roman',18), fill='black')
                                                                         canvas_electro_page15.create_text(700,300, text='''
SI unit of charge is Coulomb. We know that the electrostatic force between two charges in a vacuum is,
F=1/4πε0 x q1q2/r^2
Now in the above equation if we put,
q1=q2=1C
and r=1m
, then
F=1/4πε0=9×10^9N
So, from the above formula, we can define 1 Coulomb as,
One Coulomb is that amount of charge that repels an equal and similar charge with a force of 9×109N
when placed in a vacuum at a distance of one meter from it.
In the cgs system unit of charge is esu of charge or statcoulomb.
One esu of charge is that charge which repels an identical charge in vacuum at a distance of 1 cm from it with a force of 1 dyne.
1Coulomb=3×10^9statcoulomb''', font=('Times New Roman',14), fill='black')
                                                                         
                                                                         def electro_page16():
                                                                             global phy_electro_page16
                                                                             phy_electro_page16=Toplevel()
                                                                             phy_electro_page16.title('Electrostatics')
                                                                             canvas_electro_page16=Canvas(phy_electro_page16, width=1500, height=900, bg='white')
                                                                             canvas_electro_page16.pack(expand=YES,fill=BOTH)
                                                                             canvas_electro_page16.create_text(700,100, text='Coulombs law in vector form', font=('Times New Roman',18), fill='black')
                                                                             canvas_electro_page16.create_text(700, 200, text='''
In this section we'll learn about Coulomb's Law in vector form. From mechanics we know that force is a vector quantity. 
So force has a magnitude as well as direction. Coulomb's law is the law of electrostatics force between electric charges. 
Like other types of forces electrostatic force expressed by Coulomb's Law has magnitude as well as direction.
The direction of force between two charges depends on whether charges under consideration are like charges or opposite 
charges. Let us now understand this statement with the help of the figure given below.''', font=('Times New Roman',14), fill='black')
                                                                             canvas_electro_page16.create_text(700,600, text='''
In figure (2a) we have two charged bodies P and Q. These charged bodies carry opposite charge i.e., P has a positive charge 
and Q has a negative charge. We know that opposite charges attract each other. So there is a force of attraction between bodies 
P and Q. Now P exerts a force on Q and this force acts towards body P that is towards the left. Now Q exerts a force on P and 
this force acts towards body Q that is towards the right.''', font=('Times New Roman',14), fill='black')
                                                                             canvas_electro_page16.create_oval(400,430,440,470, outline='black',fill='orange')
                                                                             canvas_electro_page16.create_oval(700,430,740,470, outline='black', fill='orange')
                                                                             for i in range(445,690,20):
                                                                                 canvas_electro_page16.create_line(i,450,i+10,450,fill='black')
                                                                             canvas_electro_page16.create_line(350,450,390,450, fill='blue')
                                                                             canvas_electro_page16.create_polygon(350,450,355,440,355,460, fill='blue')
                                                                             canvas_electro_page16.create_line(750,450,790,450, fill='blue')
                                                                             canvas_electro_page16.create_polygon(790,450,785,440,785,460, fill='blue')
                                                                             canvas_electro_page16.create_text(360,400,text='F12', font=('Times New Roman',12), fill='black')
                                                                             canvas_electro_page16.create_text(760,400, text='F21', font=('Times New Roman',12), fill='black')
                                                                             
                                                                             def electro_page17():
                                                                                 phy_electro_page17=Tk()
                                                                                 phy_electro_page17.title('Electrostatics')
                                                                                 canvas_electro_page17=Canvas(phy_electro_page17, width=1500, height=900, bg='white')
                                                                                 canvas_electro_page17.pack(expand=YES,fill=BOTH)
                                                                                 canvas_electro_page17.create_text(700,100, text='''
Again in figure (2b), we have two charged bodies P and Q. These charged bodies carry the same charge i.e., both P and Q have 
a positive charge. We know that the same charges repel each other. So there is a force of repulsion between bodies P and Q. 
Now P exerts a force on Q and this force acts away from body P that is towards the right. Now Q exerts a force on P and this 
force acts away from body Q that is towards the left.
Let us now express Coulomb's Law in Vector form. For this let us consider a figure given below''', font=('Times New Roman',14), fill='black')
                                                                                 canvas_electro_page17.create_text(700,500, text='''
Here we have two positive charges q1 and q2 kept at a distance r from each other. Since both q1 and q2 have a positive charge 
they both would repel each other. Again from Newton's Third Law, we know that for every action there is an equal and opposite 
reaction. So here when charge q1 exerts a force (action) on charge q2, the charge q2 also exerts an equal and opposite force 
(reaction) on charge q1. In vector form, Coulomb's law may be expressed as
⃗F21= Force on charge q2 due to q1
Now you can read subscript of force ⃗F21 to determine the direction of the force. Here direction of force is from q1 to q2.''', font=('Times New Roman',14), fill='black')
                                                                                 
                                                                                 def electro_page18():
                                                                                     global phy_electro_page_18
                                                                                     phy_electro_page18=Toplevel()
                                                                                     phy_electro_page18.title('Electrostatics')
                                                                                     canvas_electro_page18=Canvas(phy_electro_page18, width=1500, height=900, bg='white')
                                                                                     canvas_electro_page18.pack(expand=YES,fill=BOTH)
                                                                                     canvas_electro_page18.create_text(700,300, text='''
So in vector form we have
⃗F21=1/4πε0 x q1q2/r^2 r12
where, r12=⃗r12/r
is the unit vector in direction from q1 to q2.

So for force on charge q1 due to q2,
⃗F12 = Force on charge q1 due to q2

So in vector form we have
⃗F12=1/4πε0 x q1q2/r^2 r21
where, ^r21=⃗r21/r
is the unit vector in direction from q2 to q1.

The same way we can write the Coulomb's Law in vector form for Columbian forces between unlike charges which are attractive 
in nature. Figure below gives the direction of force acting on q1
and q2.''', font=('Times New Roman',14), fill='black')
                                                                                     
                                                                                     def electro_page19():
                                                                                         global phy_electro_page19
                                                                                         phy_electro_page19=Toplevel()
                                                                                         phy_electro_page19.title('Electrostatics')
                                                                                         canvas_electro_page19=Canvas(phy_electro_page19, width=1500, height=900, bg='white')
                                                                                         canvas_electro_page19.pack(expand=YES,fill=BOTH)
                                                                                         canvas_electro_page19.create_text(300,100, text='Force between two charges \n in terms of their position vectors', font=('Times New Roman',22), fill='black')
                                                                                         canvas_electro_page19.create_text(700,500, text='''
To express force between two point charges in terms of their position vectors, consider two point charges q1 and q2 at points 
P and Q respectively. From the figure given above we can see that position vectors of points P and Q are ⃗OP=→r1 and ⃗OQ=→r2. 
Let us now join these two point charges q1 and q2 through a straight line. Let r be the distance between these two point charges. 
Let ^r21 is the unit vector from charge q2 to q1, then force on charge q1 doe to q2 is given by ⃗F12=14πε0⋅q1q2r2^r21 We can 
rewrite above equation as ⃗F12=14πε0⋅q1q2r3(r^r21)(1) From the triangle law of vector addition we have →OQ+→QP=→OP or →QP=→OP−→OQ.
Since (→QP=r^r21),
So we have, r^r21=⃗r1−⃗r2 and r=|⃗r1−⃗r2|
In equation ⃗F12=14πε0⋅q1q2r3(r^r21)(2) putting
r^r21=⃗r1−⃗r2
and
r=|⃗r1−⃗r2| ,
we get ⃗F12=14πε0⋅q1q2(|⃗r1−⃗r2|)3(⃗r1−⃗r2)(3) Similarly we can find the force on charge q2 due to charge q1 as
 ⃗F21=14πε0⋅q1q2(|⃗r2−⃗r1|)3(⃗r2−⃗r1)''', font=('Times New Roman',14), fill='black')
                                                                                         global vecimg
                                                                                         vecimg = tkinter.PhotoImage(file="vectorform.png")
                                                                                         button = Button(phy_electro_page19,image = vecimg,width=310,height=322,font=("Courier",20,"bold"),bg='grey')#,command=lambda:back(canvas2) 
                                                                                         button.configure(image = vecimg)
                                                                                         button.place(relx=0.50,rely=0.25,anchor = CENTER)
                                                                                         
                                                                                         def electro_page20():
                                                                                             phy_electro_page20=Tk()
                                                                                             phy_electro_page20.title('Electrostatics')
                                                                                             canvas_electro_page20=Canvas(phy_electro_page20, width=1500, height=900, bg='white')
                                                                                             canvas_electro_page20.pack(expand=YES,fill=BOTH)
                                                                                             canvas_electro_page20.create_text(700,100, text='Coulomb\'s law formula', font=('Times New Roman',18), fill='black')
                                                                                             canvas_electro_page20.create_text(700, 300, text='''
From the above discussion, we have a fair knowledge of Coulomb's Law. It is a law explaining the electrostatic interaction 
between charged particles, objects or bodies. In this section, you get the gist of what we have studied so far. So, we 
have Coulomb's law formula which is given by the expression
Fv=1/4πε0 x q1q2/r^2=9×10^9 × q1q2/r^2
is in Newton
Above equation gives only the magnitude of the electrostatic force between two charged particles in vacuum.
If material medium exists between charged particles then we have
Fm=1/4πε x q1q2/r^2
Units used:- q1 and q2 are in Coulomb, F is in Newton and r is in metre.
Constant used:- k=14πε0=9×109Nm2C−2''', font=('Times New Roman',14), fill='black')
                                                                                             
                                                                                             def electro_page21():
                                                                                                 phy_electro_page21=Tk()
                                                                                                 phy_electro_page21.title('Electrostatics')
                                                                                                 canvas_electro_page21=Canvas(phy_electro_page21, width=1500, height=900, bg='white')
                                                                                                 canvas_electro_page21.pack(expand=YES,fill=BOTH)
                                                                                                 canvas_electro_page21.create_text(700, 100, text='Principle Of Superposition of electric charges', font=('Times New Roman',18), fill='black')
                                                                                                 canvas_electro_page21.create_text(700,250, text='''
We know that Coulomb's law gives the electric force acting between two electric charges. What method or principle should 
we apply if we want to calculate the forces between many charges?
Principle of superposition gives the method to find force on a charge when system consists of large number of charges.
According to this principle when multiple charges are interacting the total force on a given charge is vector sum of forces 
exerted on it by all other charges.
    This principle makes use of the fact that the forces with which two charges attract or repel one another are not affected 
    by the presence of other charges.

If a system of charges has n
number of charges say q1, q2, ...................., qn, then total force on charge q1 according to principle of superposition is
⃗F1=⃗F12+⃗F13+.......+⃗F1n
Where ⃗F12 is force on q1 due to q2 and ⃗F13 is force on q1 due to q3 and so on.''', font=('Times New Roman',14), fill='black')
                                                                                                 
                                                                                                 def electro_page22():
                                                                                                     phy_electro_page22=Tk()
                                                                                                     phy_electro_page22.title('Electrostatics')
                                                                                                     canvas_electro_page22=Canvas(phy_electro_page22, width=1500, height=900, bg='white')
                                                                                                     canvas_electro_page22.pack(expand=YES,fill=BOTH)
                                                                                                     canvas_electro_page22.create_text(700,300, text='''
Please note that charges under consideration in above figure are all negative charges. Electrostatic Forces between these 
charges are force of repulsion as like charges repel each other.
Similarly we can calculate ⃗F12, ⃗F13 , .................. ⃗F1n from Coulomb's law i. e.
⃗F12=q1q2ˆr124πε0r212
to ,⃗F1n=q1q2ˆr1n4πε0r21n

The total force F1
on the charge q1 due to all other charges is the vector sum of the forces ⃗F12 , ⃗F13 , ................................. ⃗F1n.
⃗F1=⃗F12+⃗F13+.......+⃗F1n
⃗F1=14πε0[q1q2r212^r21+q1q3r213^r31+......q1qnr21n^rn1]
or,
⃗F1=q14πε0n∑i=1qir21i^ri1
Here the vector sum done using parallelogram law of vector addition of vector. Same way force on any other charge due to 
other charges say on q2, q3 etc. can found using this method.''', font=('Times New Roman',14), fill='black')
                                                                                                     
                                                                                                     def electro_page23():
                                                                                                         phy_electro_page23=Tk()
                                                                                                         phy_electro_page23.title('Electrostatics')
                                                                                                         canvas_electro_page23=Canvas(phy_electro_page23, width=1500, height=900, bg='white')
                                                                                                         canvas_electro_page23.pack(expand=YES,fill=BOTH)
                                                                                                         canvas_electro_page23.create_text(700,100, text='What is Electrical Field?', font=('Times New Roman',18), fill='black')
                                                                                                         canvas_electro_page23.create_text(700, 150, text='''
Electrical interaction between charged particles can be reformulated using the concept of electric field. To understand the concept 
consider the mutual repulsion of two positive charged bodies A and B. Charged body A has charge q and charged body B has charge q0 
as shown in figure (a) ''', font=('Times New Roman',14), fill='black')
                                                                                                         canvas_electro_page23.create_text(700,500, text='''
Now if we remove the charged body B and label its position as point P as shown in figure (b), then charged body A is said to 
produce an electric field at that point (and at all other points in its vicinity). When a body B is placed at point P and 
experiences force F, we explain it by a point of view that force is exerted on B by the field created due to charged body A 
not by body A itself. So, we can say that body A sets up an electric field and the force on body B is exerted by the field due to A.
An electric field is said to exists at a point if a force of electric origin is exerted on a stationary charged (test charge) 
placed at that point.

    Electric field due to a charge is the space around the charge in which any other charge experiences a force of attraction or repulsion.

In figure (a) the charge +q is called the source charge because it is producing the electric field.
The charge +q0 is called the test charge. Test charge should be as small as possible so that its presence does not have any effect 
on the electric field due to source charge.  ''', font=('Times New Roman',14), fill='black')
                                                                                                         def electro_page24():
                                                                                                             phy_electro_page24=Tk()
                                                                                                             phy_electro_page24.title('Electrostatics')
                                                                                                             canvas_electro_page24=Canvas(phy_electro_page24, width=1500, height=900, bg='white')
                                                                                                             canvas_electro_page24.pack(expand=YES,fill=BOTH)
                                                                                                             canvas_electro_page24.create_text(700, 100, text='Electric Field Intensity', font=('Times New Roman',18), fill='black')
                                                                                                             canvas_electro_page24.create_text(700, 200, text='''
 We use term ‘electric field intensity’ or ‘electric field strength’ to describe the strength of electric field due to a charge.

Electric field intensity definition:  The Electric field intensity at a point is defined as the force experienced by a unit positive 
                                            charge placed at that point.

Now consider the figure given below where a charge q is located at point O in space. ''', font=('Times New Roman',14), fill='black')
                                                                                                             canvas_electro_page24.create_text(700, 500, text='''
If ⃗F is the force acting on test charge q0 placed at a point P in an electric field then electric field at that point is ⃗
E=⃗Fq0 or ⃗F=q0⃗E 
Electric field is a vector quantity and since ⃗F=q0⃗E, the direction of ⃗E is same as the direction of ⃗F. Unit of electric 
field is (N.C^−1) and the dimensions of electric field is [MLT−3A−1].
It must be noted here that test charge we are considering here should be as small as possible we can make it so small so that 
it approaches zero or become infinitesimally small. In this case we can define electric field due to such infinitesimally small 
charge as
 ⃗E=limq0→0⃗Fq0''', font=('Times New Roman',14), fill='black')
                                                                                                             canvas_electro_page24.create_oval(300, 300, 330, 330, outline='black')
                                                                                                             canvas_electro_page24.create_line(340,315,640,315, fill='black')
                                                                                                             canvas_electro_page24.create_line(680, 315, 780,315, fill='black')
                                                                                                             canvas_electro_page24.create_line(680,370,820, 370, fill='black')
                                                                                                             
                                                                                                             def electro_page25():
                                                                                                                 phy_electro_page25=Tk()
                                                                                                                 phy_electro_page25.title('Electrostatics')
                                                                                                                 canvas_electro_page25=Canvas(phy_electro_page25, width=1500, height=900, bg='white')
                                                                                                                 canvas_electro_page25.pack(expand=YES,fill=BOTH)
                                                                                                                 canvas_electro_page25.create_text(700, 100, text='Physical Significance of electric field', font=('Times New Roman',16), fill='black')
                                                                                                                 canvas_electro_page25.create_text(700,200, text='''

    It is very important concept in understanding various electrostatic phenomenon.
    The space around every electric charge or electrically charged body is filled with an electric field thereby altering the space around it. This is the reason why electrostatic force like gravitational force is an action-at-a-distance force.
    Electric field should not be thought of as a kind of matter filled in space surrounding electric charge. It is a kind of aura or the distinctive atmosphere or quality that seems to surround and be generated by an electric charge.''', font=('Times New Roman',14), fill='black')
                                                                                                                 canvas_electro_page25.create_text(700, 359, text='Calculation of Electric Field', font=('Times New Roman',18), fill='black')
                                                                                                                 canvas_electro_page25.create_text(700,500, text='''
Let us imagine a test charge q0 to be placed at P. Now we find force on charge q0 due to q through Coulomb's law. 
→F=1/4πϵ0 x q q0/r^2ˆr 
Electric field at point P is 
→E=→Fq0=1/q0(1/4πϵ0 x qq0/r^2)ˆr 
Or, →E=1/4πϵ0 x q/r^2ˆr And |→E|=1/4πϵ0 x q/r^2=9×10^9q/r^2 
Above expression gives the magnitude of electric field intensity due to charge q at any point at a distance r from it.The 
direction of the field is away from the charge q if it is positive. Electric field for either a positive or negative charge 
in terms of unit vector ˆr directed along line from charge q to point P is 
→E=1/4πϵ0 xq/r^2ˆr 
Here, r is the distance from charge q to point P. ''', font=('Times new Roman',14), fill='black')
                                                                                                                 def electro_page26():
                                                                                                                      phy_electro_page26=Tk()
                                                                                                                      phy_electro_page26.title('Electrostatics')
                                                                                                                      canvas_electro_page26=Canvas(phy_electro_page26, width=1500, height=900, bg='white')
                                                                                                                      canvas_electro_page26.pack(expand=YES,fill=BOTH)
                                                                                                                      canvas_electro_page26.create_text(700, 100, text='Electric Field in terms of position vectors',font=('Times New Roman',18), fill='black')
                                                                                                                      canvas_electro_page26.create_text(700, 500, text='''
From this figure we can see that −−→OA=⃗r1 is the position vector of our source charge kept at point A. Our problem here is 
to find the electric field intensity at P whose position vector is −−→OB=⃗r2 due to our source charge +q at point A.
Now from triangle law of vector addition −−→OA+−−→AP=−−→OP
−−→AP=⃗r12=−−→OP- →OA 
r12=⃗r2−⃗r1 
If we place a infinitesimally small test charge +q0 at point P then force ⃗F acting on this charge +q0 can be found using 
Coulomb’s Law and is given by,
 ⃗F=1/4πε0 x qq0/(r12)^2 ^r12 = 1/4πε0 x qq0/(r12)^3 r12
 F=qq0/4πε0 x (⃗r2−⃗r1)/(|⃗r2−⃗r1|)^3 
 Therefore, ⃗E=⃗Fq0=q/4πε0 x (⃗r2−⃗r1)/(|⃗r2−⃗r1|)^3 
 Electric field is directed along from A to P and its magnitude is
∣⃗E∣ =1/4πε0 x q/(r12)^2 = 9×10^9 x q/(r12)^2 ''', font=('Times New Roman',14), fill='black')
                                                                                                                      def electro_page27():
                                                                                                                          phy_electro_page27=Tk()
                                                                                                                          phy_electro_page27.title('Electrostatics')
                                                                                                                          canvas_electro_page27=Canvas(phy_electro_page27, width=1500, height=900, bg='white')
                                                                                                                          canvas_electro_page27.pack(expand=YES,fill=BOTH)
                                                                                                                          canvas_electro_page27.create_text(700, 100, text='E due to a group of point charges', font=('Times New Roman',18), fill='black')
                                                                                                                          canvas_electro_page27.create_text(700, 300, text='''
The resultant or net electric field intensity at a point due to a group of point charges can be calculated by applying the 
principle of superposition. To calculate ⃗E due to a group of point charges consider the number of point charges which are at 
positions ⃗r1,⃗r2,⃗r3,..........,⃗rn from point P. Our problem is to find electric field intensity at point P whose position vector 
is ⃗r. Now, from principle of superposition we have. ⃗E=⃗E1+⃗E2+⃗E3+.........+⃗En where
E=resultant electric field at point P
E1=Electric field intensity at P due to q1
E2=Electric field intensity at P due to q2 and soon. 
Again let us now imagine that a very small positive test charge +q0 is placed at point P then force on this test charge +q0 is 
equal to vector sum of forces due to charges q1,q2,q3,..........qn on +q0. Therefore,
 ⃗F=q0/4πε0 ∑qi(⃗r−⃗ri)/(|⃗r−⃗ri|)^3
 Therefore,⃗E=⃗F/q0=1/4πε0 ∑qi(⃗r−⃗ri)/(|⃗r−⃗ri|)^3''', font=('Times New Roman',14), fill='black')
 
                                                                                                                          def electro_page28():
                                                                                                                              global phy_electro_page28
                                                                                                                              phy_electro_page28=Toplevel()
                                                                                                                              phy_electro_page28.title('Electrostatics')
                                                                                                                              canvas_electro_page28=Canvas(phy_electro_page28, width=1500, height=900, bg='white')
                                                                                                                              canvas_electro_page28.pack(expand=YES,fill=BOTH)
                                                                                                                              canvas_electro_page28.create_text(700, 100, text='Electric Field Lines', font=('Times New Roman',18), fill='black')
                                                                                                                              canvas_electro_page28.create_text(700, 150, text='''
For a single positive point charge q, electric field is
F=kqq′ˆr4πϵ0r2
now to get feel of this field one can sketch a few representative vectors as shown in fig below''', font=('Times New Roman',14), fill='black')
                                                                                                                              canvas_electro_page28.create_text(700, 500, text='''
1)  Since electric field varies as inverse of square of the distance that points from the charge the vector gets shorter as you 
     go away from the origin and they always points radially outwards.
2)  Connecting up these vectors to form a line is a nice way to represent this field .
3)  The magnitude of the field is indicated by the density of the field lines.
4)  Magnitude is strong near the center where the field lines are close togather, and weak farther out, where they are relatively apart.
5)  So, electric field line is an imaginary line drawn in such a way that it's direction at any point is same as the direction of field
     at that point.
6)  An electric field line is, in general a curve drawn in such a way that the tangent to it ateach point is the direction of net field 
    at that point.''', font=('Times New Roman',14), fill='black')
                                                                                                                              global vecimg
                                                                                                                              vecimg = tkinter.PhotoImage(file="elecline.gif")
                                                                                                                              button = Button(phy_electro_page28,image = vecimg,width=167,height=170,font=("Courier",20,"bold"),bg='grey')#,command=lambda:back(canvas2) 
                                                                                                                              button.configure(image = vecimg)
                                                                                                                              button.place(relx=0.50,rely=0.43,anchor = CENTER)
                                                                                                                              
                                                                                                                              def electro_page29():
                                                                                                                                  phy_electro_page29=Tk()
                                                                                                                                  phy_electro_page29.title('Electrostatics')
                                                                                                                                  canvas_electro_page29=Canvas(phy_electro_page29, width=1500, height=900, bg='white')
                                                                                                                                  canvas_electro_page29.pack(expand=YES,fill=BOTH)
                                                                                                                                  canvas_electro_page29.create_text(700, 100, text='''
Field lines of a single position charge points radially outwards while that of a negative charge are radially inwards as shown below 
in the figure.''', font=('Times New Roman',14), fill='black')
                                                                                                                                  canvas_electro_page29.create_text(700,300, text='''
Field lines around the system of two positive charges gives a different picture and describe the mutual repulsion between them.''', font=('Times new Roman',14), fill='black')
                                                                                                                                  canvas_electro_page29.create_text(700, 500, text='''
Field lines around a system of a positive and negative charge clearly shows the mutual attraction between them as shown below in the figure. ''', font=('Times New Roman',14), fill='black')
                                                                                                                                  
                                                                                                                                  def electro_page30():
                                                                                                                                      phy_electro_page30=Tk()
                                                                                                                                      phy_electro_page30.title('Electrostatics')
                                                                                                                                      canvas_electro_page30=Canvas(phy_electro_page30, width=1500, height=900, bg='white')
                                                                                                                                      canvas_electro_page30.pack(expand=YES,fill=BOTH)
                                                                                                                                      canvas_electro_page30.create_text(700, 100, text='''
Some important general properties of field lines are
1.Field lines start from positive charge and end on a negative charge.
2.Field lines never cross each other if they do so then at the point of intersection there will be two direction of electric field.
3.Electric field lines do not pass through a conductor , this shows that electric field inside a conductor is always zero.
4.Electric field lines are continuous curves in a charge free region.''', font=('Times New Roman',14), fill='black')
                                                                                                                                      canvas_electro_page30.create_text(700, 200, text='Electric flux', font=('Times New Roman',18), fill='black')
                                                                                                                                      canvas_electro_page30.create_text(700, 250, text='''

  ->  Consider a plane surface of area ΔS in a uniform electric field E in the space.
  ->  Draw a positive normal to the surface and θ be the angle between electric field E and the normal to the plane.''', font=('Times New Roman',14), fill='black')
                                                                                                                                      canvas_electro_page30.create_text(700,500, text='''
  -> Electric flux of the electric field through the choosen surface is then
      Δφ = E ΔS cosθ
  -> Corresponding to area ΔS we can define an area vector ΔS of magnitude ΔS along the positive normal. With this definition one 
     can write electric flux as
      Δφ = E . ΔS
  -> direction of area vector is always along normal to the surface being choosen.
  -> Thus electric flux is a measure of lines of forces passing through the surface held in the electric field.''', font=('Times New Roman',14), fill='black')
                                                                                                                                      
                                                                                                                                      def electro_page31():
                                                                                                                                          phy_electro_page31=Tk()
                                                                                                                                          phy_electro_page31.title('Electrostatics')
                                                                                                                                          canvas_electro_page31=Canvas(phy_electro_page31, width=1500, height=900, bg='white')
                                                                                                                                          canvas_electro_page31.pack(expand=YES,fill=BOTH)
                                                                                                                                          canvas_electro_page31.create_text(700, 300, text='''
Special Cases
If E is perpendicular to the surface i. e., parallel to the area vector then θ = 0 and
Δφ = E ΔS cos0

If θ = π i. e., electric field vector is in the direction opposite to area vector then
Δφ = - E ΔS

If electric field and area vector are perpendicular to each other then θ = π/2 and Δφ = 0

Flux is an scaler quantity and it can be added using rules of scaler addition.

For calculating total flux through any given surface , divide the surface into small area elements. Calculate the flux at each area element and add them up.

Thus total flux φ through a surface S is
φ ≅ ΣE.ΔS

This quantity is mathematically exact only when you take the limit ΔS→0 and the sum in equation 3 is written as integral









φ = ∫ΣE.dS''', font=('Times New Roman',14), fill='black')
                                                                                                                                          
                                                                                                                                          def electro_page32():
                                                                                                                                              phy_electro_page32=Tk()
                                                                                                                                              phy_electro_page32.title('Electrostatics')
                                                                                                                                              canvas_electro_page32=Canvas(phy_electro_page32, width=1500, height=900, bg='white')
                                                                                                                                              canvas_electro_page32.pack(expand=YES,fill=BOTH)
                                                                                                                                              canvas_electro_page32.create_text(700, 100, text='Electric Dipole and Dipole Moment', font=('Times New Roman',18), fill='black')
                                                                                                                                              canvas_electro_page32.create_text(700, 150, text='What is an Electric Dipole', font=('Times New Roman',18), fill='black')
                                                                                                                                              canvas_electro_page32.create_text(700, 250, text='''
Electric dipole is a pair of equal and opposite charges, +q and −q, separated by a very small distance. Total charge of the 
dipole is zero but electric field of the dipole is not zero as charges q and -q are separated by some distance and electric 
field due to them when added is not zero.
Examples of electric dipole:- Dipoles are common in nature. Molecules like H2O,HCl,CH3COOH are electric dipoles and have 
permanent dipole moments. They have permanent dipole moments because the center of their positive charges does not fall 
exactly over the center of their negative charges.Figure given below shows molecule of water. ''', font=('Times New Roman',14), fill='black')
                                                                                                                                              canvas_electro_page32.create_text(700, 350, text='Physical significance of Electric Dipole and dipole moment', font=('Times New Roman',18), fill='black')
                                                                                                                                              canvas_electro_page32.create_text(700, 550, text='''

  ->  Atoms as a whole are electrically neutral in their ground state. We know that atoms have equal amount of positive and 
         negative charge. Similar to atoms molecules are also neutral but they also have equal amount of positive and negative charges.
  ->  Now when in a system, algebraic sum of all the charges is zero it does not necessarily mean that electric field produced by the 
        system is zero everywhere. This makes study of electric dipoles important for electrical phenomenon in matter.
  ->  Matter which is made up of atoms and molecules is electrically neutral. If the center of mass of positive charges coincides with 
        that of negative charges then molecule behaves as non-polar molecule. On the other hand, if center of mass of positive charges 
        does not coincides with that of negative charges then molecule behaves as polar molecule. These polar molecules have permanent 
        dipole moments. These dipole moments are randomly oriented in the absence of external electric field. If we place a material 
        with polar molecules in external electric field then these molecules align themselves in the direction of the field. This results 
        in the development of a net dipole moment. This particular piece of material is said to be polarized.
  ->  So study of dipole and dipole moments gives a measure of the polarization of a net neutral system. The study of dipole moments 
        measures the tendency of a dipole to align with an external electric field.''', font=('Times New Roman',14), fill='black')
                                                                                                                                              def electro_page33():
                                                                                                                                                   phy_electro_page33=Tk()
                                                                                                                                                   phy_electro_page33.title('Electrostatics')
                                                                                                                                                   canvas_electro_page33=Canvas(phy_electro_page33, width=1500, height=900, bg='white')
                                                                                                                                                   canvas_electro_page33.pack(expand=YES,fill=BOTH)
                                                                                                                                                   canvas_electro_page33.create_text(700, 200, text='''

Electric dipole moment occurs when there is a separation of charge. It can occur in electrically neutral molecules with ionic bonds 
or molecules with covalent bonds. Dipole moments measures the electric polarity of system of charges.

   Electric dipole moment measures the strength of an electric dipole. It is a vector quantity.

Electric dipole moment definition :- The dipole moment of an electric field is a vector whose magnitude is charge times the 
                                        separation between two opposite charges.

  ->  Direction of dipole moment is along the dipole axis from negative charge to positive charge.
  ->  Consider the figure given below which shows an electric dipole consisting of charges (±q) separated by a small distance 2a. ''', font=('Times New Roman',14), fill='black')
                                                                                                                                                   canvas_electro_page33.create_text(700, 550, text='''
Mathematically, 
Dipole Moment=either one of charges × separation vector from +ive to -ive
 ⃗p=q(2⃗a)C.m
Above equation gives Electric dipole moment formula
* Magnitude of dipole moment is
* |⃗p|=q×2a
* The Electric dipole moment direction is from negative charge to positive charge.
* The SI unit of dipole moment is Coulomb-meter(C−m)''', font=('Times New Roman',14), fill='black')
                                                                                                                                                   
                                                                                                                                                   def electro_page34():
                                                                                                                                                       phy_electro_page34=Tk()
                                                                                                                                                       phy_electro_page34.title('Electrostatics')
                                                                                                                                                       canvas_electro_page34=Canvas(phy_electro_page34, width=1500, height=900, bg='white')
                                                                                                                                                       canvas_electro_page34.pack(expand=YES,fill=BOTH)
                                                                                                                                                       canvas_electro_page34.create_text(700, 100, text='What is an ideal electric dipole?', font=('Times New Roman',16), fill='black')
                                                                                                                                                       canvas_electro_page34.create_text(700, 150, text='''
Answer: If charge q gets larger and the distance 2a gets smaller and smaller such that the dipole moment, p=2×2a has finite value then 
        such a dipole of negligibly small size is called an ideal or point dipole''', font=('Times New Roman',14), fill='black')
                                                                                                                                                       canvas_electro_page34.create_text(700,250, text='Electric Dipole', font=('Times New Roman',18),fill='black')
                                                                                                                                                       canvas_electro_page34.create_text(700, 300, text='''

* Electric dipole is a pair of equal and opposite charges, +q and -q, separated by some distance 2a.
* Total charge of the dipole is zero but electric field of the dipole is not zero as charges q and -q are separated by some 
    distance and electric field due to them when added is not zero.
''', font=('Times New Roman',14), fill='black')
                                                                                                                                                       canvas_electro_page34.create_text(700, 450, text='''
(A)Field of an electric dipole at points in equatorial plane

-> We now find the magnitude and direction of electric field due to dipole.
''', font=('Times New Roman',14), fill='black')
                                                                                                                                                       def electro_page35():
                                                                                                                                                           phy_electro_page35=Tk()
                                                                                                                                                           phy_electro_page35.title('Electrostatics')
                                                                                                                                                           canvas_electro_page35=Canvas(phy_electro_page35, width=1500, height=900, bg='white')
                                                                                                                                                           canvas_electro_page35.pack(expand=YES,fill=BOTH)
                                                                                                                                                           canvas_electro_page35.create_text(700,400, text='''
P point in the equitorial plane of the dipole at a distance r from the centre of the dipole. Then electric field due to +q and -q are 
E−q=−qˆP4πϵ0(r2+a2)                           (1a) 
E+q=qˆP4πϵ0(r2+a2)                            (1b)
and they are equal
Pˆ = unit vector along the dipole axis (from -q to +q)
From fig we can see the direction of E+q and E-q. Their components normal to dipole cancel away and components along the dipole add up.
Dipole moment vector points from negative charge to positive charge so in vector form.
E = -(E+q + E-q) cos θ

E = q/4πϵ0(r^2 +a^2)^(3/2) x 2a
  = p/4πϵ0(r^2 +a^2)^(3/2)

When r>>a
E= p/4πϵ0r^3

->E= - ->p/4πϵ0r^3''', font=('Times New Roman',14), fill='black' )

                                                                                                                                                           def Back_to_class12_electro():
                                                                                                                                                               phy_Electrostatics.destroy()
                                                                                                                                                               phy_electro_page1.destroy()
                                                                                                                                                               phy_electro_page2.destroy()
                                                                                                                                                               phy_electro_page3.destroy()
                                                                                                                                                               phy_electro_page4.destroy()
                                                                                                                                                               phy_electro_page5.destroy()
                                                                                                                                                               phy_electro_page6.destroy()
                                                                                                                                                               phy_electro_page7.destroy()
                                                                                                                                                               phy_electro_page8.destroy()
                                                                                                                                                               phy_electro_page9.destroy()
                                                                                                                                                               phy_electro_page10.destroy()
                                                                                                                                                               phy_electro_page11.destroy()
                                                                                                                                                               phy_electro_page12.destroy()
                                                                                                                                                               phy_electro_page13.destroy()
                                                                                                                                                               phy_electro_page14.destroy()
                                                                                                                                                               phy_electro_page15.destroy()
                                                                                                                                                               phy_electro_page16.destroy()
                                                                                                                                                               phy_electro_page17.destroy()
                                                                                                                                                               phy_electro_page18.destroy()
                                                                                                                                                               phy_electro_page19.destroy()
                                                                                                                                                               phy_electro_page20.destroy()
                                                                                                                                                               phy_electro_page21.destroy()
                                                                                                                                                               phy_electro_page22.destroy()
                                                                                                                                                               phy_electro_page23.destroy()
                                                                                                                                                               phy_electro_page24.destroy()
                                                                                                                                                               phy_electro_page25.destroy()
                                                                                                                                                               phy_electro_page26.destroy()
                                                                                                                                                               phy_electro_page27.destroy()
                                                                                                                                                               phy_electro_page28.destroy()
                                                                                                                                                               phy_electro_page29.destroy()
                                                                                                                                                               phy_electro_page30.destroy()
                                                                                                                                                               phy_electro_page31.destroy()
                                                                                                                                                               phy_electro_page32.destroy()
                                                                                                                                                               phy_electro_page33.destroy()
                                                                                                                                                               phy_electro_page34.destroy()
                                                                                                                                                               phy_electro_page35.destroy()
                                                                                                                                                               
                                                                                                                                                           Back_to_class12_electro=Button(phy_electro_page35,bg='coral2', text='Class 12',font=('Castellar',18), command=Back_to_class12_electro)
                                                                                                                                                           Back_to_class12_electro.pack()
                                                                                                                                                           Back_to_class12_electro.place(relx=.87,rely=.85)
                                                                                                                                                           
                                                                                                                                                       Electro_page35=Button(phy_electro_page34, bg='coral2', text='-->', command=electro_page35)
                                                                                                                                                       Electro_page35.pack()
                                                                                                                                                       Electro_page35.place(relx=.98,rely=.0)     
                                                                                                                                                           
                                                                                                                                                   Electro_page34=Button(phy_electro_page33, bg='coral2', text='-->', command=electro_page34)
                                                                                                                                                   Electro_page34.pack()
                                                                                                                                                   Electro_page34.place(relx=.98,rely=.0)  
                                                                                                                                                   
                                                                                                                                              Electro_page33=Button(phy_electro_page32, bg='coral2', text='-->', command=electro_page33)
                                                                                                                                              Electro_page33.pack()
                                                                                                                                              Electro_page33.place(relx=.98,rely=.0)  
                                                                                                                                              
                                                                                                                                          Electro_page32=Button(phy_electro_page31, bg='coral2', text='-->', command=electro_page32)
                                                                                                                                          Electro_page32.pack()
                                                                                                                                          Electro_page32.place(relx=.98,rely=.0)  
                                                                                                                                          
                                                                                                                                      Electro_page31=Button(phy_electro_page30, bg='coral2', text='-->', command=electro_page31)
                                                                                                                                      Electro_page31.pack()
                                                                                                                                      Electro_page31.place(relx=.98,rely=.0)  
                                                                                                                                      
                                                                                                                                  Electro_page30=Button(phy_electro_page29, bg='coral2', text='-->', command=electro_page30)
                                                                                                                                  Electro_page30.pack()
                                                                                                                                  Electro_page30.place(relx=.98,rely=.0)  
                                                                                                                                      
                                                                                                                              Electro_page29=Button(phy_electro_page28, bg='coral2', text='-->', command=electro_page29)
                                                                                                                              Electro_page29.pack()
                                                                                                                              Electro_page29.place(relx=.98,rely=.0)  
                                                                                                                              
                                                                                                                          Electro_page28=Button(phy_electro_page27, bg='coral2', text='-->', command=electro_page28)
                                                                                                                          Electro_page28.pack()
                                                                                                                          Electro_page28.place(relx=.98,rely=.0)
                                                                                                                          
                                                                                                                      Electro_page27=Button(phy_electro_page26, bg='coral2', text='-->', command=electro_page27)
                                                                                                                      Electro_page27.pack()
                                                                                                                      Electro_page27.place(relx=.98,rely=.0)
                                                                                                                      
                                                                                                                 Electro_page26=Button(phy_electro_page25, bg='coral2', text='-->', command=electro_page26)
                                                                                                                 Electro_page26.pack()
                                                                                                                 Electro_page26.place(relx=.98,rely=.0)
                                                                                                                     
                                                                                                             Electro_page25=Button(phy_electro_page24, bg='coral2', text='-->', command=electro_page25)
                                                                                                             Electro_page25.pack()
                                                                                                             Electro_page25.place(relx=.98,rely=.0)
                                                                                                             
                                                                                                         Electro_page24=Button(phy_electro_page23, bg='coral2', text='-->', command=electro_page24)
                                                                                                         Electro_page24.pack()
                                                                                                         Electro_page24.place(relx=.98,rely=.0)
                                                                                                         
                                                                                                     Electro_page23=Button(phy_electro_page22, bg='coral2', text='-->', command=electro_page23)
                                                                                                     Electro_page23.pack()
                                                                                                     Electro_page23.place(relx=.98,rely=.0)
                                                                                                     
                                                                                                 Electro_page22=Button(phy_electro_page21, bg='coral2', text='-->', command=electro_page22)
                                                                                                 Electro_page22.pack()
                                                                                                 Electro_page22.place(relx=.98,rely=.0)
                                                                                                 
                                                                                             Electro_page21=Button(phy_electro_page20, bg='coral2', text='-->', command=electro_page21)
                                                                                             Electro_page21.pack()
                                                                                             Electro_page21.place(relx=.98,rely=.0)
                                                                                             
                                                                                         Electro_page20=Button(phy_electro_page19, bg='coral2', text='-->', command=electro_page20)
                                                                                         Electro_page20.pack()
                                                                                         Electro_page20.place(relx=.98,rely=.0)
                                                                                         
                                                                                     Electro_page19=Button(phy_electro_page18, bg='coral2', text='-->', command=electro_page19)
                                                                                     Electro_page19.pack()
                                                                                     Electro_page19.place(relx=.98,rely=.0)
                                                                                         
                                                                                 Electro_page18=Button(phy_electro_page17, bg='coral2', text='-->', command=electro_page18)
                                                                                 Electro_page18.pack()
                                                                                 Electro_page18.place(relx=.98,rely=.0)
                                                                                 
                                                                             Electro_page17=Button(phy_electro_page16, bg='coral2', text='-->', command=electro_page17)
                                                                             Electro_page17.pack()
                                                                             Electro_page17.place(relx=.98,rely=.0)
                                                                             
                                                                         Electro_page16=Button(phy_electro_page15, bg='coral2', text='-->', command=electro_page16)
                                                                         Electro_page16.pack()
                                                                         Electro_page16.place(relx=.98,rely=.0)
                                                                         
                                                                     Electro_page15=Button(phy_electro_page14, bg='coral2', text='-->', command=electro_page15)
                                                                     Electro_page15.pack()
                                                                     Electro_page15.place(relx=.98,rely=.0)
                                                                     
                                                                 Electro_page14=Button(phy_electro_page13, bg='coral2', text='-->', command=electro_page14)
                                                                 Electro_page14.pack()
                                                                 Electro_page14.place(relx=.98,rely=.0)
                                                                 
                                                            Electro_page13=Button(phy_electro_page12, bg='coral2', text='-->', command=electro_page13)
                                                            Electro_page13.pack()
                                                            Electro_page13.place(relx=.98,rely=.0)
                                                            
                                                        Electro_page12=Button(phy_electro_page11, bg='coral2', text='-->', command=electro_page12)
                                                        Electro_page12.pack()
                                                        Electro_page12.place(relx=.98,rely=.0)
                                                            
                                                    Electro_page11=Button(phy_electro_page10, bg='coral2', text='-->', command=electro_page11)
                                                    Electro_page11.pack()
                                                    Electro_page11.place(relx=.98,rely=.0)
                                                    
                                                Electro_page10=Button(phy_electro_page9, bg='coral2', text='-->', command=electro_page10)
                                                Electro_page10.pack()
                                                Electro_page10.place(relx=.98,rely=.0)
                                                    
                                            Electro_page9=Button(phy_electro_page8, bg='coral2', text='-->', command=electro_page9)
                                            Electro_page9.pack()
                                            Electro_page9.place(relx=.98,rely=.0)
                                                
                                        Electro_page8=Button(phy_electro_page7, bg='coral2', text='-->', command=electro_page8)
                                        Electro_page8.pack()
                                        Electro_page8.place(relx=.98,rely=.0)
                                            
                                    Electro_page7=Button(phy_electro_page6, bg='coral2', text='-->', command=electro_page7)
                                    Electro_page7.pack()
                                    Electro_page7.place(relx=.98,rely=.0)
                                    
                                Electro_page6=Button(phy_electro_page5, bg='coral2', text='-->', command=electro_page6)
                                Electro_page6.pack()
                                Electro_page6.place(relx=.98,rely=.0)
                            
                            Electro_page5=Button(phy_electro_page4, bg='coral2', text='-->', command=electro_page5)
                            Electro_page5.pack()
                            Electro_page5.place(relx=.98,rely=.0)
                    
                        Electro_page4=Button(phy_electro_page3, bg='coral2', text='-->', command=electro_page4)
                        Electro_page4.pack()
                        Electro_page4.place(relx=.98,rely=.0)      
                        
                    Electro_page3=Button(phy_electro_page2, bg='coral2', text='-->', command=electro_page3)
                    Electro_page3.pack()
                    Electro_page3.place(relx=.98,rely=.0)
                
                Electro_page2=Button(phy_electro_page1, bg='coral2', text='-->', command=electro_page2)
                Electro_page2.pack()
                Electro_page2.place(relx=.98,rely=.0)
                
            def Back_Electrostatics():
                phy_Electrostatics.destroy()
            
            Electro_page1=Button(phy_Electrostatics, bg='coral2', text='-->', command=electro_page1)
            Electro_page1.pack()
            Electro_page1.place(relx=.98,rely=.0)
            
            Back_Electrostatics=Button(phy_Electrostatics, bg='coral2', text='<--', command=Back_Electrostatics)
            Back_Electrostatics.pack()
            Back_Electrostatics.place(relx=.0,rely=.0)
                        
        def Communication_system():
            phy_Communication_system=Tk()
            phy_Communication_system.title('Communication system')
            canvas_Communication_system=Canvas(phy_Communication_system, width=1500, height=900, bg='white')
            canvas_Communication_system.pack(expand=YES,fill=BOTH)
            
            canvas_Communication_system.create_text(700,300, text='''
    Transmitter :
(a) It process and encode the information and make it suitable for transmission.
(b) The message signal for communication can be analog signals or digital signals.
(c) An analog signal can be converted suitably into a digital signal and vice-versa.
(d) An analog signal is that in which current or voltage value varies continuously with time.

    Communication channel:
The medium through which information propagate from transmitter to receiver is called communication channel.

    Receiver:
It receives and decode the signal.

    Analog signal:
A signal in which current or voltage changes its magnitude continuously with time, is called an analog signal.

    Digital signal:
A signal in which current or voltage have only two values, is called a digital signal. An analog signal can be converted suitable into a digital signal and vice-versa.

    Modulation:
The process of superimposing the audio signal over a high frequency carrier wave is called modulation.''', font=('Times New Roman',14), fill='black')
                
            def com_page1():
                phy_com_page1=Tk()
                phy_com_page1.title('Communication system')
                canvas_com_page1=Canvas(phy_com_page1, width=1500, height=900, bg='white')
                canvas_com_page1.pack(expand=YES,fill=BOTH)
                canvas_com_page1.create_text(700,300, text='''
    Need of modulation:
(a) Energy carried by low frequency audio waves (20 Hz to 20000 Hz) is very small.
(b) For efficient radiation and reception of signal, the transmitting and receiving antennas should be very high approximately 5000 m.
(c) The frequency range of audio signal is so small that overlapping of signals create a confusion.

    Amplitude Modulation:
In this type of modulation in which the amplitude of a high frequency carrier wave is varied in accordance with some 
characteristic of the modulating signal.
Band width required for amplitude modulation = twice the frequency of the modulating signal.

    Frequency modulation:
In this type of modulation, the frequency of high frequency carrier wave is varied in accordance to instantaneous frequency of modulating signal.

    Pulse modulation:
In this type of modulation, the continuous waveforms are sampled at regular intervals. Information is transmitted only at the sampling times.

    Demodulation:
The process of separating of audio signal from modulated signal is called demodulation.''', font=('Times New Roman',14), fill='black')
                
                def com_page2():
                    phy_com_page2=Tk()
                    phy_com_page2.title('Communication system')
                    canvas_com_page2=Canvas(phy_com_page2, width=1500, height=900, bg='white')
                    canvas_com_page2.pack(expand=YES,fill=BOTH)
                    canvas_com_page2.create_text(700, 300, text='''

    Antenna:
An antenna converts electrical energy into electromagnetic waves at transmitting end and pick up transmitted signal 
at receiving end and converts electromagnetic waves into electrical signal.

    Modem:
The term modem is contraction of the term modulator and demodulator. Modem is a device which can modulate as well as 
demodulate the signal. It connect one computer to another through ordinary telephone lines.

    Fax (Facsimile telegraph):
The electronic reproduction of a document at a distant place is called FAX.

    Radio waves:
Radio WaveThe radio waves are the electromagnetic waves of frequency ranging from 500 kHz to about 1000 MHz. 
These waves are used in the field of radio communication.

    Ground wave or surface wave propagation:
It is suitable for low and medium frequency upto 2 MHz. It is used for local broad casting. ''', font=('Times New Roman',14), fill='black')
                        
                    def com_page3():
                        phy_com_page3=Tk()
                        phy_com_page3.title('Communication system')
                        canvas_com_page3=Canvas(phy_com_page3, width=1500, height=900, bg='white')
                        canvas_com_page3.pack(expand=YES,fill=BOTH)
                        canvas_com_page3.create_text(700,300, text='''

    Sky wave propagation:
It is suitable for radiowaves of frequency between 2 MHz to 30 MHz. It is used for long distance radio communication.

(a) Critical frequency:
The highest frequency of radio wave that can be reflected back by the ionosphere is called critical frequency.
Critical frequency, fc = 9 (Nmax)1/2
Here, Nmax = number density of electrons/meter3

(b) Skip distance
The minimum distance from the transmitter at which a sky wave of a frequency but not more than critical frequency, is sent back to the earth.
Skip distance (Dskip) = 2h (fmax/fc)2 – 1
Here h is height of reflecting layer of atmosphere.
fmax is maximum frequency of electromagnetic waves and fc is critical frequency.

(d) Fading
The variation in the strength of a signal at receiver due to interference of waves, is called fading.''', font=('Times New Roman',14), fill='black')
                            
                        def com_page4():
                            phy_com_page4=Tk()
                            phy_com_page4.title('Communication system')
                            canvas_com_page4=Canvas(phy_com_page4, width=1500, height=900, bg='white')
                            canvas_com_page4.pack(expand=YES,fill=BOTH)
                            canvas_com_page4.create_text(700,300, text='''
    Space wave propagation:
        
It is suitable for 30 MHz to 300 Mhz. It is used in television communication and radar communication. It is also called 
line of sight communication. Range is limited due to curvature of earth. If h be the height of the transmitting antenna, 
then signal can be received up to a maximum distance.
d = √2Rh
If the height of transmitting and receiving antennas be hT and hR respectively. The effective range will be
d = √2RhT + √2RhR

Microwaves are electromagnetic wave of frequency 1 to 300 GHz, greater than those of TV signals. The wavelength of 
microwaves is of the order of a few mm. Microwave communication is used in radar to locate the flying objects in space.
These waves can be transmitted as beam signals in a particular direction, much better than radio wave.
There is no diffraction of microwave around corners of an obstacle which happens to lie along its passage.

    Satellite communication:
It is carried out between a transmitter and a receiver through a satellite. A geostationary satellite is utilized 
for this purpose, whose time period is 24 hours.

    Geo-synchronous orbit:
The orbit in which the geo-satellite above revolves around the earth is known as geo-synchronous orbit.''', font=('Times new Roman',14), fill='black')
                                
                            def com_page5():
                                phy_com_page5=Tk()
                                phy_com_page5.title('Communication system')
                                canvas_com_page5=Canvas(phy_com_page5, width=1500, height=900, bg='white')
                                canvas_com_page5.pack(expand=YES,fill=BOTH)
                                canvas_com_page5.create_text(700, 300, text='''

    Remote sensing:
It is a technique of observing or measuring the characteristics of the object at a distance. A polar satellite is 
utilized for this purpose.
Distance upto which a signal can be obtained from an antenna is given by
d = √2hR
Here, h is height of antenna and R is radius of earth.

    LED and Diode laser:
(a) Light emitting diode (LED) and diode laser are preferred sources for optical communication.
(b) Each produces light of suitable power required in optical communication. Diode laser provides light which is 
    monochromatic and coherent.
(c) LED provides almost monochromatic light. This suitable for small distance transmission.

    Line communication:
Transmission lines are used to interconnect points separated from each other. Line communication may be in the form 
of electrical signal or optical signal.

    Optical fibers:
An optical fiber is a long thread consisting of a central core of glass or plastic of uniform refractive index.
''', font=('Times New Roman',14), fill='black')
                                    
                                def com_page6():
                                    phy_com_page6=Tk()
                                    phy_com_page6.title('Communication system')
                                    canvas_com_page6=Canvas(phy_com_page6, width=1500, height=900, bg='white')
                                    canvas_com_page6.pack(expand=YES,fill=BOTH)
                                    canvas_com_page6.create_text(700,100, text='Types of Optical Fibres', font=('Times New Roman',16), fill='black')
                                    canvas_com_page6.create_text(700,150, text='''
1) Single mode step index fiber
2) Multi mode step index fiber
3) Multi mode graded index fiber''', font=('Times New Roman',14), fill='black')
                                
                                    def Back_to_class12_com():
                                        phy_Communication_system.destroy()
                                        phy_com_page1.destroy()
                                        phy_com_page2.destroy()
                                        phy_com_page3.destroy()
                                        phy_com_page4.destroy()
                                        phy_com_page5.destroy()
                                        phy_com_page6.destroy()
                                                                                                                                                               
                                    Back_to_class12_com=Button(phy_com_page6,bg='coral2', text='Class 12',font=('Castellar',18), command=Back_to_class12_com)
                                    Back_to_class12_com.pack()
                                    Back_to_class12_com.place(relx=.87,rely=.85)
                                    
                                Com_page6=Button(phy_com_page5, bg='coral2', text='-->', command=com_page6)
                                Com_page6.pack()
                                Com_page6.place(relx=.98,rely=.0)    
                                    
                            Com_page5=Button(phy_com_page4, bg='coral2', text='-->', command=com_page5)
                            Com_page5.pack()
                            Com_page5.place(relx=.98,rely=.0)
                        
                        Com_page4=Button(phy_com_page3, bg='coral2', text='-->', command=com_page4)
                        Com_page4.pack()
                        Com_page4.place(relx=.98,rely=.0)
                    
                    def Back_com_page2():
                        phy_com_page2.destroy()
                
                    Com_page3=Button(phy_com_page2, bg='coral2', text='-->', command=com_page3)
                    Com_page3.pack()
                    Com_page3.place(relx=.98,rely=.0)
                    
                    Back_Com_page3=Button(phy_com_page1, bg='coral2', text='<--', command=Back_com_page2)
                    Back_Com_page3.pack()
                    Back_Com_page3.place(relx=.0,rely=.0)      
                         
                def Back_com():
                    phy_com_page1.destroy()
                
                Com_page2=Button(phy_com_page1, bg='coral2', text='-->', command=com_page2)
                Com_page2.pack()
                Com_page2.place(relx=.98,rely=.0)
                
                Back_Com=Button(phy_com_page1, bg='coral2', text='<--', command=Back_com)
                Back_Com.pack()
                Back_Com.place(relx=.0,rely=.0)
                    
            def Back_Communication_system():
                phy_Communication_system.destroy()
                
            Com_page1=Button(phy_Communication_system, bg='coral2', text='-->', command=com_page1)
            Com_page1.pack()
            Com_page1.place(relx=.98,rely=.0)
            
            Back_Communication_system=Button(phy_Communication_system, bg='coral2', text='<--', command=Back_Communication_system)
            Back_Communication_system.pack()
            Back_Communication_system.place(relx=.0,rely=.0)
                        
        Electrostatics=Button(phy_class12, height=1, width=14, bg='coral2', text='Electrostatics', font=('Castellar',27), command=Electrostatics)
        Communication=Button(phy_class12, height=1, width=21, bg='coral2', text='Communication System', font=('Castellar',27), command=Communication_system)
        Quiz12=Button(phy_class12, height=1, width=8, bg='coral2', text='Quiz', font=('Castellar',27), command=Quiz12)
        Electrostatics.pack()
        Electrostatics.place(relx=.35,rely=.33)
        Communication.pack()
        Communication.place(relx=.30,rely=.50)
        Quiz12.pack()
        Quiz12.place(relx=.41,rely=.67)
        
        Back_class12=Button(phy_class12, bg='coral2', text='<--', command=Back12 )
        Back_class12.pack()
        Back_class12.place(relx=.0,rely=.0)
        
    Class7=Button(phy_start, height=1, width=9, bg='coral2', text='Class 7', font=('Castellar',27), command=Class7)
    Class8=Button(phy_start, height=1, width=9, bg='coral2', text='Class 8', font=('Castellar',27), command=Class8)
    Class9=Button(phy_start, height=1, width=9, bg='coral2', text='Class 9', font=('Castellar',27), command=Class9)
    Class10=Button(phy_start, height=1, width=9, bg='coral2', text='Class 10', font=('Castellar',27), command=Class10)
    Class11=Button(phy_start, height=1, width=9, bg='coral2', text='Class 11', font=('Castellar',27), command=Class11)
    Class12=Button(phy_start, height=1, width=9, bg='coral2', text='Class 12', font=('Castellar',27), command=Class12)
    Class7.pack()
    Class7.place(relx=.41,rely=.05)
    Class8.pack()
    Class8.place(relx=.41,rely=.20)
    Class9.pack()
    Class9.place(relx=.41,rely=.35)
    Class10.pack()
    Class10.place(relx=.41,rely=.50)
    Class11.pack()
    Class11.place(relx=.41,rely=.65)
    Class12.pack()
    Class12.place(relx=.41,rely=.80)
    
    Back_Start=Button(phy_start, bg='coral2', text='<--', command=Back_Start)
    Back_Start.pack()
    Back_Start.place(relx=.0,rely=.0)    
    
def About():
    phy_about=Tk()
    canvas_about=Canvas(phy_about, width=1500, height=900, bg='grey12', scrollregion=(0,0,1278,2500))
    canvas_about.pack(expand=YES,fill=BOTH,)
    
    def Back_About():
        phy_about.destroy()
    
    canvas_about.create_text(625,1225, text = 
    '''    We have illustrated the physics concepts in step by step manner for broader understanding. This application 
    gives broad explanations covering topics of each age ranging from 12 years that is class 7 to 17 years that is 
    class 12. For each class a mini-quiz of 3 questions will be available to the user who can attempt it and have 
    a deeper understanding of the concepts.
    
    Some of the topics we have included are mentioned below. 
    
    Class 7:
        For class 7, the topics included in this application are
        
        •	Light
            Light deals with formation, nature and different phenomena of light. Under this topic, daily-life 
            examples, images and activities will be depicted. The path of light will be explained with the help 
            of an activity. Mirrors, laws of reflection, spherical mirrors, spherical lenses, characteristics image 
            formed and sunlight will be among the various other topics to be discussed in this topic.

        •	Electric current and its effects
            This topic deals with the basics of electric circuit, heating and magnetic effect of electric current 
            and its applications. Here, symbols of electric components, heating effect, magnetic effect, 
            electromagnet and electric bell are among the various other topics to be explained with visual 
            representations of the circuits and many other experiments.

    Class 8:
        For class 8, the topics included in this application are
        
        •	Force and pressure
            This topic includes introduction to force, its various types, introduction to pressure, pressure exerted
            by liquids and gases and atmospheric pressure. The relation between force and pressure will be depicted 
            through various experiments. 

        •	Friction
            Friction deals with the slowing down or resistance of motion. Its causes, effects, applications and 
            other fundamental properties are discussed in this topic. This application will also depict wheels 
            reducing friction and fluid friction.

    Class 9:
        For class 9, the topics included in this application are
    
        •	Force and Laws of Motion
            This topic includes explanations and visual representation of Newton’s three laws of motion, law of 
            conservation of momentum, formulae and various applications in our everyday lives which can be displayed
            in a pictorial and animated format.
        
        •	Gravitation
            This topic includes Newton’s Universal Law of Gravitation, its importance and applications, free fall, 
            mass, weight, thrust and pressure, buoyancy, Archimedes’ Principle and relative density.  This topic 
            also includes various experiments and applications in everyday life which can be represented visually.
        
        •	Work and Energy
            Work and Energy includes introduction to the concept of work done by a body, energy, kinetic and 
            potential energy, Law of Conservation of Energy and Commercial Unit of Energy. 
        
        •	Sound
            This topic includes propagation of sound, the concept of sound being a longitudinal wave, its 
            characteristics, reflection of sound, echo, reverberation, applications of multiple reflection of sound,
            range of hearing, applications of Ultrasound, the working of SONAR and structure of the human ear. 
        
    Class 10:
        For class 10, the topics included in this application are
            
        •	Electricity
            Electricity involves topics like electric current and circuit, potential difference, Ohm’s Law, 
            resistance, resistivity, resistors in series and parallel, heating effects of electric current and its 
            applications in daily life and electric power.
            
        •	Magnetic Effects of Electric Current
            This topic involves magnetic field, field lines, magnetic field due to current carrying conductor, 
            Maxwell’s Right Hand Thumb Rule, Fleming’s Left Hand Rule, Electric Motor, Electromagnetic Induction, 
            Fleming’s Right Hand Rule, Electric Generator and Domestic Electric Circuits. There are various 
            experiments which will be pictorially represented in this application.
            
        •	Light
            This topic includes laws of reflection, plane and spherical mirrors and their characteristics and ray 
            diagrams, mirror formula and magnification, refraction of light, spherical lenses, their characteristics
            and ray diagrams, lens formula and magnification and power of a lens.
                
    Class 11:
        For class 11, the topics in this application include
        
        •	Kinematics and Laws of Motion
            	Kinematics involves motion in a straight line which includes new concepts like instantaneous 
            velocity, instantaneous accelerationand relative velocity of an object in a straight line. Kinematics 
            also includes motion in a plane which introduces the concept of vectors, projectile motion and relative 
            velocity of an object in a plane.
            	In Laws of Motion, Newton’s three Laws of Motion, Law of Conservation of Momentum, equilibrium of a 
            particle, common forces in mechanics and circular motion.
            
        •	Gravitation
            This topic includes Kepler’s Planetary Laws, Newton’s Universal Law of Gravitation, variation of 
            acceleration due to gravity with height and depth from the Earth surface, gravitational potential energy,
            escape velocity, orbital  velocity, time period and total energy and geostationary and polar satellites.
            
        •	Oscillations
            This topic includes periodic and oscillatory motions, simple harmonic motion and uniform circular motion, 
            velocity and acceleration in simple harmonic motion, systems executing SHM, damped simple harmonic 
            motion and forced oscillations and resonance.
            
    Class 12:
        For class 12, the topics included in this application are

        •	Electrostatics
            This topic includes electric charges and fields under which there are various topics like characteristics 
            of charge, Gauss’s law and its applications. Electrostatics also includes electrostatic potential and 
            capacitance which discusses topics like electrostatic potential, equipotential surfaces and capacitors 
            and capacitance.
                
        •	Communication System
            This topic includes propagation of electromagnetic wave, different types of waves, amplitude modulation 
            and production and detection of amplitude modulated wave.''', font=('courier',14), fill = 'white')
    
    hbar=Scrollbar(canvas_about,orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill=X)
    hbar.config(command=canvas_about.xview)
    vbar=Scrollbar(canvas_about,orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=canvas_about.yview)
    canvas_about.config(width=1500, height=900)
    canvas_about.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas_about.pack(side=LEFT, expand=True, fill=BOTH)
    
    Back_About=Button(phy_about, bg='coral2', text='<--', command=Back_About)
    Back_About.pack()
    Back_About.place(relx=.0,rely=.0)
    
def Quit():
    phy.destroy()
    
Start=Button(phy, height=1, width=8, bg='coral2', text='Start', font=('Castellar',27), command=Start1)
About=Button(phy, height=1, width=8, bg='coral2', text='About', font=('Castellar',27), command=About)
Quit=Button(phy, height=1, width=8, bg='coral2', text='Quit', font=('Castellar',27), command=Quit)
Start.pack()
Start.place(relx=.43,rely=.55)
About.pack()
About.place(relx=.43,rely=.65)
Quit.pack()
Quit.place(relx=.43,rely=.75)
phy.mainloop() 
