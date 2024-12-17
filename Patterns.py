import re

entity_pattern = r"^(\w+)(?:->(\w+))?$"
def is_entity(argument:str):
        entity = re.match(entity_pattern,argument)
        if entity:
            return entity.group(1),entity.group(2)  
        else:
            return None



attribute_pattern = r"^(\w+):(\w+)$"
def is_attribute(argument:str):
    attribute = re.match(attribute_pattern,argument)
    if attribute:
        return attribute.group(1),attribute.group(2)
    else:
        return None

