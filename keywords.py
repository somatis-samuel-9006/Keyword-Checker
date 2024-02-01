import string

job_desc = """
Java Java java Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam congue pulvinar dolor sed dapibus. 
In efficitur a mauris placerat ultricies. Ut non quam id nibh scelerisque bibendum sit amet sit amet arcu. 
Nulla ac bibendum orci. Vivamus varius turpis ut nibh porta, nec iaculis nulla egestas. 
Mauris ultricies quam eu nulla lobortis sagittis. Pellentesque fringilla eleifend risus, eu aliquet erat ullamcorper at. 
Aliquam faucibus, massa nec commodo elementum, nulla risus ultricies est, at hendrerit leo mi at odio. 
Donec fermentum nisi quam, et volutpat tellus eleifend in. Mauris id luctus nulla, iaculis molestie libero. 
Donec ut massa eleifend est finibus vestibulum in a nisi.
Vestibulum volutpat imperdiet pulvinar. Aenean semper mi dui, eget consequat mi finibus quis. 
In venenatis a odio vitae interdum. Donec justo nibh, lacinia in imperdiet ac, mollis eu quam. 
Aenean eu turpis et turpis dignissim venenatis vitae sit amet erat. Curabitur malesuada vulputate eros, ut porta lectus rhoncus quis.
Nunc ullamcorper orci ac odio facilisis blandit. Morbi sed scelerisque leo. Vestibulum vitae odio nibh.
Pellentesque pulvinar sodales consequat. Vestibulum id neque accumsan, bibendum tortor vel, fermentum felis. 
Phasellus accumsan tincidunt dui, vel feugiat nunc. Phasellus viverra sagittis sem, in lacinia nisi ultrices non. 
Proin et luctus sapien. Suspendisse Software ornare faucibus diam, sit amet porta mi convallis quis. Nam lobortis massa et porta mattis. 
Maecenas iaculis, arcu semper commodo scelerisque, felis metus aliquam erat, facilisis porttitor risus lacus ac quam.
Maecenas ut quam accumsan, facilisis nisi eget, aliquam elit. Maecenas viverra feugiat justo, sit amet mollis eros blandit a. 
Sed ac rhoncus tellus. Donec eget neque dignissim lorem commodo maximus. software Aenean tincidunt felis non nisl porta accumsan. 
Aenean fermentum vehicula libero. Phasellus in elementum purus, ut molestie dolor. Nulla quis euismod nisl. 
Phasellus sed faucibus sem. Morbi scelerisque lectus in dui dictum ullamcorper. 
Praesent malesuada scelerisque ipsum, et ullamcorper neque. Front Aenean euismod laoreet elit non dictum. 
Duis ut tortor vel lorem ultricies vestibulum id nec turpis. Sed non lectus sit amet orci elementum mollis. 
Pellentesque vitae elit a odio congue euismod shaders shaders shaders shaders maven maven maven software UX/UI algorithm.
Waterfall Algorithms Javascript javascript debugging Front End front end engineering Engineering testing Testing CS.
Computer Science Software Test. 
"""

keywords = ['C++', 'c++', 'Git', 'git', 'HTML', 'Html', 'html', 'Java', 'java', 'Agile', 'agile', 'Maven', 'maven', 
             'Coding', 'Python', 'python', 'Testing', 'testing', 'Teamwork', 'teamwork', 'Algorithm', 'algorithm', 
             'Algorithms', 'algorithms', 'Debugging', 'debugging', 'Front End', 'front end', 'Waterfall', 'waterfall',
             'JavaScript', 'Javascript', 'javascript', 'Code Review', 'code review', 'Engineering', 'engineering', 
             'Programming', 'programming', 'Software Test', 'software test', 'Testing', 'testing', 'Data Structures,', 
             'data structures,', 'Computer Science', 'computer science', 'CS', 'Development Tool', 'development tool', 
             'Software Solution', 'software solution', 'Software Development', 
             'software development', 'Software Engineering', 'software', 'engineering', 'Language', 'language', 
             'Methodology', 'methodology', 'Solving', 'solving', 'Communication', 'communication', 'Participating', 
             'participating', 'Data', 'data', 'Team', 'team', 'Client', 'client', 'Design', 'design', 'Analyst', 
             'analyst', 'Develop', 'develop', 'Software', 'software', 'Technology', 'technology', 'Implementation', 
             'implementation', 'SQL', 'MySQL', 'Agile', 'C', 'AWS', 'Linux', 'Git', 'Github', 'git', 
             'github', 'UXUI', 'UI', 'UX', 'ui', 'ux', 'Flask', 'flask', 'Database', 'database', 'Innovation', 'innovation', 
             'Documentation', 'documentation', 'HTML', 'CSS', 'HTML/CSS', 'Technical', 'technical', 'GLSL', 'Teams', 
             'Slack', 'Software Testing', 'software testing', 'Pytest', 'Bash', 'OpenMP', 'OpenCL', 'CUDA', 'OpenGL', 
             'Vulkan', 'shaders', 'Shaders', 'Produced', 'produced', 'Restructured', 'restructured', 'communicate', 'Communicate']

#takes in a multi-line string and builds a dict of all the keywords found in the job description string
def create_keywords_table(job_desc):
    #remove punctuation from str using string translate method
    job_desc = job_desc.translate(str.maketrans("", "", string.punctuation))

    #build dict of all words in job desc and how many times they occur
    job_desc_words = {}
    for word in job_desc.split():
        if word in job_desc_words:
            job_desc_words[word] += 1
        else:
            #add word to dict if not yet in dict
            job_desc_words.update({word : 1})
            
    #build dict of what keywords exist in job description and how often they're used
    keywords_dict = {}
    for keyword in keywords:
        if keyword in job_desc_words:
            keywords_dict.update({keyword : job_desc_words[keyword]})

    #sort keywords_dict in ascending order
    #sorted(iterable, key, reverse)
    #this returns list of tuples of dict items, sorted in ascending order by the value
    keywords_dict = sorted(keywords_dict.items(), key=lambda x: x[1], reverse=True)
    #make it a dict again
    keywords_dict = dict(keywords_dict)
    #print keywords in table format
    print("Keyword          Frequency\n")
    for word in keywords_dict:
        print(f"{word}          {keywords_dict[word]}")

    return keywords_dict


#create_keywords_table(job_desc)
        
#utility to check if a word is in keywords list
def check_for_word(keyword):
    if keyword in keywords:
        print("yes")
    else:
        print("no")

#check_for_word("Communicate")


