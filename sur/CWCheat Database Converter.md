# CWCheat Database Converter

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

> Convert CWCheat database files to JavaScript arrays for modern web applications

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Output Format](#output-format)
- [Use Cases](#use-cases)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🎯 About

CWCheat Converter is a Python utility that transforms CWCheat database files (used for PSP game cheats) into clean, structured JavaScript arrays. Perfect for developers building web applications, game databases, or PSP-related tools.

## ✨ Features

- 🔄 **Automatic Conversion** - Converts entire CWCheat databases (800+ games)
- 🌍 **Region Detection** - Auto-detects game regions from ID prefixes
- 🎮 **Smart Descriptions** - Generates intelligent cheat descriptions
- 📊 **Complete Data** - Extracts titles, IDs, cheat counts, and metadata
- 🛠️ **Multiple Formats** - Supports various CWCheat file formats
- ⚡ **Fast Processing** - Efficiently handles large databases
- 🔧 **CLI Interface** - Easy command-line usage
- 📱 **Web Ready** - Outputs JavaScript ready for web apps

## 📋 Requirements

- Python 3.6 or higher
- CWCheat database file (`.db`, `.txt`, or similar)

## 🚀 Installation

1. **Clone or Download**
   ```bash
   git clone https://github.com/yourusername/cwcheat-converter.git
   cd cwcheat-converter
   ```

2. **Or Download Script**
   - Save `cwcheat_converter.py` to your project folder

## 💻 Usage

### Command Line Interface

```bash
# Basic usage
python cwcheat_converter.py <input_file> [options]
```

### Options

| Option | Description | Example |
|--------|-------------|---------|
| `-o, --output` | Specify output file | `-o games.js` |
| `--preview` | Show first 5 games | `--preview` |
| `-h, --help` | Show help message | `-h` |

### Python Script Usage

```python
from cwcheat_converter import CWCheatConverter

converter = CWCheatConverter()
converter.process_cwcheat_database('cheat.db', 'output.js')
```

## 📖 Examples

### Basic Conversion
```bash
python cwcheat_converter.py cwcheat.db
# Output: games_database.js
```

### Custom Output File
```bash
python cwcheat_converter.py cheat.db -o psp_games.js
# Output: psp_games.js
```

### Preview Database
```bash
python cwcheat_converter.py large_database.db --preview
# Shows: First 5 games with details
```

### Real-World Example
```bash
# Convert PSP cheat database for web project
python cwcheat_converter.py /PSP/GAME/cwcheat/cheat.db -o assets/js/games.js
```

## 📤 Output Format

The converter generates clean JavaScript arrays:

```javascript
// Game database implementation
const games = [
  {
    title: "God of War: Chains of Olympus",
    id: "ULUS-10202",
    region: "USA",
    cheats: "Infinite Health, Max Orbs, Unlockables",
    cheatCount: 15,
    status: "active"
  },
  {
    title: "Monster Hunter Freedom Unite",
    id: "ULUS-10391",
    region: "USA",
    cheats: "Max Zenny, Infinite Items, One Hit Kill",
    cheatCount: 28,
    status: "active"
  }
  // ... hundreds more games
];
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `title` | String | Full game title |
| `id` | String | Game ID (ULUS-XXXXX format) |
| `region` | String | Region code (USA, EUR, JPN, etc.) |
| `cheats` | String | Description of available cheats |
| `cheatCount` | Number | Total number of cheats |
| `status` | String | Game status (active/error) |

## 🎯 Use Cases

### Web Development
```html
<!-- Include in your web project -->
<script src="games_database.js"></script>
<script>
  console.log(`Loaded ${games.length} PSP games`);
  // Build search, filters, etc.
</script>
```

### Database Import
```javascript
// Import to MongoDB
db.games.insertMany(games);

// Import to MySQL
// Convert to SQL INSERT statements
```

### Mobile Apps
```javascript
// React Native / Cordova
import games from './games_database.js';
// Build PSP game browser apps
```

### Data Analysis
```python
# Convert to pandas DataFrame
import pandas as pd
import json

with open('games_database.js', 'r') as f:
    # Extract JSON data and analyze
```

## 🔧 Troubleshooting

### Common Issues

**File Not Found**
```bash
Error: File cheat.db not found!
```
*Solution: Check file path and use absolute path if needed*

**Encoding Issues**
```bash
Could not decode file
```
*Solution: Script auto-handles multiple encodings. File may be corrupted.*

**No Games Found**
```bash
No games found in the database!
```
*Solution: Verify file is valid CWCheat database. Try preview mode.*

**Python Command Not Found**
```bash
python: command not found
```
*Solution: Install Python or try `python3` command*

### File Locations

Common CWCheat database locations:
- **PSP**: `/PSP/GAME/cwcheat/cheat.db`
- **PPSSPP**: `memstick/PSP/GAME/cwcheat/cheat.db`
- **Custom**: Various `.db`, `.txt` files

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/cwcheat-converter.git
cd cwcheat-converter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎮 Supported Regions

| Prefix | Region | Description |
|--------|--------|-------------|
| ULUS | USA | North America |
| ULES | EUR | Europe |
| ULJM | JPN | Japan |
| ULJS | JPN | Japan (Alternative) |
| UCUS | USA | North America (UMD) |
| UCES | EUR | Europe (UMD) |
| NPUH | USA | PSN North America |
| NPEH | EUR | PSN Europe |
| NPJH | JPN | PSN Japan |

## 📊 Statistics

After conversion, you'll see detailed statistics:

```
Processing CWCheat database: cheat.db
Found 847 games in database
Successfully converted 847 games to games_database.js

Conversion Summary:
- Total games processed: 847
- Output file: games_database.js
- Regions found: {'USA', 'EUR', 'JPN', 'ASA'}
```

## 🔗 Related Projects

- [PPSSPP](https://github.com/hrydgard/ppsspp) - PSP Emulator
- [CWCheat](https://cwcheat.pspgen.com/) - Original PSP Cheat System
- [PSP Game Database](https://pspdatacenter.com/) - PSP Game Information

---

**Made with --- quite**

*If this tool helped you, please ⭐ star the repository!*
