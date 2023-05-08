class Solution:
    def defangIPaddr(self, address: str) -> str:
        st=""
        l=len(address)
        for i in range (l):
            if (address[i]=="."):
                st=st+"[.]"
            else:
                st=st+address[i]
        return (st)

                