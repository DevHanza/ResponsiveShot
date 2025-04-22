<div align="center">
    <img src="https://go-skill-icons.vercel.app/api/icons?i=python"/>
    <img height="48" src="https://github.com/user-attachments/assets/409b0d4f-bbe3-4f56-b3c3-ad61ffaa362a"/>
    <img src="https://go-skill-icons.vercel.app/api/icons?i=javascript"/>
</div>

<div align="center">
  
  <h1>ResponsiveShot</h1>
  <h4>Responsive Website Screenshot Capture Tool 📸</h4>
  <p>This Python app uses Playwright to capture full-page screenshots of a website across multiple devices: iPhone 12 Pro, iPad Mini, and Desktop Chrome.</p>
</div>  

### 🛠️ Requirements

Before running the app, make sure you have:
- Python 3.7+
- Playwright

### ⚙️ Installation

```
pip install playwright
playwright install
```

🚀 How to Use
Clone this repository or download the script.

Run the script in your terminal:

```
python main.py
```
When prompted, enter the full URL of the website you want to capture (e.g., https://google.com).

### ✅ Features
- Emulates multiple devices
- Full-page screenshots with JavaScript and animation handling
- Automatically saves screenshots into a timestamped folder
- Simple terminal interface


### The tool will:

- Launch a Chromium browser (Behind the scenes)
- Emulate different devices
- Visit the website and scroll to the bottom
- Save screenshots into a folder like screenshots/22-04-2025__02-35-12PM/

### 📁 Output
Captured screenshots will be stored under the screenshots/ directory in a timestamped folder like this:

```
screenshots/
└── 22-04-2025__02-35-12PM/
    ├── iPhone_12_Pro.png
    ├── iPad_Mini.png
    └── Desktop_Chrome.png
```

### 🗒️ Notes
- You can modify the list of devices in the devices array inside the script.
- Customize viewport or zoom settings for Desktop as needed.

#### _Please rate with a ⭐ if you found this useful._