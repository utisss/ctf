 # Problem Title
 * **Event:** legumesCTF
 * **Problem Type:** Crypto
 * **Point Value / Difficulty:** Easy
 * **(Optional) Tools Required / Used:**
 
 ## Steps

 #### Step 1
 This problem involes a column cipher, a type of transposition cipher where the message is written as a block and then the columns are shuffled around. The number of columns and how they are shuffled is determined by the key (see [here](https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition) for more information). We then read down each column to get our cipher. Basically, we shuffle the columns and then transpose them. Thus, in order to decrypt, we have to transpose again and then reverse the shuffling.

 #### Step 2
To transpose again, we read along the columns to get

```
HLFG{SUAT
EDLHAVO_U
UNO_DO_ED
S_ERANBTL
}ISIONPTO
```
 #### Step 3
 We have a pretty good idea of how to reshuffle the message since we know it must start with "utflag{". In addition, we know the first column must be moved to the end so the message ends with a curly brace. This means our flag must be
 
```
UTFLAG{SH
OULD_HAVE
_DONE_DOU
BLE_TRANS
POSITION}
```
