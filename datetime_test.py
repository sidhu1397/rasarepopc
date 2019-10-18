from datetime import  datetime

d=datetime.now()
print(d)

filename=d.strftime("%d-%m-%y_%H:%M:%S")
print(filename)