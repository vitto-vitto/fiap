total_weight = 0.0

for x in range(1, 11):
    actual_weight = float(input("Inform the box weight: "))
    total_weight = total_weight + actual_weight

medium = total_weight/10

print("The total weight of the boxes is: {}".format(total_weight))
print("The medium weight of the boxes is: {}".format(medium))
