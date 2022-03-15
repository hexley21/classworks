class Book:
    def __init__(self, name, author, release, pages):
        self.name = name
        self._author = author
        self.__release = release
        self.__pages = pages

    def info(self):
        print(f"Name: {self.name}\nAuthor: {self._author}\nRelease: {self.__release}\nPages: {self.__pages}")

vefxistyaosani = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 172, 386)
thomas_calculus = Book("Thomas Calculus", "George B. Thomas", 1951, 1224)
clean_code = Book("Clean code", "Robert C. Martin", 2008, 464)

vefxistyaosani.info(); print()
thomas_calculus.info(); print()
clean_code.info()