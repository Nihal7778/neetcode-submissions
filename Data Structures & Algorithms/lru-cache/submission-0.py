class Node:

    def __init__(self, key, value):

    
        self.key = key
        self.value = value

  
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity

     
        self.cache = {}

  
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        
        self.head.next = self.tail
        self.tail.prev = self.head


  
    def addNode(self, node):

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node



    def deleteNode(self, node):

        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode


    def get(self, key: int) -> int:

 
        if key not in self.cache:
            return -1

       
        node = self.cache[key]

     
        self.deleteNode(node)
        self.addNode(node)

  
        return node.value


    def put(self, key: int, value: int) -> None:


        if key in self.cache:

         
            node = self.cache[key]
            self.deleteNode(node)

   
        newNode = Node(key, value)

 
        self.addNode(newNode)

        self.cache[key] = newNode

   
        if len(self.cache) > self.capacity:

           
            lru = self.tail.prev

        
            self.deleteNode(lru)

          
            del self.cache[lru.key]