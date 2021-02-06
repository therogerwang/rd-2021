import sqlite3
import data.database as db
import os

conn = sqlite3.connect("../data/storage.db")
c = conn.cursor()


def recommend(business_name):
    
    
    similar_business_list = get_similar_businesses(business_name)
    
    vendors = get_vendors_set(similar_business_list)
    
    vendors = filter_vendors_set(vendors)
    

    
    return ["YOHOHO", "YONONON2"]




def get_similar_businesses(business_name):
    
    
    return []

def get_vendors_set(similar_businesses_list):
    
    vendors = set([])
    
    for business_name in similar_businesses_list:
        ven_list = db.get_vendors_of_single_agency(business_name, c)
        for vendor_name in ven_list:
            vendors.add(vendor_name)
    
    return vendors


def filter_vendors_set(vendor_set):
    pass


get_vendors_set(["Fire & Emergency Medical Services"])