
# 🕹️ How to Add Cheats to PPSSPP Emulator

This guide explains how to enable and use cheats in the **PPSSPP** emulator, including using a `cheat.db` file to automatically import cheat codes for all games*.

---

## ✅ Step 1: Enable Cheats

1. Open **PPSSPP**.
2. Go to `Settings` → `System`.
3. Scroll down to the **Cheats** section.
4. Enable both:
   - ✅ **Enable cheats**
   - ✅ **Enable plugins**

> Example screenshot:

![Enable Cheats in System Settings](/screenshot/1.png)

---

## 📂 Step 2: Locate the Cheats Folder

1. Open your **PPSSPP** directory.
2. Locate or create the folder named `cheats`
   
   **Common Locations:**
- **Windows:** `Documents/PPSSPP/PSP/Cheats/`
- **Android:** `/storage/emulated/0/PSP/Cheats/`
- **macOS:** `~/Library/Application Support/PPSSPP/PSP/Cheats/`
- **Linux:** `~/.config/ppsspp/PSP/Cheats/`

---

## 🗂️ Step 3: Add Cheat Files

### Option A: Add individual cheat files manually

1. Launch the game in PPSSPP.
2. Open the **pause menu** and select `Cheats`.
3. PPSSPP will create an empty `.ini` file for your game under `cheats/`, named by its Game ID (e.g. `ULUS10202.ini`).
4. Add your cheat codes inside this file in CWCheat format.

---

### ✅ Option B: Use a `cheat.db` file (Recommended)

There is now an easier way to use cheats:

> You can use a `cheat.db` file containing a full database of cheats for many games.

1. Download a `cheat.db` file from sources like:
   - [CWCheat Database Plus+ on GitHub](https://github.com/Saramagrean/CWCheat-Database-Plus-/tree/master)
   - [PPSSPP Forum - Cheats thread](https://forums.ppsspp.org/showthread.php?tid=3590)
2. Place the `cheat.db` file inside your PPSSPP `cheats/` folder:

   ```
   PPSSPP/
   └── cheats/
       └── cheat.db
   ```

---

## 🧠 Step 4: Load Cheats from `cheat.db`

1. Open **PPSSPP**.
2. Launch the game.
3. Press the **pause menu** and click `Cheats`.

> Example screenshot:

![Cheat Menu in Game](/screenshot/3.png)

4. At the top-left, click `Import from cheat.db`.
5. PPSSPP will search for cheats using the game's **Game ID** (like `ULUS10202`), and automatically load them into the `.ini` file.
6. Toggle the cheats you want to activate.
7. Resume your game and enjoy! 🎮

---

## ✅ Tips

- Not all games or versions have cheats in the database. Make sure your ISO version matches the cheat ID (e.g., `ULUS10202` vs `ULES01500`).
- You can manually edit `.ini` files in the `cheats/` folder with a text editor.
- Be cautious: using cheats can cause crashes or bugs in some games.

---

## 📦 Download Section

You can download the required files from the official or community-maintained sources below:

- 📥 **Latest Resource from This Repository**  
  Download the latest version of the `cheat.db` or other resources directly from the [Releases](https://github.com/Zaykus/Cheats-PPSSPP-Emulator/releases) section of this repository.

- 📦 **Original CWCheat Database**  
  Maintained by **Saramagrean**, this is the most comprehensive and up-to-date CWCheat database available:  
  [CWCheat-Database-Plus+ (GitHub)](https://github.com/Saramagrean/CWCheat-Database-Plus-/tree/master)

- 🛠️ **CWCheat Database Editor Tool**  
  Developed by **DragonNeos**, this tool allows you to view and edit `.db` files easily:  
  [CWCheat DB Editor on GitHub](https://github.com/DragonNeos/cwcheatdb)

> ✅ Always respect and credit the work of original authors and maintainers when redistributing or modifying tools and databases.

---

## 🛠️ Advanced: CWCheat Database Editor

For users who want to create, modify, or meticulously manage their `cheat.db` file, a **CWCheat Database Editor** is an invaluable tool. These applications provide a graphical interface to:

- **Add new games and their specific cheat codes.**
- **Edit existing cheat codes** (e.g., change values or descriptions).
- **Remove unwanted cheats** or entire game entries.
- **Ensure correct formatting** of cheat codes before adding them to your `cheat.db`.

This is particularly useful if you're developing your own cheats or want to maintain a highly customized cheat database. You can search online for "CWCheat Database Editor" to find tools like "DragonNeos/cwcheatdb" on GitHub, which are designed for this purpose.

> Example screenshot:

![CWCheat Database Editor v2.0](/screenshot/4.png)

---

## 🔗 Resources

- 📦 CWCheat Database: https://github.com/Saramagrean/CWCheat-Database-Plus-/tree/master  
- 💬 PPSSPP Cheats Forum:
   - https://forums.ppsspp.org/showthread.php?tid=3590
   - https://forums.ppsspp.org/showthread.php?tid=11961
- 🛠️ CWCheat Database Editor: **Original** https://github.com/DragonNeos/cwcheatdb - **Updated Release available** [HERE](https://github.com/Zaykus/Cheats-PPSSPP-Emulator/releases)
- 🎮 PPSSPP repo: https://github.com/hrydgard/ppsspp

---

## 🙌 Credits

This guide includes references and assets from:

- **Pasky13**, the developer of the [CWCheat Database Editor V2.](https://www.brewology.com/downloads/download.php?id=7176&mcid=1)
- The open-source **CWCheat Database Plus+** by [Saramagrean](https://github.com/Saramagrean)
- **CWCheat Database Editor** developed by [DragonNeos](https://github.com/DragonNeos/cwcheatdb)
- Example discussions and cheat sharing from the [PPSSPP official forums](https://forums.ppsspp.org)

All trademarks, game titles, and screenshots used belong to their respective owners.


Enjoy playing !🧨💥

---

## License

This project is licensed under the [MIT License](LICENSE.md).
