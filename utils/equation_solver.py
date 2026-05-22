"""
Equation Solver Module

This module provides functionality to solve linear equations
and display step-by-step solutions.
"""

import sympy as sp
from typing import Dict, List, Tuple
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EquationSolver:
    """
    Solves linear and polynomial equations with step-by-step solutions.
    """
    
    def __init__(self):
        """Initialize the equation solver."""
        self.x = sp.Symbol('x')
    
    def parse_equation(self, equation_str: str) -> Tuple[sp.Expr, str]:
        """
        Parse an equation string into a SymPy expression.
        
        Args:
            equation_str: Equation in form "left=right"
            
        Returns:
            Tuple of (equation expression, original string)
            
        Raises:
            ValueError: If equation format is invalid
        """
        if '=' not in equation_str:
            raise ValueError("Error: Equation must contain '=' sign")
        
        left, right = equation_str.split('=', 1)
        left = left.strip()
        right = right.strip()
        
        try:
            # Replace common notations
            left = left.replace('^', '**')
            right = right.replace('^', '**')
            left = left.replace('x', 'sp.Symbol("x")')
            right = right.replace('x', 'sp.Symbol("x")')
            
            left_expr = sp.sympify(left)
            right_expr = sp.sympify(right)
            
            # Create equation: left - right = 0
            equation = left_expr - right_expr
            return equation, equation_str
        except Exception as e:
            raise ValueError(f"Error: Invalid equation format - {str(e)}")
    
    def solve_linear(self, equation_str: str) -> Dict:
        """
        Solve a linear equation and provide step-by-step solution.
        
        Args:
            equation_str: Equation string (e.g., "2*x+10=50")
            
        Returns:
            Dictionary containing solution and steps
            
        Raises:
            ValueError: If equation is invalid or not linear
        """
        try:
            equation, original = self.parse_equation(equation_str)
            
            # Solve the equation
            solutions = sp.solve(equation, self.x)
            
            if not solutions:
                return {
                    'success': False,
                    'error': 'No solution found for this equation',
                    'original_equation': original
                }
            
            solution = solutions[0]
            
            # Generate steps
            steps = self._generate_solution_steps(equation_str, equation, solution)
            
            return {
                'success': True,
                'original_equation': original,
                'solution': float(solution) if solution.is_number else solution,
                'solution_str': str(solution),
                'steps': steps
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'original_equation': equation_str
            }
    
    def _generate_solution_steps(self, original: str, equation: sp.Expr, solution: sp.Number) -> List[str]:
        """
        Generate step-by-step solution steps.
        
        Args:
            original: Original equation string
            equation: SymPy equation expression
            solution: The solution
            
        Returns:
            List of solution steps
        """
        steps = [
            f"Given equation: {original}",
            f"Rearrange: {equation} = 0",
        ]
        
        # Add algebraic manipulation steps
        try:
            # For simple linear equations, show standard form
            left, right = original.split('=')
            steps.append(f"Move all terms to one side: {equation} = 0")
            
            # Show the solution step
            steps.append(f"Solve for x: x = {solution}")
            
            # Verify solution
            left_expr = sp.sympify(left.strip().replace('^', '**'))
            right_expr = sp.sympify(right.strip().replace('^', '**'))
            left_value = left_expr.subs(self.x, solution)
            right_value = right_expr.subs(self.x, solution)
            
            steps.append(f"\nVerification:")
            steps.append(f"Substitute x = {solution}:")
            steps.append(f"Left side: {left_value} = {float(left_value) if left_value.is_number else left_value}")
            steps.append(f"Right side: {right_value} = {float(right_value) if right_value.is_number else right_value}")
            
            if left_value == right_value:
                steps.append("✓ Both sides are equal - solution is correct!")
            else:
                steps.append("✗ Solution verification failed")
        
        except Exception as e:
            logger.warning(f"Could not generate detailed steps: {str(e)}")
        
        return steps
    
    def solve_quadratic(self, equation_str: str) -> Dict:
        """
        Solve a quadratic equation.
        
        Args:
            equation_str: Quadratic equation string
            
        Returns:
            Dictionary containing solutions and steps
        """
        try:
            equation, original = self.parse_equation(equation_str)
            
            # Solve the equation
            solutions = sp.solve(equation, self.x)
            
            if not solutions:
                return {
                    'success': False,
                    'error': 'No solution found',
                    'original_equation': original
                }
            
            steps = [
                f"Given equation: {original}",
                f"Standard form: {equation} = 0"
            ]
            
            # Convert solutions to numeric if possible
            numeric_solutions = []
            for sol in solutions:
                try:
                    numeric_solutions.append(float(sol))
                except:
                    numeric_solutions.append(sol)
            
            return {
                'success': True,
                'original_equation': original,
                'solutions': numeric_solutions,
                'steps': steps
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'original_equation': equation_str
            }
    
    def solve_polynomial(self, equation_str: str) -> Dict:
        """
        Solve a polynomial equation of any degree.
        
        Args:
            equation_str: Polynomial equation string
            
        Returns:
            Dictionary containing solutions
        """
        try:
            equation, original = self.parse_equation(equation_str)
            solutions = sp.solve(equation, self.x)
            
            if not solutions:
                return {
                    'success': False,
                    'error': 'No solution found',
                    'original_equation': original
                }
            
            # Convert to numeric form when possible
            numeric_solutions = []
            for sol in solutions:
                try:
                    numeric_solutions.append(float(sol.evalf()))
                except:
                    numeric_solutions.append(str(sol))
            
            return {
                'success': True,
                'original_equation': original,
                'solutions': numeric_solutions,
                'solution_count': len(numeric_solutions)
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'original_equation': equation_str
            }


# Singleton instance
_solver = EquationSolver()


def get_solver() -> EquationSolver:
    """Get the singleton equation solver instance."""
    return _solver
