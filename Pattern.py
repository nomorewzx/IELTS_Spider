import re

pattern_keyword_list = ["Sample answer",u"剑桥雅思参考范文", u"参考范文", u"示例范文", u"9分范文", u"考官范文", u"正文部分"]

def if_keyword_sample_article_exists(list_of_paragraph):
    # Start from second last element, because we do not expect the keywords in the last paragraph.
    for i in range(len(list_of_paragraph)-2, -1, -1):
        for key_word in pattern_keyword_list:
            if list_of_paragraph[i].find(key_word) != -1:
                return i
    return -1

def remove_words_count_part(string):
    pattern = re.compile(r"\d+words")
    m = re.search(pattern, string)
    if m is not None:
        processed_string = string.replace(m.group(0), '')
        return processed_string
    return string

def remove_keyword_in_topic_paragraph(string):
    pattern = re.compile(r"^Task.\s{0,}")
    m = re.search(pattern, string)
    if m is not None:
        processed_string = string.replace(m.group(0), '')
        return processed_string
    return string.strip()

def remove_element_contanins_chinese_words(list):
    # list_no_chinese_words = filter(no_chinese_words, list)
    # return list_no_chinese_words
    new_list = [element for element in list if no_chinese_words(element)]
    if ''.join(new_list) != '':
        return new_list
    else:
        return None


def remove_chinese_words_in_string(string):
    chinese_words_pattern = re.compile(u"[\u4e00-\u9fa5]+|[\uff00-\uffef]|[\u3002]|[\d+]")
    string_without_chinese_words = re.sub(chinese_words_pattern, '', string)
    return string_without_chinese_words

def remove_chinese_words_in_elements(list):
    new_list = []
    for element in list:
        if no_chinese_words(element):
            new_list.append(element)
        else:
            new_element = remove_chinese_words_in_string(element)
            new_list.append(new_element)
    # If the list is empty after removing chinese and other chars in elements, return None.
    if ''.join(new_list).strip() == '':
        return None
    return new_list

def no_chinese_words(string):
    for char in string:
        if is_chinese(char):
            return False
    return True

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

if __name__ == '__main__':
    # list = ['Task: this is a test case', 'To what extent do you aggree or disagree',u'参考范文' 'Hello, this is article']
    # exists = if_keyword_sample_article_exists(list)
    # print(exists)
    # task = "Task： Some people want government to spend money on life on other planets, however, others think it is a waste of public money when the earth has so many problems.Discuss these two views and give your own opinion."
    # processed = remove_keyword_in_topic_paragraph(task)
    # print(processed)
    chinese_words = u"Discuss both these view and give your own opinion.生活是一成不变好，还是保持变化好。"
    new = remove_chinese_words_in_string(chinese_words)
    print(new)