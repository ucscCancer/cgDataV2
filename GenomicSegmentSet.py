class GenomicSegmentSet():
    """This class represents a collection of GenomicSegment objects, such
    as a file with GenomicSegment observations.  

    Note that while the API documentation uses the term GenomicSegment
    to refer to the individual segments and a collection of segments, this
    class contains a collection of segments.  The individual segments are
    represented by the GenomicSegment class.  

    Question: Would a sort method be useful?
    
    See also: GenomicSegmentVector
    """


    def __init__(self, genomicSegmentMetadata, validate=True):
        """Given a genomic segment set metadata object, load the
        corresponding GenomicSegmentSet object.  By default, the new
        object is validated, and if it fails validation, None is
        returned.  Otherwise, the GenomicSegmentSet object is returned.  """

    def sampleList(self):
        """Return the list of samples represented in this GenonicSegmentSet"""

    def nSamples(self):
        """Return the number of samples in this GenomicMatrix"""

    def validate(self):
        """Validate this GenomicSegmentSet. Return True or False depending on whether or
        not the object passed validation.
        """

    def write(self, filename):
        """Write the GenomicSegmentSet object to the indicated filename"""




