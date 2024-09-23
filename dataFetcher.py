import requests

def fetch_github_user(username):
   
    url = f"https://api.github.com/users/{username}"
    
    try:
       
        response = requests.get(url)

       
        if response.status_code == 200:
            user_data = response.json()
            print(f"User: {user_data['login']}")
            print(f"Name: {user_data['name']}")
            print(f"Public Repos: {user_data['public_repos']}")
            print(f"Followers: {user_data['followers']}")
            print(f"Following: {user_data['following']}")
            print(f"Profile URL: {user_data['html_url']}")
        elif response.status_code == 404:
            print(f"Error 404: The GitHub account '{username}' does not exist. Please provide a valid username.")
        else:
            print(f"Error {response.status_code}: Unable to fetch data. Something went wrong.")
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


username = input("Enter GitHub username: ")
fetch_github_user(username)
