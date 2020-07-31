# Program to validate Diffie Hellman Maths
print("This program calculates the public keys and shared secret for Diffie Hellman:")
N = int(input("Enter the common prime:")) # No validations on inputs
g = int(input("Enter the primitive root:"))
private_a = int(input("Enter Alice's private key:"))
private_b = int(input("Enter Bob's private key:"))
public_a = (g**private_a)%N
public_b = (g**private_b)%N
shared_key_one = (public_b**private_a)%N
shared_key_two = (public_a**private_b)%N
if shared_key_one != shared_key_two:
    print("There has been an error, the program will exit")
    exit()
else:
    print("The public key of Alice is:",public_a)
    print("The public key of Bob is:",public_b)
    print("The shared secret is:",shared_key_one)
input("Press any key to exit:")
exit()
