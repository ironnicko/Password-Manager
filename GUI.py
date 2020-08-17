import Guuco
import tkinter

def start():
    output.delete(0.0,tkinter.END)
    op = Guuco.paper.load_data() + '\n'
    output.insert(tkinter.END, op)


main = tkinter.Tk()
main.geometry('800x600')
main.title('Pour ton passwords')

label=tkinter.Label(main,text='Welcome')
label.grid(row='0',column='0')

can=tkinter.Canvas(main,relief='raised',borderwidth=10)
can.grid(row='0',column='10')

button=tkinter.Button(main,text='Show Me The Passwords',command=start)
button.grid(row='1',column='1')

cancelb=tkinter.Button(main,text='cancel',command=main.destroy)
cancelb.grid(row='4',column='4',sticky='w')

output = tkinter.Text(can, width=75, height=20, bg='white', wrap=tkinter.WORD, font='none 12 bold')
output.grid()

label1 = tkinter.Label(can, text='Passwords')
label1.grid(row='1', column='5')

main.mainloop()
