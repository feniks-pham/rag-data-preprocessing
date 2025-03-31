import os
from pathlib import Path
from typing import Dict
from dotenv import load_dotenv


def load_env_vars(env_path: str = None) -> Dict[str, str]:
    """
    Load environment variables from .env file.
    
    Args:
        env_path: Path to .env file. If None, will look for .env in project root
        
    Returns:
        Dict[str, str]: Dictionary of environment variables
    """
    if env_path is None:
        # Try to find .env in project root (2 levels up from this file)
        env_path = Path(__file__).parent.parent.parent / '.env'
    
    # Load environment variables
    if not load_dotenv(env_path):
        print(f"⚠️ Warning: No .env file found at {env_path}")
    
    # Get required variables
    required_vars = [
        'LLM_MODEL',
        'EMBEDDING_MODEL',
        'GOOGLE_API_KEY',
        'POSTGRES_USER',
        'POSTGRES_PASSWORD',
        'POSTGRES_DB',
        'POSTGRES_HOST',
        'POSTGRES_PORT'
    ]
    
    env_vars = {}
    for var in required_vars:
        value = os.getenv(var)
        if value is None:
            print(f"⚠️ Warning: Environment variable {var} not found")
        env_vars[var] = value
    
    return env_vars


def get_db_connection_string() -> str:
    """
    Get PostgreSQL connection string from environment variables.
    
    Returns:
        str: PostgreSQL connection string
    """
    env_vars = load_env_vars()
    return (
        f"postgresql://{env_vars['POSTGRES_USER']}:{env_vars['POSTGRES_PASSWORD']}"
        f"@{env_vars['POSTGRES_HOST']}:{env_vars['POSTGRES_PORT']}/{env_vars['POSTGRES_DB']}"
    ) 