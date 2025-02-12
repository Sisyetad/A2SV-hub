# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill)-1
        target = skill[l] + skill[r]
        chem = 0
        while(l < r):
            chem += (skill[l] * skill[r])
            l+=1
            r-=1
            if(target != skill[l] + skill[r]):
                return -1

        return chem