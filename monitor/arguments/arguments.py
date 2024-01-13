# On importe la lib argparse
import argparse

# Création d'un objet ArgumentParser
parser = argparse.ArgumentParser()

# On ajoute la gestion de l'option -n ou --name
# "store" ça veut dire qu'on attend un argument à -n

# on va stocker l'argument dans une variable
parser.add_argument("-p", "--port", type=int, default=13337,
                    help="Usage: python bs_server.py [OPTION]..."
                    "Run a server"
                    "Mandatory arguments to long options are mandatory for short options too."
                    "-p, --port                  Specify the port for the server to run on."
                    "                            Ports are integer between 0 and 65535"
                    "                            Ports below 1025 are considered privileged."
                    "-h, --help                  Help of the command"
)
# Permet de mettre à jour notre objet ArgumentParser avec les nouvelles options
# 
if (parser.parse_args()):
    args = parser.parse_args()
else : 
    pass
print(args.port)

if (args.port < 0 or args.port> 65535):
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    sys.exit(1)
elif (args.port >= 0 and args.port<= 1024):
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    sys.exit(2)
