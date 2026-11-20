from trie import WordTrie,TrieNode
def sharedStem(words: list[str]) -> str:
    # Returns the longest prefix shared by ALL the words.
    # Build a WordTrie from the words, then walk down from the root
    # while the node has exactly one child and is not a word end.
    node=WordTrie()
    for word in words:
        node.insertWord(word)
    initial=[]
    ll=""
    i=0
    dummy=node.root
    while len(dummy.children)==1 and not dummy.is_word:
        kk=words[0][i]
        initial.append(kk)
        dummy=dummy.children[kk]
        i+=1
    return ll.join(initial)
            
ii=WordTrie()

print(sharedStem(["flower", "flow", "flight"]))  # expect "fl"
print(sharedStem(["dog", "racecar", "car"]))     # expect ""
print(sharedStem(["car", "cart", "care"]))       # expect "car"
print(sharedStem(["apple"]))                     # expect "apple"
print(sharedStem([]))                            # expect ""