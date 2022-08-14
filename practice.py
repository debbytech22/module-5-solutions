import sqlite3
conn = sqlite3.connect("stud_waec_info.db")
c = conn.cursor()


# c.execute("ALTER TABLE Stud_waec_grade ADD COLUMN TOTAL INTEGER")
# print("success")


# c.execute("""UPDATE Stud_waec_grade
# SET Total =  'sum'
# """)
print("secc")
c.execute ("""SELECT NAMES, SUM(ENGLISH + MATHEMATICS + PHYSICS + CHEMISTRY + BIOLOGY + ECONOMICS + AGRIC + GEOGRAPHY)/2 AS 'sum'
FROM  Stud_waec_grade
GROUP BY NAMES
""")
item = c.fetchall()
print(item)
conn.commit()