import pcbnew


class TrackLength:
    def __init__(self, id):
        self.id = id
        self.tracks = []
        self.vias = []

    def add_tracks(self, tracks):
        self.tracks = tracks
    
    def add_vias(self, vias):
        self.vias = vias
    
    def add_track(self, track):
        self.tracks.append(track)
    
    def add_via(self, via):
        self.vias.append(via)

class Via:
    def __init__(self, via):
        self.via = via
        self.start = None
        self.end = None
    
    def add_start(self, layer):
        self.start = layer

    def add_end(self, layer):
        self.end = layer

class Current:
    def __init__(self, startpoint, startlayer, endpoint, endlayer):
        self.startpoint = startpoint
        self.startlayer = startlayer
        self.endpoint = endpoint
        self.endlayer = endlayer
        self.via1 = None
        self.via2 = None

def get_track_length(netname):
    board = pcbnew.GetBoard()
    netcode = board.GetNetcodeFromNetname(netname)
    tracks = board.TracksInNet(netcode)
    sum = 0.0
    for track in tracks:
        if track.GetClass() != "VIA":
            sum += track.GetLength()
    length = round(sum/pcbnew.IU_PER_MM, 4)
    return length

def get_min_track_lenght(reference1, pad1, reference2, pad2, stackups):
    board = pcbnew.GetBoard()
    start_pad = board.FindFootprintByReference(reference1).FindPadByNumber(pad1)
    end_pad = board.FindFootprintByReference(reference2).FindPadByNumber(pad2)
    net_name = start_pad.GetNetname()
    net_code = board.GetNetcodeFromNetname(net_name)
    tracks = list(board.TracksInNet(net_code)) #Convert Tuple to List
    start_pad_layer = board.FindFootprintByReference(reference1).IsFlipped()
    end_pad_layer = board.FindFootprintByReference(reference2).IsFlipped()

    startpoint = start_pad.GetPosition()
    startlayer = 'Any'
    if start_pad.GetAttribute() == pcbnew.PAD_ATTRIB_SMD:
        if start_pad_layer == True:
            # F_Cu = 31
            startlayer = pcbnew.B_Cu
        else:
            # F_Cu = 0
            startlayer = pcbnew.F_Cu

    endpoint = end_pad.GetPosition()
    endlayer = 'Any'
    if end_pad.GetAttribute() == pcbnew.PAD_ATTRIB_SMD:
        if end_pad_layer == True:
            endlayer = pcbnew.B_Cu
        else:
            endlayer = pcbnew.F_Cu

    isLoop = True
    isEnd = True
    trackslength = []
    trackslength.append(TrackLength(0))
    currents = []
    currents.append(Current(startpoint, startlayer, endpoint, endlayer))
    print('currents %s' %(len(currents)))
    print('trackslength %s' %(len(trackslength)))
    while (len(tracks)) > 0 and (isLoop == True) and (isEnd == True):
        isEnd = False
        for track in tracks:
            for index, current in enumerate(currents, start=0):
                if track.GetClass() == 'PCB_VIA':
                    via_point = track.GetPosition()
                    if current.startpoint == via_point:
                        via = Via(track)
                        via.add_start(current.startlayer)
                        trackslength[index].add_via(via)
                        current.via1 = len(trackslength[index].vias) -1
                        current.startlayer = 'Any'
                        tracks.remove(track)
                        isEnd = True
                    if current.endpoint == via_point:
                        via = Via(track)
                        via.add_start(current.endlayer)
                        trackslength[index].add_via(via)
                        current.via2 = len(trackslength[index].vias) - 1
                        current.endlayer = 'Any'
                        tracks.remove(track)
                        isEnd = True
                else:
                    point_start = track.GetStart()
                    point_end = track.GetEnd()
                    track_layer = track.GetLayer()
                    if current.startpoint == point_start and (current.startlayer == track_layer or current.startlayer == 'Any'):
                        if track not in trackslength[index].tracks:
                            if current.startlayer == 'Any':
                                trackslength[index].vias[current.via1].add_end(track_layer)
                            trackslength[index].add_track(track)
                            current.startpoint = point_end
                            current.startlayer = track_layer
                            tracks.remove(track)
                            isEnd = True
                    elif current.startpoint == point_end and (current.startlayer == track_layer or current.startlayer == 'Any'):
                        if track not in trackslength[index].tracks:
                            if current.startlayer == 'Any':
                                trackslength[index].vias[current.via1].add_end(track_layer)
                            trackslength[index].add_track(track)
                            current.startpoint = point_start
                            current.startlayer = track_layer
                            tracks.remove(track)
                            isEnd = True

                    if current.endpoint == point_start and (current.endlayer == track_layer or current.endlayer == 'Any'):
                        if track not in trackslength[index].tracks:
                            if current.endlayer == 'Any':
                                trackslength[index].vias[current.via2].add_end(track_layer)
                            trackslength[index].add_track(track)
                            current.endpoint = point_end
                            current.endlayer = track_layer
                            tracks.remove(track)
                            isEnd = True
                    elif current.endpoint == point_end and (current.endlayer == track_layer or current.endlayer == 'Any'):
                        if track not in trackslength[index].tracks:
                            if current.endlayer == 'Any':
                                trackslength[index].vias[current.via2].add_end(track_layer)
                            trackslength[index].add_track(track)
                            current.endpoint = point_start
                            current.endlayer = track_layer
                            tracks.remove(track)
                            isEnd = True
                    
                if current.startpoint == current.endpoint and (current.startlayer == current.endlayer):
                    isLoop = False
    
    print('trackslength via %d ' %(len(trackslength[0].vias)))
    for via in trackslength[0].vias:
        stackupsv = []
        stackupsv.clear()
        start = 2*via.start - 2
        end  = 2*via.end - 2
        if start < 0:
            start = 0
        if end >= len(stackups):
            end = len(stackups)
            stackupsv = stackups[start:]
        else:
            stackupsv = stackups[start:end]
        print('start %d end %d ' %(start, end))
        offset = (stackupsv[0].thickness + stackupsv[len(stackupsv) - 1].thickness)/2
        via_length = 0
        for item in stackupsv:
            via_length += item.thickness
            print('name %s %f' %(item.name, item.thickness))
        via_length = via_length - offset
        print('x via %f ' %(via_length))

    sum = 0.0
    for track in trackslength[0].tracks:
        startpoint = track.GetStart()
        endpoint = track.GetEnd()
        ind = trackslength[0].tracks.index(track) + 1
        print('%d, %s,%s' %(ind, startpoint, endpoint))
        sum += track.GetLength()
    length = round(sum/pcbnew.IU_PER_MM, 4)
    print('trackslength %d %7.4f' %(len(trackslength[0].tracks), length))
    return length
