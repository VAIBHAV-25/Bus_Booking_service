from tkinter import *
import sqlite3 
from PIL import Image,ImageTk
from tkinter import messagebox

conn = sqlite3.connect("Bus_info.db")

c = conn.cursor()

c.execute("""CREATE TABLE if not exists Buses(id integer ,
    Travels_full_name text,
    Contact_no integer,
    Address text,
    Operator text,
    Bus_type text,
    from_starting_point text,
    to_destination text,
    date text,
    dept_time text,
    arr_time text,
    fare integer,
    seats integer,PRIMARY KEY (id AUTOINCREMENT)
)""")

conn.commit()

conn.close()


globl_list = []

def bus_main_screen():


    def search_bus():

        def search(bus_type_selection,frm,destination,date):

            root2.destroy()
            root3= Tk()


            Label(root3,text="BUS BOOKING SERVICE",font= 100,bg="Black",fg="yellow",border=10).grid(row=0,column =5,columnspan=3)

            img1 = Image.open('bus3.png')
            re_img1 = img1.resize((616,402))
            ph = ImageTk.PhotoImage(re_img1)
            Label(root3,image = ph).grid(row=1,column=2,columnspan=8)

            def details_displaced_after_searched():
                Label(root3,text="BUS Details",font= 100,bg="Black",fg="white",border=10).grid(row=2,column = 6,columnspan=2)

                Label(root3,text="S_NO",font=3).grid(row=3,column=1)

                Label(root3,text="Travels Name",font=3).grid(row=3,column=1)

                Label(root3,text="Type",font=3).grid(row=3,column=2)

                Label(root3,text="From",font=3).grid(row=3,column=3)

                Label(root3,text="To",font=3).grid(row=3,column=4)

                Label(root3,text="Date",font=3).grid(row=3,column=5)

                Label(root3,text="Dept Time",font=3).grid(row=3,column=6)

                Label(root3,text="Arr Time",font=3).grid(row=3,column=7)

                Label(root3,text="Fare",font=3).grid(row=3,column=8)

                Label(root3,text="Seats Availability",font=3).grid(row=3,column=9)



            details_displaced_after_searched()

            Label(root3,text="Select",font=3).grid(row=3,column=10)


            var_select = IntVar()

            conn = sqlite3.connect("Bus_info.db")

            c = conn.cursor()

            bus_details_list_searched={}

            if(bus_type_selection.get()=='All Types'):
                s = c.execute("SELECT id,Travels_full_name,Bus_type,from_starting_point,to_destination,date,dept_time,arr_time,fare,seats from Buses WHERE date=:d and from_starting_point=:f and to_destination=:t",{'d':date,'f':frm,'t':destination})
                r = 4
                c = 0
                v = 1
                for i in s:
                    c=0
                    bus_details_list_searched.update({v:i})
                    for j in range(0,len(i)):
                        Label(root3,text=i[j]).grid(row = r,column=c)
                        c=c+1
                    Radiobutton(root3,variable=var_select,value=v).grid(row=r,column=c)
                    r = r+1
                    v = v + 1

            else:
                s = c.execute("SELECT id,Travels_full_name,Bus_type,from_starting_point,to_destination,date,dept_time,arr_time,fare,seats from Buses WHERE  date=:d and from_starting_point=:f and to_destination=:t and Bus_type=:b",{'d':date,'f':frm,'t':destination,'b':bus_type_selection.get()})
                r = 4
                c = 0
                v = 1
                for i in s:
                    c=0
                    bus_details_list_searched.update({v:i})
                    for j in range(0,len(i)):
                        Label(root3,text=i[j]).grid(row = r,column=c)
                        c=c+1
                        Radiobutton(root3,variable=var_select,value=v).grid(row=r,column=c)
                    r = r+1
                    v = v + 1


            def selected_bus_proceed():
                root3.destroy()
                root4 = Tk()
                Label(root4,text="BUS Details",font= 100,bg="Black",fg="white",border=10).grid(row=2,column = 2,columnspan=2)

                Label(root4,text="Travels Name",font=3).grid(row=3,column=0)

                Label(root4,text="Type",font=3).grid(row=3,column=1)

                Label(root4,text="From",font=3).grid(row=3,column=2)

                Label(root4,text="To",font=3).grid(row=3,column=3)

                Label(root4,text="Date",font=3).grid(row=3,column=4)

                Label(root4,text="Dept Time",font=3).grid(row=3,column=5)

                Label(root4,text="Arr Time",font=3).grid(row=3,column=6)

                Label(root4,text="Fare",font=3).grid(row=3,column=7)

                Label(root4,text="Seats Availability",font=3).grid(row=3,column=8)

                Label(root4,text="").grid(row=4,column =0)


                r=5
                c=0

                bdls = bus_details_list_searched[var_select.get()]
                ''' print(bdls)'''
                ids = bdls[0]
                '''print(ids)'''
                f=bdls[3]
                t=bdls[4]
                d=bdls[5]
                no_of_seats = bdls[-1]
                for i in bdls:
                    if(i==ids):
                        continue
                    Label(root4,text=i).grid(row = r,column=c)
                    c = c+1


                '''print(d)
                print(t)
                print(f)
                print(no_of_seats)'''
                dic ={}
                def make_dict_seats(no_of_seats):
                    for i in range(1,no_of_seats+1):
                        dic.update({i:"Null"})

                v1 = IntVar()
                count=1
                c=0
                r=50
                '''def count_no_seats():
                    n_seats = 0
                    for i in dic.values():
                        if(i!="Null"):
                            n_seats = n_seats + 1
                    return n_seats'''

                for i in range(no_of_seats):
                    Checkbutton(root4,variable = dic.update({count:count}),onvalue=count).grid(row=r,column=c)
                    c=c+1
                    if(c%10==0):
                        r=r+1
                        c=0

                def calling_global3():
                    root4.destroy()
                    bus_main_screen()



                make_dict_seats(no_of_seats)
                n = IntVar()
                Label(root4,text="Enter number of seats you have selected").grid(row=68,column=0)
                n = Entry(root4)
                n.grid(row=69,column=0)
                Button(root4,text="Home",border=2,command=calling_global3).grid(row=70,column=0)





                def update_seats_number(n_seats,d,t,f,ids):
                    conn = sqlite3.connect("Bus_info.db")
                    c= conn.cursor()

                    c.execute("UPDATE Buses SET seats='{}' WHERE (id ='{}'and date='{}' and from_starting_point='{}' and to_destination='{}');".format(n_seats,ids,d,f,t))

                    conn.commit()
                    conn.close()
                    Label(root4,text="Ticket Booked successfully").grid(row=75,column=5)
                    n.delete(0,END)

                    


                Button(root4,text="Book",border=2,command=lambda:update_seats_number((no_of_seats-int(n.get())),d,t,f,ids)).grid(row=70,column=8)

                root4.mainloop()



            conn.commit()

            conn.close()

            Button(root3,text="Select Book",font=3,command=selected_bus_proceed).grid(row=49,column=10)
            def calling_global2():
                root3.destroy()
                bus_main_screen()


            Button(root3,text="Home",border=2,command=calling_global2).grid(row=49,column=0)

            root3.mainloop()


        root.destroy()

        root2 = Tk()

        root2.title("Booking Service")

        Label(root2,text="BUS BOOKING SERVICE",font= 100,bg="Black",fg="white",border=10).grid(row=0,column =2)
    
        img = Image.open("bus4.png")
        x = 2
        y = 2
        re_img = img.resize((634//x,500//y))
        img = ImageTk.PhotoImage(re_img)
        Label(image = img).grid(row=1,column=2)

        Label(root2,text="Listing Buses",font=50).grid(row=2,column=2)

        bus_type_selection = StringVar()
        bus_type_selection.set("Bus Type")
        Label(root2,text="Bus Type: ").grid(row=3,column=1)
        bustype = ['AC','Non-AC','AC Sleeper','Non-Sleeper AC','All Types']
        OptionMenu(root2,bus_type_selection,*bustype).grid(row=3,column=3)


        Label(root2,text="From: ").grid(row=4,column=1)
        frm=""
        frm = Entry(root2)
        frm.grid(row=4,column=3)


        Label(root2,text="To: ").grid(row=5,column=1)
        destination=""
        destination= Entry(root2)
        destination.grid(row=5,column=3)


        Label(root2,text="Date(dd/mm/yyyy): ").grid(row=6,column=1)
        date=""
        date = Entry(root2)
        date.grid(row=6,column=3)

        def ms():
                messagebox.showwarning("warning","From and destination are equal")

        def ms1():
                messagebox.showwarning("warning","Wrong Date Format")

        def check_information():
            date_string = date.get()
            if(frm.get()==destination.get()):
                ms()
            elif((int(date_string[0])>=0 and int(date_string[0])<=2) and (int(date_string[1])>=0 and int(date_string[1])<=9) and  date_string[2]=='/' and ((int(date_string[3])==0 and (int(date_string[4])>=1 and int(date_string[4])<=9)) or (int(date_string[3])==1 and (int(date_string[4])>=0 and int(date_string[4])<=2))) and date_string[5]=='/' and int(date_string[6:10])>=1000 and int(date_string[6:10])<=9999):
                search(bus_type_selection,frm.get(),destination.get(),date.get())
            else:
                ms1()


        Button(root2,text="Search",border=2,command=check_information).grid(row=7,column=3)

        def calling_global1():
            root2.destroy()
            bus_main_screen()


        Button(root2,text="Home",border=2,command=calling_global1).grid(row=7,column=1)
        root2.mainloop()



    def add_bus():

        root.destroy()
        root1 = Tk()

        Label(root1,text="BUS BOOKING SERVICE",font= 100,bg="Black",fg="white",border=10).grid(row=0,column =2)
        img = Image.open("bus1.png")
        x = 2
        y = 2
        re_img = img.resize((634//x,500//y))
        img = ImageTk.PhotoImage(re_img)
        Label(image = img).grid(row=1,column=2)

        Label(root1,text="Bus Operator Details Filling").grid(row=2,column=2)

        Label(root1,text=" Travels Full Name: ").grid(row=3,column=1)
        travelsfullname=""
        travelsfullname = Entry(root1)
        travelsfullname.grid(row=3,column=3)


        Label(root1,text="Contact No: ").grid(row=4,column=1)
        contactno=0
        contactno = Entry(root1)
        contactno.grid(row=4,column=3)


        Label(root1,text="Address: ").grid(row=5,column=1)
        address=""
        address = Entry(root1)
        address.grid(row=5,column=3)


        def add_details():

            def entry_details_in_database():

                conn = sqlite3.connect('Bus_info.db')
                c = conn.cursor()

                c.execute("INSERT INTO Buses( Travels_full_name,Contact_no , Address ,Operator ,Bus_type ,from_starting_point ,to_destination ,date ,dept_time ,arr_time , fare , seats ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(travelsfullname.get(),contactno.get(),address.get(),operator.get(),bustype.get(),frm.get(),destination.get(),date.get(), depttime.get(),arrtime.get(),fare.get(),seats.get()))


                conn.commit()
                conn.close()

                travelsfullname.delete(0,END)
                contactno.delete(0,END)
                address.delete(0,END)
                operator.delete(0,END)
                bustype.delete(0,END)
                frm.delete(0,END)
                destination.delete(0,END)
                date.delete(0,END)
                depttime.delete(0,END)
                arrtime.delete(0,END)
                fare.delete(0,END)
                seats.delete(0,END)

                '''root10 = Tk()
                Label(root10,text="Added Successfully").grid(row=17,column = 3)
                def exit_after():
                    root10.destroy()
                Button(root10,text="Exit",command=exit_after).grid(row=19,column=3)
                root10.mainloop()'''

                root1.destroy()

                bus_main_screen()




            Label(root1,text="Operator: ").grid(row=7,column=1)
            operator=""
            operator = Entry(root1)
            operator.grid(row=7,column=3)


            Label(root1,text="Bus Type: ").grid(row=8,column=1)
            bustype=""
            bustype = Entry(root1)
            bustype.grid(row=8,column=3)


            Label(root1,text="From: ").grid(row=9,column=1)
            frm=""
            frm = Entry(root1)
            frm.grid(row=9,column=3)


            Label(root1,text="To: ").grid(row=10,column=1)
            destination=""
            destination= Entry(root1)
            destination.grid(row=10,column=3)


            Label(root1,text="Date(dd/mm/yyyy): ").grid(row=11,column=1)
            date=""
            date = Entry(root1)
            date.grid(row=11,column=3)


            Label(root1,text="Dept time: ").grid(row=12,column=1)
            depttime=""
            depttime = Entry(root1)
            depttime.grid(row=12,column=3)


            Label(root1,text="Arr time: ").grid(row=13,column=1)
            arrtime=""
            arrtime = Entry(root1)
            arrtime.grid(row=13,column=3)


            Label(root1,text="Fare: ").grid(row=14,column=1)
            fare=0
            fare = Entry(root1)
            fare.grid(row=14,column=3)


            Label(root1,text="Seats: ").grid(row=15,column=1)
            seats=0
            seats = Entry(root1)
            seats.grid(row=15,column=3)

            def ms():
                messagebox.showwarning("warning","Field is/are empty")

            def save_check_details_to_proceed():
                if(travelsfullname.get()!="" and contactno.get()!=0 and address.get() != "" and operator.get()!="" and bustype.get()!="" and frm.get()!="" and destination.get()!="" and date.get()!="" and depttime.get()!="" and arrtime.get()!="" and fare.get()!="" and seats.get()!="" ):
                    entry_details_in_database()
                else:
                    ms()


            Button(root1,text = "Save",command = save_check_details_to_proceed).grid(row=16,column =  3)
            def home_calling():
                root1.destroy()
                bus_main_screen()

            Button(root1,text="Home",command=home_calling).grid(row=16,column=1)


        Button(root1,text ="Add Details",command = add_details).grid(row=6,column = 3)

        root1.mainloop()




        root.destroy()
        root2 = Tk()

        Label(root2,text="BUS BOOKING SERVICE",font= 100,bg="Black",fg="white",border=10).grid(row=0,column =3)
        img = Image.open("bus5.png")
        x = 2
        y = 2
        re_img = img.resize((634//x,500//y))
        img = ImageTk.PhotoImage(re_img)
        Label(image = img).grid(row=1,column=3)

        Label(root2,text="Listing Buses",font=50).grid(row=2,column=3)

        bus_type_selection = StringVar()
        bus_type_selection.set("Bus Type")
        Label(root2,text="Bus Type: ").grid(row=3,column=0)
        bustype = ['AC','Non-AC','AC Sleeper','Non-Sleeper AC','All Types']
        OptionMenu(root2,bus_type_selection,*bustype).grid(row=3,column=3)


        Label(root2,text="From: ").grid(row=4,column=0)
        frm = Entry(root2)
        frm.grid(row=4,column=3)


        Label(root2,text="To: ").grid(row=5,column=0)
        destination= Entry(root2)
        destination.grid(row=5,column=3)


        Label(root2,text="Date: ").grid(row=6,column=0)
        date = Entry(root2)
        date.grid(row=6,column=3)


        Button(root2,text="Search",border=2,command=search).grid(row=7,column=3)

        Button(root2,text="Home",border=2,command=bus_main_screen).grid(row=7,column=0)

        root2.mainloop()








    root = Tk()

    root.title("Bus Booking Service")

    Label(root,text="BUS BOOKING SERVICE",font= 100,bg="Black",fg="white",border=10).grid(row=0,column =3)

    img = Image.open("bus2.png")
    x = 4
    y = 4
    re_img = img.resize((2048//x,1316//y))
    img = ImageTk.PhotoImage(re_img)
    Label(image = img).grid(row=1,column=3)

    # padx , pady , columnspan , ipadx , ipady in grid
    Button(root,text="Add Bus",font = 150,border = 2,command = add_bus).grid(row=2,column =1)

    Button(root,text="Search Bus",font = 150,border = 2,command = search_bus).grid(row=2,column=4)

    Button(root,text="EXIT !",font=150,fg='red',command = root.destroy,border = 2).grid(row=3,column = 3)

    root.mainloop()





root_details = Tk()
root_details.configure(bg="#FAEBEF")
Label(root_details,text="Project Title : Bus Booking System",font="bold 30",bg="#FAEBEF",fg="#333D79").grid(row=0,column=0)
Label(root_details,text="",bg="#FAEBEF").grid(row=1,column=0)

Label(root_details,text="Developed as a part of the course Advanced Programming Lab-1 & DBMS",font="bold 15",bg="#FAEBEF",fg="#333D79").grid(row=2,column=0)
Label(root_details,text="",bg="#FAEBEF").grid(row=3,column=0)

Label(root_details,text="Developed by: Vaibhav Singhvi , 191B277 , 7014100989 , vaibhavsinghvi254@gmail.com",font="bold 20",bg="#FAEBEF",fg="#333D79").grid(row=4,column=0)
Label(root_details,text="",bg="#FAEBEF").grid(row=5,column=0)

Label(root_details,text="-----------------------------------------------------------------------",font="bold 20",bg="#FAEBEF",fg="#333D79").grid(row=6,column=0)
Label(root_details,text="",bg="#FAEBEF").grid(row=7,column=0)

Label(root_details,text="Project Supervisors: Dr. Mahesh Kumar & Dr. Nilesh Patel",font="bold 20",bg="#FAEBEF",fg="#333D79").grid(row=8,column=0)
Label(root_details,text="",bg="#FAEBEF").grid(row=9,column=0)

Label(root_details,text="make mouse movement to close this",font="bold 10",bg="#FAEBEF",fg="#333D79").grid(row=10,column=0)


def close(e=2):
    root_details.destroy()
    bus_main_screen()

root_details.bind('<Motion>',close)
root_details.mainloop()
