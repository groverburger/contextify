# Contextify

A lightweight Python script that recursively collects all text-based files from your codebase and consolidates them into a single `repository.md` file, making it easy to provide complete project context to Large Language Models (LLMs).

## Features

- **Recursive file collection**: Automatically discovers all text-based files in your project
- **Smart file detection**: Uses MIME type detection to identify text files instead of relying on predefined extensions
- **Gitignore support**: Respects `.gitignore` patterns to exclude unwanted files
- **Project structure**: Includes a visual tree representation of your project structure
- **README integration**: Automatically includes your project's README.md at the top
- **Single file output**: Consolidates everything into one `repository.md` file for easy LLM upload
- **Error handling**: Gracefully handles binary files and encoding issues

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library modules)

## Installation

Simply download the `contextify.py` script - no installation required!

curl -O https://raw.githubusercontent.com/groverburger/contextify/master/contextify.py

## Usage

python contextify.py /path/to/your/project

The script will create a `repository.md` file in your current directory containing:
1. Your project's README.md (if it exists)
2. Complete file/folder structure
3. Contents of all text-based files (respecting .gitignore)

### Example

python contextify.py ./my-awesome-project
Creates repository.md with your entire codebase

## Why Use This Simple Approach?

While there are more feature-rich tools like [gitingest](https://github.com/cyclotruc/gitingest) available, contextify.py offers several advantages for users who prefer simplicity:

- **Zero dependencies**: No need to install packages or manage virtual environments
- **Easy customization**: Single file that you can quickly modify to fit your specific needs
- **Transparent operation**: Simple, readable code that you can understand and trust
- **Lightweight**: Minimal resource usage and fast execution
- **Portable**: Just copy the script file anywhere and run it

Perfect for developers who want a quick, hackable solution without the overhead of larger tools.

## Customization

The script is designed to be easily modified. Common customizations include:

- Adding specific file extensions to ignore
- Modifying the output format
- Changing the MIME type detection logic
- Adjusting the file structure visualization

## Output Format

The generated `repository.md` follows this structure:

[README.md content if present]
File/Folder Structure:
[Visual tree of your project]
File: [file-path]
[file contents]
File: [another-file-path]
[file contents]
...

## Contributing

This is intentionally kept as a simple single-file script. Feel free to fork and modify for your specific needs!

## License

MIT License - feel free to use, modify, and distribute as needed.
