class SprocketMetaclass(type):

    def __new__(cls, name, bases, dct):

        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        return super(SprocketMetaclass, cls).__new__(cls, name, bases, uppercase_attr)
