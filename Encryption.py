e = int(input("Enter your encryption (public e) key: "))
N = int(input("Enter your N needed for translation: "))

message = int(input("Enter your message in ASCII: "))

result = message**e%N

print("------------------")

print("Your encrypted message: \n" + str(result))

print("------------------")