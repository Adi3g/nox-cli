from __future__ import annotations

import os
import subprocess

import click


class NoxInitializer:
    def __init__(self, shell: str) -> None:
        self.shell = shell
        self.completion_script_path = os.path.expanduser(
            f"~/.nox-complete-{shell}.sh",
        )
        self.rc_file = self.get_rc_file()

    def get_rc_file(self) -> str:
        """Get the appropriate rc file based on the shell."""
        if self.shell == 'bash':
            return os.path.expanduser('~/.bashrc')
        elif self.shell == 'zsh':
            return os.path.expanduser('~/.zshrc')
        elif self.shell == 'fish':
            return os.path.expanduser('~/.config/fish/config.fish')
        else:
            raise ValueError(f"Unsupported shell: {self.shell}")

    def generate_completion_script(self) -> None:
        """Generate the auto-completion script for the specified shell."""
        if self.shell == 'fish':
            self.completion_script_path = os.path.expanduser(
                f"~/.config/fish/completions/nox.{self.shell}",
            )

        command = f"python {
            __file__
        } completion --shell {self.shell} > {self.completion_script_path}"
        subprocess.run(command, shell=True, check=True)
        click.echo(
            f"Auto-completion script generated at:{
                self.completion_script_path
            }",
        )

    def update_rc_file(self) -> None:
        """Update the rc file to source the completion script."""
        source_command = f"source {self.completion_script_path}"

        if self.shell == 'fish':
            # Fish does not use rc files in the same way, so no need to update
            return

        # Add the source command to the shell's rc file if it's not exist
        with open(self.rc_file, 'a+') as file:
            file.seek(0)
            content = file.read()
            if source_command not in content:
                file.write(f"\n# Nox CLI auto-completion\n{source_command}\n")

        click.echo(f"""Auto-completion setup complete.
                   Please run 'source {self.rc_file}' to reload
                   your shell configuration.""")
