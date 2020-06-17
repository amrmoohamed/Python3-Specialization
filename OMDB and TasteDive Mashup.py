import requests_with_caching

def get_movies_from_tastedive(movie):
    baseurl = 'https://tastedive.com/api/similar'
    dictionary = {'q':movie, 'type':'movies', 'limit':'5'}
    resp = requests_with_caching.get(baseurl,dictionary)
    return resp.json()

def extract_movie_titles(movie):
    lst = [mov['Name'] for mov in movie['Similar']['Results']]
    return lst

def get_related_titles(movielist):
    lst1 = []
    lst2 = []
    for movie in movielist:
        lst1 = extract_movie_titles(get_movies_from_tastedive(movie))
        for mov in lst1:
            if mov not in lst2:
                lst2.append(mov)
    return lst2

def get_movie_data(movie):
    baseurl= "http://www.omdbapi.com/"
    dictionary = {'t':movie, 'r':'json'}
    resp = requests_with_caching.get(baseurl,dictionary)
    return resp.json()

def get_movie_rating(movie):
    rating = ''
    for ratinglist in movie["Ratings"]:
        if ratinglist["Source"]== "Rotten Tomatoes":
            rating = (ratinglist["Value"])
    if rating != '':
        rate = int(rating[:2])
    else:
        rate = 0
    return rate

def get_sorted_recommendations(movielist):
    sortedlist = sorted(get_related_titles(movielist), key = lambda movieName: (get_movie_rating(get_movie_data(movieName)), movieName), reverse=True)
    return sortedlist
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
