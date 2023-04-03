from tkinter import *
from random import *
from math import *

def clavier(event) :
    global canvas
    global ecran
    global labyrinthe
    global position
    global arrivee
    global photo_perso
    global perso
    global stage
    global cache2
    global cache3
    global cache4
    global cache5
    global cache6
    global cache7
    global cache8
    global cache9
    global pos_boss
    global pause
    global indic_pause
    touche = event.keysym
    if ecran == 1 :
        if touche == "Return" :
            stage = 1
            pause = 0
            canvas.after(100,generationlab)
    elif ecran == 2 :
        if touche == "Return" :
            if pause == 1 :
                pause = 0
                canvas.delete(indic_pause)
            else :
                pause = 1
                if stage == 1 :
                    canvas.delete(indic_pause)
                indic_pause = canvas.create_text(780,30,text="II",font="Arial 28",fill='white')
        elif pause == 0 :
            if touche == "Up" :
                modif = -25
            elif touche == "Down" :
                modif = 25
            elif touche == "Left" :
                modif = -1
            elif touche == "Right" :
                modif = 1
            if touche == "Up" or touche == "Down" or touche == "Left" or touche == "Right" :
                if labyrinthe[position+modif] == 1 :
                    position += modif
                    canvas.delete(perso)
                    if modif == -25 :
                        photo_perso = PhotoImage(file=raccourci+'perso1.png')
                    elif modif == 1 :
                        photo_perso = PhotoImage(file=raccourci+'perso2.png')
                    elif modif == 25 :
                        photo_perso = PhotoImage(file=raccourci+'perso3.png')
                    elif modif == -1 :
                        photo_perso = PhotoImage(file=raccourci+'perso4.png')
                    perso = canvas.create_image(150+(position%25)*20,int(position/25)*20,anchor=NW,image=photo_perso)
                    if mode == 3 or mode == 4 :
                        canvas.coords(cache2,150,0,150+(position%25)*20,int(position/25)*20)
                        canvas.coords(cache3,650,0,(150+(position%25)*20)+20,(int(position/25)*20))
                        canvas.coords(cache4,150,800,150+(position%25)*20,(int(position/25)*20)+20)
                        canvas.coords(cache5,650,800,(150+(position%25)*20)+20,(int(position/25)*20)+20)
                        a = 1
                        while not labyrinthe[position+(-25)*a] == 2 and not position+(-25)*a < 25 :
                            a += 1
                        canvas.coords(cache6,150+(position%25)*20,0,(150+(position%25)*20)+20,int(position/25)*20-a*20)
                        a = 1
                        while not labyrinthe[position+a] == 2 :
                            a += 1
                        canvas.coords(cache7,801,int(position/25)*20,(150+(position%25)*20)+20+a*20,(int(position/25)*20)+20)
                        a = 1
                        while not labyrinthe[position+25*a] == 2 and not position+25*a > 599 :
                            a += 1
                        canvas.coords(cache8,150+(position%25)*20,501,(150+(position%25)*20)+20,int(position/25)*20+20+a*20)
                        a = 1
                        while not labyrinthe[position+(-1)*a] == 2 :
                            a += 1
                        canvas.coords(cache9,0,int(position/25)*20,150+(position%25)*20-a*20,(int(position/25)*20)+20)
                if position == arrivee :
                    stage += 1
                    generationlab()

def titre() :
    global canvas
    global ecran
    global photo_titre
    global score
    global record
    ecran = 1
    canvas.delete('all')
    photo_titre = PhotoImage(file=raccourci+'titre.png')
    titre = canvas.create_image(84,50,anchor=NW,image=photo_titre)
    t = canvas.create_text(400,330,text="Record : "+str(record),font="Arial 20",fill='white')
    t = canvas.create_text(400,380,text="Score : "+str(stage),font="Arial 20",fill='white')
    t = canvas.create_text(400,450,text="Appuyer sur <entrée> pour commencer",font="Arial 20",fill='white')

def gameover() :
    global canvas
    global photo_gameover
    global ecran
    global stage
    global record
    ecran = 3
    photo_gameover = PhotoImage(file=raccourci+'game over.png')
    ecran_gameover = canvas.create_image(0,-50,anchor=NW,image=photo_gameover)
    if stage > record :
        record = stage
    canvas.after(3000,titre)

def generationlab() :
    global canvas
    global labyrinthe
    global photo_mur
    global ecran
    global cote_apparition
    global position
    global arrivee
    global photo_perso
    global perso
    global mode
    global stage
    global cache2
    global cache3
    global cache4
    global cache5
    global cache6
    global cache7
    global cache8
    global cache9
    global pos_boss
    global photo_boss
    global minotaure
    global indic_pause
    ecran = 2
    if stage == 1 :
        mode = 1
    elif stage == 2 :
        mode = randint(1,5)
        if mode == 5 :
            mode = 2
        else :
            mode = 1
    elif stage == 3 :
        mode = randint(1,5)
        if mode <= 3 :
            mode = 1
        else :
            mode = 2
    elif stage == 4 :
        mode = randint(1,5)
        if mode <= 2 :
            mode = 1
        else :
            mode = 2
    elif stage == 5 :
        mode = randint(1,5)
        if not mode == 1 :
            mode = 2
    elif stage == 6 :
        mode = 3
    elif stage == 7 :
        mode = randint(1,5)
        if mode == 5 :
            mode = 4
        else :
            mode = 3
    elif stage == 8 :
        mode = randint(1,5)
        if mode <= 3 :
            mode = 3
        else :
            mode = 4
    elif stage == 9 :
        mode = randint(1,5)
        if mode <= 2 :
            mode = 3
        else :
            mode = 4
    elif stage == 10 :
        mode = randint(1,5)
        if mode == 1 :
            mode = 3
        else :
            mode = 4
    else :
        mode = 4

    labyrinthe = []
    for loop in range (50) :
        labyrinthe += [2]
    for loop in range (10) :
        labyrinthe += [2]
        for loop in range (11) :
            labyrinthe += [2,0]
        labyrinthe += [2,2]
        for loop in range (25) :
            labyrinthe += [2]
    labyrinthe += [2]
    for loop in range (11) :
        labyrinthe += [2,0]
    labyrinthe += [2,2]
    for loop in range (50) :
        labyrinthe += [2]
    case = 0
    while not labyrinthe[case] == 0 :
        case = randint(0,624)
    anciendep = []
    labyrinthe[case] = 1
    non = 1
    while non == 1 :
        if labyrinthe[case-50] == 0 or labyrinthe[case+2] == 0 or labyrinthe[case+50] == 0 or labyrinthe[case-2] == 0 :
            direc = randint(1,4)
            if direc == 1 :
                modif = -50
            elif direc == 2 :
                modif = 2
            elif direc == 3 :
                modif = 50
            elif direc == 4 :
                modif = -2
            while not labyrinthe[case+modif] == 0 :
                direc = randint(1,4)
                if direc == 1 :
                    modif = -50
                elif direc == 2 :
                    modif = 2
                elif direc == 3 :
                    modif = 50
                elif direc == 4 :
                    modif = -2
            labyrinthe[case+modif] = 1
            labyrinthe[case+int(modif/2)] = 1
            anciendep += [case]
            case += modif
        else :
            if labyrinthe[case-50] == 1 or labyrinthe[case+2] == 1 or labyrinthe[case+50] == 1 or labyrinthe[case-2] == 1 :
                direc = randint(1,4)
                if direc == 1 :
                    modif = -25
                elif direc == 2 :
                    modif = 1
                elif direc == 3 :
                    modif = 25
                elif direc == 4 :
                    modif = -1
                while not labyrinthe[case+modif*2] == 1 :
                    direc = randint(1,4)
                    if direc == 1 :
                        modif = -25
                    elif direc == 2 :
                        modif = 1
                    elif direc == 3 :
                        modif = 25
                    elif direc == 4 :
                        modif = -1
                labyrinthe[case+modif] = 1
            case = anciendep[-1]
            del anciendep[-1:len(anciendep)]
        decode = 0
        while decode < len(labyrinthe) and not labyrinthe[decode] == 0 :
            decode += 1
        if decode == len(labyrinthe) :
            non = 0
    a = 1
    while not a%2 == 0 :
        a = randint(2,22)

    labyrinthe[a+600] = 0
    labyrinthe[a+575] = 1
    position = a+575
    a = 22-(a-2)
    arrivee = 624-position
    if mode == 2 or mode == 4 :
        pos_boss = arrivee-25
        sens = 3
    labyrinthe[a] = 0
    labyrinthe[a+25] = 1
    canvas.delete('all')
    x = 0
    y = 0
    nb = 0
    photo_mur = PhotoImage(file=raccourci+'bloc jour.png')
    for loop in range (25) :
        for loop in range (25) :
            if labyrinthe[nb] == 2 :
                canvas.create_image(150+x,y,anchor=NW,image=photo_mur)
            x += 20
            nb += 1
        x = 0
        y += 20
    cache = canvas.create_rectangle(0,0,150,501,fill='black')
    cache = canvas.create_rectangle(650,0,801,501,fill='black')
    rond_arrivee = canvas.create_oval(150+(arrivee%25)*20,int(arrivee/25)*20,(150+(arrivee%25)*20)+20,(int(arrivee/25)*20)+20,fill='blue')
    photo_perso = PhotoImage(file=raccourci+'perso1.png')
    perso = canvas.create_image(150+(position%25)*20,int(position/25)*20,anchor=NW,image=photo_perso)
    if mode == 3 or mode == 4 :
        cache2 = canvas.create_rectangle(150,0,150+(position%25)*20,int(position/25)*20,fill='black')
        cache3 = canvas.create_rectangle(650,0,(150+(position%25)*20)+20,(int(position/25)*20),fill='black')
        cache4 = canvas.create_rectangle(150,800,150+(position%25)*20,(int(position/25)*20)+20,fill='black')
        cache5 = canvas.create_rectangle(650,800,(150+(position%25)*20)+20,(int(position/25)*20)+20,fill='black')
        a = 1
        boss = 0
        while not labyrinthe[position+(-25)*a] == 2 and not position+(-25)*a < 25 :
            if mode == 2 or mode == 4 :
                if position+(-25)*a == pos_boss :
                    boss = 1
            a += 1
        cache6 = canvas.create_rectangle(150+(position%25)*20,0,(150+(position%25)*20)+20,int(position/25)*20-a*20,fill='black')
        a = 1
        while not labyrinthe[position+a] == 2 :
            if mode == 2 or mode == 4 :
                if position+a == pos_boss :
                    boss = 1
            a += 1
        cache7 = canvas.create_rectangle(800,int(position/25)*20,(150+(position%25)*20)+20+a*20,(int(position/25)*20)+20,fill='black')
        a = 1
        boss = 0
        while not labyrinthe[position+25*a] == 2 and not position+25*a > 599 :
            if mode == 2 or mode == 4 :
                if position+25*a == pos_boss :
                    boss = 1
            a += 1
        cache8 = canvas.create_rectangle(150+(position%25)*20,500,(150+(position%25)*20)+20,int(position/25)*20+20+a*20,fill='black')
        a = 1
        while not labyrinthe[position+(-1)*a] == 2 :
            if mode == 2 or mode == 4 :
                if position+(-1)*a == pos_boss :
                    boss = 1
            a += 1
        cache9 = canvas.create_rectangle(0,int(position/25)*20,150+(position%25)*20-a*20,(int(position/25)*20)+20,fill='black')
    t = canvas.create_text(70,20,text="Record : "+str(record),font="Arial 20",fill='white')
    t = canvas.create_text(62,60,text="Score : "+str(stage),font="Arial 20",fill='white')
    if stage == 1 :
        indic_pause = canvas.create_text(650,20,text="Appuyez sur <entrée> pour mettre le jeu en pause.",fill='white')
    elif stage == 6 :
        t = canvas.create_text(80,480,text="La nuit vient de tomber.",fill='red')
    if mode == 2 or mode == 4 :
        t = canvas.create_text(150,480,text="Le minotaure vous cherche ne vous faite pas attraper !",fill='red')
    ecran = 2
    if mode == 2 :
        photo_boss = PhotoImage(file=raccourci+'minotaure'+str(sens)+'.png')
        minotaure = canvas.create_image(150+(pos_boss%25)*20,int(pos_boss/25)*20,anchor=NW,image=photo_boss)
    elif mode == 4 :
        minotaure = canvas.create_rectangle(0,0,1,1,fill='black')
    if mode == 2 or mode == 4 :
        mouvboss()

def mouvboss() :
    global canvas
    global labyrinthe
    global mode
    global position
    global pos_boss
    global photo_boss
    global minotaure
    global sens
    dep_poss1 = 0
    dep_poss2 = 0
    dep = 0
    if pause == 0 :
        if position%25 > pos_boss%25 and int(position/25) < int(pos_boss/25) :
            if labyrinthe[pos_boss-25] == 1 or labyrinthe[pos_boss+1] == 1 :
                if not labyrinthe[pos_boss-25] == 1 :
                    dep = 1
                elif not labyrinthe[pos_boss+1] == 1 :
                    dep = -25
                else :
                    a = randint(1,2)
                    if a == 1 :
                        dep = -25
                    else :
                        dep = 1
            else :
                a = randint(1,2)
                if a == 1 :
                    dep = 25
                else :
                    dep = -1
        elif position%25 > pos_boss%25 and int(position/25) > int(pos_boss/25) :
            if labyrinthe[pos_boss+25] == 1 or labyrinthe[pos_boss+1] == 1 :
                if not labyrinthe[pos_boss+25] == 1 :
                    dep = 1
                elif not labyrinthe[pos_boss+1] == 1 :
                    dep = 25
                else :
                    a = randint(1,2)
                    if a == 1 :
                        dep = 25
                    else :
                        dep = 1
            else :
                a = randint(1,2)
                if a == 1 :
                    dep = -25
                else :
                    dep = -1
        elif position%25 < pos_boss%25 and int(position/25) > int(pos_boss/25) :
            if labyrinthe[pos_boss+25] == 1 or labyrinthe[pos_boss-1] == 1 :
                if not labyrinthe[pos_boss+25] == 1 :
                    dep = -1
                elif not labyrinthe[pos_boss-1] == 1 :
                    dep = 25
                else :
                    a = randint(1,2)
                    if a == 1 :
                        dep = 25
                    else :
                        dep = -1
            else :
                a = randint(1,2)
                if a == 1 :
                    dep = -25
                else :
                    dep = 1
        elif position%25 < pos_boss%25 and int(position/25) < int(pos_boss/25) :
            if labyrinthe[pos_boss-25] == 1 or labyrinthe[pos_boss-1] == 1 :
                if not labyrinthe[pos_boss-25] == 1 :
                    dep = -1
                elif not labyrinthe[pos_boss-1] == 1 :
                    dep = -25
                else :
                    a = randint(1,2)
                    if a == 1 :
                        dep = -25
                    else :
                        dep = -1
            else :
                a = randint(1,2)
                if a == 1 :
                    dep = 25
                else :
                    dep = 1
        elif position%25 == pos_boss%25 and int(position/25) < int(pos_boss/25) and labyrinthe[pos_boss-25] == 1 :
            dep = -25
        elif position%25 == pos_boss%25 and int(position/25) > int(pos_boss/25) and labyrinthe[pos_boss+25] == 1 :
            dep = 25
        elif position%25 > pos_boss%25 and int(position/25) == int(pos_boss/25) and labyrinthe[pos_boss+1] == 1 :
            dep = 1
        elif position%25 < pos_boss%25 and int(position/25) == int(pos_boss/25) and labyrinthe[pos_boss-1] == 1 :
            dep = -1
        if not dep == 0 :
            pos_boss += dep
            if dep == -25 :
                sens = 1
            elif dep == 1 :
                sens = 2
            elif dep == 25 :
                sens = 3
            elif dep == -1 :
                sens = 4
                canvas.delete(minotaure)
            if mode == 2 :
                photo_boss = PhotoImage(file=raccourci+'minotaure'+str(sens)+'.png')
                perso = canvas.create_image(150+(pos_boss%25)*20,int(pos_boss/25)*20,anchor=NW,image=photo_boss)
            else :
                if mode == 4 :
                    a = 1
                    boss = 0
                    while not labyrinthe[position+(-25)*a] == 2 and not position+(-25)*a < 25 :
                        if labyrinthe[position+(-25)*a] == pos_boss :
                            boss = 1
                        a += 1
                    a = 1
                    while not labyrinthe[position+a] == 2 :
                        if position+a == pos_boss :
                            boss = 1
                        a += 1
                    a = 1
                    while not labyrinthe[position+25*a] == 2 and not position+25*a > 599 :
                        if position+25*a == pos_boss :
                            boss = 1
                        a += 1
                    a = 1
                    while not labyrinthe[position+(-1)*a] == 2 :
                        if position+(-1)*a == pos_boss :
                            boss = 1
                        a += 1
                    canvas.delete(minotaure)
                    if boss == 1 :
                        photo_boss = PhotoImage(file=raccourci+'minotaure'+str(sens)+'.png')
                        minotaure = canvas.create_image(150+(pos_boss%25)*20,int(pos_boss/25)*20,anchor=NW,image=photo_boss)
                    else :
                        minotaure = canvas.create_rectangle(0,0,1,1,fill='black')
    if mode == 2 or mode == 4 :
        if pos_boss == position :
            gameover()
        else :
            canvas.after(500,mouvboss)
fenetre = Tk()
fenetre.title("Le Minotaure")

raccourci = __file__
raccourci = raccourci[0:-8]

record = 0
stage = 0

canvas = Canvas(fenetre,width=800,height=500,bg='#E0BC7F')
canvas.pack()
canvas.focus_set()
canvas.bind("<Key>",clavier)
ecran = 1
titre()

i = 2

fenetre.mainloop()
