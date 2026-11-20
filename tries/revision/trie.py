class Node:
    def __init__(self):
        self.children ={}
        self.isWord = False
class Prefix:
    def __init__(self):
        self.root = Node()
    def insertWord(self,word:str):
        dummy=self.root
        for char in word:
            if char not in dummy.children:
                dummy.children[char] = Node()
            dummy=dummy.children[char]
        dummy.isWord = True
    def searchWord(self,word:str):
        dummy=self.root
        for char in word:
            if char not in dummy.children:
                return False
            dummy=dummy.children[char]
        return dummy.isWord
    def startWithPrefix(self,word):
        dummy=self.root
        for char in word:
            if char not in dummy.children:
                return False
            dummy=dummy.children[char]
        return True
    def collectWords(self, node: Node, path: str, result: list[str]) -> None:
    # adds every word at or below this node to result, using path as the letters walked so far
        if node.isWord:
            result.append(path)
        if not node.children:
            return
        for key in node.children.keys():
            self.collectWords(node.children[key],path+key,result)
            
    def autocomplete(self, prefix: str) -> list[str]:
        # returns every word in the trie that starts with prefix, or [] if none do
        dummy=self.root
        final=[]
        for char in prefix:
            if char in dummy.children:
                dummy=dummy.children[char]
            else: return final
        self.collectWords(dummy,prefix,final)
        return final
    def countWords(self,node,prefix):
        count=0
        if node.isWord:
            count+=1
        for child in node.children:
            count+=self.countWords(node.children[child],prefix)
        return count
    def countPrefix(self,prefix:str):
        dummy=self.root
        for char in prefix:
            if char in dummy.children:
                dummy=dummy.children[char]
            else: return 0
        return self.countWords(dummy,prefix)
    def deleteWord(self, word: str) -> None:
        def removeFrom(node: Node, i: int) -> None:
            # your recursion goes here
            if i==len(word):
                node.isWord=False
                return
            letter=word[i]
            if letter not in node.children:
                return 
            child=node.children[letter]
            
            removeFrom(child,i+1)
            
            if not child.isWord and not child.children:
                del node.children[letter]
        removeFrom(self.root, 0)   # start at the root, at letter 0
trial = Prefix()
trial.insertWord("cat")
print(trial.searchWord("cat"))
print(trial.searchWord("chat"))

trial = Prefix()
for w in ["car", "cart", "cat","care", "dog","art"]:
    trial.insertWord(w)

out = []
trial.collectWords(trial.root, "", out)
print(out)  # expect ['car', 'cart', 'cat', 'dog']

out = []
trial.collectWords(trial.root.children['c'].children['a'], "ca", out)
print(out)  # expect ['car', 'cart', 'cat']

out = []
trial.collectWords(trial.root.children['c'], "c", out)
print(out)  # expect ['car', 'cart', 'cat']

print("-------------------")
print(trial.autocomplete("ca"))   # expect ['car', 'cart', 'cat']
print(trial.autocomplete("car"))  # expect ['car', 'cart']
print(trial.autocomplete("d"))    # expect ['dog']
print(trial.autocomplete("x"))    # expect []
print(trial.autocomplete("cx"))    # expect []

trial.deleteWord("cart")
print(trial.autocomplete(""))     # expect ['car', 'cart', 'cat', 'dog', 'art'] (or in that order: ['car', 'cart', 'cat', 'dog', 'art'])
print(trial.countPrefix("ca"))


t2 = Prefix()
t2.insertWord("car")
t2.insertWord("cart")
t2.deleteWord("car")
print(t2.searchWord("car"))        # expect False
print(t2.searchWord("cart"))       # expect True
t2.deleteWord("cart")
print(t2.searchWord("cart"))       # expect False
print(t2.startWithPrefix("c"))     # expect False (all nodes cleaned up)
t2.deleteWord("dog")               # expect no crash