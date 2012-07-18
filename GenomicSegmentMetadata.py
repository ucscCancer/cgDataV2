from cgDataV2.GenomicMetadata import GenomicMetadata

class GenomicSegmentMetadata(GenomicMetadata):
    """This class describes the metadata specific to GenomicSegment objects.
    In addition to the metadata common to genomic objects, the genomic segment
    metadata describes the assembly
    """

    def __init__(self, filename, validate=True):
        """Given the pathname of a genomic metadata file, return the
        corresponding metadata object.  By default, run the validator
        method on the new object and return None if validation fails.
        """
        super(Metadata, self).__init__(filename, validate=validate)


    def assembly(self, newAssembly=None):
        """Update the assembly if a new value is specified.
        Return the assembly, or None if not defined.
        """

    def sampleMapMetadata(self):
        """Return the sampleMap metadata object, or None if none is loaded.
        """

    def subtype(self, newSubtyle=None):
        """The subtype indicates the type of GenomicMatrix data.  It is one
        value in a controlled vocabulary.  The expected values include
        ('cna' for copy number data, 'geneExp' for gene expression,
        'miRNAExp' for miRNA expression, 'protein' for protein activity,
        'DNAMethylation' for DNA methylation data, 'siRNAViability' for siRNA
        knockdown viability screens, 'RPPA' for protein activity, 'PARADIGM' for
        activity estimated with Paradigm pathway analysis, and
        'PARADIGM.pathlette' for pathway activity estimated via Paradigm pathlette
        pathway analysis.

        Return the subtype value.
        """
    
