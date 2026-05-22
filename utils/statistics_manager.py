"""
Statistics Manager Module

This module manages and tracks statistics about the application usage.
"""

import json
import os
from typing import Dict, List
from collections import Counter
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class StatisticsManager:
    """
    Manages statistics and analytics for the application.
    """
    
    def __init__(self):
        """Initialize the statistics manager."""
        self.stats = {
            'total_questions': 0,
            'total_calculations': 0,
            'operations_used': {},
            'graphs_generated': 0,
            'equations_solved': 0,
            'learned_patterns': 0,
            'accuracy_rate': 0.0,
            'voice_inputs': 0,
            'voice_outputs': 0
        }
    
    def increment_questions(self, count: int = 1) -> None:
        """Increment total questions counter."""
        self.stats['total_questions'] += count
    
    def increment_calculations(self, count: int = 1) -> None:
        """Increment total calculations counter."""
        self.stats['total_calculations'] += count
    
    def add_operation_usage(self, operation: str) -> None:
        """
        Record usage of an operation.
        
        Args:
            operation: The operation used
        """
        if operation not in self.stats['operations_used']:
            self.stats['operations_used'][operation] = 0
        self.stats['operations_used'][operation] += 1
    
    def increment_graphs(self, count: int = 1) -> None:
        """Increment graphs generated counter."""
        self.stats['graphs_generated'] += count
    
    def increment_equations(self, count: int = 1) -> None:
        """Increment equations solved counter."""
        self.stats['equations_solved'] += count
    
    def increment_learned_patterns(self, count: int = 1) -> None:
        """Increment learned patterns counter."""
        self.stats['learned_patterns'] += count
    
    def increment_voice_inputs(self, count: int = 1) -> None:
        """Increment voice inputs counter."""
        self.stats['voice_inputs'] += count
    
    def increment_voice_outputs(self, count: int = 1) -> None:
        """Increment voice outputs counter."""
        self.stats['voice_outputs'] += count
    
    def set_accuracy_rate(self, accuracy: float) -> None:
        """
        Set the accuracy rate.
        
        Args:
            accuracy: Accuracy percentage (0-100)
        """
        self.stats['accuracy_rate'] = min(100, max(0, accuracy))
    
    def get_most_used_operation(self) -> tuple:
        """
        Get the most used operation.
        
        Returns:
            Tuple of (operation, count)
        """
        if not self.stats['operations_used']:
            return None, 0
        operation = max(self.stats['operations_used'], 
                       key=self.stats['operations_used'].get)
        return operation, self.stats['operations_used'][operation]
    
    def get_statistics(self) -> Dict:
        """
        Get all statistics.
        
        Returns:
            Dictionary with all statistics
        """
        most_used, most_used_count = self.get_most_used_operation()
        
        return {
            'total_questions': self.stats['total_questions'],
            'total_calculations': self.stats['total_calculations'],
            'operations_used': self.stats['operations_used'],
            'most_used_operation': most_used,
            'most_used_count': most_used_count,
            'graphs_generated': self.stats['graphs_generated'],
            'equations_solved': self.stats['equations_solved'],
            'learned_patterns': self.stats['learned_patterns'],
            'accuracy_rate': f"{self.stats['accuracy_rate']:.2f}%",
            'voice_inputs': self.stats['voice_inputs'],
            'voice_outputs': self.stats['voice_outputs'],
            'total_operations_categories': len(self.stats['operations_used'])
        }
    
    def get_dashboard_data(self) -> Dict:
        """
        Get data formatted for dashboard display.
        
        Returns:
            Dictionary with dashboard data
        """
        stats = self.get_statistics()
        
        # Get top 5 operations
        top_operations = sorted(
            self.stats['operations_used'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        
        return {
            'total_questions': stats['total_questions'],
            'total_calculations': stats['total_calculations'],
            'most_used_operation': stats['most_used_operation'],
            'graphs_generated': stats['graphs_generated'],
            'equations_solved': stats['equations_solved'],
            'learned_patterns': stats['learned_patterns'],
            'accuracy_rate': stats['accuracy_rate'],
            'voice_inputs': stats['voice_inputs'],
            'voice_outputs': stats['voice_outputs'],
            'top_operations': top_operations
        }
    
    def reset_statistics(self) -> None:
        """Reset all statistics to zero."""
        self.stats = {
            'total_questions': 0,
            'total_calculations': 0,
            'operations_used': {},
            'graphs_generated': 0,
            'equations_solved': 0,
            'learned_patterns': 0,
            'accuracy_rate': 0.0,
            'voice_inputs': 0,
            'voice_outputs': 0
        }
        logger.info("Statistics reset")
    
    def get_summary(self) -> str:
        """
        Get a text summary of statistics.
        
        Returns:
            Formatted string summary
        """
        stats = self.get_statistics()
        
        summary = "=== Statistics Summary ===\n"
        summary += f"Total Questions: {stats['total_questions']}\n"
        summary += f"Total Calculations: {stats['total_calculations']}\n"
        summary += f"Most Used Operation: {stats['most_used_operation']} ({stats['most_used_count']} times)\n"
        summary += f"Graphs Generated: {stats['graphs_generated']}\n"
        summary += f"Equations Solved: {stats['equations_solved']}\n"
        summary += f"Learned Patterns: {stats['learned_patterns']}\n"
        summary += f"Accuracy Rate: {stats['accuracy_rate']}\n"
        summary += f"Voice Inputs: {stats['voice_inputs']}\n"
        summary += f"Voice Outputs: {stats['voice_outputs']}\n"
        
        return summary


# Singleton instance
_stats_manager = StatisticsManager()


def get_statistics_manager() -> StatisticsManager:
    """Get the singleton statistics manager instance."""
    return _stats_manager
