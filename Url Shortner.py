from flask import Flask, redirect, render_template, request
import string
import random


# A simple model for the shortened URL.
class ShortUrl:
    def __init__(self, long_url, short_code=None):
        self.long_url = long_url
        self.short_code = short_code if short_code else self.generate_short_code()

    def generate_short_code(self):
        # Generate a random string of 6 alphanumeric characters.
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


# The main URL shortener class.
class UrlShortener:
    def __init__(self):
        self.short_urls = {}

    def shorten(self, long_url):
        if long_url in self.short_urls:
            return self.short_urls[long_url].short_code
        else:
            short_url = ShortUrl(long_url)
            self.short_urls[long_url] = short_url
            return short_url.short_code

    def get_long_url(self, short_code):
        for short_url in self.short_urls.values():
            if short_url.short_code == short_code:
                return short_url.long_url
        return None


# Usage
url_shortener = UrlShortener()
short_code = url_shortener.shorten('https://www.example.com/this/is/a/very/long/url')
print(f'Shortened URL: {short_code}')
long_url = url_shortener.get_long_url(short_code)
print(f'Original URL: {long_url}')