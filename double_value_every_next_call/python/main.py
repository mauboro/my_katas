class Class:
    @staticmethod
    def get_number():
        if not hasattr(Class, "value"):
            Class.value = 1
        else:
            Class.value *= 2
        return Class.value
