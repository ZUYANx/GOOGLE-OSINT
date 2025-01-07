import requests
import time
import sys

# ANSI color codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def animate_text(text, color=WHITE, delay=0.05):
    """Display animated text on the screen."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def google_search(query, api_key, cx):
    """
    Perform a Google search using the Custom Search JSON API.
    :param query: Search query (email, phone number, username, etc.)
    :param api_key: API key from Google Cloud Console
    :param cx: Custom Search Engine ID
    :return: List of search results
    """
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cx
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        animate_text(f"Error: {response.status_code}", color=RED, delay=0.03)
        animate_text(response.text, color=YELLOW, delay=0.03)
        return []

def display_results(results):
    """Display search results with basic colors and animations."""
    if results:
        animate_text("\n=== SEARCH RESULTS ===", color=GREEN, delay=0.07)
        for i, item in enumerate(results, 1):
            animate_text(f"[{i}] {item.get('title')}", color=CYAN, delay=0.04)
            animate_text(f"    WEBSITE: {item.get('link')}", color=MAGENTA, delay=0.03)
            animate_text(f"    SNIPPET: {item.get('snippet')}\n", color=YELLOW, delay=0.03)
    else:
        animate_text("No results found or an error occurred.", color=RED, delay=0.05)

def main():
    # Replace with your actual API key
    api_key = "AIzaSyBLmcBVJtGglhV1cORPRUliai0--jeLGmo"  # Replace with your API key
    cx = "85c76cc2585784c61"         # Custom Search Engine ID from your link

    animate_text("Welcome to the Enhanced Search Tool!", color=GREEN, delay=0.07)
    query = input(f"{BLUE}Enter your search query (email, phone, or username): {RESET}")
    animate_text(f"Searching Google for: {query}", color=YELLOW, delay=0.05)
    
    results = google_search(query, api_key, cx)
    display_results(results)

if __name__ == "__main__":
    main()