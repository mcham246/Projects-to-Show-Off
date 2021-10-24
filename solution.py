# The is_valid_aux function checks if the string in the list is a valid tag
# First check for the isValid function is to see if the array is empty 
# If the length of the array is less than 2 then return false because we need at least two tags
# Create a stack and popped the start tags on to it
# Whenever a end tag is found compare it with the last element added to the stack
# If the element is a matching start tag to the end tag then proceed else return false
# If the loop fully executes then True is returned

# Run time: O(n) -> goes through list linearly
# storage space: O(n) -> stack(array) can hold at most n elements 
def is_valid_aux(tag):
    if tag == '<div>' or tag == '</div>' or tag == '<p>'  or tag == '</p>' or tag == '<h>' or tag == '</h>':
        return True

def isValid(tags):
    if tags == None:
        return False
    if len(tags) < 2:
        return False 

    stack = []
    for items in tags: 
        if is_valid_aux(items) == True:
            if items == '<div>' or items == '<p>' or items == '<h>':
                stack.append(items)
            if items == '</div>':
                val = stack.pop()
                if val != '<div>':
                    return False
            if items == '</p>':
                val = stack.pop()
                if val != '<p>':
                    return False
            if items == '</h>':
                val = stack.pop()
                if val != '<h>':
                    return False
            

    return True
