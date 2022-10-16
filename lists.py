
lucky_numbers = [4, 12, 8, 16, 20, 24, 28]
friends = ["Kevin", "Karen", "Almir", "Jim", "Oscar", "Toby"]
friends[1] = "Almir"

print(friends[1])
print(friends[-1])  # print the last element
print(friends[1:])  # print all elements after the first
print(friends[-2:])  # print all elements after the second to the last
print(friends[2:4])  # print second and third elements

# functions
friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(2, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()  # removes the last element of the list
print(friends)

print(friends.count("Almir"))

print(friends.index("Oscar"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2 )

friends.clear()
print(friends)





