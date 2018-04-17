from django.test import TestCase

# Create your tests here.

from catalog.models import Author

class TestPolindrom(TestCase):

    

    def is_palindrom(self):
        author='kazakh'
        author2=author[::-1]
        x = len(author)
        i = 0
        x = x - 1
        k = 0
        while x - i >= i:
            if author[x - i] == author[i]:
                i += 1
            else:
                k = 1
            break
        if k == 1:
            print("False")
        else:
            print("True")
        self.assertEquals(author, author2)
