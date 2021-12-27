import math
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
n1000 = GraphAlgo()
n1000.load_from_json('../data/1000Nodes.json')
n10000 = GraphAlgo()
n10000.load_from_json('../data/10000Nodes.json')
n100000 = GraphAlgo()
n100000.load_from_json('../data/100000Nodes.json')
nMillion = GraphAlgo()
nMillion.load_from_json('../data/1000000Nodes.json')


class MyTestCase(unittest.TestCase):

    # def test_load_file(self):
    #     a3 = GraphAlgo()
    #     a3.load_from_json('../data/T0.json')

    def test_save_file(self):
        self.assertEqual(a5.save_to_json('../data/SavedA5.json'), True)
        self.assertEqual(a4.save_to_json('../data/SavedA4.json'), True)
        self.assertEqual(a3.save_to_json('../data/SavedA3.json'), True)
        self.assertEqual(a2.save_to_json('../data/SavedA2.json'), True)
        self.assertEqual(a1.save_to_json('../data/SavedA1.json'), True)
        self.assertEqual(a0.save_to_json('../data/SavedA0.json'), True)
        self.assertEqual(n1000.save_to_json('../data/SavedN1000.json'), True)
        self.assertEqual(n10000.save_to_json('../data/SavedN10000.json'), True)
        self.assertEqual(n100000.save_to_json('../data/SavedN100000.json'), True)
        self.assertEqual(nMillion.save_to_json('../data/SavedNMillion.json'), True)
        self.assertEqual(T0.save_to_json('../data/SavedT0.json'), True)
        g_algo = GraphAlgo()
        self.assertEqual(g_algo.load_from_json('T0.json'), False)
        self.assertEqual(g_algo.save_to_json('../data_hgh/T0.json'), False)
        self.assertEqual(g_algo.load_from_json('../data/G9.json'), False)

    def test_shortest_path_and_get_graph(self):
        self.assertEqual(a0.shortest_path(3, 5), (3.374437071805205, [3, 4, 5]))
        self.assertEqual(a1.shortest_path(4, 13), (12.560793479202072, [4, 3, 2, 1, 0, 16, 15, 14, 13],))
        self.assertEqual(a2.shortest_path(2, 30), (10.432753865671888, [2, 1, 26, 8, 9, 10, 11, 20, 30]))
        self.assertEqual(a3.shortest_path(0, 14), (4.515586995937101, [0, 16, 15, 14]))
        self.assertEqual(a4.shortest_path(3, 28), (4.149192397274244, [3, 2, 30, 28]))
        self.assertEqual(a5.shortest_path(8, 9), (1.3111536270737347, [8, 1, 9]))
        self.assertEqual(n1000.shortest_path(53, 4), (807.3555519164579, [53, 374, 497, 861, 818, 337, 112, 4]))
        self.assertEqual(n10000.shortest_path(0, 8902), (629.8214345359398, [0, 8902]))
        self.assertEqual(n100000.shortest_path(68266, 1912), (12.849129682861793, [68266, 32574, 4905, 62357, 92481,
                                                                                   45750, 4149, 87704, 58825, 95523,
                                                                                   42464, 39966, 1912]))
        # self.assertEqual(nMillion.shortest_path(881734, 484909), ([881734, 484909], 27.693562949340148)) #cant
        # calculate because it is too big and not connected graph

        self.assertEqual(T0.shortest_path(3, 2), (math.inf, []))
        self.assertEqual(T0.shortest_path(2, 3), (1.1, [2, 3]))
        self.assertEqual(T0.shortest_path(1, 0), (1.1, [1, 0]))
        self.assertEqual(T0.shortest_path(2, 0), (math.inf, []))

        # According to a given example in the "shortest_path":
        g_algo = GraphAlgo()
        g_algo.get_graph().add_node(0)
        g_algo.get_graph().add_node(1)
        g_algo.get_graph().add_node(2)
        g_algo.get_graph().add_edge(0, 1, 1)
        g_algo.get_graph().add_edge(1, 2, 4)
        self.assertEqual(g_algo.shortest_path(0, 1), (1, [0, 1]))
        self.assertEqual(g_algo.shortest_path(0, 2), (5, [0, 1, 2]))

    def testTSP(self):
        tsp_l = [9, 5, 2, 3, 6, 13]
        self.assertEqual(a0.TSP(tsp_l), ([], math.inf))
        self.assertEqual(a1.TSP(tsp_l), ([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 15.598204536149135))
        self.assertEqual(a2.TSP(tsp_l), ([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 30, 13], 15.377469318961012))
        self.assertEqual(a3.TSP(tsp_l), ([5, 6, 2, 3, 31, 30, 13, 12, 11, 10, 9], 13.632350309300083))
        self.assertEqual(a4.TSP(tsp_l), ([13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2], 17.069950353687258))
        self.assertEqual(a5.TSP(tsp_l), ([9, 2, 3, 13, 5, 6], 6.0596711656944375))
        tspLBig = [9, 3, 6]
        self.assertEqual(n1000.TSP(tspLBig), (
            [9, 573, 305, 344, 186, 544, 896, 166, 6, 50, 149, 610, 236, 3], 1286.7743768781063))  # time: 671 ms
        self.assertEqual(n10000.TSP(tspLBig), (
            [9, 509, 3775, 6194, 2157, 2737, 6948, 6630, 6, 933, 7821, 3246, 7483, 9857, 8335, 3],
            1815.2459084037032))  # time: 47 sec 17 ms
        # self.assertEqual(n100000.TSP(tspLBig), ([9, 2, 3, 13, 5, 6], 6.0596711656944375)) #too big
        # self.assertEqual(nMillion.TSP(tspLBig), ([9, 2, 3, 13, 5, 6], 6.0596711656944375)) #too big

        tspL2 = [3, 1, 2]
        self.assertEqual(T0.TSP(tspL2), ([1, 2, 3], 2.4000000000000004))
        tspL3 = [1, 2, 3]
        self.assertEqual(T0.TSP(tspL3), ([1, 2, 3], 2.4000000000000004))
        self.assertEqual(a0.TSP(tspL2), ([3, 2, 1], 2.8136021362086723))

    def test_center_point(self):
        self.assertEqual(a0.centerPoint(), (7, 6.806805834715163))
        self.assertEqual(a1.centerPoint(), (8, 9.925289024973141))
        self.assertEqual(a2.centerPoint(), (0, 7.819910602212574))
        self.assertEqual(a3.centerPoint(), (2, 8.182236568942237))
        self.assertEqual(a4.centerPoint(), (6, 8.071366078651435))
        self.assertEqual(a5.centerPoint(), (40, 9.291743173960954))
        self.assertEqual(T0.centerPoint(), (None, math.inf))

    # def test_plot_graph(self):
    # a0.plot_graph()
    # a1.plot_graph()
    # a2.plot_graph()
    # a3.plot_graph()
    # a4.plot_graph()
    # a5.plot_graph()
    # n1000.plot_graph()
    # n10000.plot_graph()
    # n100000.plot_graph()
    # nMillion.plot_graph()
    # T0.plot_graph()


if __name__ == '__main__':
    unittest.main()
