def word_count(text):
    word_list = text.split()
    return len(word_list)

def character_counts(text):
    l_text = text.lower()
    c_dict = {}
    for c in l_text:
        if c in c_dict:
            c_dict[c] = c_dict[c] + 1
        else:
            c_dict[c] = 1
    return c_dict

def list_dict(c_dict):
    def sort_on(items):
        return items["num"]
    l_dict = []
    for i in c_dict:
        # a: 45
        temp_dict = {"char": i, "num": c_dict[i]}
        l_dict.append(temp_dict)
    l_dict.sort(reverse=True, key=sort_on)
    return l_dict
    



