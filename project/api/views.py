from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from typing import AnyStr

from . github import GitHubAPI


# Create your views here.
@api_view(['GET'])
def apiOverview(request) -> Response:
    """
    Simple API overview.
            
            Parameters:
                    request: Django request for a page
            
            Returns:
                    Response(data): Django Rest Framework response - API Overview content
    """

    api_urls = {
        'List of repositories': '/<username>/repositories/',
        'Sum of stars': '/<username>/sum-of-stars/',
        'The most popular programming languages': '/<username>/programming-languages/'
    }
    return Response(api_urls)


@api_view(['GET'])
def userRepositories(request, username: AnyStr) -> Response:
    """
    Returns response with data (name and number of stars) regarding the repositories of a specific user.
            
            Parameters:
                    request: Django request for a page
                    username: GitHub username for which the data will obtained
            
            Returns:
                    Response(data): Django Rest Framework response - name and number of stars of user's every public repository or info with the error code
    """

    github = GitHubAPI()
    repositories = github.getUserRepositories(username)
    
    if repositories[0].get("error_code"):
        return Response(repositories[0])
    else:
        data = []
        
        for repository in repositories:
            extracted = {
                "name": repository["name"],
                "stars": repository["stargazers_count"]
            }

            data.append(extracted)

        return Response(data)


@api_view(['GET'])
def userSumOfStars(request, username: AnyStr) -> Response:
    """
    Returns response with data (sum of stars) regarding the specific user.
            
            Parameters:
                    request: Django request for a page
                    username: GitHub username for which the data will obtained
            
            Returns:
                    Response(data): Django Rest Framework response - user's sum of stars or info with the error code
    """

    github = GitHubAPI()
    repositories = github.getUserRepositories(username)

    if repositories[0].get("error_code"):
        return Response(repositories[0])
    else: 
        star_counter = 0

        for repository in repositories:
            star_counter += repository["stargazers_count"]
        
        return Response({"sum_of_stars": star_counter})


@api_view(['GET'])
def userProgrammingLanguages(request, username: AnyStr) -> Response:
    """
    Returns response with data (the sum of the sizes of repositories with the same main programming languages) regarding the specific user.
            
            Parameters:
                    request: Django request for a page
                    username: GitHub username for which the data will obtained
            
            Returns:
                    Response(data): Django Rest Framework response - user's favourite programming languages or info with the error code
    """

    github = GitHubAPI()
    repositories = github.getUserRepositories(username)

    if repositories[0].get("error_code"):
        return Response(repositories[0])
    else:
        languages = {}

        for repository in repositories:
            if not repository["language"]:
                continue
            elif languages.get(repository["language"]):
                languages[repository["language"]] += repository["size"]
            else:
                languages[repository["language"]] = repository["size"]
        
        languages = dict(sorted(languages.items(), key=lambda k: (k[1], k[0]), reverse=True))  # Sort descending by size

        return Response(languages)
