import os
import sys
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "apps"))) # Add this line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
    print(sys.path)