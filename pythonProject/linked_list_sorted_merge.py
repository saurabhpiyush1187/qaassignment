# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, data):
      newNode = ListNode(data)
      if (self.head):
          current = self.head
          while (current.next):
              current = current.next
          current.next = newNode
      else:
          self.head = newNode

      # print method for the linked list

  def printLL(self):
      current = self.head
      while (current):
          print(current.val)
          current = current.next

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        l3 = res

        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        if l1: l3.next = l1
        if l2: l3.next = l2

        return res.next




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    l1=ListNode(3)
    l1.next=ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(7)
    res = mergeTwoLists(l1,l2)
    while res:
        print(res.val)
        res=res.next






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
