import pandas as pd


#1. First, download the movie_plots.csv file from Canvas and open it
movies_plot = pd.read_csv("movie_plots.csv")

#2. Let's inspect the data. Display the first rows and get the summary (.info)
print("===========Opdracht 2=============")
print(movies_plot.head())
print(movies_plot.info())

#3. Print out the number of movies for each Origin/Ethnicity
print("===========Opdracht 3=============")
print(movies_plot['Origin/Ethnicity'].value_counts())

#4. Subsetting: select only the rows with Bollywood movies
print("===========Opdracht 4=============")
bollywood_movies = movies_plot[movies_plot["Origin/Ethnicity"] == "Bollywood"]
print(bollywood_movies.head())

#5. Subsetting: select only the rows with Turkish movies released after 2000
print("===========Opdracht 5=============")
turkish_movies = movies_plot [(movies_plot["Origin/Ethnicity"] == "Turkish") & (movies_plot['Release Year'] >= 2000)]
print(turkish_movies.head())

#6. Subsetting: create a new df with only Title, Release Year, Origin/Ethnicity, Plot
new_movies_plot = movies_plot[['Title', 'Release Year', 'Origin/Ethnicity', 'Plot']]

#7. Change the column names to Title, Year, Origin, Plot. Find online how to this.
print("===========Opdracht 7=============")
new_movies_plot = new_movies_plot.rename(columns={'Release Year':'Year', 'Origin/Ethnicity':'Origin'})
print(new_movies_plot.head())
print(new_movies_plot.info())
##This is where the basic section ends.##

##Advanced section: for a more challenging assignment, try (some of) the steps below##

#8. Create a new column "kimono" that is True if the Plot contains the word "kimono"
#and false if not (tip: find a suitable Pandas string method).
#Tip: use Pandas .astype(int) to convert the resulting Boolean in 0 or 1.
print("===========Opdracht 8=============")
new_movies_plot["Kimono"] = new_movies_plot["Plot"].str.contains("kimono")
new_movies_plot["Kimono"] = new_movies_plot["Kimono"].astype(int)
print(new_movies_plot["Kimono"].value_counts())

#9. Using your new column, pd.groupby() and another Pandas function, count the number of movies
#with "kimono" in the plot, for the different origins.
print("===========Opdracht 9=============")
kimono_plot = new_movies_plot.groupby("Origin")["Kimono"]
print(kimono_plot.value_counts())

#10. Using your earlier code, create a function add_word_present() with one argument (word),
#that adds a column df[word] with a 1 if the word occurs in the plot,
#and 0 if not.
#Extra challenge: make sure that it's not counted if it's inside another word.
print("===========Opdracht 10=============")
def add_word_present(input):
    new_movies_plot["Word"] = new_movies_plot["Plot"].str.contains(input)
    new_movies_plot["Word"] = new_movies_plot["Word"].astype(int)
    print("Selected word =",  input)
    print(new_movies_plot["Word"].value_counts())
add_word_present("agent")

#11. Write another function compare_origins() with one argument (word), that:
#1. adds a column to your data frame (simply call your earlier function)
#2. prints the proportion of movies for different origins containing that word
print("===========Opdracht 11=============")
def compare_origins(input):
    new_movies_plot["Origin_Word"] = new_movies_plot["Plot"].str.contains(input)
    new_movies_plot["Origin_Word"] = new_movies_plot["Origin_Word"].astype(int)
    origin_word = new_movies_plot.groupby(["Origin"])["Origin_Word"].value_counts()
    print("Selected word =",  input)
    print(origin_word)
compare_origins("samurai")

#12. We need one more tweak: to really compare different cultures,
#we need to account for the fact that the total number of movies is not the same.
#Write another, better function that calculates a percentage rather than a count.
#Hint: note that df.groupby(["Origin"])[word].count() will get you the number of movies, grouped by origin.
#Also sort the result so that the percentage is descending.
#Finally, make it user-friendly: print the word and what the numbers mean
print("===========Opdracht 12=============")
def compare_origins2(input):
    new_movies_plot["Origin_Word2"] = new_movies_plot["Plot"].str.contains(input)
    new_movies_plot["Origin_Word2"] = new_movies_plot["Origin_Word2"].astype(int)
    origin_word = new_movies_plot.groupby(["Origin"])["Origin_Word2"].value_counts(normalize=True, ascending=False)
    print("Selected word =",  input)
    print("0 = False(Select word is not in the plot)", "1 = True(Select word is in the plot)",)
    print("Results are shown in percentages")
    print(origin_word)
compare_origins2("detective")
    
#You're done! Try out your function and paste your most interesting result
#as a comment

