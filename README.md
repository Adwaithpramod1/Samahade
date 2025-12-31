# SAMEHADE

SAMEHADE is a Python-based command-line tool built for educational and ethical security testing. It simulates SMS, CALL, and EMAIL traffic to help users understand how communication systems behave under controlled load conditions.

The tool is designed for learning purposes only and focuses on Python concurrency, API-based workflows, and terminal-based application design. SAMEHADE runs smoothly on Termux and Linux environments and provides a simple menu-driven interface for controlled testing scenarios.

## Features
- SMS, CALL, and EMAIL assessment modes
- Multi-threaded execution
- Configurable delay and task count
- Clean terminal interface
- Termux and Linux support

## Requirements
- Python 3.8+
- colorama
- Optional: toilet (for banner display)

## Installation (Termux)
pkg update && pkg upgrade  
pkg install python git toilet  
pip install colorama  

## Usage
python3 samehade.py

Follow the on-screen menu to select a mode and configure options.  
Press CTRL+C to exit safely.

## Project Structure
samehade/
- samehade.py
- utils/
- README.md

## Disclaimer
This tool is intended strictly for educational use. Use it only on systems you own or have explicit permission to test. Unauthorized use is illegal and unethical. The author is not responsible for misuse.

## Author
Adwaith Pramod

Stay legal. Stay ethical.
