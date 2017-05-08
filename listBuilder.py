print [x * x for x in range(1,9) if x %2==0]

print [m + n for n in 'hello' for m in 'world']

L=['Hello','Xiaoqi',5,2,0,'ni']
print [s.lower() for s in L if isinstance(s,str)]
