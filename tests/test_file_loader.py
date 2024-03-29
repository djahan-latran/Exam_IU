import unittest
from file_loader import FileLoader

#needs fixing
class TestFileLoader(unittest.TestCase):

    def test_load_and_construct_csv_attribute(self):

        foldername = None
        filename = None
        fileloader = FileLoader(foldername=foldername, filename=filename)

        with self.assertRaises(AttributeError):
            fileloader.load_and_construct_csv()

    def test_load_and_construct_csv_file_format(self):

        foldername = "datensaetze"
        filename = "unittest_fileloader.txt"
        fileloader = FileLoader(foldername=foldername, filename=filename)

        with self.assertRaises(ValueError):
            fileloader.load_and_construct_csv()

    def test_load_and_construct_csv_file(self):

        foldername = "datensaetze"
        filename = "train.csv"

        fileloader = FileLoader(foldername=foldername, filename=filename)
        file = fileloader.load_and_construct_csv()

        self.assertIsNotNone(file)


if __name__ == '__main__':
    unittest.main()