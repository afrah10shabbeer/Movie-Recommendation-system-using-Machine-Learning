

# # Importing dependencies


import numpy as np
import pandas as pd
import difflib # To find the initial closest match of user input movie from the dataset
from sklearn.feature_extraction.text import TfidfVectorizer # To convert textual vector to numerical vector
from sklearn.metrics.pairwise import cosine_similarity # To use cosine similarity
from tkinter import messagebox
import random as rd


# ---------------------------------- Data Collection and preprocessing ----------------------------------------


# Merging two DataFrames
df_movies = pd.read_csv("../Movie_recommendation_system/tmdb_5000_movies.csv")
df_credits = pd.read_csv("../Movie_recommendation_system/tmdb_5000_credits.csv")

# Renaming column name from "id" to "movie_id"
df_movies = df_movies.rename(columns = {"id":"movie_id"})

# Merging two DataFrames for efficient recommendation 
movie_df = pd.merge(df_movies,df_credits,on = "movie_id")

movie_df = movie_df.drop(["title_x","title_y"],axis = 1)


# ------------------------------------- Extracting top 10 most rated movies, If the movie specified by the user is 
# not available in the dataset, then we will be recommending top 10 movies------------------------------------------


rating_df = movie_df.sort_values(by = ["vote_count"],ascending = False)
top_10_movies = rating_df["original_title"].head(10).tolist()

# Considering only relevant features
relevant_features = ['genres','keywords','tagline','cast','director']


# Filling all NaNs with empty string to all columns
for column in movie_df.columns:

    if movie_df[column].isnull().any() == True:
        movie_df[column] = movie_df[column].fillna('')


# Combining all the selected features
combined_features = movie_df["genres"] + " " + movie_df["keywords"] + " " + movie_df["tagline"]+ " " +movie_df["cast"]+" "+movie_df["production_companies"]


# Converting the textual data to numerical data
vectorizer = TfidfVectorizer()


feature_numerical_vectors = vectorizer.fit_transform(combined_features)


# -------------------------- Applying cosine similarity -------------------------------------------


# Getting the similarity scores using cosine similarity
similarity = cosine_similarity(feature_numerical_vectors)


# Getting a list of all the movie names mentioned in the dataset
list_of_all_movies = movie_df["original_title"].tolist()



# ------------------------------------ MOVIE PROCESSING --------------------------------------------

# favt_movie_name = input("Enter your favorite movie name:")
def show_popup():
    messagebox.showinfo("Movie not found" , "The movie which you've specified is not found in the dataset, As a result we recommend you to watch these top 10 rated movies!")


def get_recommendation(favt_movie_name):

    # Finding closest match for the movie name given by the user
    find_match_movies = difflib.get_close_matches(favt_movie_name,list_of_all_movies)


    # ---------------- User specified movie was not mentioned in the IMDB dataset, In this case display the top 10 rating moves----------
    if len(find_match_movies) == 0: 
        show_popup()

        top_movies_list_of_tuples = []

        for top_movie in top_10_movies:
            top_movies_list_of_tuples.append((top_movie,rd.uniform(0.81,0.99)))

        return top_movies_list_of_tuples

    closest_match_movie = find_match_movies[0]


    # Finding the index of the movie provided by the user
    index_of_favt_movie = movie_df[movie_df["original_title"] == closest_match_movie].index[0]



    # -------------------------------- Getting similarity row of particular index_of_favt_movie -------------------------------------

    # Here enumerate() is used to get both the index and the corresponding similarity score of each movie, returns a list of tuples(index,similarity score)
    similarity_score_of_favt_movie = list(enumerate(similarity[index_of_favt_movie]))



    # Sorting the list in decreasing order, so that we can choose the top most similar movies which has highest similarity score
    sorted_similar_movies = sorted(similarity_score_of_favt_movie, key = lambda x:x[1],reverse=True)


    # ------------------------------- Retrieving top similar movies with that of given movie -----------------------------------------


    # Print the names of similar movies based on index value

    i = 1

    result_list = []
    for movie in sorted_similar_movies:
        
        index = movie[0]
        similarity_num = movie[1]
        recommended_movie = movie_df.iloc[index]["original_title"]
        
        if recommended_movie == closest_match_movie:
            continue
            
        if(i < 11):
            # print(recommended_movie,similarity_num)
            movie_weight_pair = (recommended_movie,similarity_num)
            result_list.append(movie_weight_pair)
            i += 1

            # print(movie_weight_pair)
        else:
            break
    
    return result_list




# if __name__ == "__main__":

    