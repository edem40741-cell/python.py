import random

attempt = 0
failed_attempt = 0
played = 0

while attempt <= 6:

    chioce = input("roll the dice or type 'quit' to stop: ")
    if chioce.lower() == "quit":
        break
    dice = random.randint(1,6)

    guess = int(input("guess the number (1-6): "))

    attempt += 1
    played += 1

    if guess == dice:
        print("correct!")
    else:
        print(f"wrong! the dice was {dice}.")

print("\n--- game summary ---")  
print(f"failed attempt: {failed_attempt}")
print(f"times played: {played}")

if failed_attempt == 0:
    print("Excellent performance!")
elif failed_attempt <= 2:
    print("good performance!")
else:
    print("very and really bad performance!")