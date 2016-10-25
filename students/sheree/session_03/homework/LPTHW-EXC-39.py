def print_separator():
	print("")
	print("-" * 10)
	pass

# create map of state abbr
states = {
"Oregon": "OR",
"Florida": "FL",
"California": "CA",
"New York": "NY",
"Michigan": "MI"
}

# create some states and cities
cities = {
"CA": "San Francisco",
"MI": "Detroit",
"FL": "Jacksonville"
}

#add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

#print some cities
print_separator()
print("NY state has:", cities["NY"])
print("OR state has", cities["OR"])
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']

#print some states
print_separator()
print("Michigan's abbr is:", states["Michigan"])
print("Florida's abbr is", states["Florida"])

#do the same but with cities, states dict
print_separator()
print("Michigan's abbr is:", cities[states["Michigan"]])
print("Florida's abbr is:", cities[states["Florida"]])

#print all the state abbrs
print_separator()
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

#print every city in state
print_separator()
for abbrev, city in cities.items():
	print("%s has the city %s") % (abbrev, city)

#now do both at the same time!
print_separator()
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print_separator()
state = states.get("Texas", None)

if not state:
	print "sorry, no Texas"

city = cities.get("TX", "Does not exist")
print "The city for the state 'TX' is %s" % city
