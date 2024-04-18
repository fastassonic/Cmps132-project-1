class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child is not child_node]

    def traverse(self):
        notes_to_visit = [self]
        while len(notes_to_visit) > 0:
            curentnode = notes_to_visit.pop()
            notes_to_visit += curentnode.children
    def tree_height(self, heightcount=0):
        notes_to_visit = [self]
        while len(notes_to_visit) > 0:
            curentnode = notes_to_visit.pop()
            if curentnode.children != []:
                heightcount += 1
                listcount = []
                for i in curentnode.children:
                    listcount.append(i.tree_height(heightcount))
                return (max(listcount))
            else:
                return heightcount
    
    def returnchild(self,value):
        for i in self.children:
            if i.value == value:
                return i
        return None