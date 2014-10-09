import re

pat = r'([a-zA-Z][\w\.-]*)@([\w-]+)\.([\w-]+)(\.[\w-]+)?$'

text1 = 'first_name.last_name@happiestminds.com'
text2 = 'first_name.last_name@happiestminds.co.in'
text3 = 'first_name.last_name@happiestminds.co.in.blr'
text4 = '.first_name.last_name@happiestminds.com'

for t in [text1, text2, text3, text4]:
    match = re.match(pat, t)
    print '\n'
    print '{} {} pattern'.format(
        t, 'matches' if match else 'does not match')

    if not match:
        continue

    # Substitution. Change a@b -> b@a
    if match.group(4):
        print re.sub(r'(\w[\w\.-]*)@([\w-]+)\.([\w-]+)(\.[\w-]+)?$',
               r'\2.\3\4@\1', t)
    else:
        print re.sub(r'(\w[\w\.-]*)@([\w-]+)\.([\w-]+)(\.[\w-]+)?$',
               r'\2.\3@\1', t)


# Reference: https://docs.python.org/2/library/re.html