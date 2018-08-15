# Take note of my use of a single quote within the double quoutes
# Using a single quotation mark within another set of single quotation marks will cause an error
message = "Hello, you're learning how to program in Python."
print(message)

# Reassigning the message variable to a new value
message = "How's your a day going today?"
print(message)

# "\n" means new line
options = input("Good?\nBad?\nFine\n")
if options == "good":
    print("Great to hear!")
elif options == "bad":
    print("I'm sorry. :(\nI hope your day gets better.")
elif options == "fine":
    print("Awesome!")
