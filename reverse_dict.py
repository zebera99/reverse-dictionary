def reverse_dict(dict):
    new_dict = {}  
    for key, value in dict.items():
        new_dict[value], new_dict[key] = key, value

    return new_dict  


# 영-한 단어장 eng-kor dict
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력 print kor-eng dict
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))
