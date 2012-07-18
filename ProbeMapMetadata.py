
from cgDataV2.Metadata import Metadata

class ProbeMapMetadata(Metadata):
    """This class describes the metadata relating to ProbeMap objects.  In addition
    to the common metadata, ProbeMap metadata specifies the genomic assembly.
    """

    def assembly(self, newAssembly=None):
        """Update the assembly if a new value is specified.
        Return the assembly, or None if not defined.
        """

    
