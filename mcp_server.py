import json
import sys
from client import VCGAuctionEngine

vcg = VCGAuctionEngine()

def handle_rpc(line):
    try:
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        rid = req.get("id")
        
        if method == "tools/list":
            tools = [
                {"name": "submit_bid", "description": "Submit valuation bid for items"},
                {"name": "resolve_auction", "description": "Resolve VCG auction for given item"}
            ]
            return json.dumps({"jsonrpc": "2.0", "id": rid, "result": {"tools": tools}})
        elif method == "tools/call":
            tname = params.get("name")
            args = params.get("arguments", {})
            if tname == "submit_bid":
                vcg.submit_bid(args["bidder"], args["valuations"])
                return json.dumps({"jsonrpc": "2.0", "id": rid, "result": {"status": "bid_recorded"}})
            elif tname == "resolve_auction":
                w, p = vcg.resolve_single_item(args["item_id"])
                return json.dumps({"jsonrpc": "2.0", "id": rid, "result": {"winner": w, "payment": p}})
    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}})

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(handle_rpc(line.strip()), flush=True)
