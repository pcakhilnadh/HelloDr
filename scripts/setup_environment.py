"""
Environment setup script for HelloDr project.
Run this script to initialize your development environment.
"""

import os
import sys
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True


def create_env_file():
    """Create environment file template."""
    env_content = """# Environment variables for HelloDr project
# Copy this to .env and fill in your actual values

# API Keys
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACE_TOKEN=your_huggingface_token_here

# Database URLs (if needed)
DATABASE_URL=sqlite:///data.db

# Other configurations
PYTHONPATH=./src
"""
    
    env_file = Path(".env.template")
    with open(env_file, 'w') as f:
        f.write(env_content)
    
    print(f"✅ Created {env_file}")
    print("💡 Copy .env.template to .env and fill in your API keys")


def check_directories():
    """Verify all required directories exist."""
    required_dirs = [
        "data/raw", "data/interim", "data/processed", "data/external",
        "notebooks/exploratory", "notebooks/modeling", "notebooks/rag",
        "src/data", "src/features", "src/models", "src/rag", "src/utils",
        "models", "reports/figures", "reports/documents",
        "config", "tests", "scripts"
    ]
    
    missing_dirs = []
    for directory in required_dirs:
        if not Path(directory).exists():
            missing_dirs.append(directory)
    
    if missing_dirs:
        print(f"❌ Missing directories: {missing_dirs}")
        return False
    
    print("✅ All required directories exist")
    return True


def main():
    """Main setup function."""
    print("🚀 Setting up HelloDr Data Science Project...")
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check directories
    if not check_directories():
        print("💡 Run the directory creation commands from the README")
        return
    
    # Create environment file
    create_env_file()
    
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print("1. Create a virtual environment: python -m venv venv")
    print("2. Activate it: venv\\Scripts\\activate (Windows) or source venv/bin/activate (Unix)")
    print("3. Install dependencies: pip install -r requirements.txt")
    print("4. Copy .env.template to .env and fill in your API keys")
    print("5. Add your dataset to data/raw/")
    print("6. Start with notebooks/exploratory/01_data_exploration.ipynb")


if __name__ == "__main__":
    main() 