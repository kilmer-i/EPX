class Entity:
    def __init__(self, name: str, inherits_from: str = None):
        """
        Constructor for the Entity class.

        :param name: The name of the entity.
        :param inherits_from: The name of the base entity this entity inherits from, if any.
        """
        self.name = name
        self.inherits_from = inherits_from  # Defaults to None if no inheritance is provided

    def __repr__(self):
        inherits_info = f" (inherits from {self.inherits_from})" if self.inherits_from else ""
        return f"Entity: {self.name}{inherits_info}"



class Attribute:
    def __init__(self,  name:str, type:str, for_entity:str):
        self.name = name
        self.for_entity = for_entity
        self.type = type

    def __repr__(self):
        return f"Attribute for {self.for_entity} name:{self.name} type:{self.type}"
    

class AttributeInfo:
    def __init__(self, specific_type,type="property"):
        self.specific_type = specific_type
        self.type = type


type_mapping = {
    "i": AttributeInfo("int"),
    "d": AttributeInfo("double"),
    "dd": AttributeInfo("DateTime"),
    "str": AttributeInfo("string"),
    "list": AttributeInfo("list","list"),
    "fk":AttributeInfo("fk","fk")
}


