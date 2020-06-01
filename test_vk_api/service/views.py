import os
from django.shortcuts import render, redirect
from django.core.cache import cache
from functools import wraps
import requests
from urllib import parse


client_id = os.environ.get("VK_CLIENT_ID")
redirect_uri = os.environ.get("VK_REDIRECT_URI")
uri_authorize = "https://oauth.vk.com/authorize"
uri_access_token = "https://oauth.vk.com/access_token"
uri_users_get = "https://api.vk.com/method/users.get"
uri_friends_get = "https://api.vk.com/method/friends.get"
version = "5.107"


def question_token(func):
    @wraps(func)
    def wrapping(request):

        session_user_id = request.session.get('user_id')

        if session_user_id and cache.get(session_user_id):
            return func(request)
        else:
            return redirect(sign_in_step_one)
    return wrapping


@question_token
def index(request):

    return render(
        request,
        "index.html",
        {
            "user": get_data_vk(
                uri_users_get, {
                    "access_token": cache.get(request.session.get('user_id')),
                    "fields": ["lists"],
                    "v": version,
                }
            ).json()["response"][0],
            "friends": get_data_vk(
                uri_friends_get, {
                    "access_token": cache.get(request.session.get('user_id')),
                    "order": "random",
                    "count": 5,
                    "fields": ["first_name", "last_name"],
                    "v": version,
                }
            ).json()["response"]
        }
    )


def sign_in_step_one(request):
    return render(
        request,
        "sign_in.html",
        {"link": get_link_auth_user_vk({
            "client_id": client_id,
            "display": "popup",
            "redirect_uri": redirect_uri,
            "scope": "friends",
            "response_type": "code",
            "v": version,
        })}
   )


def sign_in_step_two(request):
    data = get_data_vk(
        uri_access_token, {
            "client_id": client_id,
            "client_secret": os.environ.get("VK_SECRET_KEY"),
            "redirect_uri": redirect_uri,
            "code": request.GET.get("code"),
            "v": version,
        }
    ).json()

    if data.get("user_id"):

        request.session["user_id"] = data.get("user_id")

        cache.set(
            data.get("user_id"),
            data.get("access_token"),
            timeout=data.get("expires_in")
        )

        return redirect("/")

    else:
       return render(
           request,
           "index.html",
           {"data": f"Error: {data.get('error')}, {data.get('error_description')}"}
       )


def get_data_vk(uri, params):
    return requests.get(uri, params=params)


def get_link_auth_user_vk(params):
    return f"{uri_authorize}?{parse.urlencode(params)}"
