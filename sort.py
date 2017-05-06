li=[45,123,456,7,9]
for n in range(1,len(li)):
    for i in range(len(li)-n):
        if li[i]> li[i+1]:
            temp=li[i]
            li[i]=li[i+1]
            li[i+1]=temp
print(li)
