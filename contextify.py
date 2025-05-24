import os
import argparse
import fnmatch
import mimetypes

def get_text_files(base_path):
    """Recursively find all text-based files in the given directory."""
    text_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Guess the MIME type of the file
            mime_type, _ = mimetypes.guess_type(file_path)
            # Check if the MIME type is text or if it is None (some text files may not have a MIME type)
            if mime_type is None or mime_type.startswith('text'):
                text_files.append(file_path)
    return text_files

def get_file_structure(base_path):
    """Create a visual representation of the file/folder structure."""
    structure = []
    for root, dirs, files in os.walk(base_path):
        level = root.replace(base_path, '').count(os.sep)
        indent = ' ' * 4 * level
        structure.append(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            structure.append(f'{subindent}{f}')
    return '\n'.join(structure)

def read_readme(base_path):
    """Read README.md content if it exists."""
    readme_path = os.path.join(base_path, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

def read_gitignore(base_path):
    """Parse .gitignore file and return list of ignore patterns."""
    gitignore_path = os.path.join(base_path, '.gitignore')
    ignore_patterns = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.append(line)
    return ignore_patterns

def should_ignore(file_path, ignore_patterns, base_path):
    """Check if a file should be ignored based on gitignore patterns."""
    rel_path = os.path.relpath(file_path, base_path)
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(rel_path, pattern):
            return True
    return False

def create_repository_md(base_path):
    """Create repository.md file with README, structure, and code contents."""
    ignore_patterns = read_gitignore(base_path)
    readme_content = read_readme(base_path)
    file_structure = get_file_structure(base_path)
    text_files = get_text_files(base_path)

    with open('repository.md', 'w', encoding='utf-8') as repo_file:
        # Write README.md content
        if readme_content:
            repo_file.write(readme_content + '\n\n')
        
        # Write file structure
        repo_file.write('## File/Folder Structure:\n')
        repo_file.write('```')
        repo_file.write(file_structure + '\n')
        repo_file.write('```\n\n')
        
        # Write code files content
        for file_path in text_files:
            if should_ignore(file_path, ignore_patterns, base_path):
                continue
            repo_file.write(f'## File: {file_path}\n')
            repo_file.write('```\n')
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    repo_file.write(f.read())
            except UnicodeDecodeError:
                repo_file.write(f'[Binary file or encoding error: {file_path}]')
            repo_file.write('\n```')

def main():
    parser = argparse.ArgumentParser(description='Recursively collect code files and create repository.md')
    parser.add_argument('folder', type=str, help='Folder to scan for code files')
    args = parser.parse_args()
    
    if not os.path.exists(args.folder):
        print(f"Error: Folder '{args.folder}' does not exist.")
        return
    
    create_repository_md(args.folder)
    print(f"repository.md created successfully from '{args.folder}'")

if __name__ == '__main__':
    main()
