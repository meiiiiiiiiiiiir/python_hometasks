#1
def analyze_text(text):
    vowels="aeiyou"
    found_vowels=[]
    for char in text:
        char=char.lower()
        if char in vowels:
            if char not in found_vowels:
                found_vowels.append(char)
    count=len(found_vowels)
    clean_text=""
    for char in text:
        if char.isalpha():
            clean_text+=char
        else:
            clean_text+=" "
    words_list=clean_text.split()
    result=[]
    seen_words=[]
    for word in words_list:
        if len(word)>=5:
            first_char=word[0]
            last_char=word[-1]
            if first_char.lower()==last_char.lower():
                word_lower=word.lower()
                if word_lower not in seen_words:
                    result.append(word)
                    seen_words.append(word_lower)
    final_result=" ".join(result)
    return count,final_result

#2
