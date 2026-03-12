#This is print script
'''
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
*objects -	Values you want to print
sep - Separator between multiple objects
end -	What to print at the end
file - Where to send output
flush -	Force output immediately

'''

name = "Harsh"
age = 25

print(name)
print(age)

# Seprator
print("2026","03","12", sep="-")

#End Function
print("Hello", end=" ")
print("World")

#Formatted Printing
name = "Harsh"
age = 25

print(f"My name is {name} and I am {age} years old")