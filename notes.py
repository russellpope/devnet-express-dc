
##
## Intro to Git, Python, and Programming Basics (bypassing XML)
##

# going over some git basics

# git --version
# git help

# Pull down a repo from somewhere
# git clone <url>

# git branches; discussed to some degree; means of doing changes off to side without affecting core code
# then we can merge this stuff in as needed

# git remote -v
# origin	git@github.com:russellpope/devnet-express-dc.git (fetch)
# origin	git@github.com:russellpope/devnet-express-dc.git (push)

# lets us know where we're pulling stuff from and where we make a push to
# origin in this case is an alias



# git pull
# Pulls the latest changes for the selected branch

# python -V or python --version
# note you can do this with py3 in a virtualenv or python3 --version

# python YOURSCRIPT.py

# Some python bits of note:

# indentation defining scopes (WHITESPACE CHARACTER IS IMPORTANT)
# i.e. spaces and tabs are different things
#

# Sample below; illustrates white spaces

print("Hellworld!")
num = 1
if num < 1:
    print(f"I'm less than {num}!")
    print("goodbye cruel world!")

# note the 'if' condition will never execute
# editorial note: I used an f string because I wanted to


print("Helloworld!")
num = 1
print(f"Value is: {num}")
print("Value is: " + str(num))
print("Value is:", num)

if num < 1:
    print(f"I'm less than {num}!")
elif num == 1:
    print(f"I'm {num}")
else:
    print(f"{num} is something else!")


#
# tried to transcribe his example before he switched sides
# I hate his variable names because they look like java stuff

# goes through an excercise of running python from CLI
# walking through his interpreter stuff

# ran the below with expected output:
# >>> print("Hello World! How are you?")
# Hello World! How are you?

# to exit python interpreter
# >>> quit()
#

# talks about running scripts
# unix prompt below:
# #python your_script_here.py


# Covers the "shebang" line
# #!/usr/bin/python

# or you could do this which he may not cover
# #!/usr/bin/env python
# This will actually use whatever python interpreter is defined in the environment var


# Scopes, operators, conditiona statemments


# Parsing JSOn with python


sample_json = {
    "first_name" : "Mike",
    "last_name" : "Maas"
}

# data structure
# nice thing about it is that it maps to python dictionaries pretty nicely
# collections of key/value pairs enclosed in {}
# Can also have values be ordered lists of values
# or even ordered lists of key value pairs

sample_json_with_array = [{"first_name" : "Mike","last_name" : "Maas"},
                          {"first_name" : "Brett","last_name" : "Tiller"}]

# provided a more complex data structure to describe a donut to showcase the sorts of embedded stuff you can do
