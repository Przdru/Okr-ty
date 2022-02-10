import string


def if_valid_coordinates_int(coordinates: ()) -> bool:
    x, y = coordinates
    if 0 < x < 11 and 0 < y < 11:
        return True
    else:
        return False


class Player:

    def __init__(self, name):
        self.name = name

        self.x_coordinates_converter = {letter: idx + 1 for idx, letter in enumerate(string.ascii_uppercase)}

        self.player_board = self.make_board()
        self.add_y_coordinates(self.player_board)
        self.add_x_coordinates(self.player_board)

        self.player_shooting_board = self.make_board()
        self.add_x_coordinates(self.player_shooting_board)
        self.add_y_coordinates(self.player_shooting_board)

    @staticmethod
    def make_board() -> list:
        return [[f' ' for _ in range(11)] for __ in range(11)]

    @staticmethod
    def add_x_coordinates(board: list) -> None:
        for column in range(0, len(board[0])):
            if column > 0:
                board[0][column] = string.ascii_uppercase[column - 1]
            else:
                board[0][column] = " X"

    @staticmethod
    def add_y_coordinates(board: list) -> None:
        for row in range(1, len(board[0])):
            if row < 10:
                board[row][0] = f" {row}"
            else:
                board[row][0] = f"{row}"

    def print_board(self) -> None:

        print(" " * (len(self.player_board[0]) * 2 + (10 - len(self.name))), self.name)
        print(" " * (len(self.player_board[0]) // 2), "Statki gracza", " " * (len(self.player_board[0]) * 2 - 4),
              "Pole strzelań")

        for row in range(len(self.player_board[0])):

            for column in self.player_board[row]:
                print(column, sep='|', end='|', flush=True)

            print(" " * 10, sep='', end='', flush=True)

            for column in self.player_shooting_board[row]:
                print(column, sep='|', end='|', flush=True)
            print()

    def conversion(self, coordinates_of_shoot) -> ():
        y = int(self.x_coordinates_converter.get(coordinates_of_shoot[0]))
        x = int(coordinates_of_shoot[1:])
        return x, y

    def if_valid_coordinates(self, coordinates: str) -> bool:
        if coordinates[0].isalpha() and coordinates[1].isdigit():
            x, y = self.conversion(coordinates)
            if x and y > 0 and x < 11 and y < 11:
                return True
            else:
                return False
        else:
            return False

    def enter_coordinates_of_shoot(self, ):
        pass

    def ship_positioning(self):
        pass


class Human_Player(Player):
    def __init__(self, name: str):
        super().__init__(name)

    def enter_coordinates_of_shoot(self) -> ():
        while True:
            coordinates_of_shoot = input("Wproawdż współrzędne celu do ostrzału (np.A7)").replace(" ", "").upper()
            try:
                if self.if_valid_coordinates(coordinates_of_shoot):
                    return self.conversion(coordinates_of_shoot)
                else:
                    raise ValueError

            except ValueError:
                print("Wprowadziłeś niepoprawne dane.")

    def ship_positioning(self):

        ships = [(1, 4), (2, 3), (3, 2), (4, 1)]
        end_loop = False

        for ships_number, ship_size in ships:
            counter = 0

            for i in range(ships_number):
                print(f"Liczba {ship_size} masztowych statków do ustawienia: {ships_number - counter}")
                end_loop = False
                while not end_loop:
                    self.print_board()
                    try:
                        direction = input("Wprowadż w którą storne ma zostać skierowany statek od punktu centralnego (W-> w górę, S -> w dół, D -> w prawo, A -> w lewo)").replace(" ", "").upper()
                        if not direction[0].isalpha() or (direction != 'A' and direction != 'S' and direction != 'D' and direction != 'W'):
                            raise ValueError

                        c_point = input("Podaj pozycje statku").replace(" ", "").upper()
                        if self.if_valid_coordinates(c_point):
                            c_point = self.conversion(c_point)
                            e_point = [0,0]
                        else:
                            raise ValueError

                        if direction == 'A':
                            e_point[0] = c_point[0]
                            e_point[1] = c_point[1] - ship_size + 1
                            if if_valid_coordinates_int(c_point) and if_valid_coordinates_int(e_point):
                                if any([field == "#" for field in self.player_board[c_point[0]][c_point[1] - ship_size + 1 : c_point[1] + 1]]):
                                    print("Pozycja statków nachodzi na siebie")
                                    raise ValueError
                                else:
                                    for step in range(ship_size):
                                        self.player_board[c_point[0]][c_point[1] - step] = '#'
                                    end_loop = True
                            else:
                                raise ValueError

                        if direction == 'D':
                            e_point[0] = c_point[0]
                            e_point[1] = c_point[1] + ship_size - 1
                            if if_valid_coordinates_int(c_point) and if_valid_coordinates_int(e_point):
                                if any(field == "#" for field in self.player_board[c_point[0]][c_point[1] : c_point[1] + ship_size]):
                                    print("Pozycja statków nachodzi na siebie")
                                    raise ValueError
                                else:
                                    for step in range(ship_size):
                                        self.player_board[c_point[0]][c_point[1] + step] = '#'
                                    end_loop = True
                            else:
                                raise ValueError

                        if direction == 'W':
                            e_point[0] = c_point[0] - ship_size + 1
                            e_point[1] = c_point[1]
                            if if_valid_coordinates_int(c_point) and if_valid_coordinates_int(e_point):

                                if any(row[c_point[1]] == "#" for row in self.player_board[ (c_point[0] - ship_size + 1) : c_point[0]]):
                                    print("Pozycja statków nachodzi na siebie")
                                    raise ValueError
                                else:
                                    print(self.player_board[c_point[0]][c_point[1]])
                                    for step in range(ship_size):

                                        self.player_board[c_point[0] - step][c_point[1]] = '#'
                                    end_loop = True
                            else:
                                raise ValueError

                        if direction == 'S':
                            e_point[0] = c_point[0] + ship_size - 1
                            e_point[1] = c_point[1]
                            if if_valid_coordinates_int(c_point) and if_valid_coordinates_int(e_point):
                                if any(row[c_point[1]] == "#" for row in self.player_board[c_point[0] : c_point[0] + ship_size + 1]):
                                    print("Pozycja statków nachodzi na siebie")
                                    raise ValueError
                                else:
                                    for step in range(ship_size):
                                        self.player_board[c_point[0] + step][c_point[1]] = '#'
                                    end_loop = True

                            else:
                                raise ValueError
                    except ValueError:
                        print("Wprowadzone dane są nie poprawne !")
