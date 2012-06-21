
class ClinicalFeature():
    """A ClinicalFeature object contains a set of descriptions of the 
    clinical data.  The data is represented as a set of rows with three
    columns apiece.  In each row, the first column is the name of the 
    clinical feature, the second is one of (shortTitle, longTitle, valueType,
    state, stateOrder), and the third is a value.  The value is of arbitrary
    format, and is represented as a string.

    Comment: I am assuming that this data will NOT be stored in memory
    all at once, that the common operations involve processing one
    line of data at a time.
    """

    __format__ = {
        "name" : "clinicalFeature",
        "type" : "type",
        "form" : "feature",
        "rowType" : "idMap",
        "colType" : "clinicalFeature",
        "valueType" : "str",
        "nullString" : ""
    }


    def __init__(self, filehandle):
        """Given a handle to a file containing clinical feature data (the file
        is assumed to be open for reading), return a new
        ClinicalFeature object.

        Here again, I'm assuming that the constructor will take one initial
        pass through the file to collect the list of samples and clinical 
        features and verify the file format.  Note, I'm almost tempted to omit
        this functionality from this class, but it's consistent with the other
        classes.
        """

    def read(self, clinicalFeatureName=None):
        """Read a single row from the file and return the contents in a list
        (or tuple?).  If the clinicalFeatureName is None, return the
        data from the next line in the file.  Else, return the data
        for the indicated clinical feature, or None if the feature is
        not found.
        """

    def clinicalFeatureList(self):
        """Return the list of clinical features contained in this feature"""

    def nClinicalFeatures(self):
        """Return the number of clinical features in this feature"""

