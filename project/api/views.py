from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from . github import GitHubAPI


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List of repositories': '/<username>/repositories/',
        'Sum of stars': '/<username>/sum-of-stars/',
        'The most popular programming languages': '/<username>/programming-languages/'
    }
    return Response(api_urls)


@api_view(['GET'])
def userRepositories(request, username):
    github = GitHubAPI()
    repositories = github.getUserRepositories(username)
    data = []
    
    for repository in repositories:
        extracted = {
            "name": repository["name"],
            "stars": repository["stargazers_count"]
        }

        data.append(extracted)

    return Response(data)


@api_view(['GET'])
def userSumOfStars(request, username):
    github = GitHubAPI()
    repositories = github.getUserRepositories(username)
    star_counter = 0

    for repository in repositories:
        star_counter += repository["stargazers_count"]
    
    return Response({"sum_of_stars": star_counter})


@api_view(['GET'])
def userProgrammingLanguages(request, username):
    github = GitHubAPI()
    repositories = github.getUserRepositories(username)
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
