'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


def find_max(t,z):
    
    # I tried not to use built-in functions as much as I could.
    # Also, 'return max_value' was not printing the output when we run the function in terminal. That is why I used print function in the end. 

    ##### this part is to create the substring list of t

    length_of_t = 0
    for char in t:
        length_of_t += 1
    # or just simply; length_of_t = len(t)


    substring_list_of_t = []
    for index_of_first_letter in range(length_of_t):
        for index_of_last_letter in range(index_of_first_letter + 1, length_of_t + 1):
            substring = t[index_of_first_letter:index_of_last_letter]
            substring_list_of_t += [substring]

    ##### this part is to create the substring list of t



    ##### this part is to create the substring list of z

    length_of_z = 0
    for char in z:
        length_of_z += 1
    # or just simply; length_of_z = len(z)

    substring_list_of_z = []
    for index_of_first_letter in range(length_of_z):
        for index_of_last_letter in range(index_of_first_letter + 1, length_of_z + 1):
            substring = z[index_of_first_letter:index_of_last_letter]
            substring_list_of_z += [substring]

    ##### this part is to create the substring list of z


    # this part is to collect the multiplication values
    multiplication_values = []
    for substring_t in substring_list_of_t:

        count = 0
        for substring_z in substring_list_of_z:
            if substring_z == substring_t:
                count += 1

        length_of_substring = 0
        for char in substring_t:
            length_of_substring += 1

        multiplication_value = count * length_of_substring
        multiplication_values += [multiplication_value]


    # this part is to get the maximum result
    max_value = multiplication_values[0]
    for value in multiplication_values:
        if value > max_value:
            max_value = value
    # or just simply; 
    # max_value = max(multiplication_values)


    # return max_value
    print(max_value)




if __name__ == '__main__':
    find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")



