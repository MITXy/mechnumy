"""

This module provides numerical solutions for differential equations
using the Finite Difference Method (FDM). It discretizes the domain
into grid points to approximate derivatives.

Key Features:
- Forward, backward, and central difference schemes.
- Solves linear and non-linear PDEs and ODEs.
- Includes stability and convergence analysis.

Example:
    from mechnumy.FDM import solve_fdm
    result = solve_fdm(boundary_conditions, step_size)
"""
