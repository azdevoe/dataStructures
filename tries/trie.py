class TrieNode:
    def __init__(self) -> None:
        # Each node has two things:
        #   self.children: dict[str, TrieNode]  -> letter in, next node out (starts empty)
        #   self.is_word: bool                  -> True if a word ends here (starts False)
        self.children = {}
        self.is_word = False


class WordTrie:
    def __init__(self) -> None:
        # The dummy head node. It has no letter of its own.
        self.root: TrieNode = TrieNode()
    def insertWord(self, word: str) -> None:
        # Walk the word one letter at a time, starting at the root.
        # If the letter is not in this node's children, make a new node for it.
        # Walk into that node. After the last letter, mark that node as a word end.
        dummy=self.root
        for stri in word:
            if stri in dummy.children:
                dummy=dummy.children[stri]
            else:
                dummy.children[stri]=TrieNode()
                dummy=dummy.children[stri]
        dummy.is_word=True
    def searchWord(self,word):
        dummy=self.root
        for stri in word:
            if stri not in dummy.children:
                return False
            dummy=dummy.children[stri]
        return dummy.is_word
    def startWithPrefix(self,word):
        dummy= self.root
        for chr in word:
            if chr not in dummy.children:
                return False
            dummy=dummy.children[chr]
        return True
    def collectWords(self, node: TrieNode, path: str, result: list[str]) -> None:
        if node.is_word:
            result.append(path)
        for child in node.children.keys():
            self.collectWords(node.children[child],path+child,result)
    def autoComplete(self,prefix):
        final=[]
        dummy=self.root
        for chr in prefix:
            if chr in dummy.children:
                dummy=dummy.children[chr]
            else:
                return final
        self.collectWords(dummy,prefix,final)
        return final
    
    def countWordsUnder(self, node: TrieNode) -> int:
        # counts how many words exist at this node and everywhere below it
        count=0
        if node.is_word:
            count+=1
        for char in node.children:
            count+=self.countWordsUnder(node.children[char])
        return count
    def countWithPrefix(self, prefix: str) -> int:
        # walks to the prefix node, returns how many words start with prefix (0 if prefix is missing)
        dummy=self.root
        count=0
        for char in prefix:
            if char in dummy.children:
                dummy=dummy.children[char]
            else:
                return count
        return self.countWordsUnder(dummy)
    def deleteWord(self,word:str):
        dummy = self.root
        def findWord(node:TrieNode,i):
            if i == len(word):
                node.is_word=False
                return 
            letter = word[i]
            if letter not in node.children:
                return
            child=node.children[letter]
            findWord(child,i+1)
            if not child.is_word and not child.children:
                del node.children[letter]
        findWord(dummy,0)
        
if __name__ == "__main__":
    trie = WordTrie()
    # ...your test prints here
trie=WordTrie()
rr=["cat","car","cart","care","dog"]
for word in rr:
    trie.insertWord(word)
out=[]
trie.collectWords(trie.root,"",out)
print(out)

print(trie.autoComplete(""))

print(trie.countWithPrefix("ca"))

print(trie.countWithPrefix("ca"))    # expect 4
print(trie.countWithPrefix("car"))   # expect 3
print(trie.countWithPrefix("d"))     # expect 1
print(trie.countWithPrefix("cart"))  # expect 1
print(trie.countWithPrefix("carts")) # expect 0
print(trie.countWithPrefix("x"))     # expect 0
print(trie.countWithPrefix(""))      # expect 5

print(trie.autoComplete(""))
trie.deleteWord("cart")
print(trie.autoComplete(""))
