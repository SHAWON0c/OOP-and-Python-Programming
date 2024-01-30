def rev_word(s):
    words= s.split()

    reversed_word=[]

    for word in words:
        revers_word=word[::-1]
        reversed_word.append(revers_word)
    result=' '.join(reversed_word)
    return result


input_string= input()
output_string= rev_word(input_string)
print(output_string)