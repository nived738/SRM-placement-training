p = float(input())
r = float(input())
t = float(input())

interest = (p * r * t) / 100
amount = p + interest
discount = interest * 2 / 100
final_amount = amount - discount

print(f"{interest:.2f}")
print(f"{amount:.2f}")
print(f"{discount:.2f}")
print(f"{final_amount:.2f}")
