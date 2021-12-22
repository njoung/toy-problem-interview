import requests
from datetime import datetime


BASE_URL = "http://upshop-interviews.herokuapp.com"

API_URL = "http://upshop-interviews.herokuapp.com/api/reviews/v3"

LEFT_ARROW = "\x1b[C"
RIGHT_ARROW = "\x1b[D"


def get_full_url(page_url):
    return BASE_URL + page_url


# return data and page info
def fetch_reviews_for_page(page_url):
    while True:
        json_response = requests.get(page_url).json()
        if json_response.get("error"):
            # TODO: specify max number of times to retry
            continue
        return (json_response["data"], json_response["pageInfo"])

    return [[], None]


def parse_date(unixtime):
    # Just assume we want timestamps in utc
    return datetime.utcfromtimestamp(unixtime).strftime("%B %d %Y")


if __name__ == "__main__":

    page_url = API_URL
    while True:
        print(page_url)

        # fetch first page
        # print it out
        # then pause while waiting for input

        (reviews, page_info) = fetch_reviews_for_page(page_url)
        print(page_info)
        for r in reviews:
            # TODO: ideally we'd have a review object and a print function on it
            print(r["reviewerName"])
            rating = r["overall"]
            print(rating)
            parsed_date = parse_date(r["unixReviewTime"])
            print(f"Reviewed on {parsed_date}")
            print(r["summary"])
            print(r["reviewText"])
            print("***")

        prev_page = None
        if page_info["hasPrevPage"]:
            print("Press p to go back")

        if page_info["hasNextPage"]:
            print("Press n to go forward")

        user_key = str.rstrip(input())
        if user_key == "p" and page_info["hasPrevPage"]:
            page_url = get_full_url(page_info["prevPageUrl"])
            print("Fetching previous page")
        elif user_key == "n" and page_info["hasNextPage"]:
            page_url = get_full_url(page_info["nextPageUrl"])
            print("Fetching next page")
        else:
            print(user_key)
            # TODO: handle this case
            raise Exception("Wrong input")

