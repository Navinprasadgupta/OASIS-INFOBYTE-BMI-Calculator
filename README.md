# OASIS-INFOBYTE-BMI-Calculator



# 🧮 BMI Calculator – Python Project

This project demonstrates how to build a **BMI (Body Mass Index) Calculator** in Python for both **beginners** (CLI-based) and **advanced users** (GUI + data visualization). It allows users to calculate their BMI, interpret the result, and track health over time.

---

## 🎯 Objective

To calculate and classify BMI using Python through two versions:
- A **Command-Line Interface (CLI)** version for beginners
- A **Graphical User Interface (GUI)** version for advanced users with trend visualization and data storage

---

## 🟢 Beginner: CLI BMI Calculator

### 🔧 Features
- Prompts user for weight (kg) and height (m)
- Calculates BMI using: `BMI = weight / height²`
- Categorizes BMI into:
  - Underweight (BMI < 18.5)
  - Normal (18.5 ≤ BMI < 24.9)
  - Overweight (25 ≤ BMI < 29.9)
  - Obese (BMI ≥ 30)
- Validates input and handles errors gracefully

### ▶️ How to Run
```bash
python bmi_calculator_cli.py
```

---

## 🔵 Advanced: GUI BMI Calculator with Data Tracking (Optional)

### 🖥️ Features
- GUI using **Tkinter** or **PyQt**
- Input fields for height & weight
- Displays BMI result and category
- Save data to CSV or SQLite database
- Show historical BMI trends using **Matplotlib**
- Support for multiple users

---

## 📁 Project Structure

```
BMI-Calculator/
├── bmi_calculator_cli.py         # CLI version
├── bmi_gui.py                    # GUI version (optional)
├── bmi_data.csv                  # Optional storage
├── README.md                     # Project documentation
└── assets/                       # Charts / UI designs (optional)
```

---

## 📊 Example Output (CLI)
```
Welcome to the BMI Calculator!
Enter your weight in kilograms: 70
Enter your height in meters: 1.75

Your BMI is: 22.86
Health Category: Normal weight
```

---

## 🧠 Key Concepts and Challenges

| Concept                | Description                                                   |
|------------------------|---------------------------------------------------------------|
| Input Validation       | Check user input and avoid crashes from invalid entries       |
| BMI Formula            | BMI = weight / (height × height)                             |
| Categorization         | Use standard WHO ranges for health classification            |
| GUI Design (Advanced)  | Create intuitive interface for input and output               |
| Data Storage (Advanced)| Store user history for trend analysis                         |
| Visualization          | Plot BMI trends using line/bar charts                         |

---

## ⚠️ Error Handling
- Checks if weight and height are positive numbers
- Handles non-numeric input gracefully
- In GUI: alerts for missing fields or zero/negative entries

---

## 👨‍💻 Author

**Name:** Navin prasad gupta  
**Domain:** Python Developer  
**Education:** Diploma – DSEU  
**Skills:**  
- Python Programming  
,

**GitHub:** [https://github.com/Navinprasadgupta
**LinkedIn:** [https://www.linkedin.com/in/navin-prasad-gupta-b3a382372/ 
---

## 📘 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and share for educational purposes.

---

## 🙌 Contributions & Feedback

Suggestions, improvements, and pull requests are welcome!
