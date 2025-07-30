#!/usr/bin/env python3
import os
import subprocess
import glob

LOCALES = 'zh', 'es', 'fr', 'de'

def get_modified_files():
    """Get list of modified .md files in content/pages from git status."""
    result = subprocess.run(['git', 'status', '--porcelain'], 
                            capture_output=True, text=True, check=True)
    
    modified_files = []
    for line in result.stdout.strip().split('\n'):
        if line.strip():
            # Git status format: "XY filename"
            # We want files that are modified (M) or added (A)
            filename = line.split(maxsplit=1)[1]
            # Check if it's a modified file in content/pages (not in a locale subfolder)
            if filename.startswith('content/pages/') and filename.endswith('.md'):
                # Make sure it's not a translation (no locale in path)
                parts = filename.split('/')                
                if not any(locale in parts for locale in LOCALES):
                    modified_files.append(filename)
    
    return modified_files

def find_translations(original_file):
    """Find all translated versions of a given original file."""
    # Extract the relative path after content/pages/
    relative_path = original_file.replace('content/pages/', '')
    
    # Look for translations in all locale folders
    translations = []
    
    # Get all potential locale directories
    locale_dirs = glob.glob('content/pages/??/')  # Two-letter locale codes
    
    for locale_dir in locale_dirs:
        translated_file = os.path.join(locale_dir, relative_path)
        if os.path.exists(translated_file):
            translations.append(translated_file)
    
    return translations

def main():
    print("🔍 Checking for modified files in content/pages...\n")
    
    modified_files = get_modified_files()
    
    if not modified_files:
        print("No modified .md files found in content/pages")
        return
    
    print(f"Found {len(modified_files)} modified file(s):")
    for file in modified_files:
        print(f"  📝 {file}")
    
    print("\n🌍 Finding translated versions...\n")
    
    files_to_delete = []
    for original in modified_files:
        translations = find_translations(original)
        if translations:
            print(f"Original: {original}")
            print("Translations found:")
            for trans in translations:
                print(f"  🗑️  {trans}")
                files_to_delete.append(trans)
            print()
    
    if not files_to_delete:
        print("No translated versions found for the modified files.")
        return
    
    print(f"\n⚠️  Total files to be deleted: {len(files_to_delete)}")
    print("\nThe following files will be deleted:")
    for file in sorted(files_to_delete):
        print(f"  {file}")
    
    # Ask for confirmation
    confirm = input("\n❓ Do you want to proceed with deletion? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        print("\n🗑️  Deleting files...")
        deleted_count = 0
        for file in files_to_delete:
            try:
                os.remove(file)
                print(f"  ✅ Deleted: {file}")
                deleted_count += 1
            except Exception as e:
                print(f"  ❌ Error deleting {file}: {e}")
        
        print(f"\n✨ Successfully deleted {deleted_count} file(s)")
    else:
        print("\n❌ Deletion cancelled.")

if __name__ == "__main__":
    main()
