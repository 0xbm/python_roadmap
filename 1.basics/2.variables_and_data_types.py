print("""
Variables:
    A variable can have a short name (like x and y) or a more descriptive name 
    (age, carname, total_volume). 
      
    Rules for Python variables:
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores 
    (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different 
    variables)
    A variable name cannot be any of the Python keywords. 
      
    Ex.
    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"  
      
Variables ex.:
    multiple variables:
        x = "Python"
        y = "is"
        z = "awesome"
        print(x, y, z)
        
    global variables:
        x = "awesome"
        def myfunc():
          global x
          x = "fantastic"

        myfunc()
        print("Python is " + x)
        
        OR
        
        x = 15
        def change():
            global x
            x = x + 5
            print("Value of x inside a function :", x)
        
        change()
        print("Value of x outside a function :", x)
     
    private variables:
    two underscores in the beginning variable : __private_var = value
    easier in class
    
Data Types:
    Text Type:        str 
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	    dict
    Set Types:	    set, frozenset
    Boolean Type:	    bool
    Binary Types:	    bytes, bytearray, memoryview
    None Type:	    NoneType
""")
