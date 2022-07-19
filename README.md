# Basic Model Interface (BMI) with GeoClaw

This is the github repository for the BMI for GeoClaw that can be run in the Next Gen Water Modeling (Ngen) Framework. This is the first coastal model capable in running in the Ngen Framework

## GeoClaw

GeoClaw is one of the models available in [Geopack](https://github.com/clawpack/clawpack). GeoClaw is a coastal model that uses variable resolution to optimise model run times. Additional information on the GeoClaw coastal model can be found at [http://www.clawpack.org/](http://www.clawpack.org/).

## Setup
This documentation assumes that you have a working Ngen environment. For information about setting up a Ngen environment can be found on the Ngen Github page [here](https://github.com/NOAA-OWP/ngen). 

Before running the GeoClaw BMI, Geopack must also be installed. Instructions to install Geopack can be found on their installation page [here](http://www.clawpack.org/installing.html). 

After installing Geopack you will need to set the Environment Variable `CLAW`. This variable defines the loation of Geopack, so that it can run anywhere within the environment. In bash the command will be `export CLAW=/full/path/to/clawpack  # to top level clawpack directory`. Alternatively, the variable can be set in python with `import os /n os.environ["CLAW"] = "/home/jovyan/data/GeoClaw/clawpack"`. more information about defining Environemnt Variables in GeoClaw can be found [here](http://www.clawpack.org/setenv.html). 

## Running the BMI

To run the BMI you first need to run the `init()` function. After running init, you will need to run the initalize funtion. the initialize function inputs a standard setrun.py file for GeoClaw. The BMI then runs the script and can modifiy any of the parameters in the `set_value` function. After initialization, you can run the model to the specified endtime in the setrun.py by running the `update` function, or to any forward time in the `update_until`. Currently backward timesteps are not supported in this BMI, but plans for future version will include this functionality. GeoClaw check points are created for every endtime in the `update` and `update_until` functions. Checkpointing at other times is currently not supported in the version.


## Files needed for the Ngen Framework

To run the BMI in the BMI framework you will need the following files:
##### Setrun.py
This file will be called in the realization file to initalize the model. An example setrun.py named `setrun_Ike.py` is in the example folder of this directory. For the variable `clawdata.t0` it is recommended to use 0 to make it easier to line up the start of the model with the forcing file, as the Ngen Framework starts models at time 0. It is also recommended to have a low `clawdata.num_output_times` as that many outputs will be created for every timestep.
##### Forcing File
Forcing files are required in the Ngen Framework, even though GeoClaw does not use them. This forcing file can be used with other BMI models within the framework. An example forcing file named `forcing_example.csv` can be found in the example folder of this directory.
##### Catchment Files
Catchment Files for catchments and nexuses are also required in the Ngen Framework. Just like the Forcing File, the GeoClaw BMI does not use these files, but are rather used by other BMI models. We recommend using the outlet nexus and catchment to reduce confusion. Example catchment files for both nexuses and catchments can be found in the example folder named `nexus_data.geojson` and `catchment_data.geojson` respecfully.
##### Realization File
The final file needed to run the GeoClaw BMI in the Ngen Framework is the realization file. The realization file defines how different BMIs interact with the framework and eachother. This file defines the setrun.py and forcing file for the BMI. An example Realization File can be found in the example folder named `real_example.json`.

# Running in the Ngen Framework 

After setting up the Ngen framework environment you can run the GeoClaw BMI in the terminal. This can be done by running `ngen <path to catchment forcing file> "<catchment name>" <path to nexus forcing file> "<nexus name>" <path to realization file>`. For example you could run the following command to run the test senerio: `ngen ./example/catchment_data.geojson "cat-27" ./example/nexus_data.geojson "nex-28252" ./example/RealGeoClaw.json`. This will run GeoClaw BMI according to the setrun.py and end time called in the realization file. 
