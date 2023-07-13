import tkinter as tk

root = tk.Tk()

root.geometry("500x500") # display dimensions
root.title("My first GUI") # title

label = tk.Label(root, text="Hello World!", font=("Arial",18))

label.pack(padx=20,pady=20)

textbox = tk.Text(root, height=3, font=("Arial",16))
textbox.pack(padx=10)

# myentry = tk.Entry(root) # no multiline textbox with height=1
# myentry.pack()

button = tk.Button(root,text="Click Me!",font=('Ariel',18))
button.pack(padx=10,pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1) 
buttonframe.columnconfigure(2, weight=1) 

btn1 = tk.Button(buttonframe,text="1",font=("Arial",18))
btn1.grid(row=0,column=0, sticky="we") # sticks to west and east borders 


btn2 = tk.Button(buttonframe,text="2",font=("Arial",18))
btn2.grid(row=0,column=1, sticky="we") # sticks to west and east borders

btn3 = tk.Button(buttonframe,text="3",font=("Arial",18))
btn3.grid(row=0,column=2, sticky="we") # sticks to west and east borders

btn4 = tk.Button(buttonframe,text="4",font=("Arial",18))
btn4.grid(row=1,column=0, sticky="we") # sticks to west and east borders

btn5 = tk.Button(buttonframe,text="5",font=("Arial",18))
btn5.grid(row=1,column=1, sticky="we") # sticks to west and east borders

btn6 = tk.Button(buttonframe,text="6",font=("Arial",18))
btn6.grid(row=1,column=2, sticky="we") # sticks to west and east borders

buttonframe.pack(fill="x")

anotherbtn = tk.Button(root,text="TEST")
anotherbtn.place(x=200,y=200,height=100,width=100)


root.mainloop()