def isValid(self, s: str) -> bool:
        res=[]
        for i in s:
            if i== '(' or i== '{' or i== '[':
                res.append(i)
            else:
                if not res:
                    return False
                if i== ')' and r[-1] == '(':
                    res.pop()
                elif i== '}' and r[-1] == '{':
                    res.pop()
                elif i== ']' and r[-1] == '[':
                    res.pop()
                else:
                    return False
        return not res
