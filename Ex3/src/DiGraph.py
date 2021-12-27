from Ex3.src.GraphInterface import GraphInterface
from typing import List
import random


class DiGraph(GraphInterface):
    def __init__(self):
        self.mc = 0
        self.node_list: dict = {}
        self.in_edges: dict = {}
        self.out_edges: dict = {}

    def v_size(self) -> int:
        return len(self.node_list)

    def e_size(self) -> int:
        size_edge = 0
        for node in self.node_list:
            size_edge += len(self.all_out_edges_of_node(node))
        return size_edge

    def get_all_v(self) -> dict:
        return self.node_list

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.in_edges.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.out_edges.get(id1)

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 == id2:
            return False
        if (id2 in self.node_list) and (id1 in self.node_list):
            if id2 not in self.out_edges[id1]:
                self.out_edges[id1].update({id2: weight})
                self.in_edges[id2].update({id1: weight})
                self.mc += 1
                return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if pos is None:
            pos = str(35 + random.random()) + ',' + str(32 + random.random()) + ',0.0'
        if node_id not in self.node_list:
            self.node_list[node_id] = pos
            self.in_edges[node_id] = {}
            self.out_edges[node_id] = {}
            self.mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if self.node_list is None:
            return False
        if self.out_edges is None:
            return False
        if self.in_edges is None:
            return False
        for x in self.node_list:
            self.remove_edge(node_id, x)
            self.remove_edge(x, node_id)
        if node_id not in self.node_list:
            return False
        node_data = self.node_list[node_id]
        if node_data is not None:
            self.node_list.pop(node_id)
            if self.in_edges is not None:
                self.in_edges.pop(node_id)
            if self.out_edges is not None:
                self.out_edges.pop(node_id)
            self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.in_edges is None:
            return False
        if self.out_edges is None:
            return False
        if node_id1 not in self.out_edges:
            return False
        if self.out_edges[node_id1] is None:
            return False
        if node_id2 not in self.in_edges:
            return False
        if self.in_edges[node_id2] is None:
            return False
        if node_id2 in self.out_edges[node_id1]:
            self.out_edges[node_id1].pop(node_id2)
            self.in_edges[node_id2].pop(node_id1)
            self.mc += 1
            return True
        return False

    # def __repr__(self):


    def __str__(self):
        list_e = {"Edges": [], "Nodes": []}
        list_e["Nodes"].append(self.node_list)
        for node in self.node_list:
            list_out = self.all_out_edges_of_node(node)
            for x in list_out:
                list_e["Edges"].append({x, node, list_out[x]})
        return str(list_e)
        # return "[ id: " + str(self.id_b) + ", speed: " + str(self.speed) + ", min_floor: " + str(self.min_floor) + \
        #        ", max_floor: " + str(self.max_floor) + ", close_time: " + str(self.close_time) + ", open_time: " \
        #        + str(self.open_time) + ", start_time: " + str(self.start_time) + ", stop_time: " + str(
        #     self.stop_time) + "]"
        # str = ''



