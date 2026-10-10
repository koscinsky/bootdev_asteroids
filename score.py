import constants


def gameover_get_score():
    print(f"Game Over! Your score: {constants.SCORE_INGAME}")


def get_score():
    return constants.SCORE_INGAME


def update_score():
    constants.SCORE_INGAME += 100
    if constants.SCORE_INGAME % 500 == 0:
        print(f"Your score: {constants.SCORE_INGAME}")
    return constants.SCORE_INGAME


def update_highscore():
    constants.SCORE_HIGHEST = max(constants.SCORE_INGAME, constants.SCORE_HIGHEST)
