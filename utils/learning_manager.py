"""
Learning Manager Module

This module manages the learning system for the AI Math Assistant,
including storing new patterns and managing training data.
"""

import json
import os
from typing import Dict, List, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LearningManager:
    """
    Manages learning and training data for the AI model.
    
    Attributes:
        training_file: Path to the training data file
        training_data: Dictionary of training data
    """
    
    def __init__(self, training_file: str = "data/training_data.json"):
        """
        Initialize the learning manager.
        
        Args:
            training_file: Path to the training data file
        """
        self.training_file = training_file
        self.training_data = {}
        self.learned_patterns = []
        self.load_training_data()
    
    def load_training_data(self) -> bool:
        """
        Load training data from file.
        
        Returns:
            True if successful
        """
        try:
            if os.path.exists(self.training_file):
                with open(self.training_file, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    # Handle both list and dict formats
                    if isinstance(content, list):
                        # Convert list format to dict format
                        self.training_data = {}
                        for item in content:
                            if isinstance(item, dict) and 'label' in item:
                                label = item['label']
                                if label not in self.training_data:
                                    self.training_data[label] = []
                                self.training_data[label].append(item.get('text', ''))
                    else:
                        self.training_data = content
                
                logger.info(f"Loaded training data with {len(self.training_data)} categories")
                return True
            else:
                self.training_data = self._get_default_training_data()
                self.save_training_data()
                return True
        except Exception as e:
            logger.error(f"Error loading training data: {str(e)}")
            self.training_data = self._get_default_training_data()
            return False
    
    def save_training_data(self) -> bool:
        """
        Save training data to file.
        
        Returns:
            True if successful
        """
        try:
            os.makedirs(os.path.dirname(self.training_file), exist_ok=True)
            
            # Convert to list format for ML model
            training_list = []
            for label, texts in self.training_data.items():
                for text in texts:
                    training_list.append({'label': label, 'text': text})
            
            with open(self.training_file, 'w', encoding='utf-8') as f:
                json.dump(training_list, f, indent=2, ensure_ascii=False)
            logger.info("Training data saved")
            return True
        except Exception as e:
            logger.error(f"Error saving training data: {str(e)}")
            return False
    
    def _get_default_training_data(self) -> Dict:
        """
        Get default training data.
        
        Returns:
            Dictionary with default training data
        """
        return {
            'add': ['add', 'sum', 'plus', 'plus', 'addition'],
            'subtract': ['subtract', 'minus', 'difference', 'subtract', 'reduction'],
            'multiply': ['multiply', 'times', 'product', 'multiplication', 'multiply'],
            'divide': ['divide', 'division', 'quotient', 'divide', 'split'],
            'power': ['power', 'exponent', 'to the power of', 'power', 'squared', 'cubed'],
            'sqrt': ['square root', 'sqrt', 'root', 'square root of'],
            'factorial': ['factorial', 'fact', 'factorial'],
            'sin': ['sine', 'sin', 'sine of'],
            'cos': ['cosine', 'cos', 'cosine of'],
            'tan': ['tangent', 'tan', 'tangent of'],
            'log': ['logarithm', 'log', 'log base'],
            'mean': ['mean', 'average', 'avg', 'mean value'],
            'median': ['median', 'middle value'],
            'gcd': ['gcd', 'greatest common divisor', 'hcf', 'highest common factor'],
            'lcm': ['lcm', 'least common multiple'],
            'prime': ['prime', 'is prime', 'check prime'],
            'solve': ['solve', 'equation', 'find x', 'solution'],
            'graph': ['plot', 'graph', 'draw', 'visualization'],
            'percentage': ['percentage', 'percent', 'percentage of'],
            'modulus': ['modulus', 'mod', 'remainder']
        }
    
    def add_learned_pattern(self, user_input: str, operation: str, 
                           confidence: float = 0.0) -> bool:
        """
        Add a new learned pattern to the training data.
        
        Args:
            user_input: The user's input text
            operation: The correct operation
            confidence: The confidence score of the original prediction
            
        Returns:
            True if successfully added
        """
        try:
            # Avoid duplicates
            if operation in self.training_data:
                if user_input in self.training_data[operation]:
                    logger.info(f"Pattern already exists: {user_input}")
                    return False
            
            # Add to training data
            if operation not in self.training_data:
                self.training_data[operation] = []
            
            self.training_data[operation].append(user_input.lower())
            
            # Record the learning
            self.learned_patterns.append({
                'timestamp': datetime.now().isoformat(),
                'user_input': user_input,
                'operation': operation,
                'low_confidence': confidence < 0.6
            })
            
            self.save_training_data()
            logger.info(f"Added learned pattern: {user_input} -> {operation}")
            return True
        
        except Exception as e:
            logger.error(f"Error adding learned pattern: {str(e)}")
            return False
    
    def get_training_data_for_ml(self) -> tuple:
        """
        Get training data in format suitable for ML model.
        
        Returns:
            Tuple of (texts, labels)
        """
        texts = []
        labels = []
        
        for label, text_list in self.training_data.items():
            for text in text_list:
                texts.append(text)
                labels.append(label)
        
        return texts, labels
    
    def get_learned_patterns(self) -> List[Dict]:
        """
        Get all learned patterns.
        
        Returns:
            List of learned patterns
        """
        return self.learned_patterns
    
    def get_learning_stats(self) -> Dict:
        """
        Get statistics about the learning.
        
        Returns:
            Dictionary with learning statistics
        """
        return {
            'total_patterns': sum(len(v) for v in self.training_data.values()),
            'categories': len(self.training_data),
            'learned_patterns': len(self.learned_patterns),
            'low_confidence_learnings': sum(1 for p in self.learned_patterns if p.get('low_confidence'))
        }
    
    def retrain_trigger_needed(self) -> bool:
        """
        Check if retraining is needed.
        
        Returns:
            True if retraining should be triggered
        """
        # Retrain if significant new patterns have been learned
        return len(self.learned_patterns) >= 5


# Singleton instance
_learning_manager = None


def get_learning_manager(training_file: str = "data/training_data.json") -> LearningManager:
    """Get the singleton learning manager instance."""
    global _learning_manager
    if _learning_manager is None:
        _learning_manager = LearningManager(training_file)
    return _learning_manager
