# tee ratkaisu tänne
def pelaa_siirto(game_board: list, x: int, y: int, piece: str):
    if (x < 0 or x > 2) or (y < 0 or y > 2):
        return False 

    for row in range(3):
        for column in range(3): 
            if game_board[y][x] == "":
                game_board[y][x] = piece
                return True
    return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(game_board, 2, 0, "X"))
    print(game_board)