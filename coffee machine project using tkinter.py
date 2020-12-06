
#first , the menu card will be displayed
#user can order their drink , else exit, else can view report
#if user orders, payment must be payed, after verification , user will get their drink and asked for feedback
#if exit is selected , the order gets stopped
#if report is asked, the products used for each cup of drink gets displayed


from tkinter import*


def buttons():
    button1=Radiobutton(window,text="espresso",command=espresso).grid(column=0,row=1)
    button2=Radiobutton(window,text="latte",command=latte).grid(column=0,row=2)
    button3=Radiobutton(window,text="cappuccino",command=cappuccino).grid(column=0,row=3)
    button4=Radiobutton(window,text="exit",command=exit).grid(column=0,row=4)
    button5=Radiobutton(window,text="report",command=report).grid(column=0,row=5)


def yes():
    title9=Label(window,text="THANK YOU :) ").grid(column=0,row=27)
def no():
    title10=Label(window,text="OOPS ,SORRY :( thanks for letting us know ! ").grid(column=0,row=27)
    

def statement():
    title1=Label(window,text="You have made your order")
    title1.grid(column=0,row=5)



def espresso():
    statement()
    title2=Label(window,text="ESPRESSO costs $0.50\nkindly pay the cost!!!")
    title2.grid(column=0,row=6)
    payment()
    
def latte():
    statement()
    title3=Label(window,text="LATTE costs $0.62\nkindly pay the cost!!!")
    title3.grid(column=0,row=6)
    payment()
    
def cappuccino():
    statement()
    title4=Label(window,text="CAPPUCCINO costs $1.62\nkindly pay the cost!!!")
    title4.grid(column=0,row=6)
    payment()
    
def exit():
    title5=Label(window,text="order stopped!!").grid(column=0,row=5)
def report():
    title6=Label(window,text=" for each order, the following products get loaded to make the ordered drink: \n water = 60ml \n milk = 60ml \n coffee beans(powder) = 7grams \n cup = 1 ").grid(column=0,row=5)
    

    
    
def payment():
    title7=Label(window,text="-----------------------------------------------------------------------------------\n***PAY THE COST , NO CHANGE CAN BE RETURNED***\nENTER THE AMOUNT OF MONEY IN TERMS OF DIMES($0.10),NICKEL($0.05),PENNIES($0.01)").grid(column=0,row=8)
    pay1=Label(window,text="your payment: ").grid(column=0,row=11)
    payed=Entry(window).grid(column=0,row=14)
    title8=Label(window,text="PAYMENT GETS VERIFIED BY THE STAFF*******************VERIFIED!!!!!!\n //TAKE YOUR DRINK & HAVE A NICE DAY!").grid(column=0,row=17)
    feedback()



def feedback():
    title_=Label(window,text="Do you enjoyed my service :)coffee machine//").grid(column=0,row=19)
    y=Button(window,text="oh! yes",bg='green',command=yes).grid(column=0,row=21)
    n=Button(window,text="Nope",bg='red',command=no).grid(column=0,row=24)
    

    

    

window=Tk()
title=Label(window,text="COFFEE MACHINE\n-----------------------------MENU CARD------------------------------------\n1.Espresso : $0.50\n2.Latte : $0.62\n3.cappuccino : $1.63\n--------------------------------------------------------------------------\nMAKE YOUR ORDER!!!")
title.grid(column=0,row=0)
buttons()


window.mainloop()
