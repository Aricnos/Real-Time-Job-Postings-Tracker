import csv 
import os

# define a function to cteate the dir and store the data
def save_to_csv(jobs, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    fieldnames = ['title', 'company', 'location', 'tag', 'date_posted']


    # make the writer function to save the filename
    with open(filename, 'w', newline='',encoding='utf8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs)