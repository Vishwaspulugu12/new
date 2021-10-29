# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:51:44 2017

@author: vish
"""
from table import Table

class Rest:
    table_obj=[]
    def __init__(self):
        self.name=input("ENTER NAME: ")
        self.tables_count=int(input("ENTER tables_count: "))
        self.free_tables=[]
        self.occup_count=0
        self.avg_time=int( input("ENTER avg_time in sec: ")) 
        #self.table_obj=[]
        self.wait_time=0
        for obj in range (self.tables_count):
            self.table_obj.append(Table(self.avg_time)) 
        
#add a new table           
    def add_table(self):
        print ("----Adding new table-----")
        self.tables_count+=1
        self.table_obj.append (Table(self.avg_time))
        
#new customers, search for free table and allot to new customer
    def new_customers(self): 
        self.free_tables=[]
        for table_number in range (self.tables_count):
            if self.table_obj[table_number].get_status():
                self.free_tables.append(table_number)
        print ("List of Free tables:",self.free_tables)  
        table_num=int(input("enter selected table number: \t "))
        if (self.table_obj[table_num].get_status()):
            self.table_obj[table_num].new()
        else:
            print ("Invalid Input, please re-select one from the list:")
            self.new_customers()
 
#to get the minimum wait time for a table to be free
    def display_wait_times(self):
        for table_number in range (self.tables_count):
            #self.wait_times.append(self.table_obj[table_number].get_time_left())
            self.wait_time = self.table_obj[table_number].get_time_left()
            if(self.wait_time<=0):
                self.wait_time='Free'
            else:
                pass
            print ("\n WAIT TIMES: Table{}: {}" .format(table_number,self.wait_time))
        #self.wait_times.sort()
         
        

#finish table
    def finish(self):
       self.table_obj[int(input("enter table number that finished"))].finish()
       

#Master Function- Running always in a loop and calls all other functions
    def run(self):
        #functions={'1': self.add_table(),'2': self.new_customers(), '3':self.finish(), '4': self.wait_times()}
        selection= input(" MAIN MENU:Select one of the following options: \n \
                         1: ADD A NEW TABLE \n \
                         2: NEW CUSTOMERS \n \
                         3: TABLE FINISHED \n \
                         4: WAIT TIME \n \
                         5: Exit \n")
       
        if(selection=='1'):
            self.add_table() 
        elif(selection=='2'):
            self.new_customers()
        elif (selection=='3'):
            self.finish()
        elif(selection=='4'):
            self.display_wait_times()
        elif(selection=='5'):
            pass
        else:
            print("Invalid Selection. Reselect from the list")
        
        if(selection!='5'):
            self.run() 
            
#new branch1
        
        
        
        
