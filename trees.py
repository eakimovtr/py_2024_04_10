class Node:
    def __init__(self, data: int, left=None, right=None):
        self.data: int = data
        self.left: Node = left
        self.right: Node = right
        
    def append(self, node) -> None:
        if node.data < self.data:
            if not self.left:
                self.left = node
            else:
                self.left.append(node)
        elif node.data > self.data:
            if not self.right:
                self.right = node
            else:
                self.right.append(node)
        else:
            raise Exception(f"Value {node.data} is already in tree")
    
    def traverse_in_depth(self) -> None:
        if self.left:
            self.left.traverse_in_depth()
        if self.right:
            self.right.traverse_in_depth()
        print(self.data)
        
    @staticmethod
    def build_from_list(nodes: list[int]):
        root = Node(nodes[0])
        for value in nodes[1:]:
            root.append(Node(value))
        return root
            
    def delete_node(self, value: int) -> None:
        if value > self.data:
            self.right = self.right.delete_node(value)
        elif value < self.data:
            self.left = self.left.delete_node(value)
            
        if self.left is None:
            temp = self.right
            del self
            return temp
        elif self.right is None:
            temp = self.left
            del self
            return temp
        
    
    # def get_nodes_list(self, result=None) -> list:
    #     if not result:
    #         result = [self]
    #     while self is not None:
    #         result.extend(self.get_nodes_below())

    # def get_nodes_below(self) -> list:
    #     return [self.left, self.right]
    
    def __repr__(self) -> str:
        return f"{self.data}"    


nodes = [10, 5, 7, 16, 13, 2, 20]
    
root = Node.build_from_list(nodes)
root.delete_node(20)
root.traverse_in_depth()