## Purpose 
This challenge is intended to be used as part of the onsite evaluation for engineering candidates. 

The aim is to get signal on a candidate's ability to 
- break down a problem
- write code quickly
- work with APIs
- debug (we're assuming they'll make some mistakes)
- adapt their code as new requirements are released
- look up documentation and leverage third party libraries

## Setting Context
We should share the first part of the question with the candidate in a Google Doc. Let them know that there are 3 parts and we can see how much they get through. We'll share each part as they go along.

They can use whichever language, frameworks or libraries that are best for the job (SPEED). They can Google stuff if they'd like. 

They should focus on **speed** and getting something working. We can always discuss optimizations and code quality later. Saying that, there is some minimum bar for quality. They shouldn't have everything in main.

Let them know it's probably better if they talk through things at the end rather than narrating their whole approach since that'll probably be slower. 

## Heroku
The challenge server is hosted on Heroku on the free tier. It can take some time to warm up if it hasn't received traffic in the last 30 minutes so try and ping the server before the interview starts.
http://upshop-interviews.herokuapp.com/api/reviews/v1

## Evaluation
In one hour, a good candidate should be able to get through parts 1 and 2. If they are able to make their way through part 3 while writing clean code, that's great positive signal. Unless we extend the time for this challenge beyond 1 hour, it's highly unlikely anyone will ever make it to part IV.

For reference, Jeremy going through all the problems without writing the cleanest code(!) but with knowledge of the problem took 1 hour to complete all parts (25 minutes for Part I, 10 minutes for Part II, 5 minutes for Part III, 20 minutes for Part IV)

## Answers:

### Part I
```
Number of reviews: 50
Average rating: 4.26
```

### Part II
```
Number of reviews: 69
Average rating: 4.072463768115942
```

### Part III
```
Number of reviews: 81
Average rating: 4.296296296296297
```

# Reviews Challenge

Customer reviews are an essential part of the e-commerce experience. They can help new customers in their purchasing decisions and also inform merchants which brands and lines are worth investing in. 

## Approach
For this challenge, we're really trying to see your ability to build something from the ground up quickly. There are multiple parts to this challenge and while we don't have to get through all of them, it'd be great to see what progress you can make during the time.

You can choose any language, framework or library that you think will help you achieve this goal. Feel free to Google or look on Stack Overflow while you're working on this challenge.

We recommend focusing on getting something working (we'll leave it to you to decide what is the appropriate code quality) and we can discuss/refactor/optimize later.

## Part I
Moonship wants to build out its own reviews feature and we'd like your help! We currently have an API which returns reviews data for a specific product in JSON format: 

http://upshop-interviews.herokuapp.com/api/reviews/v1

We'd like you to write a script that calls this API and prints out to console some of the details for each review, a separator between the reviews and some aggregate statistics at the bottom.

For each review, you'll need to print
- reviewer's name
- rating
- when it was reviewed
- summary of the review
- body of the review


```
Bob
4 stars
Reviewed on January 10, 2014
Only ok
Yeah I think it was just ok. At least shipping was fast
***
jellybean835
5 stars
Reviewed on November 20, 2012
I like it!!
It was very good. I would recommend it for anyone to buy.
***
Number of reviews: 2
Average rating: 4.5
```

## Part II
**Please create a new file for your solution to Part II or use git to commit your changes for each part of your solution.**

Our API is now paginated. Please query the new API for all the information (i.e. all the pages) and print out the review information and aggregate statistics as in Part I.

The new API you should be using can be found at http://upshop-interviews.herokuapp.com/api/reviews/v2


The JSON payload for the API now contains a pageInfo object similar to the following
e.g.
```
{
  "data": [....],
  "pageInfo": {
    "hasNextPage": true, 
    "hasPrevPage": false, 
    "nextPageUrl": "/api/reviews/v2?page=2", 
    "prevPageUrl": null
}


```

## Part III
**Please create a new file for your solution to Part III or use git to commit your changes for each part of your solution.**

Our paginated API is now dealing with heavy load and occasionally rate limits users. Please handle the scenario where you encounter rate limits while calling the API and print out the review information and aggregate statistics as before.

The new API you should be using can be found at http://upshop-interviews.herokuapp.com/api/reviews/v3

The rate limit error will have a 429 error code and be in the format
```
{"error":"You have exceeded the rate limit for this endpoint. Please try again later"}
```

## Part IV
**Please create a new file for your solution to Part IV or use git to commit your changes for each part of your solution.**

Extend on part III by building a terminal program that allows users to paginate/query over the data in real-time. 

*You no longer need to print the aggregate statistics*

The program should look something like this
```
Fetching page

Bob
4 stars
Reviewed on January 10, 2014
Only ok
Yeah I think it was just ok. At least shipping was fast
***
jellybean835
5 stars
Reviewed on November 20, 2012
I like it!!
It was very good. I would recommend it for anyone to buy.
***

Press p to go to the previous page
Press n to go to the next page

n

Fetching next page
[...etc]

```

Where there is no previous page or next page, the program should ideally re-prompt the user for further input.

For user input, it's ok if the user has to hit enter/return after typing "p" or "n"

