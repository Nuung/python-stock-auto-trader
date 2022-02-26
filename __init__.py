
# lib
import os, sys
from dotenv import load_dotenv
load_dotenv()

# module
from core.AutoConnect import auto_conn
from core.EtfAlgoTrader import main

# main
if __name__ == "__main__":
    auto_conn(os.environ.get("ID"), os.environ.get("PWD"), os.environ.get("CERT_PWD"))
    main()