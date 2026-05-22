"""
AI Math Assistant Package

A comprehensive AI-powered mathematical assistant with a modern GUI,
supporting various mathematical operations, equation solving, graphing,
and voice features.
"""

__version__ = "1.0.0"
__author__ = "AI Math Assistant Team"
__description__ = "AI-powered Math Assistant with Modern GUI"

from gui import MathAssistantApp, run_gui
from models import get_model, MathAIModel
from utils import (
    get_calculator, Calculator,
    get_solver, EquationSolver,
    get_plotter, GraphPlotter,
    get_history_manager, HistoryManager,
    get_learning_manager, LearningManager,
    get_statistics_manager, StatisticsManager
)

__all__ = [
    'MathAssistantApp',
    'run_gui',
    'get_model',
    'MathAIModel',
    'get_calculator',
    'Calculator',
    'get_solver',
    'EquationSolver',
    'get_plotter',
    'GraphPlotter',
    'get_history_manager',
    'HistoryManager',
    'get_learning_manager',
    'LearningManager',
    'get_statistics_manager',
    'StatisticsManager',
]
