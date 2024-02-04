class treeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = int(' ') * self.get_level()
        print(spaces + self.data)
        for child in self.children:
            if len(self.children):
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
            return level


def build_product_tree():
    root = treeNode("Electronic_store")
    
    laptop = treeNode("laptop")
    laptop.add_child(treeNode("mac"))
    laptop.add_child(treeNode("thinkpad"))
    laptop.add_child(treeNode("apple"))
    root.add_child(laptop)

    cellphone = treeNode("mobile")
    cellphone.add_child(treeNode("Qmobile"))
    cellphone.add_child(treeNode("iphone"))
    cellphone.add_child(treeNode("vivo"))
    root.add_child(cellphone)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    print(root.get_level())
    root.print_tree()
    pass



