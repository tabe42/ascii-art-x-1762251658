#!/usr/bin/env python3
"""
ASCII Art X Printer
Prints a large X using dots and spaces
"""

def print_x(size=9):
    """
    Print an X pattern using dots
    
    Args:
        size: Height of the X (must be odd number)
    """
    if size % 2 == 0:
        size += 1  # Make it odd
    
    for i in range(size):
        line = ""
        for j in range(size):
            # Print dot on diagonals
            if j == i or j == size - 1 - i:
                line += "•"
            else:
                line += " "
        print(line)

def print_x_large():
    """Print a large decorative X"""
    x_pattern = [
        "•       •",
        " •     • ",
        "  •   •  ",
        "   • •   ",
        "    •    ",
        "   • •   ",
        "  •   •  ",
        " •     • ",
        "•       •"
    ]
    
    print("\n" + "=" * 40)
    print("ASCII ART X".center(40))
    print("=" * 40 + "\n")
    
    for line in x_pattern:
        print(line.center(40))
    
    print("\n" + "=" * 40)

if __name__ == "__main__":
    print("\nSimple X:")
    print_x(7)
    
    print("\n\nLarge Decorative X:")
    print_x_large()
    
    print("\n\nCustom size X (size=11):")
    print_x(11)
