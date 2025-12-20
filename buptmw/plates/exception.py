class RequireCAS(Exception):
    def __init__(self):
        self.message = "Require CAS instance."
        super().__init__(self.message)
