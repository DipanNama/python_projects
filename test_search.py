import unittest
from search import search
class SearchTests(unittest.TestCase):
    def test_first_duplicate(self): self.assertEqual(search([1,2,2,2,5],2)['index'],1)
    def test_edges(self):
        for t,i in [(1,0),(9,4),(4,-1)]: self.assertEqual(search([1,3,5,7,9],t)['index'],i)
    def test_single(self): self.assertEqual(search([4],4)['index'],0)
    def test_negative(self): self.assertEqual(search([-8,-2,0],-2)['index'],1)
    def test_trace(self): self.assertEqual(search([1,3,5],5)['steps'][0],{'low':0,'high':2,'mid':1,'value':3,'relation':'lower'})
    def test_unsorted(self):
        with self.assertRaises(ValueError): search([2,1],1)
    def test_bounds(self):
        for ns,t in [([],1),([1]*65,1),([True],1),([1.2],1),([1000001],1),([1],False)]:
            with self.assertRaises(ValueError): search(ns,t)
    def test_all_targets(self):
        ns=list(range(-64,65,2))[:64]
        for t in range(-70,71): self.assertEqual(search(ns,t)['index'],ns.index(t) if t in ns else -1)
if __name__=='__main__': unittest.main()
