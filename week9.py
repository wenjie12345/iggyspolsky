
def f(n): 
  if n == 0:
    return 1
  else:
    return n * (n-1)
n = 5

result = f(n)
print('the factorial is',n,':',result)
