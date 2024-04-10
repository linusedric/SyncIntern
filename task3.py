import requests

def shorten_url(url):
    """
    Shortens a URL using the TinyURL API.
    
    Args:
    url (str): The URL to be shortened.
    
    Returns:
    str: The shortened URL.
    """
    try:
        response = requests.get(f"http://tinyurl.com/api-create.php?url={url}")
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to shorten URL. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Get URL input from the user
url = input("Enter the URL to be shortened: ")

# Shorten the URL
shortened_url = shorten_url(url)

# Print the shortened URL
if shortened_url:
    print("Shortened URL:", shortened_url)
