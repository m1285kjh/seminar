__author__ = 'kjh12'

p =(4, 5)
x, y = p

print p
print x
print y

with open('kjh12','rt') as f:
  data = f.read()
  print data

if False:
    print 'hello1'
print 'hello2'

rng = range(1, 11)

print 'rng=', rng

num=[1,2,3,4,5,6,7,8,9,10]
m = 0
l = 0
for k in rng :

    m = k + m
    l += k
    print m
    print l