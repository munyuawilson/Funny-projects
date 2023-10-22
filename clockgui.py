from tkinter import *
root=Tk()
root.title('alarm clock')
label_gui=Label(root,fg='green',bg='orange',text='Simple Alarm Gui').pack()
label_year=Label(root,fg='green',text='Year').pack()
entry_year=Entry(root,fg='green',bg='white').pack()
label_month=Label(root,fg='green',text='Month').pack()
entry_month=Entry(root,fg='green',bg='white').pack()
label_hour=Label(root,text='Hour',fg='green').pack()


entry_hour=Entry(root,fg='green',bg='white').pack()
label_min=Label(root,text='Minutes',fg='green').pack()
entry_min=Entry(root,fg='green',bg='white').pack()
button_submit=Button(root,fg='green',text='Set').pack()








root.mainloop()
