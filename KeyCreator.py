# This program goes through the RSA algorithm to generate valid keys

p = int(input("Select a prime number for p: "))
q = int(input("Select a different prime number for q: "))
N = p * q

print("------------------")

print("p = " + str(p))
print("q = " + str(q))
print("N " + str(N))

Φ  = (p-1) * (q-1)
print("Φ = " + str(Φ))

print("------------------")

# Find e such that:
# 1. 1<e<Φ 
# 2. coprime with both N & Φ //13 for 60 and 77

# all factors of N and Φ 
allFactors = []
for i in range(2, N):
    if N % i == 0:
        allFactors.append(i)

for i in range(2, Φ):
    if Φ % i == 0:
        allFactors.append(i)

# print all numbers that are in not in list up to Φ
invalidE = []
for i in range(2, Φ): #loop through all numbers from 2 to Φ
    for factor in allFactors: #add to list if it cannot be divided by any number in allFactors
        if i % factor == 0: 
            invalidE.append(i)
            break

validE = []
for i in range(2, Φ):
    if i not in invalidE: #remove all invalid numbers from possible numbers list
        validE.append(i)

print(validE)

e = int(input("Enter your choice of e from all possible listed above: "))

print("------------------")

#Find d such that:
#e * d % Φ = 1
largeNumberForD = 100
possibleD = []
for i in range (1, largeNumberForD):
    if e * i % Φ == 1:
        possibleD.append(i)

print(possibleD)
d = int(input("Enter your choice of d from all possible listed above: "))

print("------------------")

print("Your encryption (public e) key = " + str(e))
print("Your private (private d) key = " + str(d))

print("------------------")