# Magic Grid

## Project Description

Welcome to the Magic Grid project! This project aims to model real-life objects using appropriate data structures, employ various programming techniques, and utilize famous algorithms such as Bellman-Ford and Dijkstra's algorithms to solve real-world problems.

The main objective of this project is to navigate through a complex grid composed of cells with varying lengths of walls. The goal is to start from the top left cell and reach the bottom right cell by destroying the walls between adjacent cells. The challenge lies in finding the optimal combination of cells to minimize the effort required to destroy the walls, ensuring that the walls are as slim as possible.

To represent the grid, we utilize a graph as our data structure. By employing Dijkstra's algorithm, we can find the shortest possible path through the graph, allowing us to traverse the grid efficiently. Additionally, Bellman-Ford's algorithm is utilized to ensure that the chosen path is not only the shortest but also the most optimal.

As a bonus feature, we have implemented a heuristic algorithm to find a locally optimal path in a relatively short amount of time. This heuristic algorithm provides an alternative approach for finding a near-optimal path.

## Technologies Used

- **Python**: We have utilized Python as the programming language for the entire project, leveraging its simplicity and versatility.

- **turtle.py**: Python's turtle library has been employed to draw the grid and visualize the paths, making it easier to comprehend the solution.

## Getting Started

To get started with the Magic Grid project, follow these steps:

1. Clone the project repository from GitHub: 
`git clone https://github.com/ferhat-ramdani/The-Magic-Grid.git`
2. Install the required dependencies. Make sure you have Python installed on your machine.
`pip install turtle`
3. Navigate to the project directory:
`cd The-Magic-Grid`
4. Run the main Python file to execute the grid modeling program:
`python Main.py`

## Usage

Once the program is running, you can interact with the grid modeling application through the graphical user interface. Follow the instructions displayed on the screen to:

- Specify the dimensions of the grid and the lengths of the walls in each cell.
- Visualize the grid and the current path.
- Trigger the algorithm to find the shortest and most optimal path through the grid.
- Observe the visualization of the solution, including the destroyed walls and the chosen path.

Feel free to experiment with different grid configurations and wall lengths to observe the algorithm's behavior.

## Authors

- AHMIM Mohamed ([@Mohamed](https://github.com/MohamedAhmim))
- RAMDANI Ferhat ([@Ferhat](https://github.com/ferhat-ramdani))


