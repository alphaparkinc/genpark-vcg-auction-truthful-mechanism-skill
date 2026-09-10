import sys
from client import VCGAuctionEngine

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

def run():
    print(">>> Demonstrating VCG Truthful Mechanism...")
    vcg = VCGAuctionEngine()
    vcg.submit_bid("Agent_A", {"compute_node_1": 150.0})
    vcg.submit_bid("Agent_B", {"compute_node_1": 120.0})
    vcg.submit_bid("Agent_C", {"compute_node_1": 90.0})

    winner, payment = vcg.resolve_single_item("compute_node_1")
    print(f"Auction Winner: {winner}, VCG Payment: {payment}")
    assert winner == "Agent_A"
    assert payment == 120.0
    print("[PASS] VCG Truthful Mechanism verified.")

if __name__ == "__main__":
    run()
