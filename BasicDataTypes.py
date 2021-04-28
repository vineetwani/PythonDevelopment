""" Global Variables
    Python Data Types
    Type Conversion
"""

x="Global X"
y="Global Y"

def checkGlobal():
    x="Local X"
    
    global y
    y="Modified Global"
    
    
#Function: checkDataTypes
#Output:
#  <class 'str'>
#  <class 'float'>
#  <class 'bool'>
#  <class 'list'>
#  <class 'tuple'>
#  <class 'dict'>

def checkDataTypes():
    #str
    z="Type Check"
    print(type(z))
    
    #float
    x = 20.5
    print(type(x))
    
    #bool
    k = True
    print(type(k))

    #list
    l1 = ["apple", "banana", "cherry"]
    print(type(l1))
    
    #tuple
    t1=("apple", "banana", "cherry")
    print(type(t1))
    
    #dict
    d1={47:"Vineet", 19:"Punit", 25:"Vicky"}
    #for i,j in d1.items():
        #print(i,j)

    print(type(d1))


def typeConversion():
    x=5
    #convert x into a floating point number
    x=float(x)
    
    #convert y into a int 
    y=5.5
    y=int(x)
    
    z=25
    #convert z into a complex number.
    z=complex(z)
    
if __name__ == "__main__":
    #checkGlobal()
    #print(x)
    #print(y)
    
    checkDataTypes()