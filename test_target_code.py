import unittest
from target_code_2 import *
from io import StringIO
import sys

class Test_TargetCode(unittest.TestCase):
    def setUp(self):
        """Set up a fresh calculator instance before each test."""
        self.calculator = Calculator()
        self.library = Library()


    def test_TC001_add_positive_numbers(self):
        result = self.calculator.add(5, 3)
        expected = 8
        print("TC001")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC002_subtract_positive_numbers(self):
        result = self.calculator.subtract(10, 4)
        expected = 6
        print("TC002")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC003_multiply_positive_numbers(self):
        result = self.calculator.multiply(6, 7)
        expected = 42
        print("TC003")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC004_divide_positive_numbers(self):
        result = self.calculator.divide(20, 4)
        expected = 5.0
        print("TC004")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC005_power_of_number(self):
        result = self.calculator.power(2, 3)
        expected = 8
        print("TC005")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC006_division_by_zero(self):
        result = self.calculator.divide(10, 0)
        expected = "Error! Division by zero."
        print("TC006")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC007_add_positive_and_negative(self):
        result = self.calculator.add(10, -5)
        expected = 5
        print("TC007")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC008_subtract_larger_from_smaller(self):
        result = self.calculator.subtract(3, 10)
        expected = -7
        print("TC008")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC009_multiply_with_zero(self):
        result = self.calculator.multiply(0, 7)
        expected = 0
        print("TC009")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC010_power_negative_exponent(self):
        result = self.calculator.power(2, -2)
        expected = 0.25
        print("TC010")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC011_add_two_negative_numbers(self):
        result = self.calculator.add(-5, -10)
        expected = -15
        print("TC011")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC012_subtract_zero(self):
        result = self.calculator.subtract(10, 0)
        expected = 10
        print("TC012")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC013_multiply_two_negative_numbers(self):
        result = self.calculator.multiply(-3, -7)
        expected = 21
        print("TC013")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC014_divide_negative_by_positive(self):
        result = self.calculator.divide(-20, 4)
        expected = -5.0
        print("TC014")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC015_power_zero_base(self):
        result = self.calculator.power(0, 3)
        expected = 0
        print("TC015")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC016_power_zero_exponent(self):
        result = self.calculator.power(5, 0)
        expected = 1
        print("TC016")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC017_divide_by_one(self):
        result = self.calculator.divide(10, 1)
        expected = 10.0
        print("TC017")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC018_add_large_and_small_number(self):
        result = self.calculator.add(1e9, 1)
        expected = 1000000001
        print("TC018")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC019_multiply_by_fraction(self):
        result = self.calculator.multiply(4, 0.5)
        expected = 2.0
        print("TC019")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def test_TC020_power_of_fraction(self):
        result = self.calculator.power(0.5, 2)
        expected = 0.25
        print("TC020")
        print(f"Expected: {expected}")
        print(f"Actual: {result}")
        self.assertEqual(result, expected)

    def capture_output(self, func, *args, **kwargs):
        """Helper method to capture printed output."""
        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        func(*args, **kwargs)  # Call the function
        sys.stdout = sys.__stdout__  # Reset stdout
        return captured_output.getvalue().strip()

    # TC001 - TC011 (Previous Test Cases)
    def test_TC021_add_book(self):
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 5)
        expected = "Title: The Great Gatsby, Author: F. Scott Fitzgerald, Copies: 5"
        actual = f"Title: {self.library.books[0].title}, Author: {self.library.books[0].author}, Copies: {self.library.books[0].copies}"
        print("TC001")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        self.assertEqual(expected, actual)

    def test_TC022_add_member(self):
        self.library.add_member("John Doe")
        expected = "Name: John Doe, Borrowed Books: None"
        actual = f"Name: {self.library.members[0].name}, Borrowed Books: {', '.join([book.title for book in self.library.members[0].borrowed_books]) or 'None'}"
        print("TC002")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        self.assertEqual(expected, actual)

    def test_TC023_borrow_book_success(self):
        self.library.add_book("1984", "George Orwell", 3)
        self.library.add_member("Alice")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id

        self.library.borrow_book(member_id, book_id)
        expected_copies = 2
        expected_borrowed_books = ["1984"]
        actual_copies = self.library.books[0].copies
        actual_borrowed_books = [book.title for book in self.library.members[0].borrowed_books]
        print("TC003")
        print(f"Expected: Copies: {expected_copies}, Borrowed Books: {expected_borrowed_books}")
        print(f"Actual: Copies: {actual_copies}, Borrowed Books: {actual_borrowed_books}")
        self.assertEqual(expected_copies, actual_copies)
        self.assertEqual(expected_borrowed_books, actual_borrowed_books)

    def test_TC024_borrow_book_no_copies(self):
        self.library.add_book("To Kill a Mockingbird", "Harper Lee", 0)
        self.library.add_member("Bob")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id

        output = self.capture_output(self.library.borrow_book, member_id, book_id)
        expected = f"No copies available for book: To Kill a Mockingbird"
        print("TC004")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    def test_TC025_borrow_book_limit(self):
        self.library.add_book("Book1", "Author1", 5)
        self.library.add_book("Book2", "Author2", 5)
        self.library.add_book("Book3", "Author3", 5)
        self.library.add_book("Book4", "Author4", 5)
        self.library.add_member("Charlie")
        member_id = self.library.members[0].member_id

        for book in self.library.books[:3]:
            self.library.borrow_book(member_id, book.book_id)

        output = self.capture_output(self.library.borrow_book, member_id, self.library.books[3].book_id)
        expected = "Charlie has already borrowed the maximum number of books."
        print("TC005")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    def test_TC026_return_book_success(self):
        self.library.add_book("Moby Dick", "Herman Melville", 2)
        self.library.add_member("Dave")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id

        self.library.borrow_book(member_id, book_id)
        output = self.capture_output(self.library.return_book, member_id, book_id)
        expected = f"Book returned: Moby Dick by Dave"
        print("TC006")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    def test_TC027_return_book_not_borrowed(self):
        self.library.add_book("The Hobbit", "J.R.R. Tolkien", 2)
        self.library.add_member("Eve")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id

        output = self.capture_output(self.library.return_book, member_id, book_id)
        expected = f"No record of this book being borrowed by Eve"
        print("TC007")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    def test_TC028_transaction_history(self):
        self.library.add_book("The Catcher in the Rye", "J.D. Salinger", 4)
        self.library.add_member("Frank")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id

        self.library.borrow_book(member_id, book_id)
        self.library.return_book(member_id, book_id)
        transactions = self.library.transactions
        expected = [
            (member_id, book_id, "borrow"),
            (member_id, book_id, "return"),
        ]
        print("TC008")
        print(f"Expected: {expected}")
        print(f"Actual: {transactions}")
        self.assertEqual(expected, transactions)

    def test_TC029_borrow_book_no_member(self):
        book_id = "B1234"
        member_id = "M9999"
        output = self.capture_output(self.library.borrow_book, member_id, book_id)
        expected = "No member found with ID M9999"
        print("TC009")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    def test_TC030_borrow_book_no_book(self):
        self.library.add_member("Nonexistent Book Tester")
        member_id = self.library.members[0].member_id
        book_id = "B1234"
        output = self.capture_output(self.library.borrow_book, member_id, book_id)
        expected = "No book found with ID B1234"
        print("TC010")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    def test_TC031_return_book_not_borrowed(self):
        self.library.add_member("No Borrow Test")
        member_id = self.library.members[0].member_id
        book_id = "B1234"
        output = self.capture_output(self.library.return_book, member_id, book_id)
        expected = "No record of this book being borrowed by No Borrow Test"
        print("TC011")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    # TC012 - TC018 (New Test Cases)
    # See explanations above for the new tests
    def test_TC032_borrow_book_no_books_in_library(self):
        self.library.add_member("Test User")
        member_id = self.library.members[0].member_id
        output = self.capture_output(self.library.borrow_book, member_id, "B9999")
        expected = "No book found with ID B9999"
        print("TC012")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    def test_TC033_return_book_no_books_in_library(self):
        self.library.add_member("Test User")
        member_id = self.library.members[0].member_id
        output = self.capture_output(self.library.return_book, member_id, "B9999")
        expected = "No record of this book being borrowed by Test User"
        print("TC013")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    def test_TC034_add_member_and_borrow_immediately(self):
        """Test adding a member and immediately borrowing a book."""
        self.library.add_book("Borrow Me", "Author Test", 1)
        self.library.add_member("Immediate Borrower")
        member_id = self.library.members[0].member_id
        book_id = self.library.books[0].book_id

        output = self.capture_output(self.library.borrow_book, member_id, book_id)
        expected = f"Book borrowed: Borrow Me by Immediate Borrower"
        print("TC014")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    def test_TC035_return_book_not_borrowed_by_member(self):
        """Test returning a book that exists but hasn't been borrowed by the member."""
        self.library.add_book("Book Not Borrowed", "Author Test", 1)
        self.library.add_member("Wrong Member")
        member_id = self.library.members[0].member_id
        book_id = self.library.books[0].book_id

        output = self.capture_output(self.library.return_book, member_id, book_id)
        expected = f"No record of this book being borrowed by Wrong Member"
        print("TC015")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    def test_TC036_multiple_members_borrow_simultaneously(self):
        """Test borrowing a book with multiple members."""
        self.library.add_book("Shared Book", "Author Test", 3)
        self.library.add_member("Member1")
        self.library.add_member("Member2")
        self.library.add_member("Member3")
        book_id = self.library.books[0].book_id

        # Borrow for each member
        for member in self.library.members:
            output = self.capture_output(self.library.borrow_book, member.member_id, book_id)
            expected = f"Book borrowed: Shared Book by {member.name}"
            print(f"TC016 ({member.name})")
            print(f"Expected: {expected}")
            print(f"Actual: {output}")
            self.assertIn(expected, output)

        # Check book copies
        remaining_copies = self.library.books[0].copies
        expected_copies = 0
        print("TC016 - Final Copies")
        print(f"Expected: {expected_copies}")
        print(f"Actual: {remaining_copies}")
        self.assertEqual(expected_copies, remaining_copies)

    def test_TC037_borrow_book_after_updating_copies(self):
        """Test borrowing a book after updating its copies."""
        self.library.add_book("Out of Stock", "Author Test", 0)
        self.library.books[0].copies = 2  # Update copies
        self.library.add_member("Member")
        member_id = self.library.members[0].member_id
        book_id = self.library.books[0].book_id

        output = self.capture_output(self.library.borrow_book, member_id, book_id)
        expected = f"Book borrowed: Out of Stock by Member"
        print("TC017")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

    def test_TC038_borrow_same_book_twice(self):
        """Test a member trying to borrow the same book twice."""
        self.library.add_book("Repeat Borrow", "Author Test", 1)
        self.library.add_member("Repeat Borrower")
        member_id = self.library.members[0].member_id
        book_id = self.library.books[0].book_id

        # First borrow
        self.library.borrow_book(member_id, book_id)
        
        # Second borrow
        output = self.capture_output(self.library.borrow_book, member_id, book_id)
        expected = "No copies available for book: Repeat Borrow"
        print("TC018")
        print(f"Expected: {expected}")
        print(f"Actual: {output}")
        self.assertIn(expected, output)

if __name__ == "__main__":
    unittest.main()