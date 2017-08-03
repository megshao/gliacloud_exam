
urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png"
]

file_names = {}

for url in urls:
    result = url.split('/')
    file_name = result[len(result) - 1]
    if file_names.get(file_name) is None:
        file_names[file_name] = 1
    else:
        file_names[file_name] = file_names[file_name] + 1

sorted_file_names = sorted(file_names.items(), key=lambda x: x[1], reverse=True)

for file_name in sorted_file_names[:3]:
    print(file_name[0], file_name[1])
