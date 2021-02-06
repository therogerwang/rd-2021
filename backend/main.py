import sqlite3
import data.database as db
import os

conn = sqlite3.connect("../data/storage.db")
c = conn.cursor()


def recommend(business_name):
    
    
    similar_business_list = get_similar_businesses(business_name)
    
    vendors = get_vendors_set(business_name, similar_business_list)
    
    # vendors = filter_vendors_set(business_name,vendors)
    

    
    return vendors




def get_similar_businesses(business_name):
    
    return db.get_top_x_most_similar_agency(business_name, 5, c)

def get_vendors_set(business_name, similar_businesses_list):
    
    freq = {}
    num_vendors_to_output = 10
    # vendors = set([])
    already_interacting = db.get_vendors_of_single_agency(business_name, c)
    
    for business_name in similar_businesses_list:
        ven_list = db.get_vendors_of_single_agency(business_name, c)
        for vendor_name in ven_list:
            
            #get freq of vendors
            if vendor_name in already_interacting:
                continue
            
            if vendor_name in freq:
                freq[vendor_name] += 1
            else:
                freq[vendor_name] = 1
            
            # vendors.add(vendor_name)
    
    #get top 20 most frequent vendors
    sorted_list = sorted(freq.items(), key=lambda item: item[1])
    
    if len(sorted_list) <= num_vendors_to_output:
        return [x[0] for x in sorted_list]
        
    else:
        return [x[0] for x in sorted_list[-1*num_vendors_to_output:]]



# def filter_vendors_set(business_name, vendor_set):
#     already_interacting = db.get_vendors_of_single_agency(business_name, c)
#
#     output = vendor_set.difference(set(already_interacting))
#
#     print("vendor set")
#     print(vendor_set)
#     print("already interacting")
#     print(already_interacting)
#     return list(output)


#print(recommend("Fire & Emergency Medical Services"))