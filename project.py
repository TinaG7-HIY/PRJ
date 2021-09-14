from tkinter import *
import sqlite3
import tkinter.font as tkFont



win = Tk()
win.title('School')
win.geometry('300x200')
win.configure(bg='#00BFFF')

              

myFont = tkFont.Font(family="Times New Roman" , size=11)




conn = sqlite3.connect('school.db')


c = conn.cursor()


#c.execute(''' CREATE TABLE SCHOOL
#(FirstName TEXT NOT NULL,
#LastName TEXT NOT NULL,
#City TEXT NOT NULL,
#Code INT NOT NULL,
#Score REALL NOT NULL,
#Address TEXT NOT NULL,
#Phone TEXT NOT NULL)''')

#=============================================================================================    

def Submit_page():
    
    
    def Submit():
        conn = sqlite3.connect('school.db')
        c = conn.cursor()
        
        f = f_name.get()
        l = l_name.get()
        ct = city.get()
        cd = code.get()
        s = score.get()
        a = address.get()
        p = phone.get()
        
        if (len(f) == 0) or (len(l) == 0) or (len(ct) == 0) or (len(cd) == 0) or (len(s) == 0) or (len(a) == 0) or (len(p) == 0) :
            error_label.configure(text="Fill All Boxes" , fg = 'red')
            return
        
        
        
        c.execute("INSERT INTO SCHOOL VALUES (:f_name, :l_name, :city, :code, :score, :address, :phone)",
                  {'f_name':f, 'l_name':l, 'city':ct, 'code':cd, 'score':s, 'address':a, 'phone':p } )
        
        error_label.configure(text = "Welcome:))" , fg = 'green')
        
        conn.commit()
        conn.close()
        
        
        #clear Text Boxes
        f_name.delete(0,100)
        l_name.delete(0,100)
        city.delete(0,100)
        code.delete(0,100)
        score.delete(0,100)
        address.delete(0,100)
        phone.delete(0,100)
        
        
        
        
    sbm = Tk()
    sbm.title('Submit')
    sbm.geometry('300x250')
    sbm.configure(bg='#00BFFF')
    
                  
    
    
    #Text Boxes
    f_name = Entry(sbm, width = 30)
    f_name.grid(row=0 , column=1 , padx=20)
    l_name = Entry(sbm, width = 30)
    l_name.grid(row=1 , column=1 )
    city = Entry(sbm, width = 30)
    city.grid(row=2 , column=1 )
    code = Entry(sbm, width = 30)
    code.grid(row=3 , column=1 )
    score = Entry(sbm, width = 30)
    score.grid(row=4 , column=1 )
    address = Entry(sbm, width = 30)
    address.grid(row=5 , column=1 )
    phone = Entry(sbm, width=30)
    phone.grid(row=6 , column=1)
    
    
    
    #Text Box Labels
    f_name_label = Label(sbm, text="First Name", bg='#00BFFF' , fg='#000080', font = myFont)
    f_name_label.grid(row=0 , column=0)    
    l_name_label = Label(sbm, text="Last name", bg='#00BFFF' , fg='#000080', font = myFont)
    l_name_label.grid(row=1 , column=0)    
    city_label = Label(sbm, text="City", bg='#00BFFF' , fg='#000080', font = myFont)
    city_label.grid(row=2 , column=0)    
    code_label = Label(sbm, text="Code", bg='#00BFFF' , fg='#000080', font = myFont)
    code_label.grid(row=3 , column=0) 
    score_label = Label(sbm, text="Score", bg='#00BFFF' , fg='#000080', font = myFont)
    score_label.grid(row=4 , column=0)
    address_label = Label(sbm, text="Address", bg='#00BFFF' , fg='#000080', font = myFont)
    address_label.grid(row=5 , column=0)
    phone_label = Label(sbm, text="Phone", bg='#00BFFF' , fg='#000080', font = myFont)
    phone_label.grid(row=6 , column=0)
    
    #Submit Button
    submit_btn = Button(sbm, text="Submit" , command= Submit, bg='#1874CD', fg ='white', font=myFont )
    submit_btn.grid(row=7, column=1 , padx=10, pady=10 , ipadx=70)
    
    error_label = Label(sbm, text ="", bg='#00BFFF' , fg='#000080', font = myFont)
    error_label.grid(row=8 , column=1)
    
    
    
#=============================================================================================    
    
def save():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    
    record_id = id_box.get()
    
    c.execute("""UPDATE SCHOOL SET
        FirstName = :first,
        LastName = :last,
        City = :city,
        Code = :code,
        Score = :score,
        Address = :address,
        Phone = :phone
        
        WHERE oid = :oid""",
        {'first': f_name_edit.get(),
         'last': l_name_edit.get(),
         'city': city_edit.get(),
         'code': code_edit.get(),
         'score': score_edit.get(),
         'address': address_edit.get(),
         'phone' : phone_edit.get(),
         'oid': record_id 
         })
    
    
    save_message.configure(text='saved successfully!' , fg='green')
    
    conn.commit()
    conn.close()
    
    
    
    
    
#=============================================================================================        
def Edit_page():
  
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    
    student_id = id_box.get()
    
    
    c.execute("SELECT * FROM SCHOOL WHERE oid = " + student_id)
    records = c.fetchall()
    
    

        
    conn.commit()
    conn.close()
    
    
    edt = Tk()
    edt.title('Edit')
    edt.geometry('300x250')
    edt.configure(bg='#00BFFF')
    
    global f_name_edit
    global l_name_edit
    global city_edit
    global code_edit
    global score_edit
    global address_edit
    global phone_edit
    
    global save_message
    
    
     #Text Boxes
    f_name_edit = Entry(edt, width = 30)
    f_name_edit.grid(row=2 , column=1 , padx=20)
    l_name_edit = Entry(edt, width = 30)
    l_name_edit.grid(row=3 , column=1 )
    city_edit = Entry(edt, width = 30)
    city_edit.grid(row=4 , column=1 )
    code_edit = Entry(edt, width = 30)
    code_edit.grid(row=5 , column=1 )
    score_edit = Entry(edt, width = 30)
    score_edit.grid(row=6 , column=1 )
    address_edit = Entry(edt, width = 30)
    address_edit.grid(row=7 , column=1 )
    phone_edit = Entry(edt, width = 30)
    phone_edit.grid(row=8 , column=1 )
    
    #Text Box Labels
    f_name_label = Label(edt, text="First Name", bg='#00BFFF', fg='#000080', font = myFont)
    f_name_label.grid(row=2 , column=0)    
    l_name_label = Label(edt, text="Last name", bg='#00BFFF', fg='#000080', font = myFont)
    l_name_label.grid(row=3 , column=0)    
    city_label = Label(edt, text="City", bg='#00BFFF', fg='#000080', font = myFont)
    city_label.grid(row=4 , column=0)    
    code_label = Label(edt, text="Code", bg='#00BFFF', fg='#000080', font = myFont)
    code_label.grid(row=5 , column=0) 
    score_label = Label(edt, text="Score", bg='#00BFFF', fg='#000080', font = myFont)
    score_label.grid(row=6 , column=0)
    address_label = Label(edt, text="Address", bg='#00BFFF', fg='#000080', font = myFont)
    address_label.grid(row=7 , column=0)
    phone_label = Label(edt, text="Phone number", bg='#00BFFF', fg='#000080', font = myFont)
    phone_label.grid(row=8 , column=0)
    
    for i in records:
        f_name_edit.insert(0,i[0])
        l_name_edit.insert(0,i[1])
        city_edit.insert(0,i[2])
        code_edit.insert(0,i[3])
        score_edit.insert(0,i[4])
        address_edit.insert(0,i[5])
        phone_edit.insert(0,i[6])
        
    
   
    
    save_Button = Button(edt, text="Save" , command=save, bg='#1874CD', fg ='white', font=myFont)
    save_Button.grid(row=9, column=1 , padx=10, pady=10 )
    

    save_message = Label(edt, text="", bg='#00BFFF', fg ='white', font=myFont)
    save_message.grid(row=10, column=1)
    
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    
    
    
    
    
    
    
    conn.commit()
    conn.close()
    
    
    
#=============================================================================================    
def Report_page():
    rpt = Tk()
    rpt.title('Report')
    rpt.geometry('350x200')
    rpt.configure(bg='#00BFFF')
    
    def score_report():
        
        conn = sqlite3.connect('school.db')
        c = conn.cursor()
        
        
        sb = score_box.get()
         
        c.execute("SELECT First, Last,Score FROM SCHOOL")
         
        name = c.fetchall()
        final =''
        for i in name:
            if i[2]>= float(sb):
                final += i[0] + " " + i[1] + ": " + str(i[2]) + "\n"
        main_label.configure(text = final)
        print(final)
        
        
    
    def city_report():
        
        conn = sqlite3.connect('school.db')
        c = conn.cursor()
        
        cy = city_box.get()
        
        c.execute("SELECT First, Last,City FROM SCHOOL")
        
        name = c.fetchall()
        
        final =''
        for i in name:
            if i[2]== cy:
                 final += i[0] + " " + i[1] + "\n"
                
        main_label.configure(text = final)
        print(final)
        
        conn.close()
        
   
    global main_label
#    Labels
    score_label = Label(rpt , text='Enter the score ', bg='#00BFFF', fg='#000080', font = myFont)
    score_label.grid(row=0 , column=0)    
    score_box = Entry(rpt, width = 20)
    score_box.grid(row=0 , column=1)
    
    city_report_label = Label(rpt, text='Enter the City', bg='#00BFFF', fg='#000080', font = myFont )
    city_report_label.grid(row=1 , column=0)
    city_box = Entry(rpt, width= 20)
    city_box.grid(row=1, column=1)
    
    
    main_label = Label(rpt, text=' ', bg='#00BFFF', fg='#000080', font = myFont)
    main_label.grid(row=2 , column=1)
    
#    Buttons
    score_btn = Button(rpt, text ='Search' , command= score_report, bg='#1874CD', fg ='white', font=myFont)
    score_btn.grid(row=0 , column=2)
    city_btn = Button(rpt, text='search' , command= city_report, bg='#1874CD', fg ='white', font=myFont)
    city_btn.grid(row=1 , column=2)
    
    
    
    
    
#=============================================================================================    
def Search_page():
    srch = Tk()
    srch.title('Search')
    srch.geometry('300x200')
    srch.configure(bg='#00BFFF')
    
    def code_search():
        conn = sqlite3.connect('school.db')
        c = conn.cursor()
        
        cb = code_box.get()
        
        c.execute("SELECT * FROM SCHOOL")
        
        name = c.fetchall()
        
        final =''
        for i in name:
            if i[3]== int(cb):
                 final += i[0] + " " + i[1] + "\n" + i[2] + "\n" + str(i[3]) + "\n" + str(i[4]) + "\n" + i[5] + "\n" + i[6]
                
        main_label.configure(text = final)
        print(final)
        
        conn.close()
        
    global  main_label 
    
    code_label = Label(srch , text='Enter the code ', bg='#00BFFF', fg='#000080', font = myFont)
    code_label.grid(row=0 , column=0)   
    
    code_box = Entry(srch, width = 20)
    code_box.grid(row=0 , column=1)
    
    code_btn = Button(srch, text ='Search' , command= code_search, bg='#1874CD', fg ='white', font=myFont)
    code_btn.grid(row=0 , column=2)
    
    main_label = Label(srch, text=' ', bg='#00BFFF', fg='#000080', font = myFont)
    main_label.grid(row=1 , column=1)
    
    
    
    
    
    
    
    
    
    
    
 #=============================================================================================    



btn_submit = Button(win, text = 'Submit' , command= Submit_page , bg='#1874CD', fg ='white', font=myFont)
btn_submit.grid(row =0, column = 1)
btn_edit = Button(win, text = 'Search ID' , command= Edit_page, bg='#1874CD', fg ='white', font=myFont)
btn_edit.grid(row =5, column = 1 , padx=5)
btn_report = Button(win, text = 'Report' , command= Report_page, bg='#1874CD', fg ='white', font=myFont)
btn_report.grid(row =2, column = 1, ipadx=1)
btn_search = Button(win, text = 'Search' , command= Search_page, bg='#1874CD', fg ='white', font=myFont)
btn_search.grid(row =3, column = 1)

id_box = Entry(win, width = 10)
id_box.grid(row=4 , column=1)


submit_label = Label(win, text="Click to submit :", bg='#00BFFF', fg='#000080', font = myFont)
submit_label.grid(row=0 , column=0)
id_label = Label(win, text="Enter ID to edit profile :", bg='#00BFFF' , fg='#000080', font = myFont)
id_label.grid(row=4 , column=0)    
report_label = Label(win, text="Click to see reports :", bg='#00BFFF' , fg='#000080', font = myFont)
report_label.grid(row=2 , column=0)
search_label = Label(win, text="Click to search :", bg='#00BFFF' , fg='#000080', font = myFont)
search_label.grid(row=3 , column=0)





#conn.commit()

conn.close()
win.mainloop()