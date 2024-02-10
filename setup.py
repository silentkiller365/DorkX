from subprocess import call

modules = ["googlesearch-python", "termcolor"]

for module in modules:
    try:
        call(["pip", "install", module])
        print(f"Successfully installed {module}")
    except Exception as e:
        print(f"Error installing {module}: {str(e)}")
