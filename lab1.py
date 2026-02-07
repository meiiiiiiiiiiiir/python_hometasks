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
string_function=lambda text: " ".join([
    word[::-1] for word in text.split()
    if not any(char.isdigit() for char in word)
    if len(word)%2==0
])
#3
def top_k_words(text,k):
    text=text.lower()
    clean_text=""
    for char in text:
        if char.isalpha() or char==" ":
            clean_text+=char
        else:
            clean_text+=" "
    words=clean_text.split()
    counts={}
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    items=list(counts.items())
    items.sort(key=lambda x: (-x[1], x[0] ))
    result=[]
    for i in range(min(k,len(items))):
        result.append(items[i][0])
    return result
#4
