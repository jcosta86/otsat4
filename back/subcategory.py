class Subcategory:
    __subcategory_name: str
    __products: list = []

    def __init__(self, name: str, products: list):
        self.__subcategory_name = name

        for p in products:
            self.set_products(p)

    def set_products(self, product) -> None:
        self.__products.append(product)

    def set_name(self, name) -> None:
        self.__subcategory_name = name

    def get_name(self) -> str:
        return self.__subcategory_name

    def get_products(self) -> list:
        return self.__products

    def __str__(self):
        return f"""
                {self.get_name()}
                Produtos: {self.get_products()}
                """