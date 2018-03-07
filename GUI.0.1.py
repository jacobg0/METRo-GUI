
from Tkinter import *
import os
import webbrowser
import tkFileDialog, Tkconstants, Tkinter

from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile

root = Tk()
root.title("METRo")



class Application(Frame):
    # declaring global variables
    global code0
    global code
    global code1
    global code2
    global code3
    code0 = ""
    code = ""
    code1 = ""
    code2 = ""
    code3 = ""



    global Metro_wiki
    Metro_wiki = 'https://framagit.org/metroprojects/metro/wikis/METRo'


    # defining classes
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_label()
        self.btn_forecast()
        self.btn_station()
        self.btn_observation()
        self.btn_roadcast()
        self.create_widget()
        self.run_metro()
        self.Metro_def()
        self.Explination()
        self.Explain_code()
        self.result()
        self.btn_clear()

    # Label for text, background color(bg), font color, font style and size, heigth and width of the label


    def create_label(self):
        self.label = Label(self, text="Welcome to METRo", fg="black", font=(None, 18), height=2, width=0)
        self.label.grid(row =0,column=2)

    def Metro_def(self):
        self.label = Label(self,
                           text="METRo stands for Model of the Environment and Temperature of Roads which is able to predict the road conditions", fg="black", font=(None, 10))
        self.label.grid(row=1, column=0, columnspan=5)

    def Explination(self):
        self.label = Label(self,
                           text=" Use the following buttons to import your data and select a proper output file destination",
                           fg="black", font=(None, 10))
        self.label.grid(row=2, column=0, columnspan=5)

    def Explain_code(self):
        self.label = Label(self,
                           text="Additonally the box below will display the code that will executed",
                           fg="black", font=(None, 10))
        self.label.grid(row=7, column=0, columnspan=5)



    # define all of the possible input buttons
    def btn_forecast(self):
        self.button = Button(root, text="Forecast", command=self.forecast, justify='center')
        self.button.grid(row=2, column=0, padx =10,sticky = W)


    def btn_station(self):
        self.button = Button(root, text="Station", command=self.station)
        self.button.grid(row=2, column=0, padx = 10)

    def btn_observation(self):
        self.button = Button(root, text="Observation", command=self.observation)
        self.button.grid(row=2, column=0, padx =10,sticky = E)

    def btn_roadcast(self):
        self.button = Button(root, text="Roadcast", command=self.roadcast)
        self.button.grid(row=3, column=0, padx = 10, sticky =  W )


    def btn_clear(self):
        self.button = Button(root, text = "Clear", command = self.clear)
        self.button.grid(row=3, column=0, padx = 10, sticky =  E )


    # defines the forecast button
    def forecast(self):
        global code
        global code0

        code0 = "python metro"


        code += " --input-forecast "
        forecast = tkFileDialog.askopenfilename(filetypes=(("All files", "*.*"), ("XML", "*.xml")))
        code += forecast

        self.result.delete(0.0, END)
        self.result.insert(0.0,code0+ code)


        # box where metro code is displayed
    def result(self):

        self.result = Text(self, width=80, height=10, wrap=WORD)
        self.result.grid(row= 20, column=2)

    # defines the station button
    def station(self):
        global code1
        # global stat

        code1 += " --input-station "
        stat = tkFileDialog.askopenfilename(filetypes=(("All files", "*.*"), ("XML", "*.xml")))
        code1 += stat

        self.result.delete(0.0, END)
        self.result.insert(0.0, code0+code+code1)

    # defines the observation button
    def observation(self):
        global code2

        code2 += " --input-observation "
        observation = tkFileDialog.askopenfilename(filetypes=(("All files", "*.*"), ("XML", "*.xml")))
        code2 += observation

        self.result.delete(0.0, END)
        self.result.insert(0.0, code0+code+code1+code2)

    # defines the roadcast button
    def roadcast(self):
        global code3

        code3 += " --output-roadcast "
        roadcast = tkFileDialog.askopenfilename(filetypes=(("All files", "*.*"), ("XML", "*.xml")))
        code3 += roadcast

        self.result.delete(0.0, END)
        self.result.insert(0.0, code0+code+code1+code2+code3)

    # defines the run Metro button
    def create_widget(self):
        self.button = Button(root, text="Run Metro", command=self.run_metro)
        self.button.grid(row=3, column=0, pady=10)

    # defines what run button actually does
    def run_metro(self):
        global code0
        global code
        global code1
        global code2
        global code3
        global observation

        # os.system(fore)
        print(code0+code+code1+code2+code3)
        os.system(code0+code+code1+code2+code3)

    def clear(self):
        global code0
        global code
        global code1
        global code2
        global code3

       # del code
      #  code = False
       # code = None

        code0 =""
        code=""
        code1 =""
        code2=""
        code3=""

        self.result.delete(0.0, 'end')


        #command = root.quit()

        #os.system('python GUI.0.py')




# Defining a top bar menu
def NewFile():
    print ""


def OpenFile():
    name = askopenfilename()
    print name


def About():
    webbrowser.open(Metro_wiki, 2)
    print "You are being redirected to the Metro Wiki"





    def forecast_conversion(self):
        forecast_conversion = tkFileDialog.askopenfilename(filetypes=(("All files", "*.*"), ("XML", "*.xml")))
        forecast_conversion = fore_csy.py

    def btn_observation(self):
        self.button = Button(root, text="Observation", command=self.observation)
        self.button.grid(row=2, column=0, padx =10,sticky = E)




# Defining a file menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)


filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Defining a help Menu
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Metro Wiki", command=About)

#root.geometry("410x500")


app = Application(root)

root.mainloop()

