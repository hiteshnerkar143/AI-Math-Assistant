# Quick Start Guide 🚀

Get the AI Math Assistant up and running in 5 minutes!

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected output**: "Successfully installed..." with package list

## 2️⃣ Run Application

```bash
python main.py
```

**Expected output**: GUI window opens with title "AI Math Assistant"

## 3️⃣ Try Your First Math Problem

Type in the input field: `add 5 and 6`

Press Enter or click "📤 Send"

**Expected result**: "5 + 6 = 11"

## 🎯 Feature Quick Links

### Basic Math
```
Input: "multiply 7 times 8"
Result: 7 × 8 = 56
```

### Solve Equations
```
Input: "solve x+5=15"
Result: Solution: x = 10
        [With step-by-step explanation]
```

### Plot Graphs
```
Input: "plot x^2"
Result: [Graph window opens with parabola]
```

### View Statistics
Click the "📊 Statistics" button to see your usage analytics

### Export Conversations
Click the "📄 Export" button to save your chat history

## 📊 Available Operations

| Operation | Example | Result |
|-----------|---------|--------|
| Addition | add 3 and 4 | 7 |
| Subtraction | subtract 10 from 15 | 5 |
| Multiplication | multiply 6 by 7 | 42 |
| Division | divide 20 by 4 | 5 |
| Square Root | square root 16 | 4 |
| Power | 2 to the power of 8 | 256 |
| Factorial | factorial 5 | 120 |
| Mean | mean of 1 2 3 4 5 | 3 |
| Sine | sine 30 | 0.5 |
| Solve | solve x+10=20 | x = 10 |

## 🎮 GUI Controls

| Button | Action |
|--------|--------|
| 📤 Send | Process your input |
| 🗑️ Clear Chat | Clear chat history display |
| 📋 History | View past conversations |
| 📊 Statistics | See usage dashboard |
| 📄 Export | Save conversations as file |

## 🔧 Troubleshooting

### GUI doesn't open
```bash
pip install --upgrade customtkinter
python main.py
```

### Module not found
```bash
pip install -r requirements.txt
```

### Permission denied (Linux/macOS)
```bash
chmod +x main.py
python main.py
```

## 📚 Next Steps

1. **Explore**: Try different math operations
2. **Learn**: Read the README.md for detailed features
3. **Customize**: Modify GUI in `gui/app.py`
4. **Extend**: Add new operations in `utils/calculator.py`
5. **Deploy**: Share your modified version

## 💡 Tips

- Type naturally: "what is 5 plus 6?" instead of just "5+6"
- Use "solve" to solve equations with variables
- Use "plot" to visualize functions
- Check history to see all past interactions
- Export to save important calculations

## 🎓 Learning Path

1. **Basic**: Try arithmetic operations
2. **Intermediate**: Solve equations and plot graphs
3. **Advanced**: Create custom functions in the code
4. **Expert**: Modify ML model for better predictions

## 🐛 Common Issues

| Issue | Fix |
|-------|-----|
| Slow startup | Wait for ML model to initialize (first run only) |
| Graph errors | Ensure matplotlib is installed: `pip install matplotlib` |
| Voice not working | Install system audio libraries (see INSTALLATION.md) |
| Input field empty | Click in the text field before typing |

## 📞 Quick Help

```bash
# View application logs
tail -f app.log

# Test Python installation
python --version

# Check installed packages
pip list

# Reinstall all packages
pip install --force-reinstall -r requirements.txt
```

## 🎯 Use Cases

### Student
- Solve homework problems
- Verify calculations
- Learn step-by-step solutions

### Professional
- Quick calculations
- Data analysis
- Graph visualization

### Developer
- Understand AI implementation
- Learn GUI development
- Study architecture

## ⏱️ Performance Tips

- First run: May take 5-10 seconds (ML training)
- Subsequent runs: Instant startup
- Large expressions: May take 1-2 seconds
- Graph plotting: May take 2-3 seconds

## 🎉 You're All Set!

You're now ready to use the AI Math Assistant. Enjoy exploring all the features!

---

**Need more help?** Check README.md or INSTALLATION.md for detailed information.
