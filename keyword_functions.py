import string
import re
import keywords

#new version, now correctly includes multi-word keywords
def create_keywords_table(job_desc):
    #remove punctuation from str using string translate method
    job_desc = job_desc.translate(str.maketrans("", "", string.punctuation))
    keywords_dict = {}
    #loop over keywords, count all occurences of each one in job_desc string
    for keyword in keywords.keywords:
        #this reg expression counts all instances of keyword in the job_desc string,
        #without counting occurences where keyword is substring of a different word
        occurences = len(re.findall(rf"\b{keyword}\b", job_desc))
        if occurences > 0:
            keywords_dict.update({keyword : occurences})
        
    #sort keywords_dict in ascending order: sorted(iterable, key, reverse)
    #this returns list of tuples of dict items, sorted in ascending order by the value
    keywords_dict = sorted(keywords_dict.items(), key=lambda x: x[1], reverse=True)
    #make it a dict again
    keywords_dict = dict(keywords_dict)


    #print keywords in table format
    # print("Keyword          Frequency\n")
    # for word in keywords_dict:
    #     print(f"{word}          {keywords_dict[word]}")

    return keywords_dict
        
#utility to check if a word is in keywords list
def check_for_word(keyword):
    if keyword in keywords.keywords:
        print("yes")
    else:
        print("no")

#check_for_word("Object oriented")
