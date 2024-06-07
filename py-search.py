import pythainlp
from pythainlp.tokenize import word_tokenize
from pythainlp.tag import pos_tag

def find_subject_name(text):
    tokens = word_tokenize(text, engine='newmm')
    pos_tags = pos_tag(tokens)
    
    print(f"Tokens: {tokens}")
    print(f"POS Tags: {pos_tags}")

    subject_name = []
    found_subject = False

    for word, pos in pos_tags:
        if pos == 'PPRS' and not found_subject:
            # Start of the subject
            subject_name.append(word)
            found_subject = True
        elif found_subject and (pos == 'NCMN' or pos == 'NPRP'):
            # Continue appending if it's part of the subject's full name
            subject_name.append(word)
        elif found_subject:
            # Stop if we have found the subject and encounter a non-NCMN word
            break
    
    return " ".join(subject_name)

text = "สวัสดีครับ ผมชื่อชัชวาล"
subject_name = find_subject_name(text)
print(f"ประธานของประโยคคือ: {subject_name}")
