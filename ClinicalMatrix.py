
class ClinicalMatrix():
    """A ClinicalMatrix object contains the clinical data associated with
    a given set of samples.  In this matrix, the rows are samples and
    the columns are clinical features.  Missing values are denoted as blanks.

    Comment: I am assuming that the ClinicalMatrix will NOT be stored in 
    memory all at once, that the common operations involve processing one
    line of data at a time.

    Comment: each row in the file will be represented as a vector of 
    strings, with blanks to denote missing values.
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


    def __init__(self, filehandle):
        """Given a handle to a file containing clinical data (the file is
        assumed to be open for reading), return a new ClinicalMatrix object.

        Here again, I'm assuming that the constructor will take one initial
        pass through the file to collect the list of samples and clinical 
        features and verify the file format.
        """

    def read(self, sampleId=None):
        """Read a single row from the file and return the contents in a list
        (or tuple?).  If the sampleId is None, return the data from
        the next line in the file.  Else, return the data for the
        indicated sample, or None if the sample is not found.
        """

    def sampleList(self):
        """Return the list of samples represented in this matrix"""

    def clinicalFeatureList(self):
        """Return the list of clinical features contained in this matrix"""

    def getValue(self, sampleId, clinicalFeature):
        """Get the data value for the indicated sample and clinical feature"""

    def setValue(self, sample, cliincalFeature, newValue):
        """Update the value stored for the indicated probe and sample
        
        Comment: I wonder if I should bother with this.  I'm not sure how
        I'm going to store the change, and I'm not sure if this functionality
        is necessary.
        """

    def nSamples(self):
        """Return the number of samples in this matrix"""

    def nClinicalFeatures(self):
        """Return the number of clinical features in this matrix"""

