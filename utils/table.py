# Your code here
class Seat:
    """
    Represents a single seat in the office.
    A seat can be occupied or free.
    """
    def __init__(self, free=True, occupant=None ):
        # A seat starts free and empty

        self.free = free
        self.occupant = occupant
    def set_occupant(self, name ):
        if self.free == True:
            #we will assign an occupant to a seat 
            # we MUST update BOTH occupant AND free

            self.occupant = name
            self.free = False
        else:
          print("This seat is already occupied")
    def remove_occupant(self):  
          # removes person and frees seat
          if self.free == False:
            previous = self.occupant
            self.free = True
            self.occupant = None
            return previous

    
    def __str__(self) -> str:
        if self.occupant:
           return self.occupant
        return "Empty"
 

# Your code here
class Table:
    """
    Represents a table containing multiple seats.
    """
    def __init__ (self, capacity) :
        # capacity = number of seats per table
       self.capacity = capacity
        # We create an empty list that will contain ALL seats of this table
        # IMPORTANT IDEA:
        # This is NOT a list of numbers — it is a list of OBJECTS (Seat instances)
       self.seats = []
       # We loop "capacity" times because:
       # capacity = number of seats this table should have
       # Example: capacity = 4 → we create 4 Seat objects
       for i in range(capacity):
           # Each iteration creates ONE Seat object
           # Seat() = a real seat with:
           # - free = True (available)
           # - occupant = None (empty)
           self.seats.append( Seat())

        
    def has_free_spot(self):
    # PURPOSE:
    # Check if this table still has at least ONE empty seat


    # We don't check numbers, we check EACH Seat object state
     for seat  in self.seats :
        if seat.free == True:
            return True 
     return False 
    
        
    def assign_seat(self, name):
        # PURPOSE:
        # Put a person in the FIRST available seat

        for seat in self.seats:
          if seat.free == True:
             seat.set_occupant(name)
             return 
        print("No free seats available")
        
    def left_capacity(self):
       #PURPOSE: Count how many seats are still free
       counter = 0

       for seat in self.seats:
        if seat.free == True:
          counter= counter+1

       return counter
        
   

    def __str__(self) -> str:
        seats_str = []

        for seat in self.seats:
            seats_str.append(str(seat))

        return " | ".join(seats_str)

    

