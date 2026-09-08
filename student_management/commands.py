
import click
@click.command("hello-app")

def hello_app():
    print("Hello from the custom Bench CLI!")

commands=[hello_app]