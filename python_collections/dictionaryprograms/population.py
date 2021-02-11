population={"ind":100,"china":200,"nz":10,"wi":40,"aus":35}
data=sorted(population,key=population.get)
print(data)
population["russia"]=190
print(population)
print(data)
