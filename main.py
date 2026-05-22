"""
AI Math Assistant - Main Entry Point

A comprehensive AI-powered mathematical assistant with a modern GUI,
supporting various mathematical operations, equation solving, graphing,
and voice features.

Author: AI Math Assistant Team
Version: 1.0
"""

import sys
import os
import logging

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def main():
    """Main entry point for the application."""
    try:
        logger.info("=" * 60)
        logger.info("Starting AI Math Assistant Application")
        logger.info("=" * 60)
        
        # Import GUI after logging is configured
        from gui.app import run_gui
        
        logger.info("Initializing GUI...")
        run_gui()
        
    except ImportError as e:
        logger.error(f"Import Error: {str(e)}")
        logger.error("Please ensure all required packages are installed.")
        logger.error("Run: pip install -r requirements.txt")
        sys.exit(1)
    
    except Exception as e:
        logger.error(f"Fatal Error: {str(e)}")
        sys.exit(1)
    
    finally:
        logger.info("Application closed")
        logger.info("=" * 60)


if __name__ == "__main__":
    main()
