class BinaryTree:
  def __init__(self, rootElement):
    self.key = rootElement
    self.left = None
    self.right = None

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def getRootVal(self):
    return self.key

  def setRootVal(self,val):
    self.key=val
  
  def insertLeft(self,newNode):
    if self.left == None:
      self.left = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.left = self.left
      self.left = t
  
  def insertRight(self,newNode):
    if self.right == None:
      self.right = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.right = self.right
      self.right = t

  def contains(self, anObject):
    if self.key == anObject:
      return True
    elif self.getLeft() == None:
      if self.getRight() == None:
        return False
      else:
        return self.getRight().contains(anObject)
    elif self.getRight() == None:
      return self.getLeft().contains(anObject)
    else:
      leftResponse = self.getLeft().contains(anObject)
      rightResponse = self.getRight().contains(anObject)
      if leftResponse or rightResponse:
        return True
      else:
        return False
      
  def add(self, anObject):
    if self == None:
      self = BinaryTree(anObject)
    elif self.left == None:
      self.left = BinaryTree(anObject)
    elif self.right == None:
      self.right = BinaryTree(anObject)
    else:
      self.getLeft().add(anObject)
      
  def remove(self, anObject, rightMostParent=None, rightMost=None):
    #check if it's in this subtree
    verification = self.contains(anObject)
    if not verification:
      return "%s Not in tree" % str(anObject)
      
    #find the right most node
    if rightMostParent==None:
      previous = None
      current = self
      flag = True
      while flag:
        #loop while you don't have a leaf node 
        while current.getRight()!=None:
          previous = current
          current = current.getRight()
        if current.getLeft()!=None:
          previous = current
          current = current.getLeft()
        else:
          rightMost = current
          rightMostParent = previous
          flag = False
      #If the right most leaf is the one to be deleted then simply find its previous and set it to none
      if rightMost.key == anObject:
        if rightMostParent.getRight() == rightMost:
          rightMostParent.right = None
        else:
          rightMostParent.left = None
        
    #Now that rightmost node is found we have to locate our object (same method as contains:
    #check the key, if its not equal check left and right subtrees
    #we carry the rightmost node with us, copy the key over and then use the parent of rightMostParent 
    
    if self.key == anObject:
      self.key = rightMost.key
      if rightMostParent.getRight() == rightMost:
        rightMostParent.right = None
      else:
        rightMostParent.left = None
    else:
      if self.getRight()!=None:
        self.getRight().remove(anObject, rightMostParent, rightMost)
      if self.getLeft()!=None:
        self.getLeft().remove(anObject, rightMostParent, rightMost)
      
      
def preorder(tree):
  if tree != None:
    print(tree.getRootVal(), end=' ')
    preorder(tree.getLeft())
    preorder(tree.getRight())


def inorder(tree):
  if tree != None:
    inorder(tree.getLeft())
    print(tree.getRootVal(), end=' ')
    inorder(tree.getRight())


def postorder(tree):
  if tree != None:
    postorder(tree.getLeft())
    postorder(tree.getRight())
    print(tree.getRootVal(), end=' ')


def findMinValue(tree):
  minValue = None
  if tree!=None:
    l = findMinValue(tree.left)
    r = findMinValue(tree.right)
    m = tree.key
    if l != None and r != None:
      minValue = min(l,r,m)
    elif l!=None:
      minValue = min(l,m)
    elif r!=None:
      minValue = min(r,m)
    else:
      minValue = m
  return minValue


def findMaxValue(tree):
  maxValue = None
  minValue = None
  if tree!=None:
    l = findMaxValue(tree.left)
    r = findMaxValue(tree.right)
    m = tree.key
    if l != None and r != None:
      maxValue = max(l,r,m)
    elif l!=None:
      maxValue = max(l,m)
    elif r!=None:
      maxValue = max(r,m)
    else:
      maxValue = m

  return maxValue


def main():
  tree = BinaryTree(1)
  tree.insertLeft(2)
  tree.insertRight(7)
  tree.getLeft().insertLeft(3)
  tree.getLeft().insertRight(6)
  tree.getLeft().getLeft().insertLeft(4)
  tree.getLeft().getLeft().insertRight(5)
  tree.getRight().insertLeft(8)
  tree.getRight().insertRight(9)

  preorder(tree)
  print()
  inorder(tree)
  print()
  postorder(tree)
  print()

  print('Max value in tree:', findMaxValue(tree))
  print('Min value in tree:', findMinValue(tree))
  print(tree.contains(3))
  print(tree.contains(15))
  tree.add(15)
  preorder(tree)
  print()
  tree.remove(1)
  preorder(tree)
  print()
  tree.remove(15)
  preorder(tree)
  print()  

if __name__ == "__main__":
  main()