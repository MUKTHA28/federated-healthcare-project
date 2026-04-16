import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clients.client1 import client_train as c1
from clients.client2 import client_train as c2
from clients.client3 import client_train as c3

from server.federated import federated_average
from server.security import encrypt_weights

def run_server():

    print("🔵 Running Federated Server...\n")

    # Get weights from clients
    w1 = c1("data/hospital1.csv")
    w2 = c2("data/hospital2.csv")
    w3 = c3("data/hospital3.csv")

    print("\nCollected weights from all clients ✅")

    # Federated Averaging
    global_coef, global_intercept = federated_average([w1, w2, w3])

    print("\nGlobal Model Created ✅")
    print("Global Weights:", global_coef)

    # Security
    secure_hash = encrypt_weights(global_coef, global_intercept)

    print("\n🔐 Security Hash:", secure_hash)

    return global_coef, global_intercept


if __name__ == "__main__":
    run_server()
