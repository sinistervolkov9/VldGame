# --- Screen ---

RES = WIDTH, HEIGHT = 600, 400  # 1920, 1080  1366, 768  900, 500 || # 600, 400
FPS = 60  # 60

BASE_RES = (1920, 1080)

SCREEN_POS = {
    "tl": (0, 0),  # Top Left
    "t01": (WIDTH // 8, 0),  # Top 1/8
    "t02": (2 * WIDTH // 8, 0),  # Top 2/8
    "t03": (3 * WIDTH // 8, 0),  # Top 3/8
    "t04": (4 * WIDTH // 8, 0),  # Top 4/8
    "t05": (5 * WIDTH // 8, 0),  # Top 5/8
    "t06": (6 * WIDTH // 8, 0),  # Top 6/8
    "t07": (7 * WIDTH // 8, 0),  # Top 7/8
    "tr": (WIDTH, 0),  # Top Right

    "tl1": (0, HEIGHT // 8),  # Left 1/8
    "t11": (WIDTH // 8, HEIGHT // 8),  # Center 1/8
    "t12": (2 * WIDTH // 8, HEIGHT // 8),  # Center 2/8
    "t13": (3 * WIDTH // 8, HEIGHT // 8),  # Center 3/8
    "t14": (4 * WIDTH // 8, HEIGHT // 8),  # Center 4/8
    "t15": (5 * WIDTH // 8, HEIGHT // 8),  # Center 5/8
    "t16": (6 * WIDTH // 8, HEIGHT // 8),  # Center 6/8
    "t17": (7 * WIDTH // 8, HEIGHT // 8),  # Center 7/8
    "tr1": (WIDTH, HEIGHT // 8),  # Right 1/8

    "tl2": (0, 2 * HEIGHT // 8),  # Left 2/8
    "t21": (WIDTH // 8, 2 * HEIGHT // 8),  # Center 8/8
    "t22": (2 * WIDTH // 8, 2 * HEIGHT // 8),  # Center 9/8
    "t23": (3 * WIDTH // 8, 2 * HEIGHT // 8),  # Center 10/8
    "t24": (4 * WIDTH // 8, 2 * HEIGHT // 8),  # Center 11/8
    "t25": (5 * WIDTH // 8, 2 * HEIGHT // 8),  # Center 12/8
    "t26": (6 * WIDTH // 8, 2 * HEIGHT // 8),  # Center 13/8
    "t27": (7 * WIDTH // 8, 2 * HEIGHT // 8),  # Right 2/8
    "tr2": (WIDTH, 2 * HEIGHT // 8),  # Right 3/8

    "tl3": (0, 3 * HEIGHT // 8),  # Left 3/8
    "t31": (WIDTH // 8, 3 * HEIGHT // 8),  # Center 14/8
    "t32": (2 * WIDTH // 8, 3 * HEIGHT // 8),  # Center 15/8
    "t33": (3 * WIDTH // 8, 3 * HEIGHT // 8),  # Center 16/8
    "t34": (4 * WIDTH // 8, 3 * HEIGHT // 8),  # Center 17/8
    "t35": (5 * WIDTH // 8, 3 * HEIGHT // 8),  # Center 18/8
    "t36": (6 * WIDTH // 8, 3 * HEIGHT // 8),  # Center 19/8
    "t37": (7 * WIDTH // 8, 3 * HEIGHT // 8),  # Right 4/8
    "tr3": (WIDTH, 3 * HEIGHT // 8),  # Right 5/8

    "cl": (0, 4 * HEIGHT // 8),  # Left 4/8
    "cl1": (WIDTH // 8, 4 * HEIGHT // 8),  # Center 20/8
    "cl2": (2 * WIDTH // 8, 4 * HEIGHT // 8),  # Center 21/8
    "cl3": (3 * WIDTH // 8, 4 * HEIGHT // 8),  # Center 22/8
    "c": (4 * WIDTH // 8, 4 * HEIGHT // 8),  # Center
    "cr3": (5 * WIDTH // 8, 4 * HEIGHT // 8),  # Center 24/8
    "cr2": (6 * WIDTH // 8, 4 * HEIGHT // 8),  # Center 25/8
    "cr1": (7 * WIDTH // 8, 4 * HEIGHT // 8),  # Right 6/8
    "cr": (WIDTH, 4 * HEIGHT // 8),  # Right 7/8

    "bl3": (0, 5 * HEIGHT // 8),  # Left 5/8
    "b37": (WIDTH // 8, 5 * HEIGHT // 8),  # Center 26/8
    "b36": (2 * WIDTH // 8, 5 * HEIGHT // 8),  # Center 27/8
    "b35": (3 * WIDTH // 8, 5 * HEIGHT // 8),  # Center 28/8
    "b34": (4 * WIDTH // 8, 5 * HEIGHT // 8),  # Center 29/8
    "b33": (5 * WIDTH // 8, 5 * HEIGHT // 8),  # Center 30/8
    "b32": (6 * WIDTH // 8, 5 * HEIGHT // 8),  # Center 31/8
    "b31": (7 * WIDTH // 8, 5 * HEIGHT // 8),  # Right 8/8
    "br3": (WIDTH, 5 * HEIGHT // 8),  # Right 9/8

    "bl2": (0, 6 * HEIGHT // 8),  # Left 6/8
    "b27": (WIDTH // 8, 6 * HEIGHT // 8),  # Center 32/8
    "b26": (2 * WIDTH // 8, 6 * HEIGHT // 8),  # Center 33/8
    "b25": (3 * WIDTH // 8, 6 * HEIGHT // 8),  # Center 34/8
    "b24": (4 * WIDTH // 8, 6 * HEIGHT // 8),  # Center 35/8
    "b23": (5 * WIDTH // 8, 6 * HEIGHT // 8),  # Center 36/8
    "b22": (6 * WIDTH // 8, 6 * HEIGHT // 8),  # Center 37/8
    "b21": (7 * WIDTH // 8, 6 * HEIGHT // 8),  # Right 10/8
    "br2": (WIDTH, 6 * HEIGHT // 8),  # Right 11/8

    "bl1": (0, 7 * HEIGHT // 8),  # Left 7/8
    "b17": (WIDTH // 8, 7 * HEIGHT // 8),  # Center 38/8
    "b16": (2 * WIDTH // 8, 7 * HEIGHT // 8),  # Center 39/8
    "b15": (3 * WIDTH // 8, 7 * HEIGHT // 8),  # Center 40/8
    "b14": (4 * WIDTH // 8, 7 * HEIGHT // 8),  # Center 41/8
    "b13": (5 * WIDTH // 8, 7 * HEIGHT // 8),  # Center 42/8
    "b12": (6 * WIDTH // 8, 7 * HEIGHT // 8),  # Center 43/8
    "b11": (7 * WIDTH // 8, 7 * HEIGHT // 8),  # Right 12/8
    "br1": (WIDTH, 7 * HEIGHT // 8),  # Right 13/8

    "bl": (0, HEIGHT),  # Bottom Left
    "b07": (WIDTH // 8, HEIGHT),  # Bottom 1/8
    "b06": (2 * WIDTH // 8, HEIGHT),  # Bottom 2/8
    "b05": (3 * WIDTH // 8, HEIGHT),  # Bottom 3/8
    "b04": (4 * WIDTH // 8, HEIGHT),  # Bottom 4/8
    "b03": (5 * WIDTH // 8, HEIGHT),  # Bottom 5/8
    "b02": (6 * WIDTH // 8, HEIGHT),  # Bottom 6/8
    "b01": (7 * WIDTH // 8, HEIGHT),  # Bottom 7/8
    "br": (WIDTH, HEIGHT),  # Bottom Right
}

# --- Card ---

CARD_WIDTH = 2  # 2
CARD_HEIGHT = 3  # 3

BASE_CARD_SCALE = 110  # 1920 x 1080
CARD_SCALE_COEF = 0.1  # 0.27
CARD_SCALE = BASE_CARD_SCALE * ((RES[0] * RES[1]) / (BASE_RES[0] * BASE_RES[1])) ** CARD_SCALE_COEF  # 1920 x 1080, 110

FRAME_WIDTH = 20  # 20, px  # NEED RENAME!!!

# --- Player ---

BASE_HP = 100  # 100 - стартовое значение Здоровья
HEALTH_COEFFICIENT = 30  # 30 - сколько ХП прибавляется за каждую единицу strength
HEALTH_DECREASE_FACTOR = 0.2  # 0.2 - во сколько будет уменьшаться HEALTH_COEFFICIENT за единицу strength

BASE_SPEED = 10  # 10 - стартовое начение Скорости
SPEED_COEFFICIENT = 10  # 10 - сколько Скорости прибавляется за каждую единицу dexterity
SPEED_DECREASE_FACTOR = 0.8  # 0.8 - во сколько будет уменьшаться SPEED_COEFFICIENT за единицу dexterity

# --- Button ---

BUTTON_WIDTH = 2
BUTTON_HEIGHT = BUTTON_WIDTH / 2

BASE_BUTTON_SCALE = 100  # 1920 x 1080
BUTTON_SCALE_COEF = 0.2  # 0.2
BUTTON_SCALE = BASE_BUTTON_SCALE * ((RES[0] * RES[1]) / (BASE_RES[0] * BASE_RES[1])) ** BUTTON_SCALE_COEF
# 1920 x 1080, 100

# ---

# Игра:
# Включить автопасование
# Задержка перед отображением подсказок

# Видео:
# Полноэкранный режим
# Разрешение

# Аудио:
# Звук: общий, музыка, эффекты


# print(SCREEN_POS)
# print(SCREEN_POS["topleft"])
# print(SCREEN_POS["topcenter"])
# print(SCREEN_POS["topright"])
