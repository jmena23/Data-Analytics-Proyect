import re

def neighborhood(x):
    res = re.findall(r"Neighborhood\s\d+", x)
    if res:
        return res[0]
    else:
        return x

def barrio(x):
    res = re.findall(r":\s.*\s[(]", x)
    if res:
        return res[0][2:-2]
    else:
        return x

def house_type(x):
    res = re.findall(r":.*", x)
    if res:
        return res[0][2:]
    else:
        return x

def euro_m2(x):
    res = re.findall(r"\d+\.\d+", x)
    if res:
        return res[0]
    else:
        return x

def n_distrito(x):
    res = re.findall(r"District\s\d+", x)
    if res:
        return res[0]
    else:
        return x

