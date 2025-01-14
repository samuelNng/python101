#Exercise 1: Roll The Dice
import random
def roll_dice():
    return random.randint(1, 6)
def main():
# Roll the dice
    result = roll_dice()
# Check the result
    if result == 6:
        print("Congrats! Move 2 spaces!")
    else:
        print(result,"Try again!")
        
if __name__ == "__main__":
    main()
#diceNum = random.randint(1,6)
#print(diceNum)

#Exercise 2: Tuple Scenario
# Define tuples for different items in stock
#ApplyQuantity= int(input("Apply's Quantity: ") )
#item1 = ('Apple', 0.5, ApplyQuantity)
item1 = ('Apple', 0.5, 100)
item2 = ('Banana', 0.3, 150)
item3 = ('Milk', 1.2, 50)
item4 = ('Bread', 1.0, 80)
# Display the items in stock
print("Items in Stock:")
print("1. Name: {}, Price: ${}, Quantity: {}".format(item1[0], item1[1], item1[2]))
print("2. Name: {}, Price: ${}, Quantity: {}".format(item2[0], item2[1], item2[2]))
print("3. Name: {}, Price: ${}, Quantity: {}".format(item3[0], item3[1], item3[2]))
print("4. Name: {}, Price: ${}, Quantity: {}".format(item4[0], item4[1], item4[2]))
# Calculate the total value of the inventory
total_value = (item1[1] * item1[2]) + (item2[1] * item2[2]) + (item3[1] * item3[2]) +(item4[1] * item4[2])
print("\nTotal Value of Inventory: ${}".format(total_value))
# Identify items that need restocking based on their quantity
items_to_restock = [item for item in [item1, item2, item3, item4] if item[2] < 10]
if items_to_restock:
    print("\nItems to Restock:")
    for item in items_to_restock:
        print("Name: {}, Quantity: {}".format(item[0], item[2]))
else:
    print("\nAll items are well stocked.")

#Exercise 3: Set Scenario
# Create sets representing different categories of attendees
regular_attendees = {'Alice', 'Bob', 'Charlie'}
vip_attendees = {'David', 'Eva', 'Fiona','Bob'}
speakers = {'Grace', 'Henry', 'Isabel'}
# Add attendees to the respective sets
regular_attendees.add('John')
vip_attendees.add('Kate')
speakers.add('James')
# Perform set operations to analyze the attendee data
common_attendees = regular_attendees.intersection(vip_attendees)
print("Common Attendees:", common_attendees)
unique_regular_attendees = regular_attendees.difference(vip_attendees,
speakers)
unique_vip_attendees = vip_attendees.difference(regular_attendees, speakers)
unique_speakers = speakers.difference(regular_attendees, vip_attendees)

print(regular_attendees)
print(vip_attendees)
print(speakers)

print("Unique Regular Attendees:", unique_regular_attendees)
print("Unique VIP Attendees:", unique_vip_attendees)
print("Unique Speakers:", unique_speakers)