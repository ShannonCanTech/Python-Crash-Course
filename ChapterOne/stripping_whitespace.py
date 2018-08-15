email = input("Enter your email: ")

#Adds whitespace to the right of the output, then strips it away
print("'" + email + '\t' + "'")
print("'" + email.rstrip() + "'")

# Adds whitespce to the left of the output, then strips it away
print("'" + '\t' + email + "'")
print("'" + email.lstrip() + "'")

# Adds whitespace to both the left and right of the output, then strips it away
print("'" + '\t'+  email + '\t' + "'")
print("'" + email.strip() + "'")