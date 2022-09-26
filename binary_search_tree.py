# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:04:56 2022

@author: sandh
"""

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self,data):
        if(data):
            if(data<self.data):
                if(self.left is None):
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                    
            elif(data>self.data):
                if(self.right is None):
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                    
        else:
            self.data = data
            
    def findvalue(self,value):
        if value < self.data:
            if(self.left is None):
                return str(value) + " not found"
            return self.left.findvalue(value)
        elif value > self.data:
            if(self.right is None):
                return str(value) + " not found"
            return self.right.findvalue(value)
        else:
            return str(value) + "found"
        
        
        
    def tr(self,value):
        if(value<self.data):
            if self.left is None:
                return str(value) + "is not found"
            return self.elft.findvalue(value)
        elif(value>self.data):
            if self.right is None:
                return str(value) + "is not found"
            return self.right().findvalue(value)
        else:
            return str(value) + " is found"
          
            
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
            
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()
print(root.findvalue(7))
print(root.findvalue(14))



