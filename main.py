class Node:
    def __init__(self,key):
       self.data=key
       self.left=None
       self.right=None

def level_order_traversal(root):
    queue=[]
    queue.append(root)
    while(len(queue)!=0):
        value=queue.pop(0)
        print(value.data,end=" ")
        if(value.left!=None):
            #print(value.left.data)
            queue.append(value.left)
        if(value.right!=None):
             #print(value.right.data)
             queue.append(value.right)

def reverse_level_order_traversal(root):
    queue1=[]
    queue2=[]
    queue1.append(root)
    while(len(queue1)!=0):
         value=queue1.pop(0)
         queue2.append(value)
         if(value.left!=None):
             queue1.append(value.left)
         if(value.right!=None):
             queue1.append(value.right)
    queue2.reverse() 
    for x in queue2:
        print(x)    
    # for i in queue2[::-1]:
    #     print(queue2[i])         
    
        
def height_of_the_tree(root):
    if(root==None):
        return 0
    return 1+ max(height_of_the_tree(root.left),height_of_the_tree(root.right))

def diameter_of_tree(root):    
    if(root==None):
        return 0
    lheight=height_of_the_tree(root.left)
    rheight=height_of_the_tree(root.right)

    ldiameter=diameter_of_tree(root.left)
    rdiameter=diameter_of_tree(root.right)

    return max(1+lheight+rheight,max(ldiameter,rdiameter))   

def mirror_of_the_tree(root):

    if(root==None):
        return None
    created_node=Node(root)
    created_node.left=mirror_of_the_tree(root.right)
    created_node.right=mirror_of_the_tree(root.left)

    return created_node


def print_at_given_height(root,height):
    if(root==None):
        return None
    if(height==0):
        print(root.data)
    else:
        print_at_given_height(root.left,height-1)
        print_at_given_height(root.right,height-1)



def left_view(root):
    if(root==None):
        return
    queue=[]
    queue.append(root)
    queue.append(None)
    print(queue)
    while(len(queue)):
        curr=queue[0]

        if(curr):
            print(curr.data,end="")

            while(queue[0]!=None):
                curr=queue[0]
                if(curr.left!=None):
                    queue.append(curr.left)
                if(curr.right!=None):
                    queue.append(curr.right)    
                queue.pop(0)
           
            queue.append(None)

        queue.pop()    




            


def right_view(root):
    if(root==None):
        return None
    print(root.data)
    return right_view(root.right)



if __name__== "__main__" :

    root = Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(7)
    root.left.right=Node(9)
    root.right.left=Node(8)
    root.right.right=Node(11)
    #level_order_traversal(root)
    #reverse_level_order_traversal(root)
    #print(height_of_the_tree(root))
    #print(diameter_of_tree(root))
    print("-------------------------")
    #curr=mirror_of_the_tree(root)
    #level_order_traversal(curr)
    left_view(root)
    