from multiprocessing.pool import ThreadPool
from socket import AF_INET, SOCK_STREAM, socket
from tqdm import tqdm


def test_port_number(host, port):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.settimeout(5)
        try:
            sock.connect((host, port))
            return True
        except:
            return False

# scan ports in single thread
def port_scan(host, ports):
    print(f"Scaning {host}")
    for port in tqdm(ports):
        if test_port_number(host, port):
            print(f"> {host}:{port} open")

# scan ports in multithreads
def port_scan(host, ports):
    print(f"Scaning {host}")
    with ThreadPool(len(ports)) as pool:
        args = ((host, port) for port in ports)
        results = pool.starmap(test_port_number, args)
        for port, is_open in zip(ports, results):
            if is_open:
                print(f"> {host}:{port} open")


if __name__ == "__main__":
    host = 'python.org'
    ports = range(1024)
    port_scan(host, ports)