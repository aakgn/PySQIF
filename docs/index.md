# About 

SQUIDpy is an open-source and user-friendly statistical analysis library for  SQUIDs/Bi-SQUIDs. Our library solves Bi-SQUID systems of differential equations. Our methodology is based on finding the voltage response of the Bi-SQUID for each time steps in the period. SQUIDpy library gives the average voltage response of symmetric Bi-SQUID for each corresponding normalized applied external magnetic flux as an output. The normalized applied external magnetic flux range can be determined by the user. Moreover, SQUIDpy provides multiple runs for the statistical analysis of Bi-SQUID. Users can determine margin and data range for one of the input parameters, and the tool generates gaussian distributed random numbers in a specific margin and data range for the said parameter. After that, the voltage response in an external applied magnetic field is achieved in the defined margin. These output sets, provide a wide range of design options to the user who can easily observe a reliable working range of Bi-SQUID circuits and can optimize Bi-SQUID design problems by using this output dataset.

## How SQUIDpy works

For an overview of the SQUIDpy methodology and the algorithmic methods which implement it, go to our technical paper[link](link).

## Authors

SQUIDpy is currently developed and maintained by [Ali AKGUN](https://linkedin.com/in/ali-akgün-592185147) and [Sasan RAZMKHAH](https://linkedin.com/in/razmkhahsasan), Electrical and Electronics Engineering Department, TOBB University of Economics and Technology, Ankara, Turkey. 

## Contact

Don’t hesitate to contact:
- Ali at [ali.akgunphys@gmail.com](ali.akgunphys@gmail.com)
- Sasan at [sasan.razmkhah@gmail.com](sasan.razmkhah@gmail.com)

## Contributing
Your contribution is more than welcome! You can submit pull requests on our Github, or contact [Ali](https://linkedin.com/in/ali-akgün-592185147) if you want to bring big contributions to the project.

## Citing this project

If you find SQUIDpy useful, please consider citing this project as:


This will also help us secure future funding supporting the development of this software.


If you do use SQUIDpy in a publication, please take a few minutes and let us know via email at [ali.akgunphys@gmail.com](ali.akgunphys@gmail.com). We would love to hear how SQUIDpy is being used as a research tool.

## Funding

# Installation
In this installation guide, we used Anaconda environment, you can track all steps by using another enviroment if you want.

## Windows

## Mac

## Linux

# Tutorials
This section provides instructive tutorial to SQUIDpy newbies.
## Input Text File
 SQUIDpy has an input csv file for input protocol with user, this file is named as input.csv in SQUIDpy folder. Figure shows below input parameters of this simulation in input csv file, which can be edited by user.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/zG07rrr/input-text-file.jpg" alt="input-text-file" border="0" /></a>

"input.csv" file has two columns, "circuit_parameters" columns represents Bi-SQUID circuit elements, and "values" columns represents mathematical value of these circuit elements. Figure shows below Bi-SQUID circuit representation:

<a href="https://imgbb.com/"><img src="https://i.ibb.co/tBkg38y/bisquid.png" alt="bisquid" border="0"></a>

- l1a, and l1b represents inductances at top of circuit.
- l2a, and l2b represents inductances at parallel third Josephson Junction.
- l3a, and l3b repesents inductances at bottom of circuit.

## Requirements

SQUIDpy depends on several open-source libraries. The following packages are currently required:

- scipy
- numpy
- Solver
- matplotlib
- statistics
- pandas

# Report a bug

If you are using the SQUIDpy library and think you have found a bug, or if you have questions about installing or using SQUIDpy, please don’t hesitate to contact with us:

- Ali at [ali.akgunphys@gmail.com](ali.akgunphys@gmail.com)
- Sasan at [sasan.razmkhah@gmail.com](sasan.razmkhah@gmail.com)

# Developer Guides

# References
