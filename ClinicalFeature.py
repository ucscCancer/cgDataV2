
class ClinicalFeature():
    """A ClinicalFeature object contains a set of descriptions of the 
    clinical data.  The data is represented as a set of rows with three
    columns apiece.  In each row, the first column is the name of the 
    clinical feature, the second is one of (shortTitle, longTitle, valueType,
    state, stateOrder), and the third is a value.  The value is of arbitrary
    format, and is represented as a string.

    Question: would it be correct to assume that all of these values are unique
    per feature, i.e. that any feature can have no more than one shortTitle, longTitle,
    state?

    Question: would a sort method be useful?
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


    def __init__(self, clinicalFeatureMetadata, validate=True):
        """Given a clinical feature metadata object, load the
        corresponding ClinicalFeature object.  By default, the new
        object is validated, and if it fails validation, None is
        returned.  Otherwise, the ClinicalFeature object is returned.  """

    def featuresByName(self, name):
        """Return the list of features pertaining to the named feature"""

    def featuresByType(self, type):
        """Return the list of features of the indicated type"""

    def nClinicalFeatures(self, name=None):
        """Return the number of clinical features in this object.
        If name is specified, return only the number of features relating
        to the named feature.  Otherwise, return the total number of features
        in this set.
        """

    def validate(self):
        """Validate this ClinicalFeature. Return True or False depending on whether or
        not the object passed validation.
        """

    def write(self, filename):
        """Write the ClinicalFeature object to the indicated filename"""


