import sqlite3
import csv

# conn = sqlite3.connect('example.db')
#
# c = conn.cursor()
def run_me():
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()


    # build_init_table_from_csv(c)
    # conn.commit()

    results = c.execute('SELECT * FROM transactions WHERE AGENCY = "Department of Motor Vehicles" LIMIT 50')
    for row in results:
        print(row)
    
    conn.close()




def build_init_table_from_csv(connection_cursor):
    

    with open('Purchase_Card_Transactions.csv','r') as fin: # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
    
        db_rows = [(
            row['ï»¿OBJECTID'],
            row['AGENCY'],
            row['TRANSACTION_DATE'],
            row['TRANSACTION_AMOUNT'],
            row['VENDOR_NAME'],
            row['VENDOR_STATE_PROVINCE'],
            row['MCC_DESCRIPTION']) for row in dr]
    
    #create table
    connection_cursor.execute('''CREATE TABLE transactions
             (OBJECTID int, AGENCY text, TRANSACTION_DATE text, TRANSACTION_AMOUNT real, VENDOR_NAME text,
              VENDOR_STATE_PROVINCE text, MCC_DESCRIPTION text)''')
    
    #insert into table
    connection_cursor.executemany("INSERT INTO transactions (OBJECTID,AGENCY,TRANSACTION_DATE,TRANSACTION_AMOUNT,VENDOR_NAME,VENDOR_STATE_PROVINCE,MCC_DESCRIPTION) VALUES (?,?,?,?,?,?,?);", db_rows)

# Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
# # Save (commit) the changes
# conn.commit()
#
#
# t = ('RHAT',)
# c.execute('SELECT * FROM stocks WHERE symbol=?', t)
# print(c.fetchone())
#
# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()

run_me()