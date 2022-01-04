import requests


class GitHubAPI():
    def getUserRepositories(self, username):
        page = 1
        r = requests.get(f'https://api.github.com/users/{username}/repos?per_page=100&page={page}')    
        data = r.json()

        while r.json():
            page += 1
            r = requests.get(f'https://api.github.com/users/{username}/repos?per_page=100&page={page}')
            data += r.json()
        
        return data
