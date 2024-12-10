import re

#check weither an argument is of type Entity
entity_pattern = r"^(\w+)(?:->(\w+))?$"
def is_entity(argument:str):
        entity = re.match(entity_pattern,argument)
        if entity:
            return entity.group(1),entity.group(2)  
        else:
            return None



#check weither an argument is of type Attribute
attribute_pattern = r"^(\w+):(\w+)$"
def is_attribute(argument:str):
    attribute = re.match(attribute_pattern,argument)
    if attribute:
        return attribute.group(1),attribute.group(2)
    else:
        return None

