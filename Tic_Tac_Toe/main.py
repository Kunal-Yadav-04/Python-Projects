from  tkinter import *                               #from tkinter import everything

root = Tk()                                          # This is for root window
root.geometry("375x580")                             # for gemotery of game 
root.title("Tic Tac Toe Game")                       # for title

frame_1 = Frame(root)
frame_1.pack()
titleLabel = Label(frame_1 , text="Tic Tac Toe" , font=("Arial" , 35) , bg="turquoise2",width=14 )
titleLabel.grid(row=0,column=0)

frame_2 = Frame(root)
frame_2.pack()
 
board = { 1:" " , 2:" ",3:" ",                       #creating dictionary for key value pair 
          4:" " , 5:" ",6:" ",
          7:" " , 8:" ",9:" "}

turn="x"
game_end = False

def checkForWin(player):                             #Check for Win
    #All Rows
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[6] == player:
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True
    #All Columns
    elif board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[9] == player:
        return True
    #All Diagonals
    elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
        return True
    return False

def checkForDraw():                                  #Check For Draw
        for i in board.keys():
            if board[i] == " ":
                return False
        return True

def restartGame():                                   #For Restart Game
    global game_end
    game_end = False
    for button in buttons:
        button["text"] = " "

    for i in board.keys():
        board[i] = " "

    titleLabel = Label(frame_1 , text="Tic Tac Toe" , font=("Arial" , 35) , bg="turquoise2",width=14)
    titleLabel.grid(row=0,column=0)     

    
def play(event):                                    #For print X after click        
    global turn                                     #This whole function is used to turn X into o after clicking 
    button = event.widget  
    buttonText = str(button)                        # find which buton is clicked 
    clicked = buttonText[-1]
    #print(clicked)
    if clicked == "n":                              #When we click on 1 row it print {n} so to convert it into {1}
        clicked = 1
    else:
        clicked = int(clicked)    

    
    if button["text"] == " ":                       #For avoiding overwriting like <X> and <O>
        if turn == "x":
            button["text"] ="X " 
            board[clicked]  = turn 
            if checkForWin(turn):
                #print(turn,"Wins the Game")        # for print in commande plate
                #print("Game Over")

                                                    #Print win label in GUI
                winingLabel = Label(frame_1,text=f"{turn} wins the game",bg = "MediumOrchid1",font=("Arial",35),width=14)
                winingLabel.grid(row = 0 , column=0, columnspan=3)
                game_end=True                       #for stop clicking 
            turn = "O"
        else:
            button["text"] = "O"
            board[clicked]  = turn
            if checkForWin(turn):
                #print(turn,"Wins the Game")        # for print in commande plate
                #print("Game Over")#

                                                    #Print win label in GUI
                winingLabel = Label(frame_1,text=f"{turn} wins the game",bg = "MediumOrchid1",font=("Arial",35),width=14)
                winingLabel.grid(row = 0 , column=0, columnspan=3)
                game_end=True
            turn = "x"

        if checkForDraw():                          
                                                    #Print Draw in GUI 
            drawLabel = Label(frame_1,text=f"Game  Draw",bg = "firebrick1",font=("Arial",35),width=14)
            drawLabel.grid(row = 0 , column=0, columnspan=3)


        #print(board)                                 #print dictionary
        



# Tic Tac Toe Board

#First Row

button1 = Button(frame_2,text=" ",width=4,height=2,font=("Arial",35),relief="raised",bg="maroon1",borderwidth=5)
button1.grid(row = 0,column=0)
button1.bind("<Button-1>" , play)                   # For every click print "x" or "O"

button2 = Button(frame_2,text=" ",width=4,height=2,bg="maroon1",font=("Arial",35),borderwidth = 5)
button2.grid(row = 0,column=1)
button2.bind("<Button-1>" , play)                   # For every click print "x" or "O"

button3 = Button(frame_2,text=" ",width=4,height=2,bg="maroon1",font=("Arial",35),borderwidth=5)
button3.grid(row = 0,column=2)
button3.bind("<Button-1>" , play)                   # For every click print "x" or "O"


#Second Row


button4 = Button(frame_2,text=" ",width=4,height=2,bg="maroon1",font=("Arial",35),borderwidth=5)
button4.grid(row = 1,column=0)
button4.bind("<Button-1>" , play)                   # For every click print "x" or "O"   

button5 = Button(frame_2,text=" ",width=4,height=2,bg="maroon1",font=("Arial",35),borderwidth=5)
button5.grid(row = 1,column=1)
button5.bind("<Button-1>" , play)                   # For every click print "x" or "O" 

button6 = Button(frame_2,text=" ",width=4,height=2,bg="maroon1",font=("Arial",35),borderwidth=5)
button6.grid(row = 1,column=2)
button6.bind("<Button-1>" , play)                   # For every click print "x" or "O" 
   

#Third Row


button7 = Button(frame_2,text=" ",width=4,height=2,bg="maroon1",font=("Arial",35),borderwidth=5)
button7.grid(row = 2,column=0)
button7.bind("<Button-1>" , play)                   # For every click print "x" or "O" 

button8 = Button(frame_2,text=" ",width=4,height=2,bg="maroon1",font=("Arial",35),borderwidth=5)
button8.grid(row = 2,column=1)
button8.bind("<Button-1>" , play)                   # For every click print "x" or "O" 

button9 = Button(frame_2,text=" ",width=4,height=2,bg="maroon1",font=("Arial",35),borderwidth=5)
button9.grid(row = 2,column=2)
button9.bind("<Button-1>" , play)                   # For every click print "x" or "O"   



                                                    #For Restart Button 
restartButton = Button(frame_2,text="Restart Game",width=25,height=2,font=("Arial",18),relief=RAISED,bg="turquoise2",borderwidth=5,command=restartGame)
restartButton.grid(row=4,column=0,columnspan=3 )
 

buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9]


root.mainloop()                                    #for remain screen in window 

