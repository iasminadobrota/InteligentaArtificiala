#Scrieti un program pentru a extrage
# anul, luna, data si ora folosind Lambda.
# ex: 2023-04-24 09:03:32.744178
# 2023
# 04
# 24
# 09:03:32.744178

data = "2004-08-22 09:03:32.744178"

an=lambda x: x.split("-") [0]
luna=lambda x: x.split("-") [1]
zi=lambda x: x.split("-") [2].split(" ")[0]
ora=lambda x: x.split(" ")[1]

print("AN:",an(data))
print("LUNA:",luna(data))
print("DATA:",zi(data))
print("ORA:",ora(data))
