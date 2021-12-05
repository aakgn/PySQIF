.. PySQIF documentation master file, created by
   sphinx-quickstart on Sat Dec  4 23:19:18 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PySQIF's documentation!
==================================


==================
PySQIF
==================

PySQIF is an open-source and user-friendly statistical analysis library for SQUIDs/Bi-SQUIDs.
Our library solves Bi-SQUID systems of differential equations. Our methodology is based on
finding the voltage response of the Bi-SQUID for each time steps in the period.
PySQIF library gives the average voltage response of symmetric Bi-SQUID for each corresponding
normalized applied external magnetic flux as an output. The normalized applied external magnetic
flux range can be determined by the user. Moreover, PySQIF provides multiple runs for the statistical
analysis of Bi-SQUID. Users can determine margin and data range for one of the input parameters,
and the tool generates gaussian distributed random numbers in a specific margin and data range
for the ciritical current of shunted Josephson Junction. After that, the voltage response in an external
applied magnetic field is achieved in the defined margin. These output sets, provide a wide range of design
options to the user who can easily observe a reliable working range of Bi-SQUID circuits and can optimize Bi-SQUID
design problems by using this output dataset.
