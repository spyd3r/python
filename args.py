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


if __name__ == "__main__":
    ask_ok('Is python fun?: ')