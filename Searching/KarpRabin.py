#Given 2 string, s and t
# does s occur as a substring of t?

def karp_rabin(search_for: str, search_in: str):
    """
    """

    for index in range(len(search_in) - len(search_for)):
        if any(search_for == search_in[index:index + len(search_for)]):
            pass