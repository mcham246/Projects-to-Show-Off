# The rotation of a linked list can be defined as an operation that makes a node k 
# the new head of the linked list, and appends each element that was before k to the 
# end of the linked list. We can call the element selected the kth element of the linked 
# list, and thus call the resulting linked list the kth rotation. 

# Write a function, which takes a Node and an integer k as it’s arguments and returns a new 
# node that is the head of the kth rotation of the linked list. If the value k is longer than 
# the length of the linked list, is 0, or is negative, instead return the original linked list. 
# If the Node is None, return None. You will not be passed a circular linked list.
# You are guaranteed the linked list will have no more than 1,000,000 nodes.

# Write Up:
# if the head is empty of k = 0 then return head
# loop to point to the kth element also checks if k > then length of list
# if the last element is none we know k is greater than the list length
# Assign the new head (newNode)
# Find the last node so we know where to put the old head
# Assign head as the last node
# Because nothing should come after the old head we set that placeholder to none

# O(n) time to rotate list and O(n) space to store n items



class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

def rotate_list(head: 'Node', k: int) -> 'Node':
    temp = head
    if temp == None or k == 0 :
        return head
    
    c = 1
    while(c <k and temp != None):
        temp = temp.next
        c += 1
    if temp == None:
            return head
    newNode = temp
    while(temp.next != None):
        temp = temp.next
    temp.next = head
    head = newNode.next
    newNode.next = None

    return head