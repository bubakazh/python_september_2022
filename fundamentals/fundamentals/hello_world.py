# print("皆さん、こんにちは、こんばんは、おはようございます。")

# x = "Pythonの野郎が！（笑）"
# print(x)
# y = 42
# print(y)

# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Troy!" with the name in a variable
name = "Troy"
print("Hello", str(name),"!")	# with a comma (USING COMMAS ALWAYS ADDS SPACE BETWEEN THE CONCATENATED THINGIES.)
print("Hello " + str(name)+"!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 816
print( "Hello", int(name), "!")	# with a comma (AGAIN, USING COMMAS PUTS SPACE BETWEEN THE OBJECTS OF CONCATENATION.)
print("Hello " + str(name) + "!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sinigang"
fave_food2 = "水炊き鍋"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

