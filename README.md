# OOP_Ex2_python
## 
The GUI works through a pygame and thus displays the directed graph that receives its details for creating the graph.
The dots represent the nodes within each node listed the id of the node
The arrow marks the direction of the edge and where it is linked.
The small rectangles within which there are a decimal number that are on the arrow mark the weight of the edge while the rectangle farther from the point (src) marks the weight up to the point (dest that the rectangle is closer to).
### Initial run of T0.json file
**pic 1:** Initial execution of T0.json file This file does not receive pos data (the geographical location of the node) so when the algorithm "loads" the file and adds the data to the data structures in DiGraph it creates random data for pos so that x will be a decimal number between 35 and 36 (Not including 36) and y will be a decimal number between 32 and 33 (not including 33).
<img width="490" alt="1" src="https://user-images.githubusercontent.com/93534494/147417503-aa046ab2-77e0-4c5d-8def-d3f8ceb5087c.png">

### "CENTER_POINT" button in the menu of an unlinked graph
**pic 2:** By going to the "CENTER_POINT" button in the menu, the button changes color to dark pink, pressing the "CENTER_POINT" button in the menu displays a message at the bottom of the page "no center point" that the graph is not linked so there can be no midpoint for the graph.

<img width="491" alt="2" src="https://user-images.githubusercontent.com/93534494/147417766-fcc83a54-1ad4-4816-93bc-f4e93cf8d86e.png">

### "REMOVE_NODE" button in menu
**pic 3:** By going to the "REMOVE_NODE" button in the menu, the button changes color to dark pink, by pressing the" "REMOVE_NODE" button a message will open where you select the node's id, you will have the option to select id from the existing list of nodes. In the image, id 1 is selected and then click "Select" for the message to close and the update will appear on the screen according to the node you have chosen to download (in this specific example it will be id 1)

<img width="492" alt="3" src="https://user-images.githubusercontent.com/93534494/147417817-1984b960-1444-4fc9-8cd0-def72969654e.png">

**pic 4:** As you can see in the picture node with id 1 has indeed been deleted and so have all the ribs that are connected to it (ribs can not be connected to a non-existent node).

<img width="492" alt="4" src="https://user-images.githubusercontent.com/93534494/147417820-22fe07bd-ef5b-4301-ae58-75d2579eb7f2.png">

### "SAVE_FILE" button in menu:
**pic 5:** By pressing the "SAVE_FILE" button in the menu, the button changes its color to dark pink, pressing the "SAVE_FILE" button opens a screen where you select the place where you want to save the file and the name of the new file and then click "Save", if not Fill in the correct name and you will get an error message.

<img width="568" alt="5" src="https://user-images.githubusercontent.com/93534494/147417986-90e2a69a-7e81-43b3-9370-5858193a1983.png">

**pic 6:** Proof that the file was saved in the location you chose to save with the name. The saved file is attached to the date folder.

<img width="638" alt="6" src="https://user-images.githubusercontent.com/93534494/147417995-c99679c9-50bc-44d2-9258-b661c170ce0b.png">

