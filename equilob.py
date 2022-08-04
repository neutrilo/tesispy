#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 19:56:30 2022

@author: albert
"""

class eq:
    def explain(self):
        print ("This is the plasma equlibrium dataset")

    def autor(self):
        print('Neutrilo')
    def author(self):
        print('Neutrilo')
    #Definimos la estructura 
    class numpar:
       pass
       class solver:
           pass
           class Ip_correct:
                pass
    class target:
        pass
        class param:
            pass
    class geom:
        pass
        

        
    def __init__(self):
      import numpy as np
      # print('okey makey')
      # self.file.id = eq_id;
      # self.file.eq_dir = '../self_files/';
      # ### =====================================
      
      ### =============================================================================
      ### Numerical scheme variables. Grid sizes. Solver tolerances and Max. it. number
      ### =============================================================================
      ### Profile grid size
      self.numpar.Nrho = 100;    ## Size of rho_hat grid for plasma profiles
      self.numpar.Nrad = 200;    ## Size of radial grid
    
      ### Solver Parameters
      self.numpar.solver.Nmeshsize = 300;  ## Number of nodes at plasma boundary (passed to the FEM solver to build mesh)
      self.numpar.solver.Ncont     = 100;  ## Number of flux contours to compute selfibrium quantities
      self.numpar.solver.Nsubmesh  = 200;  ## Size of the sub mesh generated for each plasma contour
    
      self.numpar.solver.Newton_tol   = 1.e-4;  ## Tolerance for Newton solver
      self.numpar.solver.Newton_maxit = 20;     ## Maximum number of iterations for Newton solver
      self.numpar.solver.qsol_tol     = 0.1;    ## Tolerance for Newton solver
      self.numpar.solver.qsol_maxit   = 10;     ## Maximum number of iterations for Newton solver
    
      ## Relaxation factor for the ('second') correction term for ggp_sim
      self.numpar.solver.qqrho_factor = 0.5;
      
      ## Target q profile is corrected to match target Ip
      ## To disable the correction set self.target.param.Ipcorrect.factor = 0.;
      self.numpar.solver.Ip_correct.factor = 1.; ## correction factor from 0 to 1
      self.numpar.solver.Ip_correct.exp    = 25;  ## order of polynomial correction
      self.numpar.solver.iqerr = np.arange(4,95);
      ### =============================================================================
      self.target.param.target = 1;
      ### =============================================================================
    
      ### ============================================================
      ### Basic default specification of the separatrix
      ### ============================================================
      ## Definition options:  [ 'PTRANSP'   'file'   'function' ]
      self.geom.definition  = 'function'; 
 #    self.geom.sepfilename = [self.file.eq_dir,'sep_curve_',self.file.id,'.dat'];
      self.geom.sepfromfile = 'sep_iter.dat';
      self.geom.Nsep   = 300;
      self.geom.R0     = 2.85;
      self.geom.kappa  = 1.8;
      self.geom.delta  = 0.35;
      self.geom.NRgrid = 100;
      self.geom.NZgrid = 180;
      self.geom.agrid  = 1.05;
      self.geom.kgrid  = 1.05;
      ### ============================================================
      
      ### ============================================================
      ### Default specification of Reference/Normalizing scales
      ### ============================================================
      Minor_Radius  = 0.6;     ## (m) Minor Radius
      Vac_Tor_Field = 2.0;    ## (T) Vacuum Toroidal Field
 #   self = GS_self_Set_Scales(self,Minor_Radius,Vac_Tor_Field);
      ### ============================================================
    
      ### ===================================================
      ### Target data for selfibrium solver
      ### Data used by GS_Update_RHS
      ### ===================================================
      self.target.solver = 'nul';   ## 
      self.target.seed   = 'eig';   ##
      ### ===================================================
                

        
ob=eq()
#equ=selfibrium()
#self.numpar.solver.Nmeshsize = 300

