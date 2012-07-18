class GenomicSegmentVector():
    """GenomicSegmentVector objects indicate which segments were
    present in the indicated samples, and with what score For example,
    copy number data can be represented as GenomicSegmentVectors.

    Each GenomicSegmentVector contains the following fields:
    - sampleId: the name of the sample in which the segment was observed
    - chrom: name of the chromosome
    - start: starting position within the chromosome or scaffold
    - end: ending position within the chromosome or scaffold.
    - strand: either '+' for forward, '-' for reverse, or '.' for both
    - score: floating point score for the segment

    Comment: in the API document, the term "GenomicSegment" seems to
    refer to a file of genomic segment observations.  But I feel like
    there are two different classes: GenomicSegmentVector objects, in
    which each object represents the observation of one segment in one
    indicated sample; and GenomicSegmentSet objects, representing a
    set of GenomicSegmentVectors that are contained together in a
    file.

    See Also: GenomicSegmentSet
    """

    __format__ = {
            "name" : "genomicSegment",
            "type" : "type",
            "form" : "table",
            "columnOrder" : [
                "id",
                "chrom",
                "chrom_start",
                "chrom_end",
                "strand",
                "value"
            ],
            "groupKey" : "id",
            "columnDef" : {
                "chrom_start" : { "type" : "int" },
                "chrom_end" :   { "type" : "int" },
                "value" : { "type" : "float" }
            }
        }

    def __init__(self, line=None, validate=True):
        """Creates a new GenomicSegmentVector object.  If line is
        None, an empty object is returned.  Else, the contents of the
        GenomicSegmentVector are parsed from the line, which should
        contain the indicated fields and be whitespace-delimited.
        If validate is True, then the validator is run on the object
        as a final initialization step.  If successful, the object is
        returned.  Else, None is returned.
        """

    def validate(self):
        """Validate this GenomicSegmentVector. Return True or False
        depending on whether or not the object passed validation.  """

    def write(self, filehandle, delimiter="\t"):
        """Write a GenomicSegmentVector object to the indicated
        filehandle.  The data is written in tab-delimited format by
        default.
        """



