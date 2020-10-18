while True:
        if len(lst)>k:
            print('-1')
            break
        elif lst[p]==x:
            print(f)
            break
        elif x not in lst and len(lst)>k:
            lst[k]=x
            s=lst
            s.sort()
            if s[p]==x:
                print(o)
                break
            else:
                print('-1')
                break
        
        
        elif x in lst and len(lst)>k:
            lst[k]=j
            f=f+1
            g=lst
            g.sort()
            if g[p]==x:
                print('s')
                print(f)
                break
            else:
                j=j+1
        else:
            break
            
