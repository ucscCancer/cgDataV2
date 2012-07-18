
from cgDataV2.Metadata import Metadata

class ClinicalMatrixMetadata(Metadata):
    """This class describes the metadata specific to ClinicalMatrix objects.
    In addition to the metadata common to genomic objects, the clinical matrix
    metadata may contain references to the CinicalFeature metadata.
    """

    def __init__(self, filename, validate=True):
        """Given the pathname of a genomic metadata file, return the
        corresponding metadata object.  By default, run the validator
        method on the new object and return None if validation fails.
        """
        super(Metadata, self).__init__(filename, validate=validate)

    def clinicalFetureMetadata(self):
        """Return the clinicalFeature metadata object, or None if none is loaded.
        """

