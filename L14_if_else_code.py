price = 1000000
good_credit =   True
down = 0

if good_credit:
    down = 0.1*price
else:
    down = 0.2*price
print(f"Down Payment: ${down}")