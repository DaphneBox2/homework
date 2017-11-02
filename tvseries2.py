# #!/usr/bin/env python
# # Name: Daphne Box
# # Student number: 10455701
# '''
# This script scrapes IMDB and outputs a CSV file with highest rated tv series.
# '''
# import csv

# from pattern.web import URL, DOM

# TARGET_URL = "http://www.imdb.com/search/title?num_votes=5000,&sort=user_rating,desc&start=1&title_type=tv_series"
# BACKUP_HTML = 'tvseries.html'
# OUTPUT_CSV = 'tvseries.csv'
# result = []
# # title = []
# # genres = []
# # number_only_runtime = []
# # rating = []
# # actors = []

# print("hoi")


# def extract_tvseries(dom):
#     '''
#     Extract a list of highest rated TV series from DOM (of IMDB page).

#     Each TV series entry should contain the following fields:
#     - TV Title
#     - Rating
#     - Genres (comma separated if more than one)
#     - Actors/actresses (comma separated if more than one)
#     - Runtime (only a number!)
#     '''

#     # ADD YOUR CODE HERE TO EXTRACT THE ABOVE INFORMATION ABOUT THE
#     # HIGHEST RATED TV-SERIES
#     # NOTE: FOR THIS EXERCISE YOU ARE ALLOWED (BUT NOT REQUIRED) TO IGNORE
#     # UNICODE CHARACTERS AND SIMPLY LEAVE THEM OUT OF THE OUTPUT.
    
#     print("5")
#     for e in dom.by_tag("div.lister-list"): # Top 5 reddit entries 
#         print("6")
#         for f in e.by_tag("div.lister-item-content"):
#             title = f.by_tag("a")[0].content.encode('utf-8')
#             print("7")
#             for g in f.by_tag("p.text-muted"):
#                 prepre_genres = f.by_tag("span.genre")[0].content.encode('utf-8')
#                 pre_genres = prepre_genres.split("\n")
#                 genres = pre_genres[1]
#                 print("8")
#                 runtime = f.by_tag("span.runtime")
#                 if runtime == []:
#                     runtime = ""
#                     print("9")
#                 else:   
#                     pre_runtime = f.by_tag("span.runtime")[0].content.encode('utf-8')
#                     number_only_runtime = pre_runtime.split(" ")
#                     runtime = number_only_runtime[0]
#                     print("9")
#                 rating = f.by_tag("strong")[0].content.encode('utf-8')
#                 print("10")
#             actors = f.by_tag("p")[2].by_tag("a")
#             actors = ", ".join([p.content for p in actors]).encode('utf-8')
#             print("11")
#             temp_res = []
#             temp_res.extend([title, genres, runtime, rating, actors])
#             result.append(temp_res)
#         print(result)
#         # temp_res = temp_res.extend([title, genres, runtime, rating, actors])
#         # print("21 {}".format(temp_res))
#         # result = result.append(temp_res)
#         # print("22 {}".format(result))
#         # return [result]             
#         return [result]  # replace this line as well as appropriate


# def save_csv(f, tvseries):
#     '''
#     Output a CSV file containing highest rated TV-series.
#     '''
#     print("10")
#     writer = csv.writer(f)
#     writer.writerow(['title', 'genres', 'runtime', 'rating', 'actors'])
#     for item in tvseries:
#         for sublist in item:
#             #substring = ''.join(str(i) for i in sublist)
#             writer.writerow(sublist)
#     print("11")

#     # ADD SOME CODE OF YOURSELF HERE TO WRITE THE TV-SERIES TO DISK

# if __name__ == '__main__':
#     print("2")
#     # Download the HTML file
#     url = URL(TARGET_URL)
#     html = url.download()
#     #dom = DOM(url.download(cached=True))

#     # Save a copy to disk in the current directory, this serves as an backup
#     # of the original HTML, will be used in grading.
#     print("3")
#     with open(BACKUP_HTML, 'wb') as f:
#         f.write(html)

#     # Parse the HTML file into a DOM representation
#     print("4")
#     dom = DOM(html)

#     # Extract the tv series (using the function you implemented)
#     print("7")
#     tvseries = extract_tvseries(dom)

#     # Write the CSV file to disk (including a header)
#     print("8")
#     with open(OUTPUT_CSV, 'wb') as output_file:
#         save_csv(output_file, tvseries)
#     print("9")    


#!/usr/bin/env python
# Name: Daphne Box
# Student number: 10455701
'''
This script scrapes IMDB and outputs a CSV file with highest rated tv series.
'''
import csv

from pattern.web import URL, DOM

TARGET_URL = "http://www.imdb.com/search/title?num_votes=5000,&sort=user_rating,desc&start=1&title_type=tv_series"
BACKUP_HTML = 'tvseries.html'
OUTPUT_CSV = 'tvseries.csv'
result = []


def extract_tvseries(dom):
    '''
    Extract a list of highest rated TV series from DOM (of IMDB page).

    Each TV series entry should contain the following fields:
    - TV Title
    - Rating
    - Genres (comma separated if more than one)
    - Actors/actresses (comma separated if more than one)
    - Runtime (only a number!)
    '''
    
    # Inspiration about how to scrap the IMDB website is obtained from: 
    #"http://mlwhiz.com/blog/2014/10/02/data_science_101_python_pattern/"

    # Go inside the html file and go to the header in which all the data from one movies is stored
    for f in dom.by_tag("div.lister-item-content"):
        title = f.by_tag("a")[0].content.encode('utf-8')
        
        # Go to header where runtime and genre are stored
        for g in f.by_tag("p.text-muted"):
            
            # Get genre without \n first
            prepre_genres = f.by_tag("span.genre")[0].content.encode('utf-8')
            pre_genres = prepre_genres.split("\n")
            genres = pre_genres[1]
            
            # Check if run time for serie if given, if so show minutes only else leave empty
            runtime = f.by_tag("span.runtime")
            if runtime == []:
                runtime = ""
            else:   
                pre_runtime = f.by_tag("span.runtime")[0].content.encode('utf-8')
                number_only_runtime = pre_runtime.split(" ")
                runtime = number_only_runtime[0]
            rating = f.by_tag("strong")[0].content.encode('utf-8')
        
        # Get first all actors and put them together separated with a comma
        actors = f.by_tag("p")[2].by_tag("a")
        actors = ", ".join([p.content for p in actors]).encode('utf-8')
        
        # Put all the data together
        temp_res = []
        temp_res.extend([title, genres, runtime, rating, actors])
        result.append(temp_res)
    
    # Return all the data
    return [result]


def save_csv(f, tvseries):
    '''
    Output a CSV file containing highest rated TV-series.
    '''
    writer = csv.writer(f)
    
    # Make headers for all colums
    writer.writerow(['title', 'genres', 'runtime', 'rating', 'actors'])
    
    # write all the data in sublists to the appropriate cell
    for item in tvseries:
        for sublist in item:
            writer.writerow(sublist)

    # ADD SOME CODE OF YOURSELF HERE TO WRITE THE TV-SERIES TO DISK

if __name__ == '__main__':
    
    # Download the HTML file
    url = URL(TARGET_URL)
    html = url.download()
    #dom = DOM(url.download(cached=True))

    # Save a copy to disk in the current directory, this serves as an backup
    # of the original HTML, will be used in grading.
    with open(BACKUP_HTML, 'wb') as f:
        f.write(html)

    # Parse the HTML file into a DOM representation
    dom = DOM(html)

    # Extract the tv series (using the function you implemented)
    tvseries = extract_tvseries(dom)

    # Write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'wb') as output_file:
        save_csv(output_file, tvseries)    
