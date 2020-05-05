1. create dictionary
2. res


# how to deal with ties
can use heap can you preallocate res?
every new word

(occ,index,word)

dict{word:[earliest index:occ]}
def word_count_engine(document):
    "Practice makes perfect. you'll only get Perfect by practice. just practice!"
    #
    var: word
    test cases:
    '''
    ppra/a makes
    //aa. makes
    a a a
    you/ll
    practice. 
    
    sp___sp
    ___sp
    /__/__sp
    ///_sp
    ///sp_sp
    last_index
    '''
    updatedict():-lowercaseword
    loop document:
        1. if char: add to word
        2. if " " or last_index: update dictionary - check if word ""
        3. if last index: update dictionary

