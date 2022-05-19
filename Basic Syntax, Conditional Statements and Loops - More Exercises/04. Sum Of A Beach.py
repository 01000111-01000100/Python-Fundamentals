string = input().lower()

list1 = ["sand", "water", "fish", "sun"]
count = 0
for words in list1:
    if words in string:
        words_count = string.count(words)
        count += words_count

print(count)