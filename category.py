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
