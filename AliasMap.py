
class AliasMap():
    """An AliasMap object links probes to other sets of identifiers.  For
    example, an alias map might map probes to gene names

    (To appear)
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

    def __init__(self):
        """(to appear)"""
