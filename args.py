__author__ = 'Scott'


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


def write_multiple_items(file, separator, *args):
    """Write arbitrary number of arguments to file, separated by separator."""
    f = open(file, 'w')
    f.write(separator.join(args))


def concat(*args, sep="/"):
    """Join arbitrary number of arguments with '/' separator."""
    return sep.join(args)


if __name__ == "__main__":
    # ask_ok('Is python fun?: ')
    cheeseshop("Limburger", "It's very runny, sir.",
               "It's really very, VERY runny, sir",
               shopkeeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")
    write_multiple_items('/Users/Scott/multiple_write_function_file', '&', 'arg1', 'arg2', 'arg3')
    print(concat('arg1', 'arg2', 'arg3'))