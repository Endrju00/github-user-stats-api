import requests
from django.test import TestCase
from django.urls import reverse

from api.github import GitHubAPI


# Create your tests here.
class ApiTests(TestCase):
    def test_connection(self):
        """
        Downlads the data from GitHub API, then checks if downloaded data is correct.
        """
        r = requests.get('https://api.github.com/users/allegro')
        data = r.json()
        self.assertEqual(data.get("id"), 562236)

    def test_api_overview(self):
        """
        Checks if the response status code from API Overview view is correct.
        """
        response = self.client.get(reverse('api:api-overview'))
        self.assertEqual(response.status_code, 200)
    
    def test_user_repositories(self):
        """
        Checks if the response status code from User Repositories view is correct.
        """
        response = self.client.get(reverse('api:user-repositories', kwargs={'username': 'allegro'}))
        self.assertEqual(response.status_code, 200)
    
    def test_user_stars(self):
        """
        Checks if the response status code from User Stars view is correct.
        """
        response = self.client.get(reverse('api:user-stars', kwargs={'username': 'allegro'}))
        self.assertEqual(response.status_code, 200)

    def test_user_programming_languages(self):
        """
        Checks if the response status code from User Programming Languages view is correct.
        """
        response = self.client.get(reverse('api:user-programming-languages', kwargs={'username': 'allegro'}))
        self.assertEqual(response.status_code, 200)
