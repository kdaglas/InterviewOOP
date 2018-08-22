first_string = input("Enter first string: ")
second_string = input("Enter second string: ")

count1 = 0
count2 = 0

for i in first_string:
    count1 = count1 + 1
for j in second_string:
    count2 = count2 + 1
if(count1 < count2):
    print("Larger string is:")
    print(second_string)
elif(count1 == count2):
    print("Both strings are equal.")
else:
    print("Larger string is:")
    print(first_string)