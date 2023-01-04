# simple-data-visualizer
This is a flask app which contains api's consisting of data. Data is used to plot various graphs using matplotlib.


To run the application kindly have python installed in your system.

Create a virtual environment
For windows,
`python -m venv env`
`env\Scripts\activate`
`pip install requirements.txt`

For ubuntu,
`python -m venv env`
`source env\bin\activate`
`pip install requirements.txt`

First, we will start the flask app.
For Windows, run `run-windows.bat` file under flask-api
For Ubuntu, run `run.sh` file under flask-api

Second, we will run graph_invoker.py file using `python graph_invoker.py`