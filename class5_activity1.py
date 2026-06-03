# Taking total amount as input for user
Amount = int(input("Please enter amount for Withdraw :"))

#calculating the number of notes of different denominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("Note of 100 rupees", note_1)
print("Note of 50 rupees", note_2)
print("Note of 10 rupees", note_3)