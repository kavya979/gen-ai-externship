d={"name":"Kavya","age":22,"city": "Dallas"}
d["favourite color"] = "Mauve"
d["city"] = "Chennai"
k=[]
v=[]
for i in d:
    k.append(i)
for j in d.values():
    v.append(j)
d1 = ", ".join(k)
d2 = ", ".join(str(k) for k in v)
print("Key: ",d1,"\nValue: ",d2)