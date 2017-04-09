def write_topic_into_file(param):
    with open("data/topic", 'a') as f:
        f.write(remove_new_line_char(param)+"\n")


def write_essay_into_file(param):
    with open("data/essay", 'a') as f:
        f.write(remove_new_line_char(param)+"\n")

def remove_new_line_char(string):
    return string.replace("\n", "").replace("\r","")

def get_seed_urls():
    with open("data/seed_urls", "r") as f:
        return [line.rstrip() for line in f]

def get_visited_urls():
    with open("data/visited_urls", "r") as f:
        return [line.rstrip() for line in f]

def get_to_visit_xiezuo_page_url():
    with open("data/to_visit_xiezuo_page_url", "r") as f:
        return [line.rstrip() for line in f][0]

def write_url_into_visited_urls(url):
    with open("data/visited_urls", "a") as f:
        f.write(remove_new_line_char(url)+"\n")

def write_valid_article_url_into_file(url):
    with open("data/valid_urls", "a") as f:
        f.write(remove_new_line_char(url)+"\n")

def write_next_xiezuo_page_url_into_file(url):
    with open("data/to_visit_xiezuo_page_url", "w") as f:
        f.write(remove_new_line_char(url))