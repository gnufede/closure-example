"""
Some days ago someone asked me about closures,
so this is just an example.
"""
import types

class MyString(str):
    """
    Subclass of String, as we cannot patch a Python's String object.
    """
    # pylint: disable=R0904
    #   Too many public methods: we are a subclass of String
    def __init__(self, current_string):
        """
        Init
        """
        self.current_str = current_string
        super(MyString, self).__init__()

    def __str__(self):
        """
        Redefine str, to return current_str
        """
        return self.current_str


def monkey_patch(remembered_str):
    """
    Outer function can have local variables and  functions,
    like remembered_str or length_was
    """
    def length_was():  # As it is a local function, will be remembered
        """
        Returns the length of the remembered_str
        """
        return len(remembered_str)

    def has_changed(self):  # A method to be patched into our String
        """
        Tells if the remembered_str is different than the current one
        """
        return str(self) != remembered_str

    def same_length(self):  # Uses the local method of length to compare
        """
        Is actual length the same as the remembered_str's?
        """
        return length_was() == len(str(self))

    # Now we add the functions we'd like tu have in the object
    remembered_str.has_changed = types.MethodType(has_changed, remembered_str)
    remembered_str.same_length = types.MethodType(same_length, remembered_str)


def check(my_string):
    """
    Runs some checks to show the string properties
    """
    def conditional_string(string_true, string_false, method, *args):
        """
        Returns the first or the second string depending on the result
        of the method passed.
        """
        return (string_false, string_true)[int(method(*args))]

    def print_check(string_true, string_false, method, *args):
        """
        Prints the checks so they're readable
        """
        print '"%s": %s' % (my_string, conditional_string(string_true,
                                                          string_false,
                                                          method, *args))

    print_check("Is a different string", "Is the same string",
                my_string.has_changed)
    print_check("Has same length", "Length is different",
                my_string.same_length)


def main():
    """
    Main function
    """
    my_string = MyString('hello')
    monkey_patch(my_string)  # Properties of my_string will be remembered at
                             # this point
    check(my_string)

    for i in 'good bye', 'hello', 'Hello':
        my_string.current_str = i
        check(my_string)

if __name__ == '__main__':
    main()
