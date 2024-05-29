import os
import numpy as np
import pandas as pd
import random
from surprise import Dataset, NormalPredictor, Reader
from surprise.model_selection import cross_validate
from collections import defaultdict
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split



def data_frame_sample(df, fraction):
    df = df.sample(frac=fraction, replace=True)
    return df

def concat_with_user_rating(df, user_rating):
    listOfTuples = [("newUser", movieId, rating) for movieId, rating in user_rating.items()]
    user_df = pd.DataFrame(listOfTuples, columns =["userID", "itemID", "rating"])
    concated_df = pd.concat([df, user_df])
    return concated_df

def get_top_n(predictions, n=20):
    top_n = [(iid, est) for uid, iid, true_r, est, _ in predictions]
    top_n.sort(key=lambda x: (x[1], random.random()), reverse=True)

    return top_n[:n]

def fit_model_and_predict(concated_df, ratings):

    reader = Reader(rating_scale=(1, 10))
    data = Dataset.load_from_df(concated_df[["userID", "itemID", "rating"]], reader)
    trainset, testset = train_test_split(data, test_size=0.01)
    algo = SVD()
    algo.fit(trainset)

    all_movies = data.build_full_trainset().build_testset()
    # Remove the movies that the user has already rated
    unseen_movies = [movie for movie in all_movies if movie[1] not in ratings]
    prediction_set = [("newUser", x, 0) for x in unseen_movies]
    # Predict ratings for unseen movies using the updated model
    predictions = algo.test(unseen_movies)
    # Get top N recommendations for the unseen movies
    top_n = get_top_n(predictions, n=10)
    # Print the top N recommendations
    return top_n


def get_recommendations(ratings):
    file_path = os.path.join(os.path.dirname(__file__), 'top_user_processed.csv')
    df = pd.read_csv(file_path)
    df = data_frame_sample(df, 0.01)
    new_df = concat_with_user_rating(df, ratings)
    return fit_model_and_predict(new_df, ratings)

if __name__ == '__main__':
    # loading top users' data
    df = pd.read_csv("top_user_processed.csv")
    df = data_frame_sample(df, 0.01)

    ratings = {"get-out-2017":7,"parasite-2019":9,"pulp-fiction":10,"interstellar":10,"the-truman-show":9,"the-wolf-of-wall-street":9,"inception":9,"the-dark-knight":9,"whiplash-2014":8,"joker-2019":8,"fight-club":8,"la-la-land":8,"everything-everywhere-all-at-once":7}
    new_df = concat_with_user_rating(df, ratings)
    print(fit_model_and_predict(new_df, ratings))

