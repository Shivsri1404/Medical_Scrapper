#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from PIL import ImageTk,Image
import sqlite3,re
from tkinter import messagebox
import requests as rt
import bs4
import os



class Gui:
    def __init__(s):
        s.scr=Tk(className='Medical_Scrapper')
        s.db=sqlite3.connect("userdata.db")
        s.cur=s.db.cursor()
        try:
            s.cur.execute('create table user(name varchar(100),password varchar(20),email varchar(100) unique,mobile varchar(10) unique)') 
        except:
            pass
        s.content=[]
        s.lst=[]
        s.lst2=[]
        s.login()
    def login(s):
        if len(s.content)!=0:
            list(map(lambda i:i.destroy(),s.content))
        mx,my=s.scr.maxsize()
        s.scr.geometry('%dx%d'%(mx,my))
        s.img=ImageTk.PhotoImage(Image.open("bgimg1.jpg"))
        l=Label(s.scr,image=s.img)
        l.image=s.img
        l.pack()
        l0=Label(s.scr,text='Please fill the details & login....',font=('times',25,'bold','underline'))
        l0.place(x=(mx//2)-250,y=0)
        f=Frame(s.scr,bg='ghost white',height=400,width=600)
        f.place(x=(mx//2)-100,y=(my//2)-250)
        l1=Label(f,text='Username : ',font=('times',20,'bold'),bg="sky blue",fg="black")
        l1.place(x=30,y=50)
        l2=Label(f,text='Password : ',font=('times',20,'bold'),bg="sky blue",fg="black")
        l2.place(x=30,y=150)
        user=Entry(f,font=('times',19,'bold'))
        user.place(x=230,y=50)
        passwd=Entry(f,font=('times',19,'bold'),show='*')
        passwd.place(x=230,y=150)
        reg=Button(f,text='Register',font=('times',19,'bold'),bg="alice blue",fg="black",command=s.register)
        reg.place(x=30,y=250)
        log=Button(f,text='Login',font=('times',19,'bold'),bg="alice blue",fg="black",command=lambda :s.login_main(user.get(),passwd.get()))
        log.place(x=400,y=250)
        s.content.extend([l,l0,f,l1,l2,user,passwd,reg,log])
        s.scr.mainloop()
    def login_main(s,user,passwd):
        if len(user)==0 or len(passwd)==0:
            messagebox.showerror('login','please enter a all fields required') 
        else:
            s.cur.execute('select count(*) from user where name=%r and password=%r'%(user,passwd))
            if s.cur.fetchone()[0]==0:
                messagebox.showerror('login page','Invalid credentials')
            else:
                #messagebox.showinfo('login page','login succesful')
                s.homepage()
    def register(s):
        if len(s.content)!=0:
            list(map(lambda i:i.destroy(),s.content))
        mx,my=s.scr.maxsize()
        s.scr.geometry('%dx%d'%(mx,my))
        s.img=ImageTk.PhotoImage(Image.open("bgimg2.jpg"))
        l=Label(s.scr,image=s.img)
        l.image=s.img
        l.pack()
        l0=Label(s.scr,text='Please fill the details & Signup....',font=('times',25,'bold','underline'))
        l0.place(x=(mx//2)-250,y=0)
        f=Frame(s.scr,bg='honeydew2',height=600,width=600)
        f.place(x=(mx//2)-450,y=(my//2)-300)
        l1=Label(f,text='Username : ',font=('times',20,'bold'),bg="sky blue",fg="black")
        l1.place(x=30,y=50)
        l2=Label(f,text='Password : ',font=('times',20,'bold'),bg="sky blue",fg="black")
        l2.place(x=30,y=130)
        l3=Label(f,text='Reenter : ',font=('times',20,'bold'),bg="sky blue",fg="black")
        l3.place(x=30,y=210)
        l4=Label(f,text='E-mail : ',font=('times',20,'bold'),bg="sky blue",fg="black")
        l4.place(x=30,y=290)
        l5=Label(f,text='Mobile : ',font=('times',20,'bold'),bg="sky blue",fg="black")
        l5.place(x=30,y=370)
        user=Entry(f,font=('times',19,'bold'))
        user.place(x=250,y=50)
        passwd=Entry(f,font=('times',19,'bold'),show='*')
        passwd.place(x=250,y=130)
        passwd1=Entry(f,font=('times',19,'bold'),show='*')
        passwd1.place(x=250,y=210)
        email=Entry(f,font=('times',19,'bold'))
        email.place(x=250,y=290)
        mobile=Entry(f,font=('times',19,'bold'))
        mobile.place(x=250,y=370)
        reg=Button(f,text='Login',font=('times',19,'bold'),bg="alice blue",fg="black",command=s.login)
        reg.place(x=30,y=450)
        log=Button(f,text='Signup',font=('times',19,'bold'),bg="alice blue",fg="black",command=lambda :s.register_main(user.get(),passwd.get(),passwd1.get(),email.get(),mobile.get()))
        log.place(x=400,y=450)
        s.content.extend([l,f,l1,l2,user,passwd,reg,log,l0,l3,l4,l5,passwd1,email,mobile])
        s.scr.mainloop()
    def register_main(s,u,p,p1,e,m):
        if len(u)==0 or len(p)==0 or len(p1)==0 or len(e)==0 or len(m)==0:
            messagebox.showerror('login','please enter a all fields required')
        elif p!=p1:
            messagebox.showerror('login','both password did not match')
        elif not(re.search(r'^\S+@\w+[.][a-z]{2,3}$',e)):
            messagebox.showerror('login','invalid email')
        elif not(re.search(r'^\d{10}$',m)):
            messagebox.showerror('login','invalid mobile')
        else:
            try:
                s.cur.execute('insert into user values(%r,%r,%r,%r)'%(u,p,e,m))
                s.db.commit()
                s.login()
            except Exception as ex:
                messagebox.showerror('login',ex)
    def homepage(s):
        if len(s.content)!=0:
            list(map(lambda i:i.destroy(),s.content))
        mx,my=s.scr.maxsize()
        s.scr.geometry('%dx%d'%(mx,my))
        s.img=ImageTk.PhotoImage(Image.open("bgimg3.jpeg"))
        l=Label(s.scr,image=s.img)
        l.image=s.img
        l.pack() 
        l0=Label(s.scr,text='Welcome! User....',font=('times',40,'bold','underline'),bg='black',fg='Cyan2')
        l0.place(x=(mx//2)-250,y=10)
        l2=Label(s.scr,text='...MEDICAL SCRAPPER...',font=('times',40,'bold','underline'),bg='black',fg='cyan2')
        l2.place(x=(mx//2)-330,y=80)
        l1=Label(s.scr,text='Type_keyword : ',font=('times',25,'bold'),bg="cyan2",fg="black")
        l1.place(x=700,y=250)
        keyword=Entry(s.scr,font=('times',25,'bold'))
        keyword.place(x=1000,y=250)
        search=Button(s.scr,text='Search',font=('times',19,'bold'),bg="cyan2",fg="black",activebackground="white",activeforeground="black",width=10,relief='sunken',
                      command=lambda :s.homepage_main(keyword.get()))
        search.place(x=1185,y=350)
        s.content.extend([l,l0,l1,l2,keyword,search])
        s.scr.mainloop()
    def homepage_main(s,k):
        if len(k)==0:
            messagebox.showerror('Search_error','please enter a search keyword')
        else:
            head={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
            data=rt.request('get','https://www.1mg.com/search/all?name={}'.format(k),headers=head)
            s_0=bs4.BeautifulSoup(data.text,'html.parser')
            s.detailpage(s_0)
    def detailpage(s,s_0):
        if len(s.content)!=0 or s.lst!=0 or s.lst2!=0:
            list(map(lambda i:i.destroy(),s.content))
            s.lst.clear()
            s.lst2.clear()
            
        org_path=os.getcwd()
        path=org_path+'\\newsearch'
        try:
            os.mkdir('newsearch')
        except:
            pass
        os.chdir(path)
        lst=[]
        name='img{}.png'
        j=0
        head={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        if s_0.find_all('div',{'class':'col-md-3 col-sm-4 col-xs-6 style__container___jkjS2'}):
            for i in s_0.find_all('div',{'class':'col-md-3 col-sm-4 col-xs-6 style__container___jkjS2'}):
                data_1=rt.request('get','https://www.1mg.com'+i.find('a').get("href"),headers=head)
                s_1=bs4.BeautifulSoup(data_1.text,'html.parser')
                try:
                    s.lst.append(s_1.find('div',{'class':'ProductDescription__product-description___1PfGf'}).text)
                    img_0=s_1.find('div',{'class':'col-xs-10 ProductImage__preview-container___2oTeX'})
                    img_src=img_0.find('img').get('src')
                    img=rt.request('get',img_src)#it will bring the image as binary data
                    open(name.format(j),'wb').write(img.content)#img.content will give the binary content of file
                    j+=1
                except:
                    pass
            os.chdir(org_path)
        else:
            for i in s_0.find_all('div',{'class':'col-xs-12 col-md-9 col-sm-9 style__container___cTDz0'}):
                data_1=rt.request('get','https://www.1mg.com'+i.find('a').get("href"),headers=head)
                s_1=bs4.BeautifulSoup(data_1.text,'html.parser')
                try:
                    s.lst.append(s_1.find('div',{'class':'DrugPane__content___3-yrB'}).text)
                    img_0=s_1.find('div',{'class':''})
                    img_src=img_0.find('img').get('src')
                    img=rt.request('get',img_src)#it will bring the image as binary data
                    open(name.format(j),'wb').write(img.content)#img.content will give the binary content of file
                    j+=1
                except:
                    pass
            os.chdir(org_path)
        s.details()
    def details(s): 
        if len(s.content)!=0:
            list(map(lambda i:i.destroy(),s.content))
        #print(s.lst) 
        for i in range(len(s.lst)):
            s.lst2.append(i)
        s.lst3=iter(s.lst2[1:])
        mx,my=s.scr.maxsize()
        s.scr.geometry('%dx%d'%(mx,my))
        s.img=ImageTk.PhotoImage(Image.open("bgimg4.jpg"))
        l=Label(s.scr,image=s.img)
        l.image=s.img
        l.pack() 
        l0=Label(s.scr,text='Your medicine details...',font=('times',40,'bold','underline'),bg='black',fg='Cyan2')
        l0.place(x=(mx//2)-250,y=10)
        imginfo=Label(s.scr,text='Medicine Image:-',font=('times',20,'bold'),width=15,bg='black',fg='cyan2')
        imginfo.place(x=10,y=300)
        detail=Label(s.scr,text='Description:-',font=('times',20,'bold'),width=15,bg='black',fg='cyan2')
        detail.place(x=900,y=100)
        next_btn=Button(s.scr,text='NEXT->',activebackground="white",activeforeground="black",bg="cyan2",fg="black",width=20,command=s.showdetails(0) or s.nxt)
        next_btn.place(x=10,y=150)
        back_btn=Button(s.scr,text='back to homepage',activebackground="white",activeforeground="black",bg="cyan2",fg="black",width=20,command=s.homepage)
        back_btn.place(x=10,y=200)
        s.content.extend([l,l0,imginfo,detail,next_btn,back_btn])
        s.scr.mainloop() 
    def nxt(s):
        k=next(s.lst3)
        s.showdetails(k)
    def showdetails(s,k):
        if len(s.content)==2:
            list(map(lambda i:i.destroy(),s.content))
        try:
            img=ImageTk.PhotoImage(Image.open('newsearch/img{}.png'.format(k)).resize((400,400),Image.ANTIALIAS))
            b=Label(s.scr,image=img)
            b.image=img#if pyimage does not error show
            b.place(x=150,y=350)
        except:
            img=ImageTk.PhotoImage(Image.open('newsearch1/Screenshot 2020-10-05 004718.png').resize((400,400),Image.ANTIALIAS))
            b=Label(s.scr,image=img)
            b.image=img#if pyimage does not error show
            b.place(x=150,y=350)
            pass
        d=Message(s.scr,bg='white',text=s.lst[k],width=900)
        d.place(x=600,y=150)
        s.content.extend([b,d])
    def __del__(s):
        del(s.db)

Gui()  


# In[ ]:




