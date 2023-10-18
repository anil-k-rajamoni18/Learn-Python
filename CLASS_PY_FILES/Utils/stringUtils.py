username = "bhanu"
password = "bhanu@123"

def string_length(input_string: str) -> int:
    '''
    display the length of the string
    '''
    len =  0 
    for _ in input_string:
        len = len+1
    return len 

def string_len_without_spaces(input_string: str) -> int:
    '''
     display string length without spaces 
    '''
    pass


def print_vowels(input: str) -> list[str]: 
    '''
    display all vowels 
    '''
    vowels = "a e i o u A E I O U".split()
    output = []
    for ch in input:
        if ch in vowels:
            output.append(ch)
    return output




def check_palindrome(input: str) -> bool:
    ''''
    display whether string is palindrome or not 
    '''
    pass


def check_panagram(input: str) -> bool:
    '''
    display whether string is panagram or not 
    '''
    pass

def count_of_special_chars(input: str) -> int:
    '''
    display count of special characters   
    '''
    pass

def reverse(input: str) -> str:
    ''''
    display reverse of a string.
    '''
    pass









