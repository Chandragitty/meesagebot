import PySimpleGUI as sg
import random

himsg=["Hai", "Hello", "hai", "hello", "hi", "Hey", "Hey there"]
hireply=["Hello, How are you doing ?","Hai, How can I help you ?","Hey, How may I asssit you today ?"]

namemsg =["What's your name ?","Your name ?","Name"]
namereply = ["My name's botty","Well, you can call me botty"]

hrumsg = ["how are you ?","How are you ?","How r u ?","how are you"]
hrureply = ["I'm doing good","I'm good","I'm fine "]

created = ["Who created you ?","Who made you ?","Who founded you ?"]
created_reply = ["I was made by Chandu","I was created by Chandu","My creater is Chandu","Chandu made me"]

pythons =["Where can I learn Python","How can I learn Python","How to learn Python","python"]
pythonsreply=["You can learn it from:\n https://www.programiz.com/python-programming\n https://www.w3schools.com/python/"]

javas = ["Where can I learn Java","How can I learn Java","How to learn Java","java"]
javasreply = ["You can learn Java in detail here:\n https://www.javatpoint.com/java-tutorial \n https://www.programiz.com/java-programming"]

Clang = ["Where can I learn C","How can I learn C","How to learn C","C"]
Clangreply =["You can learn C in detail here:\n https://www.programiz.com/c-programming \n https://www.tutorialspoint.com/cprogramming/index.html"]

SQLs = ["Where can I learn SQL ?","How can I learn SQL ? ","How to learn SQL","SQL"]
SQLSreply = ["You can learn SQL in detail here:\n https://learnsql.com \n https://www.codecademy.com/learn/learn-sql"]

sg.theme("Black")  # Add a touch of color
# All the stuff inside your window should be taken uder layout
layout =[   [sg.Text("An app designed for newbies who are interested to learn Programing")],
            [sg.Text('Enter a Query: '),sg.InputText()],
            [sg.Button("Send"),sg.Button('Close')]]
# Create the Window
window = sg.Window('Programing Resources', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read() #values [0] returns the first scanned value from its list i.e value is a list type
    for i in range(len(himsg)):
        if (values[0] == himsg[i]) and (event != "Close"):
            sg.popup_ok_cancel(random.choice(hireply),"\n",title="Bot")
    for i in range(len(namemsg)):
        if (values[0] == namemsg[i]) and (event != "Close"):
            sg.popup_ok_cancel(random.choice(namereply),"\n",title="Bot")
    for i in range(len(hrumsg)):
        if (values[0] == hrumsg[i]) and (event != "Close"):
            sg.popup_ok_cancel(random.choice(hrureply),"\n",title="Bot")
    for i in range(len(created)):
        if (values[0] == created[i]) and (event != "Close"):
            sg.popup_ok_cancel(random.choice(created_reply),"\n",title="Bot")
    for i in range(len(pythons)):
        if (values[0] == pythons[i]) and (event != "Close"):
            sg.popup_ok_cancel(pythonsreply[0],"\n", title="Bot")
    for i in range(len(javas)):
        if(values[0] == javas[i]) and (event != "Close"):
            sg.popup_ok_cancel(javasreply[0],title = "Bot")
    for i in range(len(Clang)):
         if(values[0] == Clang[i]) and (event != "Close"):
            sg.popup_ok_cancel(Clangreply[0], "\n", title = "Bot")
    for i in range(len(SQLs)):
         if(values[0] == SQLs[i]) and (event != "Close"):
            sg.popup_ok_cancel(SQLSreply[0], "\n", title = "Bot")


    if event == sg.WIN_CLOSED or event == 'Close':  # if user closes window or clicks cancel
        break
window.close()