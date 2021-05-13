#Python has a feature which lets it to modify a function, by using another function. It lets us use function as input/output
def announce(f):
    def wrap():
        print("The function is about to start...")
        f()
        print("Done with the function")
    return wrap
@announce
def hello():
    print("Hello, World")

hello()
