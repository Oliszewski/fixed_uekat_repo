import magazine.utils as u


class Product:
    def __init__(self, name):
        self.name = name
        u.info(f"Product: {name}")
