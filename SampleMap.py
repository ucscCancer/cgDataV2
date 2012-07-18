
class SampleMap:
    """The SampleMap connects the samples in GenomicMatrix objects to the
    clinical data in ClinicalMatrix objects, and relates sample IDs in
    a parent-child model.  This model expresses that one patient can
    have a tumor sample and a normal sample, the tumor and normal
    biopsies can both yield multiple laboratory samples, and so forth.

    This data is described in a two-column file.  In the simplest case
    (with no relationships), each sample ID appears on one line in both
    columns: (sampleId sampleId)
    In the more general case (with parent-child relationships), there is
    also some line with the parent in the left column and the child in the
    right.  For example, in the case of one parent and one child, the file
    would look like this:
    1. parent parent
    2. parent child
    3. child child
    """

    def __init__(self, sampleMapMetadata, validate=True):
        """Given a sample map metadata object, load the
        corresponding SampleMap object.  By default, the new
        object is validated, and if it fails validation, None is
        returned.  Otherwise, the SampleMap object is returned.  """

    def getSampleList(self):
        """Return a list of the samples contained in this SampleMap."""

    def getParent(self, sampleId):
        """Given a sample ID, return its parent.  If the sample ID has no parent,
        return None.
        """

    def getChildren(self, sampleId):
        """Given a sample ID, return its children.  If the sample has no children,
        return None.
        """

    def validate(self):
        """Validate this SampleMap. Return True or False depending on whether or
        not the object passed validation.
        """

    def write(self, filename):
        """Write the SampleMap object to the indicated filename"""



    
        



