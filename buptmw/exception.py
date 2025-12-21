class RequireCASInstance(Exception):
    def __init__(self):
        self.message = "Require CAS instance."
        super().__init__(self.message)

class RequireCASCredential(Exception):
    def __init__(self):
        self.message = "Require CAS credential."
        super().__init__(self.message)
