import magazine.utils as u


class Order:
    def __init__(self, id):
        self.id = id
        u.info(f"Order: {id}")
