# TrialManager
Make Experiments Management EASY!

# Prerequisite
Python>=3.8,

TinyDB,

Tkinter

# Usage

## Search 
https://tinydb.readthedocs.io/en/latest/usage.html#query-modifiers

e.g.

~ (User.name == 'John')

(User.name == 'John') & (User.age <= 30)

(User.name == 'John') | (User.name == 'Bob')

## Create a new Trial

Double Quote is necessary for key, Single Quote for string value.

`
{
"Ca": 30,
"Na": 10,
"Enzyme": 'Ca'
}
`
