# 🧮 Advanced Python Calculator Application

A powerful, extensible command-line calculator that supports **arithmetic operations, calculation history management, and plugin integration**. Designed with **Pandas for data handling**, **professional logging**, and **scalable architecture**.

---

## 📌 Table of Contents
- [🧮 Advanced Python Calculator Application](#-advanced-python-calculator-application)
  - [📌 Table of Contents](#-table-of-contents)
  - [🚀 Project Overview](#-project-overview)
  - [🔧 Core Functionalities](#-core-functionalities)
  - [🔌 Plugin System](#-plugin-system)
  - [📜 Calculation History Management (with Pandas)](#-calculation-history-management-with-pandas)
  - [📊 Advanced Data Handling with Pandas](#-advanced-data-handling-with-pandas)
  - [📝 Professional Logging Practices](#-professional-logging-practices)
  - [🏗️ Scalable Architecture with Design Patterns](#️-scalable-architecture-with-design-patterns)
  - [✅ Testing and Code Quality](#-testing-and-code-quality)
  - [📝 Documentation](#-documentation)
  - [🎥 Video Showcase](#-video-showcase)
  - [📥 Cloning the Repository](#-cloning-the-repository)

---

## 🚀 Project Overview
The **Advanced Python Calculator** provides a **command-line interface (REPL)** for performing arithmetic operations, managing calculation history, and dynamically integrating plugins for extended functionality. It employs **Pandas for advanced data handling** and **logging for professional-grade application tracking**.

---

## 🔧 Core Functionalities
This application features a **REPL (Read-Eval-Print Loop)** that supports:
✅ **Arithmetic Operations:** Addition, subtraction, multiplication, and division.  
✅ **History Management:** Show, save, clear, and delete history entries.  
✅ **Extensibility:** Integrate dynamically loaded plugins for enhanced features.  

---

## 🔌 Plugin System
The calculator follows a **modular plugin system**, allowing seamless **integration of new commands or features**:
🔹 **Dynamically load and integrate plugins** without modifying the core application.  
🔹 **View available plugins using a menu command** inside the REPL.  

---

## 📜 Calculation History Management (with Pandas)
The **calculation history is managed using Pandas**, enabling:  
📂 **Loading and displaying history from a CSV file.**  
💾 **Saving the current history to a CSV file.**  
🗑️ **Clearing or deleting specific history entries,** with real-time updates in the CSV file.  

---

## 📊 Advanced Data Handling with Pandas
Pandas is leveraged for:
🔹 **Efficient reading/writing of calculation history to CSV files.**  
🔹 **Ensuring robust and scalable data management.**  

---

## 📝 Professional Logging Practices
A **comprehensive logging system** is implemented to track:
✅ **Detailed application operations and data manipulations.**  
⚠️ **Warnings and errors for debugging.**  
📌 **Log messages with different severity levels (INFO, WARNING, ERROR).**  

The logging system is configurable via **environment variables**, allowing customization of logging levels and output destinations.

---

## 🏗️ Scalable Architecture with Design Patterns
The calculator employs **industry-standard design patterns** for better **scalability and maintainability**:
- **🎭 Facade Pattern:** Simplifies complex Pandas data manipulations.
- **📝 Command Pattern:** Structures REPL commands for efficient execution.
- **🏭 Factory Method, Singleton, and Strategy Patterns:** Enhances modularity, flexibility, and reusability.

---

## ✅ Testing and Code Quality
📌 **Minimum 93% test coverage** using **Pytest**.  
📌 Code quality adheres to **PEP 8 standards**, validated using **Pylint**.  

---

## 📝 Documentation
This `README.md` serves as **comprehensive documentation**, covering:
📌 **Setup instructions & usage examples.**  
📌 **Design patterns and logging strategies implemented.**  
📌 **Project architecture and decision-making process.**  

---

## 🎥 Video Showcase
A detailed **video showcase** of this calculator application is available!  
▶️ **[Watch the Video Here]("googledrivelink")**.

---

## 📥 Cloning the Repository
To **clone the repository**, run the following command:
```bash
git clone https://github.com/your-username/calculator-app.git
