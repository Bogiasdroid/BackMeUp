import sqlite3

def make_db():
    con = sqlite3.connect("Paths.db")
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Paths
             ( Fromm text not null, Tooo text not null)''')
    con.commit()


def insert(x,y):
    con = sqlite3.connect("Paths.db")
    SQLinsertfb = '''INSERT INTO Paths (Fromm,Tooo) VALUES(?,?)'''
    c = con.cursor()
    c.execute(SQLinsertfb, (x,y))
    con.commit()

def get_last_element():
    Sqlmaxid='''SELECT Fromm,Tooo FROM Paths WHERE rowid=(SELECT MAX(rowid) FROM Paths)'''
    con = sqlite3.connect("Paths.db")
    c=con.cursor()
    returned=c.execute(Sqlmaxid)
    returned=[list(elem) for elem in returned]
    con.commit()
    return returned
