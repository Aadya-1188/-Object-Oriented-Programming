#create class
class Employee:

        #Initialising
        def __init__(self):
            print("Employee created")

        #calling destructor
        def __delf__(self):
              print("destructor called")

def Create_Obj():
      print("Making Object...")
      obj = Employee()
      print("function end...")
      return obj()

print("Calling Created_obj() function...")
obj = Create_Obj
print("Program End...")