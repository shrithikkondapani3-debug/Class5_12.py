# take marks as input for user
print("Enter marks obtained in 4 subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
computer = int(input("computer :"))

#Let's calculate the percentage of marks
sum = math+english+science+computer
print("Sum of math, english, science, and computer = ", sum)

perc = (sum/400)*100

print(end="Percentage marks = ")
print(perc)