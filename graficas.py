#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:55:30 2022

@author: albert
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from equilob import eq

style = 2

if style == 1:
    equilibrio=eq('dif_01')
    fig = plt.figure(figsize=(18, 24))
    outer = gridspec.GridSpec(4, 2, wspace=0.2, hspace=0.3)
    title1 = 'Corriente total del plasma'
    title2 = 'Potencia total de los haces de neutrones'
    title3 = 'Potencia total de radiacion de ciclotron'
    xlab = 'Tiempo (s)'
    ylab1 = 'Corriente (MA)'
    ylab2 = 'Potencia (MW)'
    
    for i in range(7):
        inner = gridspec.GridSpecFromSubplotSpec(3, 1,
                        subplot_spec=outer[i], wspace=0.1, hspace=0.5)
        
        #Data extraction
        equilibrio.getdata(i)
        tittle_main = 'Corrida experimental ' + equilibrio.run_name + '\n'
        t = equilibrio.ptransp.disch.t
        I0 = equilibrio.ptransp.disch.Ip
        pnb_tot = equilibrio.ptransp.disch.pnb_tot
        pec_tot = equilibrio.ptransp.disch.pec_tot
        
        #Ploting
        # inner.title(tittle_main)
        #Subplot(fig, outer[i]).set_title(tittle_main)
        # plt.title(tittle_main)
        # inner.suptitle(tittle_main, fontsize=16)
        # fig.title(tittle_main, fontsize=16)
        
        ax = plt.Subplot(fig, outer[i])
        ax.set_title(tittle_main, fontsize=16)
        # ax.set_xticks([])
        # ax.set_yticks([])
        ax.axis('off')
        fig.add_subplot(ax)
        
        ax = plt.Subplot(fig, inner[0])
        ax.plot(t, I0)
        ax.set_xticks([])
        ax.grid()
        ax.set_title(title1)
        ax.set_ylabel(ylab1)
        fig.add_subplot(ax)
        
        ax = plt.Subplot(fig, inner[1])
        ax.plot(t, pnb_tot/1e6)
        ax.set_xticks([])
        ax.grid()
        ax.set_title(title2)
        ax.set_ylabel(ylab2)
        fig.add_subplot(ax)
        
        ax = plt.Subplot(fig, inner[2])
        ax.plot(t, pec_tot/1e6)
        ax.grid(visible=None, which='major', axis='y')
        ax.set_title(title3)
        ax.set_ylabel(ylab2)
        ax.set_xlabel(xlab)
        fig.add_subplot(ax)
        
        
        print(i)
        
    
    fig.suptitle('Analisis de descargas',fontsize=20)
    fig.show()
    
    
elif style ==2:
    equilibrio=eq('dif_01')
    fig = plt.figure(figsize=(16, 20))
    outer = gridspec.GridSpec(4, 2, wspace=0.2, hspace=0.3)
    title1 = 'Corriente total del plasma'
    title2 = 'Potencia de haces de neutrones'
    title3 = 'Potencia de radiacion de ciclotron'
    xlab = 'Tiempo (s)'
    ylab1 = 'Corriente (MA)'
    ylab2 = 'Potencia (MW)'
    for i in range(7):
        inner = gridspec.GridSpecFromSubplotSpec(1, 1,
                        subplot_spec=outer[i], wspace=0.1, hspace=0.3)
        
        #Data extraction
        equilibrio.getdata(i)
        tittle_main = 'Corrida experimental ' + equilibrio.run_name 
        t = equilibrio.ptransp.disch.t
        I0 = equilibrio.ptransp.disch.Ip
        pnb_tot = equilibrio.ptransp.disch.pnb_tot
        pec_tot = equilibrio.ptransp.disch.pec_tot
        
        #Ploting
        # inner.title(tittle_main)
        #Subplot(fig, outer[i]).set_title(tittle_main)
        # plt.title(tittle_main)
        # inner.suptitle(tittle_main, fontsize=16)
        # fig.title(tittle_main, fontsize=16)
        
        ax = plt.Subplot(fig, outer[i])
        ax.set_title(tittle_main, fontsize=16)
        # ax.set_xticks([])
        # ax.set_yticks([])
        ax.axis('off')
        fig.add_subplot(ax)
        
        ax = plt.Subplot(fig, inner[0])
        ax.plot(t, I0, label = title1 + ' (MA)')
        ax.plot(t, pnb_tot/1e6, label = title2 + ' (MW)')
        ax.plot(t, pec_tot/1e6, label = title3 + ' (MW)')
        ax.legend(loc='upper left')
        ax.grid('minor')
        ax.set_xlabel(xlab)
        # ax.set_ylabel(ylab1)
        fig.add_subplot(ax)
        
        # ax = plt.Subplot(fig, inner[1])
        # ax.plot(t, pnb_tot/1e6)
        # ax.set_xticks([])
        # ax.grid()
        # ax.set_title(title2)
        # ax.set_ylabel(ylab2)
        # fig.add_subplot(ax)
        
        # ax = plt.Subplot(fig, inner[2])
        # ax.plot(t, pec_tot/1e6)
        # ax.grid(visible=None, which='major', axis='y')
        # ax.set_title(title3)
        # ax.set_ylabel(ylab2)
        # fig.add_subplot(ax)
        
        
        print(i)
        
    
        # for j in range(3):
        #     ax = plt.Subplot(fig, inner[j])
        #     plt.plot(t, I0)
        #     # t = ax.text(0.5,0.5, 'outer=%d, inner=%d' % (i, j))
        #     # t.set_ha('center')
        #     # ax.set_xticks([])
        #     # ax.set_yticks([])
        #     fig.add_subplot(ax)
        #     # plt.plot(t, I0, 'outer=%d, inner=%d' % (i, j))
    fig.suptitle('Analisis de descargas',fontsize=20)
    fig.show()