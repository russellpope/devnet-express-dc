var = {"car": "volvo", "fruit": "apple"}
print(var["fruit"])
for f in var:
    print("key: " + f + " value: " + var[f])
print()
print()

var1 = {"donut": ["chocolate", "glazed", "sprinkled"]}
print(var1["donut"][0])
print("My favorite donut flavors are:", end=" ")
for f in var1["donut"]:
    print(f, end=" ")
print()
print()

# Using the examples above write code to print one value of each JSON structure and a loop to print all values.
var = {"vegetable": "carrot", "fruit": "apple", "animal": "cat", "day": "Friday"}

# He did a bad example here:

var1 = {"animal": ["dog", "cat", "fish", "tiger", "camel"]}

# # he did
# for animal in var1:
# 	print(var1['animal'][3])
#
# I hope he doesn't end here
# I would prefer

for animal in var1['animal']:
    if animal == "tiger":
        print(animal)

myvar = {"dessert": "ice cream", "exercise": "push ups", "eyes": "blue", "gender": "male"}

myvar1 = {"dessert": ["cake", "candy", "ice cream", "pudding", "cookies"]}
