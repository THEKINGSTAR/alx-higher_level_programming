class LockedClass:
    __slots__ = ('first_name',)

    def __setattr__(self, key, value):
        if hasattr(self, key) or key != 'first_name':
            raise AttributeError\
                    ("'{}' object has no attribute '{}'".format(__class__.__name__ ,key))
        else:
            super().__setattr__(key, value)
