d = int(input("Enter your decryption (private d) key: "))
N = int(input("Enter your N needed for translation: "))

message = int(input("Enter your message in ASCII: "))

result = message**d%N

print("------------------")

print("Your decrypted message: \n" + str(result))

print("------------------")