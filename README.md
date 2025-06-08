# Star Pattern Generator

A simple Python program that generates three different star patterns using a menu-driven approach.

## Description

This program allows users to create beautiful star patterns including:
- **Lower Triangular Pattern** - Stars increase from 1 to n rows
- **Upper Triangular Pattern** - Stars decrease from n to 1 rows  
- **Pyramid Pattern** - Centered stars forming a pyramid shape

The program uses a dictionary-based approach to simulate switch-case functionality in Python.

## How to Execute

### Using Command Line/Terminal

1. Save the code as `pattern.py`
2. Open terminal/command prompt
3. Navigate to the folder containing the file
4. Run the command:
   ```bash
   python pattern.py
   ```

## Program Flow

1. The program displays a menu with 4 options
2. User selects a pattern (1-3) or exits (4)
3. User enters the number of rows for the pattern
4. The selected pattern is displayed
5. Program returns to menu for next operation

## Sample Usage

```
Enter your choice (1-4): 1
Enter number of rows: 5

Lower Triangular Pattern:
-------------------------
* 
* * 
* * * 
* * * * 
* * * * * 
```

## Features

- ✅ Menu-driven interface
- ✅ Input validation
- ✅ Clean and formatted output
- ✅ Continuous operation until user exits
- ✅ Error handling for invalid inputs

## Output Screenshots

### Lower Triangular Pattern

![Lower Triangular Pattern](screenshots/lower_triangular.png)

### Upper Triangular Pattern  
![Upper Triangular Pattern](screenshots/upper_triangular.png)

### Pyramid Pattern
![Pyramid Pattern](screenshots/pyramid.png)

### Menu Interface
![Menu Interface](screenshots/menu.png)


## Notes

- The program runs in a continuous loop until the user chooses to exit
- All patterns use the "*" character with proper spacing
- Input validation ensures only positive integers are accepted for row count
