from app.utils import game, interface_game


def main():
    """main function, launch the interface and the game"""
    score = {'humain': 0, 'spidey': 0} 
    preview_user = [] 
    preview_ia = []
    game_play = True
    interface_game()
    while game_play:
        game_play = game(score=score, preview_ia=preview_ia, preview_user=preview_user)

    print("\n=============================================")
    print(f"SCORE FINAL : You({score['humain']}) - Spidey({score['spidey']})")
    print("=============================================")

if __name__ == "__main__":
    main()

