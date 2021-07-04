"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    This function makes a breakout game.
    The user has NUM_LIVES to play the game until the
    bricks are all hit or the live is 0.
    """
    graphics = BreakoutGraphics()
    vx = graphics.get_dx()  # the horizontal velocity
    vy = graphics.get_dy()  # the vertical velocity
    global NUM_LIVES
    while True:
        a = graphics.get_event()  # whether the user click the mouse to start the game  # discuss with Ilona
        if a:  # click and start the game
            graphics.ball.move(vx, vy)
            if graphics.check_brick() is True:  # the ball hits the brick
                vy = -vy
                if graphics.get_no_bricks() == 0:  # every brick is hit and disappeared!
                    graphics.no_bricks()  # the ball and the paddle will removed from the window
                    break
            if graphics.check_paddle() is True:  # the ball hits the paddle
                vy = -vy
                graphics.ball.move(vx, graphics.ball.y-graphics.paddle.y)
                # avoid the ball hits the paddle more than 1 time
            if graphics.ball.y <= 0:  # the ball hits the top of the window
                vy = -vy
            if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                # the ball hits the right and left side of the window
                vx = -vx
        pause(FRAME_RATE)
        if graphics.ball.y >= graphics.window.height:  # the ball is get out of the window and will lose 1 live
            NUM_LIVES -= 1
            graphics.window.add(graphics.ball, x=(graphics.window.width-graphics.ball.width)/2,
                                y=(graphics.window.height-graphics.ball.height)/2)
            # put the ball back to wait for the start
            graphics.event = False
        if NUM_LIVES == 0:  # if the live is 0 then the game is over
            break


if __name__ == '__main__':
    main()
