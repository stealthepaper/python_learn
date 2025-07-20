class File:
    def __init__(self, size):
        self._size_in_bytes = size

    def convert_size(self):
        # match self._size_in_bytes:
        #     case < 1024:
        #         print(f"{self._size_in_bytes} B")
        #     case < 1024*2:
        if self._size_in_bytes < 1024:
            return f"{self._size_in_bytes} B"
        elif self._size_in_bytes < 1024**2:
            return f"{self._size_in_bytes/1024:.2f} KB"
        elif self._size_in_bytes < 1024**3:
            return f"{self._size_in_bytes/1024**2:.2f} MB"
        elif self._size_in_bytes < 1024**4:
            return f"{self._size_in_bytes/1024**3:.2f} GB"
        

file = File(5)
print(file.convert_size())