def camel_case(s):
    # Clean-Up the String (filenameUsage Only)
    forbidden_chars = [',', '.', '*', '&', '%', ':']
    s = s.translate({ord(c): '' for c in forbidden_chars})

    # Camel Case the new String
    s = ''.join(x for x in s.title() if not x.isspace())

    # Return the Camel-Cased String
    return s

# On execution grab the string to be camel-cased from the user
if __name__ == '__main__':
    res = camel_case(input('Please Enter the String you want to be camel-cased\n'))
    print(f'Camel-Cased String is:\n{res}')
