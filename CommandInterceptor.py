import sys
from Types import *
from EntityCreators.CS_POCO_Creator import populateCSEntities
from Patterns import *




def main():
    commands = []
    last_seen_entity = ""
    for _,arg in enumerate(sys.argv[1:]):


        classification_result = is_entity(arg)
        if classification_result:
            entity_name,parent = classification_result
            commands.append(Entity(entity_name,parent))
            last_seen_entity = entity_name

        elif last_seen_entity == "":
            raise SyntaxError(f"ensure first argument should be an entity,error at {arg}")
        

        classification_result = is_attribute(arg)
        if classification_result:
            attribute_name,attribute_type = classification_result
            if attribute_type not in type_mapping:
                raise RuntimeError(f"the type {attribute_type} is not supported at the moment")

            commands.append(Attribute(attribute_name,attribute_type,last_seen_entity))    
        else:
            RuntimeError(f"we don't support this yet, error at {arg}")     
    populateCSEntities(commands)


                    
if __name__ == "__main__":
    main()