# Step 35 - Locator Ranking

ranking = [
"1. ID",
"2. CSS Selector",
"3. Name",
"4. Relative XPath",
"5. Class Name",
"6. Absolute XPath"
]

for item in ranking:
    print(item)

print("\nComments:")
print("- ID: Best (unique, readable, fast)")
print("- CSS: Fast and maintainable")
print("- Name: Good if unique")
print("- Relative XPath: Flexible")
print("- Class Name: May not be unique")
print("- Absolute XPath: Avoid because HTML changes break it")
