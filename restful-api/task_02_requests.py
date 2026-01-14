#!/usr/bin/python3
"""Module for consuming and processing data from an API using Python."""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print their titles.
    
    Prints the status code and all post titles if successful.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save to CSV file.
    
    Saves posts with id, title, and body columns to posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        structured_data = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]
        
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(structured_data)
