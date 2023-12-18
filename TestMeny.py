import argparse
import subprocess
def do_command_1():
    subprocess.run(["python", "oppgaveH.py"])
def do_command_2():
     raise SystemExit

parser = argparse.ArgumentParser( 

    prog= "menyTestForCliOppgave",
    description= "test for Cli oppgave",
    epilog= "slutt på test",
    argument_default=None,
    add_help=True)

parser = argparse.ArgumentParser(description="Bildebehandling")

parser.add_argument("commando",
    action="store",
    nargs="1",
    default="None",
    choices=["1," "2"],
    required="True",
    help="trykk  1 for meny eller 2 for å avslutte")

args = parser.parse_args()

if args.command == "1":
    do_command_1()
  
elif args.command == "2":
   do_command_2()