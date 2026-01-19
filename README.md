# numerical-simulation-free-fall

This project performs a numerical simulation of the free fall of a body under gravity,
taking into account air resistance. The motion is modeled using ordinary differential
equations and solved with explicit numerical integration methods.

The program allows the user to choose both the physical drag model and the numerical
integration method.

---

## Mathematical Model

The motion of the body is described by Newton’s second law in one dimension:

m * dv/dt = mg − F_drag  
dx/dt = v

where:
- x is the height above the ground
- v is the velocity
- g is the gravitational acceleration
- F_drag is the air resistance force

Two drag models are implemented:

- Linear air resistance:  
  F_drag = k · v

- Quadratic air resistance:  
  F_drag = k · v²

The direction of motion is assumed to be vertical, and gravity is treated as constant.

---

## Numerical Methods

The system of differential equations is solved numerically using one of the following
methods:

- Euler Method
- Improved Euler Method (Heun’s Method)

The improved Euler method provides better accuracy compared to the standard Euler method
by evaluating the slope at an intermediate step.

---

## Features

- Numerical simulation of free fall with air resistance
- Choice of drag model: linear or quadratic
- Choice of numerical integration method
- Computation of position, velocity, and acceleration as functions of time
- Visualization of results using matplotlib
- Interactive query of the body’s height at any given moment after the simulation

---

## Visualization and Interaction

After the simulation is completed, the program displays plots of:
- height vs time
- velocity vs time
- acceleration vs time

Once the plots are closed, the user can interactively query the height above the ground
for any chosen time moment within the simulated interval.

---

## Project Structure

src/ - source code
README.md - project description
LICENSE - license information
.gitignore - ignored files

---

## Requirements

- Python 3.x
- matplotlib
- numpy

---

## How to Run

1. Clone the repository
2. Install the required dependencies
3. Run the main script:

`bash
python main.py

Follow the on-screen instructions to select the numerical method and drag model.

---

## Educational Purpose

- This project was developed for educational purposes to demonstrate:

- numerical solution of ordinary differential equations

- comparison of numerical integration methods

- physical modeling of motion with resistive forces

- basic scientific visualization in Python

---

## License

This project is licensed under the MIT License.
See the LICENSE file for details.
