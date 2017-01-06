zoo = ("Lion", "Tiger", "Bear")
print(zoo.index("Bear"))

for animal in zoo:
	if animal == "Lion":
		print("GRRR")

(Lion, Tiger, Bear) = zoo
print(Lion)

new_zoo = list(zoo)
new_zoo.extend(["omy", "monkey", "snake"])
tuple(new_zoo)
print('Zoo List: {}'.format(new_zoo))

