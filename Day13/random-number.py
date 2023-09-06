import random

random_num = random.randrange(1000,9999)

user_input = int(input('Enter your OTP : '))

print("OTP is MATCHED!...") if random_num == user_input else print(f"OTP is NOT MATCHED!... OTP was {random_num}")