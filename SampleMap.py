
Class SampleMap:
    """The SampleMap connects the samples in GenomicMatrix objects to the
    clinical data in ClinicalMatrix objects, and relates sample IDs in
    a parent-child model.  This model expresses that one patient can
    have a tumor sample and a normal sample, the tumor and normal
    biopsies can both yield multiple laboratory samples, and so forth.

    This data is described in a two-column file.  In the simplest case
    (with no relationships), each sample ID appears on one line in both
    columns:
        sampleId sampleId
    In the more general case (with parent-child relationships), there is
    also some line with the parent in the left column and the child in the
    right.  For example, in the case of one parent and one child, the file
    would look like this:
        parent parent
        parent child
        child child

    I need more information before I can do justice to this class.
    How will the data be used?  Is it best to have it all loaded into
    memory, or read from a file one line at a time (which would have the
    advantage of consistency with the other classes)?  To be determined.
    """



