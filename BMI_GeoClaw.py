import numpy as np
import importlib.util
import sys
import os

from bmipy import Bmi


class BMI_GeoClaw(Bmi):
    
    
    _name = "ClawPack GeoClaw Coastal model BMI Wrapper" 
    _input_var_names = ['pkg', 'num_dim', 'data_list.0.num_dim', 'data_list.0.num_eqn', 'data_list.0.num_waves', 'data_list.0.num_aux', 'data_list.0.output_style', 'data_list.0.output_times', 'data_list.0.num_output_times', 'data_list.0.output_t0', 'data_list.0.output_step_interval', 'data_list.0.total_steps', 'data_list.0.tfinal', 'data_list.0.output_format', 'data_list.0.output_q_components', 'data_list.0.output_aux_components', 'data_list.0.output_aux_onlyonce', 'data_list.0.dt_initial', 'data_list.0.dt_max', 'data_list.0.dt_variable', 'data_list.0.cfl_desired', 'data_list.0.cfl_max', 'data_list.0.steps_max', 'data_list.0.order', 'data_list.0.dimensional_split', 'data_list.0.verbosity', 'data_list.0.verbosity_regrid', 'data_list.0.source_split', 'data_list.0.capa_index', 'data_list.0.limiter', 'data_list.0.t0', 'data_list.0.num_ghost', 'data_list.0.use_fwaves', 'data_list.0.lower', 'data_list.0.upper', 'data_list.0.num_cells', 'data_list.0.bc_lower', 'data_list.0.bc_upper', 'data_list.0.transverse_waves', 'data_list.0.restart', 'data_list.0.restart_file', 'data_list.0.checkpt_style', 'data_list.0.checkpt_interval', 'data_list.0.checkpt_time_interval', 'data_list.0.checkpt_times', 'data_list.1.memsize', 'data_list.1.max1d', 'data_list.1.amr_levels_max', 'data_list.1.refinement_ratios_x', 'data_list.1.refinement_ratios_y', 'data_list.1.variable_dt_refinement_ratios', 'data_list.1.refinement_ratios_t', 'data_list.1.aux_type', 'data_list.1.flag_richardson', 'data_list.1.flag_richardson_tol', 'data_list.1.flag2refine', 'data_list.1.flag2refine_tol', 'data_list.1.regrid_interval', 'data_list.1.regrid_buffer_width', 'data_list.1.clustering_cutoff', 'data_list.1.verbosity_regrid', 'data_list.1.dprint', 'data_list.1.eprint', 'data_list.1.edebug', 'data_list.1.gprint', 'data_list.1.nprint', 'data_list.1.pprint', 'data_list.1.rprint', 'data_list.1.sprint', 'data_list.1.tprint', 'data_list.1.uprint', 'data_list.2.regions', 'data_list.2.num_dim', 'data_list.3.flagregions', 'data_list.3.num_dim', 'data_list.4.gauges', 'data_list.4.file_format', 'data_list.4.display_format', 'data_list.4.q_out_fields', 'data_list.4.aux_out_fields', 'data_list.4.min_time_increment', 'data_list.4.gtype', 'data_list.5.use_adjoint', 'data_list.5.adjoint_outdir', 'data_list.5.adjoint_files', 'data_list.5.numadjoints', 'data_list.5.t1', 'data_list.5.t2', 'data_list.5.innerprod_index', 'data_list.6.gravity', 'data_list.6.rho', 'data_list.6.rho_air', 'data_list.6.ambient_pressure', 'data_list.6.earth_radius', 'data_list.6.coordinate_system', 'data_list.6.coriolis_forcing', 'data_list.6.theta_0', 'data_list.6.friction_forcing', 'data_list.6.manning_coefficient', 'data_list.6.manning_break', 'data_list.6.dry_tolerance', 'data_list.6.friction_depth', 'data_list.6.sea_level', 'data_list.7.topo_missing', 'data_list.7.test_topography', 'data_list.7.topofiles', 'data_list.7.topo_location', 'data_list.7.topo_left', 'data_list.7.topo_right', 'data_list.7.topo_angle', 'data_list.7.x0', 'data_list.7.x1', 'data_list.7.x2', 'data_list.7.basin_depth', 'data_list.7.shelf_depth', 'data_list.7.beach_slope', 'data_list.8.dtopofiles', 'data_list.8.dt_max_dtopo', 'data_list.9.wave_tolerance', 'data_list.9.speed_tolerance', 'data_list.9.deep_depth', 'data_list.9.max_level_deep', 'data_list.9.variable_dt_refinement_ratios', 'data_list.10.fixedgrids', 'data_list.11.qinit_type', 'data_list.11.qinitfiles', 'data_list.11.variable_eta_init', 'data_list.11.force_dry_list', 'data_list.11.num_force_dry', 'data_list.12.fgmax_files', 'data_list.12.num_fgmax_val', 'data_list.12.fgmax_grids', 'data_list.13.wind_forcing', 'data_list.13.drag_law', 'data_list.13.pressure_forcing', 'data_list.13.wind_index', 'data_list.13.pressure_index', 'data_list.13.display_landfall_time', 'data_list.13.wind_refine', 'data_list.13.R_refine', 'data_list.13.storm_type', 'data_list.13.storm_specification_type', 'data_list.13.storm_file', 'data_list.14.variable_friction', 'data_list.14.friction_index', 'data_list.14.friction_regions', 'data_list.14.friction_files', 'data_list.15.num_layers', 'data_list.15.rho', 'data_list.15.eta', 'data_list.15.wave_tolerance', 'data_list.15.eigen_method', 'data_list.15.inundation_method', 'data_list.15.check_richardson', 'data_list.15.richardson_tolerance', 'data_list.15.layer_index', 'data_list.15.dry_limit', 'xclawcmd', 'clawdata.num_dim', 'clawdata.num_eqn', 'clawdata.num_waves', 'clawdata.num_aux', 'clawdata.output_style', 'clawdata.output_times', 'clawdata.num_output_times', 'clawdata.output_t0', 'clawdata.output_step_interval', 'clawdata.total_steps', 'clawdata.tfinal', 'clawdata.output_format', 'clawdata.output_q_components', 'clawdata.output_aux_components', 'clawdata.output_aux_onlyonce', 'clawdata.dt_initial', 'clawdata.dt_max', 'clawdata.dt_variable', 'clawdata.cfl_desired', 'clawdata.cfl_max', 'clawdata.steps_max', 'clawdata.order', 'clawdata.dimensional_split', 'clawdata.verbosity', 'clawdata.verbosity_regrid', 'clawdata.source_split', 'clawdata.capa_index', 'clawdata.limiter', 'clawdata.t0', 'clawdata.num_ghost', 'clawdata.use_fwaves', 'clawdata.lower', 'clawdata.upper', 'clawdata.num_cells', 'clawdata.bc_lower', 'clawdata.bc_upper', 'clawdata.transverse_waves', 'clawdata.restart', 'clawdata.restart_file', 'clawdata.checkpt_style', 'clawdata.checkpt_interval', 'clawdata.checkpt_time_interval', 'clawdata.checkpt_times', 'amrdata.memsize', 'amrdata.max1d', 'amrdata.amr_levels_max', 'amrdata.refinement_ratios_x', 'amrdata.refinement_ratios_y', 'amrdata.variable_dt_refinement_ratios', 'amrdata.refinement_ratios_t', 'amrdata.aux_type', 'amrdata.flag_richardson', 'amrdata.flag_richardson_tol', 'amrdata.flag2refine', 'amrdata.flag2refine_tol', 'amrdata.regrid_interval', 'amrdata.regrid_buffer_width', 'amrdata.clustering_cutoff', 'amrdata.verbosity_regrid', 'amrdata.dprint', 'amrdata.eprint', 'amrdata.edebug', 'amrdata.gprint', 'amrdata.nprint', 'amrdata.pprint', 'amrdata.rprint', 'amrdata.sprint', 'amrdata.tprint', 'amrdata.uprint', 'regiondata.regions', 'regiondata.num_dim', 'flagregiondata.flagregions', 'flagregiondata.num_dim', 'gaugedata.gauges', 'gaugedata.file_format', 'gaugedata.display_format', 'gaugedata.q_out_fields', 'gaugedata.aux_out_fields', 'gaugedata.min_time_increment', 'gaugedata.gtype', 'adjointdata.use_adjoint', 'adjointdata.adjoint_outdir', 'adjointdata.adjoint_files', 'adjointdata.numadjoints', 'adjointdata.t1', 'adjointdata.t2', 'adjointdata.innerprod_index', 'geo_data.gravity', 'geo_data.rho', 'geo_data.rho_air', 'geo_data.ambient_pressure', 'geo_data.earth_radius', 'geo_data.coordinate_system', 'geo_data.coriolis_forcing', 'geo_data.theta_0', 'geo_data.friction_forcing', 'geo_data.manning_coefficient', 'geo_data.manning_break', 'geo_data.dry_tolerance', 'geo_data.friction_depth', 'geo_data.sea_level', 'topo_data.topo_missing', 'topo_data.test_topography', 'topo_data.topofiles', 'topo_data.topo_location', 'topo_data.topo_left', 'topo_data.topo_right', 'topo_data.topo_angle', 'topo_data.x0', 'topo_data.x1', 'topo_data.x2', 'topo_data.basin_depth', 'topo_data.shelf_depth', 'topo_data.beach_slope', 'dtopo_data.dtopofiles', 'dtopo_data.dt_max_dtopo', 'refinement_data.wave_tolerance', 'refinement_data.speed_tolerance', 'refinement_data.deep_depth', 'refinement_data.max_level_deep', 'refinement_data.variable_dt_refinement_ratios', 'fixed_grid_data.fixedgrids', 'qinit_data.qinit_type', 'qinit_data.qinitfiles', 'qinit_data.variable_eta_init', 'qinit_data.force_dry_list', 'qinit_data.num_force_dry', 'fgmax_data.fgmax_files', 'fgmax_data.num_fgmax_val', 'fgmax_data.fgmax_grids', 'surge_data.wind_forcing', 'surge_data.drag_law', 'surge_data.pressure_forcing', 'surge_data.wind_index', 'surge_data.pressure_index', 'surge_data.display_landfall_time', 'surge_data.wind_refine', 'surge_data.R_refine', 'surge_data.storm_type', 'surge_data.storm_specification_type', 'surge_data.storm_file', 'friction_data.variable_friction', 'friction_data.friction_index', 'friction_data.friction_regions', 'friction_data.friction_files', 'multilayer_data.num_layers', 'multilayer_data.rho', 'multilayer_data.eta', 'multilayer_data.wave_tolerance', 'multilayer_data.eigen_method', 'multilayer_data.inundation_method', 'multilayer_data.check_richardson', 'multilayer_data.richardson_tolerance', 'multilayer_data.layer_index', 'multilayer_data.dry_limit']
    _output_var_names = ""
    _model=None
    def __init__(self):        
        self._model = None
        self._values = {}
        self._var_units = {}
        self._var_loc ={}
        self._grids ={}
        self._grid_type ={}
        
        self._start_time = 0.0
        self._end_time = np.finfo("d").max
        self._time_units = "s"
        self._current_time= self._start_time
        
        
    ### Model Control Functions    
    def initialize(self,filename=None):
        #filename should be the same as setrun.py
        if filename == None:
            #todo: raise exception
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
            #todo: raise exception
            return
        
        #define self._values start
        self._values={}
        for i in(vars(self._model)):
            if i[0] =="_":
                continue
            if not "data" in i:
                self._values[i]=vars(self._model).get(i)
            elif i == "data_list":
                for i in self._model.data_list:
                    name="data_list."+str((self._model.data_list.index(i)))
                    for j in vars(i):
                        if  not j[0] in "_":
                            self._values[name+"."+j]=vars(i).get(j)
            elif  i == "amrdata":
                for x in vars(self._model.amrdata):
                    if x[0] == '_':
                        continue
                    else:
                        self._values[i+"."+x]=vars(vars(self._model).get("amrdata")).get(x)
            else:
                for j in vars(vars(self._model).get(i)):
                    if  not j[0] == "_":
                        self._values[i+"."+j]=vars(vars(self._model).get(i)).get(j)
        #define self._values end
        self._start_time = self.get_value('data_list.0.t0')
        self._end_time = self.get_value('data_list.0.tfinal')
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
        self._current_time =self._end_time
        pass
    
    def update_until(self,time = 0):
        #todo: implement function
        self._current_time = time
        pass
    
    def finalize(self):
        self._model.close()
        self._model = None
        self._values =None
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
        return str(type(self.get_value_ptr(variable_name)).__name__)

    def get_var_units(self, variable_name):
        return self._var_units[variable_name];

    def get_var_itemsize(self, variable_name):
        return np.dtype(self.get_var_type(variable_name)).itemsize

    def get_var_nbytes(self, variable_name):
        return sys.getsizeof(self.get_value_ptr(variable_name))

    def get_var_location(self, variable_name):
        pass
    
    
    ### Time Functions
    def get_current_time(self):
        return self._current_time

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def get_time_units(self):
        return self._time_units
        
    def get_time_step(self):
        #return a time step of 0 if variable time steps
        if self.get_value('data_list.0.dt_variable') == 1:
            return 0
        return self.get_value('data_list.0.dt_initial')
        pass
    
    
    
    ### Variable Getter and Setter Functions
    def get_value(self, variable_name, dest):
        dest[:] =np.array(self.get_value_ptr(variable_name),dtype=object).flatten()
        return dest

    def get_value_ptr(self, variable_name):
        return self._values[variable_name]
    
    def get_value_at_indices(self, variable_name, dest, inds):
        #todo throw exception
        dest[:] = self.get_value_ptr(variable_name).take(inds)
        return dest

    def set_value(self, variable_name, src):
        path=variable_name.split(".")
        if path[0]=='data_list':    
            setattr(getattr(self._model,path[0])[int(path[1])],path[2],src)
        elif len(path) == 1:
            setattr(self._model,path[0],src)
        elif len(path) == 2:       setattr(getattr(self._model,path[0]),path[1],src)
        self._values[variable_name]=src
        self._model.write()
        return None
    
    def set_value_at_indices(self, variable_name, inds, src):
        #todo throw exception
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
