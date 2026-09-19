# Rebekah Kinghorn
# A11 Movie Database. Displays a menu where yo ucan view movies, rate movies, etc



"""this is the initial db stuff"""
from peewee import *

movie_db = SqliteDatabase("movies.db")

#create Movie Class to create Movie table in the db
class Movie(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    year_released = IntegerField()
    status = CharField(default="want to watch")
    rating = IntegerField(null=True)

    class Meta:
        database = movie_db

    @classmethod
    def create(cls, **query):
        #year validation logic - we know to use "year_released" bc that's what I called it in the class Movie (the IntegerField)
        year_input = query.get("year_released")
        year_valid = True

        #change year_valid to False if it is invalid
        if len(str(year_input)) != 4:
            year_valid = False
        elif not (year_input > 1888 and year_input <= 2024):
            year_valid = False
        
        if year_valid == True:
            print(f"\nMovie {movie_name} added to the watchlist.")
            return super().create(**query)
        else:
            print("\nMovie not saved because of an invalid year. Please provide a valid 4-digit year.")


    def get_info(self):
        print(f"ID: {self.id}| Name: {self.name}| Year: {self.year_released} | Status: {self.status}| Rating: {self.rating}")

    
    def rate_movie(self, id, rating):
        the_movie_found = Movie.get(Movie.id == id)
        the_movie_found.rating = rating
        the_movie_found.status = "Watched"
        the_movie_found.save()
        print(f"\nMovie {self.name} updated to 'Watched' with rating {the_movie_found.rating}.")


movie_db.connect()
movie_db.create_tables([Movie])


# Movie.delete().execute()


"""this is the actual program stuff"""
#display menu until option 6 is chosen
exit_menu = False
while exit_menu == False:
    print("\nMovie Tracker Menu:\n")
    print("1. Add a movie to the watchlist")
    print("2. View all movies")
    print("3. Update movie status to 'Watched' and provide a rating")
    print("4. View only watched movies with rating of 4 or above")
    print("5. Delete a movie")
    print("6. Exit")
    menu_choice = int(input("Choose an option (1-6): "))


    #invalid number entered - repeat menu
    if menu_choice not in [1,2,3,4,5,6]:
        print("\nInvalid choice. Please choose again.")
        continue


    #option 6 they want to exit - break loop
    if menu_choice == 6:
        print("Goodbye!")
        break


    #option 1 add movie
    if menu_choice == 1:
        movie_name = input("\nEnter the movie name: ")
        movie_release_year = int(input("Enter the year released: "))

        #add movie to db
        movie_addition = Movie.create(name=movie_name, year_released=movie_release_year)


    #option 2 view all movies
    if menu_choice == 2:
        list_all_movies = Movie.select()

        print()
        for movie in list_all_movies:
            movie.get_info()

    
    #option 3 update movie status to "watched" and rate the movie
    if menu_choice == 3:
        input_id = input("\nEnter the ID of the movie you've watched: ")
        input_rating = input("Enter your rating (1-5): ")
        
        movie_found = Movie.get(Movie.id == input_id)
        movie_found.rate_movie(input_id, input_rating)

    
    #option 4 display movies with rating 4 or above
    if menu_choice == 4:
        list_all_movies = Movie.select().where(Movie.rating >= 4)

        print()
        for movie in list_all_movies:
            movie.get_info()

    
    #option 5 delete a movie
    if menu_choice == 5:
        id_to_delete = input("Enter the ID of the movie to delete: ")

        movie_to_delete = Movie.get(Movie.id == id_to_delete)
        movie_to_delete.delete_instance()
        print(f"\nMovie {movie_to_delete.name} deleted successfully.")