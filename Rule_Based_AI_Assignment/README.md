# *Building Rule Based AI Using Python Assignment*

---

## Part 1 - Prompting The AI For Project Ideas (Three Project Ideas)

### 1. Basic Device Troubleshooting Assistant

  **How it works:**
	The user provides a problem to a device and it recognizes key words like wi-fi and provide pre-written responses

  **Rule Based Approach:**
  * System checks for key words
  * Provides Written Solutions


### 2. Move Recommendation System

  **How it works:**
  The user provides a single or set of categories, and the system will respond with a list of movies that fit those categories as recommendations for the user to watch based on what they would like to watch.
  
  **Rule Based Approach:**
  * The system checks for specific words in the user's input such as “action”, "comedy", etc.
  * The system matches the key word to its corresponding category and list of movies
  * If the system finds a match, it will provide a movie/show list in that genre
  * If the system doesn’t find a match it informs the user and provides default recommendations such as One Piece.
  * If the system finds “Thank you” In the user response the system will respond with “Your welcome” (For common courtesy).


### 3. Study Helper Chatbot
	
  **How it works:**
	The user provides a problem they have while studying and the system checks for key words such as lack of concentration, habits, etc. and recommends solutions for the problems that are proven to work.

  **Rule Based Approach:**
  * The system checks for key words such as habits, distraction, focus
  * Provides study solutions, and systems for the user based on the specific problems
  

  I chose **2. “Move Recommendation System”** for a couple reasons those being it is simple enough to create cleanly while learning the rule based system people used to use to create AI back then, yet complex enough to be creative and expand the system to be as complex and interactive as I want it (Combining categories), which I believe is perfect for what the assignment entails.
  
---

## Part 2 - Design Your Rule Based System

**Design -**

```text
IF the user enters action
    THEN recommend an action movie.

IF the user enters comedy
    THEN recommend a comedy movie.

IF the user enters horror or scary
    THEN recommend a horror movie.

IF the user enters family or kids
    THEN recommend a family movie.

IF the user enters sci-fi or science fiction
    THEN recommend a science fiction movie.

ELSE
    Give a default recommendation.
```

**Pseudocode -**

```text
Bool exit

Do while (exit = false)

Ask the user what type of movie they want to watch

If input contains "action" or "combat"
    Then recommend "action_movie_list"

If input contains "comedy" or "funny" or "silly"
    Then recommend "comedy_movie_list"

If input contains "horror" or "scary"
    Then recommend "horror_movie_list"

If input contains "family" or "kids" or "children"
    Then recommend "family_movie_list"

If input contains "sci-fi" or "science fiction"
    Then recommend "sciencefiction_movie_list"

If input does not match
    Then say "no matches found"
    Then say "These are the default recommendations"
    Then recommend "default_movie_list"

If input contains "exit" or "bye"
    Then say "Goodbye hope you have a great watch, come again soon!"
    Then exit = true
```

  ---

## Part 3 - Rules

**Sample Input & Output:**
```text
Input: Can you provide movies and shows that are funny or/and action pact
Output: 
- Movie/Recommendations -
Comedy:
Superbad
Talladega Nights
Step Brothers
	Action:
One Piece
John Wick
Mad Max
Die Hard

Input: Thank you
Output: 
No Genre Found
Default Recommendations -
1. …
2. …
3. …
You're welcome!
```
---

## Part 4 - Reflection

### Project Reflection:
The project is a rule based system that takes in user input and finds key words. The rules of the system state that if in the user input it finds a key word/category of a type of show or movie it will recommend movies in that genre. As long as the system contains the genre it will be able to provide an answer, if the user input does not contain any genre already in the system then the system will provide a default recommendations list. I added some more quality of life features as well and UX features such as if the user input contains anything along the lines of thank you the system will answer with your welcome at the end. 

For challenges I encountered while iterating on the project and prompting AI, there were a few the two main ones were structure and quality of life. The challenges and solutions are provided below.

**1. Structure**
While going back and forth with AI to create the code I encountered some parts of the program to be unintuitive and not complete. For example the code only ran once and recommended only 1 movie/show per category. This was an issue as it did not align with what I had envisioned the program to do. I had to add a while loop to the program, as well as movie lists for each category, now when a keyword is said in user input it will match the correct category and provide a list instead of one recommendation. It will also repeat until user inputs “exit” or “bye”

**2. Missing Quality Of Life:**
The system did not say anything if the user said thank you so I added the feature that if the user inputs “Thank you” or “Thanks”  the AI rule based system will say “Your welcome”.
