# You will be given a list of words, and you have to write an algorithm to group all the words which are anagrams of each other.

def group_anagrams(words):
    groups = {}
    for word in words:
        sort = "".join(sorted(word))
        if sort in groups:
            groups[sort].append(word)
        else:
            groups[sort] = [word]
    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["tea", "eat", "bat", "ate", "arc", "car"]))
