from client_server.constants import PORT
from threading import Thread
from client_server import Server, Client
from time import sleep
import sys
import getopt
from distutils.util import strtobool
def main(argv):
    f_node = True
    host = '127.0.0.1'
    port = 57600
    try: 
        opts, args = getopt.getopt(argv, "hf:host:p",["f_node=","host=", "port="])
    except getopt.GetoptError as error:
        print('peer2peer.py -f <fullnode: bool> -host <host: string> -p <port: int>')
        print(error)
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print('peer2peer.py -f <fullnode: bool> -h <host: string> -p <port: int>')
        elif opt in ("-f"):
            f_node = bool(strtobool(arg))
        elif opt in ("-h"):
            host = arg
        elif opt in ("-p"):
            port = arg
                
    threads = [None] * 2
        

        
    if f_node: threads[0] = Thread(target=Server, args=(host, port))

    threads[1] = Thread(target=Client, args=(host, port))

    for thread in range(len(threads)): 
        if threads[thread]:
            threads[thread].start()
            if thread == 0:
                sleep(2)

if __name__ == "__main__":
    main(sys.argv[1:])