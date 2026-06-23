class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n% groupSize != 0:
            return False

        count = Counter(hand)
        for card in sorted(count.keys()):
            freq = count[card]

            if freq > 0:
                for nextcard in range(card,card + groupSize):
                    if count[nextcard] < freq:
                        return False
                    count[nextcard] -= freq

        return True