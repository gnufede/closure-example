"""
Some days ago someone asked me about closures,
so I just had a look at them.
"""
import urlparse
import string
import types

class URL(str):
    """
    Class representing a url (or not), as we cannot patch a String object.
    """
    def __init__(self, url_string):
        """ Init """
        super(URL, self).__init__()
        is_url(self)

    def pretty_prints(self, string_to_format, method, *args):
        """ Formats the string adding 'not' if the function is False """
        print string_to_format % ('not ', '')[int(method(*args))]

    def prints(self):
        """ Some prints to show the url properties """
        print '"%s":' % self
        self.pretty_prints("\tIt's %sa correct url", self.is_url)
        if self.is_url():
            self.pretty_prints("\tIt's %sa robots.txt file", self.is_robots)
            self.pretty_prints("\tIt's %sa gzipped file", self.is_gzip)
            self.pretty_prints("\tIt's %sin google", self.in_domain,
                               'google.com')
            self.pretty_prints("\tIt's %sin yahoo", self.in_domain,
                               'yahoo.com')


def is_url(url):
    """ Uses urlparser to check url regexp """
    _pieces = urlparse.urlparse(url)
    _is_correct_url = all([_pieces.scheme, _pieces.netloc]) and\
        _pieces.scheme in ['http', 'https'] and\
        set(_pieces.netloc) <= set(string.letters + string.digits + '-.')

    def is_robots(self):
        """ Positive if it is a url of a robots.txt file """
        return url.endswith('robots.txt')

    def is_gzip(self):
        """ Positive if it is a url of an gzipped file """
        return url.endswith('.gz')

    def in_domain(self, domain):
        """ Positive if the url is the specified domain """
        return domain in _pieces.netloc

    def is_correct_url(self):
        """ Positive if it's a correct url """
        return _is_correct_url

    url.is_url = types.MethodType(is_correct_url, url)
    if is_correct_url:
        url.is_robots = types.MethodType(is_robots, url)
        url.is_gzip = types.MethodType(is_gzip, url)
        url.in_domain = types.MethodType(in_domain, url)


def main():
    "Main function, test a correct url and an incorrect one"
    for i in ('http://google.com/robots.txt', "hi!, I'm not a url"):
        url = URL(i)
        url.prints()

if __name__ == '__main__':
    main()
