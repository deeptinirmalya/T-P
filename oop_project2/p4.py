class Movie:
    def __init__(self, name, showtime, seats):
        self.name = name
        self.showtime = showtime
        self.seats = seats


class BookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, name, showtime, seats):
        m = Movie(name, showtime, seats)
        self.movies.append(m)

    def show_movies(self):
        for m in self.movies:
            print(m.name, m.showtime, "Seats:", m.seats)

    def book_ticket(self, movie_name, seat_count):
        for m in self.movies:
            if m.name == movie_name:
                if m.seats >= seat_count:
                    m.seats = m.seats - seat_count
                    print("Booking Confirmed")
                    print("Movie:", m.name)
                    print("Showtime:", m.showtime)
                    print("Seats Booked:", seat_count)
                else:
                    print("Not enough seats")


b = BookingSystem()

b.add_movie("Avengers", "6 PM", 50)
b.add_movie("Batman", "9 PM", 40)

b.show_movies()

b.book_ticket("Avengers", 3)

b.show_movies()