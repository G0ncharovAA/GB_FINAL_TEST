class Counter:
    def __init__(self):
        self.value = 0
        self.is_resource_acquired = False

    def add(self):
        if not self.is_resource_acquired:
            raise Exception('Resource not acquired')
        self.value += 1

    def __enter__(self):
        self.is_resource_acquired = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_resource_acquired = False
        if exc_type is not None:
            return False
        return True
