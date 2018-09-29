'''
=========================================================
Vigenère cipher script for TJCTF 2018, challenge: vinegar
=========================================================

Algorithm:

1. Get key
> key = get_key()

2. Decrypt
> ct = uucbx{simbjyaqyvzbzfdatshktkbde}
> pt = vigener(key, ct)

3. Add to file
> file = open("vinegar.txt", "a")
> file.write(pt)
'''

import itertools
import pycipher


if __name__ == "__main__":
    iterable = "abcdefghijklmnopqrstuvwxyz"
    known_pt = "blais"
    ct = "uucbxsimbjyaqyvzbzfdatshktkbde"

    #product = itertools.combinations(iterable, 4)  # WRONG
    product = itertools.product(iterable, repeat=4)

    # Add known pt to key, in form 'blais----'
    for i in product:
        key = known_pt

        # Append letters from tuple to key
        for letter in i:
            key += letter
        #print(i)
        #print(key)

        pt = pycipher.Vigenere(key).decipher(ct).lower()

        # Split plaintext into two to add the curly braces, then combine again
        pt_1 = pt[:5]
        pt_2 = pt[5:]
        pt = pt_1 + "{" + pt_2 + "}"
        #print(pt)

        # Append to file
        file = open("vinegar_pt.txt", "a")
        file.write(pt + "\n")   

