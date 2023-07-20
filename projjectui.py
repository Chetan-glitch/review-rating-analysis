import tkinter as t
import projectui2 as p2
import projectui3 as p3

win=t.Tk()
win.geometry('600x700')
win.title('Project Name')
win.resizable(False,False)
def checkreview():
        p2.load()
def typereview():
        p3.load()
        
###########frames Design done###################
top=t.Frame(win,width=600,height=200,bd=2,relief='raise',pady=4)
top.pack(side='top')
middle=t.Frame(win,width=600,height=250,bd=2,relief='raise',pady=35)
middle.pack(side='top')
bottom=t.Frame(win,width=600,height=250,bd=2,relief='raise',pady=25,padx=2)
bottom.pack(side='bottom')
#############top Frame Design#####################
l1=t.Label(top,text='Project Name',font=('arial',20,'bold'),pady=10)
l1.pack(side='top')
con1='''This Application basically help the user to check the revies given by
any user on the websites or application is said to be bad or good
and it also gives a option to check the type of review that this
review basically belongs to which type we basically focus on
movie hotels and email data So Hurry Up and use it'''
l2=t.Label(top,text=con1,font=('arial',14),padx=15,justify='left',pady=12)
l2.pack(side='top')
############middle frame design#######################
l3=t.Label(middle,text='Check The Review',font=('arial',20,'bold'),pady=12)
l3.pack(side='top')
con1='''  This section basically focus on the sentiment of the user acccording
  to the given feedback to use it please click on the given button '''
l4=t.Label(middle,text=con1,font=('arial',14),padx=20,justify='left',pady=12)
l4.pack(side='top')
b1=t.Button(middle,text='Check Review',font=('arial',16,'bold'),bg='powderblue',fg='red',command=checkreview)
b1.pack(side='top')
############bottom frame design#######################
l3=t.Label(bottom,text='Check Review Type',font=('arial',20,'bold'),pady=12)
l3.pack(side='top')
con1='''  This section basically focus on the type of review like which
  area this review is given like hotel movie or email to use it please
  click on the given button '''
l4=t.Label(bottom,text=con1,font=('arial',14),padx=20,justify='left',pady=12)
l4.pack(side='top')
b1=t.Button(bottom,text='Check Review Type',font=('arial',16,'bold'),bg='powderblue',fg='red',command=typereview)
b1.pack(side='top')












