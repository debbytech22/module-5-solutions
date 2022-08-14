import sqlite3
import csv
conn = sqlite3.connect("stud_waec_info.db")
c = conn.cursor()
# My_table = """
# CREATE TABLE Stud_waec_grade(
# STUDENT_NO TEXT,
# NAMES TEXT,
# MATHEMATICS INTEGER,
# ENGLISH INTEGER,
# PHYSICS INTEGERS,
# CHEMISTRY INTEGER,
# BIOLOGY INTEGER,
# ECONOMICS INTEGER,
# AGRIC INTEGER,
# GEOGRAPHY INTEGER
# )
# """
# c.execute(My_table)
with open('WAEC DATA.csv','r') as waec_file:
    read_file =csv.reader(waec_file)
    next(read_file)
    c.executemany("INSERT INTO Stud_waec_grade  VALUES (?,?,?,?,?,?,?,?,?,?)",read_file)
print("table created successfully")
conn.commit()
conn.close()

