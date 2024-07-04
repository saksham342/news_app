# News Fetcher

This Python script fetches and displays news articles using the NewsAPI based on user input for the topic and date range.

## Features

- Fetch news articles based on a specified topic.
- Retrieve news from a specified date range.
- Display detailed information about each news article including the source, author, title, description, content, URL, and published date.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/saksham342/news_app.git
    ```
2. Navigate to the project directory:
    ```
    cd news_app
    ```
3. Install the required library:
    ```
    pip install requests
    ```

## Usage

1. Replace `"your_api_key_here"` with your actual NewsAPI key in the `main_function()`:
    ```python
    my_api_key = "your_api_key_here"
    Regsiter and get your api key: https://newsapi.org
    ```
2. Run the script:
    ```
    python script.py
    ```
3. Follow the prompts to enter the news topic and the number of days back you want to fetch the news for.

## Example

```sh
$ python script.py
Enter your news topic: technology
Enter how many days back news you want to read: 2
