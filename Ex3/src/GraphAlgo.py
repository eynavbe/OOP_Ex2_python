import math

from Ex3.src.DiGraph import DiGraph
from Ex3.src.GraphAlgoInterface import GraphAlgoInterface
import json
from typing import List
import sys
from Ex3.src.GraphInterface import GraphInterface
from Ex3.src.GraphView import GraphView


class GraphAlgo(GraphAlgoInterface):
    path_min: List
    min = sys.float_info.max

    def __init__(self, di_graph: DiGraph = DiGraph()):
        self.di_graph = di_graph

    def get_graph(self) -> GraphInterface:
        return self.di_graph

    def load_from_json(self, file_name: str) -> bool:
        if file_name.find("json") == -1:
            file_name += ".json"
        self.di_graph = DiGraph()
        try:
            f = open(file_name)
            data = json.load(f)
            for i in data['Nodes']:
                if "pos" in i:
                    self.di_graph.add_node(i["id"], i["pos"])
                else:
                    self.di_graph.add_node(i["id"])
            for i in data['Edges']:
                self.di_graph.add_edge(i["src"], i["dest"], i["w"])
            f.close()
            return True
        except IOError:
            return False
        except:
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            a_list = {"Edges": [], "Nodes": []}
            for key_v in self.di_graph.get_all_v():
                for key in self.di_graph.all_out_edges_of_node(key_v):
                    a_list["Edges"].append(
                        {"src": key_v, "w": self.di_graph.all_out_edges_of_node(key_v)[key], "dest": key})
            for key in self.di_graph.get_all_v():
                a_list["Nodes"].append({"pos": self.di_graph.get_all_v()[key], "id": key})
            json_string = json.dumps(a_list)
            json_file = open(file_name, "w")
            json_file.write(json_string)
            json_file.close()
            return True
        except IOError:
            return False
        except:
            return False

    """Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm"""
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        nodes = list(self.di_graph.get_all_v())
        distance_path, pre_node = {}, {}
        for node in nodes:
            distance_path[node] = sys.maxsize
        distance_path[id1] = 0
        while nodes:
            node_m = None
            for node in nodes:
                if node_m is None:
                    node_m = node
                elif distance_path[node] < distance_path[node_m]:
                    node_m = node
            out_edges = self.di_graph.all_out_edges_of_node(node_m)
            for edge in out_edges:
                distance = distance_path[node_m] + self.di_graph.all_out_edges_of_node(node_m)[edge]
                if distance < distance_path[edge]:
                    distance_path[edge] = distance
                    pre_node[edge] = node_m
            nodes.remove(node_m)
        end_path = id2
        shortest_path = [end_path]
        while end_path != id1:
            if end_path not in pre_node:
                return math.inf, []
            shortest_path.append(pre_node[end_path])
            end_path = pre_node[end_path]
        shortest_path.reverse()
        return distance_path[id2], shortest_path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        list_min = []
        self.path_min = []
        distance_min = 0.0
        self.min = sys.float_info.max
        # sends to the function that checks after placing the first value
        if node_lst is not None:
            for i in range(len(node_lst)):
                path = [[node_lst[i], 0]]
                self.tsp_shortest_route_i(node_lst, path)
            if self.path_min is not None:
                for i in range(len(self.path_min)-1):
                    distance_path, shortest_path = self.shortest_path(self.path_min[i], self.path_min[i+1])
                    if len(shortest_path) > 0:
                        distance_min += distance_path
                    for y in range(len(shortest_path)-1):
                        list_min.append(shortest_path[y])
                    if i == len(self.path_min)-2:
                        list_min.append(self.path_min[len(self.path_min)-1])
        if len(list_min) == 0:
            return [], math.inf
        return list_min, distance_min

    """ 
     The function checks which route is the shortest (with the least weight).
     According to the list given when the first value of the route is given.
     save the route minimal.
    """
    def tsp_shortest_route_i(self, node_lst, path):
        sum_w = 0.0
        if len(path) == len(node_lst):
            for key in path:
                sum_w += key[1]
            if sum_w < self.min:
                self.min = sum_w
                self.path_min = []
                for key in path:
                    self.path_min.append(key[0])
            return
        for i in range(len(node_lst)):
            w = node_lst[i]
            visited = False
            for x in path:
                if x[0] == w:
                    visited = True
            if not visited:
                distance_path, shortest_path = self.shortest_path(path[len(path)-1][0], w)
                if len(shortest_path) > 0:
                    path.append([w, distance_path])
                    self.tsp_shortest_route_i(node_lst, path)
                    path.remove(path[len(path)-1])


    def centerPoint(self) -> (int, float):
        min_max = sys.maxsize
        node_data_choose = -1
        for node_id in self.di_graph.get_all_v():
            max_w = 0.0
            for node_id2 in self.di_graph.get_all_v():
                if node_id != node_id2:
                    max_new, shortest_path = self.shortest_path(node_id, node_id2)
                    if max_new == math.inf:
                        return None, math.inf
                    if max_w < max_new:
                        max_w = max_new
            if min_max > max_w != 0:
                min_max = max_w
                node_data_choose = node_id
        return node_data_choose, min_max

    def plot_graph(self) -> None:
        GraphView(self.di_graph)
