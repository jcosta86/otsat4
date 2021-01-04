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

