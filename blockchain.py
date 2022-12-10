import hashlib







class block:
    blockno = 0
    def __init__(self,previous_hash,blockNo,data):
        self.previous_hash = previous_hash
        self.blockno = blockNo
        self.data = data
        self.hash = hashlib.sha256((str(previous_hash)+str(blockNo)+str(data)).encode()).hexdigest()
        
        
    def __str__(self):
        
        return "data "+ self.data + "\nhash "+ str(self.hash) + "\nprevious hash "+ str(self.previous_hash) 
        
    
       
       
        
block1 = block(0,1,"hello world")
block2 = block(block1.hash,2,"srinidhi")
block3 = block(block2.hash,3,"niranjan")
print(block1,block2,block3)




