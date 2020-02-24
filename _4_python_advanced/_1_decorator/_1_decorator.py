def mydeco(f):
    def deco():
        f()
        print('deco')
    return deco

@mydeco
def aaa():
    print('aaa')
'''
aaa = mydeco(aaa)
'''
aaa()

# >> aaa
# >> deco