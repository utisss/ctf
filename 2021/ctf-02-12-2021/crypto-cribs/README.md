# Cribs
* **Event:** Stonks CTF
* **Problem Type:** Cryptography
* **Difficulty:** Medium
* **(Optional) Tools Required / Used:** [toolbox.lotusfa.com/crib_drag](https://toolbox.lotusfa.com/crib_drag/)

## Background
One-Time Pads must use a unique secret key for every message. Otherwise, an attack known as crib dragging can be carried out. Crib dragging is a known plaintext attack.

One-Time Pads work via XOR. For a message, `m`, such that `m_i` refers to the byte at the ith position in `m`, a key, `k`, such that `k_i` refers to the byte at the ith position in `k`, and a ciphertext `c` such that `c_i` refers to the byte at the ith position in `c`, `c_i = k_i ^ m_i`, where `^` is the XOR operation.

```
c_1_i ^ c_2_i = k_i ^ m_1_i ^ k_i ^ m_2_i = m_1_i ^ m_2_i

c_1_i ^ c_2_i ^ m_1_i = m_2_i
c_1_i ^ c_2_i ^ m_2_i = m_1_i
```

This means that XORing the two ciphertexts together and XORing a message with that will return the other message. If one can make guesses about a message and a recognizable plaintext is the result of XORing the guess and the two ciphertexts, then it is likely the guess was correct.

## Solution
The tool [toolbox.lotusfa.com/crib_drag](https://toolbox.lotusfa.com/crib_drag/) is useful for performing a crib dragging attack. Paste the hexadecimal encoding of the messages into the two ciphertext boxes. Then guess a word, like `utflag`, and observe that more of the flag appears in the other ciphertext (`tflag{`). Continue making guesses until the plaintext message is revealed.
