# настройки игры

# --- Screen ---

RES = WIDTH, HEIGHT = 600, 400  # 600, 400
FPS = 60  # 60

SCREEN_POS = {
    "topleft": (0, 0),
    "topcenter": (RES[0] / 2, 0),
    "topright": (RES[0], 0)
}

# --- Card ---

CARD_WIDTH = 2  # 2
CARD_HEIGHT = 3  # 3
# scale = 100

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
# scale = 50

# ---

# Игра:
# Включить автопасование
# Задержка перед отображением подсказок

# Видео:
# Полноэкранный режим
# Разрешение

# Аудио:
# Звук: общий, музыка, эффекты


print(SCREEN_POS)
print(SCREEN_POS["topleft"])
print(SCREEN_POS["topcenter"])
print(SCREEN_POS["topright"])
