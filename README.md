````md
# challenge-openspace-classifier


---

## 🏢 Description

The OpenSpace Organizer is a Python program that randomly assigns colleagues to available seats in an open-space office environment.

The office contains:

- 6 tables
- 4 seats per table
- Total: 24 seats

Each time the program runs, colleagues are randomly shuffled and assigned to different seats, encouraging collaboration and interaction between team members.

The final seating arrangement is:

- displayed in the terminal
- saved into a CSV output file



## 📦 Repo Structure

```text
.
├── utils/
│   ├── table.py
│   ├── openspace.py
│   └── file_utils.py
│
├── main.py
├── new_colleagues.csv
├── seating_output.csv
├── notebook_guide.ipynb
└── README.md
````

---

## ⚙️ How It Works

1. The program reads a list of colleagues from `new_colleagues.csv`
2. Names are cleaned and loaded into a Python list
3. The OpenSpace system creates 6 tables with 4 seats each
4. Colleagues are randomly shuffled
5. Each person is assigned to the first available seat
6. The final seating plan is:

   * displayed in the terminal
   * saved to `seating_output.csv`

---

## 🚀 Usage

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd challenge-openspace-classifier
```

### 2. Run the Program

```bash
python main.py
```

---

## 📥 Input File Example

The `new_colleagues.csv` file must contain one name per line:

```text
Anna
Dan
Gaetan
Guillermo
Gunay
Hiba
Hussein
Ibrahim
Ibtihel
Imad
Iness
Irene
Jeong
Mahalakshmi
Max
Neha
Siegried
Sitara
Sooyoung
Stephane
Thi
Uzair
Victor
Vanessa
```

---

## 📤 Output Example

```text
Table 1
Anna | Dan | Max | Hiba

Table 2
Victor | Neha | Irene | Gaetan
```

The result is also saved in:

```text
seating_output.csv
```

---

## 🧱 Main Features

* Random seat assignment
* Multiple tables support
* CSV file reading
* Seating plan export
* Object-Oriented Programming structure
* Clean modular project organization

---

## 📌 OOP Structure

This project uses three main classes:

* `Seat` → represents one seat
* `Table` → manages several seats
* `OpenSpace` → manages all tables and seating organization

Each class contains:

* type hints
* docstrings
* comments
* `__str__()` methods

---

## ⏱️ Timeline

This project took 2 days to complete.

---

## 📌 Personal Situation

This project was completed as part of a Python and Object-Oriented Programming learning exercise.

The objective was to practice:

* OOP principles
* modular Python architecture
* file handling
* clean code structure
* imports and project organization

---

## 👤 Author

Project developed by **Ibtihel Katar**.

Connect with me on LinkedIn:

https://www.linkedin.com/in/ibtihel-katar/

```
```
