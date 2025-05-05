def is_obj_has_attr(sm_class, sm_attr):
    return hasattr(sm_class,sm_attr)



class Duck:
    weight = 5
    height = 10
    
print(is_obj_has_attr(Duck, 'weight'))
print(is_obj_has_attr(Duck, 'name'))
print(is_obj_has_attr(Duck, 'height'))