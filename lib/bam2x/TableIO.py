import csv
import bam2x
import sys
from bam2x import IO,Annotation
from bam2x import Translator
hclass = {
    "bed3":Annotation.BED3,
    "bed6":Annotation.BED6,
    "bed12":Annotation.BED12,
    "bed":Annotation.BED6,
    "vcf":Annotation.VCF,
}
htranslate = {
    "bam2bed12": Translator.BamToBed12,
    "bam2fragment":Translator.BamToFragmentIterator,
}
FormatToIterator=dict(hclass.items()+htranslate.items())
def parse(handle,convert_cls,**dict):
    if hclass.has_key(convert_cls):
        return parse_tuples(handle,convert_cls,**dict)
    elif htranslate.has_key(convert_cls):
        return htranslate[convert_cls](handle,**dict)
def parse_tuples(handle,cls,**dict):
    sep="\t"
    if dict.has_key("sep"):
        sep=dict["sep"]
    if isinstance(cls,str):
        if hclass.has_key(cls):
            cls=hclass[cls]
        else:
            raise "can't regonize this format"
    if isinstance(handle,str):
        try:
            handle=IO.fopen(handle,"r")
            for i in csv.reader(handle,delimiter=sep):
                if i[0].strip()[0]=="#": continue
                i=cls._types(i)
                
                yield cls._make(i)
            handle.close()
        except IOError as e:
            print >>sys.stderr,"I/O error({0}): {1}".format(e.errno, e.strerror)
    else:
        try:    
            for i in csv.reader(handle,delimiter=sep):
                if i[0].strip()[0]=="#": continue
                i=cls._types(i)
                yield cls._make(i)
        except:
            raise
            i#print >>sys.stderr,"error({0}): {1}".format(e.errno, e.strerror)


def Main():
    for i in parse(sys.argv[1],"bed12"):
        print i
if __name__=="__main__":
    Main()








