
class ProbeMapVector:
    """A ProbeMapVector is a set of mappings that describe the genomic coordinates
    for the probes in a GenomicMatrix object

    Comment: in the API document, the term 'ProbeMap' seems to refer
    to a set of vectors.  I feel that if the vectors are not kept all
    kept in memory at once, the data is best represented by two
    classes: one to describe each vector, and one to describe the set
    of vectors.  I'm using 'ProbeMapVector' to describe individual vectors
    and 'ProbeMapSet' to describe the set of vectors.

    Each ProbeMapVector contains the following fields:
    * probeId: the name of the probe
    * aliasList: a comma-separated list of aliases (optional but recommended)
    * chrom: name of the chromosome
    * start: starting position within the chromosome or scaffold
    * end: ending position within the chromosome or scaffold.
    * strand: either '+' for forward, '-' for reverse, or '.' for both

    See Also: ProbeMapSet
    """

    __format__ =  {
        "name" : "probeMap",
        "form" : "table",
        "columnOrder" : [
            "probe",
            "aliases",
            "chrom",
            "chrom_start",
            "chrom_end",
            "strand"
            ],
        "primaryKey" : "probe",
        "columnDef" : {
            "chrom_start" : { "type" : "int", "index" : 1 },
            "chrom_end" : { "type" : "int", "index" : 1 }
            }
        }

    def __init__(self, line=None, validate=True):
        """Creates a new ProbeMapVector object.  If line is None, an 
        empty object is returned.  Else, the contents of the ProbeMapVector
        are parsed from the line, which should contain the indicated fields
        and be whitespace-delimited
        If the validate flag is set to True, the object is validated as a
        final initialization step.  If the validation was successful, the new
        object is returned.  Otherwise, the return value is None.
        """

    def validate(self):
        """Validate this ProbeMapVector. Return True or False depending on whether or
        not the object passed validation.
        """

    def write(self, filehandle, delimiter="\t"):
        """Write a ProbeMapVector object to the indicated filehandle.
        The data is written in tab-delimited format by default.
        """


