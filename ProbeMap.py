
class ProbeMap:
    """A ProbeMap is a set of mappings that describe the genomic coordinates
    for the probes in a GenomicMatrix object

    Comment: in the API document, the term "ProbeMap" seems to refer to
    a set of vectors.  I feel that if the vectors are not kept all kept in
    memory at once, the data is best represented by two classes: one to describe
    each vector, and one to describe the set of vectors.  I'm using 'ProbeMap'
    to describe individual vectors and 'ProbeMapSet' to describe the set of
    vectors.

    Each ProbeMap contains the following fields:
    - probeId: the name of the probe
    - aliasList (optional but recommended): a comma-separated list of
      aliases for the quantity (e.g. gene) measured with the probe.
    - chrom: name of the chromosome
    - start: starting position within the chromosome or scaffold
    - end: ending position within the chromosome or scaffold.
    - strand: either '+' for forward, '-' for reverse, or '.' for both
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

    def __init__(self, line=None):
        """Creates a new ProbeMap object.  If line is None, an 
        empty object is returned.  Else, the contents of the ProbeMap
        are parsed from the line, which should contain the indicated fields
        and be whitespace-delimited
        """

    def read(self, filehandle):
        """Read a ProbeMap object from the indicated filehandle.
        Assumes a whitespace-delimited line.
        """

    def write(self, filehandle, delimiter="\t"):
        """Write a ProbeMap object to the indicated filehandle.
        The data is written in tab-delimited format by default.
        """


