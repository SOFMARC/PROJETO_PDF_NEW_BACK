import re

def get_value(expression, text):
    value = ""

    ref_value = re.compile(f"{expression}")

    value = ref_value.search(text)
    
    return value.group()