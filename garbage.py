import wikipedia
url='rohti sharma'
a=wikipedia.search(url)
print(wikipedia.summary(a[0],sentences=2))
