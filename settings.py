# --- Screen ---

RES = WIDTH, HEIGHT = 600, 400  # 1920, 1080  1366, 768  900, 500 || # 600, 400
FPS = 60  # 60

BASE_RES = (1920, 1080)

SCREEN_POS = {
    "tl": (0, 0),  # Top Left
    "t1": (WIDTH // 8, 0),  # Top 1/8
    "t2": (2 * WIDTH // 8, 0),  # Top 2/8
    "t3": (3 * WIDTH // 8, 0),  # Top 3/8
    "t4": (4 * WIDTH // 8, 0),  # Top 4/8
    "t5": (5 * WIDTH // 8, 0),  # Top 5/8
    "t6": (6 * WIDTH // 8, 0),  # Top 6/8
    "t7": (7 * WIDTH // 8, 0),  # Top 7/8
    "tr": (WIDTH, 0),  # Top Right

    "l1": (0, HEIGHT // 8),  # Left 1/8
    "c1": (WIDTH // 8, HEIGHT // 8),  # Center 1/8
    "c2": (2 * WIDTH // 8, HEIGHT // 8),  # Center 2/8
    "c3": (3 * WIDTH // 8, HEIGHT // 8),  # Center 3/8
    "c4": (4 * WIDTH // 8, HEIGHT // 8),  # Center 4/8
    "c5": (5 * WIDTH // 8, HEIGHT // 8),  # Center 5/8
    "c6": (6 * WIDTH // 8, HEIGHT // 8),  # Center 6/8
    "c7": (7 * WIDTH // 8, HEIGHT // 8),  # Center 7/8
    "r1": (WIDTH, HEIGHT // 8),  # Right 1/8

    "l2": (0, 2 * HEIGHT // 8),  # Left 2/8
    "c8": (WIDTH // 8, 2 * HEIGHT // 8),  # Center 8/8
    "c9": (2 * WIDTH // 8, 2 * HEIGHT // 8),  # Center 9/8
    "c10": (3 * WIDTH // 8, 2 * HEIGHT // 8),  # Center 10/8
    "c11": (4 * WIDTH // 8, 2 * HEIGHT // 8),  # Center 11/8
    "c12": (5 * WIDTH // 8, 2 * HEIGHT // 8),  # Center 12/8
    "c13": (6 * WIDTH // 8, 2 * HEIGHT // 8),  # Center 13/8
    "r2": (7 * WIDTH // 8, 2 * HEIGHT // 8),  # Right 2/8
    "r3": (WIDTH, 2 * HEIGHT // 8),  # Right 3/8

    "l3": (0, 3 * HEIGHT // 8),  # Left 3/8
    "c14": (WIDTH // 8, 3 * HEIGHT // 8),  # Center 14/8
    "c15": (2 * WIDTH // 8, 3 * HEIGHT // 8),  # Center 15/8
    "c16": (3 * WIDTH // 8, 3 * HEIGHT // 8),  # Center 16/8
    "c17": (4 * WIDTH // 8, 3 * HEIGHT // 8),  # Center 17/8
    "c18": (5 * WIDTH // 8, 3 * HEIGHT // 8),  # Center 18/8
    "c19": (6 * WIDTH // 8, 3 * HEIGHT // 8),  # Center 19/8
    "r4": (7 * WIDTH // 8, 3 * HEIGHT // 8),  # Right 4/8
    "r5": (WIDTH, 3 * HEIGHT // 8),  # Right 5/8

    "l4": (0, 4 * HEIGHT // 8),  # Left 4/8
    "c20": (WIDTH // 8, 4 * HEIGHT // 8),  # Center 20/8
    "c21": (2 * WIDTH // 8, 4 * HEIGHT // 8),  # Center 21/8
    "c22": (3 * WIDTH // 8, 4 * HEIGHT // 8),  # Center 22/8
    "c": (4 * WIDTH // 8, 4 * HEIGHT // 8),  # Center
    "c24": (5 * WIDTH // 8, 4 * HEIGHT // 8),  # Center 24/8
    "c25": (6 * WIDTH // 8, 4 * HEIGHT // 8),  # Center 25/8
    "r6": (7 * WIDTH // 8, 4 * HEIGHT // 8),  # Right 6/8
    "r7": (WIDTH, 4 * HEIGHT // 8),  # Right 7/8

    "l5": (0, 5 * HEIGHT // 8),  # Left 5/8
    "c26": (WIDTH // 8, 5 * HEIGHT // 8),  # Center 26/8
    "c27": (2 * WIDTH // 8, 5 * HEIGHT // 8),  # Center 27/8
    "c28": (3 * WIDTH // 8, 5 * HEIGHT // 8),  # Center 28/8
    "c29": (4 * WIDTH // 8, 5 * HEIGHT // 8),  # Center 29/8
    "c30": (5 * WIDTH // 8, 5 * HEIGHT // 8),  # Center 30/8
    "c31": (6 * WIDTH // 8, 5 * HEIGHT // 8),  # Center 31/8
    "r8": (7 * WIDTH // 8, 5 * HEIGHT // 8),  # Right 8/8
    "r9": (WIDTH, 5 * HEIGHT // 8),  # Right 9/8

    "l6": (0, 6 * HEIGHT // 8),  # Left 6/8
    "c32": (WIDTH // 8, 6 * HEIGHT // 8),  # Center 32/8
    "c33": (2 * WIDTH // 8, 6 * HEIGHT // 8),  # Center 33/8
    "c34": (3 * WIDTH // 8, 6 * HEIGHT // 8),  # Center 34/8
    "c35": (4 * WIDTH // 8, 6 * HEIGHT // 8),  # Center 35/8
    "c36": (5 * WIDTH // 8, 6 * HEIGHT // 8),  # Center 36/8
    "c37": (6 * WIDTH // 8, 6 * HEIGHT // 8),  # Center 37/8
    "r10": (7 * WIDTH // 8, 6 * HEIGHT // 8),  # Right 10/8
    "r11": (WIDTH, 6 * HEIGHT // 8),  # Right 11/8

    "l7": (0, 7 * HEIGHT // 8),  # Left 7/8
    "c38": (WIDTH // 8, 7 * HEIGHT // 8),  # Center 38/8
    "c39": (2 * WIDTH // 8, 7 * HEIGHT // 8),  # Center 39/8
    "c40": (3 * WIDTH // 8, 7 * HEIGHT // 8),  # Center 40/8
    "c41": (4 * WIDTH // 8, 7 * HEIGHT // 8),  # Center 41/8
    "c42": (5 * WIDTH // 8, 7 * HEIGHT // 8),  # Center 42/8
    "c43": (6 * WIDTH // 8, 7 * HEIGHT // 8),  # Center 43/8
    "r12": (7 * WIDTH // 8, 7 * HEIGHT // 8),  # Right 12/8
    "r13": (WIDTH, 7 * HEIGHT // 8),  # Right 13/8

    "bl": (0, HEIGHT),  # Bottom Left
    "b1": (WIDTH // 8, HEIGHT),  # Bottom 1/8
    "b2": (2 * WIDTH // 8, HEIGHT),  # Bottom 2/8
    "b3": (3 * WIDTH // 8, HEIGHT),  # Bottom 3/8
    "b4": (4 * WIDTH // 8, HEIGHT),  # Bottom 4/8
    "b5": (5 * WIDTH // 8, HEIGHT),  # Bottom 5/8
    "b6": (6 * WIDTH // 8, HEIGHT),  # Bottom 6/8
    "b7": (7 * WIDTH // 8, HEIGHT),  # Bottom 7/8
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
