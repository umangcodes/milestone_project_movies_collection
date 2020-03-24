'''
Project name: milestone project(movies collection)

Author: Umang A
Start Date: 24 March 2020| 1630
Version 1.0 release date: 24 march 2020 | 1820

description:

This program will create a menu which will ask the user for type of action.
Then it will execute the corresponding function and p[orvide visual output to the user if user asks for it.

Updates for next version:
 upgrade the find function by introducing method in which you can search by name, duration, time or watched/notwatchhed.
'''
'''
Format of the data storage:

[("title":"name_of_title","director":"name_of_director","duration":"duration__of_movies"),
    ("title":"name_of_title","director":"name_of_director","duration":"duration__of_movies"),
    ("title":"name_of_title","director":"name_of_director","duration":"duration__of_movies"),

]
'''

print("WELCOME TO YOUR PERSONAL MOVIE DATABASE, SIR.")

database_movies = []
def yes_no():                          # ::// for version 2: use lower() function instead of if statements
    while True:
        condition = input()
        condition = condition.lower()
        if condition == "y" or condition == "yes":
            return True
        elif condition == "n" or condition == "no":
            return False
        print("invalid command enter either y/n or yes/no.")
def add_movie_to_database(database):
    continue_adding = True
    while continue_adding == True:
        movie_title = input("Please enter the title of the movie: ")
        movie_director = input("Please enter the director of the movie: ")
        movie_duration = input("Please enter the duration of the movie(hhmm): ")   #:://Error handling if the input is not int
        database.append({"title" : movie_title, "director" : movie_director,"duration" : int(movie_duration)})
        print("Do you want to continue adding more movies(y/n):")
        continue_adding = yes_no()# if it provides false or nothing it will end the loop

def find_the_movie_by_name(movie_name):
    for movie_location in database_movies:
        if movie_name == movie_location["title"]:
            print("Movie found!")
            print(f"Index of movie in database is {database_movies.index(movie_location)+1}.")
            return movie_location
    else:
        print("ghhh! Sorry sir. Movie is not available in the database.")
        return False

def remove_movies_from_database(database):
    continue_removing = True
    while continue_removing:
        movie_to_be_removed = input("Please enter the name of the movie you want to remove:")
        movie_found = find_the_movie_by_name(movie_to_be_removed)
        if movie_found:
            database.remove(movie_found)
            print("movie removed successfully!")
        else:
            print("Not found!")
        print("Do you want to remove more movies: ")
        continue_removing = yes_no()

def view_movies(database):
    print("You are currently viewing the movie database of Umang A") # add the functionality to display the properties in presentable way
    for movie in database:
        movie_name = movie["title"]
        movie_director = movie["director"]
        movie_duration = movie["duration"]
        print(f"Movie : {movie_name.title()}  ||  "
              f"director : {movie_director.title()}  ||  "
              f"duration : {movie_duration} ")
'''
4 available function:

1. add movies to the database
2. remove movies from the database
3. view database
4. find the movie
5. quit the function/program
'''
end_program = False
while end_program != 1:
    user_input = input("What will you like me to do for you? arfvq ")
    if user_input == "a":
        add_movie_to_database(database_movies)
    elif user_input == "r":
        remove_movies_from_database(database_movies)
    elif user_input == "v":
        view_movies(database_movies)
    elif user_input == "f" :
        movie = input("Please enter the movie name you want to find: ")
        find_the_movie_by_name(movie)
    elif user_input == "q":
        end_program = True
    else:
        print("I am not programmed to do that.")

print("Bye!")
input()
print("[PROGRAM ENDED SUCCESSFULLY]")