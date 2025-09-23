import array

# -------------------------------
# Integers
# -------------------------------
sales = [120, 150, 90, 200, 175]  # quantities of fuel sold (example data)
total_sales = sum(sales)
average_sales = total_sales / len(sales)
min_sales = min(sales)
max_sales = max(sales)

print("=== Fuel Station Sales Report ===")
print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales:.2f}")
print(f"Minimum Sales: {min_sales}")
print(f"Maximum Sales: {max_sales}")

# -------------------------------
# Strings (formatted report)
# -------------------------------
report = f"""
Fuel Station Sales Summary:
---------------------------
Total Sales = {total_sales}
Average Sales = {average_sales:.2f}
"""
print(report)

# -------------------------------
# Booleans (Threshold Check)
# -------------------------------
threshold = 140
status = "Above Standard" if average_sales > threshold else "Below Standard"
print(f"Performance Status: {status}")

# -------------------------------
# Lists (modifications)
# -------------------------------
print("\nOriginal sales list:", sales)
sales.append(160)  # add new element
print("After adding 160:", sales)
sales.remove(90)   # remove element
print("After removing 90:", sales)
sales.sort()
print("Sorted sales list:", sales)

# -------------------------------
# Arrays
# -------------------------------
sales_array = array.array('i', [120, 150, 200, 175])  # subset
print("\nArray contents:", sales_array)
print("Sum of array:", sum(sales_array))
print("Compare with sum of list:", sum(sales))

# -------------------------------
# Dictionaries
# -------------------------------
records = [
    {"id": 1, "name": "Petrol", "value": 120},
    {"id": 2, "name": "Diesel", "value": 150},
    {"id": 3, "name": "Kerosene", "value": 90}
]

print("\nOriginal Records:", records)

# Update one record
records[0]["value"] = 130

# Delete one record
records.pop(2)

# Compute total value
total_value = sum(item["value"] for item in records)
print("Updated Records:", records)
print("Total Value across records:", total_value)
