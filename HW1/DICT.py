rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix_dict = {}

for r in range(rows):
    row = []
    print(f"\nRow {r+1}")
    for c in range(cols):
        num = float(input(f"Enter number{c+1}: "))
        row.append(num)
    matrix_dict[r] = row

print("\nThe numbers are (Dictionary):\n")
for r in range(rows):
    print(" ".join(str(x) for x in matrix_dict[r]))

search_num = float(input("\nSearch: "))

found = []
for r in range(rows):
    for c in range(cols):
        if matrix_dict[r][c] == search_num:
            found.append((r, c))

if found:
    print(f"Number {search_num} found at:", found)
else:
    print(f"Number {search_num} not found.")
