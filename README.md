# CS340-Client-Server-Development
<b> About the Project </b>

The client, Grazioso-Salvare, needs a software application that can work with existing data from animal shelters to identify and categorize available dogs that can be used for disaster rescue. The purpose of this project was to create a reusable Python module that is able to access MongoDB databases and collections and to use this module to act as a glue level between MongoDB and the client-side Python application, provided as an .ipynb file. Once the database is accessed, the Python module provides methods to perform CRUD operations on the documents within the database collection. This way, the client-side user interface can be used to access a database and its collection and perform CRUD operations on the documents.



<b> Project Funcionality </b>

Starting state of dashboard: 

The table shows each animal of the database on the chart, with the first animal as the default view for the geolocation map. The pie chart will initially show every breed which makes it difficult to read, so it is best to double-click on a breed to isolate it and then single-click on other breeds to add them to the chart. By using the buttons next to each animal on the chart, the geolocation map will update to show the location of the selected animal. Using the water, wilderness, disaster, or reset filters will update the table to show dog breeds that are best suited for that task, or to reset the table to its original state. The pie chart will update to show the distribution of breeds for that filter. Clicking the Grazioso Salvare logo will open the SNHU homepage.

![image](https://user-images.githubusercontent.com/95947696/209023782-7d9a3018-9aef-429e-bee5-7689d78f4213.png)

Water Rescue Filter:

![image](https://user-images.githubusercontent.com/95947696/209025649-c283a644-00fa-47d2-9ab7-e7122a7df63c.png)




