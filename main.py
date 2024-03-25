from src.interface import run_gui
from src.game import run_game
COMP_CAMERA = 0


if __name__ == '__main__':
    # config = run_gui()
    config ={'trials': 4, 'max_time': '30.00', 'side': 'RIGHT', 'alpha': 2.1}
    run_game(config, COMP_CAMERA)
