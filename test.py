import argparse
import subprocess

parser = argparse.ArgumentParser(
    prog="menyTestForCliOppgave",
    description="Test for CLI oppgave",
    epilog="Slutt på test",
    add_help=True
)

parser = argparse.ArgumentParser(description="Bildebehandling")

parser.add_argument("command",
    choices=["1", "2"],
    help="Velg kommando: 1 for oppgaveA.py, 2 for avslutte")

args = parser.parse_args()

if args.command == "1":
    subprocess.run(["python", "oppgaveH.py"])
elif args.command == "2":
    raise SystemExit
else:
    print("Ugyldig kommando valgt")
