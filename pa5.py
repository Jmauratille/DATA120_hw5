def gcd(a,b):       
    if b == 0:               
        return a       
    return gcd(b, a%b)
def remove_pairs(s):       
    if len(s) == 1:       
        return s       
    direction_dict = {"S": "N", "E": "W", "N": "S", "W": "E"}        
    if direction_dict[s[0]] == s[1]:               
        if len(s) == 2:                        
            return ""                
        else:                        
            return remove_pairs(s[2:])       
    else:                
        print(s[0])                
        return s[0] + remove_pairs(s[1:])        
def bisection_root(func, a, b):        
    if func(a) > 0 and func(b) < 0:               
        lower = b                
        upper = a        
    elif func(a) < 0 and func(b) > 0:                
        lower = a                
        upper = b        
    else:                
        raise ValueError 
    if abs(func(lower)) < 0.0000000001:               
        return lower       
    elif abs(func(upper)) < 0.0000000001:                
        return upper       
    else:               
        midway = (lower+upper)/2  
        mid = func(midway)               
        if mid > 0:                       
            return bisection_root(func, lower, midway)     
        elif mid < 0:                        
            return bisection_root(func, midway, upper) 
        else:
            return midway
