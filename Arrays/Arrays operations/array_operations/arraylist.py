class ArrayList:
    def __init__(self):
        self.size = 1  
        self.count = 0 
        self.array = self.create_array(self.size)
        
    def create_array(self, size):
     
        return [None] * size

    def resize(self):
      
        new_size = self.size * 2
        new_array = self.create_array(new_size)
        
        
        for i in range(self.size):
            new_array[i] = self.array[i]
            
        self.array = new_array
        self.size = new_size

    def add(self, element):

        if self.count == self.size:
            self.resize()
        
        self.array[self.count] = element
        self.count += 1

    def get(self, index):
       
        if 0 <= index < self.count:
            return self.array[index]
        else:
            raise IndexError('Index out of bounds')
        
    def __str__(self):
        elements = []
        for i in range(self.count):
            elements.append(self.array[i])
        return str(elements)
     
 

array_list = ArrayList()
array_list.add(1)
array_list.add(2)
array_list.add(3)
array_list.add(4)

print(array_list)  
array_list.add(5)  
print(array_list) 