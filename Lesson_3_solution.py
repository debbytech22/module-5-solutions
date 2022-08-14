import sqlite3
conn=sqlite3.connect("Stationary_inventt.db")
c = conn.cursor()
print(" database successful")
#using drop table to avoid duplicate copy
c.execute("DROP TABLE  IF EXISTS Stationery_stock")
c.execute("""
CREATE TABLE Stationery_stock(
ITEM_ID INTEGER,
ITEMS TEXT,
COST_PRICE INTEGER,
QUANTITY_IN_STOCK INTEGER
)
""")
print("table created successfully")
Avail_items = [
(1,"2b 60 leaves bks",600,10),
(2,"Staple pin",800,5),
(3,"Gum",1000,15),
(4,"Pencils",500,30),
(5,"A4 paper",5000,7),
(6,"Flexible Ruler",1500,22),
(7,"set square",4000,5),
(8,"Math set",2500,3),
(9,"Eraser",750,8),
(10,"Calculator",3000,10)
]
c.executemany("INSERT INTO Stationery_stock VALUES(?,?,?,?)",Avail_items)
#amount the business owner invested in the procurement of the items.
c.execute("SELECT SUM(COST_PRICE) FROM Stationery_stock" )
print(c.fetchall())
# average quantity of items in stock.
c.execute("SELECT AVG(QUANTITY_IN_STOCK) FROM Stationery_stock")
print(c.fetchall())
#item with the least quantity in stock
c.execute("SELECT ITEMS, MIN(QUANTITY_IN_STOCK) FROM Stationery_stock")
print(c.fetchall())
# item with the most quantity in stock
c.execute("SELECT ITEMS,MAX(QUANTITY_IN_STOCK) FROM Stationery_stock")
print(c.fetchall())

conn.commit()
conn.close()










