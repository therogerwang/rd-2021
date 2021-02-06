import sqlite3
import csv

# conn = sqlite3.connect('example.db')
#
# c = conn.cursor()
def setup():
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()


    # build_init_table_from_csv(c)
    # conn.commit()

    vendor_list = get_all_vendors(c)
    print(vendor_list)
    
    conn.close()


def get_vendor_transactions_list(business_name : str, connection_cursor):
    results = connection_cursor.execute('SELECT * FROM transactions WHERE AGENCY = "{}"'.format(business_name))
    return list(results)

def get_all_agencies(connection_cursor):
    results = connection_cursor.execute('SELECT DISTINCT AGENCY from transactions')
    agency_list = [row[0] for row in results]
    return agency_list

def get_all_vendors(connection_cursor):
    results = connection_cursor.execute('SELECT DISTINCT VENDOR_NAME from transactions')
    vendor_list = [row[0] for row in results]
    return vendor_list

def create_similarity_table(similarity_func, connection_cursor):
    connection_cursor.execute('''CREATE TABLE similarity
                 (AGENCY_1 text, AGENCY_2 text, similarity_val real)''')
    
    agencies = get_all_agencies(connection_cursor)
    
    for agency_1 in agencies:
        for agency_2 in agencies:
            # if agency_1 == agency_2:
            #     continue
            
            similarity_value = similarity_func(agency_1, agency_2)
            connection_cursor.execute("INSERT INTO similarity VALUES ('{}', '{}', {})".format(agency_1, agency_2, similarity_value))
            
    


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


setup()