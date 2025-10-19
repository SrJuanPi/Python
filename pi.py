for i in range(1, 10001):
    print(i)
    i += 1
    
# test 3.14 aprox 2s

# t-strs

from string.templatelib import Interpolation

def lower_upper(template):
    parts = []
    for part in template:
        if isinstance(part, Interpolation):
            parts.append(str(part.value).upper())  # variables en MAYÚSCULAS
        else:
            parts.append(part.lower())            # texto en minúsculas
    return "".join(parts)

name = "katty"
tpl = t"hola me llamo {name}."
print(lower_upper(tpl))
# → "mister WENSLYDALE"

