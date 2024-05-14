# Title :- Digital News Paper GUI
# Description :- A digital news paper GUI (Graphical User Interface) in Python is a software application that provides a graphical interface for users to access and view news articles and information. It shows user to display top 20 news of the present day.The GUI for the digital news paper can be created using Tkinter. The layout and design of the digital news paper can be customized to meet the specific needs and preferences of the users. In this project the news data can be fetched from news API.

import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image

class Newsapp:
    def __init__(self):
        '''
        This is the constructor of a Newsapp class
        '''

        #fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=f40d442ab1f24355b560565239df4c89').json()

        #initial GUI load
        self.load_gui()

        #load the 1st news item
        self.load_news(0)

    def load_gui(self):
        '''
        This method is used to set the GUI size and display into the screen
        '''

        self.root=Tk()
        self.root.title('News Application')
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.config(bg='black')

    def clear(self):
        '''
        This method is used to clear the screen
        '''

        for i in self.root.pack_slaves():
            i.destroy()

    def open_link(self,url):
        '''
        This method is used to redirect on show the detailed information of the news.
        '''

        webbrowser.open(url)

    def load_news(self,index):
        '''
        This method is load the news on GUI from the API
        '''

        # clear the screen for next news
        self.clear()

        # image place
        try:
            img_url = self.data['articles'][index]['urlToImage']
            img_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(img_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

        # if image is not place then the default image has been see in the gui window
        except:
            img_url = 'https://bitsofco.de/content/images/2018/12/Screenshot-2018-12-16-at-21.06.29.png'
            img_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(img_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root,image=photo)
        label.pack()

        headling = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='center')
        headling.config(font=('verdana',15))
        headling.pack(pady=10)

        detail = Label(self.root,text=self.data['articles'][index]['description'],bg='black',fg='white',wraplength=350,justify='center')
        detail.config(font=('verdana',12))
        detail.pack(pady=3)

        frame= Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        if index!=0:
            prev = Button(frame,text='Prev',width=16,height=3,command=lambda :self.load_news(index-1))
            prev.pack(side=LEFT)

        more = Button(frame,text='More Detail',width=16,height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
        more.pack(side=LEFT)

        if index!=len(self.data['articles'])-1:
            next = Button(frame,text='Next',width=16,height=3,command=lambda :self.load_news(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()

obj = Newsapp()
