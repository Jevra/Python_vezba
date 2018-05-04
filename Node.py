from vezba.structures import Stack, Node, List, Queue


listOfInformation = [1, 2, 3, 4, 5]

myList = List()
stack = Stack()
queue = Queue()

for value in listOfInformation:
    myList.add_element(Node(value))
    stack.push(Node(value))
    queue.add(Node(value))


print("My List :")
temp = myList.head
while temp is not None:
    print(temp.read_information())
    temp = temp.next

print("Delete element 2: ")
myList.delete_element(Node(2))
temp = myList.head
while temp is not None:
    print(temp.read_information())
    temp = temp.next

print("Delete element 5: ")
myList.delete_element(Node(5))
temp = myList.head
while temp is not None:
    print(temp.read_information())
    temp = temp.next


print("My stack: ")
temp = stack.head
while temp is not None:
    print(temp.read_information())
    temp = temp.next

stack.push(Node(6))

print("Push 6: ")
temp = stack.head
while temp is not None:
    print(temp.read_information())
    temp = temp.next

stack.pop()
stack.pop()
stack.pop()

print("Pop 3 times: ")
temp = stack.head
while temp is not None:
    print(temp.read_information())
    temp = temp.next


print("My queue: ")
temp = queue.head
while temp is not None:
    print(temp.read_information())
    temp = temp.next


queue.remove()

print("Remove element: ")
temp = queue.head
while temp is not None:
    print(temp.read_information())
    temp = temp.next