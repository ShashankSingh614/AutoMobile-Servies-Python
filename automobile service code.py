#Project on Automobile Service - Python, MySQL Connectivity
#Title: Porsche Automobile Service

import pickle   #importing pickel module
import csv  #importing csv module
import os   #importing the os module

def add():  #To Add new record
    cust = open("Customer.dat",'wb')    #open file in write mode
    ch = 'y'
    cust4 = []
    while ch == 'Y' or ch == 'y':
        vrn = int(input('Enter the vehicle Registration number:'))
        nm_drv = input("Enter the driver's name:")
        dob = input('Enter the date of birth (DD-MM-YY):')
        ln = input('Enter the license number:')
        acn = int(input('Enter the aadhar card number:'))
        no = int(input ('Enter the contact number:'))
        add = input('Enter the address:')
        car_model = int(input('Select the car model:-\n 1:Porsche 911\n 2:Porsche Cayennen\n 3:Porsche Macanin\n 4:Porsche Panamera\n 5:Porsche Cayman\n 6:Porsche Boxster\n Enter the Number:'))
        a = True
        while a == True:
            if car_model == 1:
                car_model = 'Porsche 911'
                a = False
            elif car_model == 2:
                car_model = 'Porsche Cayennen'
                a = False
            elif car_model == 3:
                car_model = 'Porsche Macanin'
                a = False
            elif car_model == 4:
                car_model = 'Porsche Panamera'
                a = False
            elif car_model == 5:
                car_model = 'Porsche Cayman'
                a = False
            elif car_model == 6:
                car_model = 'Porsche Boxster'
                a = False
            else:
                print()
                print('Invalid choice. Enter the correct choice again:')    #error message
                car_model = int(input('Select the car model:-\n 1:Porsche 911\n 2:Porsche Cayennen\n 3:Porsche Macanin\n 4:Porsche Panamera\n 5:Porsche Cayman\n 6:Porsche Boxster\n Enter the Number:'))
                a = False
        #add the data into list
        data = [vrn,nm_drv,dob,ln,acn,no,add,car_model]
        cust4.append(data)
        print()
        ch = input('Want to enter more records? (y/n):')
        if ch == 'n' or ch == 'N':
            break
        print()
    pickle.dump(cust4,cust)
    cust.close()
        
def update():   #To Update the record
    s = []
    found = False
    searchkey = input('Enter the vehicle Registration number:')
    with open('Customer.dat','rb+') as file:
        s = pickle.load(file)
        b = True
        while b == True:
            len1 = len(s)
            for x in range(0,len1):
                if searchkey in s[x]:
                    rpos = file.tell()
                    print()
                    print('Current Record:')    #displaying the current records 
                    print("Driver's name:",s[x][1])  
                    print('Date of Birth:',s[x][2]) 
                    print('License number:',s[x][3]) 
                    print('Aadhar Card Number:',s[x][4])
                    print('Contact Number:',s[x][5])
                    print('Address:',s[x][6])
                    print('Car Model:',s[x][7]) 
                    print()

                    #updating the record
                    s[x][1] = input("Enter the driver's name:")
                    s[x][2] = input('Enter the date of birth (DD-MM-YY):')
                    s[x][3] = input('Enter the license number:')
                    s[x][4] = int(input('Enter the aadhar card number:'))
                    s[x][5] = int(input ('Enter the contact number:'))
                    s[x][6] = input('Enter the address:')
                    s[x][7] = int(input('Select the car model:-\n 1:Porsche 911\n 2:Porsche Cayennen\n 3:Porsche Macanin\n 4:Porsche Panamera\n 5:Porsche Cayman\n 6:Porsche Boxster\n Enter the Number:'))
                    a = True
                    while a == True:
                        if s[x][7] == 1:
                            s[x][7] = 'Porsche 911'
                            a = False
                        elif s[x][7] == 2:
                            s[x][7] = 'Porsche Cayennen'
                            a = False
                        elif s[x][7] == 3:
                            s[x][7] = 'Porsche Macanin'
                            a = False
                        elif s[x][7] == 4:
                            s[x][7] = 'Porsche Panamera'
                            a = False
                        elif s[x][7] == 5:
                            s[x][7] = 'Porsche Cayman'
                            a = False
                        elif s[x][7] == 6:
                            s[x][7] = 'Porsche Boxster'
                            a = False
                        else:
                            print()
                            print('Invalid choice. Enter the correct choice again:')    #error message
                            s[x][7] = int(input('Select the car model:-\n 1:Porsche 911\n 2:Porsche Cayennen\n 3:Porsche Macanin\n 4:Porsche Panamera\n 5:Porsche Cayman\n 6:Porsche Boxster\n Enter the Number:'))
                            a = False
                
                    file.seek(rpos)
                    pickle.dump(s, file)
                    found = True
            b = False
    if found == False:
        print()
        print('No such record found in the file')
    else:
        print('Updated Successfully')
    file.close()

def search():   #to Search a record
    cust3 = []
    found = False
    searchkey = input('Enter the vehicle Registration number:')
    fin = open('Customer.dat','rb') #open file in read mode
    try:
        while True:
            cust3 = pickle.load(fin)
            len1 = len(cust3)
            for x in range(0,len1):
                if searchkey in cust3[x]:   #to search a record from the list
                    found = True
                    print("Driver's name:",cust3[x][1])  #displaying the records 
                    print('Date of Birth:',cust3[x][2]) 
                    print('License number:',cust3[x][3]) 
                    print('Aadhar Card Number:',cust3[x][4])
                    print('Contact Number:',cust3[x][5])
                    print('Address:',cust3[x][6])
                    print('Car Model:',cust3[x][7]) 
                    print()
                    print('Search Successful.')
    except EOFError:
        if found == False:
            print()
            print('No such record found in the file')
    fin.close()    
    
def delete():   #to Delete a record
    cust3 = []
    found = False
    searchkey = input('Enter the vehicle Registration number:')
    fin = open('Customer.dat','rb+') #open file in read mode
    temp = open('Delete.dat','wb')
    try:
        while True:
            cust3 = pickle.load(fin)
            len1 = len(cust3)
            for x in range(0,len1):
                if searchkey in cust3[x]:   #to search a record from the list
                    rpos = fin.tell()
                    found = True
                    print("Driver's name:",cust3[x][1])  #displaying the records 
                    print('Date of Birth:',cust3[x][2]) 
                    print('License number:',cust3[x][3]) 
                    print('Aadhar Card Number:',cust3[x][4])
                    print('Contact Number:',cust3[x][5])
                    print('Address:',cust3[x][6])
                    print('Car Model:',cust3[x][7]) 
                    print()
                    del cust3[x]
                break
            pickle.dump(cust3,temp)
            print('Deletion Successful')
            found = True
            break
    except EOFError:
        if found == False:
            print()
            print('No such record found in the file')   #error message
    fin.close()
    temp.close()
    os.remove('Customer.dat')
    os.rename('Delete.dat','Customer.dat')
   
def customer(): #Customer function using binary data files
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        print('='*60)
        print()
        print('Customer')   #Customer Menu
        print()
        print('1. To Add new record')
        print('2. To Update the record')
        print('3. To Search a record')
        print('4. To Delete a record')
        print('5. Back')
        print()
        cust_option = int(input('Enter your choice:'))
        print('='*60)
        print()
        while cust_option in (1,2,3,4):
            if cust_option == 1:
                add()   #calling add fuction
                break
            elif cust_option == 2:
                update()    #calling update fuction
                break
            elif cust_option == 3:
                search()    #calling search fuction
                break
            elif cust_option == 4:
                delete()    #calling delete fuction
                break
            else:
                input('Invalid choice. Enter the correct choice again:')    #error message
                cust_option = int(input('Enter your choice:'))
        print()
        ch = input('Want to display Customer Menu? (y/n):')
        if cust_option == 5:    #terminating the program
            break

def feedback(): #to take feedbacks from the customer
    cust = open("Feedback.dat",'ab')    #open file in write mode
    cust_data8 = {}
    feedback = input('Enter your Comments and Suggestons here:')
    pickle.dump(cust_data8,cust)
    print()
    print()
    print('='*25,'Thank You!','='*25)
    print('='*24,'Visit Again!','='*24)
    print()
    
def main(): #Main Menu
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        print('='*60)
        print()
        print('\t\tPorsche Automobile Service Centre')
        print('\t\t\tMumbai, Maharashtra')
        print('\t\t\tIndia')
        print()
        print('='*60)
        print()
        print('\t\t\tMain Menu')   #Main Menu
        print()
        print('\t\t1. Customer')
        print('\t\t2. Type of Service')
        print('\t\t3. Transaction')
        print('\t\t4. Report')
        print('\t\t5. Exit')
        print()
        main_option = int(input('Enter Your Choice:'))
        while main_option in (1,2,3,4,5):
            if main_option == 1:
                customer()  #calling customer menu fuction
                break
            elif main_option == 2:
                tos()   #calling types of service menu fuction
                break
            elif main_option == 3:
                transaction()   #calling transaction menu fuction
                break
            elif main_option == 4:
                report()    #calling report menu fuction
                break
            elif main_option == 5: 
                feedback()  #calling feedback fuction
                ch = str('n')
                break
            else:
                print('Invalid choice. Enter the correct choice again:')    #error message
                main_option = int(input('Enter your choice:'))      
        
#services available

def services():
    print('Folllowing are the services available at our service station')
    print('1. Periodic Service\n 2. A/C Service and Repair\n 3. Insurance Claim\n 4. Tyres and Wheel Care\n 5. Batteries')

def Caynne():   #price of services for caynne
    cust = open("Caynne.dat",'wb')    #open file in write mode
    cust4 = {}
    data=0
    ch='y'
    while ch=='Y' or ch=='y':
        print('Prices for each services for Caynne:-\n 1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210')
        service=int(input('Which service would you like to have from the available services?'))
        print()
        while service in (1,2,3,4,5):
            if service == 1:
                data+=12179
                break
            elif service == 2:
                data+=18247
                break
            elif service == 3:
                data+=171639
                break
            elif service == 4:
                data+=16589
                break
            elif service == 5:
                data+=21210
                break
            else:
                print()
                print('Invalid choice. Enter the correct choice again:')    #error message
                service=int(input('Prices for each services for Caynne:-\n1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210'))
        print()
        ch = input('Want to enter more service? (y/n):')
        
        #add the data into dictionary
    cust4['Caynne Total Amount (Rs.)'] = data
    pickle.dump(cust4,cust)
           
def P911(): #price of services for 911
    cust = open("911.dat",'wb')    #open file in write mode
    cust4 = {}
    data=0
    ch='y'
    while ch=='Y' or ch=='y':
        print('Prices for each services for 911:-\n 1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210')
        service=int(input('Which service would you like to have from the available services?'))
        print()
        while service in (1,2,3,4,5):
            if service == 1:
                data+=12179
                break
            elif service == 2:
                data+=18247
                break
            elif service == 3:
                data+=171639
                break
            elif service == 4:
                data+=16589
                break
            elif service == 5:
                data+=21210
                break
            else:
                print()
                print('Invalid choice. Enter the correct choice again:')    #error message
                service=int(input('Prices for each services for 911:-\n1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210'))
        print()
        ch = input('Want to enter more service? (y/n):')
        
    #add the data into dictionary
    cust4['911 Total Amount (Rs.)'] = data
    pickle.dump(cust4,cust)       

def Macain():   #price of services for macain
    cust = open("Macain.dat",'wb')    #open file in write mode
    cust4 = {}
    data=0
    ch='y'
    while ch=='Y' or ch=='y':
        print('Prices for each services for Macain:-\n 1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210')
        service=int(input('Which service would you like to have from the available services?'))
        print()
        while service in (1,2,3,4,5):
            if service == 1:
                data+=12179
                break
            elif service == 2:
                data+=18247
                break
            elif service == 3:
                data+=171639
                break
            elif service == 4:
                data+=16589
                break
            elif service == 5:
                data+=21210
                break
            else:
                print()
                print('Invalid choice. Enter the correct choice again:')    #error message
                service=int(input('Prices for each services for Macain:-\n1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210'))
        print()
        ch = input('Want to enter more service? (y/n):')
        
    #add the data into dictionary
    cust4['Macain Total Amount (Rs.)'] = data
    pickle.dump(cust4,cust)
    
def Cayman():   #price of services for cayman
    cust = open("Cayman.dat",'wb')    #open file in write mode
    cust4 = {}
    data=0
    ch='y'
    while ch=='Y' or ch=='y':
        print('Prices for each services for Cayman:-\n 1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210')
        service=int(input('Which service would you like to have from the available services?'))
        print()
        while service in (1,2,3,4,5):
            if service == 1:
                data+=12179
                break
            elif service == 2:
                data+=18247
                break
            elif service == 3:
                data+=171639
                break
            elif service == 4:
                data+=16589
                break
            elif service == 5:
                data+=21210
                break
            else:
                print()
                print('Invalid choice. Enter the correct choice again:')    #error message
                service=int(input('Prices for each services for Cayman:-\n1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210'))
        print()
        ch = input('Want to enter more service? (y/n):')
        
    #add the data into dictionary
    cust4['Cayman Total Amount (Rs.)'] = data
    pickle.dump(cust4,cust)

def Boxster():  #price of services for boxster
    cust = open("Boxster.dat",'wb')    #open file in write mode
    cust4 = {}
    data=0
    ch='y'
    while ch=='Y' or ch=='y':
        print('Prices for each services for Boxster:-\n 1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210')
        service=int(input('Which service would you like to have from the available services?'))
        print()
        while service in (1,2,3,4,5):
            if service == 1:
                data+=12179
                break
            elif service == 2:
                data+=18247
                break
            elif service == 3:
                data+=171639
                break
            elif service == 4:
                data+=16589
                break
            elif service == 5:
                data+=21210
                break
            else:
                print()
                print('Invalid choice. Enter the correct choice again:')    #error message
                service=int(input('Prices for each services for Boxster:-\n1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210'))
        print()
        ch = input('Want to enter more service? (y/n):')
        
    #add the data into dictionary
    cust4['Boxster Total Amount (Rs.)'] = data
    pickle.dump(cust4,cust)

def Panamera(): #price of services for panamera
    cust = open("911.dat",'wb')    #open file in write mode
    cust4 = {}
    data=0
    ch='y'
    while ch=='Y' or ch=='y':
        print('Prices for each services for Panamera:-\n 1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210')
        service=int(input('Which service would you like to have from the available services?'))
        print()
        while service in (1,2,3,4,5):
            if service == 1:
                data+=12179
                break
            elif service == 2:
                data+=18247
                break
            elif service == 3:
                data+=171639
                break
            elif service == 4:
                data+=16589
                break
            elif service == 5:
                data+=21210
                break
            else:
                print()
                print('Invalid choice. Enter the correct choice again:')    #error message
                service=int(input('Prices for each services for Panamera:-\n1. Periodic Service:Rs.12179\n 2. A/C Service and Repair:Rs.18247\n 3. Insurance Claim:Rs.171639\n 4. Tyres and Wheel Care:Rs.16589\n 5. Batteries:Rs.21210'))
        print()
        ch = input('Want to enter more service? (y/n):')
        
    #add the data into dictionary
    cust4['Panamera Total Amount (Rs.)'] = data
    pickle.dump(cust4,cust)

def additon():  #addition of services requested by customer
    cust_data5 = []
    cust_data6 = {}
    value = []
    key = []
    vrn = int(input('Enter the vehicle Registration number:'))
    found = False 
    cust = open("Customer.dat",'rb+')    #open file in read and write mode
    try:
        while True:
            rpos = cust.tell()
            cust_data5 = pickle.load(cust)
            len1 = len(cust_data5)
            for x in range(0,len1):
                if vrn in cust_data5[x]:   #to search a record from the list
                    found = True
                    nm_drv1 = cust_data5[x][1]  
                    dob1 = cust_data5[x][2]
                    ln1 = cust_data5[x][3]
                    acn1 = cust_data5[x][4]
                    no1 = cust_data5[x][5]
                    add1 = cust_data5[x][6]
                    car_model1 = cust_data5[x][7] 
                    value = [vrn,nm_drv1,dob1,ln1,acn1,no1,add1,car_model1]    #values of the dictionary
                    key = ['Vehicle_Registration_Number',"Driver's_name",'Date_of_Birth','License_number','Aadhar_Card_Number','Contact_Number','Address','Car_Model']    #keys of the dictinoary
                    cust_data6 = dict(zip(('Vehicle_Registration_Number',"Driver's_name",'Date_of_Birth','License_number','Aadhar_Card_Number','Contact_Number','Address','Car_Model'),(vrn,nm_drv1,dob1,ln1,acn1,no1,add1,car_model1)))
            if cust_data6['Vehicle_Registration_Number'] == vrn: 
                car_model = int(input('Select the car model:-\n 1:Porsche 911\n 2:Porsche Cayennen\n 3:Porsche Macanin\n 4:Porsche Panamera\n 5:Porsche Cayman\n 6:Porsche Boxster\n Enter the Number:'))
                while car_model in (1,2,3,4,5,6):
                    if car_model == 1:
                        P911()  #calling P911 fuction
                        #accessing 911 data using read mode
                        cust8 = {}
                        fin2 = open('911.dat','rb')
                        try:
                            while True:
                                cust8 = pickle.load(fin2)
                                amt = cust8['911 Total Amount (Rs.)']
                        except EOFError:
                            fin2.close()
                        break
                        
                    elif car_model == 2:
                        Caynne()    #calling Caynne fuction
                        #accessing Caynne data using read mode
                        cust8 = {}
                        fin2 = open('Caynne.dat','rb')
                        try:
                            while True:
                                cust8 = pickle.load(fin2)
                                amt = cust8['Caynne Total Amount (Rs.)']
                        except EOFError:
                            fin2.close()
                        break

                    elif car_model == 3:
                        Macain()    #calling Macain fuction
                        #accessing Macain data using read mode
                        cust8 = {}
                        fin2 = open('Macain.dat','rb')
                        try:
                            while True:
                                cust8 = pickle.load(fin2)
                                amt = cust8['Macain Total Amount (Rs.)']
                        except EOFError:
                            fin2.close()
                        break
                             
                    elif car_model == 4:
                        Panamera()  #calling Panamera fuction 
                        #accessing Panamera data using read mode
                        cust8 = {}
                        fin2 = open('Panamera.dat','rb')
                        try:
                            while True:
                                cust8 = pickle.load(fin2)
                                amt = cust8['Panamera Total Amount (Rs.)']
                        except EOFError:
                            fin2.close()
                        break
                              
                    elif car_model == 5:
                        Cayman()    #calling Cayman fuction
                        #accessing Cayman data using read mode
                        cust8 = {}
                        fin2 = open('Cayman.dat','rb')
                        try:
                            while True:
                                cust8 = pickle.load(fin2)
                                amt = cust8['Cayman Total Amount (Rs.)']
                        except EOFError:
                            fin2.close()
                        break
                             
                    elif car_model == 6:
                        Boxster() #calling Boxster fuction 
                        #accessing Boxster data using read mode
                        cust8 = {}
                        fin2 = open('Boxster.dat','rb')
                        try:
                            while True:
                                cust8 = pickle.load(fin2)
                                amt = cust8['Boxster Total Amount (Rs.)']
                        except EOFError:
                            fin2.close()
                        break
                            
                    else:
                        print()
                        print('Invalid choice. Enter the correct choice again:')    #error message
                        car_model = int(input('Select the car model:-\n 1:Porsche 911\n 2:Porsche Cayennen\n 3:Porsche Macanin\n 4:Porsche Panamera\n 5:Porsche Cayman\n 6:Porsche Boxster\n Enter the Number:'))

                #accessing customer data using read mode
                nm_drv = cust_data6["Driver's_name"]
                dob = cust_data6['Date_of_Birth']
                ln = cust_data6['License_number'] 
                acn = cust_data6['Aadhar_Card_Number']
                no = cust_data6['Contact_Number']
                add = cust_data6['Address']

                #adding data to list
                with open("Customer.csv", "a+") as outfile: #open file in write and read mode using csv
                    csv_writer = csv.writer(outfile)
                    csv_writer.writerow(['Vehicle_Registration_Number',"Driver's_name",'Date_of_Birth','License_number','Aadhar_Card_Number','Contact_Number','Address','Car_Model','Total Amount (Rs.)'])
                    csv_writer.writerow([vrn,nm_drv,dob,ln,acn,no,add,car_model,amt])

    except EOFError:
        if found == False:
            print()
            print('No such record found in the file')   #error message
            print()
        else:
            print()
            print('Updated Successfully.')
            print()
        cust.close()

def tos():
    services()
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        print('='*60)
        print()
        print('Type of Service')   #type of service Menu
        print()
        print('1. To Add new service')
        print('2. Back')
        print()
        cust_option = int(input('Enter your choice:'))
        print('='*60)
        print()
        while cust_option in (1,2):
            if cust_option == 1:
                additon()   #calling addition fuction
                break
            elif cust_option == 2:
                main()  #calling main menu fuction
                break
            else:
                input('Invalid choice. Enter the correct choice again:')    #error message
                cust_option = int(input('Enter your choice:'))
        print()
        ch = input('Want to display Type of Service? (y/n):')

def transaction():  #Transaction
    print('Transaction')
    cust_transaction = {}
    found = False

    while (found == False):
        searchkey = input('Enter the Vehicle Registration number:')
        with open('Customer2.bin','rb') as fin:  
            cust_transaction = pickle.load(fin)
            for record in cust_transaction:
                cust = record.split(',')
                if cust[0] == searchkey:
                    found = True
                    break

        if found == False:
            print()
            print('No such record found in the file')
            cont = int(input("Enter 1 if you wish to re-enter the VRN - "))
            if (cont == 1):
                continue
            else:
                break
        else:
            break

    if (found == True):
    
        #check order details in csv
        fieldsR = []
        rowsR = []
        with open("Customer.csv",'r') as f:
            csvreader = csv.reader(f)
            fieldsR = next(csvreader)
            for row in csvreader:
                rowsR.append(row)

            fordatabase_vrn = ''
            fordatabase_amount = ''
            fordatabase_mode = ''
            fordatabase_bank = ''
            fordatabase_cardno = ''
            fordatabase_date_of_expiry = ''
            fordatabase_cvv = ''
        
            found = False 
        
            for row in rowsR:
                if searchkey == row[0]:
                    found = True 
                    fordatabase_vrn = row[0]
                    print("Your total bill is for Rs. "+row[2])
                    fordatabase_amount = row[2]
                    while True:
                        print("Choose mode of payment - \n1. Net Banking\n2. Credit/Debit/ATM Card")
                        ch = int(input("Enter 1/2 > "))
                        if (ch in (1,2)):
                            if ch == 1:
                                fordatabase_mode = "Net Banking"
                                while True:
                                    print("Choose your bank - \n1. HDFC Bank\n2. ICICI Bank\n3. State Bank of India\n4. Axis Bank\n5. Kotak Mahindra Bank")
                                    ch = int(input("Enter 1/2/3/4/5 > "))
                                    if (ch in (1,2,3,4,5)):
                                        if ch == 1:
                                            fordatabase_bank = 'HDFC Bank'
                                        elif ch == 2:
                                            fordatabase_bank = 'ICICI Bank'
                                        elif ch == 3:
                                            fordatabase_bank = 'State Bank of India'
                                        elif ch == 4:
                                            fordatabase_bank = 'Axis Bank'
                                        elif ch == 5:
                                            fordatabase_bank = 'Kotak Mahindra Bank'
                                        break
                                    else:
                                        print("Invalid input for bank!")
                                        continue
                            else:
                                while True:
                                    print("Choose - \n1. Credit Card\n2. Debit Card\n3. ATM Card")
                                    ch = int(input("Enter 1/2/3 > "))
                                    if (ch in (1,2,3)):
                                        if ch == 1:
                                            fordatabase_mode = "Credit Card"
                                        elif ch == 2:
                                            fordatabase_mode = "Debit Card"
                                        elif ch == 3:
                                            fordatabase_mode = "ATM Card"

                                        fordatabase_cardno = input("Enter card number > ")
                                        fordatabase_date_of_expiry = input("Enter date of expiry > ")
                                        fordatabase_cvv = input("Enter CVV > ")
                                        break
                                    else:
                                        print("Invalid input - Enter correct card!")
                                        continue                            
                            break
                        else:
                            print("Invalid input for mode of payment!")
                            continue
                    
                                
            if found == False:
                print("No transaction found for Vehicle Registration Number", searchkey)            
    
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="toor",
        database="dbproject"
        )

        mycursor = mydb.cursor()

        query = ''
    
        if fordatabase_mode == "Net Banking":
            query = "INSERT INTO transaction (vrn, amount, mode_pyt, bank) VALUES (\"" + fordatabase_vrn + "\", \"" + fordatabase_amount + "\", \"" + fordatabase_mode + "\", \"" + fordatabase_bank + "\")"
            print(query)
            mycursor.execute(query)
            mydb.commit()
            mydb.close()

def report():  #Report
    Tax=0
    cust_id=int(input("Enter the customer id:"))
    str="select cust_id,cust_name,adress,mobileno,licenseno,adharcarno,adv_payment,total"
    query=str.format(cust_id)
    print('='*60)
    mycur.execute(query)
    myrec=mycur.fetchall()
    for x in myrec:
        cust_id= x[0]
        cust_name= x[1]
        address= x[2]
        mobileno= x[3]
        licenseno= x[4]
        adharno= x[5]
        adv_payment= x[6]
        total= x[7]
    print('='*60)
    print("PORSCHE AUTOMOBILE SERVICE CENTRE :)")
    print("Mumbai,Maharashtra")
    print("India")
    print('='*60)
    print("customer no",cust_id)
    print("customer name",cust_name)
    print("customer address",address)
    print('='*60)
    print("mobile number",mobileno)
    print("license number",licenseno)
    print("Adhar card number",adharno)
    print('='*60)
    print("Advance",'Rs.',adv_payment)
    print('Total','Rs.',total)
    tax=total*0.10
    print("Tax:",'Rs.',tax)
    net=float(adv_payment)-(float(total)+float(Tax))
    netmat=float(total)+float(Tax)
    print("net amount",'Rs.',netmat)
    print("Total balance paybale to the customer",'Rs.',net)
    
#=============================================================
    
#Main Program
a = main()  #calling main menu fuction