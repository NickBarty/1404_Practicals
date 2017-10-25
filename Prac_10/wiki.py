import wikipedia

page_name = input("Enter a page to search for: ")
wikipedia.summary(page_name, "html.parser")
# try:
#     page = wikipedia.page(page_name)
#     print(page.title)
#     print(page.url)
# except wikipedia.exceptions.DisambiguationError as e:
#     print(e.options)
#
# try:
#     summary = wikipedia.summary(page_name, r)
#     print(summary)
# except wikipedia.exceptions.DisambiguationError as e:
#     print(e.options)
# url = page.url()
#
# print(title)
# print(url)
