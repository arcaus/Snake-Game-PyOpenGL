# Snake Game using OpenGL

This project is an implementation of the classic Snake Game using only the OpenGL library. It was developed as part of the BracU CSE423 lab projects for Spring 2023. The unique requirement for this project was to create the game solely using PyOpenGL and the included OpenGL libraries, without utilizing any other libraries like PyGame.

## Instructions to Run the Game

To run the Snake Game on your system, follow these steps:

1. Create a Python project in a virtual environment (venv) using your preferred development environment, such as PyCharm, for a smoother setup process.

2. Install the necessary libraries within the virtual environment by following these steps:

   - Open the terminal inside the virtual environment.
   - Check your Python version by running the following command:
     ```sh
     py -V
     ```
   - Visit the following link to download the required [Python Extension Packages for Windows - Christoph Gohlke (Click here)](https://www.lfd.uci.edu/~gohlke/pythonlibs/#_pyopengl:~:text=PyOpenGL%E2%80%913.1.5%E2%80%91cp36%E2%80%91cp36m%E2%80%91win_amd64.wh)
   - Download the following files from the website:
     ```sh
     PyOpenGL‑3.1.6‑cp3x‑cp3x‑win_amd64.whl
     ```
     ```sh
     PyOpenGL_accelerate‑3.1.6‑cp3x‑cp3x‑win_amd64.whl
     ```
     Replace `cp3x` with your version of Python. For example, if your Python version is 3.10, the filenames should be:
     ```sh
     PyOpenGL‑3.1.6‑cp310‑cp310‑win_amd64.whl
     ```
     ```sh
     PyOpenGL_accelerate‑3.1.6‑cp310‑cp310‑win_amd64.whl
     ```
     Note that `cp3x` is replaced by `cp310` to match your Python version.
     Now Install these libraries using `pip`
     ```sh
     pip install PyOpenGL‑3.1.6‑cp3x‑cp3x‑win_amd64.whl
     ```
     ```sh
     pip install PyOpenGL_accelerate‑3.1.6‑cp3x‑cp3x‑win_amd64.whl
     ```

3. Download the `snake.py` script and place it in the same folder as your project.

4. Run the game and enjoy playing!

## How to Play

- Use the arrow keys (up, down, left, right) or the keyboard keys (W, A, S, D) to control the snake's movement.
- The objective is to eat the food (represented by squares blocks and circles) to grow longer.
- Avoid colliding with your own body, as it will result in game over.

Enjoy the classic Snake Game experience brought to you through the power of OpenGL! GG ! Enjoy the OG game!!

## License

This project is licensed under the [MIT License](LICENSE).
