import unittest
from Ex3.src.GraphAlgo import GraphAlgo

a0 = GraphAlgo()
a0.load_from_json('../data/A0.json')
a1 = GraphAlgo()
a1.load_from_json('../data/A1.json')
a2 = GraphAlgo()
a2.load_from_json('../data/A2.json')
a3 = GraphAlgo()
a3.load_from_json('../data/A3.json')
a4 = GraphAlgo()
a4.load_from_json('../data/A4.json')
a5 = GraphAlgo()
a5.load_from_json('../data/A5.json')
T0 = GraphAlgo()
T0.load_from_json('../data/T0.json')


class MyTestCase(unittest.TestCase):

    def test_v_size(self):
        self.assertEqual(a0.get_graph().v_size(), 11)
        self.assertEqual(a1.get_graph().v_size(), 17)
        self.assertEqual(a2.get_graph().v_size(), 31)
        self.assertEqual(a3.get_graph().v_size(), 49)
        self.assertEqual(a4.get_graph().v_size(), 40)
        self.assertEqual(a5.get_graph().v_size(), 48)
        self.assertEqual(T0.get_graph().v_size(), 4)
        million = GraphAlgo()
        million.load_from_json('../data/1000000Nodes.json')
        self.assertEqual(million.get_graph().v_size(), 1000000)

    def test_e_size(self):
        self.assertEqual(a0.get_graph().e_size(), 22)
        self.assertEqual(a1.get_graph().e_size(), 36)
        self.assertEqual(a2.get_graph().e_size(), 80)
        self.assertEqual(a3.get_graph().e_size(), 136)
        self.assertEqual(a4.get_graph().e_size(), 102)
        self.assertEqual(a5.get_graph().e_size(), 166)
        self.assertEqual(T0.get_graph().e_size(), 5)
        million = GraphAlgo()
        million.load_from_json('../data/1000000Nodes.json')
        self.assertEqual(million.get_graph().e_size(), 1999996)
        n100000 = GraphAlgo()
        n100000.load_from_json('../data/100000Nodes.json')
        self.assertEqual(n100000.get_graph().e_size(), 1999804)

    def test_get_all_v(self):
        self.assertEqual(a0.get_graph().get_all_v().get(2), "35.19341035835351,32.10610841680672,0.0")
        self.assertEqual(a1.get_graph().get_all_v().get(56), None)
        self.assertEqual(a2.get_graph().get_all_v().get(20), "35.19188202905569,32.10579947394958,0.0")
        self.assertEqual(a3.get_graph().get_all_v().get(48), "35.21213239225182,32.1077621697479,0.0")
        self.assertEqual(a4.get_graph().get_all_v().get(32), "35.20115813882163,32.10750774621849,0.0")
        self.assertEqual(a5.get_graph().get_all_v().get(42), "35.20033029378531,32.10919784537815,0.0")
        self.assertNotEqual(T0.get_graph().get_all_v().get(0), None)

    def test_all_in_edges_of_node(self):
        self.assertEqual(a0.get_graph().all_in_edges_of_node(0), {1: 1.8884659521433524, 10: 1.1761238717867548})
        self.assertEqual(a1.get_graph().all_in_edges_of_node(6),
                         {2: 1.7938753352369698, 5: 1.734311926030133, 7: 1.5786081900467002})
        self.assertEqual(a2.get_graph().all_in_edges_of_node(16), {0: 1.3118716362419698, 15: 1.8726071511162605})
        self.assertEqual(a3.get_graph().all_in_edges_of_node(37), {36: 1.3286046556630244, 38: 1.4524481904211108})
        self.assertEqual(a4.get_graph().all_in_edges_of_node(4), {3: 1.9908441205772092, 5: 1.0131908397905627})
        self.assertEqual(a5.get_graph().all_in_edges_of_node(4),
                         {3: 1.3762856877574432, 5: 1.741663365681239, 13: 0.8625859471230286})
        self.assertEqual(T0.get_graph().all_in_edges_of_node(0), {1: 1.1})
        self.assertEqual(T0.get_graph().all_in_edges_of_node(1), {0: 1})

    def test_all_out_edges_of_node(self):
        self.assertEqual(a0.get_graph().all_out_edges_of_node(0), {1: 1.4004465106761335, 10: 1.4620268165085584})
        self.assertEqual(a1.get_graph().all_out_edges_of_node(6),
                         {2: 1.8474047229605628, 5: 1.4964304236123005, 7: 1.237565124536135})
        self.assertEqual(a2.get_graph().all_out_edges_of_node(16), {0: 1.4418017651347552, 15: 1.5677693324851103})
        self.assertEqual(a3.get_graph().all_out_edges_of_node(37), {36: 1.2220121679023612, 38: 1.3491411111500056})
        self.assertEqual(a4.get_graph().all_out_edges_of_node(4), {3: 1.6284986709004998, 5: 1.1712767410444496})
        self.assertEqual(a5.get_graph().all_out_edges_of_node(4),
                         {3: 1.0325537061811674, 5: 1.8112664253321413, 13: 0.8688885415846178})
        self.assertEqual(T0.get_graph().all_out_edges_of_node(2), {3: 1.1})
        self.assertEqual(T0.get_graph().all_out_edges_of_node(3), {})

    def test_add_edge_and_add_node(self):
        g_algo = GraphAlgo()
        self.assertEqual(g_algo.get_graph().add_node(0), True)
        self.assertEqual(g_algo.get_graph().add_node(1), True)
        self.assertEqual(g_algo.get_graph().add_node(2), True)
        self.assertEqual(g_algo.get_graph().add_node(2), False)
        self.assertEqual(g_algo.get_graph().add_edge(0, 1, 1), True)
        self.assertEqual(g_algo.get_graph().add_edge(1, 2, 4), True)
        self.assertEqual(g_algo.get_graph().add_edge(1, 2, 3), False)
        self.assertEqual(g_algo.get_graph().all_in_edges_of_node(0), {})
        self.assertEqual(g_algo.get_graph().all_in_edges_of_node(1), {0: 1})

    def test_remove_edge(self):
        self.assertEqual(a0.get_graph().e_size(), 22)
        self.assertEqual(a0.get_graph().remove_edge(0, 1), True)
        self.assertEqual(a0.get_graph().e_size(), 21)
        self.assertEqual(a0.get_graph().remove_edge(0, 1), False)

    def test_remove_node(self):
        self.assertEqual(a0.get_graph().v_size(), 11)
        self.assertEqual(a0.get_graph().remove_node(3), True)
        self.assertEqual(a0.get_graph().v_size(), 10)
        self.assertEqual(a0.get_graph().remove_node(3), False)
        self.assertEqual(a0.get_graph().add_node(3), True)


if __name__ == '__main__':
    unittest.main()
