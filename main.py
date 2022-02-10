from Game_classes import Human_Player


class Game_mechanic:
    """ The class stores methods that operate on objects of Player classes.  """

    @staticmethod
    def shot(player_1, player_2, g_round) -> None:
        """Method check if shot was successful, and mark them on players boards"""
        if g_round == 1:
            x, y = player_1.enter_coordinates_of_shoot()
            if player_2.player_board[x][y] == r"#":
                player_1.player_shooting_board[x][y] = "X"
                player_2.player_board [x][y] = "X"
            else:
                player_1.player_shooting_board[x][y] = "O"
                player_2.player_board[x][y] = "O"
        else:
            x, y = player_2.enter_coordinates_of_shoot()
            if player_1.player_board[x][y] == r"#":
                player_2.player_shooting_board[x][y] = "X"
                player_1.player_board[x][y] = "X"
            else:
                player_2.player_shooting_board[x][y] = "O"
                player_1.player_board[x][y] = "O"

    @staticmethod
    def wining_conditions(player):
        """Method checks the condition of victory."""
        if any(row[w] == "#" for row in player.player_board[:] for w in range(11)):
            return False
        else:
            return True


def play(game_object, player_1, player_2):

    player_1.ship_positioning()
    player_2.ship_positioning()

    while True:
        player_1.print_board()
        game_object.shot(player_1, player_2, 1)
        player_1.print_board()

        if game_object.wining_conditions(player_2):
            print(f"Gracz {player_1.name} wygrał rozgrywkę")
            break

        player_2.print_board()
        game_object.shot(player_1, player_2, 2)
        player_2.print_board()

        if game_object.wining_conditions(player1):
            print(f"Gracz {player_2.name} wygrał rozgrywkę")
            break


game = Game_mechanic

player1 = Human_Player("Player 1")
player2 = Human_Player("Player 2")

play(game, player1, player2)

