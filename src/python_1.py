def camel_snake(s):
    lower=""
    for i in s:
        if(i.isupper()):
            lower +="_"+i.lower()
        else:
            lower+=i
    return lower[1:]
s = "KuldeepManagoli"
print(camel_snake(s))