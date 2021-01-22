# String Methods

name = "aKsHaT nEhRa"

print(name.upper())     # UPPERCASE --> AKSHAT NEHRA
print(name.lower())     # LOWERCASE --> akshat nehra
print(name.title())     # Title     --> Akshat Nehra


# Replace "aks" by "check"  --> checkhat
print(name.replace("aKs", "check"))
# if substring present return True else False
print("aKs" in name)


name = "   akshat   "

print(name.strip())     # removes extra spaces from left and right both --> akshat
print(name.lstrip())    # removes extra spaces only from left           --> akshat
# removes extra spaces only from right          -->    akshat
print(name.rstrip())
