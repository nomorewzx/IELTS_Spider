from pyquery import PyQuery as pq
import requests
import re
import Pattern
import SpiderIO
import UrlUtils

VISITED_URL = []

def main():
    VISITED_URL = get_visited_url_from_file()
    to_visit_xiezuo_page_url = SpiderIO.get_to_visit_xiezuo_page_url()
    print(to_visit_xiezuo_page_url)
    for count in range(1, 100):
        to_visit_article_urls = UrlUtils.generate_article_url_from_ielts_xiezuo_page(to_visit_xiezuo_page_url)
        new_xiezuo_page_url = UrlUtils.generate_next_xiezuo_url_from_ielts_xiezuo_page(to_visit_xiezuo_page_url)

        if new_xiezuo_page_url is None or new_xiezuo_page_url == '':
            SpiderIO.write_next_xiezuo_page_url_into_file(to_visit_xiezuo_page_url)
            print(to_visit_xiezuo_page_url, " is the last visited page url")
            return

        to_visit_xiezuo_page_url = new_xiezuo_page_url

        for url in to_visit_article_urls:
            if url in VISITED_URL:
                print(url, " has been visited")
            else:
                update_visited_url(url)
                fetch_content_and_write_into_files_according_to_keywords(url)

        print("%dth page" % count)
        count += 1
    SpiderIO.write_next_xiezuo_page_url_into_file(to_visit_xiezuo_page_url)

def get_visited_url_from_file():
    VISITED_URL = SpiderIO.get_visited_urls()
    return VISITED_URL

def update_visited_url(url):
    SpiderIO.write_url_into_visited_urls(url)
    VISITED_URL.append(url)

def test_single_article():
    url = "http://ielts.zhan.com/xiezuo54860.html"
    fetch_content_and_write_into_files_according_to_keywords(url)

def fetch_content_and_write_into_files_according_to_keywords(url):
    paragraph_list = fetch_page_article_area_as_list_of_string(url)
    index_key_words = Pattern.if_keyword_sample_article_exists(paragraph_list)
    if index_key_words != -1:
        topic_list_raw = paragraph_list[:index_key_words]
        esssay_list_raw = paragraph_list[index_key_words + 1:]
        topic_list = Pattern.remove_chinese_words_in_elements(topic_list_raw)
        essay_list = Pattern.remove_chinese_words_in_elements(esssay_list_raw)
        if (topic_list and essay_list):
            print("Valid article found:", url)
            SpiderIO.write_topic_into_file(Pattern.remove_keyword_in_topic_paragraph(''.join(topic_list)))
            SpiderIO.write_essay_into_file(Pattern.remove_words_count_part(''.join(essay_list)))
            SpiderIO.write_valid_article_url_into_file(url)


def fetch_page_article_area_as_list_of_string(url):
    response_string = get_response_string(url)
    document = pq(response_string)
    pdivs = document(".article-content").items("p")
    plist = [i.text() for i in pdivs]
    return plist

def fetch_content_and_write_into_files(url):
    response_string = get_response_string(url)
    document = pq(response_string)
    pdivs = document(".article-content").items("p")
    plist = [i.text() for i in pdivs]

    new_list = Pattern.remove_element_contanins_chinese_words(plist)

def get_response_string(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

if __name__ == '__main__':
    main()
    # test_single_article()