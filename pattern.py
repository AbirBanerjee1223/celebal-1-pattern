def lower_triangular(rows):
    print("\nLower Triangular Pattern:")
    print("-" * 25)
    for i in range(1, rows + 1):
        print("* " * i)

def upper_triangular(rows):
    print("\nUpper Triangular Pattern:")
    print("-" * 25)
    for i in range(rows, 0, -1):
        print("* " * i)

def pyramid(rows):
    print("\nPyramid Pattern:")
    print("-" * 25)
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "* " * i
        print(spaces + stars)

def display_menu():
    print("\n" + "="*40)
    print("       STAR PATTERN GENERATOR")
    print("="*40)
    print("1. Lower Triangular Pattern")
    print("2. Upper Triangular Pattern")
    print("3. Pyramid Pattern")
    print("4. Exit")

def get_rows():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            if rows > 0:
                return rows
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    pattern_functions = {
        1: lower_triangular,
        2: upper_triangular,
        3: pyramid
    }
    
    print("Welcome to Star Pattern Generator!")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 4:
                break
            elif choice in pattern_functions:
                rows = get_rows()
                pattern_functions[choice](rows)
                input("\nPress Enter to continue...")
            else:
                print("Invalid choice! Please select 1-4.")
                
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()