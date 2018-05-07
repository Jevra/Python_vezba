from vezba.structures import Stack, Node, List, Queue, Tree, NodeTree


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


myTree = Tree()
myTree.add_node(8)
myTree.add_node(3)
myTree.add_node(10)
myTree.add_node(1)
myTree.add_node(6)
myTree.add_node(4)
myTree.add_node(7)
myTree.add_node(14)
myTree.add_node(13)

print("My tree in preorder: ")
myTree.pre_order(myTree.root)
print("My tree in inorder: ")
myTree.in_order(myTree.root)

print("Removing element '1'")
myTree.remove_node(1)
print("My tree in preorder: ")
myTree.pre_order(myTree.root)

print("Removing element '14'")
myTree.remove_node(14)
print("My tree in preorder: ")
myTree.pre_order(myTree.root)


myTree.add_node(1)

print("Removing element '3'")
myTree.remove_node(3)
print("My tree in preorder: ")
myTree.pre_order(myTree.root)

print("Removing element '14' again!")
myTree.remove_node(14)