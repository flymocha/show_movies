#!/usr/local/bin/python

import media
import fresh_tomatoes

toy_story = media.Movies("Toy Story", 
                        "A story of boy and his toys come to life", 
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print (toy_story.storyline)

avatar = media.Movies("Avatar",
                      "A marine on an alien planet",
                      "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=aVdO-cx-McA&list=TLcJzi8xrznj7GntSwS9A6Ffoc6vpwazbn")

#print(avatar.trailer_youtube_url)

#avatar.show_trailer()


school_of_rock = media.Movies("School of Rock",
                              "Using rock music to learn",
                              "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                              "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movies("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=cxbruOoXfOA")

midnight_in_paris = media.Movies("Midnight in Paris",
                                 "Going back in time to meet authors",
                                 "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
"https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movies("Hunger Games",
                            "A really real reality show",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                            "https://www.youtube.com/watch?v=C_Tsj_wTJkQ")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)

print(media.Movies.VALID_RATINGS)
