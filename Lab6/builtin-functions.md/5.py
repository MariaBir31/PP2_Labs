def all_elements_true(t):
    return all(t)  

print(all_elements_true((True, True, True))) 
print(all_elements_true((True, False, True)))  
print(all_elements_true((1, 2, 3)))             
print(all_elements_true((1, 0, 3)))            
