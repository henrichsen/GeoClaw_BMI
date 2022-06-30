import numpy as np
import importlib.util
import sys
import os

from bmipy import Bmi


class BMI_GeoClaw(Bmi):
    
    
    _name = "GeoPack GeoClaw Coastal model BMI Wrapper" 
    _input_var_names = ""
    _output_var_names = ""
    
    def __init__(self):        
        self._model = None
        self._values = {}
        self._var_units = {}
        self._var_loc ={}
        self._grids ={}
        self._grid_type ={}
        
        self._Start_time = 0.0
        self._end_time = np.finfo("d").max
        self._time_units = ""
        
        
    ### Model Control Functions    
    def initialize(self,filename=None):
        #filename should be the same as setrun.py
        if filename == None:
            return
        elif isinstance(filename, str):
            spec = importlib.util.spec_from_file_location("setrun",filename)
            module = importlib.util.module_from_spec(spec)
            sys.modules["setrun"]=module
            spec.loader.exec_module(module)
            self._model = module.setrun()
            self._model.write()
            self._file_loc = ("/".join(filename.split("/")[:-1]))
            
        else:
            return
        self._values = self._model.data_list
        self._var_units = {}
        self._var_loc ={}
        self._grids ={}
        self._grid_type ={}
            
        return
    
    def update(self):
        file=os.environ.get("CLAW")+"/clawutil/src/python/clawutil/runclaw.py"
        spec_rc = importlib.util.spec_from_file_location("runclaw",file)
        module_rc=importlib.util.module_from_spec(spec_rc)
        sys.modules["runclaw"]=module_rc
        spec_rc.loader.exec_module(module_rc)
        module_rc.runclaw("xgeoclaw","_output",True, None, ".", False, False, None)
       # /home/jovyan/data/GeoClaw/clawpack/clawutil/src/python/clawutil/runclaw.py xgeoclaw                  _output                True None . False False None
        pass
    def update_until(self,time = 0):
        
        pass
    def finalize(self):
        self._model = None
        pass
    
    
    
    ### Model Information Functions
    def get_component_name(self):
        return self._name

    def get_input_item_count(self):
        return len(self._input_var_names)
    
    def get_output_item_count(self):
        return len(self._output_var_names)

    def get_input_var_names(self):
        return self._input_var_names

    def get_output_var_names(self):
        return self._output_var_names
    
    
    
    ### Variable Information Functions
    def get_var_grid(self, var_name):
        for grid_id, var_name_list in self._grid.items():
            if var_name in var_name_list:
                return grid_id
        #todo: raise exception if var_name not found in grid 
        pass
    def get_var_type(self, variable_name):
        return str(self.get_value_ptr(varable_name).dtype)

    def get_var_units(self, variable_name):
        return self._var_units[varable_name];

    def get_var_itemsize(self, variable_name):
        return np.dtype(self.get_var_type(variable_name)).itemsize

    def get_var_nbytes(self, variable_name):
        return self.get_value_ptr(variable_name).nbytes

    def get_var_location(self, variable_name):
        return self._var_loc[variable_name]
    
    
    
    ### Time Functions
    def get_current_time(self):
        pass
    def get_start_time(self):
        pass
    def get_end_time(self):
        pass
    def get_time_units(self):
        pass
    def get_time_step(self):
        pass
    
    
    
    ### Variable Getter and Setter Functions
    def get_value(self, variable_name, dest):
        dest[:] =self.get_value_ptr(variable_name).flatten()
        return dest

    def get_value_ptr(self, variable_name):
        return self._values[varable_name]
    
    def get_value_at_indices(self, variable_name, dest, inds):
        #verify inds type
        dest[:] = self.get_value_ptr(variable_name).take(inds)
        return dest

    def set_value(self, variable_name, src):
        val = self.get_value_ptr(variable_name)
        val[:] =src.reshape(val.shape)
        return None
    
    def set_value_at_indices(slef, variable_name, inds, src):
        val =self.get_value_ptr(variable_name)
        val.flat[inds] = src
        return None
    
    
    
    ##Model Grid Functions
    def get_grid_type(self,grid):
        pass
    def get_grid_rank(self, grid):
        pass
    def get_grid_size(self, grid):
        pass
    def get_grid_shape(self, grid, shape):
        var_name =self._grids[grid][0]
        shape[:] = self.get_value_ptr(var_name).shape
        return shape
    
    def get_grid_spacing(self, grid, spacing):
        pass
    def get_grid_origin(self, grid, origin):
        #origin is at bottom left of cell
        pass
    def get_grid_x(self, grid, x):
        pass
    def get_grid_y(self, grid, y):
        pass
    def get_grid_z(self, grid, z):
        pass
    def get_grid_node_count(self, grid):
        pass
    def get_grid_edge_count(self, grid):
        pass
    def get_grid_face_count(self, grid):
        pass
    def get_grid_face_edges(self, grid):
        return grid
    def get_grid_edge_nodes(self, grid, edge_nodes):
        #for unstructured grids only
        pass
    def get_grid_edge_edges(self, grid, face_edges):
        #for unstructured grids only
        pass
    def get_grid_face_nodes(self, grid, face_nodes):
        #for unstructured grids only
        pass
    def get_grid_face_nodes(self, grid, face_nodes):
        #for unstructured grids only
        pass
    def get_grid_nodes_per_face(self, grid, nodes_per_face):
        #for unstructured grids only
        pass
    
