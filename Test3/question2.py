
# 2. Product ID Search
# An e-commerce website stores product IDs in ascending order.
# Write a program to find whether a customer-entered product ID exists in
# the inventory. If it exists, display its index; otherwise, display "Product
# Not Available."
def binary_search(inventory, target):
    low  = 0
    high = len(inventory) - 1

    while low <= high:
        mid = (low + high) // 2

        if inventory[mid] == target:
            return mid                  
        elif target < inventory[mid]:
            high = mid - 1             
        else:
            low  = mid + 1 

    return -1                          



inventory = [1012, 1045, 1078, 1103, 1156, 1200, 1234, 1289, 1345, 1400]

print("Inventory (sorted):", inventory)
print()
print("Inventoru(soed)",inventory)
target = int(input("Enter Product ID to search: "))

index = binary_search(inventory, target)

if index != -1:
    print(f"Product ID {target} found at index {index}.")
else:
    print("Product Not Available.")