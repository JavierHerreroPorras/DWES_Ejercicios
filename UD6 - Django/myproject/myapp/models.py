from django.db import models
# Create your models here.
class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

    @property
    def is_classic(self):
        """
        Check if the book is a classic (published before 1970).
        """
        return self.published_date.year < 1970

    def get_summary(self):
        """
        Return a summary of the book.
        """
        return f"{self.title} by {self.author.name}, published on {self.published_date.year}"