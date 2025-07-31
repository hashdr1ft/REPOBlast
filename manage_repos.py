import requests

# Replace with your GitHub username and Personal Access Token dawg.
USERNAME = ""
TOKEN = ""

def get_repositories():
    """Fetch all repositories for the user."""
    repos = []
    page = 1
    while True:
        response = requests.get(
            f"https://api.github.com/user/repos",
            auth=(USERNAME, TOKEN),
            params={"per_page": 100, "page": page}
        )
        if response.status_code != 200:
            print("Failed to fetch repositories.")
            print(f"Error: {response.json()}")
            break

        data = response.json()
        if not data:
            break

        repos.extend(data)
        page += 1

    return repos

def delete_repository(repo_name):
    """Delete a specific repository."""
    delete_url = f"https://api.github.com/repos/{USERNAME}/{repo_name}"
    response = requests.delete(delete_url, auth=(USERNAME, TOKEN))
    if response.status_code == 204:
        print(f"Deleted repository: {repo_name}")
    else:
        print(f"Failed to delete repository: {repo_name} - {response.status_code}")

def main():
    #this func fetches all repos either private or public depending upon the permissions given to the PAT
    repositories = get_repositories()

    if not repositories:
        print("No repositories found.")
        return

    # list repositories
    print("\nYour Repositories:")
    for idx, repo in enumerate(repositories, start=1):
        print(f"{idx}. {repo['name']}")

    # User selects repositories to delete
    try:
        to_delete = input("\nEnter the numbers of the repositories to delete (comma-separated): ")
        indices = [int(i.strip()) - 1 for i in to_delete.split(",")]

        for index in indices:
            if 0 <= index < len(repositories):
                delete_repository(repositories[index]["name"])
            else:
                print(f"Invalid choice: {index + 1}")

    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")

if __name__ == "__main__":
    main()
