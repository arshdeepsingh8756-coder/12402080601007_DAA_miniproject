# Personal Expense Analyzer and Budget Assistant
# Simple DAA mini project

expenses = []
budget = 0

def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][2] <= right[j][2]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]


while True:
    print("\n--- Personal Expense Analyzer ---")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Search category (Linear Search)")
    print("4. Sort by amount (Merge Sort)")
    print("5. Set budget")
    print("6. Budget summary")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        category = input("Category: ")
        amount = float(input("Amount: "))
        expenses.append([name, category, amount])
        print("Expense added.")

    elif choice == "2":
        for e in expenses:
            print(e[0], "-", e[1], "- Rs.", e[2])

    elif choice == "3":
        category = input("Category to search: ").lower()
        found = False
        for e in expenses:  # Linear Search
            if e[1].lower() == category:
                print(e[0], "- Rs.", e[2])
                found = True
        if not found:
            print("No expense found.")

    elif choice == "4":
        for e in merge_sort(expenses):
            print(e[0], "-", e[1], "- Rs.", e[2])

    elif choice == "5":
        budget = float(input("Enter budget: Rs. "))

    elif choice == "6":
        total = sum(e[2] for e in expenses)
        print("Budget: Rs.", budget)
        print("Total expenses: Rs.", total)
        print("Money left: Rs.", budget - total)
        if total > budget:
            print("Warning: Budget exceeded!")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
