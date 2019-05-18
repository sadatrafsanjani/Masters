from tkinter import *


accounts = []
customers = []

class Account(object):
    
    def __init__(self, id, balance, types, created, last):
        
        self.id = id
        self.balance = balance
        self.types = types
        self.created = created
        self.last = last
        
    def getId(self):
        
        return self.id
    
    def setId(self, id):
        
        self.id = id
    
    def getBalance(self):
        
        return self.balance
    
    def setBalance(self, balance):
        
        self.balance = balance
    
    def getTypes(self):
        
        return self.types
    
    def setTypes(self, types):
        
        self.types = types
    
    def getCreated(self):
        
        return self.created
    
    def setCreated(self, created):
        
        self.created = created
    
    def getLast(self):
        
        return self.last
    
    def setLast(self, last):
        
        self.last = last

class Customer(object):
    
    def __init__(self, name="", username="", password="", phone="", address="", account=None, types=""):
        
        self.name = name
        self.username = username
        self.password = password
        self.phone = phone
        self.address = address
        self.account = account
        self.types = types
        
    def getName(self):
        
        return self.name
    
    def setNname(self,name):
        
        self.name = name
        
    def getUsername(self):
        
        return self.username
    
    def setUsername(self,username):
        
        self.username = username
    
    def getPassword(self):
        
        return self.password
    
    def setPassword(self, password):
        
        self.password = password
    
    def getPhone(self):
        
        return self.phone
    
    def setPhone(self, phone):
        
        self.phone = phone
    
    def getAddress(self):
        
        return self.address
    
    def setAddress(self, address):
        
        self.address = address
    
    def getAccount(self):
        
        return self.account
    
    def setAccount(self, account):
        
        self.account = account
        
    def getTypes(self):
        
        return self.types
    
    def setTypes(self, types):
        
        self.types = types


class Application(Frame):
    
    def __init__(self, master):
        
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        
        self.label1 = Label(self, text = "Name:")
        self.label1.grid(row=0, column=0, columnspan=2, sticky = W)
        self.label2 = Label(self, text = "Username:")
        self.label2.grid(row=1, column=0, columnspan=2, sticky = W)
        self.label3 = Label(self, text = "Password:")
        self.label3.grid(row=2, column=0, columnspan=2, sticky = W)
        self.label4 = Label(self, text = "Phone:")
        self.label4.grid(row=3, column=0, columnspan=2, sticky = W)
        self.label5 = Label(self, text = "Address:")
        self.label5.grid(row=4, column=0, columnspan=2, sticky = W)
        self.label6 = Label(self, text = "Type:")
        self.label6.grid(row=5, column=0, columnspan=2, sticky = W)
        
        self.entry1 = Entry(self)
        self.entry1.grid(row=0, column=3, columnspan=2, sticky = W)      
        self.entry2 = Entry(self)
        self.entry2.grid(row=1, column=3, columnspan=2, sticky = W)
        self.entry3 = Entry(self)
        self.entry3.grid(row=2, column=3, columnspan=2, sticky = W)
        self.entry4 = Entry(self)
        self.entry4.grid(row=3, column=3, columnspan=2, sticky = W)
        self.entry5 = Entry(self)
        self.entry5.grid(row=4, column=3, columnspan=2, sticky = W)
        self.entry6 = Entry(self)
        self.entry6.grid(row=5, column=3, columnspan=2, sticky = W)
        
        self.btn = Button(self, text="Register")
        self.btn["command"] = self.register
        self.btn.grid()
        
    def register(self):
        
        name = self.entry1.get()
        username = self.entry2.get()
        password = self.entry3.get()
        phone = self.entry4.get()
        address = self.entry5.get()
        types = self.entry6.get()
        
        register = Customer(name, username, password, phone, address, types)
        customers.append(register)
        
        
                
        self.login()
        
        
    def login(self):
                
        self.label1 = Label(self, text = "Username:")
        self.label1.grid(row=1, column=0, columnspan=2, sticky = W)
        self.label2 = Label(self, text = "Password:")
        self.label2.grid(row=1, column=0, columnspan=2, sticky = W)
        
        
        self.entry1 = Entry(self)
        self.entry1.grid(row=0, column=3, columnspan=2, sticky = W)      
        self.entry2 = Entry(self)
        self.entry2.grid(row=1, column=3, columnspan=2, sticky = W)
        self.entry2.config(show="*")
        
        self.btn = Button(self, text="Login")
        self.btn["command"] = self.authenticate
        self.btn.grid()
        
        
    def authenticate(self):
        
        username = self.entry1.get()
        password = self.entry2.get()
        
        if(username is 'abc' and password is 'abc'):
            print('Logged In!')
        else:
            print('Error!')
        

root  = Tk()
root.title("Bipasha")
root.geometry("300x400")
app = Application(root)
root.mainloop()