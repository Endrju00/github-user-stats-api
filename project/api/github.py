import requests

from typing import AnyStr, List, Dict


class GitHubAPI():
    """
    Class for handling GitHub API
    """

    def getUserRepositories(self, username: AnyStr) -> List[Dict]:
        """
        Returns user repositories data.

            Parameters:
                    username: GitHub username for which the data will obtained
            
            Returns:
                    data: List of dicts with repository data
        """

        page = 1
        r = requests.get(f'https://api.github.com/users/{username}/repos?per_page=100&page={page}')    
        data = r.json()

        while r.json():  # Check if there are more pages
            page += 1
            r = requests.get(f'https://api.github.com/users/{username}/repos?per_page=100&page={page}')
            data += r.json()
        
        return data
