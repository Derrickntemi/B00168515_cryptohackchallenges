# Explanation
zlib is a lossy compression method, therefore, it gets rid of duplicate characters when compressing. Since we know the flag starts with the following prefix (crypto{). We can attempt to guess the next character,
If we guess the correct character then the length of the output remains the same compared to the initial size, otherwise the length of the output will be bigger than the initial size.


# flag
crypto{CRIME_571ll_p4y5}