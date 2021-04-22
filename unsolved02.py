"""
Write Python code that asks a user how many pizza slices they want.
The pizzeria charges Rs 123.00 a slice
if user order even number of slices, price per slice is Rs 120.00
Print the total price depending on how many slices user orders.

"""

slices=int(input("How many slices:"))
if slices%2==0:
    total=slices*120.00
else:
    total=slices*123.00

print(float(total))
