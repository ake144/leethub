class Solution:
    def defangIPaddr(self, address: str) -> str:
        defang = address.replace(".","[.]")
        return defang