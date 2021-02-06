import sqlite3
import csv
import numpy as np
import pandas as pd

# conn = sqlite3.connect('example.db')
#
# c = conn.cursor()
def setup():
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    
    create_similarity_table(c, conn)
    
    conn.close()



def get_vendor_transactions_list(business_name : str, connection_cursor):
    results = connection_cursor.execute('SELECT * FROM transactions WHERE AGENCY = "{}"'.format(business_name))
    return list(results)


def get_vendors_of_single_agency(business_name : str, connection_cursor):
    results = connection_cursor.execute('SELECT DISTINCT VENDOR_NAME FROM transactions WHERE AGENCY = "{}"'.format(business_name))
    return list(results)

def get_all_agencies(connection_cursor):
    results = connection_cursor.execute('SELECT DISTINCT AGENCY from transactions')
    agency_list = [row[0] for row in results]
    return agency_list

def get_all_vendors(connection_cursor):
    results = connection_cursor.execute('SELECT DISTINCT VENDOR_NAME from transactions')
    vendor_list = [row[0] for row in results]
    return vendor_list

def create_similarity_table(connection_cursor, connection):
    connection_cursor.execute('''DROP TABLE similarity IF EXISTS''')
    connection_cursor.execute('''CREATE TABLE similarity
                 (AGENCY_1 text, AGENCY_2 text, similarity_val real)''')
    
    agencies = get_all_agencies(connection_cursor)
    vendors = get_all_vendors(connection_cursor)
    
    # map each agency and vendor to an arbitray index
    agency_id = {a:i for i,a in enumerate(agencies)}
    vendor_id = {v:i for i,v in enumerate(vendors)}
    
    # TODO: Test this 
    query = "SELECT AGENCY, VENDOR_NAME, COUNT(*) AS count, AVG(ABS(TRANSACTION_AMOUNT)) as avg_amount FROM transactions GROUP BY AGENCY, VENDOR_NAME"
    transactions = pd.read_sql_query(query, connection)
    
    # compare based on frequency 
    adj_mat = np.zeros((len(vendor_id), len(agency_id)))
    avg_mat = np.zeros((len(vendor_id), len(agency_id)))
    
    for i, t in transactions.iterrows():
        adj_mat[vendor_id[t['VENDOR_NAME']]][agency_id[t['AGENCY']]] = t['count']
        avg_mat[vendor_id[t['VENDOR_NAME']]][agency_id[t['AGENCY']]] = t['avg_amount']
    
    cos_sim = lambda x,y: np.dot(x, y)/(np.linalg.norm(x)*np.linalg.norm(y))
    
    # TODO: edit adj_mat
    
    for agency_1 in agencies:
        for agency_2 in agencies:
            # if agency_1 == agency_2:
            #     continue
            similarity_value = 0.5 * cos_sim(adj_mat[:,agency_id[agency_1]], adj_mat[:,agency_id[agency_2]]) 
            similarity_value += 0.5 * cos_sim(avg_mat[:,agency_id[agency_1]], avg_mat[:,agency_id[agency_2]]) 
            
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