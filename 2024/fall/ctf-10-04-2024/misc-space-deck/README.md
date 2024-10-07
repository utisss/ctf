# Space Deck
* **Event:** SpaceCTF (ISSS CTF 10-04-2024)
* **Problem Type:** Misc

## Background
N/A

## Exploit

The main challenge is to figure out where this screenshot came from. There is nothing hidden in the
image itself since this is not a forensics challenge. You could try a variety of methods, including
social engineering (I will yap about Pokemon if given the chance to), but a reverse google image
search eventually points you to the correct site, [pokemoncard.io](https://pokemoncard.io), which
you can verify by comparing the CSS present in the site as well as the site layout with that shown
in the screenshot. After finding the site, now we want to find the specific page the screenshot is
from. After poking around on the site for a while, you might find that there is an advanced search
feature, where you can search for decks containing specific cards. The deck in the screenshot is the
only deck which contains those cards; but also you can simply enter a couple of the cards present
and look manually, since the deck was only made while I was making this CTF problem. Or, if you just
searched for utflag, this is also the only deck on the whole site that has that in its name.