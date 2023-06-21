import sys

# get argument
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    # Default
    name = "World"

print("Hello,", name + "!")

# requirements
# desired output
# $ python helloworld.py Richard
# Hello, Richard!

# install and code support:
# pycharm installation guide: https://www.jetbrains.com/pycharm/
# chat GPT prompt: python script to print a user's input argument