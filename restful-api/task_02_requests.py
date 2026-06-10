#!/usr/bin/python3
"""Consume JSONPlaceholder API and process posts"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save to CSV file"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        rows = []
        for post in data:
            rows.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)
