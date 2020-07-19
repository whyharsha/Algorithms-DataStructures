#Given 2 string, s and t
# does s occur as a substring of t?
base_size = 1024
modulus = 1000037 #arbitrary prime ~ the unicode character set size

def karp_rabin(pattern: str, in_text: str):
    """
    Uses the Karp-Rabin algorithm to search for substrings.
    Returns the index of the first match.
    """
    l_pattern = len(pattern)
    l_in_text = len(in_text)

    if l_pattern > l_in_text:
        return -1
    
    h_pattern = rolling_hash(pattern, 0, True)
    h_in_text = rolling_hash(in_text[0:l_pattern], 0, True)

    for index in range(0, (l_in_text - l_pattern)):
        if h_pattern == h_in_text and pattern == in_text[index:index + l_pattern]:
            return index
        else:
            if index + l_pattern + 1 < l_in_text:
                h_in_text = rolling_hash(in_text[index + 1:index + 1 + l_pattern], h_in_text, False)
    
    return -1

def rolling_hash(input_str: str, current_hash: float, is_start: bool):

    l_input = len(input_str)

    if is_start:
        for index in range(l_input):
            multiple = base_size ** (l_input - index - 1)
            current_hash = (ord(input_str[index]) * multiple) + current_hash
    else:
        delete_initial = ord(input_str[0]) * (base_size ** (l_input - 1))
        current_hash = ((current_hash - delete_initial) * base_size) + ord(input_str[l_input - 1])
    
    return current_hash % modulus