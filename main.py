import sys

print(sys.version)


def process(a,b):
  return a+b,a*b

x=5
y=7
print(x,y)
print(process(x,y))
#Rindā 1 – tiek ielādēta bibliotēka sys (mēs šo bibliotēku izmantosim izmantotās
# Python versijas noskaidrošanai).
#  Rindā 3 – tiek iegūta un izdrukāta Python versija, ar kuru strādājam (3.8.0).
#  Rindās 5,6 – tiek ielādēta (un nevis izpildīta) funkcija process.
#  Rindās 8,9,11 – tiek definēti un izdrukāti mainīgie x,y (5,7).
#  Rindā 13 tiek izsaukta funkcija process un izdrukāts, ko tā atgriež (skaitļu 5 un 7
# summu 12 un reizinājumu 35)