from tkinter import *
from tkinter import messagebox


# Generate welcoming page that ask user to input their name
def welcome():
    global entry1, entry2, welcome
    
    welcome_message = """
   WELCOME TO
TIC TAC TOE GAME
"""
    welcome = Label(text=welcome_message, font=('arial', 16, 'bold'))
    welcome.grid(row=1, column=2)

    text1 = Label(text='Input Player 1 Name:')
    text1.grid(row=3, column=1)

    entry1 = Entry(root)
    entry1.grid(row=4, column=1)

    text2 = Label(text='Input Player 2 Name:')
    text2.grid(row=3, column=3)

    entry2 = Entry(root)
    entry2.grid(row=4, column=3)

    submit = Button(root, text="START GAME", command=start)
    submit.grid(row=5, column=2)
    

# Handle program to collect user name from the entry box
def start():
    global player1_name, player2_name
    
    player1_name = entry1.get()
    player2_name = entry2.get()

    if (player1_name == '') or (player2_name == ''):
        name = messagebox.askyesno(title= 'WARNING', message='Seems like there is empty player name.\nDo you want to play as anonymous?')
        if name == True:
            player1_name = "Player 1" if len(player1_name) == 0 else entry1.get()
            player2_name = "Player 2" if len(player2_name) == 0 else entry2.get()
            welcome.destroy()
            play()
    else:
        welcome.destroy()
        play()


# Procedure to generate the main arena and all of the label and button
def play():
    global player, o, x, box
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, label4, header
    global label1, label2, label3, label4
    global round
    
    player = 0
    o = []
    x = []
    box = [x+1 for x in range(9)]
    
    header = Label(text="TIC TAC TOE GAME", font=('helvetica', 12, 'bold'))
    header.grid(row=0, column=2)

    match = "Round: " + str(round)
    label1 = Label(text=match)
    label1.grid(row=1, column=2)

    player1 = str(player1_name) + ": " + str(player1_win)
    label2 = Label(text=player1, fg='turquoise1')
    label2.grid(row=1, column=1)

    player2 = str(player2_name) + ": " + str(player2_win)
    label3 = Label(text=player2, fg='firebrick2')
    label3.grid(row=1, column=3)

    button1 = Button(root,width=20, height=10, text="1", font=('helvetica', 9, 'bold'), command=lambda: click(1))
    button1.grid(row=2, column=1)

    button2 = Button(root,width=20, height=10, text="2", font=('helvetica', 9, 'bold'), command=lambda: click(2))
    button2.grid(row=2, column=2)

    button3 = Button(root,width=20, height=10, text="3", font=('helvetica', 9, 'bold'), command=lambda: click(3))
    button3.grid(row=2, column=3)

    button4 = Button(root,width=20, height=10, text="4", font=('helvetica', 9, 'bold'), command=lambda: click(4))
    button4.grid(row=3, column=1)

    button5 = Button(root,width=20, height=10, text="5", font=('helvetica', 9, 'bold'), command=lambda: click(5))
    button5.grid(row=3, column=2)

    button6 = Button(root,width=20, height=10, text="6", font=('helvetica', 9, 'bold'), command=lambda: click(6))
    button6.grid(row=3, column=3)

    button7 = Button(root,width=20, height=10, text="7", font=('helvetica', 9, 'bold'), command=lambda: click(7))
    button7.grid(row=4, column=1)

    button8 = Button(root,width=20, height=10, text="8", font=('helvetica', 9, 'bold'), command=lambda: click(8))
    button8.grid(row=4, column=2)

    button9 = Button(root,width=20, height=10, text="9", font=('helvetica', 9, 'bold'), command=lambda: click(9))
    button9.grid(row=4, column=3)

    label4 = Label(text=player1_name + " TURN (O)")
    label4.grid(row=5, column=2)


# Procedure to handle command after click the boxes
def click(gridNum):
    global player, o, x, box
    
    textOnBox = ""

    if (gridNum == 1):
        if player%2 == 0:
            textOnBox = "O"
            button1.config(bg='turquoise1')
            o.append(1)
        else:
            textOnBox = "X"
            button1.config(bg='firebrick2')
            x.append(1)
        button1.config(text=textOnBox)
        button1["state"] = "disabled"
        box.remove(1)

    elif (gridNum == 2):
        if player%2 == 0:
            textOnBox = "O"
            button2.config(bg='turquoise1')
            o.append(2)
        else:
            textOnBox = "X"
            button2.config(bg='firebrick2')
            x.append(2)
        button2.config(text=textOnBox)
        button2["state"] = "disabled"
        box.remove(2)

    elif (gridNum == 3):
        if player%2 == 0:
            textOnBox = "O"
            button3.config(bg='turquoise1')
            o.append(3)
        else:
            textOnBox = "X"
            button3.config(bg='firebrick2')
            x.append(3)
        button3.config(text=textOnBox)
        button3["state"] = "disabled"
        box.remove(3)

    elif (gridNum == 4):
        if player%2 == 0:
            textOnBox = "O"
            button4.config(bg='turquoise1')
            o.append(4)
        else:
            textOnBox = "X"
            button4.config(bg='firebrick2')
            x.append(4)
        button4.config(text=textOnBox)
        button4["state"] = "disabled"
        box.remove(4)

    elif (gridNum == 5):
        if player%2 == 0:
            textOnBox = "O"
            button5.config(bg='turquoise1')
            o.append(5)
        else:
            textOnBox = "X"
            button5.config(bg='firebrick2')
            x.append(5)
        button5.config(text=textOnBox)
        button5["state"] = "disabled"
        box.remove(5)

    elif (gridNum == 6):
        if player%2 == 0:
            textOnBox = "O"
            button6.config(bg='turquoise1')
            o.append(6)
        else:
            textOnBox = "X"
            button6.config(bg='firebrick2')
            x.append(6)
        button6.config(text=textOnBox)
        button6["state"] = "disabled"
        box.remove(6)

    elif (gridNum == 7):
        if player%2 == 0:
            textOnBox = "O"
            button7.config(bg='turquoise1')
            o.append(7)
        else:
            textOnBox = "X"
            button7.config(bg='firebrick2')
            x.append(7)
        button7.config(text=textOnBox)
        button7["state"] = "disabled"
        box.remove(7)

    elif (gridNum == 8):
        if player%2 == 0:
            textOnBox = "O"
            button8.config(bg='turquoise1')
            o.append(8)
        else:
            textOnBox = "X"
            button8.config(bg='firebrick2')
            x.append(8)
        button8.config(text=textOnBox)
        button8["state"] = "disabled"
        box.remove(8)

    elif (gridNum == 9):
        if player%2 == 0:
            textOnBox = "O"
            button9.config(bg='turquoise1')
            o.append(9)
        else:
            textOnBox = "X"
            button9.config(bg='firebrick2')
            x.append(9)
        button9.config(text=textOnBox)
        button9["state"] = "disabled"
        box.remove(9)

    player += 1
    if player%2 == 0:
        label4.config(text=player1_name + " TURN (O)")
    else:
        label4.config(text=player2_name + " TURN (X)")
    check_win()


# Procedure to check who is the winner
def check_win():
    global condition
    global player1_win, player2_win
    
    winner = ''
    
    if 1 in o and 2 in o and 3 in o:
        winner = 'o'
    elif 4 in o and 5 in o and 6 in o:
        winner = 'o'
    elif 7 in o and 8 in o and 9 in o:
        winner = 'o'
    elif 1 in o and 4 in o and 7 in o:
        winner = 'o'
    elif 2 in o and 5 in o and 8 in o:
        winner = 'o'
    elif 3 in o and 6 in o and 9 in o:
        winner = 'o'
    elif 1 in o and 5 in o and 9 in o:
        winner = 'o'
    elif 3 in o and 5 in o and 7 in o:
        winner = 'o'
    elif 1 in x and 2 in x and 3 in x:
        winner = 'x'
    elif 4 in x and 5 in x and 6 in x:
        winner = 'x'
    elif 7 in x and 8 in x and 9 in x:
        winner = 'x'
    elif 1 in x and 4 in x and 7 in x:
        winner = 'x'
    elif 2 in x and 5 in x and 8 in x:
        winner = 'x'
    elif 3 in x and 6 in x and 9 in x:
        winner = 'x'
    elif 1 in x and 5 in x and 9 in x:
        winner = 'x'
    elif 3 in x and 5 in x and 7 in x:
        winner = 'x'
    elif (box == []) and (winner != 'x') and (winner != 'o'):
        winner = '/'

    if winner == 'o':
        condition = messagebox.askyesno(title='GAME FINISH', message=str(player1_name) + ' HAS WON!\nDo you want to play again?')
        for i in box:
            if i == 1:
                button1["state"] = "disabled"
            elif i == 2:
                button2["state"] = "disabled"
            elif i == 3:
                button3["state"] = "disabled"
            elif i == 4:
                button4["state"] = "disabled"
            elif i == 5:
                button5["state"] = "disabled"
            elif i == 6:
                button6["state"] = "disabled"
            elif i == 7:
                button7["state"] = "disabled"
            elif i == 8:
                button8["state"] = "disabled"
            elif i == 9:
                button9["state"] = "disabled"
        player1_win += 1
        next_round()
            
    elif winner == 'x':
        condition = messagebox.askyesno(title='GAME FINISH', message=str(player2_name) + ' HAS WON!\nDo you want to play again?')
        for i in box:
            if i == 1:
                button1["state"] = "disabled"
            elif i == 2:
                button2["state"] = "disabled"
            elif i == 3:
                button3["state"] = "disabled"
            elif i == 4:
                button4["state"] = "disabled"
            elif i == 5:
                button5["state"] = "disabled"
            elif i == 6:
                button6["state"] = "disabled"
            elif i == 7:
                button7["state"] = "disabled"
            elif i == 8:
                button8["state"] = "disabled"
            elif i == 9:
                button9["state"] = "disabled"
        player2_win += 1
        next_round()
                
    elif winner == '/':
        condition = messagebox.askyesno(title='GAME OVER', message='DRAW!\nDo you want to play again?')
        next_round()


# Procedure to handle algorithm for start an new round
def next_round():
    global condition
    global round

    if condition == True:
        round += 1
        play()
    else:
        root.destroy()


# Procedure to let the user enter new name for player
def changeName():
    global new_name1, new_name2
    global top
    
    top = Toplevel()
    top.title("Setting")

    x_coor = top.winfo_screenwidth()/2 - 135
    y_coor = top.winfo_screenheight()/2 - 148

    top.geometry("270x74+%d+%d" % (x_coor, y_coor))

    instruction1 = Label(top, text="Enter new Player 1 name: ")
    instruction1.grid(row=1, column=1)

    new_name1 = Entry(top)
    new_name1.grid(row=1, column=2)

    instruction2 = Label(top, text="Enter new Player 2 name: ")
    instruction2.grid(row=2, column=1)

    new_name2 = Entry(top)
    new_name2.grid(row=2, column=2)

    submit = Button(top, text="Submit", command=newName)
    submit.grid(row=3, column=1)


# Procedure to assign player new name to every aspect of the game
def newName():
    global player1_name, player2_name
    
    player1_name = new_name1.get()
    player2_name = new_name2.get()

    label2.config(text=" ")
    label2.config(text=str(player1_name) + ": " + str(player1_win))

    label3.config(text=" ")
    label3.config(text=str(player2_name) + ": " + str(player2_win))
    
    label4.config(text=" ")
    if player%2 == 0:
        label4.config(text=player1_name + " TURN (O)")
    else:
        label4.config(text=player2_name + " TURN (X)")
    
    top.destroy()


# Procedure to restart the game with the initial condition
def reset():
    global round, player, player1_win, player2_win
    global o, x, box
    
    round = 1
    player1_win = 0
    player2_win = 0
    player = 0
    o = []
    x = []
    box = [x+1 for x in range(9)]

    ask_reset = messagebox.askyesno(title="Reset Game", message="Are you sure want to reset game?")

    if ask_reset == True:
        play()
        messagebox.showinfo(title="Information", message="Game successfully reseted.")


# Procedure to quit from the game
def exit():
    ask_exit = messagebox.askyesno(title="Exit Game", message="Are you sure want to exit game?")

    if ask_exit == True:
        root.destroy()


# Main program
root = Tk()
root.title("Tic Tac Toe Game by Raffi Zulvian")
root.iconbitmap('icon.ico')

x_coor = root.winfo_screenwidth()/2 - 227
y_coor = root.winfo_screenheight()/2 - 320

root.geometry("454x550+%d+%d" % (x_coor, y_coor))

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Reset Game", command=reset)
file_menu.add_command(label="Exit Game", command=exit)

setting_menu = Menu(menu)
menu.add_cascade(label="Setting", menu=setting_menu)
setting_menu.add_command(label="Change Player Name", command=changeName)

round = 1
player1_win = 0
player2_win = 0

welcome()

root.mainloop()
