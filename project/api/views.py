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
        d = {}
        d["name"] = repository["name"]
        d["stars"] = repository["stargazers_count"]
        data.append(d)

    return Response(data)


@api_view(['GET'])
def userSumOfStars(request, username):
    github = GitHubAPI()
    repositories = github.getUserRepositories(username)
    star_counter = 0

    for repository in repositories:
        star_counter += repository["stargazers_count"]
    
    return Response({"sum_of_stars": star_counter})