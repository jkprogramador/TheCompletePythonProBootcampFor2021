import pandas


class MapData:
    def __init__(self):
        self.__data = pandas.read_csv("50_states.csv")
        self.__states = self.__data.state.to_list()

    def get_count(self) -> int:
        return len(self.__states)

    def get_states(self) -> list:
        return self.__states

    def get_coordinates(self, state: str) -> tuple:
        row = self.__data[self.__data.state == state]

        if len(row):
            return int(row.x), int(row.y)

        return None
