class GenomicSegmentSet():
    """This class represents a collection of GenomicSegment objects, such
    as a file with GenomicSegment observations.  

    Note that while the API documentation uses the term GenomicSegment
    to refer to the individual segments and a collection of segments, this
    class contains a collection of segments.  The individual segments are
    represented by the GenomicSegment class
    """


    def __init__(self, filehandle):
        """Given a handle to a file containing the GenomicSegment data, 
        return a new GenomicSegmentSet object.  The file is assumed to be
        open for reading.

        Comments: I'm assuming that I'll make an initial read through the
        file to collect a list of samples, verify the format, etc.
        """

    def read(self, sampleId=None):
        """Read a single GenomicSegment object from the file.  If the sampleId
        is None, return the next object from in the file.  Else,
        return the next row for the indicated sampleId, or None if the
        sampleId is not found.
        """

    def sampleList(self):
        """Return the list of samples represented in this GenonicSegmentSet"""

    def nSamples(self):
        """Return the number of samples in this GenomicMatrix"""

