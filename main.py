from src.input_manager.console_manager import ConsoleInputManager
from src.viewer.console_viewer import ConsoleViewer
from src.commander.console_commander import ConsoleCommander
from src.commander.list_commands import commands
from src.api.list_apis import apis


def main():
    input_manager = ConsoleInputManager()
    viewer = ConsoleViewer()
    commander = ConsoleCommander(input_manager=input_manager, viewer=viewer)

    for command in commands:
        viewer.show_message(f"{command} - {commands[command]}")

    viewer.show_message(f"Доступные сайты: {' '.join(apis.keys())}")
    commander.run()


if __name__ == "__main__":
    main()
