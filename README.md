# Vantage

**Vantage** is a scalable, desktop-based payroll application built with **Python**, **Tkinter**, and **SQLite**. Designed to serve small to medium-sized businesses, Vantage can manage payroll operations across up to **300 companies** with features including salary calculations, PDF and XLS report generation, and full employee lifecycle management.

---

## ✨ Features

- 🏢 **Supports up to 300 companies**
- 👩‍💼 **Employee Management** (add, update, delete)
- 💰 **Salary Calculation Engine**
- 📄 **PDF and XLS Report Generation**
- 🏢 **Follows ESI & EPF Compliance**
- 🖥️ **User-Friendly GUI** using Tkinter
- 🗃️ **Local Database Storage** using SQLite

---

## 🛠️ Technologies Used

- `Python 3.13.3` 
- `Tkinter` (GUI)
- `SQLite3` (Database)
- `FPDF` (PDF Generation)
- `xlsxwriter` (XLS Generation)

---

## 🚫 License & Usage

Vantage is **free for personal, non-commercial use only**.  
Distribution, redistribution, or commercial usage of this software is **strictly prohibited**.

> See the [LICENSE](./LICENSE) file for full terms.

---

## ⚠️ Disclaimer

This software is provided **"as is"**, without any warranty of any kind. The author shall not be held liable for any damages or issues arising from the use of this software.

---

## 📦 Installation

1. **Clone the repository:**

```
git clone https://github.com/TheHackerClown/Vantage.git
cd Vantage
```

2. **Install Requirements:**

```
pip install -r requirements.txt
```

3. **Run the App:**

```
python main.py
```

---

## 📦 Build

1. **Clone the repository:**

```
git clone https://github.com/TheHackerClown/Vantage.git
cd Vantage
```

2. **Install Requirements:**

```
pip install -r requirements.txt

#For Windows
Install Microsoft Visual Studio Build Tools

#For Linux
apt/dnf/etc install build-essential

#For Arch
pacman -S base-devel

#For Mac
xcode-select --install
```



3. **Run Nuitka with given arguements:**

```
nuitka --standalone --enable-plugin=tk-inter --lto=yes --follow-imports --show-progress --remove-output --enable-plugin=pylint-warnings main.py
```

4. **Use Executables Generated in main.dist/ folder**

```
main.dist/
├── main.exe       (if compiled for Windows)
├── Python DLLs
├── Dependencies
├── main.bin       (If compiled for Linux)
├── main           (If compiled for Macos)
```


---

## 🙋‍♂️ Author

Dhruv Pratap Singh,
github.com/TheHackerClown
---