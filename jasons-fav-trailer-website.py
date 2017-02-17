import fresh_tomatoes
import media

blade_runner = media.Movie(
    "Blade Runner",
    "Do androids dream of electric sheep?",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
    "https://www.youtube.com/watch?v=eogpIG53Cis")

alien = media.Movie(
    "Alien",
    "In space no one can hear you scream.",
    "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
    "https://www.youtube.com/watch?v=bEVY_lonKf4")

pulp_fiction = media.Movie(
    "Pulp Fiction",
    "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of \
    diner bandits intertwine in four tales of violence and redemption.",
    "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
    "https://www.youtube.com/watch?v=wZBfmBvvotE")

rogue_one = media.Movie(
    "Rogue One",
    "Rebels out on a mission to steal the plans for the Death Star.",
    "http://ia.media-imdb.com/images/M/MV5BMjQyMzI2OTA3OF5BMl5BanBnXkFtZTgwNDg5NjQ0OTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # N0QA
    "https://youtu.be/9MqVeJeDfio")

the_godfather = media.Movie(
    "The Godfather",
    "The aging patriarch of an organized crime dynasty transfers control of his\
    clandestine empire to his reluctant son.",
    "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
    "https://www.youtube.com/watch?v=sY1S34973zA")

raiders_of_the_lost_ark = media.Movie(
    "Raiders of the Lost Ark",
    "Archaeologist and adventurer Indiana Jones is hired by the U.S. government\
    to find the Ark of the Covenant before the Nazis.",
    "http://ia.media-imdb.com/images/M/MV5BMjA0ODEzMTc1Nl5BMl5BanBnXkFtZTcwODM2MjAxNA@@._V1_SY1000_CR0,0,664,1000_AL_.jpg",  # N0QA
    "https://youtu.be/0ZOcoxjeUYo")

predator = media.Movie(
    "Predator",
    "A team of commandos on a mission in a Central American jungle find \
    themselves hunted by an extraterrestrial warrior.",
    "http://ia.media-imdb.com/images/M/MV5BY2QwYmFmZTEtNzY2Mi00ZWMyLWEwY2YtMGIyNGZjMWExOWEyXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_SY1000_CR0,0,671,1000_AL_.jpg",  # N0QA
    "https://youtu.be/Y1txEAywdiw")

monty_python_and_the_holy_grail = media.Movie(
    "Monty Python and the Holy Grail",
    "King Arthur and his knights embark on a low-budget search for the Grail, \
    encountering many, very silly obstacles.",
    "http://ia.media-imdb.com/images/M/MV5BMTkzODczMTgwM15BMl5BanBnXkFtZTYwNTAwODI5._V1_.jpg",  # N0QA
    "https://youtu.be/zIbx7jU35X0")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Going back in time to meet authors",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # N0QA
    "https://www.youtube.com/watch?v=atLg2wQQxvU")

dumb_and_dumber = media.Movie(
    "Dumb and Dumber",
    "The cross-country adventures of two good-hearted but incredibly stupid \
    friends.",
    "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
    "https://www.youtube.com/watch?v=PbA63a7H0bo")

# Prepares movies as well as determines their order on the webpage
movies = [blade_runner, alien, the_godfather, rogue_one,
          raiders_of_the_lost_ark, predator, midnight_in_paris,
          monty_python_and_the_holy_grail, dumb_and_dumber, ]

fresh_tomatoes.open_movies_page(movies)
