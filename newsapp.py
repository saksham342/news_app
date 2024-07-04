import requests
from datetime import datetime, timedelta
import json

def fetch_news(query, date, api_key):
    try:
        # Send a GET request to the NewsAPI endpoint with the query, date, and API key
        response = requests.get(f"https://newsapi.org/v2/everything?q={query}&from={date}&sortBy=popularity&apiKey={api_key}").json()
        
        # Iterate through each article in the response
        for article in response["articles"]:
            # Format the article details for printing
            to_print = f'''
Source: {article['source']['name']}
Author: {article["author"]}
Title: {article["title"]}
------------------------------
------------------------------
Description: {article["description"]}

Content: {article["content"]}
----------------------------------------------------------------------
----------------------------------------------------------------------
URL: {article["url"]}

Published At: {article["publishedAt"]}
______________________________________________________________________________________________________________________________________________________________________
______________________________________________________________________________________________________________________________________________________________________
            '''
            print(to_print)
    except Exception as e:
        # Handle specific network error
        if "([Errno 11001] getaddrinfo failed)" in str(e):
            print(f"News cannot be fetched. [Errno 11001] getaddrinfo failed")
        else:
            # Handle any other exceptions
            print(f"News cannot be fetched.\nReason: {e}")

def main_function():
    # Get the news topic from the user
    query = input("Enter your news topic: ")
    # Get the number of days back from the user
    days_back = int(input("Enter how many days back news you want to read: "))
    my_api_key = "your_api_key_here"
    today = datetime.today()
    # Calculate the date 'days_back' days before today
    previous_date = (today - timedelta(days=days_back)).strftime('%Y-%m-%d')
    # Fetch and display news based on user input
    fetch_news(query, previous_date, my_api_key)

if __name__ == "__main__":
    main_function()
