dq_events = getData(file1, "Events")

(x, y, eng, labels, labels_decrease, seeds, seed_labels) = multi_clusters(dq_events)#here performed clustering
(h4x, h4y) = h4_bytuple(dq_events)

dq_st23 = dq_events["st23"]
dq_track = dq_events["track"]
trkls_coord = np.stack((dq_st23["x"], dq_st23["y"], dq_st23["z"], dq_st23["px"], dq_st23["py"], dq_st23["pz"]), axis=1)
trkls_cal = np.stack((dq_st23["Cal_x"], dq_st23["Cal_y"]), axis=1)
track_st3 = np.stack((dq_track["x"], dq_track["y"], dq_track["pz"]), axis=1)
whole_tuple_result = []
i=266
evt_result=[]

trkl_cal = np.array(trkls_cal[i].tolist()).T
evt_h4x = np.unique(h4x[i], axis=0)
evt_h4y = np.unique(h4y[i], axis=0)
trkl_coord = np.array(trkls_coord[i].tolist()).T

if len(h4x) or len(h4y):#prepare evt_h4
    ext_h4x, ext_h4y = extp_trkl(trkls_coord[i])
    evt_h4 = []
    for val in range(41, 47):#get the experiment value of h4
        if val <= 44:
            evt_h4.append(evt_h4y[evt_h4y[:, 0] == float(val)])
        else:
            evt_h4.append(evt_h4x[evt_h4x[:, 0] == float(val)])

for label in labels_decrease[i]:
    hits_mask = (labels[i] == label)
    cluster_info = [
        gen_wid(x[i][hits_mask], y[i][hits_mask]),
        gen_wew(x[i][hits_mask], y[i][hits_mask], eng[i][hits_mask]),
        seeds[i][seed_labels[i] == label]
    ]

    distances = np.linalg.norm(trkl_cal - cluster_info[2], axis=1)
    idx = distances.argmin()

    if distances[idx] <= 8:
        cluster_info.extend([trkl_coord[idx],#append st3 trkl xyzpxpypz, h4 info
                             #trkl_Ep(trkl_coord[idx], eng[i][hits_mask]),
                             h4_matchup(ext_h4y[idx], evt_h4[:4]),
                             h4_matchup(ext_h4x[idx], evt_h4[4:])])


    else:
        cluster_info.append(np.full(13, -9999))
    evt_result.append(unfold_output(cluster_info))
whole_tuple_result.append(evt_result)
