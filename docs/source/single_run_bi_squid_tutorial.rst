*******************************
Bi-SQUID Single Run Simulation
*******************************

Input Text File Preparation
==================

Firstly, we should prepare input text file for our simulation goals.
Input csv file content is shown in below for this tutorial. Input csv file
represents circuit and simulation parameters. Download link for this input csv file:
https://github.com/aakgn/PySQIF/blob/main/docs/tutorial_resources/bi-squid_single_run.csv




Visualization
==================

Finally, we can visualize our results by using PySQIF Plot module. As we did before
firstly, we should import and construct our Plot module ,and then we can plot our results
by using the plot method.

``from PySQIF.Plot import Plot as plt``

``plot = plt(voltage_response)``

``plot.plot(voltage_response)``

Figure shows output visualization below:

.. image:: ../images/bi-squid-output.png
   :width: 200
