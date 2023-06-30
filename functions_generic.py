# Generate lyndon words
def generate_lyndon_words(alphabet_size, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output_array = []
    S = []
    for i in range(alphabet_size):
        S.append(alphabet[i])
    k = len(S)
    S.sort()

    # To store the indices
    # of the characters
    w = [-1]

    # Loop till w is not empty
    while w:

        # Incrementing the last character
        w[-1] += 1
        m = len(w)
        if m == n:
            output_array.append(''.join(S[i] for i in w))

        # Repeating w to get a
        # n-length string
        while len(w) < n:
            w.append(w[-m])

        # Removing the last character
        # as long it is equal to
        # the largest character in S
        while w and w[-1] == k - 1:
            w.pop()

    return output_array

def rotations(string):
    output = []
    n = len(string)
    s = string
    for i in range(n):
        s = s[-1] + s[:n - 1]
        output.append(s)
    return output


def rotate(string):
    n = len(string)
    s = string
    s = s[-1] + s[:n - 1]
    return s

def duval_factorization(word):
    factors = []
    i = 0
    n = len(word)
    while i < n:
        j = i + 1
        k = i
        while j < n and word[k] <= word[j]:
            if word[k] < word[j]:
                k = i
            else:
                k += 1
            j += 1
        while i <= k:
            factors.append(word[i: i + j - k])
            i += j - k
    return factors

def bbwt(string):
    # Create an array of factors
    # babbaba --> ['b', 'abb', 'ab', 'a']
    sub_words = duval_factorization(string)

    # Find the longest factor, so we can extend to that length
    # ['b', 'abb', 'ab', 'a'] --> len('aab') == 3
    longest_factor = 0
    for sub_word in sub_words:
        if len(sub_word)>longest_factor:
            longest_factor = len(sub_word)

    # Create a sorted array of (extended) rotations
    # Start with    ---> ['b', 'abb', 'ab', 'a']
    # All rotations ---> ['b','bab', 'bba', 'abb','ba', 'ab','a']
    # Extend ----------> ['bbb', 'bab', 'bba', 'abb', 'baba', 'abab', 'aaa']
    # Then sort -------> ['aaa', 'abab', 'abb', 'bab', 'baba', 'bba', 'bbb']
    bbwt = []
    for sub_word in sub_words:
        bbwt_rotations = rotations(sub_word)
        for rotation in bbwt_rotations:
            extended_rotation = rotation
            while len(extended_rotation)<longest_factor:
                extended_rotation = extended_rotation + rotation
            bbwt.append(extended_rotation)
    bbwt = sorted(bbwt)

    # Create the BBWT
    # ['aaA', 'abaB', 'abB', 'baB', 'babA', 'bbA', 'bbB'] --> abbbaab
    output_string = ""
    for sub_word in bbwt:
        output_string += sub_word[-1]

    return output_string

def bwt(s):
    n = len(s)
    s = s + "$"
    rotations = [s[i:n+1] + s[0:i] for i in range(n+1)]
    rotations.sort()
    return ''.join([r[-1] for r in rotations])

def is_lyndon_word(s):
    n = len(s)
    i = 0
    j = 1
    k = 0

    while i < n and j < n and k < n:
        if s[(j + k) % n] == s[(i + k) % n]:
            k += 1
        elif s[(j + k) % n] < s[(i + k) % n]:
            i = i + k + 1
            k = 0
        else:
            j = j + k + 1
            k = 0

        if i == j:
            j = j + 1

    return i == 0