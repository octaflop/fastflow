def trimmer(line):
    """
    Simple transformer

    Args: line (bytes): the line of fastq file
    Returns: good_read (str) or None: trims and spits out a valid read
    """
    line = str(line)
    stripped = line.strip().replace('\n', '')
    rna = None
    if stripped.endswith('CACA'):
        rna = stripped[4:-6]
    return rna


