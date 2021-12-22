import requests
from datetime import datetime

# from collections import namedtuple

API_URL = "http://upshop-interviews.herokuapp.com/api/reviews/v1"

# Review = namedtuple('Review', 'name, age, title, department, paygrade')


def fetch_reviews():
    data = requests.get(API_URL)
    return data.json()["data"]


def parse_date(unixtime):
    # Just assume we want timestamps in utc
    return datetime.utcfromtimestamp(unixtime).strftime("%B %d %Y")


if __name__ == "__main__":
    reviews = fetch_reviews()

    sum_ratings = 0

    for r in reviews:
        print(r["reviewerName"])
        rating = r["overall"]
        print(rating)
        parsed_date = parse_date(r["unixReviewTime"])
        print(f"Reviewed on {parsed_date}")
        print(r["summary"])
        print(r["reviewText"])
        print("***")
        sum_ratings += rating

    count_reviews = len(reviews)
    average_rating = sum_ratings / count_reviews
    print(f"Number of reviews: {count_reviews}")
    print(f"Average rating: {average_rating}")

