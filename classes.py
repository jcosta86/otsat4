class Marketplace:
    __name: str
    __categories: list = []

    def __init__(self, name: str, categories: list):
        self.__name = name

        for category in categories:
            self.set_category(category)

    def set_category(self, category) -> None:
        self.__categories.append(category)

    def set_name(self, name) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_categories(self) -> list:
        return self.__categories

    def __str__(self):
        return f"""
                {self.get_name()}
                Categorias: {self.get_categories()}
                """


class Category:
    __category_name: str
    __subcategories: list = []

    def __init__(self, name: str, subcategories: list):
        self.__category_name = name

        for subcategory in subcategories:
            self.set_subcategory(subcategory)

    def set_subcategory(self, subcategory) -> None:
        self.__subcategories.append(subcategory)

    def set_name(self, name) -> None:
        self.__category_name = name

    def get_name(self) -> str:
        return self.__category_name

    def get_subcategories(self) -> list:
        return self.__subcategories

    def __str__(self):
        return f"""
                {self.get_name()}
                Subcategorias: {self.get_subcategories()}
                """


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
