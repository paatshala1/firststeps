# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:24:07 2019

@author: HPC
"""

class Appliances():
    
    def __init__ (self , category , maker , location , smart=False , soldout=False):
        self.code = None
        self.category = category
        self.maker = maker
        self.smart = smart
        self.soldout = soldout
        self.location = location

    def stockout(self):
        if self.soldout == False:
            self.soldout = True
        else:
            self.soldout = False
            
    def trasfer(self , destination):
        origin = self.location
        self.location = destination
        print("You've changed the default location from" , origin , 'to' , self.location)

    def sale(self, off):
        discount = float(off) / 100
        self.offer = off
        self.cprice *= (1 - discount)
        print('Discount applied, new price is: $' , self.cprice)


class Tv(Appliances):
    
    def __init__ (self , category , maker , location , inches , oprice , tech='Plasma'):
        super().__init__(category , maker , location)
        self.inches = inches
        self.oprice = oprice
        self.cprice = oprice
        self.tech = tech
        self.code = next(autocode)

    
class Micro(Appliances):
    
    def __init__(self , category , maker , location , capacity , power):
        super().__init__(category , maker , location)
        self.capacity = capacity
        self.power = power
        self.code = next(autocode)

        
class Stove(Appliances):
    
    def __init__(self , category , maker , location , heater , color='black'):
        super().__init__(category , maker , location)
        self.heater = heater
        self.color = color
        self.code = next(autocode)

def Createappliance():
    vcat = input('Enter Category: ')
    vmaker = input('Enter Maker: ')
    vloc = input('Enter Location: ')
    
    if vcat.lower() == 'tv':
        
        t1 = Tv(vcat , vmaker, vloc , input('Inches: '), float(input('List Price: ')))
        Printaddition(t1)
        return t1
    
    elif vcat.lower() == 'microwave':
        m1 = Micro(vcat, vmaker, vloc, float(input('Capacity: ')), input('Power: '))
        Printaddition(m1)
        return m1
        
    elif vcat.lower() == 'stove':
        s1 = Stove(vcat, vmaker, vloc, input('Heat surface: '))
        Printaddition(s1)
        return s1
        
    else:
        print('ERROR\nYou must select a valid category')

def Printaddition(obj):
        print('\nCreado el artículo:\n' + 20*'-')
        print('\t' , obj.category)
        print('\t' , obj.maker)

def __Codificador():
    for i in range(1 , 1000):
        serie = "A-"
        comp = (4 - len(str(i))) * "0"
        code = serie + comp + str(i)
        yield code

# =============================================================================
# ACÁ EMPIEZA A CORRER EL PROGRAMA, LO ANTERIOR ES CONSTRUCCIÓN DE CLASES
# =============================================================================

print("\n***Starting sku's charge***\n")
autocode = __Codificador()
again = ''
masterdata = dict()
while True:
    if again.lower() == 'n':
        break
    else:
        x = Createappliance()
        if x == None:
            again = input('Would you like to continue adding? (Y/N): ')
        else:
            masterdata[x.code] = x
            again = input('Would you like to continue adding? (Y/N): ')
        
currentstock = dict()
for i in masterdata:
    currentstock[masterdata[i].category] = currentstock.get((masterdata[i].category), 0) + 1

print('\nAddition process completed\n' + 20*'-')
print("There're" , str(len(masterdata)) , "sku's, thus:")
print([(k , v) for k , v in currentstock.items()])

print('\n-------info: masterdata objects-------')
print(masterdata.keys())
print('-------info: masterdata objects-------')