print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"*2,end='')
print("$$$   ______________  __________    __________  ___   __  __________  __        __   $$$")
print("$$$   |____    ____| |  ______  |  | ________|  | |  / /  | _______|  \ \      / /   $$$")
print("$$$        |  |      | |      | |  | |          | | / /   | |______    \ \   / /     $$$")
print("$$$        |  |      | |      | |  | |          |  < <    |  ______|     \ V /       $$$")
print("$$$      __|  |      | |______| |  | |_______   | | \ \   | |_______      | |        $$$")
print("$$$     |_____|      |__________|  |_________|  |_|  \_\  |________|      |_|        $$$")
print("$$$                                                                                  $$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"*2) 
print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
print("^v^v^v^v^v^v^v^v^v^v^v^v^                                       ^v^v^v^v^v^v^v^v^v^v^v^v^")
print("^v^v^v^v^v^v^v^v^v^v^v^v^    WELCOME TO HABIB JOCKEY CLUB!!!    ^v^v^v^v^v^v^v^v^v^v^v^v^")
print("^v^v^v^v^v^v^v^v^v^v^v^v^        WHERE STABLES TURN!!!          ^v^v^v^v^v^v^v^v^v^v^v^v^")
print("^v^v^v^v^v^v^v^v^v^v^v^v^                                       ^v^v^v^v^v^v^v^v^v^v^v^v^")
print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^\n")
print("#########################################################################################")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXX      THERE ARE THREE HORSE:      XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("#########################################################################################\n")
print(" "*21+"(((((((((((((' BLACK HORSE '))))))))))))")
print(" "*21+"(((((((((((((' BLUE HORSE ')))))))))))))")
print(" "*21+"((((((((((((((' RED HORSE ')))))))))))))")
print()
print()
correcthorse = True
while correcthorse == True:
    k = str(input("Choose your horse: "))
    k = k.lower()
    if k!="red" and k!="black" and k!="blue":
        print("Invalid choice")
        print("Please choose a horse between the following colors: Black, Blue or Red Horse")
        correcthorse = True
    else:
        correcthorse = False


bettedamount = True
while bettedamount   ==  True:
    w = int(input("Place your bet (limit 500-10000): "))
    if w<500 or w>10000:
        print("Invalid Betting Amount")
        print("Enter a value between 500 and 10000")
        bettedamount = True
    else:
        bettedamount = False


from tkinter import *
import time
import random

winner = False

#defining coordinates

black_horse_x = 5      #this is black horse
red_horse_y = 70

red_horse_x = -15           #this is the red horse
horse_red_y = 220

blue_horse_x= 5                #this is the blue horse
black_horse_y = 170

crowd1_x = 0
crowd1_y = 0

crowd2_x = 0
crowd2_y = 340

track1_x = 0
track1_y = 150

track2_x = 0
track2_y = 240

#creating function:

def start_game():
    global red_horse_x
    global blue_horse_x
    global black_horse_x
    global winner

    while winner == False:
        time.sleep(0.07)
        random_move_blue_horse = random.randint(0,20)
        random_move_black_horse = random.randint(0,20)
        random_move_red_horse = random.randint(0,20)

        blue_horse_x += random_move_blue_horse
        black_horse_x += random_move_black_horse
        red_horse_x += random_move_red_horse

        move_horses(random_move_red_horse,random_move_blue_horse,random_move_black_horse)
        main_screen.update()
        winner = check_winner(w)

    if winner == "Tie":
        Label(main_screen,text=winner,font=('Helvetica',20),fg='green').place(x=200,y=450)
    elif winner == "SORRY!! Blue Horse Won" or winner == "SORRY!! Red Horse Won" or winner == "SORRY!! Black Horse Won":
        Label(main_screen,text=winner+". "+str(w)+' lost !!',font=('Helvetica',20),fg='green',bg='white').place(x=140,y=450)
    else:
        Label(main_screen,text=winner,font=('Helvetica',20),fg='green',bg='white').place(x=60,y=450)




def move_horses(red_horses_random_move,blue_horse_random_move,black_horse_random_move):
    canvas.move(red_horse,red_horses_random_move,0)
    canvas.move(blue_horse,blue_horse_random_move,0)
    canvas.move(black_horse,black_horse_random_move,0)

def check_winner(w):
    if red_horse_x >= 670 and blue_horse_x >=670 and black_horse_x >=670:
        return "TIE"
    if blue_horse_x >= 670:
        if k == "blue":
            t = w*3
            z = "Congrats!! Blue Horse Won. Your winnings: " + str(t)
            return (z)
        else:
            return "SORRY!! Blue Horse Won"
    if red_horse_x >= 670:
        if k=="red":
            t = w*3
            z ="Congrats!! Red Horse Won. Your winnings: " + str(t)
            return (z)
        else:
            return "SORRY!! Red Horse Won"
    if black_horse_x >= 670:
        if k == "black":
            t = w*3
            z = "Congrats!! Black Horse Won. Your winnings: " + str(t)
            return (z)
        else:
            return "SORRY!! Black Horse Won"
    return False

#main screen settings

main_screen = Tk()
main_screen.title('Horse Racing')
main_screen.geometry('750x650')
#Background image
main_screen.config(background='white')
#Size of canvas
canvas = Canvas(main_screen,width=750,height=400,bg='#7FFF00')
canvas.pack(pady=20)
#Horses' Images
red_horse_img = PhotoImage(file="./horse_red (2).png")
horse_img = PhotoImage(file="./horse_redi.png")
black_horse_img = PhotoImage(file="./Black_horse.png")

#crowd images
crowd1_img = PhotoImage(file="./crowd.png")
crowd2_img = PhotoImage(file="./crowds.png")

crowd1_img = crowd1_img.zoom(2)
crowd1_img = crowd1_img.subsample(15)

crowd2_img = crowd2_img.zoom(2)
crowd2_img = crowd2_img.subsample(15)

#track images

track1_img =  PhotoImage(file="./track.png")
track2_img =  PhotoImage(file="./track.png")


#Sizing the horses
red_horse_img = red_horse_img.zoom(11)
red_horse_img = red_horse_img.subsample(80)
horse_img = horse_img.zoom(3)
horse_img = horse_img.subsample(55)
black_horse_img = black_horse_img.zoom(11)
black_horse_img = black_horse_img.subsample(90)

#Attaching images to canvas
black_horse = canvas.create_image(black_horse_x,red_horse_y, anchor=NW, image=red_horse_img)        #black
blue_horse = canvas.create_image(blue_horse_x,black_horse_y, anchor=NW, image=black_horse_img)    #blue
red_horse = canvas.create_image(red_horse_x,horse_red_y, anchor=NW, image=horse_img)               #red

crowd1 = canvas.create_image(crowd1_x,crowd1_y, anchor=NW, image=crowd1_img)
crowd2 = canvas.create_image(crowd2_x,crowd2_y, anchor=NW, image=crowd2_img)

track1 = canvas.create_image(track1_x,track1_y, anchor=NW, image=track1_img)
track2 = canvas.create_image(track2_x,track2_y, anchor=NW, image=track2_img)

#designing labels


l1 = Label(main_screen,text="Click PLAY when ready !",font=('calibri',23),bg='white')
l1.place(x=210,y=495)

b1 = Button(main_screen,text='Play!',height=1,width = 14,bg='white',font=('calibri',28),command=start_game)

b1.place(x=220,y=550)



main_screen.mainloop()
