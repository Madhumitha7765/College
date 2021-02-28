# create dictionary and initialise
alice_ratings = {"alonzo": 1, "bob": 3, "turing": 2}
bob_ratings = {"alice": 1, "alonzo": 2, "turing": 3}
alonzo_ratings = {"alice": 3, "bob": 2, "turing": 1}
turing_ratings = {"alice": 2, "alonzo": 1, "bob": 3}
friends = {"alice": alice_ratings, "bob": bob_ratings, "alonzo": alonzo_ratings, "turing": turing_ratings}


# function that returns most popular student
def most_popular():
    # create dictionary 'results' whose keys=keys of 'friends' dictionary,value=0
    results = dict.fromkeys(friends.keys(), 0)

    # iterate through friends, value of friends to update values of results dictionary
    for key, value in friends.items():
        for name, rating in value.items():
            results[name] += rating
    # finding student with min rating with inbuilt min function
    min_rating = min(results.values())
    # assigning popular student with list comprehension
    popular = [key for key, value in results.items() if value == min_rating]

    return popular


if __name__ == '__main__':
    # printing return value of most_popular function
    print(str(most_popular()))
