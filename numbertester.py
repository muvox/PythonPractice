def testme(string):
    if string.isalpha() or \
            string.isnumeric() or \
            string.islower() or \
            len(string) < 6:
        return False
    else:
        return True
