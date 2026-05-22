"""
GUI Application Module

This module provides the CustomTkinter-based GUI for the AI Math Assistant.
"""

import customtkinter as ctk
from PIL import Image, ImageDraw
import io
import threading
import logging
from datetime import datetime
import re
from typing import Optional

# Import all utility modules
from utils.calculator import get_calculator
from utils.equation_solver import get_solver
from utils.graph_plotter import get_plotter
from utils.history_manager import get_history_manager
from utils.learning_manager import get_learning_manager
from utils.statistics_manager import get_statistics_manager
from models.ml_model import get_model

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MathAssistantApp(ctk.CTk):
    """
    Main GUI application for the AI Math Assistant.
    """
    
    def __init__(self):
        """Initialize the application."""
        super().__init__()
        
        # Initialize managers
        self.calculator = get_calculator()
        self.solver = get_solver()
        self.plotter = get_plotter()
        self.history_manager = get_history_manager()
        self.learning_manager = get_learning_manager()
        self.stats_manager = get_statistics_manager()
        self.model = get_model()
        
        # Train model if needed
        if not self.model.is_trained:
            self._train_model_initial()
        
        # Configure window
        self.title("AI Math Assistant")
        self.geometry("1000x700")
        self.minsize(800, 600)
        
        # Set window icon (create a simple one if not exists)
        self._create_icon()
        
        # Configure grid
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Create widgets
        self._create_header()
        self._create_main_content()
        self._create_footer()
        
        logger.info("GUI Application initialized")
    
    def _train_model_initial(self):
        """Train the model with default data."""
        try:
            texts, labels = self.learning_manager.get_training_data_for_ml()
            if texts and labels:
                self.model.train(texts, labels)
                logger.info("Model trained with initial data")
        except Exception as e:
            logger.error(f"Error training initial model: {str(e)}")
    
    def _create_icon(self):
        """Create a simple application icon."""
        try:
            # Create a simple icon programmatically
            img = Image.new('RGB', (64, 64), color='blue')
            draw = ImageDraw.Draw(img)
            # Draw a simple math symbol
            draw.text((20, 20), "π", fill='white')
            
            # Convert to PhotoImage
            from PIL import ImageTk
            photo = ImageTk.PhotoImage(img)
            self.iconphoto(False, photo)
        except Exception as e:
            logger.warning(f"Could not set icon: {str(e)}")
    
    def _create_header(self):
        """Create the header section."""
        header_frame = ctk.CTkFrame(self, fg_color="#1e1e1e")
        header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        header_frame.grid_columnconfigure(1, weight=1)
        
        # Title
        title_label = ctk.CTkLabel(
            header_frame,
            text="🤖 AI Math Assistant",
            font=("Arial", 24, "bold"),
            text_color="#00ff00"
        )
        title_label.grid(row=0, column=0, padx=20, pady=15)
        
        # Status bar
        self.status_label = ctk.CTkLabel(
            header_frame,
            text="Ready",
            font=("Arial", 10),
            text_color="#888888"
        )
        self.status_label.grid(row=0, column=1, sticky="e", padx=20, pady=15)
    
    def _create_main_content(self):
        """Create the main content area."""
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Chat display area
        chat_container = ctk.CTkFrame(main_frame)
        chat_container.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        chat_container.grid_rowconfigure(0, weight=1)
        chat_container.grid_columnconfigure(0, weight=1)
        
        # Chat label
        chat_label = ctk.CTkLabel(
            chat_container,
            text="Chat History",
            font=("Arial", 14, "bold")
        )
        chat_label.grid(row=0, column=0, sticky="nw", padx=10, pady=(10, 5))
        
        # Chat text area with scrollbar
        self.chat_textbox = ctk.CTkTextbox(
            chat_container,
            font=("Arial", 11),
            fg_color="#2e2e2e",
            text_color="#ffffff",
            wrap="word"
        )
        self.chat_textbox.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.chat_textbox.configure(state="disabled")
        chat_container.grid_rowconfigure(1, weight=1)
        
        # Input area
        input_frame = ctk.CTkFrame(main_frame)
        input_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        input_frame.grid_columnconfigure(0, weight=1)
        
        input_label = ctk.CTkLabel(
            input_frame,
            text="Your Input:",
            font=("Arial", 12, "bold")
        )
        input_label.grid(row=0, column=0, sticky="nw", padx=5, pady=(0, 5))
        
        # Input entry
        self.input_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Enter a math problem or question...",
            font=("Arial", 11),
            height=40
        )
        self.input_entry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.input_entry.bind("<Return>", lambda e: self._handle_send())
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(input_frame)
        buttons_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        buttons_frame.grid_columnconfigure(5, weight=1)
        
        # Send button
        send_btn = ctk.CTkButton(
            buttons_frame,
            text="📤 Send",
            command=self._handle_send,
            fg_color="#00ff00",
            text_color="#000000",
            font=("Arial", 11, "bold")
        )
        send_btn.grid(row=0, column=0, padx=2)
        
        # Clear chat button
        clear_chat_btn = ctk.CTkButton(
            buttons_frame,
            text="🗑️ Clear Chat",
            command=self._handle_clear_chat,
            font=("Arial", 10)
        )
        clear_chat_btn.grid(row=0, column=1, padx=2)
        
        # View history button
        history_btn = ctk.CTkButton(
            buttons_frame,
            text="📋 History",
            command=self._show_history,
            font=("Arial", 10)
        )
        history_btn.grid(row=0, column=2, padx=2)
        
        # Statistics button
        stats_btn = ctk.CTkButton(
            buttons_frame,
            text="📊 Statistics",
            command=self._show_statistics,
            font=("Arial", 10)
        )
        stats_btn.grid(row=0, column=3, padx=2)
        
        # Export PDF button
        export_btn = ctk.CTkButton(
            buttons_frame,
            text="📄 Export",
            command=self._handle_export,
            font=("Arial", 10)
        )
        export_btn.grid(row=0, column=4, padx=2)
    
    def _create_footer(self):
        """Create the footer section."""
        footer_frame = ctk.CTkFrame(self, fg_color="#1e1e1e")
        footer_frame.grid(row=2, column=0, sticky="ew", padx=0, pady=0)
        footer_frame.grid_columnconfigure(0, weight=1)
        
        footer_label = ctk.CTkLabel(
            footer_frame,
            text="© 2026 AI Math Assistant | Version 1.0",
            font=("Arial", 9),
            text_color="#666666"
        )
        footer_label.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
    
    def _handle_send(self):
        """Handle send button click."""
        user_input = self.input_entry.get().strip()
        
        if not user_input:
            self._show_message("User", "Please enter a question or problem")
            return
        
        # Clear input
        self.input_entry.delete(0, "end")
        
        # Update status
        self._update_status("Processing...")
        
        # Process in background thread
        thread = threading.Thread(target=self._process_input, args=(user_input,))
        thread.daemon = True
        thread.start()
    
    def _process_input(self, user_input: str):
        """
        Process user input and generate response.
        
        Args:
            user_input: The user's input text
        """
        try:
            # Display user message
            self._show_message("You", user_input)
            
            # Try to predict operation
            operation, confidence = self.model.predict(user_input)
            
            self.stats_manager.increment_questions()
            
            # Process based on operation
            response = self._process_operation(user_input, operation, confidence)
            
            # Store in history
            self.history_manager.add_entry(user_input, response, operation, confidence)
            self.stats_manager.add_operation_usage(operation)
            
            # Display response
            self._show_message("Assistant", response)
            
            # Handle low confidence
            if confidence < 0.6:
                self._handle_low_confidence(user_input, operation)
            
            self._update_status("Ready")
        
        except Exception as e:
            logger.error(f"Error processing input: {str(e)}")
            self._show_message("Assistant", f"Error: {str(e)}")
            self._update_status("Error occurred")
    
    def _process_operation(self, user_input: str, operation: str, confidence: float) -> str:
        """
        Process an operation and return result.
        
        Args:
            user_input: Original user input
            operation: Predicted operation
            confidence: Confidence score
            
        Returns:
            Response string
        """
        try:
            # Try to extract numbers from input
            numbers = re.findall(r'-?\d+\.?\d*', user_input)
            
            if operation == 'solve':
                # Try to solve equation
                if '=' in user_input:
                    result = self.solver.solve_linear(user_input)
                    if result['success']:
                        self.stats_manager.increment_equations()
                        steps = '\n'.join(result['steps'])
                        return f"Solution: x = {result['solution']}\n\nSteps:\n{steps}"
                    else:
                        return f"Could not solve equation: {result.get('error', 'Unknown error')}"
            
            elif operation == 'graph':
                # Plot a graph
                if numbers or any(char in user_input for char in ['x', 'sin', 'cos', 'tan']):
                    self.stats_manager.increment_graphs()
                    self.plotter.plot_function(user_input.lower())
                    return "Graph plotted successfully!"
            
            elif len(numbers) >= 2:
                # Process arithmetic operations
                a, b = float(numbers[0]), float(numbers[1])
                self.stats_manager.increment_calculations()
                
                if operation == 'add':
                    result = self.calculator.add(a, b)
                    return f"{a} + {b} = {result}"
                
                elif operation == 'subtract':
                    result = self.calculator.subtract(a, b)
                    return f"{a} - {b} = {result}"
                
                elif operation == 'multiply':
                    result = self.calculator.multiply(a, b)
                    return f"{a} × {b} = {result}"
                
                elif operation == 'divide':
                    if b != 0:
                        result = self.calculator.divide(a, b)
                        return f"{a} ÷ {b} = {result}"
                    else:
                        return "Error: Division by zero!"
                
                elif operation == 'power':
                    result = self.calculator.power(a, b)
                    return f"{a} ^ {b} = {result}"
                
                elif operation == 'modulus':
                    result = self.calculator.modulus(a, b)
                    return f"{a} mod {b} = {result}"
            
            elif len(numbers) >= 1:
                # Single number operations
                a = float(numbers[0])
                self.stats_manager.increment_calculations()
                
                if operation == 'sqrt':
                    result = self.calculator.square_root(a)
                    return f"√{a} = {result}"
                
                elif operation == 'factorial':
                    if a >= 0 and a == int(a):
                        result = self.calculator.factorial(int(a))
                        return f"{int(a)}! = {result}"
                
                elif operation == 'sin':
                    result = self.calculator.trigonometric('sin', a)
                    return f"sin({a}°) = {result:.6f}"
                
                elif operation == 'cos':
                    result = self.calculator.trigonometric('cos', a)
                    return f"cos({a}°) = {result:.6f}"
                
                elif operation == 'tan':
                    result = self.calculator.trigonometric('tan', a)
                    return f"tan({a}°) = {result:.6f}"
                
                elif operation == 'log':
                    result = self.calculator.logarithm(a)
                    return f"log₁₀({a}) = {result:.6f}"
                
                elif operation == 'mean':
                    result = self.calculator.mean(numbers)
                    return f"Mean of {numbers} = {result:.2f}"
                
                elif operation == 'prime':
                    is_prime = self.calculator.is_prime(int(a))
                    return f"{int(a)} is {'prime' if is_prime else 'not prime'}"
            
            # Fallback: evaluate as expression
            try:
                result = self.calculator.evaluate_expression(user_input)
                return f"Result: {result}"
            except:
                return f"I understood '{operation}' but couldn't extract the numbers. Please provide numbers in your input."
        
        except Exception as e:
            logger.error(f"Error processing operation: {str(e)}")
            return f"Error processing operation: {str(e)}"
    
    def _handle_low_confidence(self, user_input: str, predicted_operation: str):
        """
        Handle cases with low confidence predictions.
        
        Args:
            user_input: User's input
            predicted_operation: The predicted operation
        """
        # Ask user for confirmation (in a real app, this would be a dialog)
        logger.info(f"Low confidence prediction for: {user_input}")
        # For now, just log it
    
    def _handle_clear_chat(self):
        """Clear chat history."""
        self.chat_textbox.configure(state="normal")
        self.chat_textbox.delete("1.0", "end")
        self.chat_textbox.configure(state="disabled")
        self._show_message("System", "Chat cleared!")
    
    def _show_history(self):
        """Show chat history in a new window."""
        history = self.history_manager.get_all_history()
        
        if not history:
            self._show_message("System", "No history available")
            return
        
        # Create history window
        hist_window = ctk.CTkToplevel(self)
        hist_window.title("Chat History")
        hist_window.geometry("600x400")
        
        # Create text box
        text_box = ctk.CTkTextbox(hist_window, font=("Arial", 10))
        text_box.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Add history entries
        for entry in history:
            text = f"[{entry['timestamp']}]\n"
            text += f"Q: {entry['question']}\n"
            text += f"A: {entry['answer']}\n"
            text += "-" * 50 + "\n\n"
            text_box.insert("end", text)
        
        text_box.configure(state="disabled")
    
    def _show_statistics(self):
        """Show statistics in a new window."""
        stats = self.stats_manager.get_dashboard_data()
        
        # Create stats window
        stats_window = ctk.CTkToplevel(self)
        stats_window.title("Statistics Dashboard")
        stats_window.geometry("500x600")
        
        # Create frame with statistics
        frame = ctk.CTkScrollableFrame(stats_window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Add stats labels
        stat_items = [
            ("Total Questions", str(stats['total_questions'])),
            ("Total Calculations", str(stats['total_calculations'])),
            ("Most Used Operation", str(stats['most_used_operation'] or 'N/A')),
            ("Graphs Generated", str(stats['graphs_generated'])),
            ("Equations Solved", str(stats['equations_solved'])),
            ("Learned Patterns", str(stats['learned_patterns'])),
            ("Accuracy Rate", str(stats['accuracy_rate'])),
            ("Voice Inputs", str(stats['voice_inputs'])),
            ("Voice Outputs", str(stats['voice_outputs']))
        ]
        
        for label, value in stat_items:
            row_frame = ctk.CTkFrame(frame)
            row_frame.pack(fill="x", padx=10, pady=5)
            
            label_widget = ctk.CTkLabel(row_frame, text=label + ":", font=("Arial", 12, "bold"))
            label_widget.pack(side="left", padx=5)
            
            value_widget = ctk.CTkLabel(row_frame, text=value, font=("Arial", 12), text_color="#00ff00")
            value_widget.pack(side="right", padx=5)
    
    def _handle_export(self):
        """Export chat history."""
        try:
            filename = f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            self.history_manager.export_to_text(filename)
            self._show_message("System", f"History exported to {filename}")
        except Exception as e:
            self._show_message("System", f"Export error: {str(e)}")
    
    def _show_message(self, sender: str, message: str):
        """
        Display a message in the chat area.
        
        Args:
            sender: Who sent the message
            message: The message content
        """
        self.chat_textbox.configure(state="normal")
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {sender}: {message}\n"
        formatted_message += "-" * 50 + "\n"
        
        self.chat_textbox.insert("end", formatted_message)
        self.chat_textbox.see("end")
        self.chat_textbox.configure(state="disabled")
    
    def _update_status(self, status: str):
        """
        Update status bar.
        
        Args:
            status: New status text
        """
        self.status_label.configure(text=status)
        self.update_idletasks()


def run_gui():
    """Run the GUI application."""
    app = MathAssistantApp()
    app.mainloop()


if __name__ == "__main__":
    run_gui()
