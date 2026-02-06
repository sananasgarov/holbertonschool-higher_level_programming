#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Sadece id, title ve body alanlarını alalım
        data_to_save = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]

        fieldnames = ['id', 'title', 'body']

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)

        print("\nVeriler başarıyla 'posts.csv' dosyasına kaydedildi.")
