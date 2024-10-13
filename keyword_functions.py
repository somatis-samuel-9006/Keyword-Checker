import string
import re
import keywords

#new version, now correctly includes multi-word keywords
def create_keywords_table(job_desc):
    #remove punctuation from str using string translate method
    job_desc = job_desc.translate(str.maketrans("", "", string.punctuation))

    #read in keywords list
    with open("Keywords.txt", "r+") as f:
        file_words = f.readlines()

    for i in range(len(file_words)):
        file_words[i] = file_words[i].strip('\n')

    keywords_dict = {}
    #loop over keywords, count all occurences of each one in job_desc string
    for keyword in file_words:
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

def add_word(word):
    #dont add word that is already in the file
    if not check_for_word(word):
        with open("Keywords.txt", "a+") as f:
            f.write(f"{word}\n")
            return True
    else:
        return False

#remove word from keywords file by reading in the data, removing a value if present, then writing the new data back to file
def remove_word(word_to_delete):
    with open("Keywords.txt", "r+") as f:
        file_words = f.readlines()

    for i in range(len(file_words)):
        file_words[i] = file_words[i].strip('\n')

    if word_to_delete in file_words:
        file_words.remove(word_to_delete)

        #re-write to file the new list
        with open("Keywords.txt", "w+") as f:
            for word in file_words:
                f.write(f"{word}\n")

        return True
    else:
        return False

        
#utility to check if a word is in keywords list
def check_for_word(keyword):
     #read in keywords list
    with open("Keywords.txt", "r+") as f:
        file_words = f.readlines()

    for i in range(len(file_words)):
        file_words[i] = file_words[i].strip('\n')

    if keyword in file_words:
        return True
    else:
        return False


# with open("Keywords.txt", "w+") as f:
#     for word in keywords.keywords:
#         f.write(f"{word}\n")

#check_for_word("Object oriented")
#add_word("jo")
#add_word("bob")
# remove_word("jo")
# remove_word("bob")
#remove_word("Qt")

#create_keywords_table("java java mavdsaddsavdsa")

