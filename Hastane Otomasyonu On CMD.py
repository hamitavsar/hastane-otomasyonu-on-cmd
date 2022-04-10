import os
import sqlite3
from sqlite3.dbapi2 import Cursor
import time

try:
    con =sqlite3.connect("lab.db")
    cur = con.cursor()
except os.error:
    print (os.error)
    
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



def autoCreateTable():
    cur.execute('''
    
        CREATE TABLE IF NOT EXISTS DOCTORS(
            id integer PRIMARY KEY,
            name text NOT NULL,
            specialty text NOT NULL,
            costOfAdmission integer NOT NULL,
            nameOfTheReception text NOT NULL,
            percentageOfDeductionsOnSalaries integer NOT NULL
            
        )
    
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS HISTORYOFPATENTS(
            id integer PRIMARY KEY NOT NULL,
            idPatients int  NOT NULL,
            idDoctors1 int  NOT NULL,
            dateofAdmission text NOT NULL,
            reservationDate text NOT NULL,
            costOfAdmission int NOT NULL,
            FOREIGN KEY (idPatients)  REFERENCES PATIENTS (id)
            FOREIGN KEY (idDoctors1)   REFERENCES DOCTORS  (id)
           
             
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS PATIENTS(
        id integer PRIMARY KEY,
        patientName text NOT NULL,
        patientSurname text NOT NULL,
        dateOfBirthPatient date NOT NULL,
        patientAdress text NOT NULL
       
        )
    ''')

def autoMakeData():

    #Auto creater make some Doctors 
    cur.executescript ("""    
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Alex Ibrahimovic','Therapist',100,'Hamit Avsar',10);
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Natalia Alexandrova','Pyhsicologist',150,'Can', 10);
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Kerem ER','Cardiologist',450,'Yagiz Ali', 15);
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Bora Samdanli','Cardiologist',450,'Hasan Sabbah', 10);
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Dmitry','Surgeon',200,'Yagiz Bora',10);
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Natasa','Surgeon',200,'Atahan',15);
    """)
    cur.executescript("""
    INSERT INTO PATIENTS(patientName,patientSurname,dateOfBirthPatient,patientAdress) values ('Cabbar','Donergil','16-05-1990','Ankara');
    INSERT INTO PATIENTS(patientName,patientSurname,dateOfBirthPatient,patientAdress) values ('Bora','Samdanli','16-05-1998','Kharkiv');
    INSERT INTO PATIENTS(patientName,patientSurname,dateOfBirthPatient,patientAdress) values ('Kemal','Donmez','1-01-1999','Istanbul');
    INSERT INTO PATIENTS(patientName,patientSurname,dateOfBirthPatient,patientAdress) values ('Tayyar','Yılmaz','12-03-1995','Antalya');
    
    """)
    
def makeAppointment(doctorName1,doctorName2,doctorName3,speciality1,speciality2,speciality3,Patients,Price,date,dateOfappointment):
    clear = clearConsole()
    clear
    print("""
                Hello! Mr. / Mrs. {0}.
                Your Speciality is: {1} - {2} - {3}-
                Your Doctors: {4} - {5} - {6}
                Date: {8}
                Your Reservation: {9}
                Price: {7}
            """.format(Patients,speciality1,speciality2,speciality3,doctorName1,doctorName2,doctorName3,Price,date,dateOfappointment))

    

def makePrice(costOfAdmission,costfOfReception):
    price = costOfAdmission
    Percentage = (costOfAdmission * costfOfReception) / 100
    price += (Percentage*0.13)
    return price
autoCreateTable()

def savePatients(Name,Surname,BirthDay,Adres):
    cur.execute('INSERT INTO PATIENTS(patientName, patientSurname, dateOfBirthPatient,patientAdress) values(?,?,?,?)',(Name,Surname,BirthDay,Adres))
    con.commit()
    print("Succesfull!")
def updatePatients(id,patientName, patientSurname, dateOfBirthPatient,patientAdress):
    updateQuery="""UPDATE PATIENTS SET patientName=?,patientSurname=?,dateOfBirthPatient =?,patientAdress=? WHERE id=?"""
    setValues =(patientName,patientSurname,dateOfBirthPatient,patientAdress,id)
    con.execute(updateQuery,setValues)
    con.commit()
    clearConsole()
    print("UPDATE SUCCESFUL!")
    mainmenu()
def saveHistoryPatients(idPatients,idDoctors1,dateOfAdmission,reservationDate,costOfAdmission):
    cur.execute ("INSERT INTO HISTORYOFPATENTS(idPatients,idDoctors1,dateOfAdmission,reservationDate,costOfAdmission) values (?,?,?,?,?);",(idPatients,idDoctors1,dateOfAdmission,reservationDate,costOfAdmission))
    con.commit()
    


def saveReception(receptionName,percentage):
    cur.execute ("INSERT INTO RECEPTIONOFPATIENTS(nameOfTheReception,percentageOfDeductionsOnSalaries) values (?,?);",(receptionName,percentage))
    con.commit()
    print("Succesfull!")
def getReception():
    cur.execute("SELECT * FROM RECEPTIONOFPATIENTS")
    data=cur.fetchall()
    return data

def makeReception():
    breakToReception = 0
    while breakToReception !=1:
        print("""
        *************************************************************
        *         Welcome To Make New Recepitonist                  *
        * 1) Create New Reception                                   *
        * 2) Delete Reception                                       *
        * If you want to turn back main menu please push to any key *
        *************************************************************
        """)
        selecting = input()
        if selecting == "1":
            while breakToReception !=1:    
                try:            
                    receptionName = input("Reception name and surname: ")
                    percentageSaleries = int(input("\n!!!!!! JUST DIGIT PLEASE !!!!!! \nPercentage of Deductions On Salaries: "))
                except ValueError:
                    print("\n\nYou must to be saleries just digit!")
                    continue
                saveReception(receptionName,percentageSaleries)
                print("Register Succesfull.. You're Turning Main Menu")
                mainmenu()
        elif selecting == "2":
            receptions=getReception()
            for i in receptions:
                print("{0})     {1}".format(i[0], i[1]))
            while breakToReception !=1:    
                try:            
                   
                    receptionId = int(input("\n!!!!!! JUST DIGIT PLEASE !!!!!! \n Reception Order: "))
                except ValueError:
                    print("\n\nYou must to be saleries just digit!")
                    continue
                deleteReception(receptionId)
                print("Proccess Succesfull.. You're Turning Main Menu")
                mainmenu()
                     

        mainmenu()
def deleteReception(id):
    cur.execute ("DELETE FROM RECEPTIONOFPATIENTS WHERE id=?",(id,))
    con.commit()
    print("Succesfull!")

def updateDoctor(id,name,specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries):
    updateQuery="""UPDATE DOCTORS SET name=?,specialty=?,costOfAdmission =?,nameOfTheReception=?,percentageOfDeductionsOnSalaries=? WHERE id=?"""
    setValues =(name,specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries,id)
    con.execute(updateQuery,setValues)
    con.commit()
    clearConsole()
    print("UPDATE SUCCESFUL!")
    mainmenu()
def saveDoctor(DoctorName,specialty,costOfAdmissin,nameOfTheReception,percentageOfDeductionsOnSalaries):
    cur.execute ("INSERT INTO DOCTORS(name,specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values (?,?,?,?,?);",(DoctorName,specialty,costOfAdmissin,nameOfTheReception,percentageOfDeductionsOnSalaries))
    con.commit()
    print("Succesfull!")
def deleteDoctors(id):
    cur.execute ("DELETE FROM DOCTORS WHERE id=?",(id,))
    cur.execute("DELETE FROM HISTORYOFPATENTS WHERE idDoctors1=?",(id,))
    con.commit()
    print("Succesfull!")
def makeDoctor():
    doctorlist = getDoctor()
    breakToReception = 0
    breakUpdate =0
    while breakToReception !=1:
        print("""
        *************************************************************
        *         Welcome To Make New Doctor                        *
        * 1) Create New Doctor                                      *
        * 2) Delete Doctors                                         *
        * 3) Update Doctors                                         *
        * If you want to turn back main menu please push to any key *
        *************************************************************
        """)
        selecting = input()
        if selecting == "1":
            while breakToReception !=1:    
                try:            
                    doctorName = input("Doctor name and surname: ")
                    doctorSpecialty = input("Doctor Specialty: ")
                    costOfAdmission = int(input("\n!!!!!! JUST DIGIT PLEASE !!!!!! \nCost Of Admission: "))
                    nameOftheRecepsion = input("Reception Name: ")
                    percentageOfDeductionsOnSalaries = int(input("\n !!!! JUST DIGIT PLEASE !!!! \n Cost Of Reception: "))
                except ValueError:
                    print("\n\nYou must to be Cost Of Admission is just digit!")
                    continue
                saveDoctor(doctorName,doctorSpecialty,costOfAdmission,nameOftheRecepsion,percentageOfDeductionsOnSalaries)
                print("Register Succesfull.. You're Turning Main Menu")
                mainmenu()
        if selecting == "2":
            
            print("\n")
            for i in doctorlist:
                print("{0})        {1}".format(i[0],i[1]))
            while breakToReception !=1:    
                try:            
                    doctorsId = int(input("\n!!!!!! JUST DIGIT PLEASE !!!!!! \nOrder of Doctor: "))
                except ValueError:
                    print("\n\nYou must to be push is just digit!")
                    continue
                deleteDoctors(doctorsId)
                print("Register Succesfull.. You're Turning Main Menu")
                mainmenu()
        if selecting =="3":
            print("\n")
            for i in doctorlist:
                print("{0}) {1}    {2}     {3}    {4}     {5}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
            while breakUpdate !=1:
                try:
                  doctorsId = int(input("\n!!!!!! JUST DIGIT PLEASE !!!!!! \nOrder of Doctor: "))
                except ValueError:
                    print("\n\n You must to insert is just digit!")
                    continue
                try:            
                    doctorName = input("Doctor name and surname: ")
                    doctorSpecialty = input("Doctor Specialty: ")
                    costOfAdmission = int(input("\n!!!!!! JUST DIGIT PLEASE !!!!!! \nCost Of Admission: "))
                    nameOftheRecepsion = input("Reception Name: ")
                    percentageOfDeductionsOnSalaries = int(input("\n !!!! JUST DIGIT PLEASE !!!! \n Cost Of Reception: "))
                except ValueError:
                    print("\n\nYou must to be Cost Of Admission is just digit!")
                    continue
                updateDoctor(doctorsId,doctorName,doctorSpecialty,costOfAdmission,nameOftheRecepsion,percentageOfDeductionsOnSalaries)
                break
            mainmenu()

                     

        mainmenu()
def getDoctor():
    cur.execute("SELECT * FROM DOCTORS")
    data=cur.fetchall()
    return data
def selectDoctor(id):
    cur.execute("SELECT * FROM DOCTORS WHERE id=?",(id,))
    data=cur.fetchall()
    return data


#autoMakeData()

def createAppointment():
    error = 0
    end = 0
    
    while end != 1:
       
        try:       
            name = str(input("What's your name?: \n"))
            surname=str(input ("What's your surname?: \n"))
            birth = input ("Date Of Birth: \n")
            adress = input("Adres: \n")
        except os.error:
            print("Please just you can input string on name and surname!")
            error =1
        if error == 1:
            continue
        else:
            
            savePatients(name,surname,birth,adress)
            break
def getAppointment(id=0):
    if id==0:
        cur.execute("SELECT * FROM PATIENTS")
        data=cur.fetchall()
        return data
    else:
        cur.execute("SELECT * FROM PATIENTS WHERE id=?",(id,))
        data=cur.fetchall()
        return data
def  registerAppointment():
    today = time.strftime("%d/%m/%Y")
    stop = 0
    cost =0
    allAppointment = getAppointment()
    totalCost =0
    doctors = getDoctor()
    selectOneMore =""
    selectSpeciality = []
    selectSpeciality1 =[]
    selectSpeciality2=[]
    tempId = 0
    tempName =""
    tempSurname = ""
    tempBirth =""
    tempAdres=""
    tempDoctorName1=""
    idDoctor1= 0
    costOfReception = 0
    while stop != 1:
         
         for i in allAppointment:
             print("{0})      {1} {2}      {3}".format(i[0],i[1],i[2],i[3]))

         try:
            select = int(input("\nSelect Appointment: "))
         except:
             clearConsole()
             print("You can use just DIGIT!")
             continue
         while select != None:
             select = getAppointment(select)
             for i in select:
                 tempId = i[0]
                 tempName = i[1]
                 tempSurname =i[2]
                 tempBirth = i[3]
                 tempAdres = i[4]

             print("""
             ********************************************
             *                                          *
             *                                          *
             * WELCOME TO BEST OF CLINIC IN KHARKIV!    *
             *                                          *
             *                                          *
             ********************************************
             Welcome Mr./Mrs. {0} {1} \n\t\t\tHow we can help you?
             
             """.format(tempName,tempSurname))
             
             for i in doctors:
                    print("{})""{}"                 "\t\t\t{}"                  "\t\t\tPrice:{}$      Reception: {}".format(i[0],i[1],i[2],i[3],i[4]))
             while select != None:
                 try:
                    idDoctor1 = int(input("Select Your Doctor: "))
                    selectSpeciality = selectDoctor(idDoctor1)
                    for i in selectSpeciality:
                        idDoctor1=i[0]
                        cost =  i[3]
                        tempDoctorName1=i[1]
                        tempSpeciality1=i[2]
                        costOfReception=i[5]
                    print("Do you want to be next time rezervation or now?\n 1) Now \n 2) Select time")
                    rezervation=input("Your Select is: ")
                    if rezervation == "1":
                        saveHistoryPatients(tempId,idDoctor1,today,0,makePrice(cost,costOfReception))
                        totalCost = totalCost +makePrice(cost,costOfReception)
                    elif rezervation =="2":
                        rezervationDate= input("Input Your Date: ")
                        saveHistoryPatients(tempId,idDoctor1,0,rezervationDate,makePrice(cost,costOfReception))
                        totalCost = totalCost +makePrice(cost,costOfReception)
                    selectOneMore=input("Do you want to one more rezervation new Doctor? (Y/N)?: ")
                    if selectOneMore =="Y" or selectOneMore == "N":
                        if selectOneMore == "Y" or selectOneMore == "y":
                            idDoctor1 = int(input("Select Your 2. Doctor : "))
                            selectSpeciality1 = selectDoctor(idDoctor1)
                            for i in selectSpeciality1:
                                 idDoctor1=i[0]
                                 cost =  i[3]
                                 tempDoctorName2=i[1]
                                 tempSpeciality2=i[2]
                                 costOfReception=i[5]
                            print("Do you want to be next time rezervation or now?\n 1) Now \n 2) Select time")
                            rezervation=input("Your Select is: ")
                            if rezervation == "1":
                                saveHistoryPatients(tempId,idDoctor1,today,0,makePrice(cost,costOfReception))
                                totalCost = totalCost +makePrice(cost,costOfReception)
                            elif rezervation =="2":
                                rezervationDate= input("Input Your Date: ")
                                saveHistoryPatients(tempId,idDoctor1,0,rezervationDate,makePrice(cost,costOfReception))
                                totalCost = totalCost +makePrice(cost,costOfReception)
                            selectOneMore=input("Do you want to one more rezervation new Doctor? (Y/N)?: ")
                            if selectOneMore =="Y" or selectOneMore == "N":
                                if selectOneMore == "Y" or selectOneMore == "y":
                                    idDoctor1 = int(input("Select Your 3. Doctor: "))
                                    selectSpeciality2 = selectDoctor(idDoctor1)
                                    for i in selectSpeciality2:
                                        idDoctor1=i[0]
                                        cost =  i[3]
                                        tempDoctorName3=i[1]
                                        tempSpeciality3=i[2]
                                        costOfReception=i[5]
                                    print("Do you want to be next time rezervation or now?\n 1) Now \n 2) Select time")
                                    rezervation=input("Your Select is: ")
                                    if rezervation == "1":
                                        saveHistoryPatients(tempId,idDoctor1,today,0,makePrice(cost,costOfReception))
                                        totalCost = totalCost +makePrice(cost,costOfReception)
                                    elif rezervation =="2":
                                        rezervationDate= input("Input Your Date: ")
                                    saveHistoryPatients(tempId,idDoctor1,0,rezervationDate,makePrice(cost,costOfReception))
                                    totalCost = totalCost +makePrice(cost,costOfReception)
                                else:
                                    break
                            else:
                                print("YOU CAN JUST 'Y' or 'N'")
                        else:
                            break

                    else:
                        print("YOU CAN JUST 'Y' or 'N'")
                
                 except:
                     print("You can use just DIGIT!")
                 break
             
            # saveHistoryPatients(tempId,idDoctor1,dateOfAdmission,makePrice(cost))      
            # makeAppointment(tempDoctorName1,tempDoctorName2,tempDoctorName3,tempSpeciality1,tempSpeciality2,tempSpeciality3,tempName,totalCost,today,rezervationDate)   
             break
         mainmenu()
         

def mainmenu():
    end = 0
    select = 0
    while end != 1:
        print("""
        *********************************************************************
        * 1) Doctors                                                        *
        * 2) Create New Appointment                                         *
        * 3) Register Appointment                                           *
        *If you want to turn back main menu please push to any key          *
        *********************************************************************
        """)
        try:
            select = int(input("Your Option: "))
            if select == "a-z" or select =="A-Z":
                break
        except OSError:
            print("You Can Select range 1 to 4. For example: 1")
           
            
        if select == 1:
            makeDoctor()
            select = 0
        elif select ==2:
            createAppointment()
            select = 0
        elif select ==3:
            registerAppointment()
            select = 0
        
        break


mainmenu()