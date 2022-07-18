# Basic Model Interface (BMI) with GeoClaw

This is the github repository for the BMI for GeoClaw that can be run in the Next Gen Water Modeling (Ngen) Framework. This is the first coastal model capable in running in the Ngen Framework

## GeoClaw

GeoClaw is one of the models available in [Geopack](https://github.com/clawpack/clawpack). GeoClaw is a coastal model that uses variable resolution to optimise model run times. Additional information on the GeoClaw coastal model can be found at [http://www.clawpack.org/](http://www.clawpack.org/).

## Setup
Before running the GeoClaw BMI, Geopack must first be installed. Instructions to install Geopack can be found on their installation page [here](http://www.clawpack.org/installing.html). 

After installing Geopack you will need to set the Environment Variable `CLAW`. This variable defines the loation of Geopack, so that it can run anywhere within the environment. In bash the command will be `export CLAW=/full/path/to/clawpack  # to top level clawpack directory`  depending on the directory. Alternatively, the variable can be set in python with ` `. more information about defining Environemnt Variables in GeoClaw can be found [here](http://www.clawpack.org/setenv.html). 

## Running in Python


## Running in the Ngen Framework
