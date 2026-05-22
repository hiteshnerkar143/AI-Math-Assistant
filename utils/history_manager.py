"""
History Manager Module

This module manages chat history, including storing, retrieving,
exporting, and clearing conversation history.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HistoryManager:
    """
    Manages chat history and conversation data.
    
    Attributes:
        history_file: Path to the history JSON file
        history: List of history entries
    """
    
    def __init__(self, history_file: str = "data/chat_history.json"):
        """
        Initialize the history manager.
        
        Args:
            history_file: Path to the history file
        """
        self.history_file = history_file
        self.history = []
        self.load_history()
    
    def load_history(self) -> bool:
        """
        Load history from file.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    self.history = json.load(f)
                logger.info(f"Loaded {len(self.history)} history entries")
                return True
            else:
                self.history = []
                return True
        except Exception as e:
            logger.error(f"Error loading history: {str(e)}")
            self.history = []
            return False
    
    def save_history(self) -> bool:
        """
        Save history to file.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
            
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, indent=2, ensure_ascii=False)
            logger.info("History saved successfully")
            return True
        except Exception as e:
            logger.error(f"Error saving history: {str(e)}")
            return False
    
    def add_entry(self, question: str, answer: str, operation: str = "", 
                  confidence: float = 0.0) -> Dict:
        """
        Add a new entry to the history.
        
        Args:
            question: User's question
            answer: Assistant's answer
            operation: The operation performed
            confidence: Confidence score of the prediction
            
        Returns:
            The created entry dictionary
        """
        entry = {
            'timestamp': datetime.now().isoformat(),
            'question': question,
            'answer': str(answer),
            'operation': operation,
            'confidence': float(confidence)
        }
        self.history.append(entry)
        self.save_history()
        logger.info(f"Added history entry: {question[:50]}...")
        return entry
    
    def get_all_history(self) -> List[Dict]:
        """
        Get all history entries.
        
        Returns:
            List of history entries
        """
        return self.history
    
    def get_history_by_operation(self, operation: str) -> List[Dict]:
        """
        Get history entries for a specific operation.
        
        Args:
            operation: The operation to filter by
            
        Returns:
            List of matching history entries
        """
        return [entry for entry in self.history if entry.get('operation') == operation]
    
    def get_recent_history(self, limit: int = 10) -> List[Dict]:
        """
        Get recent history entries.
        
        Args:
            limit: Number of recent entries to return
            
        Returns:
            List of recent history entries
        """
        return self.history[-limit:]
    
    def get_history_stats(self) -> Dict:
        """
        Get statistics about the history.
        
        Returns:
            Dictionary containing history statistics
        """
        if not self.history:
            return {
                'total_entries': 0,
                'unique_operations': 0,
                'most_used_operation': None,
                'total_unique_questions': 0
            }
        
        operations = [entry.get('operation', '') for entry in self.history]
        questions = [entry.get('question', '') for entry in self.history]
        
        from collections import Counter
        operation_counts = Counter(operations)
        most_used = operation_counts.most_common(1)[0] if operation_counts else (None, 0)
        
        return {
            'total_entries': len(self.history),
            'unique_operations': len(set(operations)),
            'most_used_operation': most_used[0],
            'most_used_count': most_used[1],
            'total_unique_questions': len(set(questions))
        }
    
    def clear_history(self) -> bool:
        """
        Clear all history.
        
        Returns:
            True if successful
        """
        self.history = []
        self.save_history()
        logger.info("History cleared")
        return True
    
    def delete_entry(self, index: int) -> bool:
        """
        Delete a specific history entry.
        
        Args:
            index: Index of entry to delete
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if 0 <= index < len(self.history):
                self.history.pop(index)
                self.save_history()
                return True
            return False
        except Exception as e:
            logger.error(f"Error deleting entry: {str(e)}")
            return False
    
    def search_history(self, query: str) -> List[Dict]:
        """
        Search history by question content.
        
        Args:
            query: Search query
            
        Returns:
            List of matching entries
        """
        query_lower = query.lower()
        return [entry for entry in self.history 
                if query_lower in entry.get('question', '').lower()]
    
    def export_to_json(self, filename: str) -> bool:
        """
        Export history to a JSON file.
        
        Args:
            filename: Output filename
            
        Returns:
            True if successful
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, indent=2, ensure_ascii=False)
            logger.info(f"History exported to {filename}")
            return True
        except Exception as e:
            logger.error(f"Error exporting history: {str(e)}")
            return False
    
    def export_to_text(self, filename: str) -> bool:
        """
        Export history to a text file.
        
        Args:
            filename: Output filename
            
        Returns:
            True if successful
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=== AI Math Assistant Chat History ===\n")
                f.write(f"Exported: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 40 + "\n\n")
                
                for idx, entry in enumerate(self.history, 1):
                    f.write(f"Entry {idx}:\n")
                    f.write(f"Time: {entry.get('timestamp', 'N/A')}\n")
                    f.write(f"Question: {entry.get('question', 'N/A')}\n")
                    f.write(f"Answer: {entry.get('answer', 'N/A')}\n")
                    f.write(f"Operation: {entry.get('operation', 'N/A')}\n")
                    f.write(f"Confidence: {entry.get('confidence', 'N/A')}\n")
                    f.write("-" * 40 + "\n\n")
            
            logger.info(f"History exported to {filename}")
            return True
        except Exception as e:
            logger.error(f"Error exporting history: {str(e)}")
            return False


# Singleton instance
_history_manager = None


def get_history_manager(history_file: str = "data/chat_history.json") -> HistoryManager:
    """Get the singleton history manager instance."""
    global _history_manager
    if _history_manager is None:
        _history_manager = HistoryManager(history_file)
    return _history_manager
