class ProbeMapSet():
    """This class represents a collection of ProbeMap objects, such
    as a file with ProbeMap observations.  

    Here, I'm assuming that what the documentation refers to as "ProbeMap"
    actually refers to a ProbeMapSet, a set of individual ProbeMap vectors.

    See also: ProbeMap.
    
    Note that while the API documentation uses the term ProbeMap
    to refer to the individual segments and a collection of segments, this
    class contains a collection of segments.  The individual segments are
    represented by the ProbeMap class
    """


    def __init__(self, filehandle):
        """Given a handle to a file containing the ProbeMap data, 
        return a new ProbeMapSet object.  The file is assumed to be
        open for reading.

        Comments: I'm assuming that I'll make an initial read through the
        file to collect a list of samples, verify the format, etc.
        """

    def read(self, probeId=None):
        """Read a single ProbeMap object from the file.  If the probeId
        is None, return the next object from in the file.  Else,
        return the next row for the indicated probeId, or None if the
        probeId is not found.
        """

    def probeList(self):
        """Return the list of probes represented in this ProbeMapSet"""

    def nProbes(self):
        """Return the number of probes in this ProbeMapSet"""

