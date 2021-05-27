class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.is_end = False
        # counter to indicate how often a word is inserted into the tree
        # useful to rank words based on popularity (in the autocomplete example)
        self.counter = 0
        # {
        #   'a': <TrieNode>
        # }
        self.children = {}

    def __repr__(self) -> str:
        return f'<TrieNode: {self.char}>'


class Trie(object):
    def __init__(self):
        # a tries root is always empty
        self.root = TrieNode('')

    def insert(self, word):
        node = self.root

        # loop through each character in the word
        # if there's no child with the current charachter, we create a child
        # node for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # if we haven't seen the character before, create a new node
                # in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # once we've added all characters, mark the final node as end node
        node.is_end = True
        # increment the counter on the final node, so we know how often
        # we've seen it
        node.counter += 1

    def dfs(self, node, prefix):
        if node.is_end:
            return self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, prefix):
        """
        Given a prefix, retrieve all words stored in the trie that have that
        prefix, sorted by the number of times that word has been inserted.
        """
        # we re-initialize an `output` variable on the instance, as there can
        # be multiple outputs for the same prefix
        self.output = []
        node = self.root

        # first, we'll see if the prefix is in the trie
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                # return the empty output list if the prefix is not in the trie
                return self.output
        print(node, prefix, prefix[:-1])
        self.dfs(node, prefix[:-1])

        return sorted(self.output, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    t = Trie()
    t.insert('was')
    t.insert('where')
    t.insert('what')
    t.insert('war')
    t.insert('word')
    t.insert('what')
    assert(t.query('wh') == [('what', 2), ('where', 1)])
    assert(t.query('42') == [])
