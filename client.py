class VCGAuctionEngine:
    """
    Vickrey-Clarke-Groves (VCG) Mechanism.
    Maximizes social welfare while charging bidders the externality they impose on other agents.
    """
    def __init__(self):
        self.bids = {}

    def submit_bid(self, bidder_id, item_valuations):
        """item_valuations is a dict of item_id -> bid value."""
        self.bids[bidder_id] = item_valuations

    def resolve_single_item(self, item_id):
        item_bids = []
        for bidder, vals in self.bids.items():
            if item_id in vals:
                item_bids.append((bidder, vals[item_id]))

        if not item_bids:
            return None, 0.0

        item_bids.sort(key=lambda x: x[1], reverse=True)
        winner, win_val = item_bids[0]
        # VCG payment equals the externality (the second highest bid)
        payment = item_bids[1][1] if len(item_bids) > 1 else 0.0
        return winner, payment
