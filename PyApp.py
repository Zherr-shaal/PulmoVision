import tkinter as tk

window = tk.Tk()
window.geometry('150x400')
upload=tk.Frame()
uploaded_pic=tk.Label(master=upload,text="Здесь будет картинка",fg="black",bg="white", width=20, height=20)
uploaded_pic.pack()
upload_button=tk.Button(master=upload, text="Загрузить картинку")
upload_button.pack()
upload.pack()
conclusion=tk.Frame()
conclusion_info=tk.Label(master=conclusion,text="Статус", width=20,height=2)
conclusion_text=tk.Label(master=conclusion,text="Здоров", width=20,height=2)
conclusion_info.pack()
conclusion_text.pack()
conclusion.pack()
conclusion.place(x=0,y=0)
upload.place(x=0,y=50)
window.mainloop()

