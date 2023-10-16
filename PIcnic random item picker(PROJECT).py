# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:14:28 2023

@author: Don Jeffrey
"""

from tkinter import*
root=Tk()
root.title("PICNIC") 
root.geometry("400x400")


import random 

list_items = ["water bottle","Chocolates","Bread,Butter","sunglasses","Chips","Football","Jam","IDCard","Hanky"]
own_list = Label(root,text="LIST ITEMS :"+"\n"+str(list_items),wraplength=300)
bag_list = Label(root,text="BASKET ITEMS:")
sorted_list = Label(root,text="ITEMS ADDED TO BAG")


def rendlistgenerator():
    rand_1 = random.randint(1,len(list_items))
    print(rand_1)
    
    sorted_list["text"]+="\n"+str(list_items[rand_1-1])
    
    
randGen = Button(root,text="ADD TO BAG",command=rendlistgenerator,bg="orange")
    
own_list.place(relx=0.5,rely=0.5,anchor=CENTER)    
sorted_list.place(relx=0.5,rely=0.7,anchor=CENTER)   
randGen.place(relx=0.5,rely=0.9,anchor=CENTER)    


root.mainloop()