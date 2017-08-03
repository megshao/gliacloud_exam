from part_2_PTT import PTTParser

parser = PTTParser(forum='baseball')
parser.get_posts()
print(parser.posts)
parser.get_posts_next_page()
print(parser.posts)
