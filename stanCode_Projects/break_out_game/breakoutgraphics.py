"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10     # Number of rows of bricks.
BRICK_COLS = 10   # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=PADDLE_WIDTH, height=PADDLE_HEIGHT, x=(self.window.width-PADDLE_WIDTH)/2,
                            y=self.window.height-PADDLE_OFFSET)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=BALL_RADIUS*2, height=BALL_RADIUS*2, x=self.window.width/2-BALL_RADIUS,
                          y=self.window.height/2-BALL_RADIUS)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self._dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self._dx = -self._dx
        self._dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmouseclicked(self.start_game)  # discuss with Rita and Ilona
        self.event = False  # if the mouse is clicked then it will be TRUE
        onmousemoved(self.paddle_move)

        # Draw bricks
        set_color = (brick_height+brick_spacing)*brick_rows // 5  # 5 kinds of color for bricks
        for i in range(0, brick_cols*(brick_width+brick_spacing), brick_width+brick_spacing):  # col
            for j in range(brick_offset, brick_rows*(brick_height+brick_spacing)+brick_offset,  # row
                           brick_height+brick_spacing):
                if j >= brick_offset+set_color*4:  # row NO.9-10
                    color = 'blue'
                elif j >= brick_offset+set_color*3:  # row NO.7-8
                    color = 'green'
                elif j >= brick_offset+set_color*2:  # row NO.5-6
                    color = 'yellow'
                elif j >= brick_offset + set_color:  # row NO.3-4
                    color = 'orange'
                else:  # row NO.1-2
                    color = 'red'
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                self.brick.fill_color = color
                self.brick.color = color
                self.window.add(self.brick, x=i, y=j)

        # Number of bricks
        self.num_brick = brick_rows*brick_cols

    # control the position of the paddle
    def paddle_move(self, move):
        if move.x-(self.paddle.width/2) + self.paddle.width > self.window.width:  # the paddle hits the right side of w
            self.paddle.x = self.window.width-self.paddle.width
        elif move.x-(self.paddle.width/2) <= 0:  # the paddle hits the left side of w
            self.paddle.x = 0
        else:
            self.paddle.x = move.x-(self.paddle.width/2)  # the mouse control the paddle by its central

    # identify whether the game is begin
    def start_game(self, m):  # discuss with Rita and Ilona
        self.event = True  # click the mouse means the game start

    # get the result of starting game
    def get_event(self):  # discuss with Rita and Ilona
        return self.event

    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

    # whether the ball hits the brick
    def check_brick(self):
        for i in range(int(self.ball.x), int(self.ball.x)+4*BALL_RADIUS, 2*BALL_RADIUS):
            for j in range(int(self.ball.y), int(self.ball.y)+4*BALL_RADIUS, 2*BALL_RADIUS):
                # check by the 4 points of the ball
                maybe_brick = self.window.get_object_at(i, j)
                if maybe_brick is not None and maybe_brick is not self.paddle:  # a brick is hit
                    self.window.remove(maybe_brick)  # the hit brick will disappear
                    self.num_brick -= 1  # decrease the number of brick for counting
                    return True

    # All brick is hit. The ball and the paddle will disappear then the window will show "Completed!"
    def no_bricks(self):
        self.window.remove(self.ball)
        self.window.remove(self.paddle)
        complete = GLabel('Completed!')
        complete.font = '-30'
        self.window.add(complete, x=(self.window.width-complete.width)/2, y=(self.window.height-complete.height)/2)

    # get the number of remain brick
    def get_no_bricks(self):
        return self.num_brick

    # whether the ball hits the paddle
    def check_paddle(self):
        for i in range(int(self.ball.x), int(self.ball.x) + 4 * BALL_RADIUS, 2 * BALL_RADIUS):
            maybe_paddle = self.window.get_object_at(i, int(self.ball.y) + 2*BALL_RADIUS)
            #  check by the two lower points of the ball
            if maybe_paddle is self.paddle:
                return True


if __name__ =='breakoutgraphics':
    pass
