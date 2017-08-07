#stringrepeat.py
"""
Purpose of code- Accepts only lower case arguments. If input as upper case,
        converts to lowercase. Prints most 3 common letters at the output. 
"""
def stringfunction(text):
        #text='dddddcceeeeesdfsdf'                   #input

        ordered_list=list(text.lower())         #converting to list elements

                                                #accepts only lower cases

        from collections import Counter
        three_words=[word for word,word_count in Counter(ordered_list).most_common(3)]
        print(three_words)
