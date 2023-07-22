# Imprt os to get size of terminal
import os

screen_width=os.get_terminal_size().columns

given_str=input("Enter your string: ")
print("Center string")
print(given_str.center(screen_width).title())
print("Left justify")
print(given_str.ljust(screen_width).title())
print("Right justify")
print(given_str.rjust(screen_width).title())

