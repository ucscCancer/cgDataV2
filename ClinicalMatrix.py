
class ClinicalMatrix():
    """A ClinicalMatrix object contains the clinical data associated with
    a given set of samples.  In this matrix, the rows are samples and
    the columns are clinical features.  Missing values are denoted as blanks.
    """

    __format__ = {
        "name" : "clinicalMatrix",
        "type" : "type",
        "form" : "matrix",
        "rowType" : "idMap",
        "colType" : "clinicalFeature",
        "valueType" : "str",
        "nullString" : ""
    }


    def __init__(self, clinicalMatrixMetadata, validate=True):
        """Given a clinical matrix metadata object, load the
        corresponding ClinicalMatrix object.  By default, the new
        object is validated, and if it fails validation, None is
        returned.  Otherwise, the ClinicalMatrix object is returned.  """



    def sampleList(self):
        """Return the list of samples represented in this matrix"""

    def clinicalFeatureList(self):
        """Return the list of clinical features contained in this matrix"""

    def getValue(self, sampleId, clinicalFeature):
        """Get the data value for the indicated sample and clinical feature"""

    def setValue(self, sample, cliincalFeature, newValue):
        """Update the value stored for the indicated probe and sample
        """

    def nSamples(self):
        """Return the number of samples in this matrix"""

    def nClinicalFeatures(self):
        """Return the number of clinical features in this matrix"""

    def validate(self):
        """Validate this ClinicalMatrix, and return True or False
        depending on whether or not the object passed validation.  """

    def write(self, filename):
        """Write the CinicalMatrix object to the indicated filename"""


