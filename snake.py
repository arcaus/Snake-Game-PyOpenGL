import sys
import random
from OpenGL.GL import *
from OpenGL.GLUT import *


# Midpoint Line Algorithm using Find Zone and Convert to Zone zero and convert back to original zone
def find_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    absolute_dy = abs(dy)
    absolute_dx = abs(dx)
    if absolute_dx > absolute_dy:
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 <= dy:
            return 3
        elif dx <= 0 and dy <= 0:
            return 4
        elif dx >= 0 >= dy:
            return 7
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 <= dy:
            return 2
        elif dx <= 0 and dy <= 0:
            return 5
        elif dx >= 0 >= dy:
            return 6


def convert_to_zone_zero(x, y, zone):
    if zone == 0:  # Zone 0 to Zone 0
        return x, y
    elif zone == 1:  # Zone 1 to Zone 0
        return y, x
    elif zone == 2:  # Zone 2 to Zone 0
        return y, -x
    elif zone == 3:  # Zone 3 to Zone 0
        return -x, y
    elif zone == 4:  # Zone 4 to Zone 0
        return -x, -y
    elif zone == 5:  # Zone 5 to Zone 0
        return -y, -x
    elif zone == 6:  # Zone 6 to Zone 0
        return -y, x
    elif zone == 7:  # Zone 7 to Zone 0
        return x, -y


def convert_back(x, y, zone):
    if zone == 0:  # zone 0 to zone 0
        return x, y
    elif zone == 1:  # zone 0 to zone 1
        return y, x  # X0 = y , Y0= x
    elif zone == 2:  # zone 0 to zone 2
        return -y, x
    elif zone == 3:  # zone 0 to zone 3
        return -x, y
    elif zone == 4:  # zone 0 to zone 4
        return -x, -y
    elif zone == 5:  # zone 0 to zone 5
        return -y, -x
    elif zone == 6:  # zone 0 to zone 6
        return y, -x
    elif zone == 7:  # zone 0 to zone 7
        return x, -y


def midpoint_line(x1, y1, x2, y2):
    zone = find_zone(x1, y1, x2, y2)
    x1_new, y1_new = convert_to_zone_zero(x1, y1, zone)
    x2_new, y2_new = convert_to_zone_zero(x2, y2, zone)

    dx = x2_new - x1_new
    dy = y2_new - y1_new
    d = 2 * dy - dx
    ne = 2 * (dy - dx)
    e = 2 * dy

    while x1_new < x2_new:
        x1_new += 1
        if d < 0:
            d += e
        else:
            y1_new += 1
            d += ne
        temp_x, temp_y = convert_back(x1_new, y1_new, zone)
        glVertex2f(temp_x, temp_y)


# Midpoint Circle Algorithm
def midpoint_circle(cx, cy, r):
    x, y, d = 0, r, 1 - r
    while x <= y:
        glVertex2f(cx + x, cy + y)
        glVertex2f(cx - x, cy + y)
        glVertex2f(cx + x, cy - y)
        glVertex2f(cx - x, cy - y)
        glVertex2f(cx + y, cy + x)
        glVertex2f(cx - y, cy + x)
        glVertex2f(cx + y, cy - x)
        glVertex2f(cx - y, cy - x)

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1


# Draw  square
def draw_square(x, y, size):
    half_size = size // 2
    # Draw the square using the midpoint_line function
    # Top edge
    midpoint_line(x - half_size, y + half_size, x + half_size, y + half_size)
    # Bottom edge
    midpoint_line(x - half_size, y - half_size, x + half_size, y - half_size)
    # Left edge
    midpoint_line(x - half_size, y - half_size, x - half_size, y + half_size)
    # Right edge
    midpoint_line(x + half_size, y - half_size, x + half_size, y + half_size)
    # Fill the square
    for i in range(x - half_size, x + half_size):
        midpoint_line(i, y - half_size, i, y + half_size)


# Add Color
def add_color(r, g, b):
    glColor3f(r / 255, g / 255, b / 255)


# Draw text on the screen
def draw_text(text, x, y):
    glPushMatrix()
    glTranslatef(x, y, 0)
    # increase spacing between characters
    glScalef(0.2, 0.2, 0.2)
    for ch in text:
        # Draw each character using the arial font
        glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(ch))

    glPopMatrix()


# Draw game over text on the screen
def draw_game_over(text, x, y):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(0.5, 0.5, 0.5)

    for ch in text[0]:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(ch))

    glPopMatrix()
    glPushMatrix()
    glScalef(0.4, 0.4, 0.4)
    # Move to the next line and draw the score text below the game over text
    glTranslatef(100, 450, 0)
    for ch in text[1]:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(ch))

    glPopMatrix()


# Draw the snake
def draw_snake(snake):
    for segment in snake:
        x, y = segment
        draw_square(x * 10 + 5, y * 10 + 5, 10)
        # midpoint_circle(x * 10 + 5, y * 10 + 5, 6)

# Draw the food


def draw_food(food, food_type):
    x, y = food
    if food_type == "circle":
        midpoint_circle(x * 10 + 5, y * 10 + 5, 6)
    elif food_type == "square":
        draw_square(x * 10 + 5, y * 10 + 5, 10)


# Game state

snake = [(20, 20), (20, 21), (20, 22)]
food = (40, 40)
food_type = random.choice(["circle", "square"])
direction = (1, 0)
score = 0
game_over = False


# OpenGL display function
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    if not game_over:
        # Draw the snake
        add_color(14, 124, 227)
        glBegin(GL_POINTS)
        draw_snake(snake)
        glEnd()

        # Draw the food
        add_color(227, 31, 14)
        glBegin(GL_POINTS)
        draw_food(food, food_type)
        glEnd()

        # Display score
        add_color(149, 14, 227)
        glLineWidth(4)
        draw_text(f"Score: {score}", 5, 470)

    else:
        add_color(227, 14, 14)
        glLineWidth(4)
        gmv = "Your Score: " + str(score)
        draw_game_over(["Game Over!", gmv], 50, 350)
        glutTimerFunc(2000, update, 0)

    glutSwapBuffers()


# Game update function
def update(value):
    global snake, food, food_type, direction, score, game_over

    if not game_over:
        glClearColor(0.720, 0.955, 0.150, 1.0)
        head_x, head_y = snake[-1]
        new_head_x = (head_x + direction[0]) % 50
        new_head_y = (head_y + direction[1]) % 50

        if (new_head_x, new_head_y) in snake:
            game_over = True
            glutPostRedisplay()
            return

        if (new_head_x, new_head_y) == food:
            if food_type == "square":
                score += 30
            else:
                score += 10
            food = (random.randint(0, 49), random.randint(0, 49))
            food_type = random.choice(["circle", "square"])
        else:
            snake.pop(0)

        snake.append((new_head_x, new_head_y))

        glutPostRedisplay()
        glutTimerFunc(150, update, 0)

    else:
        # close the game and exit
        glutDestroyWindow(glutGetWindow())
        sys.exit()


# Keyboard input function
def keyboard(key, x, y):
    global direction
    if key == b"w":
        if direction[1] == 0:
            direction = (0, 1)
    elif key == b"s":
        if direction[1] == 0:
            direction = (0, -1)
    elif key == b"a":
        if direction[0] == 0:
            direction = (-1, 0)
    elif key == b"d":
        if direction[0] == 0:
            direction = (1, 0)


# Arrow keys input function
def arrow_keys(key, x, y):
    global direction
    if key == GLUT_KEY_UP:
        if direction[1] == 0:
            direction = (0, 1)
    elif key == GLUT_KEY_DOWN:
        if direction[1] == 0:
            direction = (0, -1)
    elif key == GLUT_KEY_LEFT:
        if direction[0] == 0:
            direction = (-1, 0)
    elif key == GLUT_KEY_RIGHT:
        if direction[0] == 0:
            direction = (1, 0)


# Initialize and run the game
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(400, 80)
    glutCreateWindow(b"Snake Game")

    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, -1, 1)

    glutDisplayFunc(display)
    glutSpecialFunc(arrow_keys)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(200, update, 0)

    glutMainLoop()

# Run the game
if __name__ == "__main__":
    main()
