import requests
from datetime import datetime


BASE_URL = "http://upshop-interviews.herokuapp.com"

API_URL = "http://upshop-interviews.herokuapp.com/api/reviews/v2"


def get_full_url(page_url):
    return BASE_URL + page_url


def fetch_reviews():
    # go through and fetch data until there's no more pages
    reviews = []
    page_url = API_URL
    while True:
        json_response = requests.get(page_url).json()
        reviews += json_response["data"]
        page_info = json_response["pageInfo"]  # TODO: I'll change this to be pageInfo

        if not page_info["hasNextPage"]:
            break

        relative_page_url = page_info["nextPageUrl"]
        page_url = get_full_url(relative_page_url)
    return reviews


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
