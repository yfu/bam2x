__all__=["getseq","query_bam","read","sort","cmpgene","getanno","query_RNASeq","load_bed_to_db","query_db","query_RNA_RPKM","tabix","aggregation","translator","count_compatible_reads","pileup_compatible_reads","aggregation_bed","query_bw","query_tabix","query_RNASeq_bed","remove_small_introns","pileup_to_json"]
from . import *

'''
command lines
'''
commands= {
    "getseq":getseq,
    "getanno":getanno,
    "query_bam":query_bam,
    "query_bw":query_bw,
    "query_tabix":query_tabix,
    "query_RNASeq":query_RNASeq,
    "query_RNASeq_bed":query_RNASeq_bed,
    "query_RNA_RPKM":query_RNA_RPKM,
    "read":read,
    "sort":sort,
    "cmpgene":cmpgene,
    "load_bed_to_db":load_bed_to_db,
    "query_db":query_db,
    "tabix":tabix,
    "aggregation":aggregation,
    "aggregation_bed":aggregation_bed,
    "translator":translator,
    "count_compatible_reads":count_compatible_reads,
    "pileup_compatible_reads":pileup_compatible_reads,
    "pileup_to_json":pileup_to_json,
    "remove_small_introns":remove_small_introns,
}


