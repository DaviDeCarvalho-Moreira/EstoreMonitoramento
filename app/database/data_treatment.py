import regex as re

def price_float(value):
    
    clean_value = re.sub(r'[^\d,\.]', '', value)
    
    float_value =  clean_value.replace('.','').replace(',','.')
    
    
    return float(float_value)
    


    
    