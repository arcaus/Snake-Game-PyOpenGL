# Snake Game using OpenGL

![Snake Game](snake_game_screenshot.png)

This project is an implementation of the classic Snake Game using only the OpenGL library. It was developed as part of the BracU CSE423 lab projects for Spring 2023. The unique requirement for this project was to create the game solely using PyOpenGL and the included OpenGL libraries, without utilizing any other libraries like PyGame.

## Instructions to Run the Game

To run the Snake Game on your system, follow these steps:

1. Create a Python project in a virtual environment (venv) using your preferred development environment, such as PyCharm, for a smoother setup process.

2. Install the necessary libraries within the virtual environment by following these steps:
   - Open the terminal inside the virtual environment.
   - Check your Python version by running the following command:
     ```bash
     py -V
     ```
   - Visit the following link to download the required Python Extension Packages for Windows by Christoph Gohlke: [Python Extension Packages for Windows - Christoph Gohlke](https://www.lfd.uci.edu/~gohlke/pythonlibs/#_pyopengl:~:text=PyOpenGL%E2%80%913.1.5%E2%80%91cp36%E2%80%91cp36m%E2%80%91win_amd64.wh)
   - Download the following files from the website:
     ```bash
     PyOpenGL‑3.1.6‑cp3x‑cp3x‑win_amd64.whl
     ```
     ```bash
     PyOpenGL_accelerate‑3.1.6‑cp3x‑cp3x‑win_amd64.whl
     ```
     Replace `cp3x` with your version of Python. For example, if your Python version is 3.10, the filenames should be:
     ```bash
     PyOpenGL‑3.1.6‑cp310‑cp310‑win_amd64.whl
     ```
     ```bash
     PyOpenGL_accelerate‑3.1.6‑cp310‑cp310‑win_amd64.whl
     ```
     Note that `cp3x` is replaced by `cp310` to match your Python version.
     Now Install these libraries using `pip`
     ```bash
     pip install PyOpenGL‑3.1.6‑cp3x‑cp3x‑win_amd64.whl
     ```
     ```bash
     pip install PyOpenGL_accelerate‑3.1.6‑cp3x‑cp3x‑win_amd64.whl
     ```

3. Download the `snake.py` script and place it in the same folder as your project.

4. Run the game and enjoy playing!

## How to Play

- Use the arrow keys (up, down, left, right) to control the snake's movement.
- The objective is to eat the food (represented by the red squares) to grow longer.
- Avoid hitting the boundaries or colliding with your own body, as it will result in game over.

Enjoy the classic Snake Game experience brought to you through the power of OpenGL!

## Acknowledgments

Special thanks to the BracU CSE423 course and its instructors for providing the opportunity to work on this project and learn more about PyOpenGL and OpenGL programming.

Feel free to explore, modify, and have fun with the Snake Game. Contributions and enhancements to the project are welcome!

## License

This project is licensed under the [MIT License](LICENSE).

