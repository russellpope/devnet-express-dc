## I modified this per the exercise requested
# Decided to use f strings everywhere
# I also swapped tabs for space so this would run like I would expect

print("Hello world!")

num = 823

if num < 1000:
    print(f"I'm less than 1000!")
elif num == 1:
    print("I'm equal to 1.")
else:
    print("Goodbye Cruel World!")

print("I always get printed!")


# A question came up here about the values
# This line executes and sets it to 134
val = 134

# This reports it as it was done just above
print("the value is: ", val)

print("the val is " + str(val))
print(f"A better way to represent the value of val would be to use an f string! {val}")

# now we set it
val = 234

# This will now report a new value
new_val = "the value is" + str(val)

print(new_val)