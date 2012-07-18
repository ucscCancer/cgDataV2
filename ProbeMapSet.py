class ProbeMapSet():
    """This class represents a collection of ProbeMap objects, such
    as a file with ProbeMap observations.  

    Here, I'm assuming that what the documentation refers to as "ProbeMap"
    actually refers to a ProbeMapSet, a set of individual ProbeMap vectors.

    Note that while the API documentation uses the term ProbeMap
    to refer to the individual segments and a collection of segments, this
    class contains a collection of segments.  The individual segments are
    represented by the ProbeMap class

    See Also: ProbeMapVector.

    Question: Would a sort method be useful?
    """


    def __init__(self, probeMapSetMetadata, validate=True):
        """Given a probeMap set metadata object, load the
        corresponding ProbeMapSet object.  By default, the new
        object is validated, and if it fails validation, None is
        returned.  Otherwise, the ProbeMapSet object is returned.  """


    def probeList(self):
        """Return the list of probes represented in this ProbeMapSet"""

    def nProbes(self):
        """Return the number of probes in this ProbeMapSet"""

    def validate(self):
        """Validate this ProbeMapSet. Return True or False depending on whether or
        not the object passed validation.
        """

    def write(self, filename):
        """Write the ProbeMapSet object to the indicated filename"""

