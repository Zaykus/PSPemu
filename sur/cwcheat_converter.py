#!/usr/bin/env python3
"""
CWCheat Database to JavaScript Converter
Converts CWCheat database files to JavaScript array format
"""

import re
import os
import json
from typing import List, Dict, Tuple

class CWCheatConverter:
    def __init__(self):
        # Region mapping based on game ID prefixes
        self.region_map = {
            'ULUS': 'USA',
            'ULES': 'EUR', 
            'ULJM': 'JPN',
            'ULJS': 'JPN',
            'UCUS': 'USA',
            'UCES': 'EUR',
            'UCJS': 'JPN',
            'UCAS': 'ASA',
            'NPUH': 'USA',
            'NPEH': 'EUR',
            'NPJH': 'JPN',
            'BCES': 'EUR',
            'BCUS': 'USA',
            'BCJS': 'JPN'
        }
        
        # Common cheat patterns for description generation
        self.cheat_patterns = {
            'health': ['health', 'hp', 'life', 'vitality'],
            'money': ['money', 'cash', 'gil', 'zenny', 'gold', 'coins', 'funds'],
            'ammo': ['ammo', 'ammunition', 'bullets'],
            'items': ['items', 'inventory', 'materials'],
            'experience': ['exp', 'experience', 'xp'],
            'stats': ['stats', 'attributes', 'parameters'],
            'unlock': ['unlock', 'unlock all', 'everything'],
            'infinite': ['infinite', 'unlimited', 'max'],
            'weapons': ['weapons', 'arms', 'equipment'],
            'magic': ['mp', 'magic', 'mana', 'spell']
        }

    def detect_region(self, game_id: str) -> str:
        """Detect region from game ID prefix"""
        if not game_id:
            return "UNK"
        
        # Extract first 4 characters as prefix
        prefix = game_id[:4].upper()
        return self.region_map.get(prefix, "UNK")

    def parse_cwcheat_file(self, file_path: str) -> List[Dict]:
        """Parse CWCheat database file and extract game information"""
        games = []
        current_game = None
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
        except UnicodeDecodeError:
            # Try different encodings
            encodings = ['latin-1', 'cp1252', 'iso-8859-1']
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as file:
                        lines = file.readlines()
                    break
                except UnicodeDecodeError:
                    continue
            else:
                print(f"Could not decode file {file_path}")
                return []

        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#') or line.startswith('//'):
                continue
            
            # Check for game header (game ID and title)
            # Format: _S GAME_ID or _G Game Title
            if line.startswith('_S '):
                # Save previous game if exists
                if current_game:
                    games.append(current_game)
                
                # Extract game ID
                game_id = line[3:].strip()
                current_game = {
                    'id': game_id,
                    'title': '',
                    'cheats': [],
                    'region': self.detect_region(game_id)
                }
                
            elif line.startswith('_G ') and current_game:
                # Extract game title
                current_game['title'] = line[3:].strip()
                
            elif line.startswith('_C') and current_game:
                # Cheat code line - extract cheat name
                # Format: _C0 Cheat Name or _C1 Cheat Name
                cheat_match = re.match(r'_C[01] (.+)', line)
                if cheat_match:
                    cheat_name = cheat_match.group(1).strip()
                    current_game['cheats'].append(cheat_name)
        
        # Don't forget the last game
        if current_game:
            games.append(current_game)
        
        # Filter out games without titles or IDs
        games = [game for game in games if game.get('title') and game.get('id')]
        
        return games

    def generate_cheat_description(self, cheats: List[str]) -> str:
        """Generate a concise description of available cheats"""
        if not cheats:
            return "Various cheats available"
        
        # Count cheat types
        cheat_types = set()
        
        for cheat in cheats[:10]:  # Analyze first 10 cheats to avoid over-processing
            cheat_lower = cheat.lower()
            
            for category, keywords in self.cheat_patterns.items():
                if any(keyword in cheat_lower for keyword in keywords):
                    if category == 'infinite' and any(word in cheat_lower for word in ['health', 'hp', 'life']):
                        cheat_types.add('Infinite Health')
                    elif category == 'infinite' and any(word in cheat_lower for word in ['money', 'cash', 'gil', 'zenny']):
                        cheat_types.add('Max Money')
                    elif category == 'infinite' and 'ammo' in cheat_lower:
                        cheat_types.add('Infinite Ammo')
                    elif category == 'money':
                        cheat_types.add('Max Money')
                    elif category == 'health':
                        cheat_types.add('Infinite Health')
                    elif category == 'items':
                        cheat_types.add('All Items')
                    elif category == 'unlock':
                        cheat_types.add('Unlockables')
                    elif category == 'weapons':
                        cheat_types.add('All Weapons')
                    elif category == 'stats':
                        cheat_types.add('Max Stats')
                    break
        
        if cheat_types:
            return ', '.join(sorted(cheat_types)[:4])  # Limit to 4 types
        else:
            return "Various cheats available"

    def convert_to_javascript(self, games: List[Dict], output_file: str = 'games_database.js'):
        """Convert games data to JavaScript format"""
        
        js_content = "// Game database implementation\nconst games = [\n"
        
        for i, game in enumerate(games):
            title = game['title'].replace('"', '\\"')  # Escape quotes
            game_id = game['id']
            region = game['region']
            cheat_desc = self.generate_cheat_description(game['cheats'])
            cheat_count = len(game['cheats'])
            status = "active"  # Default status
            
            # Generate JavaScript object
            js_line = f'  {{ title: "{title}", id: "{game_id}", region: "{region}", cheats: "{cheat_desc}", cheatCount: {cheat_count}, status: "{status}" }}'
            
            # Add comma except for last item
            if i < len(games) - 1:
                js_line += ","
            
            js_content += js_line + "\n"
        
        js_content += "];\n\n// Export for use in other modules\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = games;\n}"
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(js_content)
        
        print(f"Successfully converted {len(games)} games to {output_file}")
        return js_content

    def process_cwcheat_database(self, input_path: str, output_file: str = 'games_database.js'):
        """Main processing function"""
        print(f"Processing CWCheat database: {input_path}")
        
        if not os.path.exists(input_path):
            print(f"Error: File {input_path} not found!")
            return
        
        # Parse the database
        games = self.parse_cwcheat_file(input_path)
        
        if not games:
            print("No games found in the database!")
            return
        
        print(f"Found {len(games)} games in database")
        
        # Convert to JavaScript
        js_content = self.convert_to_javascript(games, output_file)
        
        # Print summary
        print(f"\nConversion Summary:")
        print(f"- Total games processed: {len(games)}")
        print(f"- Output file: {output_file}")
        print(f"- Regions found: {set(game['region'] for game in games)}")
        
        return js_content

def main():
    """Main function for command line usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert CWCheat database to JavaScript format')
    parser.add_argument('input_file', help='Path to CWCheat database file')
    parser.add_argument('-o', '--output', default='games_database.js', help='Output JavaScript file name')
    parser.add_argument('--preview', action='store_true', help='Show preview of first 5 games')
    
    args = parser.parse_args()
    
    converter = CWCheatConverter()
    
    if args.preview:
        games = converter.parse_cwcheat_file(args.input_file)
        print("Preview of first 5 games:")
        for game in games[:5]:
            print(f"- {game['title']} ({game['id']}) - {len(game['cheats'])} cheats")
        return
    
    converter.process_cwcheat_database(args.input_file, args.output)

if __name__ == "__main__":
    main()

# Example usage:
# converter = CWCheatConverter()
# converter.process_cwcheat_database('cwcheat.db', 'output_games.js')
