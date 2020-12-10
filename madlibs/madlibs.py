# string concatenation

a = "Hello World"

# a few ways to do this
# print("Concat me with " + a)
# print("Concat me with {}".format(a))
# print(f"Concat me with {a}")

adj = input("Adjective: ")
adj2 = input("Adjective2: ")
famous_person = input("Famous person name: ")

madlib = f"Programming in Python is just {adj} and {adj2}! No problems at all \
 So its another line of story with {famous_person}"

print(madlib)