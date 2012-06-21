
import sys

class GenomicVector():
    """GenomicVector objects contain a set of observations for a given
    probe across a number of samples.  Each GenomicVector object
    contains the following fields: 
    - probe: the name of the probe 
    - observations: a hash of experimental observations for this probe.  
      The keys are the sample names, and the values are the experimental
      observations.  If any observation is missing, the sample is still a 
      key in the hash, but the value is None.

    Question: does it make more sense to have the list of observations
    be a hash or a vector?  It depends on the expected use cases.
    A vector would make more sense if multiple GenomicVectors would be 
    operated on together, as it's more efficient.  But if you'd operate on
    one GenomicVector at a time, then it might make more sense to store
    them in a hash, to make the mapping to sample more explicit.  Note that
    if they're stored in a hash, I'll have to do something to preserve
    the correct column order when they're written out.

    Note that missing values in the input files can appear as NA,
    blank tokens, etc., but will be parsed to None.

    See also: GenomicMatrix
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

    def __init__(self, line=None):
        """If line is None, return an empty GenomicVector object.  Else,
        parse a GenomicVector object from the line (assumed to be 
        whitespace-delimited) and return the contents.
        """

    def write(self, filehandle):
        """Writes the genomicVector object to the filehandle.  It is
        assumed that the filehandle is already open for writing.
        """

    def getValue(self, sample):
        """Get the data value for the indicated sample"""

    def setValue(self, sample, newValue):
        """Update the value stored for the indicated sample"""

    def nSamples(self):
        """Return the number of samples in this GenomicVector"""



