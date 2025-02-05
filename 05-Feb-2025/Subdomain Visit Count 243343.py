# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        List_domains = []
        domain_map = {}
        for pair in cpdomains:
            List_domains.append(pair.split())
        for domain in List_domains:
            domain[1] = domain[1].split('.')
            for i in range(1,len(domain[1]) + 1):
                sub_domain = ".".join(domain[1][-i:])
                if sub_domain in domain_map:
                    domain_map[sub_domain] += int(domain[0])
                else:
                    domain_map[sub_domain] = int(domain[0])
                
        for key in domain_map:
            ans.append(f"{domain_map[key]} {key}")
        return ans