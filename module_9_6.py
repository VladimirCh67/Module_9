def all_variants(text):
    j = 0
    while j < len(text):
        j += 1
        for i in range(len(text)):
            x = i + j
            if x  <= len(text):
                yield text[i:x]



a = all_variants("abcd")
for i in a:
    print(i)