import sqlite3
conn = sqlite3.connect("stud_waec_info.db")
c = conn.cursor()

#student with highest in Math
def max_in_math():
    query= "SELECT NAMES,MAX(MATHEMATICS) FROM Stud_waec_grade"
    c.execute(query)
    students=c.fetchall()
    print(f"NAME\t\t\t BEST_IN_MATH\n {'.'*50}")
    for i in students:
        NAMES,MATHEMATICS= i 
        print(f"{NAMES}\t\t{MATHEMATICS}")    
max_in_math()


#student with  lowest in English
def min_in_eng():
    query= "SELECT NAMES,MIN(ENGLISH) FROM Stud_waec_grade"
    c.execute(query)
    students=c.fetchall()
    print(f"NAME\t\t\t LOWEST IN ENGLISH\n {'.'*50}")
    for i in students:
        NAMES,ENGLISH= i 
        print(f"{NAMES}\t\t{ENGLISH}")
min_in_eng()


#Average score of students in math
def avg_score_math():
    query= "SELECT AVG(MATHEMATICS) FROM Stud_waec_grade"
    c.execute(query)
    item = c.fetchall()
    print(f"AVERAGE MATH SCORE IS {item}")
avg_score_math()

#Average score of students in english
def avg_score_eng():
    query= "SELECT AVG(ENGLISH) FROM Stud_waec_grade"
    c.execute(query)
    item = c.fetchall()
    print(f"AVERAGE ENGLISH SCORE IS {item}")
avg_score_eng()

#best performing student across all nine subjects in terms of overall scores

c.execute("""SELECT NAMES, MAX(sum)/2 FROM(
SELECT NAMES, SUM(ENGLISH + MATHEMATICS + PHYSICS + CHEMISTRY + BIOLOGY + ECONOMICS + AGRIC + GEOGRAPHY)/2 AS 'sum'
FROM  Stud_waec_grade
GROUP BY NAMES)
""")
item = c.fetchall()
print(item)



#best performing student across all nine subjects in term of average scores

c.execute("""SELECT NAMES, AVG(sum)/2 FROM(
SELECT NAMES, SUM(ENGLISH + MATHEMATICS + PHYSICS + CHEMISTRY + BIOLOGY + ECONOMICS + AGRIC + GEOGRAPHY)/2 AS 'sum'
FROM  Stud_waec_grade
GROUP BY NAMES)
""")
item = c.fetchall()
print(item)
conn.commit()
conn.close()

