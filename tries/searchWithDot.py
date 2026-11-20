from trie import WordTrie,TrieNode
def searchWithDot(words: list[str], pattern: str) -> bool:
    # Returns True if any word in words matches the pattern.
    # A "." in the pattern matches any single letter.
    # Every other letter must match exactly, and the length must match too.
    node=WordTrie()
    for word in words:
        node.insertWord(word)
    dummy=node.root
    def helper(dummy:TrieNode,i):
        if i == len(pattern) and dummy.is_word:
            return True
        letter=pattern[i]
        if letter==".":
            for key in dummy.children:
                helper(i+1,dummy.children[key])
        else:
            

print(searchWithDot(["cat", "cut", "dog"], "cat"))   # expect True
print(searchWithDot(["cat", "cut", "dog"], "c.t"))   # expect True
print(searchWithDot(["cat", "cut", "dog"], "d.."))   # expect True
print(searchWithDot(["cat", "cut", "dog"], "c."))    # expect False
print(searchWithDot(["cat", "cut", "dog"], "..."))   # expect True
print(searchWithDot(["cat", "cut", "dog"], "x.."))   # expect False