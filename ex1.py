#Python searches first for a local variable above the print statement if none then it checks for a global variable..
def f():
    global s
    print(s)
    s="WTF is THIS SHIT!"
    print(s)

s="Ez-Pz lemon squezy"
f()
