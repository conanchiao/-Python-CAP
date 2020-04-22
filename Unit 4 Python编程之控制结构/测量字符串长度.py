# measue some strings
words=["cat","window","defensestrate"]
for w in words:
    print(w,len(w))

for w in words[:]:    # Loop over a slice copy of the enter list.
    if len(w)>6:
        words.insert(0, w)
        
