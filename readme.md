# 🎮 Complete Guide: Adding Cheats to PPSSPP Emulator

A comprehensive guide to enable, install, and manage cheat codes in the PPSSPP PlayStation Portable emulator using cheat databases and manual methods.

---

## 🚀 Quick Start

**TL;DR:** Enable cheats in PPSSPP settings, download a `cheat.db` file, place it in your cheats folder, then import cheats directly from the in-game menu.

---

## 📋 Table of Contents  

1. [Prerequisites](https://github.com/Zaykus/Cheats-PPSSPP-Emulator?tab=readme-ov-file#-prerequisites)  
2. [Enabling Cheats](https://github.com/Zaykus/Cheats-PPSSPP-Emulator?tab=readme-ov-file#%EF%B8%8F-enabling-cheats)  
3. [Locating Your Cheats Directory](https://github.com/Zaykus/Cheats-PPSSPP-Emulator?tab=readme-ov-file#-locating-your-cheats-directory)  
4. [Method 1: Using Cheat Database (Recommended)](https://github.com/Zaykus/Cheats-PPSSPP-Emulator?tab=readme-ov-file#-method-1-using-cheat-database-recommended)  
5. [Method 2: Manual Cheat Entry](https://github.com/Zaykus/Cheats-PPSSPP-Emulator?tab=readme-ov-file#%EF%B8%8F-method-2-manual-cheat-entry)  
6. [Activating Cheats In-Game](https://github.com/Zaykus/Cheats-PPSSPP-Emulator?tab=readme-ov-file#-activating-cheats-in-game)  
7. [Advanced Management](https://github.com/Zaykus/Cheats-PPSSPP-Emulator?tab=readme-ov-file#%EF%B8%8F-advanced-management)  
8. [Troubleshooting](https://github.com/Zaykus/Cheats-PPSSPP-Emulator?tab=readme-ov-file#-troubleshooting)  
9. [Resources & Downloads](https://github.com/Zaykus/Cheats-PPSSPP-Emulator?tab=readme-ov-file#-resources--downloads)

---

## 🔧 Prerequisites

- **PPSSPP Emulator** (latest version recommended)
- **Game ROM/ISO** files
- Basic file system navigation knowledge

---

## ⚙️ Enabling Cheats

**Step 1:** Configure PPSSPP Settings

1. Launch **PPSSPP**
2. Navigate to `Settings` → `System`
3. Scroll to the **Cheats** section
4. Enable the following options:
   - ✅ **Enable cheats**
   - ✅ **Enable plugins** (recommended for advanced features)
> Example screenshot:

![Enable Cheats in System Settings](/screenshot/1.png)

> **Important:** Both options must be enabled for cheats to function properly.

---

## 📂 Locating Your Cheats Directory

The cheats folder location varies by platform:

### Platform-Specific Paths

| Platform | Default Path |
|----------|--------------|
| **Windows** | `Documents/PPSSPP/PSP/Cheats/` |
| **Android** | `/storage/emulated/0/PSP/Cheats/` |
| **macOS** | `~/Library/Application Support/PPSSPP/PSP/Cheats/` |
| **Linux** | `~/.config/ppsspp/PSP/Cheats/` |

### Alternative Method
If you can't locate the folder:
1. Open PPSSPP
2. Go to `Settings` → `System`
   ```
   PSP Memory Stick
   └── Memory Stick folder "or" Show Memory Stick folder
   ```
> Example screenshot:
![Show Memory Stick folder](/screenshot/5.png)
   
4. The cheats folder will be at `[System Path]/PSP/Cheats/`

**Note:** If the `cheats` folder doesn't exist, create it manually.

---

## 🎯 Method 1: Using Cheat Database (Recommended)

This method provides access to thousands of pre-compiled cheats for most PSP games.

### Step 1: Download Cheat Database

Choose one of these trusted sources:

- **[Cheats-PPSSPP-Emulator Releases](https://github.com/Zaykus/Cheats-PPSSPP-Emulator/releases)** (From this repo)
- **[CWCheat Database Plus+](https://github.com/Saramagrean/CWCheat-Database-Plus-)** (Most comprehensive)
- **[PPSSPP Forums](https://forums.ppsspp.org/showthread.php?tid=3590)** (Community maintained)

### Step 2: Install Database

1. Download the `cheat.db` file
2. Place it in your PPSSPP cheats directory:
   ```
   PPSSPP/
   └── PSP/
       └── Cheats/
           └── cheat.db
   ```

### Step 3: Import Cheats

1. Launch your game in PPSSPP
2. Open the pause menu (typically `Esc` or back button)
3. Select `Cheats`
4. Click `Import from cheat.db`
> Example screenshot:
![Cheat Menu in Game](/screenshot/3.png)
6. PPSSPP automatically finds and imports relevant cheats
7. Toggle desired cheats on/off
8. Resume gameplay

---

## ✏️ Method 2: Manual Cheat Entry

[Using CWCheat Database Editor](#advanced-management)

For custom cheats or when database doesn't have your game.

### Step 1: Generate Cheat File

1. Launch your game in PPSSPP
2. Open pause menu → `Cheats`
3. PPSSPP creates an empty `.ini` file named after the Game ID
   - Example: `ULUS10202.ini` for God of War: Chains of Olympus (USA)

### Step 2: Add Cheat Codes

1. Navigate to your cheats folder
2. Open the `.ini` file with a text editor
3. Add cheats in CWCheat format:

```ini
_S ULUS-10202
_G God of War - Chains of Olympus [USA]
_C0 Infinite Health
_L 0x200xxxxx 0x12345678
_C0 Max Orbs
_L 0x200xxxxx 0x0098967F
```

### CWCheat Format Explanation

- `_S`: Game ID identifier
- `_G`: Game title (optional, for reference)
- `_C0`: Cheat name/description
- `_L`: Cheat code line (address and value)

---

## 🎲 Activating Cheats In-Game

### Standard Activation

1. **Pause the game** (Esc key or pause button)
2. Select **"Cheats"** from the menu
3. **Toggle individual cheats** on/off using checkboxes
4. **Resume game** to see effects

### Managing Active Cheats

- **Green checkmark**: Cheat is active
- **Empty checkbox**: Cheat is inactive
- **Red warning**: Cheat may be incompatible or causing issues

---

## 🛠️ Advanced Management

### Using CWCheat Database Editor

For users who want to customize or create their own cheat databases:

**Recommended Tool:** [CWCheat Database Editor](https://github.com/DragonNeos/cwcheatdb)

**Features:**
- Add new games and cheat codes
- Edit existing cheat descriptions and values
- Remove unwanted entries
- Validate cheat code formatting
- Export custom databases

### Custom Cheat Creation

**Finding Memory Addresses:**
1. Use PPSSPP's built-in debugger
2. Search for specific values (health, money, etc.)
3. Modify values and test
4. Document working addresses for future use

> Example screenshot:

![CWCheat Database Editor v2.0](/screenshot/4.png)

---

## 🔍 Troubleshooting

### Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| **"Import from cheat.db" not appearing** | Ensure `cheat.db` is in the correct folder and cheats are enabled |
| **Cheats not working** | Verify Game ID matches your ROM version (EUR/USA/JPN) |
| **Game crashes with cheats** | Disable problematic cheats one by one to identify conflicts |
| **Empty cheat menu** | Check if your game is supported in the database |

### Game ID Verification

**Finding Your Game's ID:**
1. In PPSSPP, go to `Game Settings`
2. Look for the Game ID (e.g., `ULUS-10202`)
3. Ensure cheat database has matching ID

**Common ID Patterns:**
- `ULUS`: USA releases
- `ULES`: European releases  
- `ULJM`: Japanese releases

### Performance Considerations

- **Some cheats may impact performance** - disable if experiencing slowdowns
- **Save frequently** when using cheats to avoid losing progress
- **Test cheats in non-critical save files** first

---

## 📥 Resources & Downloads

### Essential Downloads

- **📦 [CWCheat Database Plus+](https://github.com/Saramagrean/CWCheat-Database-Plus-)** - Most comprehensive cheat collection
- **🔧 [CWCheat Database Editor](https://github.com/DragonNeos/cwcheatdb)** - Database management tool
- **📋 [PPSSPP Official Site](https://www.ppsspp.org/)** - Latest emulator versions

### Community Resources

- **💬 [PPSSPP Forums - Cheats](https://forums.ppsspp.org/showthread.php?tid=3590)** - Community discussions
- **🔍 [GameFAQs](https://gamefaqs.gamespot.com/)** - Individual game cheat codes
- **📖 [PPSSPP Documentation](https://github.com/hrydgard/ppsspp)** - Technical information

---

## ⚠️ Important Notes

### Best Practices

- **Always backup your save files** before using cheats
- **Test cheats on non-critical saves** first
- **Use cheats responsibly** to maintain game enjoyment

### Legal Disclaimer

- Cheats are for **personal use only**
- Ensure you **legally own** the games you're modifying  
- **Don't distribute** copyrighted game files or proprietary cheat codes
- Some online features may be **disabled** when cheats are active

---

## 🙏 Credits & Acknowledgments

This guide incorporates work and resources from:

- **[Saramagrean](https://github.com/Saramagrean)** - CWCheat Database Plus+ maintenance
- **[DragonNeos](https://github.com/DragonNeos/cwcheatdb)** - CWCheat Database Editor
- **[Pasky13](https://www.brewology.com/)** - Original CWCheat Database Editor V2
- **PPSSPP Development Team** - Emulator development
- **PPSSPP Community** - Cheat sharing and support

---

## 📄 License

This guide is provided under the [MIT License](LICENSE.md) for educational purposes.

**Happy Gaming! 🎮✨**
