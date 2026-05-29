from utils.table import Seat
from utils.table import Table
from utils.openspace import OpenSpace
from utils.file_utils import read_names_from_csv


names = read_names_from_csv("new_colleagues.csv")

openspace1 = OpenSpace(6)

openspace1.organize(names)

openspace1.display()

openspace1.store("seating_output.csv")

   



