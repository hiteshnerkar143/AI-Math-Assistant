"""
Machine Learning Model Module

This module provides the AI model for predicting mathematical operations
from natural language input using scikit-learn.
"""

import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle
import logging
from typing import Tuple, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MathAIModel:
    """
    AI model for predicting mathematical operations from natural language.
    
    Uses TF-IDF Vectorizer and Multinomial Naive Bayes classifier.
    
    Attributes:
        model_path: Path to save/load the trained model
        pipeline: The sklearn pipeline with vectorizer and classifier
        is_trained: Whether the model has been trained
    """
    
    def __init__(self, model_path: str = "models/math_model.pkl"):
        """
        Initialize the AI model.
        
        Args:
            model_path: Path to save/load the model
        """
        self.model_path = model_path
        self.pipeline = None
        self.is_trained = False
        self.classes = []
        self.load_model()
    
    def create_pipeline(self) -> Pipeline:
        """
        Create the ML pipeline.
        
        Returns:
            Sklearn Pipeline with TF-IDF and Naive Bayes
        """
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(lowercase=True, 
                                     max_features=500,
                                     stop_words='english',
                                     ngram_range=(1, 2))),
            ('clf', MultinomialNB(alpha=1.0))
        ])
        return pipeline
    
    def train(self, texts: List[str], labels: List[str]) -> bool:
        """
        Train the model with provided data.
        
        Args:
            texts: List of input texts
            labels: List of corresponding operation labels
            
        Returns:
            True if training successful
        """
        try:
            if not texts or not labels or len(texts) != len(labels):
                logger.error("Invalid training data")
                return False
            
            logger.info(f"Training model with {len(texts)} samples...")
            
            # Create and train pipeline
            self.pipeline = self.create_pipeline()
            self.pipeline.fit(texts, labels)
            
            self.classes = self.pipeline.classes_
            self.is_trained = True
            
            # Save the model
            self.save_model()
            
            logger.info(f"Model trained successfully with {len(self.classes)} classes")
            return True
        
        except Exception as e:
            logger.error(f"Error training model: {str(e)}")
            self.is_trained = False
            return False
    
    def predict(self, text: str) -> Tuple[str, float]:
        """
        Predict the operation for given text.
        
        Args:
            text: Input text
            
        Returns:
            Tuple of (predicted_operation, confidence_score)
            
        Raises:
            RuntimeError: If model is not trained
        """
        if not self.is_trained or self.pipeline is None:
            raise RuntimeError("Model is not trained yet")
        
        try:
            # Get prediction
            prediction = self.pipeline.predict([text])[0]
            
            # Get confidence scores
            probabilities = self.pipeline.predict_proba([text])[0]
            max_prob = max(probabilities)
            
            return prediction, float(max_prob)
        
        except Exception as e:
            logger.error(f"Error making prediction: {str(e)}")
            return None, 0.0
    
    def predict_proba(self, text: str) -> Dict[str, float]:
        """
        Get probability distribution for all classes.
        
        Args:
            text: Input text
            
        Returns:
            Dictionary of {operation: probability}
        """
        if not self.is_trained or self.pipeline is None:
            return {}
        
        try:
            probabilities = self.pipeline.predict_proba([text])[0]
            result = {}
            for cls, prob in zip(self.classes, probabilities):
                result[cls] = float(prob)
            
            # Sort by probability
            return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
        
        except Exception as e:
            logger.error(f"Error getting probabilities: {str(e)}")
            return {}
    
    def retrain(self, texts: List[str], labels: List[str]) -> bool:
        """
        Retrain the model with new data.
        
        Args:
            texts: List of input texts
            labels: List of corresponding labels
            
        Returns:
            True if retraining successful
        """
        logger.info("Retraining model...")
        return self.train(texts, labels)
    
    def save_model(self) -> bool:
        """
        Save the trained model to disk.
        
        Returns:
            True if successful
        """
        try:
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            
            with open(self.model_path, 'wb') as f:
                pickle.dump(self.pipeline, f)
            
            logger.info(f"Model saved to {self.model_path}")
            return True
        
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            return False
    
    def load_model(self) -> bool:
        """
        Load a trained model from disk.
        
        Returns:
            True if successful
        """
        try:
            if os.path.exists(self.model_path):
                with open(self.model_path, 'rb') as f:
                    self.pipeline = pickle.load(f)
                
                self.classes = self.pipeline.classes_
                self.is_trained = True
                logger.info("Model loaded successfully")
                return True
            else:
                logger.info("Model file not found, will need to train first")
                return False
        
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            return False
    
    def get_feature_names(self) -> List[str]:
        """
        Get the feature names from the vectorizer.
        
        Returns:
            List of feature names
        """
        if self.pipeline and hasattr(self.pipeline.named_steps['tfidf'], 'get_feature_names_out'):
            return list(self.pipeline.named_steps['tfidf'].get_feature_names_out())
        return []
    
    def get_model_info(self) -> Dict:
        """
        Get information about the model.
        
        Returns:
            Dictionary with model information
        """
        return {
            'is_trained': self.is_trained,
            'num_classes': len(self.classes) if self.is_trained else 0,
            'classes': list(self.classes) if self.is_trained else [],
            'model_path': self.model_path,
            'num_features': len(self.get_feature_names())
        }


# Singleton instance
_model = None


def get_model(model_path: str = "models/math_model.pkl") -> MathAIModel:
    """Get the singleton model instance."""
    global _model
    if _model is None:
        _model = MathAIModel(model_path)
    return _model
