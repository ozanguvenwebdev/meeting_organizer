'''
You have a text that some of the words in reverse order.
The text also contains some words in the correct order, and they are wrapped in parenthesis.
Write a function fixes all of the words and,
remove the parenthesis that is used for marking the correct words.

Your function should return the same text defined in the constant CORRECT_ANSWER
'''


INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"


def fix_text(mystr):


    # I tried not to use built-in functions as much as I could.
    # I separated words that start and end with parentheses. 
    # Afterwards I left them as they were. 
    # I reversed all the other words and eliminated the space at the end.


    # turning the input into a single line 
    single_line = ""
    for word in mystr:
        single_line += word


    # making the single line a list
    output_list = []
    temporary_word = ""
    for char in single_line:
        if char != " ":
            temporary_word += char
        else:
            output_list += [temporary_word]
            temporary_word = ""

    if temporary_word != "":
        output_list += [temporary_word]



    # output_list:  ['nhoJ', '(Griffith)', 'nodnoL', 'saw', '(an)', '(American)', ',tsilevon', ',tsilanruoj', '(and)', 'laicos', '.tsivitca', '((A)', 'reenoip', '(of)', 'laicremmoc', 'noitcif', '(and)', 'naciremA', ',senizagam', '(he)', 'saw', 'eno', '(of)', '(the)', 'tsrif', '(American)', 'srohtua', '(to)', 'emoceb', '(an)', 'lanoitanretni', 'ytirbelec', '(and)', 'nrae', 'a', 'egral', 'enutrof', '(from)', ').gnitirw']

    final_list = []
    for item in output_list:        
        if item[0] == "(" and item[-1] == ")":
            
            char_list = []
            for char in item:
                char_list += char

            char_list.pop(0)
            char_list.pop(-1)

            new_word = ""
            for char in char_list:
                new_word += char
            # new_word: 'Griffith'
            final_list += [new_word]

        else:
            new_word = item[::-1]
            final_list += [new_word]

    final_string = ""



    for string in final_list:
        # erase the last space in the end of the final_string
        if not final_list[-1] == string: 
            string = string + " "
            final_string += string
        else:
            final_string += string

    mystr = final_string

    return mystr




if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")
