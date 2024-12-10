from pathlib import Path
import os
from Types import Entity,Attribute,type_mapping,AttributeInfo
from Templates.CS_Templates import fk_template,class_template,list_template,property_template



models_path = Path("./Models")
if not models_path.is_dir():
    models_path.mkdir()
entities_path = models_path.joinpath("entities")
if not entities_path.is_dir():
    entities_path.mkdir()

os.chdir(entities_path)

def add_attribute_to_class(command,properties):
            properties[command.for_entity] = properties.get(command.for_entity,"") +globals().\
                get(f"{type_mapping[command.type].type}_template").\
                format(property_name=command.name,type=type_mapping[command.type].specific_type)
            

def add_entity_and_its_inherent(command,inheritance):
     inheritance[command.name] = inheritance.get(command.name, "") or command.inherits_from


def populateCSEntities(commands:str):
    properties = {}
    inheritance = {}
    for _,command in enumerate(commands):
        if isinstance(command,Entity):
            add_entity_and_its_inherent(command,inheritance)
        elif isinstance(command,Attribute):
            add_attribute_to_class(command,properties)
    for key in properties.keys():
        with open(key+".cs",'w') as entity_file:
                entity_file.write(class_template.\
                    format(class_name=key,
                           inheritance=f" : {parent}" if (parent := inheritance.get(key)) else "",
                           properties=properties[key]))



                    