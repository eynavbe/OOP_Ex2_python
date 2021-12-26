# OOP_Ex2_python
## 
The GUI works through a pygame and thus displays the directed graph that receives its details for creating the graph.
The dots represent the nodes within each node listed the id of the node
The arrow marks the direction of the edge and where it is linked.
The small rectangles within which there are a decimal number that are on the arrow mark the weight of the edge while the rectangle farther from the point (src) marks the weight up to the point (dest that the rectangle is closer to).
### Initial run of T0.json file
**pic 1:** Initial execution of T0.json file This file does not receive pos data (the geographical location of the node) so when the algorithm "loads" the file and adds the data to the data structures in DiGraph it creates random data for pos so that x will be a decimal number between 35 and 36 (Not including 36) and y will be a decimal number between 32 and 33 (not including 33).
<img width="490" alt="1" src="https://user-images.githubusercontent.com/93534494/147417503-aa046ab2-77e0-4c5d-8def-d3f8ceb5087c.png">

### "CENTER_POINT" button in the menu of an unconnected graph
**pic 2:** By going to the "CENTER_POINT" button in the menu, the button changes color to dark pink, pressing the "CENTER_POINT" button in the menu displays a message at the bottom of the page "no center point" that the graph is not linked so there can be no midpoint for the graph.

<img width="491" alt="2" src="https://user-images.githubusercontent.com/93534494/147417766-fcc83a54-1ad4-4816-93bc-f4e93cf8d86e.png">

### "REMOVE_NODE" button in menu
**pic 3:** By going to the "REMOVE_NODE" button in the menu, the button changes color to dark pink, by pressing the "REMOVE_NODE" button a message will open where you select the node's id, you will have the option to select id from the existing list of nodes. In the image, id 1 is selected and then click "Select" for the message to close and the update will appear on the screen according to the node you have chosen to download (in this specific example it will be id 1)

<img width="492" alt="3" src="https://user-images.githubusercontent.com/93534494/147417817-1984b960-1444-4fc9-8cd0-def72969654e.png">

**pic 4:** As you can see in the picture node with id 1 has indeed been deleted and so have all the ribs that are connected to it (ribs can not be connected to a non-existent node).

<img width="492" alt="4" src="https://user-images.githubusercontent.com/93534494/147417820-22fe07bd-ef5b-4301-ae58-75d2579eb7f2.png">

### "SAVE_FILE" button in menu:
**pic 5:** By pressing the "SAVE_FILE" button in the menu, the button changes its color to dark pink, pressing the "SAVE_FILE" button opens a screen where you select the place where you want to save the file and the name of the new file and then click "Save", if not Fill in the correct name and you will get an error message.

<img width="568" alt="5" src="https://user-images.githubusercontent.com/93534494/147417986-90e2a69a-7e81-43b3-9370-5858193a1983.png">

**pic 6:** Proof that the file was saved in the location you chose to save with the name. The saved file is attached to the date folder.

<img width="638" alt="6" src="https://user-images.githubusercontent.com/93534494/147417995-c99679c9-50bc-44d2-9258-b661c170ce0b.png">

### LOAD_FILE menu button:
**pic 7:** By pressing the "LOAD_FILE" button in the menu, the button changes color to dark pink, by pressing the "LOAD_FILE" button a screen opens where you select the file you want to display on the graph and then click "Open", if the file is incorrect you will get an error message . pic 7 is an example when an invalid file is selected.

<img width="557" alt="7" src="https://user-images.githubusercontent.com/93534494/147418079-c4bdf659-d7f3-4f76-864d-9f0c3d1f157d.png">

**pic 8:** The error message that appears that an incorrect file was selected according to pic 7.

<img width="488" alt="8" src="https://user-images.githubusercontent.com/93534494/147418083-746445c2-4896-40ab-b294-5584da065b9d.png">

**pic 9:** By pressing the "LOAD_FILE" button in the menu, the button changes color to dark pink, by the clicking "LOAD_FILE" button a screen opens where you select the file you want to display on the graph and then click "Open", if the file is incorrect you will get an error message . pic 9 is an example when a valid file is selected. The A1.json file is attached to the data folder.

<img width="557" alt="9" src="https://user-images.githubusercontent.com/93534494/147418085-cd02e9a2-5647-4666-9ca5-fc5d396b9878.png">

**pic 10:** The result on the graph after running the normal file according to pic 9.

<img width="489" alt="10" src="https://user-images.githubusercontent.com/93534494/147418155-d5248df2-174e-4f9f-ae4b-4503622c29c7.png">

### CENTER_POINT button in the connected graph menu
**pic 11:** By pressing the "CENTER_POINT" button in the menu, the button changes color to dark pink, pressing the "CENTER_POINT" button displays a message at the bottom of the page "min-maximum distance:" Then the distance in the specific example is 9.93 and the graph will be marked in red.

<img width="487" alt="11" src="https://user-images.githubusercontent.com/93534494/147418161-4b7ff2b4-339c-4bdb-b8d2-71b0ec6654c9.png">

### "TSP" menu button:
**pic 12:** By going to the "TSP" button in the menu, the button changes its color to dark pink, pressing the "TSP" button in the menu opens a message where you select the noded id, you will have the option to select an id list from the existing nodes id list. In the image the id 0,4,5,6 is selected and then click on "Select" so that the message closes and the shortest route will appear on the screen that will go through any ID list you selected.

<img width="540" alt="12" src="https://user-images.githubusercontent.com/93534494/147418239-1b38929b-c36e-424c-a752-30318a86fbb9.png">

**pic 13:** The route is marked in red according to the points selected in Figure 12 (0,4,5,6) so that the route passes through all the nodes and is also the shortest possible route passing through these points. And a message will appear at the bottom of the page "the overall distance:" and then the distance in the specific example is 7.91

<img width="486" alt="13" src="https://user-images.githubusercontent.com/93534494/147418246-3c58ad01-5937-4cf1-9dfb-c2e0acefad37.png">

### "GRAPH" button in the menu:
**pic 14:** By pressing the "GRAPH" button in the menu, the button changes its color to dark pink, pressing the "GRAPH" button in the algorithm draws the graph without all the markings that each of the different menus marks (displays the graph as in the first run).

<img width="491" alt="14" src="https://user-images.githubusercontent.com/93534494/147418526-999c8143-fbf5-4aaa-b71c-cb8818715d90.png">

### "SHORTEST PATH" button in the menu:
**pic 15:** By pressing the "SHORTEST PATH" button in the menu, the button changes its color to dark pink, pressing the "SHORTEST PATH" button in the menu opens a message where you select src and dest, you will have the option to select from the list id of existing nodes. In the image, select 0.9 and then click "Select" so that the message closes and the shortest route appears on the screen so that the output is 0 and the destination is 9, if there is no route (possible only in an unlinked graph) a message "no path between the points" will appear.

<img width="492" alt="15" src="https://user-images.githubusercontent.com/93534494/147418529-c0e5492a-fedd-4818-90e9-3a8102ecd480.png">

**pic 16:** The route is marked in red according to the points selected in Figure 12 (that the origin will be 0 and the destination will be 9) so that the route is the shortest route in the order of origin and destination. And a message will appear at the bottom of the page "the overall distance:" then the distance in the specific example is 8.97 the exact result is 8.969663987876642 but only one number is taken after the decimal point and what after the number is rounded i.e. 3.878 the number 3.88 will be printed and in the specific example chosen it will be 8.97.

<img width="485" alt="16" src="https://user-images.githubusercontent.com/93534494/147418532-c7ab1e10-0d12-4048-90c5-d344e2cc6926.png">

### "REMOVE_EDGE" button in menu:
**pic 17:** By pressing the "REMOVE_EDGE" button in the menu, the button changes color to dark pink, pressing the "REMOVE_EDGE" button in the menu opens a message where you select src and dest, you will have the option to select from the list id of existing nodes. Then clicking "Select" will delete the edge when the origin and destination according to what you selected if no edge exists a message will appear. In the image, an output is selected that is 0 and a destination that is 1 (such an edge exists).

<img width="486" alt="17" src="https://user-images.githubusercontent.com/93534494/147418592-56d8b60c-0451-4f9c-bc01-091cfe896015.png">

**pic 18:** You can see that the edgh selected in the previous image has been deleted (find that it is 0 and destination that it is 1)

<img width="489" alt="18" src="https://user-images.githubusercontent.com/93534494/147418594-01407c6a-e314-4733-adf1-1b9e70abbcef.png">

### "REMOVE_NODE" button in menu:
**pic 19:** By pressing the "REMOVE_ NODE" button in the menu, the button changes color to dark pink, pressing the "REMOVE_ NODE" button in the menu opens a message where you select id node, you will have the option to select from an existing list of nodes. Then clicking "Select" will delete the node. In the image an id is selected which is 3.

<img width="489" alt="19" src="https://user-images.githubusercontent.com/93534494/147418671-ee53a5e7-5919-460b-afe6-70f578978ddd.png">

**pic 20:** You can see that the node has been deleted and so has the entire edge that is connected to it (it is not possible to be connected to a node that does not exist)

<img width="487" alt="20" src="https://user-images.githubusercontent.com/93534494/147418672-75206664-1194-4f91-8629-2a24e26ce6f8.png">

### add node by clicking on a point on the screen with the mouse:
**pic 21:** Clicking on a point on the screen will display a message that "You want to add node at this point?" Clicking "Yes" will add a dot where you clicked with the mouse, clicking "No" will not add a dot.

<img width="487" alt="21" src="https://user-images.githubusercontent.com/93534494/147418712-0ef4ff40-f1d0-4c30-a923-9a2b1f3e6fd5.png">

**pic 22:** Demonstrate that he added the dot where you clicked with the mouse the dot is marked in red for emphasis.

<img width="489" alt="22" src="https://user-images.githubusercontent.com/93534494/147418714-5af8cf39-c1b0-4f77-be25-6c4d19fe90c0.png">

**pic 23:** Clicking "CENTER_POINT" in the menu displays a message at the bottom of the page "no center point" that the graph is not linked because of the point added in 
pic 22 so there can be no midpoint for the graph.

<img width="490" alt="23" src="https://user-images.githubusercontent.com/93534494/147418715-c3f266bf-60f9-4201-baee-9265ff52b92e.png">

### "ADD_EDGE" button in menu:
**pic 24:** By going to the "ADD_EDGE" button in the menu, the button changes its color to dark pink, clicking on the "ADD_EDGE" button in the menu opens a message where you select src and you will have the option to select from the existing id list of nodes. And enter a decimal number as weight if what you wrote down in weight an error message will appear, then clicking "Select" will add the edge. It can be seen in the image that id 3 deleted in image 20 does not appear in the list, a selected image finds that it is 0 and a destination that is 1 (such an edge exists).

<img width="500" alt="24" src="https://user-images.githubusercontent.com/93534494/147418743-8a2c5680-2d96-4899-ae9f-200718879e1d.png">

**pic 25:** In the picture we chose to add an edge so that the origin is 0 and the destination is 17 and the weight is 11.

<img width="490" alt="25" src="https://user-images.githubusercontent.com/93534494/147418745-4f959438-6585-4ef7-8ace-d645018eca56.png">

**pic 26:** Marked with the red edge added according to the details of Figure 25 (whose origin is 0 and target is 17 and weight is 11).

<img width="494" alt="26" src="https://user-images.githubusercontent.com/93534494/147418747-f029ce53-3636-485a-bf34-de4f91f45e5e.png">




