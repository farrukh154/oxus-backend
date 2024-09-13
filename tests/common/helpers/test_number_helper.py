import unittest

from common.helpers.number_helper import number_to_words_tj


class TestNumberToWordsTJ(unittest.TestCase):

    def test_single_digits(self):
        self.assertEqual('сифр', number_to_words_tj(0))
        self.assertEqual('як', number_to_words_tj(1))

    def test_teen_numbers(self):
        self.assertEqual('ёздаҳ', number_to_words_tj(11))
        self.assertEqual('понздаҳ', number_to_words_tj(15))

    def test_tens(self):
        self.assertEqual('бист', number_to_words_tj(20))
        self.assertEqual('навад', number_to_words_tj(90))

    def test_miscellaneous_numbers(self):
        self.assertEqual('бисту як', number_to_words_tj(21))
        self.assertEqual('як саду як', number_to_words_tj(101))
        self.assertEqual('як ҳазор', number_to_words_tj(1000))

    def test_large_numbers(self):
        self.assertEqual('як миллион', number_to_words_tj(1000000))
        self.assertEqual('се миллиону як', number_to_words_tj(3000001))
        self.assertEqual('як саду бисту се миллиону чор саду панҷоҳу шаш ҳазору ҳафт саду ҳаштоду нӯҳ',
                         number_to_words_tj(123456789))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            number_to_words_tj(-1)
        with self.assertRaises(ValueError):
            number_to_words_tj(1000000000)
