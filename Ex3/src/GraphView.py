import math
import sys
import pygame
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
import tkinter
from Ex3.src.DiGraph import DiGraph


class GraphView:
    width = 635
    height = 600
    RED = (255, 0, 0)
    PINK = (255, 102, 102)
    AZURE = (0, 204, 255)
    BLUE = (0, 0, 128)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (62, 91, 91)
    PALE_YELLOW = (255, 255, 179)

    def __init__(self, di_graph: DiGraph = DiGraph()):
        self.di_graph = di_graph
        self.draw()

    """Creates the GUI screen: Menu, Action..."""
    def draw(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('graph')
        screen.fill(self.PALE_YELLOW)
        status_a = 'menu'
        button_graph = self.button_create("GRAPH", (0, 0, 45, 30), self.AZURE, self.PINK, self.on_click_button_graph)
        button_shortest_path = self.button_create("SHORTEST PATH", (45, 0, 100, 30), self.AZURE, self.PINK,
                                                  self.on_click_button_shortest_path)
        button_tsp = self.button_create("TSP", (145, 0, 25, 30), self.AZURE, self.PINK, self.on_click_button_tsp)
        button_center = self.button_create("CENTER_POINT", (170, 0, 90, 30), self.AZURE, self.PINK,
                                           self.on_click_button_center_point)
        button_add_edge = self.button_create(
            "ADD_EDGE", (260, 0, 65, 30), self.AZURE, self.PINK, self.on_click_button_add_edge)
        button_remove_node = self.button_create(
            "REMOVE_NODE", (325, 0, 90, 30), self.AZURE, self.PINK, self.on_click_remove_node)
        button_remove_edge = self.button_create(
            "REMOVE_EDGE", (415, 0, 90, 30), self.AZURE, self.PINK, self.on_click_remove_edge)
        button_load = self.button_create("LOAD_FILE", (505, 0, 65, 30), self.AZURE, self.PINK, self.on_click_button_load)
        button_save = self.button_create("SAVE_FILE", (570, 0, 65, 30), self.AZURE, self.PINK, self.on_click_button_save)
        self.get_graph_paint()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # create a new node at the click of a mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 < event.pos[0] < 550 and 50 < event.pos[1] < 550:
                        tk_notice = tk.Tk()
                        tk_notice.eval('tk::PlaceWindow . center')
                        tk_notice.title('add node')

                        def add_node_yes():
                            start = 50
                            graph_dimensions = 500
                            radius = 7
                            all_nodes = self.di_graph.get_all_v()
                            min_lat = sys.float_info.max
                            min_lon = sys.float_info.max
                            max_lat = sys.float_info.min
                            max_lon = sys.float_info.min
                            for node_data in all_nodes:
                                point = all_nodes[node_data].split(",")
                                min_lat = min(min_lat, float(point[0]))
                                min_lon = min(min_lon, float(point[1]))
                                max_lat = max(max_lat, float(point[0]))
                                max_lon = max(max_lon, float(point[1]))
                            lat_extent = float(max_lat - min_lat)
                            lon_extent = float(max_lon - min_lon)
                            y = min_lat + lat_extent - (lat_extent * (event.pos[1] - start)) / graph_dimensions
                            x = min_lon + ((lon_extent * (event.pos[0] - start)) / graph_dimensions)
                            k = list(all_nodes.keys())
                            id_node = (k[len(all_nodes) - 1])
                            while id_node in all_nodes:
                                id_node += 1
                            pos = '' + str(y) + ',' + str(x) + ',0.0'
                            # pos += str(y)
                            # pos += ','
                            # pos += str(x)
                            # pos += ',0.0'
                            self.di_graph.add_node(id_node, pos)
                            ly3 = start + int(
                                (graph_dimensions - (graph_dimensions * (y - min_lat) / lat_extent)))
                            lx3 = start + int(((graph_dimensions * (
                                    x - min_lon) / lon_extent)))
                            pygame.draw.circle(screen, self.RED, (lx3 - radius, ly3 - radius), 7)
                            font = pygame.font.SysFont("Times New Roman", 10)
                            text = font.render(str(id_node), True, self.BLACK, self.RED)
                            text_rect = text.get_rect()
                            text_rect.center = (lx3 - radius, ly3 - radius)
                            screen.blit(text, text_rect)
                            tk_notice.destroy()

                        def add_node_no():
                            tk_notice.destroy()
                        ttk.Label(tk_notice, text="You want to add node at this point? ").grid(column=0, row=0)
                        ttk.Button(tk_notice, text='Yes', command=add_node_yes).grid(column=0, row=1)
                        ttk.Button(tk_notice, text='No', command=add_node_no).grid(column=1, row=1)
                        tk_notice.mainloop()
                if status_a == 'menu':
                    self.button_check(button_graph, event)
                    self.button_check(button_shortest_path, event)
                    self.button_check(button_tsp, event)
                    self.button_check(button_center, event)
                    self.button_check(button_add_edge, event)
                    self.button_check(button_load, event)
                    self.button_check(button_save, event)
                    self.button_check(button_remove_node, event)
                    self.button_check(button_remove_edge, event)
            if status_a == 'menu':
                self.button_draw(screen, button_graph)
                self.button_draw(screen, button_shortest_path)
                self.button_draw(screen, button_tsp)
                self.button_draw(screen, button_center)
                self.button_draw(screen, button_add_edge)
                self.button_draw(screen, button_load)
                self.button_draw(screen, button_save)
                self.button_draw(screen, button_remove_node)
                self.button_draw(screen, button_remove_edge)
            pygame.display.update()
        pygame.quit()

    """Creates the menu button"""
    def button_create(self, text, rect, inactive_color, active_color, action):
        font = pygame.font.Font(None, 16)
        button_rect = pygame.Rect(rect)
        text = font.render(text, True, self.BLACK)
        text_rect = text.get_rect(center=button_rect.center)
        return [text, text_rect, button_rect, inactive_color, active_color, action, False]

    """Clicking one of the menu buttons"""
    def button_check(self, info, event):
        text, text_rect, rect, inactive_color, active_color, action, hover = info
        if event.type == pygame.MOUSEMOTION:
            info[-1] = rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hover and action:
                action()

    """Draws the menu button"""
    def button_draw(self, screen, info):
        text, text_rect, rect, inactive_color, active_color, action, hover = info
        if hover:
            color = active_color
        else:
            color = inactive_color
        pygame.draw.rect(screen, color, rect)
        screen.blit(text, text_rect)

    """Clicking the 'get graph' menu button create the graph"""
    def on_click_button_graph(self):
        status_a = 'get graph'
        self.get_graph_paint()

    """Clicking the 'shortest path' menu button 
    Opens a message where you select the details to get the shortest path on the graph"""
    def on_click_button_shortest_path(self):
        # global status_a
        status_a = 'shortest path'
        all_nodes_d = self.di_graph.get_all_v()
        points_tsp = []
        for x in all_nodes_d:
            points_tsp.append(x)
        window = tk.Tk()
        window.eval('tk::PlaceWindow . center')
        window.title(status_a)
        ttk.Label(window, text="select src:", font=("Times New Roman", 10)).grid(column=0, row=15, padx=10, pady=25)
        n = tk.StringVar()
        combo_box = ttk.Combobox(window, width=3, textvariable=n)
        combo_box['values'] = points_tsp
        combo_box.grid(column=1, row=15)
        ttk.Label(window, text="select dest:", font=("Times New Roman", 10)).grid(column=7, row=15, padx=10, pady=25)
        n = tk.StringVar()
        combo_box2 = ttk.Combobox(window, width=3, textvariable=n)
        combo_box2['values'] = points_tsp
        combo_box2.grid(column=14, row=15)
        combo_box2.current(1)
        combo_box.current(0)

        def choose_what_to_mark():
            id2 = int(combo_box2.get())
            id1 = int(combo_box.get())
            window.destroy()
            from Ex3.src.GraphAlgo import GraphAlgo
            dis, list_s = GraphAlgo(self.di_graph).shortest_path(id1, id2)
            if dis == math.inf:
                dis = -1
            self.get_graph_paint(status_a, list_s, dis)

        slogan = tk.Button(window, text="Select", command=choose_what_to_mark)
        slogan.grid(column=22, row=15)
        window.mainloop()
        pygame.display.flip()

    """Draws the graph by the details obtained when creating this class and also gets
     'status_a' which marks the details on the graph according to the selected menu type, 
     'list_to_mark' which marks the route of the points there, 
     'dis' writes text of a certain distance (according to each menu type Pressed)"""
    def get_graph_paint(self, status_a='', list_to_mark=None, dis=0):
        if list_to_mark is None:
            list_to_mark = []
        screen = pygame.display.set_mode((self.width, self.height))
        screen.fill(self.PALE_YELLOW)
        start = 50
        graph_dimensions = 500
        radius = 7
        all_nodes = self.di_graph.get_all_v()
        min_lat = sys.float_info.max
        min_lon = sys.float_info.max
        max_lat = sys.float_info.min
        max_lon = sys.float_info.min
        for node_data in all_nodes:
            point = all_nodes[node_data].split(",")
            min_lat = min(min_lat, float(point[0]))
            min_lon = min(min_lon, float(point[1]))
            max_lat = max(max_lat, float(point[0]))
            max_lon = max(max_lon, float(point[1]))
        lat_extent = float(max_lat - min_lat)
        lon_extent = float(max_lon - min_lon)
        all_nodes = self.di_graph.get_all_v()
        for node_data in all_nodes:
            point = all_nodes[node_data].split(",")
            ly = start + int((graph_dimensions - ((graph_dimensions * (float(point[0]) - min_lat)) / lat_extent)))
            lx = start + int(((graph_dimensions * (float(point[1]) - min_lon)) / lon_extent))
            pygame.draw.circle(screen, self.AZURE, (lx - radius, ly - radius), 7)
            font = pygame.font.SysFont("Times New Roman", 10)
            text = font.render(str(node_data), True, self.BLACK, self.AZURE)
            text_rect = text.get_rect()
            text_rect.center = (lx - radius, ly - radius)
            screen.blit(text, text_rect)
            out_edges = self.di_graph.all_out_edges_of_node(node_data)
            for edge_data in out_edges:
                point = all_nodes[edge_data].split(",")
                ly_dest = start + int(
                    (graph_dimensions - ((graph_dimensions * (float(point[0]) - min_lat)) / lat_extent)))
                lx_dest = start + int(((graph_dimensions * (float(point[1]) - min_lon)) / lon_extent))
                lx_new2 = int((0.9 * (lx_dest - lx)))
                lx_new2_start = int((0.1 * (lx_dest - lx)))
                ly_new2 = int((0.9 * (ly_dest - ly)))
                ly_new2_start = int((0.1 * (ly_dest - ly)))
                self.draw_arrow(screen, self.GREY, (lx + lx_new2_start, ly + ly_new2_start),
                                (lx + lx_new2, ly + ly_new2))
                font = pygame.font.SysFont("Times New Roman", 12)
                text = font.render("{0:.1f}".format(out_edges[edge_data]), True, self.BLACK, self.AZURE)
                text_rect = text.get_rect()
                text_rect.center = ((lx + int((0.7 * (lx_dest - lx)))), (ly + int((0.7 * (ly_dest - ly)))))
                screen.blit(text, text_rect)
        if status_a == 'centerPoint':
            font = pygame.font.SysFont("Times New Roman", 20)
            if dis == -1:
                text = font.render("no center point", True, self.WHITE, self.BLUE)
            else:
                text = font.render("min-maximum distance: {0:.2f}".format(dis), True, self.WHITE, self.BLUE)
            text_rect = text.get_rect()
            text_rect.center = (200, 570)
            screen.blit(text, text_rect)
            if dis != -1:
                point = all_nodes[list_to_mark[0]].split(",")
                ly3 = start + int((graph_dimensions - (graph_dimensions * (float(point[0]) - min_lat) / lat_extent)))
                lx3 = start + int((graph_dimensions * (float(point[1]) - min_lon) / lon_extent))
                pygame.draw.circle(screen, self.RED, (lx3 - radius, ly3 - radius), 9)
                font = pygame.font.SysFont("Times New Roman", 10)
                text = font.render(str(list_to_mark[0]), True, self.BLACK, self.RED)
                text_rect = text.get_rect()
                text_rect.center = (lx3 - radius, ly3 - radius)
                screen.blit(text, text_rect)
        if status_a == 'tsp' or status_a == 'shortest path' or status_a == 'add edge':
            font = pygame.font.SysFont("Times New Roman", 20)
            if status_a != 'add edge':
                if dis == -1:
                    text = font.render("no path between the points", True, self.WHITE, self.BLUE)
                else:
                    print(dis)
                    text = font.render("the overall distance: {0:.2f}".format(dis), True, self.WHITE, self.BLUE)
                text_rect = text.get_rect()
                text_rect.center = (200, 570)
                screen.blit(text, text_rect)
            if list_to_mark is None:
                list_to_mark = []
            if len(list_to_mark) > 0:
                for nodeI in range(len(list_to_mark) - 1):
                    point = all_nodes[list_to_mark[nodeI]].split(",")
                    ly3 = start + int(
                        (graph_dimensions - ((graph_dimensions * (float(point[0]) - min_lat)) / lat_extent)))
                    lx3 = start + int(((graph_dimensions * (float(point[1]) - min_lon)) / lon_extent))
                    point = all_nodes[list_to_mark[nodeI + 1]].split(",")
                    ly_dest1 = start + int(
                        (graph_dimensions - ((graph_dimensions * (float(point[0]) - min_lat)) / lat_extent)))
                    lx_dest1 = start + int(((graph_dimensions * (float(point[1]) - min_lon)) / lon_extent))
                    lx_new3 = int((0.9 * (lx_dest1 - lx3)))
                    ly_new3 = int((0.9 * (ly_dest1 - ly3)))
                    lx_new2_start = int((0.1 * (lx_dest1 - lx3)))
                    ly_new2_start = int((0.1 * (ly_dest1 - ly3)))
                    self.draw_arrow(screen, self.RED, (lx3 + lx_new2_start, ly3 + ly_new2_start),
                                    (lx3 + lx_new3, ly3 + ly_new3))
                    font = pygame.font.SysFont("Times New Roman", 12)
                    w = self.di_graph.all_out_edges_of_node(list_to_mark[nodeI]).get(list_to_mark[nodeI + 1])
                    text = font.render("{0:.1f}".format(w), True, self.BLACK, self.RED)
                    text_rect = text.get_rect()
                    text_rect.center = ((lx3 + int((0.7 * (lx_dest1 - lx3)))), (ly3 + int((0.7 * (ly_dest1 - ly3)))))
                    screen.blit(text, text_rect)
                    point = all_nodes[list_to_mark[nodeI]].split(",")
                    ly = start + int(
                        (graph_dimensions - ((graph_dimensions * (float(point[0]) - min_lat)) / lat_extent)))
                    lx = start + int(((graph_dimensions * (float(point[1]) - min_lon)) / lon_extent))
                    pygame.draw.circle(screen, self.RED, (lx - radius, ly - radius), 7)
                    font = pygame.font.SysFont("Times New Roman", 10)
                    text = font.render(str(list_to_mark[nodeI]), True, self.BLACK, self.RED)
                    text_rect = text.get_rect()
                    text_rect.center = (lx - radius, ly - radius)
                    screen.blit(text, text_rect)
                point = all_nodes[list_to_mark[len(list_to_mark) - 1]].split(",")
                ly3 = start + int((graph_dimensions - (graph_dimensions * (float(point[0]) - min_lat) / lat_extent)))
                lx3 = start + int((graph_dimensions * (float(point[1]) - min_lon) / lon_extent))
                pygame.draw.circle(screen, self.RED, (lx3 - radius, ly3 - radius), 7)
                font = pygame.font.SysFont("Times New Roman", 10)
                text = font.render(str(list_to_mark[len(list_to_mark) - 1]), True, self.BLACK, self.RED)
                text_rect = text.get_rect()
                text_rect.center = (lx3 - radius, ly3 - radius)
                screen.blit(text, text_rect)
        pygame.display.flip()

    """Clicking on the button in the 'tsp' menu creates 
    a message where you select the relevant information 
    (all the points where you want to get the shortest route between all the points on the graph)"""
    def on_click_button_tsp(self):
        # global status_a
        val = []
        status_a = 'tsp'
        tk_notice = tk.Tk()
        tk_notice.eval('tk::PlaceWindow . center')
        tk_notice.title(status_a)
        all_nodes_d = self.di_graph.get_all_v()
        keys_list = list(all_nodes_d)

        def var_states():
            list_node = []
            for id_k in range(len(val)):
                if val[id_k].get() == 1:
                    list_node.append(keys_list[id_k])
            from Ex3.src.GraphAlgo import GraphAlgo
            list_s, dis = GraphAlgo(self.di_graph).TSP(list_node)
            if dis == math.inf:
                dis = -1
            tk_notice.destroy()
            self.get_graph_paint(status_a, list_s, dis)

        ttk.Label(tk_notice, text="Choose points_tsp: ").grid(column=0, row=0)
        r, c = 0, 1
        for x in range(len(all_nodes_d)):
            val.append(tk.IntVar())
            ttk.Checkbutton(tk_notice, text=keys_list[x], variable=val[x]).grid(column=c, row=r)
            if c > 10:
                r += 1
                c = 1
            else:
                c += 1
        ttk.Button(tk_notice, text='Select', command=var_states).grid(row=r + 2, sticky=W, pady=4)
        tk_notice.mainloop()
        pygame.display.flip()

    """Draws an arrow with the details obtained"""
    def draw_arrow(self, screen, colour, start, end):
        pygame.draw.line(screen, colour, start, end, 2)
        rotation = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
        pygame.draw.polygon(screen, colour, (
            (end[0] + 6 * math.sin(math.radians(rotation)), end[1] + 6 * math.cos(math.radians(rotation))),
            (end[0] + 6 * math.sin(math.radians(rotation - 120)), end[1] + 6 * math.cos(math.radians(rotation - 120))),
            (end[0] + 6 * math.sin(math.radians(rotation + 120)), end[1] + 6 * math.cos(math.radians(rotation + 120)))))

    """Clicking on the button in the 'centerPoint' menu 
    sends to the function of drawing a graph the center point of all points"""
    def on_click_button_center_point(self):
        # global status_a
        status_a = 'centerPoint'
        from Ex3.src.GraphAlgo import GraphAlgo
        num, dis = GraphAlgo(self.di_graph).centerPoint()
        if dis == math.inf:
            num, dis = -1, -1
        list_c = [num]
        self.get_graph_paint(status_a, list_c, dis)
        pygame.display.flip()

    """Checks if the str is a decimal number"""
    def check_float(self, num) -> bool:
        try:
            float(num)
        except ValueError:
            return False
        return True

    """Clicking on the button in the 'remove node' menu creates 
         a message where you select the relevant information 
        (the node you want to remove)"""
    def on_click_remove_node(self):
        # global status_a
        status_a = 'remove node'
        all_nodes_d = self.di_graph.get_all_v()
        points_tsp = []
        for x in all_nodes_d:
            points_tsp.append(x)
        window = tk.Tk()
        window.eval('tk::PlaceWindow . center')
        window.title(status_a)
        ttk.Label(window, text="select node id:", font=("Times New Roman", 10)).grid(column=0, row=15, padx=10, pady=25)
        n = tk.StringVar()
        combo_box = ttk.Combobox(window, width=3, textvariable=n)
        combo_box['values'] = points_tsp
        combo_box.grid(column=1, row=15)
        combo_box.current(0)

        def choose_what_to_mark():
            id1 = int(combo_box.get())
            self.di_graph.remove_node(id1)
            self.get_graph_paint()
            window.destroy()

        slogan = tk.Button(window, text="Select", command=choose_what_to_mark)
        slogan.grid(column=22, row=15)
        window.mainloop()
        pygame.display.flip()

    """Clicking on the button in the 'remove edge' menu creates 
             a message where you select the relevant information 
            (the edge you want to remove)"""
    def on_click_remove_edge(self):
        # global status_a
        status_a = 'remove edge'
        all_nodes_d = self.di_graph.get_all_v()
        points_tsp = []
        for x in all_nodes_d:
            points_tsp.append(x)
        window = tk.Tk()
        window.eval('tk::PlaceWindow . center')
        window.title(status_a)
        ttk.Label(window, text="select src:", font=("Times New Roman", 10)).grid(column=0, row=15, padx=10, pady=25)
        n = tk.StringVar()
        combo_box = ttk.Combobox(window, width=3, textvariable=n)
        combo_box['values'] = points_tsp
        combo_box.grid(column=1, row=15)
        ttk.Label(window, text="select dest:", font=("Times New Roman", 10)).grid(column=7, row=15, padx=10, pady=25)
        n = tk.StringVar()
        combo_box2 = ttk.Combobox(window, width=3, textvariable=n)
        combo_box2['values'] = points_tsp
        combo_box2.grid(column=14, row=15)
        combo_box2.current(1)
        combo_box.current(0)

        def choose_what_to_mark():
            id2 = int(combo_box2.get())
            id1 = int(combo_box.get())
            test = self.di_graph.remove_edge(id1, id2)
            if test:
                self.get_graph_paint()
                window.destroy()
            else:
                window.destroy()
                tk_notice = tk.Tk()
                tk_notice.eval('tk::PlaceWindow . center')
                tk_notice.title('error')
                ttk.Label(tk_notice, text="something went wrong").grid(column=0, row=0)

                def add_node_no():
                    tk_notice.destroy()
                    self.get_graph_paint()

                ttk.Button(tk_notice, text='Ok', command=add_node_no).grid(column=1, row=1)
                tk_notice.mainloop()

        slogan = tk.Button(window, text="Select", command=choose_what_to_mark)
        slogan.grid(column=22, row=15)
        window.mainloop()
        pygame.display.flip()

    """Clicking on the button in the 'save' menu creates 
           a message where you select the relevant information 
           (The location you want to save the details of the graph in the json file and the name of the new file)"""
    def on_click_button_save(self):
        # global status_a
        status_a = 'save'

        def file_save() -> str:
            top = tk.Tk()
            top.eval('tk::PlaceWindow . center')
            top.withdraw()
            file_name_save = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".json")
            if file_name_save is None:
                str1 = ''
            else:
                str1 = file_name_save.name
            top.destroy()
            return str1

        file_name = file_save()
        from Ex3.src.GraphAlgo import GraphAlgo
        g_algo = GraphAlgo(self.di_graph)
        test = g_algo.save_to_json(file_name)
        if test:
            self.get_graph_paint()
        else:
            tk_notice = tk.Tk()
            tk_notice.eval('tk::PlaceWindow . center')
            tk_notice.title('error')
            ttk.Label(tk_notice, text="something went wrong").grid(column=0, row=0)

            def add_node_no():
                tk_notice.destroy()
                self.get_graph_paint()

            ttk.Button(tk_notice, text='Ok', command=add_node_no).grid(column=1, row=1)
            tk_notice.mainloop()
        pygame.display.flip()

    """Clicking on the button in the 'save' menu creates 
               a message where you select the relevant information 
               (The file you want to import, only a valid json file can be imported, an invalid file will appear message)"""
    def on_click_button_load(self):
        status_a = 'load'

        def prompt_file():
            top = tk.Tk()
            top.eval('tk::PlaceWindow . center')
            top.withdraw()
            file_name = tkinter.filedialog.askopenfilename(parent=top)
            top.destroy()
            return file_name

        f = prompt_file()
        from Ex3.src.GraphAlgo import GraphAlgo
        g_algo1 = GraphAlgo()
        test = g_algo1.load_from_json(f)
        if test is True:
            self.di_graph = g_algo1.get_graph()
            self.get_graph_paint()
        if test is False:
            tk_notice = tk.Tk()
            tk_notice.eval('tk::PlaceWindow . center')
            tk_notice.title('error')

            def add_node_no1():
                tk_notice.destroy()

            ttk.Label(tk_notice, text="something went wrong").grid(column=0, row=0)
            ttk.Button(tk_notice, text='Ok', command=add_node_no1).grid(column=1, row=1)
            tk_notice.mainloop()
        pygame.display.flip()

    """Clicking on the button in the 'tsp' menu creates 
       a message where you select the relevant information 
       (all the points where you want to get the shortest route between all the points on the graph)"""
    def on_click_button_add_edge(self):
        # global status_a
        status_a = 'add edge'
        all_nodes_d = self.di_graph.get_all_v()
        points_tsp = []
        for x in all_nodes_d:
            points_tsp.append(x)
        window = tk.Tk()
        window.eval('tk::PlaceWindow . center')
        window.title(status_a)
        ttk.Label(window, text="select src:", font=("Times New Roman", 10)).grid(column=0, row=15, padx=10, pady=25)
        n = tk.StringVar()
        combo_box = ttk.Combobox(window, width=3, textvariable=n)
        combo_box['values'] = points_tsp
        combo_box.grid(column=1, row=15)
        ttk.Label(window, text="select dest:", font=("Times New Roman", 10)).grid(column=7, row=15, padx=10, pady=25)
        n = tk.StringVar()
        combo_box2 = ttk.Combobox(window, width=3, textvariable=n)
        combo_box2['values'] = points_tsp
        combo_box2.grid(column=14, row=15)
        combo_box2.current(1)
        combo_box.current(0)
        ttk.Label(window, text="select weight:", font=("Times New Roman", 10)).grid(column=15, row=15, padx=10, pady=25)
        box_text = Text(window, height=1, width=5)
        box_text.grid(column=22, row=15)

        def choose_what_to_mark():
            id2 = int(combo_box2.get())
            id1 = int(combo_box.get())
            text_from_box = box_text.get("1.0", 'end-1c')
            window.destroy()

            def add_node_no():
                tk_notice.destroy()
                self.get_graph_paint()

            if self.check_float(text_from_box):
                test = self.di_graph.add_edge(id1, id2, float(text_from_box))
                if test:
                    list_a_n = [id1, id2]
                    self.get_graph_paint(status_a, list_a_n, 0)
                else:
                    tk_notice = tk.Tk()
                    tk_notice.eval('tk::PlaceWindow . center')
                    tk_notice.title('error')
                    ttk.Label(tk_notice, text="There is already a edge between the selected nodes").grid(column=0,
                                                                                                         row=0)
                    ttk.Button(tk_notice, text='Ok', command=add_node_no).grid(column=1, row=1)
                    tk_notice.mainloop()
            else:
                tk_notice = tk.Tk()
                tk_notice.eval('tk::PlaceWindow . center')
                tk_notice.title('error')
                ttk.Label(tk_notice, text="The text listed in weight is not a decimal number").grid(column=0, row=0)
                ttk.Button(tk_notice, text='Ok', command=add_node_no).grid(column=1, row=1)
                tk_notice.mainloop()

        slogan = tk.Button(window, text="Select", command=choose_what_to_mark)
        slogan.grid(column=23, row=15)
        window.mainloop()
        pygame.display.flip()
