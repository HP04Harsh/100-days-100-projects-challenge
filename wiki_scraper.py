import wikipedia

topic = input("Enter topic: ")

try:
    print("\nTitle:", wikipedia.page(topic).title)
    print("\nSummary:", wikipedia.summary(topic, sentences=2))
    print("\nURL:", wikipedia.page(topic).url)
except:
    print("Error: Topic not found or ambiguous")