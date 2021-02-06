def recommend(business_name):
    
    
    similar_business_list = get_similar_businesses(business_name)
    
    vendors = get_vendors_set(similar_business_list)
    
    vendors = filter_vendors_set(vendors)
    
    return ["YOHOHO", "YONONON2"]




def get_similar_businesses(business_name):
    
    
    return []

def get_vendors_set(similar_businesses_list):
    
    vendors = set([])
    
    for business in similar_businesses_list:
        #TODO get vendor list
        
        #vendors.add(vendor name)
    
    


def filter_vendors_set(vendor_set):
    pass