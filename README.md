# 🎵 Media Player Desktop-App

A _device-downloadable_ desktop audio application engineered to _run completely offline_ and independently on each user's machine, with zero cloud or server dependencies, that runs independently on individual devices with zero cloud dependencies. It automates local file caching into a permanent native directory vault (app_music_library) and compiles into a standalone, zero-dependency executable (.exe) for direct client-side execution.

From Design to deploy a standalone desktop media library application utilizing Python and the Tkinter GUI framework, focused on localized data persistence. Engineered an automated filesystem pipeline using low-level OS and Shutil modules to manage a dedicated runtime directory (app_music_library), eliminating redundant user I/O operations. 

---

## Key Features

* **Persistent Local Library:** Automatically builds an internal storage vault (`app_music_library`) to preserve your music tracks across sessions.
* **Frictionless File Importing:** Allows one-click file copying directly from your Downloads or local directories straight into the app's permanent ecosystem.
* **Zero-Dependency Execution:** Compiled into a standalone executable (`.exe`) file—users can download and run it instantly without installing Python, Pygame, or any external dependencies.
* **Dynamic UI Feedback:** Built-in live tracking labels to monitor play, pause, stop, and file import success states inside a modern dark-mode aesthetic.
* **Run Completely Offline:** no required any dependencies or internet, it runs on independent device.

---

## 🛠️ Technology Stack

| Technology / Library | Purpose |
| :--- | :--- |
| **Python** | Core application programming language |
| **Tkinter** | Native Desktop Graphical User Interface (GUI) layout engine |
| **Pygame (Mixer)** | High-fidelity hardware audio loading and playback system |
| **Shutil & OS** | Low-level operating system file management and system copy logic |
| **PyInstaller** | Hard-compilation deployment tool for bundling the app into a single `.exe` |

---

## 📂 File Structure

The project repository maintains a highly modular and organized structural design:

```text
Music-Player-App/
│
├── app_music_library/     # Automated local directory where imported audio files are permanently saved
├── .gitignore             # Strict configuration ensuring build binary/music files are kept out of Git tracking
├── music_player.py        # Main Python source code architecture containing logic & UI bindings
└── README.md              # Project documentation, setup roadmap, and deployment manual
└── License 

```

## Download & Installation Roadmap
You don't need to install any programming languages or command-line interfaces to use this app. Follow these straightforward steps to run the software directly on your machine:

## Step 1: Download the Application
* Head to the right-hand sidebar of this repository page and click on Releases.

* Locate the Assets dropdown under the latest stable build version (v1.0.0).

* Click on music_player.exe to download the standalone app directly to your device.

## Step 2: Launch and Handle Windows Protections
* Navigate to your computer's Downloads folder and double-click music_player.exe.

### Note on Windows SmartScreen: Because this app is built by an independent developer, Windows may display a blue warning box stating "Windows protected your PC".

* Simply click "More Info" on that popup, and then click the "Run Anyway" button. The app will open safely and immediately.

## 🎵 Step 3: Start Listening
* Click the green ➕ Import Single Song File to Library button.

* Select any audio track (such as an .mp3 or .aac file) from your device.

* The application will automatically duplicate it into your permanent directory layout. Double-click the song name in the app menu to start playing!

***
## 👩‍💻 Developer Roadmap: Cloning & Local Execution


### 📋 Prerequisites
Before starting, ensure you have the following installed on your local machine:
* **Python 3.8 or higher** (Make sure to check the box that says *"Add Python to PATH"* during installation).
* **Git** installed on your system.

### 🛠️ Local Setup Setup Step-by-Step

#### Step 1: Clone the Repository
Open your terminal (Command Prompt, PowerShell, or Git Bash) and run the following command to clone this project to your local machine:
```bash
git clone [https://github.com/Butkii025/Music_Player_App.git](https://github.com/Butkii025/Music_Player_App.git)
```
#### Step 2: Navigate into the Project Directory
```
cd Music-Player-App
```
#### Step 3: Install Required Dependencies
```
pip install pygame
```
#### Step 4: Run the Application
```
python music_player.py
```
***
## Visual
<img width="74" height="92" alt="Screenshot 2026-06-14 000005" src="https://github.com/user-attachments/assets/2ec6a6d1-b6ef-4bc1-a970-0d3b599b8718" /><br/><br/><br/>
<img width="333" height="432" alt="Screenshot 2026-06-13 190026" src="https://github.com/user-attachments/assets/b012c62a-8821-4321-b58a-18bc0fa98b8a" />

***
##  Built & Developed By
Developer: [Priyanshu Vijay](https://p-vijay.vercel.app/)

Role: Software/Machine Learning Engineer

### Purpose: 
Developed as an open-source tool showcasing native desktop GUI design patterns, automated operating system directory manipulation, and clean binary distribution frameworks.

## 📝 License
This project is open-source and available under the MIT License  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](/LICENSE)


***
