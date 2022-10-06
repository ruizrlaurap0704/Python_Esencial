"""
>>> set1={1,2,3}
>>> set2={1,2,3,4,1}
>>> set2
{1, 2, 3, 4}
>>> set3={1,2.0,"texto"}
>>> set3
{1, 2.0, 'texto'}
>>> set3.add(0)
>>> set3
{0, 1, 2.0, 'texto'}
>>> set3.update([2,3,4])
>>> set3
{0, 1, 2.0, 3, 4, 'texto'}
>>> len(set3)
6
>>> set3.discard(4)
>>> set3
{0, 1, 2.0, 3, 'texto'}
>>> set3.remove(3)
>>> set3
{0, 1, 2.0, 'texto'}
>>> set3.clear
<built-in method clear of set object at 0x000002172E32ECE0>
>>> set3
{0, 1, 2.0, 'texto'}

"""
