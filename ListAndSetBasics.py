#Define a list, set

#Output of Function listBasics: 
#   <class 'list'>
#   [['Punit', 79], ['Vineet', 66]]
#   ['Punit', 'Vineet']
#   [79, 66]
def listBasics():
    
    #l1=list()  Can define like this as well
    l1=[]
    
    print(type(l1))
    
    l1.insert(0,["Vineet",66])
    l1.insert(0,["Punit",79])
    
    #l1=[["Vineet",66],["Punit",79]]
    
    print(l1)
    print([name for name,marks in l1])
    print([marks for name,marks in l1])

#Output of Function setBasics: 
#   <class 'dict'>
#   <class 'set'>
#   <class 'set'>
#   {44, 22}

def setBasics():

    #Empty curly braces {} will make an empty dictionary in Python.     
    s={}
    print(type(s))

    s1={ 13 , 12 }
    print(type(s1))
    
    #To make a set without any elements, we use the set() function without any argument.
    s2=set()
    print(type(s2))
    
    #Sets are mutable. However, since they are unordered, indexing has no meaning.
    s2.add(22)
    s2.add(44)
    s2.add(22)
    
    print(s2)

if __name__ == "__main__":
    #listBasics()
    setBasics()