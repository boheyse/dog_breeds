#http://google.com/search?client=safari&rls=en&q=rhodesian+ridgeback&ie=UTF-8&oe=UTF-8

##JavaScript script used with jquery in Google Chrome to put all image links into
#one .txt file so the python code can iterate through and download the photo
#
#// pull down jquery into the JavaScript console
#var script = document.createElement('script');
#script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";
#document.getElementsByTagName('head')[0].appendChild(script);
#
#var urls = $('.rg_di .rg_meta').map(function() { return JSON.parse($(this).text()).ou; });
#
#// write the URls to file (one per line)
#var textToSave = urls.toArray().join('\n');
#var hiddenElement = document.createElement('a');
#hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
#hiddenElement.target = '_blank';
#hiddenElement.download = 'urls.txt';
#hiddenElement.click();


import urllib.request
import os

breed = "black_lab"
t_set = "training_set/"

file_path = "dataset/" + t_set + breed

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Folder --" + directory)
        os.makedirs(directory)

def create_url_files(path, base_url):
    queue = file_path + "/queue.txt"
    crawled = file_path + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

def write_file(file_path, data):
    f = open(file_path, 'w')
    f.write(data)
    f.close()

#appends to a file
def append_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data + '\n')

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#this takes a set of downloaded links to a set and appends it to a file.
def set_to_file(links):
    for link in links:
        append_file(file_path, link)


#images = open("urls.txt").read().split("\n")

# =============================================================================
# name = 0
#
# def img_download(url, file_path):
#     full_name = file_path + str(name) + ".jpg"
#     urllib.request.urlretrieve(url, full_name)
#
#
# for url in images:
#
#     try:
#         print(url)
#         image = img_download(url, "dataset/" + breed)
#         print("Image download complete")
#         name = name + 1
#
#     except:
#         print("Unable to download image")
# =============================================================================
