
class AliasMap():
    """An AliasMap object links probes to other sets of identifiers.  For
    example, an alias map might map probes to gene names

    Melissa's Assumptions: I might be wrong, but here's my impression.  It looks
    like this is a set of key-value pairs, where the key is the probe name and the value
    is some alias that it might also be known by.  Yes?

    Question: can a probe have more than one alias in a single AliasMap?
    """

    __format__ =  {
            "name" : "aliasMap",
            "type" : "type",
            "form" : "table",
            "columnOrder" : [
            "probe",
            "alias"
            ],
            "groupKey" : "probe"
            }

    def __init__(self, aliasMapMetadata, validate=True):
        """Given an alias map metadata object, load the corresponding AliasMap
        object.  By default, the new object is validated, and if it fails validation,
        None is returned.  Otherwise, the AliasMap object is returned.
        """

    def probeList(self):
        """Return the list of probes included in this AliasMap"""

    def aliasList(self):
        """Return the list of aliases included in this AliasMap"""

    def aliasThisProbe(self, probe):
        """Return the alias for the indicated probe, or None if it is not in this
        AliasMap.
        """

    def validate(self):
        """Validate this AliasMap, and return True or False depending on whether or
        not the object passed validation.
        """

    def write(self, filename):
        """Write the AliasMap to the indicated filename."""
