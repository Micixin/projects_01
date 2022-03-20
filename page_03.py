s = '8 (916) 651-23-43'
new_s = ''
for i in s:
    if i.isdigit() is True:
        new_s += i 
    else:
        pass
print(new_s)