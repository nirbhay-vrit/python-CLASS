# Create a Movie class with title and director. Use __str__() to return a sentence like:
# "<title> directed by <director>".

class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def __str__(self):
        return f"{self.title} directed by {self.director}"

movie1 = Movie("Inception", "Christopher Nolan")
print(movie1)
