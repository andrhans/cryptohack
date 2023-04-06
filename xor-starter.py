
string="label"
result= ""

for x in string:
    result+=chr(ord(x)^13)
    
print(f"crypto{{{result}}}")
