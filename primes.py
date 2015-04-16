from datetime import datetime
start = datetime.now()
primes = [2]
for n in range (3, 10001):
  for p in primes[:len(primes)/2]:
    rem = n%p
    if rem == 0:
      break
    else:
      primes += [n]
print len(primes)
print datetime.now() - start