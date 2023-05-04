class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_senators = []
        dire_senators = []
        n = len(senate)

        # Divide the senators into two parties
        for i in range(n):
            if senate[i] == 'R':
                radiant_senators.append(i)
            else:
                dire_senators.append(i)

        while radiant_senators and dire_senators:
            if radiant_senators[0] < dire_senators[0]:
                # Radiant senator bans Dire senator's right
                dire_senators.pop(0)
                radiant_senators.append(radiant_senators.pop(0) + n)
            else:
                # Dire senator bans Radiant senator's right
                radiant_senators.pop(0)
                dire_senators.append(dire_senators.pop(0) + n)

        return "Radiant" if radiant_senators else "Dire"
