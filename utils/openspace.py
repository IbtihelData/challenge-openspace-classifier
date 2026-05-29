import random
from utils.table import Table
class OpenSpace :
    """
    Represents the full office containing multiple tables.
    Handles seating organization.
    """
    def __init__(self,  number_of_tables):
        
        self.number_of_tables = number_of_tables
        
        # We store all Table objects in a list
        self.tables = []
        # IMPORTANT CONCEPT:
        # We create tables automatically here
        # Each table has FIXED capacity = 4 seats
        for i in range(number_of_tables):
            self.tables.append(Table(4))

   
    def organize (self, names ):
       # PURPOSE:
        # Randomly distribute people into seats

        # STEP 1: shuffle names
        # This ensures random distribution every time
       

       random.shuffle(names)
       for name in names:               # STEP 2: assign each person one by one
          for table in self.tables:                   # STEP 3: find a table with a free seat
             if table.has_free_spot():
                table.assign_seat(name)
                 
                break                                   # VERY IMPORTANT:
                                                        # Stop after assigning ONE seat per person
                                                        # (otherwise same person could be placed multiple times)
    """def display(self):
        for index, table in enumerate(self.tables):
            print(f"Table {index+1}")                       # +1 because humans don't use index 0
            for seat in table.seats:
                print(seat.occupant)"""
    def display(self):
        print(self)
    def store(self, filename):
        with open(filename, "w") as file:                        # 'w' mode = write (overwrite file if it exists)

           for index, table in enumerate(self.tables):
             file.write(f"Table {index+1}\n")
             for seat in table.seats:                              # write all seats in this table
                file.write(str(seat.occupant) + "\n")

             file.write("\n")                                      # empty line between tables for readability


    def __str__(self) -> str:
     result = "OpenSpace:\n"

     for i, table in enumerate(self.tables):
        result += f"Table {i + 1}: {table}\n"

     return result