from pyquery import PyQuery as pq
import requests
import re
import Pattern
import SpiderIO

def generate_article_url_from_ielts_xiezuo_page(url):
    response_string = get_response_string(url)
    document = pq(response_string)
    urls = document(".those_content").items(".pull-right p a")
    article_urls = [i.attr('href') for i in urls]
    return article_urls

def generate_next_xiezuo_url_from_ielts_xiezuo_page(url):
    response_string = get_response_string(url)
    document = pq(response_string)
    a_element = document(".pagination .next a")
    next_xiezuo_page_url = a_element.attr('href')
    return next_xiezuo_page_url

def generate_xiezuo_page_url(url):
    response_string = get_response_string(url)
    document = pq(response_string)
    urls = document(".those_content").items(".pull-right p a")

def get_response_string(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

if __name__ == '__main__':
    url = "http://ielts.zhan.com/xiezuo/"
    # urls = generate_article_url_from_ielts_xiezuo_page(url)
    next_url = generate_next_xiezuo_url_from_ielts_xiezuo_page(url)
    print(next_url)