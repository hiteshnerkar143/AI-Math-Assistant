# AI Math Assistant 🤖

A comprehensive AI-powered mathematical assistant with a modern GUI, advanced mathematical operations, equation solving, graph plotting, and voice features. Built with Python, CustomTkinter, scikit-learn, and SymPy.

## 🌟 Features

### Core Features
- **Modern GUI**: Professional dark-themed interface using CustomTkinter
- **AI-Powered**: Machine learning model for natural language understanding using TF-IDF and Naive Bayes
- **Chat Interface**: Conversational interaction style with scrollable history
- **Status Tracking**: Real-time status updates and application feedback

### Mathematical Operations
- **Arithmetic**: Addition, Subtraction, Multiplication, Division, Modulus
- **Advanced Math**: Power, Square Root, Cube Root, Factorial
- **Trigonometry**: Sine, Cosine, Tangent (degrees and radians)
- **Logarithms**: Log (any base), Natural Log
- **Number Theory**: GCD/HCF, LCM, Prime Check, Even/Odd Check
- **Statistics**: Mean, Median, Mode, Standard Deviation
- **Combinatorics**: Permutation, Combination
- **General**: Percentage, Absolute Value

### Equation Solver
- Solves linear and polynomial equations
- Step-by-step solution display
- Solution verification
- Multiple solutions support

### Graph Plotting
- Plot mathematical functions (e.g., x², sin(x), cos(x))
- Support for complex expressions
- Grid, axis labels, and legends
- Separate plot windows
- Parametric equations

### Expression Evaluation
- Evaluate complex expressions: `(5+5)*10`, `sqrt(81)+5`
- Support for SymPy notation
- Error handling for invalid expressions

### Learning System
- Automatic pattern learning from user interactions
- Unknown pattern storage
- Model retraining with new data
- Duplicate prevention
- Learning statistics tracking

### History Management
- View past conversations
- Search functionality
- Export to JSON and text formats
- Timestamp tracking
- Operation categorization

### Statistics Dashboard
- Total questions asked
- Total calculations performed
- Most used operations
- Graphs generated count
- Equations solved count
- Learned patterns count
- Accuracy rate display
- Voice interactions tracking

### Advanced Features
- **Voice Input**: Speak your math problems
- **Voice Output**: Listen to answers
- **PDF Export**: Generate professional reports with ReportLab
- **Responsive Design**: Adapts to different window sizes
- **Error Handling**: Graceful handling of all error cases
- **Logging**: Comprehensive logging for debugging

## 📋 Project Structure

```
AI_Math_Assistant/
│
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── README.md               # This file
│
├── data/
│   ├── training_data.json  # ML training data
│   └── chat_history.json   # Conversation history
│
├── gui/
│   └── app.py             # CustomTkinter GUI implementation
│
├── models/
│   └── ml_model.py        # Scikit-learn ML model
│
├── utils/
│   ├── calculator.py              # Mathematical operations
│   ├── equation_solver.py         # Equation solving
│   ├── graph_plotter.py           # Graph plotting with Matplotlib
│   ├── history_manager.py         # History and persistence
│   ├── learning_manager.py        # Learning system
│   └── statistics_manager.py      # Statistics tracking
│
└── assets/
    └── icon.ico            # Application icon
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download
```bash
cd AI_Math_Assistant
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

Activate virtual environment:
- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Required Packages:**
- customtkinter (GUI framework)
- scikit-learn (Machine learning)
- sympy (Symbolic mathematics)
- matplotlib (Graph plotting)
- numpy (Numerical computing)
- scipy (Scientific computing)
- Pillow (Image processing)
- reportlab (PDF generation)
- SpeechRecognition (Voice input)
- pyttsx3 (Text-to-speech)
- pandas (Data manipulation)

### Step 4: Run Application
```bash
python main.py
```

## 📖 Usage Guide

### Basic Math Operations

#### Addition
```
Input: "add 5 and 6"
Output: 5 + 6 = 11
```

#### Multiplication
```
Input: "multiply 7 and 8"
Output: 7 × 8 = 56
```

#### Square Root
```
Input: "square root 144"
Output: √144 = 12
```

### Equation Solving

#### Linear Equations
```
Input: "solve x+5=15"
Output: Solution: x = 10
         Steps: [detailed step-by-step solution]
```

#### Complex Equations
```
Input: "solve 2*x+10=50"
Output: Solution: x = 20
         [With verification steps]
```

### Graphing

#### Simple Functions
```
Input: "plot x^2"
Output: [Graph window opens with parabola]
```

#### Trigonometric Functions
```
Input: "graph sin(x)"
Output: [Graph window opens with sine wave]
```

### Statistics

#### Mean Calculation
```
Input: "mean of 10, 20, 30"
Output: Mean = 20
```

#### Median and Mode
```
Input: "median 1 2 3 4 5"
Output: Median = 3
```

### Advanced Features

#### View History
- Click "📋 History" button
- See all past questions and answers with timestamps

#### Check Statistics
- Click "📊 Statistics" button
- View dashboard with usage metrics

#### Export Data
- Click "📄 Export" button
- Save conversations as text file with timestamp

#### Clear Chat
- Click "🗑️ Clear Chat" button
- Clears current chat display

## 🤖 Machine Learning Details

### Model Architecture
- **Vectorizer**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Classifier**: Multinomial Naive Bayes
- **Features**: Up to 500 max features with bigrams
- **Training Data**: 70+ labeled mathematical operation examples

### Training Data
The model is trained on labeled examples for operations like:
- Arithmetic operations (add, subtract, multiply, divide)
- Advanced math (power, sqrt, factorial)
- Trigonometry (sin, cos, tan)
- Statistics (mean, median, mode)
- Equation solving
- Graph plotting
- And more...

### Model Performance
- Trained with 70+ examples
- Supports 20+ operation categories
- Confidence scoring for predictions
- Automatic retraining when new patterns learned

### Learning System
When confidence is low (< 60%):
1. System flags uncertain predictions
2. Stores new patterns for retraining
3. Automatically retrains after 5 new patterns
4. Improves accuracy over time

## 🔧 Configuration

### Appearance
Modify in `gui/app.py`:
```python
ctk.set_appearance_mode("dark")  # "light" or "dark"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"
```

### Model Parameters
Modify in `models/ml_model.py`:
```python
Pipeline([
    ('tfidf', TfidfVectorizer(
        max_features=500,  # Adjust feature count
        ngram_range=(1, 2)  # Adjust n-gram range
    )),
    ('clf', MultinomialNB(alpha=1.0))  # Adjust smoothing
])
```

## 📊 Statistics Tracked

- **Total Questions**: Number of queries processed
- **Total Calculations**: Mathematical operations performed
- **Most Used Operation**: Frequently used math operations
- **Graphs Generated**: Number of plots created
- **Equations Solved**: Number of equations resolved
- **Learned Patterns**: New patterns learned by AI
- **Accuracy Rate**: Model prediction confidence average
- **Voice Inputs**: Voice commands processed
- **Voice Outputs**: Spoken responses delivered

## 🎯 Use Cases

### Education
- Math homework assistance
- Concept explanation
- Step-by-step solutions

### Professional
- Quick calculations
- Equation solving
- Data analysis

### Scientific Research
- Expression evaluation
- Graph visualization
- Statistical analysis

### Internship/Portfolio Projects
- Demonstrates ML knowledge
- Shows GUI development skills
- Proves system design ability
- Full production-ready code

## 🐛 Error Handling

The application handles:
- ✓ Division by zero
- ✓ Invalid equations
- ✓ Malformed expressions
- ✓ Negative square roots
- ✓ Invalid factorial inputs
- ✓ Missing input data
- ✓ Graph plotting errors
- ✓ File I/O exceptions
- ✓ Speech recognition failures
- ✓ Voice synthesis errors

All errors are logged and displayed gracefully to the user.

## 📝 Code Quality

### Architecture
- **Object-Oriented Design**: Classes for each module
- **Modular Structure**: Separate concerns into different modules
- **Singleton Pattern**: Single instances of managers
- **Factory Pattern**: Model and manager creation

### Standards
- **Type Hints**: Full type annotations throughout
- **Docstrings**: Complete documentation for all functions
- **Logging**: Comprehensive logging system
- **Comments**: Clear, concise code comments
- **PEP 8**: Follows Python style guidelines

### Testing
- Comprehensive error handling
- Input validation
- Edge case management
- Logging for debugging

## 🚀 Future Improvements

1. **Enhanced UI**
   - Dark/Light theme toggle in GUI
   - Customizable fonts and colors
   - Keyboard shortcuts

2. **Advanced Features**
   - Integration with WolframAlpha API
   - Handwriting recognition
   - Matrix operations
   - Complex number support

3. **Performance**
   - Caching for repeated calculations
   - Async processing for heavy operations
   - GPU acceleration for matrix ops

4. **Deployment**
   - Web interface with Flask
   - Mobile app with Kivy
   - Cloud synchronization

5. **AI Improvements**
   - Deep learning models
   - Multi-language support
   - Better confidence scoring

## 📄 Screenshots

### Main Interface
The application features a professional dark-themed interface with:
- Large chat display area
- Input field with send button
- Quick action buttons (History, Statistics, Export, Clear)
- Status bar showing current state
- Responsive layout

### Features
1. **Chat History**: Scrollable area showing all interactions
2. **Input Area**: Text entry field with send button
3. **Action Buttons**: Quick access to key features
4. **Status Bar**: Real-time application status
5. **Modern Styling**: Professional dark theme with green accents

## 🔐 Security & Privacy

- All data stored locally
- No external API calls for calculations
- Optional voice features can be disabled
- Clean chat history anytime
- No telemetry or tracking

## 📧 Support & Contribution

### Reporting Issues
- Check the `app.log` file for error messages
- Ensure all dependencies are installed
- Try reinstalling requirements

### Future Enhancements
- Fork the repository
- Create feature branches
- Submit pull requests with improvements

## 📜 License

This project is provided as-is for educational and portfolio purposes.

## 👨‍💼 Professional Use

This project is suitable for:
- ✓ **Internship Portfolios**: Shows full-stack development skills
- ✓ **GitHub Portfolio**: Production-ready code with documentation
- ✓ **LinkedIn**: Demonstrates ML, GUI, and system design expertise
- ✓ **Final Year Project**: Comprehensive, well-documented solution
- ✓ **Job Interviews**: Discussing architecture and design decisions

## 🎓 Learning Outcomes

By studying this project, you'll learn:
1. GUI development with CustomTkinter
2. Machine learning with scikit-learn
3. Mathematical programming with SymPy
4. Data persistence with JSON
5. Logging and error handling
6. OOP and design patterns
7. Voice feature integration
8. Professional code organization

## 📚 Technology Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Programming language |
| **CustomTkinter** | Modern GUI framework |
| **scikit-learn** | Machine learning |
| **SymPy** | Symbolic mathematics |
| **Matplotlib** | Graph plotting |
| **ReportLab** | PDF generation |
| **NumPy/SciPy** | Numerical computing |
| **SpeechRecognition** | Voice input |
| **pyttsx3** | Text-to-speech |
| **JSON** | Data storage |

## 🎉 Getting Started

1. **Install Requirements**: `pip install -r requirements.txt`
2. **Run Application**: `python main.py`
3. **Explore Features**: Try different math operations
4. **Check History**: Click History button to see past interactions
5. **View Statistics**: Click Statistics for usage analytics

## 💡 Tips & Tricks

1. **Natural Language**: Ask questions in natural language, not just formulas
2. **Voice Input**: Enable voice for hands-free operation
3. **Export**: Regularly export your chat history
4. **Learning**: The AI learns from your interactions
5. **Graphs**: Use "plot" or "graph" followed by the function

## 🏆 Achievements

This project demonstrates:
- ✓ Full-stack application development
- ✓ Machine learning implementation
- ✓ GUI design and user experience
- ✓ API-like architecture (modular)
- ✓ Professional code standards
- ✓ Production-ready quality
- ✓ Comprehensive documentation
- ✓ Error handling and logging

---

**Version**: 1.0  
**Last Updated**: 2026  
**Status**: Production Ready

For questions or improvements, refer to the code documentation and docstrings throughout the project.
