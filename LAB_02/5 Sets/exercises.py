#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#Answer: in
 
#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#Answer: fruits.add("orange")
 
#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#Answer: fruits.update(more_fruits)

#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#Answer: fruits.remove("banana")

#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#Answer: fruits.discard("banana")