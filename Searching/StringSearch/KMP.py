def KMP_search(pattern: str, text: str):

    l_pattern = len(pattern)
    l_text = len(text)
    pst = build_prefix_table(pattern, l_pattern)

    i_pattern = 0
    i_text = 0

    looped_through = False

    while not looped_through:
        if pattern[i_pattern] == text[i_text]:
            i_pattern += 1

            if i_pattern == l_pattern:
                return i_text
            
            i_text += 1
            
        else:
            i_pattern = pst[i_pattern]
        
        if i_text == l_text:
            return -1

def build_prefix_table(pattern: str, l_pattern: int):
    table = [0] * l_pattern
    
    i_prefix = 0
    i_text = 1

    looped_through = False
    
    while not looped_through:
        if pattern[i_text] == pattern[i_prefix]:
            table[i_text] = i_prefix
            i_prefix += 1
            i_text += 1
        else:
            i_prefix = 0
            table[i_text] = i_prefix
            i_text += 1
        
        if i_text == l_pattern:
            looped_through = True
    
    return table