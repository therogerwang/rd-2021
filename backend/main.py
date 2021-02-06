import sqlite3
import data.database as db
import os

conn = sqlite3.connect("../data/storage.db")
c = conn.cursor()


def recommend(business_name):
    
    
    similar_business_list = get_similar_businesses(business_name)
    
    vendors = get_vendors_set(similar_business_list)
    
    vendors = filter_vendors_set(business_name,vendors)
    

    
    return vendors




def get_similar_businesses(business_name):
    
    return db.get_top_x_most_similar_agency(business_name, 5, c)

def get_vendors_set(similar_businesses_list):
    
    vendors = set([])
    
    for business_name in similar_businesses_list:
        ven_list = db.get_vendors_of_single_agency(business_name, c)
        for vendor_name in ven_list:
            vendors.add(vendor_name)
    
    return vendors


def filter_vendors_set(business_name, vendor_set):
    already_interacting = db.get_vendors_of_single_agency(business_name, c)
    
    output = vendor_set.difference(set(already_interacting))
    
    return list(output)


print(recommend("Fire & Emergency Medical Services"))