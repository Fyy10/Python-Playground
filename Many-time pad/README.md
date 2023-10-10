# Many-time pad

[Homework Page](https://cseweb.ucsd.edu/classes/fa23/cse207B-a/hw1/)

## Encryption

First, let's look at the encryption procedure.

I modified the code given from the homework page to explore the relationship between message and cipher.

Given the following encryption code:

```python
import os

# MSGS = open("hw1-message.txt").readlines()
MSGS = open('input.txt').readlines()

def bytexor(a, b):
    # xor two byte arrays (trims the longer input)
    return bytes([x ^ y for (x, y) in zip (a, b)])

def random(size=16):
    return os.urandom(size)

def encrypt(key, msg):
    c = bytexor(key, msg)
    print(c.hex())
    return c

def main():
    key = random(1024)
    ciphertexts = [encrypt(key, msg.encode('utf-8')) for msg in MSGS]
    return ciphertexts

if __name__=='__main__':
    main()
```

The `readlines()` function reads the file line by line and returns a list of strings, while the `\n` characters are kept.

I used the following message to test the behavior:

```plain
a
aa
aaa
aaaa
b
bb
bbb
bbbb
1
11
111
1111


```

Note that there are 2 `\n` characters in the end.

The output of the program differs from run to run due to the randomness of key. One of the outputs is:

```plain
57dc
57b725
57b74e81
57b74eeaee
54dc
54b425
54b44d81
54b44de9ee
07dc
07e725
07e71e81
07e71ebaee
3c
3c
```

The encryption is `c[i] = m[i] ^ k[i]`. If we know any pair of `m[i]` and `c[i]`, we can retrieve `k[i]` by `k[i] = c[i] ^ m[i]`. Then all other `m[i]` can be decrypted with `m[i] = c[i] ^ k[i]`.

For example, from the first column, we know that `\n` (`0x0a`) is encrypted as `3c` (`m[0] ^ k[0] = 0x3c`), then we get `k[0] = 0x3c ^ 0x0a = 0x36`. With `k[0]` we can decrypt all `m[0]`s, where `0x57 ^ 0x36 = 0x61 (a)`, `0x54 ^ 0x36 = 0x62 (b)`, etc.

With this approach, only the `m[i]`s where at least one `m[i]` is `'\n'` (or known) can be decrypted.

There are some other properties:

1. If the two messages are the same, the ciphers would be the same, and vise versa (key is unchanged)
2. Xoring two ciphers gives the xor result of the two messages

The above observations lead to the following possible approaches to decrypting the cipher:

1. Guess the next character of any of the ciphers, and use it to decrypt all other characters. See if the results are reasonable.
2. Most of the messages would be alphabetic (`[a-zA-Z]`). We can xor the pairs of ciphers (`c_a[i] ^ c_b[i] = m_a[i] ^ m_b[i]`) and then xor it with letters in the alphabet. If the result is also alphabetic, then this could be a valid pair of messages. Then decrypt the other messages with this trial and see if the results are reasonable.

## Decryption

### Guessing

The given cipher has a single `c7` in line 15, this character should be `\n` (the last character of each line should be `\n`), then we know `k[0]` is `0xc7 ^ ord('\n')`.

The first colum is decrypted as `['A', 'I', 'O', '"', 'W', 'H', 'A', 'h', 'a', 'F', 'T', 'T', 'B', 'T', '\n', ' ', ' ', ' ']`. Looks good.

Looking into the ciphers, I found that line 11 and 12 have the same prefix `991ca61565` and the first letter is `T`. In English, the words starting with `T` that show up at the beginning of the sentence are usually `The`, `Then`, `They`, `Them`, etc.

After experimenting with the listed possible words, I found that the word is `They` followed by a space. Now the decrypted parts are (ignore the lines that are already ended with `\n`):

```python
['A', 'I', 'O', '"', 'W', 'H', 'A', 'h', 'a', 'F', 'T', 'T', 'B', 'T', '\n', ' ', ' ', ' ']
['p', 't', 'n', 'N', 'i', 'e', 'f', 'e', 'n', 'o', 'h', 'h', 'e', 'h', 't', ' ', ' ', ' ']
['p', ' ', 'l', 'S', 't', ' ', 't', ' ', ' ', 'r', 'e', 'e', 'c', 'e', 'Ã', ' ', ' ', ' ']
['a', 'h', 'y', 'A', 'h', 'd', 'e', 'w', 'e', ' ', 'y', 'y', 'k', 'y', 'l', 'C', 'Y', 'h']
['r', 'a', ' ', ',', ' ', 'r', 'r', 'a', 'l', 't', ' ', ' ', 'e', ' ', 'E', 'o', 'o', 't']
```

Each line above shows a column of the decrypted message. Note the word `After` in the 7-th row, the following should be a space (end of word). Then we get the following:

```python
['A', 'I', 'O', '"', 'W', 'H', 'A', 'h', 'a', 'F', 'T', 'T', 'B', 'T', '\n', ' ', ' ', ' ']
['p', 't', 'n', 'N', 'i', 'e', 'f', 'e', 'n', 'o', 'h', 'h', 'e', 'h', 't', ' ', ' ', ' ']
['p', ' ', 'l', 'S', 't', ' ', 't', ' ', ' ', 'r', 'e', 'e', 'c', 'e', 'Ã', ' ', ' ', ' ']
['a', 'h', 'y', 'A', 'h', 'd', 'e', 'w', 'e', ' ', 'y', 'y', 'k', 'y', 'l', 'C', 'Y', 'h']
['r', 'a', ' ', ',', ' ', 'r', 'r', 'a', 'l', 't', ' ', ' ', 'e', ' ', 'E', 'o', 'o', 't']
['e', 'd', '3', '"', 'a', 'o', ' ', 's', 'i', 'h', 'h', 's', 'r', 's', 'Ð', 'n', 'u', 't']
```

Now the pattern seem to be clearer. The 1st line could start with `Apparently`, the last line would start with `http://` or `https://`, the 3rd last line could be `Congratulations`, etc.

Therefore, we have the following cracked key prefix:

```python
# some hard-coded keys derived from observing the cipher and guessing
key = [
    0xc7 ^ ord('\n'),
    0x1c ^ ord('h'),
    0xa6 ^ ord('e'),
    0x15 ^ ord('y'),
    0x65 ^ ord(' '),
    0xf0 ^ ord(' '),
    0x42 ^ ord('n'),
    0x16 ^ ord('t'),
    0xc6 ^ ord('l'),
    0x64 ^ ord('y'),
    0xe5 ^ ord('u'),
    0xc4 ^ ord('l'),
    0x13 ^ ord('a'),
    0x5c ^ ord('t'),
    0xb5 ^ ord('i'),
    0xe2 ^ ord('o'),
    0x20 ^ ord('n'),
    0x30 ^ ord('s'),
]
```

And the decrypted messages are:

```plain
Apparently, not on
I had een gather
Only 3 percent of 
"NSA," his buddy j
With a mixtue of 
He drove the thirt
After passing thro
he was escorted to
an elite group of 
For the first hour
They hovered aroun
They spoke of stre
Becker observed, l
They scrawled symb

   Congratulations
   You can find th
   https://cseweb.
```

Then the last line could start with `https://cseweb.ucsd.edu/classes/`, and now we get the following text:

```plain
Apparently, not only did the NSA ex
I had een gathering global electr
Only 3 percent of Americans were ev
"NSA," his buddy joked, "stands for
With a mixtue of apprehension and 
He drove the thirty-seven miles to 
After passing through endless secur
he was escorted to a plush research
an elite group of mathematical brai
For the first hour, the cryptograph
They hovered around an enormous tab
They spoke of stream ciphers, self-
Becker observed, lost.
They scrawled symbols on graph pape

   Congratulations, you have gotten
   You can find the rest of the hom
   https://cseweb.ucsd.edu/classes/
```

Note the 2nd last sentence "You can find the rest of the hom", the following could be `homework` followed by a space. Now we are at:

```plain
Apparently, not only did the NSA exist, b
I had een gathering global electronic i
Only 3 percent of Americans were even awa
"NSA," his buddy joked, "stands for 'No S
With a mixtue of apprehension and curios
He drove the thirty-seven miles to their 
After passing through endless security ch
he was escorted to a plush research facil
an elite group of mathematical brainiacs 
For the first hour, the cryptographers se
They hovered around an enormous table and
They spoke of stream ciphers, self-decima
Becker observed, lost.
They scrawled symbols on graph paper, por

   Congratulations, you have gotten this 
   You can find the rest of the homework 
   https://cseweb.ucsd.edu/classes/fa23/c
```

With this approach, the farthest I can go is shown in the following:

```plain
Apparently, not only did the NSA exist, but it was considered 
It had been gathering global electronic intelligence data and 
Only 3 percent of Americans were even aware it existed.
"NSA," his buddy joked, "stands for 'No Such Agency.' "
With a mixture of apprehension and curiosity, Becker accepted 
He drove the thirty-seven miles to their eighty-six-acre headq
After passing through endless security checks and being issued
he was escorted to a plush research facility where he was told
an elite group of mathematical brainiacs known as the code-bre
For the first hour, the cryptographers seemed unaware Becker w
They hovered around an enormous table and spoke a language Bec
They spoke of stream ciphers, self-decimated generators, knaps
Becker observed, lost.
They scrawled symbols on graph paper, pored over computer prin

   Congratulations, you have gotten this far.  But you're not 
   You can find the rest of the homework problems here:
   https://cseweb.ucsd.edu/classes/fa23/cse207B-a/hw1/hw1.pdf
```

And I used the following incremental guesses:

```python
def new_keys(ciphers, guesses):
    # get new keys from guesses / ground truth
    ciphers = bytes.fromhex(ciphers)
    assert len(ciphers) == len(guesses)
    return [c ^ ord(m) for c, m in zip(ciphers, guesses)]

# adding new keys by guessing
key += new_keys('92aea2225e1c65b5b2bb9411d1bac9f2df', 'ucsd.edu/classes/')
key += new_keys('162fd05f505d', 'ework ')
key += new_keys('906d69b21bb7f539471f13f29c', 'se207B-a/hw1/')
key += new_keys('6f51146c', '\'re ')
key += new_keys('72', 'r')
key += new_keys('9dafa8', 'ed ')
```

## References

The following resources helped me while coding:

- [How to convert hexadecimal string to bytes in Python](https://stackoverflow.com/questions/5649407/how-to-convert-hexadecimal-string-to-bytes-in-python)
- [Python zip with padding](https://stackoverflow.com/questions/1277278/is-there-a-zip-like-function-that-pads-to-longest-length)
