from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
# Add your own database name and password here to reflect in the code
mypass = "root" #kendi şifrenizi kullanın 
mydatabase="db"  #Veritabanı adı 

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()


root = Tk()
root.title("Kütüphane")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
background_image =Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),resample=Image.LANCZOS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

# Setting up the Head Frame
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Kütüphane Otomasyonuna \n Hosgeldiniz", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# Adding the Buttons
btn1 = Button(root,text="Kitap Detaylarını Ekle",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Kitabı Sil",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Kitap Listesini Görüntüle",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Öğrenciye Kitap Teslim Et",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Kitaba Git",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)



root.mainloop()
