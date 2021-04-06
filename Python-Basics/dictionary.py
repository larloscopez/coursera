#file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#for extension in file_counts:
#    print(extension)
#
#for ext, amount in file_counts.items():
#    print("There are {} of {} files".format(amount, ext))
#
#print(file_counts.keys())
#print(file_counts.values())
#
#cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
#for animal, arms in cool_beasts.items():
#    print("{} have {}".format(animal, arms))
#
## Counting Occurences of letters in text
#def count_letters(text):
#    result = {}
#    for letter in text:
#        if letter not in result:
#            result[letter] = 0
#        result[letter] += 1
#    return print(result)
#
#count_letters("AAAAAAAAAAAAAAAA")
#count_letters("TESTIMONYAGAOINTTTT")
#
##Iterating through Keys and Values
#
#wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
#for style, colors in wardrobe.items():
#	for color in colors:
#		print("{} {}".format(color, style))

#Sets store elements that are only present ONCE - "keys with no associated value" "in list or not"

#Dictionary Methods Cheat Sheet
#Definition

#x = {key1:value1, key2:value2} 

#Operations

#len(dictionary) - Returns the number of items in the dictionary
#for key in dictionary - Iterates over each key in the dictionary
#for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
#if key in dictionary - Checks whether the key is in the dictionary
#dictionary[key] - Accesses the item with key key of the dictionary
#dictionary[key] = value - Sets the value associated with key
#del dictionary[key] - Removes the item with key key from the dictionary
#Methods
#
#dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
#dict.keys() - Returns a sequence containing the keys in the dictionary
#dict.values() - Returns a sequence containing the values in the dictionary
#dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
#dict.clear() - Removes all the items of the dictionary

## QUIZ

#Q1
def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user+"@"+domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

#Q2
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
			# groups for this user, creating the entry
			# in the dictionary if necessary
			
			if user not in user_groups:
				user_groups[user] = [] #initialize values for key
			user_groups[user].append(group) #append user after key has been created to prevent duplicates

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

#Q3
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)

print(wardrobe)

#Q5
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item in basket:
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += basket[item]
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44


# Assessment

#Q1 - formatting addresses

def format_address(address_string):
  # Declare variables
  house_number = []
  street_name = ""
  # Separate the address string into parts
  address_string = address_string.split(" ")
  # Traverse through the address parts
  for part in address_string:
    # Determine if the address part is the
    # house number or part of the street name
    if part.isdecimal():
        house_number = part
    else:
        street_name += part + " "
    
  # Does anything else need to be done 
  # before returning the result?

  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


#Q2 -- capitalizing key words in a string
def highlight_word(sentence, word):
	return(" ".join(part.upper() if word in part else part for part in sentence.split(" ")))
	

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

#Q3 -- reversing and combining lists

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  combined = list2
  list1.reverse()
  combined += list1
  return combined
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

#Q4 -- Squaring each number within a specified range

def squares(start, end):
	return [num*num for num in range(start,end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#Q5 -- Split dictionary items into make and cost, print formatted string for each entry in dict

def car_listing(car_prices):
  result = ""
  for cars, prices in car_prices.items():
    result += "{} costs {} dollars".format(cars, prices) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

