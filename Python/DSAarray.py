class Array1:

    def __init__(self , size):
        assert size > 0
        self._size = size
        pyarray = ctypes.py_object * size
        self._element = pyarray()
        self.clear(None)
       
    def __len__(self):
        return(self._size)
   
    def __getitem__(self,index):
        assert index >= 0 and index < len(self)
        return self._element [index]
   
    def __setitem__(self,index, value):
        assert index >= 0 and index < len(self)
        self._element [index] = value
       
    def clear(self,value):
        for i in range(len(self)):
            self._element[i] = value
           
    def __iter__(self):
        return _ArrayIterator(self._element)
   
class _ArrayIterator:
   
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0
       
    def __iter1__(self):
        return(self)
   
    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIterartion
size = 10          
ob1 = Array1(size)
ob1.__len__()
ob1.__setitem__(1,'Saad')
ob1.__getitem__(1)
# ob1.__setitem__(2,'Ali')
# ob1.__getitem__(2)
# ob1.clear(1)
print(ob1.__iter__().__iter__())
print(ob1.__iter__().__next__())
