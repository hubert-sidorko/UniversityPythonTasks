import unittest
from task1 import AdresEmail

class Test(unittest.TestCase):
    def setUp(self):
        self.adres = AdresEmail("test_user")

    def test_konstruktor(self):
        self.assertEqual(self.adres.user, "test_user")

    def test_add_adres(self):
        wynik = self.adres.addAddress('prawidlowymail@gmail.com')
        self.assertTrue(wynik)

        wynik = self.adres.addAddress('prawidlowymail@gmail.com')
        self.assertFalse(wynik)

        with self.assertRaises(ValueError):
            self.adres.addAddress('nieprawidlowymail@gmail.c om')

        with self.assertRaises(ValueError):
            self.adres.addAddress('nieprawidlowymail@gmail.com\t')

        with self.assertRaises(ValueError):
            self.adres.addAddress('nieprawidlowymail@gmail.com\n')

        with self.assertRaises(ValueError):
            self.adres.addAddress('nieprawidlowymail@@@@@gmail.com')

        with self.assertRaises(ValueError):
            self.adres.addAddress('@nieprawidlowymail@gmail.com')

        with self.assertRaises(ValueError):
            self.adres.addAddress('nieprawidlowymail@gmail.com@')

        with self.assertRaises(ValueError):
            self.adres.addAddress('nieprawidlowymail@gmailcom')

        with self.assertRaises(ValueError):
            self.adres.addAddress('nieprawidlowymail@gmail.com.')

        wynik = self.adres.addAddress('prawidlowymail@gmail.com')
        self.assertFalse(wynik)
        self.assertEqual(len(self.adres.emails), 1)

    def test_remove_adres(self):
        self.adres.addAddress('przykladowymail@gmail.com')

        wynik = self.adres.removeAddress('przykladowymail@gmail.com')
        self.assertTrue(wynik)
        self.assertNotIn('przykladowymail@gmail.com', self.adres.emails)
        self.assertEqual(len(self.adres.emails), 0)

        wynik = self.adres.removeAddress('nieistniejący@email.com')
        self.assertFalse(wynik)
        self.assertEqual(len(self.adres.emails), 0)

    def test_sort_adres(self):
        self.adres.sortAddresses()
        self.assertEqual(self.adres.emails, [])

        self.adres.addAddress('c@gmail.com')
        self.adres.addAddress('a@gmail.com')
        self.adres.addAddress('b@gmail.com')

        self.adres.sortAddresses()
        self.assertEqual(self.adres.emails,['a@gmail.com', 'b@gmail.com', 'c@gmail.com'])

        self.adres.addAddress('a@gmail.com')
        self.adres.addAddress('b@gmail.com')
        self.adres.addAddress('c@gmail.com')

        self.adres.sortAddresses()
        self.assertEqual(self.adres.emails,['a@gmail.com', 'b@gmail.com', 'c@gmail.com'])

        pusty_adres = AdresEmail("empty_user")
        pusty_adres.sortAddresses()
        self.assertEqual(pusty_adres.emails, [])

if __name__ == '__main__':
    unittest.main()
