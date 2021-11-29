"""
Module with validators
======================
"""
def valid_test(mytest):
    """
    Function validate count questions
    """
    if mytest.card_set.count() >= 4:
        mytest.flag = True
        mytest.save()
    return mytest

