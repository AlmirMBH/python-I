
friends = [
    ["Kevin", "Smith", 33],
    ["John", "Wayne", 44],
    ["Mark", "Turner", 55]
]


for letter in "tower":
    print(letter)

for index in range(len(friends)):
    if index == 0:
        print("List of friends")
    print(friends[index])

for friend in friends:
    print(friend[0] + " " + friend[1] + " " + str(friend[2]))
    # for item in friend:
    #     print(item)
