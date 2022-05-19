class Node:
    def __init__(self):
        self.parent=None
        self.childnodelist=[]
        self.datalist=[]
class Tree:
    def __init__(self):
        self.rootnode=Node()

    def is_leaf(self,node:Node):
        if len(node.childnodelist)==0:
            return True
        else:
            return False

    def insert_node(self,node:Node,data):
        while True:
            if self.is_leaf(node):
                node.datalist.append(data)
                node.datalist.sort()
                self.split(node)
                break
            else:
                if len(node.datalist)==1:
                    if data>node.datalist[0]:
                        node=node.childnodelist[1]
                    else:
                        node=node.childnodelist[0]
                elif len(node.datalist)==2:
                    if data<node.datalist[0]:
                        node=node.childnodelist[0]
                    elif data>node.datalist[1]:
                        node=node.childnodelist[2]
                    else:
                        node=node.childnodelist[1]

    def is_three(self,node:Node):
        if len(node.datalist)==3:
            return True
        else:
            return False

    def split(self, node: Node):
        if self.is_three(node):
            if self.is_leaf(node):
                if node.parent == None:
                    pnode=Node()
                    node.parent = pnode
                else:
                    pnode=node.parent
                leftnode = Node()
                leftnode.datalist.append(node.datalist[0])
                rightnode = Node()
                rightnode.datalist.append(node.datalist[2])
                pnode.datalist.append(node.datalist[1])
                pnode.datalist.sort()

                pnode.childnodelist.append(leftnode)
                pnode.childnodelist.append(rightnode)
                for child in pnode.childnodelist:
                    if child==node:
                        pnode.childnodelist.remove(child)
                        child.parent=None
                leftnode.parent, rightnode.parent = pnode,pnode
                pnode.childnodelist.sort(key=lambda x:x.datalist[0])
                node=pnode
                self.to_root(pnode)
            else:
                if node.parent == None:
                    pnode = Node()
                else:
                    pnode=node.parent
                leftnode = Node()
                leftnode.datalist.append(node.datalist[0])
                rightnode = Node()
                rightnode.datalist.append(node.datalist[2])

                pnode.datalist.append(node.datalist[1])
                pnode.datalist.sort()
                node.childnodelist.sort(key=lambda  x:x.datalist[0])

                leftnode.childnodelist.append(node.childnodelist[0])
                node.childnodelist[0].parent=leftnode
                leftnode.childnodelist.append(node.childnodelist[1])
                node.childnodelist[1].parent=leftnode
                rightnode.childnodelist.append(node.childnodelist[2])
                node.childnodelist[2].parent=rightnode
                rightnode.childnodelist.append(node.childnodelist[3])
                node.childnodelist[3].parent=rightnode
                pnode.childnodelist.append(leftnode)
                pnode.childnodelist.append(rightnode)
                for child in pnode.childnodelist:
                    if child==node:
                        pnode.childnodelist.remove(child)
                        child.parent=None
                pnode.childnodelist.sort(key=lambda x:x.datalist[0])
                leftnode.parent, rightnode.parent=pnode,pnode
                node=pnode
                self.to_root(node)
            self.split(pnode)
        else:
            return

    def delete_node(self,data):
        delnode=self.find_node_without_route(data)
        if self.is_three(delnode):
            if self.is_leaf(delnode):
                delnode.datalist.remove(data)
            else:
                if delnode.datalist[0]==data:
                    if len(delnode.childnodelist[0].datalist)==2 and len(delnode.childnodelist[1].datalist)==2:


                elif delnode.datalist[1]==data:





    def merge(self,node:Node):


    def to_root(self,node:Node):
        while node.parent!=None:
            node=node.parent
        self.rootnode=node

    def show(self,node:Node):
        if len(node.datalist)==0:
            return
        for data in node.datalist:
            print(data ,",",end='')
        for childnode in node.childnodelist:
            print("(", end='')
            self.show(childnode)
            print(")",end='')

    def get_min(self,node:Node):
        while node.childnodelist:
            node=node.childnodelist[0]
        print(node.datalist[0])

    def get_max(self,node:Node):
        while node.childnodelist:
            node=node.childnodelist[-1]
        print(node.datalist[-1])

    def height(self,node:Node):
        count=1
        while node.childnodelist:
            node=node.childnodelist[0]
            count+=1
        print(count)

    def find_node(self,data):
        node=self.rootnode
        route="root"
        while node.childnodelist:
            if data in node.datalist:
                print(route)
                return node
            else:
                if len(node.datalist)==1:
                    if data>node.datalist[0]:
                        node=node.childnodelist[1]
                        route+=" right"
                    else:
                        node=node.childnodelist[0]
                        route+=" left"
                else:
                    if data<node.datalist[0]:
                        node=node.childnodelist[0]
                        route+=" left"
                    elif data>node.datalist[1]:
                        node=node.childnodelist[2]
                        route+=" right"
                    else:
                        node=node.childnodelist[1]
                        route+=" middle"
        print("없어요ㅠ")
        return None

    def find_node_without_route(self,data):
        node=self.rootnode
        while node.childnodelist:
            if data in node.datalist:
                return node
            else:
                if len(node.datalist)==1:
                    if data>node.datalist[0]:
                        node=node.childnodelist[1]
                    else:
                        node=node.childnodelist[0]
                else:
                    if data<node.datalist[0]:
                        node=node.childnodelist[0]
                    elif data>node.datalist[1]:
                        node=node.childnodelist[2]
                    else:
                        node=node.childnodelist[1]
        return None


    def left_traverse(self,node:Node):
        if node==None:
            return

        if len(node.datalist)==1:
            if self.is_leaf(node):
                print(node.datalist[0],end=' ')
            else:
                self.left_traverse(node.childnodelist[0])
                print(node.datalist[0],end=' ')
                self.left_traverse(node.childnodelist[1])

        if len(node.datalist)==2:
            if self.is_leaf(node):
                print(node.datalist[0],node.datalist[1],end=' ')
            else:
                if node.childnodelist[0]:
                    self.left_traverse(node.childnodelist[0])
                print(node.datalist[0],end=' ')
                if node.childnodelist[1]:
                    self.left_traverse(node.childnodelist[1])
                print(node.datalist[1],end=' ')
                if node.childnodelist[2]:
                    self.left_traverse(node.childnodelist[2])

    def right_traverse(self,node:Node):
        if node==None:
            return

        if len(node.datalist)==1:
            if self.is_leaf(node):
                print(node.datalist[0],end=' ')
            else:
                self.right_traverse(node.childnodelist[1])
                print(node.datalist[0],end=' ')
                self.right_traverse(node.childnodelist[0])

        if len(node.datalist)==2:
            if self.is_leaf(node):
                print(node.datalist[1],node.datalist[0],end=' ')
            else:
                if node.childnodelist[2]:
                    self.right_traverse(node.childnodelist[2])
                print(node.datalist[1],end=' ')
                if node.childnodelist[1]:
                    self.right_traverse(node.childnodelist[1])
                print(node.datalist[0],end=' ')
                if node.childnodelist[0]:
                    self.right_traverse(node.childnodelist[0])

    def get_right_child(self,data):
        node=self.find_node_without_route(data)
        if node==None or node.childnodelist==None:
            print("없슴")
            return
        print(node.childnodelist[-1].datalist)

    def get_left_child(self,data):
        node=self.find_node_without_route(data)
        if node==None or node.childnodelist==None:
            print("없슴")
            return
        print(node.childnodelist[0].datalist)

    def get_middle_child(self,list):
        node=self.find_node_without_route(list[0])
        if node==None or node.childnodelist==None or len(node.datalist)==1:
            print("없슴")
            return
        print(node.childnodelist[1].datalist)

    def count_node(self,node):
        total=0
        if self.is_leaf(node):
            total+=1
        else:
            for child in node.childnodelist:
                total+=self.count_node(child)

        return total

    def clear(self,node):
        self.rootnode=None



