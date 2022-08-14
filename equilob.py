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
    class scales:
        pass
    class file:
        pass
    class ptransp:
        pass
        class file:
            pass
        class prof:
            pass
        class param:
            pass
        class geom:
            pass
        class disch:
            pass
    
        

        
    def __init__(self,eq_id):
      import numpy as np
      print('okey makey') #Nobody could hate this
      self.file.id = eq_id;
      self.file.eq_dir = '../equil_files/';
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
      self.geom.sepfilename = eq.file.eq_dir+'sep_curve_'+eq.file.id+'.dat'
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
      self.scales.mu0  = 4.*np.pi*1e-7;     ## (kg.m/C^2)  
      self.scales.a    = Minor_Radius;   ## (m) Minor Radius
      self.scales.B0   = Vac_Tor_Field;  ## (T) Vacuum Toroidal Field
      self.scales.I0   = 1.e-6*self.scales.a*self.scales.B0/self.scales.mu0; ## (MA)    Current
      self.scales.J0   = self.scales.B0/(self.scales.mu0*self.scales.a);     ## (A/m^2) Current density
      self.scales.Phi0 = self.scales.B0*self.scales.a**2;                      ## (Wb)    Magnetic Flux
      self.scales.p0   = self.scales.B0**2/self.scales.mu0;                    ## (Pa)    Thermal Pressure
      ### ============================================================
    
      ### ===================================================
      ### Target data for selfibrium solver
      ### Data used by GS_Update_RHS
      ### ===================================================
      self.target.solver = 'nul';   ## 
      self.target.seed   = 'eig';   ##
      ### ===================================================
      
      def getdata(self,file):
          lablist=["150320W04","154692W02","154358W03","154359W02","147394S01","147634S01","155543W09"]
          if type(file) == int & size(file) in range(0,7):
              file=lablist(file)
          elif type(file) == int & size(file) not in range(0,7):
              print('If you are typing an int input, it mush be between 0 and 6')
          elif type(file) == str & file not in lablist:
              print('If you are typing an string as input, it must be in the next list:')
              print('Valid data ID list: ', lablist)
              
              
                

        
ob=eq('dif_01')
#equ=selfibrium()
#self.numpar.solver.Nmeshsize = 300

