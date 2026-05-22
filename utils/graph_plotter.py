"""
Graph Plotter Module

This module provides functionality to plot mathematical functions
using Matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from typing import Optional, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GraphPlotter:
    """
    Plots mathematical functions and expressions.
    """
    
    def __init__(self):
        """Initialize the graph plotter."""
        self.figure = None
        self.ax = None
    
    def plot_function(self, 
                     function_str: str, 
                     x_min: float = -10, 
                     x_max: float = 10,
                     title: Optional[str] = None,
                     y_min: Optional[float] = None,
                     y_max: Optional[float] = None) -> bool:
        """
        Plot a mathematical function.
        
        Args:
            function_str: Function as string (e.g., "x**2", "sin(x)", "cos(x)")
            x_min: Minimum x value for plotting
            x_max: Maximum x value for plotting
            title: Title for the plot
            y_min: Minimum y value for plot range
            y_max: Maximum y value for plot range
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Create figure and axis
            self.figure, self.ax = plt.subplots(figsize=(10, 6))
            
            # Parse function string
            x = sp.Symbol('x')
            function_str = function_str.replace('^', '**')
            
            try:
                func = sp.sympify(function_str)
            except Exception as e:
                logger.error(f"Invalid function: {str(e)}")
                return False
            
            # Create lambda function for numerical plotting
            func_lambda = sp.lambdify(x, func, 'numpy')
            
            # Generate x values
            x_vals = np.linspace(x_min, x_max, 1000)
            
            # Calculate y values with error handling
            try:
                y_vals = func_lambda(x_vals)
            except Exception as e:
                logger.error(f"Error evaluating function: {str(e)}")
                return False
            
            # Filter out inf and nan values
            valid_mask = np.isfinite(y_vals)
            x_vals_filtered = x_vals[valid_mask]
            y_vals_filtered = y_vals[valid_mask]
            
            if len(x_vals_filtered) == 0:
                logger.error("No valid points to plot")
                return False
            
            # Plot the function
            self.ax.plot(x_vals_filtered, y_vals_filtered, 'b-', linewidth=2, label=function_str)
            
            # Customize the plot
            self.ax.grid(True, alpha=0.3)
            self.ax.axhline(y=0, color='k', linewidth=0.5)
            self.ax.axvline(x=0, color='k', linewidth=0.5)
            
            self.ax.set_xlabel('x', fontsize=12)
            self.ax.set_ylabel('y', fontsize=12)
            
            if title:
                self.ax.set_title(title, fontsize=14, fontweight='bold')
            else:
                self.ax.set_title(f'Graph of {function_str}', fontsize=14, fontweight='bold')
            
            # Set y-axis limits if provided
            if y_min is not None and y_max is not None:
                self.ax.set_ylim(y_min, y_max)
            
            self.ax.legend(fontsize=10)
            
            # Display the plot
            plt.tight_layout()
            plt.show()
            
            return True
        
        except Exception as e:
            logger.error(f"Error plotting function: {str(e)}")
            return False
    
    def plot_multiple_functions(self,
                               functions: List[str],
                               x_min: float = -10,
                               x_max: float = 10,
                               title: str = "Multiple Functions") -> bool:
        """
        Plot multiple functions on the same graph.
        
        Args:
            functions: List of function strings
            x_min: Minimum x value
            x_max: Maximum x value
            title: Title for the plot
            
        Returns:
            True if successful
        """
        try:
            if not functions:
                return False
            
            self.figure, self.ax = plt.subplots(figsize=(10, 6))
            
            colors = ['b', 'r', 'g', 'm', 'c', 'orange', 'purple']
            x = sp.Symbol('x')
            
            for idx, func_str in enumerate(functions):
                try:
                    func_str_clean = func_str.replace('^', '**')
                    func = sp.sympify(func_str_clean)
                    func_lambda = sp.lambdify(x, func, 'numpy')
                    
                    x_vals = np.linspace(x_min, x_max, 1000)
                    y_vals = func_lambda(x_vals)
                    
                    # Filter valid values
                    valid_mask = np.isfinite(y_vals)
                    x_vals_filtered = x_vals[valid_mask]
                    y_vals_filtered = y_vals[valid_mask]
                    
                    if len(x_vals_filtered) > 0:
                        color = colors[idx % len(colors)]
                        self.ax.plot(x_vals_filtered, y_vals_filtered, color=color, 
                                   linewidth=2, label=func_str_clean)
                
                except Exception as e:
                    logger.warning(f"Error plotting function {func_str}: {str(e)}")
                    continue
            
            # Customize plot
            self.ax.grid(True, alpha=0.3)
            self.ax.axhline(y=0, color='k', linewidth=0.5)
            self.ax.axvline(x=0, color='k', linewidth=0.5)
            
            self.ax.set_xlabel('x', fontsize=12)
            self.ax.set_ylabel('y', fontsize=12)
            self.ax.set_title(title, fontsize=14, fontweight='bold')
            self.ax.legend(fontsize=10)
            
            plt.tight_layout()
            plt.show()
            
            return True
        
        except Exception as e:
            logger.error(f"Error plotting multiple functions: {str(e)}")
            return False
    
    def plot_parametric(self,
                       x_func: str,
                       y_func: str,
                       t_min: float = 0,
                       t_max: float = 2*np.pi,
                       title: str = "Parametric Plot") -> bool:
        """
        Plot a parametric function.
        
        Args:
            x_func: X function in terms of t
            y_func: Y function in terms of t
            t_min: Minimum t value
            t_max: Maximum t value
            title: Title for the plot
            
        Returns:
            True if successful
        """
        try:
            self.figure, self.ax = plt.subplots(figsize=(10, 6))
            
            t = sp.Symbol('t')
            x_func_clean = x_func.replace('^', '**')
            y_func_clean = y_func.replace('^', '**')
            
            x_expr = sp.sympify(x_func_clean)
            y_expr = sp.sympify(y_func_clean)
            
            x_lambda = sp.lambdify(t, x_expr, 'numpy')
            y_lambda = sp.lambdify(t, y_expr, 'numpy')
            
            t_vals = np.linspace(t_min, t_max, 1000)
            x_vals = x_lambda(t_vals)
            y_vals = y_lambda(t_vals)
            
            # Filter valid values
            valid_mask = np.isfinite(x_vals) & np.isfinite(y_vals)
            x_vals_filtered = x_vals[valid_mask]
            y_vals_filtered = y_vals[valid_mask]
            
            if len(x_vals_filtered) == 0:
                return False
            
            self.ax.plot(x_vals_filtered, y_vals_filtered, 'b-', linewidth=2)
            
            self.ax.grid(True, alpha=0.3)
            self.ax.set_xlabel('x', fontsize=12)
            self.ax.set_ylabel('y', fontsize=12)
            self.ax.set_title(title, fontsize=14, fontweight='bold')
            
            plt.tight_layout()
            plt.show()
            
            return True
        
        except Exception as e:
            logger.error(f"Error plotting parametric function: {str(e)}")
            return False


# Singleton instance
_plotter = GraphPlotter()


def get_plotter() -> GraphPlotter:
    """Get the singleton graph plotter instance."""
    return _plotter
