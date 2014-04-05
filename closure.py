"""
Some days ago someone asked me about closures,
so this is just an example.
"""
import types

class MyString(str):
    """
    Subclass of String, as we cannot patch a Python's String object.
    """
    def __init__(self, current_string):
        """ Init """
        self.current_str = current_string
        super(MyString, self).__init__()

    def __str__(self):
        return self.current_str

    def conditional_string(self, string_true, string_false, method, *args):
        """
        Returns the first or the second string depending on the result
        of the method passed.
        """
        return (string_false , string_true)[int(method(*args))]

def monkey_patch(remembered_str):
    """ Outer function can have local variables, like remembered_str"""

    def has_changed(self):
        """Tells if the original_str is different than the current one"""
        return self.current_str != remembered_str
    remembered_str.has_changed = types.MethodType(has_changed, remembered_str)

    def length_was(self):
        """Returns the length of the remembered_str"""
        return len(remembered_str)
    remembered_str.length_was = types.MethodType(length_was, remembered_str)

    def same_length(self):
        """Is actual length the same as the remembered_str's?"""
        return self.length_was() == len(self.current_str)
    remembered_str.same_length = types.MethodType(same_length, remembered_str)

    def checks(self):
        """ Some prints to show the string properties """
        print '"%s": %s' % (self,
                            self.conditional_string("Is a different string",
                                                    "Is the original string",
                                                    self.has_changed)
                            )
        print '"%s": %s' % (self,
                            self.conditional_string("It's the same length",
                                                    "Length is different",
                                                    self.same_length)
                            )
    remembered_str.checks = types.MethodType(checks, remembered_str)



def main():
    """Main function"""
    my_string = MyString('hello')
    monkey_patch(my_string)  # Properties of my_string will be remembered at
                             # this point
    my_string.checks()
    my_string.current_str = 'good bye'
    my_string.checks()
    my_string.current_str = 'hello'
    my_string.checks()
    my_string.current_str = 'Hello'
    my_string.checks()

if __name__ == '__main__':
    main()
