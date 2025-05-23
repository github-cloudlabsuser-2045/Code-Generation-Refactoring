import sys
from typing import List

MAX = 100
INVALID_INPUT_MSG = "Invalid input. Please try again."

def calculate_sum(arr: List[int]) -> int:
   """Calculate the sum of a list of integers."""
   return sum(arr)

def get_integer_input(prompt: str) -> int:
   """Prompt the user for an integer input with error handling."""
   while True:
      try:
         return int(input(prompt))
      except ValueError:
         print(INVALID_INPUT_MSG)

def main() -> None:
   """Main function to execute the program."""
   try:
      n = get_integer_input("Enter the number of elements (1-100): ")
      if not 1 <= n <= MAX:
         print("Invalid input. Please provide a number ranging from 1 to 100.")
         sys.exit(1)

      arr = []
      print(f"Enter {n} integers:")
      for _ in range(n):
         arr.append(get_integer_input("> "))

      total = calculate_sum(arr)
      print("Sum of the numbers:", total)

   except KeyboardInterrupt:
      print("\nProgram terminated by user.")
      sys.exit(1)

if __name__ == "__main__":
   main()
