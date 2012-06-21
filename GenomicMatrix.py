
import sys

class GenomicMatrix():
    """GenomicMatrix objects contain sets of experimental observations.
    They operate on files that are structured as matrices, with the
    rows representing probes and the columns representing samples.
    Each cell, representing the intersection of one probe and one
    sample, represents one single experimental observation

    Comment: I feel like the GenomicMatrix object should actually be a list of 
    GenomicVector classes, where each GenomicVector contains a probe ID and 
    a vector of floats (or perhaps a hash keyed by the sample name).  If that
    seems like too much abstraction, speak up now.

    Comment: How should we write out a new GenomicMatrix?  Should we 
    even provide such a method?  I've provided a way to write out 
    a GenomicVector, but one would still need to write out the first line
    with the sample names.
    """
    __format__ = {
        "name" : "genomicMatrix",
        "type" : "type",
        "form" : "matrix",
        "rowType" : "probeMap",
        "colType" : "sampleMap",
        "valueType" : "float",
        "nullString" : "NA",
        "links" : {
            "dataSubType" : {}
            }
        }

    def __init__(self, filehandle):
        """Given a handle to a file containing the GenomicMatrix data, 
        return a new GenomicMatrix object.  The file is assumed to be
        open for reading.

        Comments: perhaps the constructor could read through the file once,
        collect the list of probes, perform a rudimentary format check, and
        then reopen to the beginning of the file.  It would incur some overhead,
        but would permit some useful housekeeping.
        """

    def read(self, probe=None):
        """Read a single row from the file and return the contents in a
        GenomicVector object.  If the probe is None, return the next
        GenomicVector in the file.  Else, return the next
        GenomicVector for the indicated probe, or None if the probe is
        not found.
        """

    def probeList(self):
        """Return the list of probes represented in this GenomicMatrix

        Comments: if the constructor makes one initial pass through the file
        (see __init()__), then the probeList could be stored internally.
        """

    def sampleList(self):
        """Return the list of samples represented in this GenonicMatrix"""

    def getValue(self, probe, sample):
        """Get the data value for the indicated probe and sample"""

    def setValue(self, probe, sample, newValue):
        """Update the value stored for the indicated probe and sample
        
        Comment: I wonder if I should bother with this.  I'm not sure how
        I'm going to store the change, and I'm not sure if this functionality
        is necessary.
        """

    def nProbes(self):
        """Return the number of probes in this GenomicMatrix"""

    def nSamples(self):
        """Return the number of samples in this GenomicMatrix"""



