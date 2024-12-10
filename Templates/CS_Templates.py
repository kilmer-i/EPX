        # Base template with placeholders
class_template = """
using System;

namespace project_name.Models.entities
{{
    public class {class_name} {inheritance}
    {{
        {properties}
    }}
}}
"""


property_template= """
        public {type} {property_name} {{get;set;}} 
"""

#foreign key template 
fk_template="""
        public int {property_name}Id {{get;set}}
        public {property_name} {property_name} {{get;set}}
"""

#list template 
list_template="""
        public ICollection<{property_name}> {property_name}s {{get;set;}} 
"""