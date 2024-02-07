import numpy as np
import os,sys
import math
from sklearn.cluster import KMeans
import scipy.stats as sp
import uproot

def getData(fname="", procName="Events"):
    file = uproot.open(fname)
    dq_dict = file[procName].arrays(library="np")
    dq_events = {
        "Hits":{
            "detID": dq_dict["hit_detID"],
            "edep": dq_dict["hit_edep"],
            "elmID": dq_dict["hit_elmID"],
            "hit_pos": dq_dict["hit_pos"]
        },
        "track":{
            "x": dq_dict["track_x_st3"],
            "y": dq_dict["track_y_st3"],
            "Cal_x": dq_dict["track_x_CAL"],
            "Cal_y": dq_dict["track_y_CAL"],
            "ID": dq_dict["eventID"],
            "pz": dq_dict["track_pz_st1"]
        },
        "st23": {
            "ntrack23": dq_dict["n_st23tracklets"],
            "px":   dq_dict["st23tracklet_px_st3"],
            "py":   dq_dict["st23tracklet_py_st3"],
            "pz":   dq_dict["st23tracklet_pz_st3"],
            "x":   dq_dict["st23tracklet_x_st3"],
            "y":   dq_dict["st23tracklet_y_st3"],
            "z":   dq_dict["st23tracklet_z_st3"],
            "Cal_x": dq_dict["st23tracklet_x_CAL"],
            "Cal_y": dq_dict["st23tracklet_y_CAL"]
        },
        "gen":{
            "pz": dq_dict["gpz"]
        },
    }

    return dq_events

#--------------------------------------------------------------------------------------------------------------------------------------------

ntowersx=72
ntowersy=36
sizex=5.53 # in cm
sizey=5.53 # in cm
ecalx=[-200,200] #size in cm
ecaly=[-100,100]
binsx=ecalx[1]- ecalx[0]
binsy=ecaly[1]- ecaly[0]
sfc = 0.1146337964120158 #sampling fraction of emcal
emin=0.0005
seed_threshold=0.2

#--------------------------------------------------------------------------------------------------------------------------------------------

def emcal_byevent(dq_hits, evtNum):
    raw_elmID = dq_hits["elmID"][evtNum]
    raw_edep = dq_hits["edep"][evtNum]
    
    emcal_mask = dq_hits["detID"][evtNum] == 100
    eng_mask = raw_edep[emcal_mask] >= emin
    
    elmID = raw_elmID[emcal_mask][eng_mask]
    edep = raw_edep[emcal_mask][eng_mask]
    
    emcal_towerx = elmID // ntowersy
    emcal_towery = elmID % ntowersy
    emcal_edep = edep / sfc
    
    seed_coord, seed_eng = find_energy_seeds_neighbour(emcal_towerx, emcal_towery, emcal_edep)
    
    emcal_x = ecalx[0] + emcal_towerx * sizex
    emcal_y = ecaly[0] + emcal_towery * sizey
   
    
    return emcal_x, emcal_y, emcal_edep, seed_coord, seed_eng

def find_energy_seeds_neighbour(x_cell, y_cell, edep):
    energy_grid = np.zeros((ntowersx, ntowersx))
    energy_grid[x_cell, y_cell] = edep  # Assign energy values based on x_cell and y_cell indices
    
    seed_energy_mask = energy_grid > seed_threshold
    
    # Create padded version of the energy grid to handle edge cases
    padded_energy_grid = np.pad(energy_grid, pad_width=1, mode='constant', constant_values=0)
    
    # Pre-compute slices for neighbor comparison
    center_slice = padded_energy_grid[1:-1, 1:-1]
    neighbors = [
        padded_energy_grid[0:-2, 0:-2], padded_energy_grid[0:-2, 1:-1], padded_energy_grid[0:-2, 2:],
        padded_energy_grid[1:-1, 0:-2],                                   padded_energy_grid[1:-1, 2:],
        padded_energy_grid[2:  , 0:-2], padded_energy_grid[2:  , 1:-1], padded_energy_grid[2:  , 2:]
    ]
    
    # Find seeds: cells with energy > 0.2 and higher than all their neighbors
    seed_mask = seed_energy_mask & np.all(np.dstack([center_slice > neighbor for neighbor in neighbors]), axis=2)
    
    # Return indices of seeds
    seed_grids = np.argwhere(seed_mask)
    seed_eng = energy_grid[seed_mask]
    seed_coords = np.array([ecalx[0], ecaly[0]]) + seed_grids * np.array([sizex, sizey])
 
    
    return seed_coords, seed_eng



def emcal_bytuple(dq_events):
    dq_hits = dq_events["Hits"]
    x_pos, y_pos, eng, seed_pos = [], [], [], []

    for i in range(len(dq_hits["edep"])):
        emcal_x, emcal_y, emcal_edep, seeds, seedeng = emcal_byevent(dq_hits, i)
        x_pos.append(emcal_x)
        y_pos.append(emcal_y)
        eng.append(emcal_edep)
        seed_pos.append(seeds)

    return x_pos, y_pos, eng, seed_pos
