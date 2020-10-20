from fastai import *
from fastai.vision import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import traceback

WIDTH  = 150
HEIGHT = 430
PATH   = "./models/tmp"
MODEL  = "stage-1_2.pkl"

def err_msg(msg = "Херня случилась!"):
    messagebox.showerror(title="Ашыбка", message=msg)

def process_file(filename, learn):
    txt = filename.get()
    arch = models.resnet34
    sz = 224
    img = None
    try:
        img = ImageTk.PhotoImage(Image.open(txt))
        #Тут бы отобразить картинку
    except:
        err_msg();
    try:
        path = os.path.abspath('./'+txt)
        print(path)
        img_t = open_image(path)
        img_t = img_t.apply_tfms(tfms=get_transforms()[1], size=224, resize_method=1)
        pred_class, pred_idx, outputs = learn.predict(img_t)
        print(pred_class.obj)
        err_msg(pred_class.obj)
        print(outputs)

    except Exception as e:
        traceback.print_exc()
        err_msg("predict error");

    print(txt)
    

def main():
    window = tk.Tk()
    filename = tk.StringVar() # загружаемый файл
    window.geometry(f'{WIDTH}x{HEIGHT}')
    learn = load_learner(os.path.abspath(PATH), MODEL) # обученная модель
    #print(learn)
    
    upload=tk.Frame()
    uploaded_pic=tk.Label(master=upload,text="Здесь будет картинка",fg="black",bg="white", width=20, height=20)
    uploaded_pic.pack()
    upload_button=tk.Button(master=upload, text="Загрузить картинку", command = lambda: process_file(filename, learn))
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
    
    #текстбокс для файла
    filename_tb = tk.Entry(window, width = 15, textvariable = filename)
    filename_tb.place(y = HEIGHT - 25, x = 10)
    #nameEntered.grid(column = HEIGHT - 20, row = 10)
    
    #клик по кнопке загрузки
    
    window.mainloop()
    
main()

