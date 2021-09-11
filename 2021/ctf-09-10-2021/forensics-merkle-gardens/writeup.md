# Merkle Gardens
* **Event:** monopolyCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** 700 (Hard)
* **(Optional) Tools Required / Used:**

### Solution
In order to find the tampered file, you need to verify the hashes. To do this, you get a SHA256 hash of the file and concatenate it with the given leaf hash, then hash that concatenation. Then concatenate *that* hash with the sibling's hash and hash *those*. You repeat this until you get a hash for the root of the tree, at which point you could verify it against the Merkle Tree's root. If they match, then that file is untampered. However, if they don't match, then you know that this file has been altered. Applying this verification process iteratively to all the given files until you find the tampered one. 
