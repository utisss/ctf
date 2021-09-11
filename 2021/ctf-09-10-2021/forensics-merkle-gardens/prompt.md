# Merkle Gardens

I was so excited for monopolyCTF that I made this folder FILLED with potential flags! But I think someone tampered with my files!! Luckily, I have a Merkle Tree for my filesystem. Can you find the flag that's been tampered with?

For every file _a_ that I had, I made a query to the Merkle Tree and saved that resulting data in a file _a.meta_.

This specific Merkle Tree works by taking the hash of a file as the leaf, and every parent node is created by hashing the concatenation of its children's hashes (all hashes use the SHA256 algorithm). When querying the Merkle Tree, it returns the necessary hashes to verify the file integrity in the form of nested tuples. Each tuple represents a tree (or a subtree) where the first element is the root, the second element is the left child, and the third element is the right child. Any time you see a "_", that means it's a hash that you should be able to compute yourself. 

_by Aya The Awesome_
