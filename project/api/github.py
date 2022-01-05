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

        if r.status_code == 200:
            data = r.json()

            while r.json():  # Check if there are more pages
                page += 1
                r = requests.get(f'https://api.github.com/users/{username}/repos?per_page=100&page={page}')
                
                if r.status_code == 200:
                    data += r.json()
                else:
                    error = self.errorHandler(r.status_code)
                    return error
        
        else:
            error = self.errorHandler(r.status_code)
            return error
        
        return data

    def errorHandler(self, status_code: int) -> Dict: 
        """
        Returns information about the error resulting from the status code.

                Parameters:
                        status_code: request status code
                
                Returns: Dict with information about error and error code
        """
        
        error = {
            "info": "Something went wrong with GitHub API",
            "error_code": status_code
        }

        if status_code == 404:
            error["info"] = "User not found"

        return error
