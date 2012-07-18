
from cgDataV2.GenomicMatrixMetadata import GenomicMatrixMetadata

import sys

class GenomicMatrix():
    """GenomicMatrix objects contain sets of experimental observations.
    They operate on files that are structured as matrices, with the
    rows representing probes and the columns representing samples.
    Each cell, representing the intersection of one probe and one
    sample, represents one single experimental observation
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

    def __init__(self, genomicMatrixMetadata, validate=True):
        """Given a genomic matrix metadata object, load the
        corresponding GenomicMatrix object.  By default, the new
        object is validated, and if it fails validation, None is
        returned.  Otherwise, the GenomicMatrix object is returned.
        """

    def probeList(self):
        """Return the list of probes represented in this GenomicMatrix
        """

    def sampleList(self):
        """Return the list of samples represented in this GenonicMatrix"""

    def observationsByProbe(self, probe):
        """Given a probe, return a vector of the experimental observations
        from the GenomicMatrix for this probe

        Question: would it be most useful if the data was returned as a
        vector or a dictionary keyed by sample?
        """

    def observationsBySample(self, sample):
        """Given the name of a sample from the GenomicMatrix, return the
        set of experimental observations for this sample.

        Question: would it be most useful if the data was returned as a
        vector or a dictionary keyed by probe?
        """

    def getValue(self, probe, sample):
        """Get the data value for the indicated probe and sample"""

    def setValue(self, probe, sample, newValue):
        """Update the value stored for the indicated probe and sample
        """

    def nProbes(self):
        """Return the number of probes in this GenomicMatrix"""

    def nSamples(self):
        """Return the number of samples in this GenomicMatrix"""

    def validate(self):
        """Validate this GenomicMatrix. Return True or False depending on whether or
        not the object passed validation.
        """

    def write(self, filename):
        """Write the GenomicMatrix object to the indicated filename"""

