# CS340-Client-Server-Development
<b> About the Project </b>

The client, Grazioso-Salvare, needs a software application that can work with existing data from animal shelters to identify and categorize available dogs that can be used for disaster rescue. The purpose of this project was to create a reusable Python module that is able to access MongoDB databases and collections and to use this module to act as a glue level between MongoDB and the client-side Python application, provided as an .ipynb file. Once the database is accessed, the Python module provides methods to perform CRUD operations on the documents within the database collection. This way, the client-side user interface can be used to access a database and its collection and perform CRUD operations on the documents.



<b> Project Functionality </b>

The table shows each animal of the database on the chart, with the first animal as the default view for the geolocation map. The pie chart will initially show every breed which makes it difficult to read, so it is best to double-click on a breed to isolate it and then single-click on other breeds to add them to the chart. By using the buttons next to each animal on the chart, the geolocation map will update to show the location of the selected animal. Using the water, wilderness, disaster, or reset filters will update the table to show dog breeds that are best suited for that task, or to reset the table to its original state. The pie chart will update to show the distribution of breeds for that filter. Clicking the Grazioso Salvare logo will open the SNHU homepage.

Starting state of dashboard: 


![image](https://user-images.githubusercontent.com/95947696/209023782-7d9a3018-9aef-429e-bee5-7689d78f4213.png)

Water Rescue Filter:


![image](https://user-images.githubusercontent.com/95947696/209025649-c283a644-00fa-47d2-9ab7-e7122a7df63c.png)

<br>
<br>

<b> Tools Used </b>

MongoDB
<br>
&emsp;•	MongoDB was used because it is a good way to store and retrieve data and is compatible with many programming languages, including Python which was used for this project. It stores data in BSON format meaning that applications can receive the data in JSON format, which is helpful when using MongoDB with Python because using Python dictionaries make both simple and advanced querying a straightforward task. MongoDB has a driver for Python, PyMongo, which allows for easy connection to the database.
<br>
<br>
Dash Framework
<br>
&emsp;•	Dash was used to build the dashboard and is great for building a customized interface, especially with Python. It provides methods to build many different interactive options, such as the radio items, datatable, geolocation map, and pie chart that were used in this project. Combined with Dash callbacks, a fully interactive and functional dashboard interface can be built. Since it is compatible with Python and Python is compatible with MongoDB, it is a valuable tool for integrating the functionalities of all three together.
<br>
<br>
Jupyter Notebook
<br>
&emsp;•	Jupyter Notebook was used to write the CRUD Python module as a .py file, and to test the module in a .ipynb Python script. The dashboard was also created in a .ipynb Python script.

<br>
<br>

<b> Reproducing the Project </b>

•	Have the AAC database ready to access or import it through the terminal.
<br>
•	Enable user authentication for the database and connect to the MongoDB server under that user.
<br>
•	Use a tool like Jupyter Notebook to open the .ipynb dashboard file and the .py CRUD Python module.
<br>
•	In the dashboard code, edit the instantiation of the CRUD Python module to the correct username, password, and port number.
<br>
•	Run the code to view the dashboard. As mentioned before the pie chart will be crowded, so double-click on one breed to isolate and single-click to add more breeds to the chart.
<br>
•	Use the radio buttons next to each row to see that animal’s location on the map. Hover over the marker to see their breed and click the marker to see their name.
<br>
•	Use the radio buttons above the chart to filter for dogs that are best suited to the job specified by the button. Again, breeds on the pie chart may be selected/deselected for a customized view.
<br>
•	If more specific filters are desired, text can be typed in the empty box above any column to perform a specific query.
<br>
•	Click the Grazioso Salvare logo to be redirected to the client homepage.





