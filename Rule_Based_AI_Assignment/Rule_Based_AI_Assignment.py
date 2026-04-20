
# - Rule Based AI Assignment -

print("\n\n- Welcome to the Movie/Show Recommendation System! -\n")

print("Enter one or more genres like: action, comedy, horror, family, sci-fi")
print("Example: funny and scary")
print("Enter: 'Bye' or 'Exit' to exit the AI recommendation assistant\n\n")

exit = False


# User input
while True:
    user_input = input("What type of movie or show would you like to watch next? ").lower()

    # Movie lists
    action_movies = [
        "One Piece",
        "John Wick",
        "Mad Max: Fury Road",
        "Die Hard"
    ]

    comedy_movies = [
        "Superbad",
        "Talladega Nights",
        "Step Brothers"
    ]

    horror_movies = [
        "The Conjuring",
        "The Conjuring 2",
        "IT"
    ]

    family_movies = [
        "Toy Story",
        "Finding Nemo",
        "Shrek"
    ]

    scifi_movies = [
        "Interstellar",
        "The Matrix",
        "Blade Runner 2049"
    ]

    # Store matches
    recommendations = {}

    # Rule-based keyword checks
    if "action" in user_input or "combat" in user_input:
        recommendations["Action"] = action_movies

    if "comedy" in user_input or "funny" in user_input or "silly" in user_input:
        recommendations["Comedy"] = comedy_movies

    if "horror" in user_input or "scary" in user_input or "terror" in user_input:
        recommendations["Horror"] = horror_movies

    if "family" in user_input or "kids" in user_input or "children" in user_input:
        recommendations["Family"] = family_movies

    if "sci-fi" in user_input or "science fiction" in user_input:
        recommendations["Sci-Fi"] = scifi_movies


    # Output results
    if recommendations:
        print("\n--------- Movie/Show Recommendation List ---------")

        for genre, movies in recommendations.items():
            print(f"\n{genre}:")
            for movie in movies:
                print(f"- {movie}")

        print("\n")

        # Default if no matches
    else:
        print("\nNo genre matched.")
        print("--------- Default Recommendation List ---------")
        print("- One Piece")
        print("- John Wick")
        print("\n")

    if "bye" in user_input or "exit" in user_input:
        exit = True

    if exit == True:
        break

print("\nThanks for using the Movie/Show Recommendation System! See you again soon!\n\n")

