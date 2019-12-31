
import pickle

# =============================================================================
# EL MÉTODO __str__ NO PERMITE IMPRIMIR LA INFO DEL OBJETO COMO STRING, YA QUE
# DE LO CONTRARIO EL MÉTODO showp() MOSTRARÍA LOS OBJETOS CREADOS EN MEMORIA
# PERO NO SU INFO: (<__main__.People object at 0x00000218F088B9C8>)
# =============================================================================
class Person:
    def __init__(self , name , nac , age):
        self.name = name
        self.nac = nac
        self.age = age
        print("\nIt's been created:" , self.name)
    
    def __str__(self): 
        return "{} {} {}".format(self.name , self.nac , self.age)
        
# =============================================================================
# LA CLASE NO TENÍA EL __init__ PERO SI SU CONTENIDO, LO AGREGUÉ PARA TENER 
# CLARO QUE LO QUE SE ESTABA HACIENDO ERA CREAR UNA "PROPIEDAD" DEL OBJETO
# PEOPLELIST QUE CONSISTE EN UNA LISTA Y QUE POR LO TANTO COMO CUALQUIER OTRA
# PROPIEDAD DEBE SER LLAMADA EXPRESAMENTE PARA PODERLA UTILIZAR/MODIFICAR
# =============================================================================
class Peoplelist:
    
    def __init__(self):
        self.persons = []
    
    def addp(self , p):
        self.persons.append(p)
        
    def showp(self):
        for i in self.persons:
            print(i)
    

# =============================================================================
x = input("Would you like to add (a) or read (r)?: \n>> ")

while True:
    if x == "q":
        print("\t--Process finished by user--")
        del x
        break

    if x== "r":
        try:
            with open("People_info" , "rb") as pickledfile:
                unpickled = pickle.load(pickledfile)
            
            for i in unpickled:
                print(i)
            del unpickled
            x = input("Would you like to add (a), read (r) or quit (q)?: \n>> ")
        except:
            print("\t--File doesn't exist, you should create one first--")
            x = input("Would you like to add (a), read (r) or quit (q)?: \n>> ")
        
    elif x== "a":
        lst = Peoplelist()
        p = Person(input("Name: "), input("Country: "), int(input("Age: ")))

        try:
            with open("People_info" , "rb") as reading2update:
                lst.persons = pickle.load(reading2update)
                lst.addp(p)
        except:
            lst.addp(p)
        
        finally:
            lst.showp()
        
        with open("People_info" , "wb") as file:
            pickle.dump(lst.persons, file)
            # del lst
            
        print("Pickling process succesfully finished")
        x = input("Would you like to add (a), read (r) or quit (q)?: \n>> ")
    
    else:
        print("\t--You must select a valid option (a, r or q--")
        x = input("Would you like to add (a), read (r) or quit (q)?: \n>> ")

print("\n** THIS IS THE END **")



