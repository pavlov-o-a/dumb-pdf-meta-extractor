# dumb-pdf-meta-extractor
Dumb python script to extract meta info from pdf

This script exctracts meta info from pdf. Script is not optimized and doesnt supprort pdf files with incremental updates if i got adobe pdf reference right.

pdf strucutre with info object position in document and how to find it

![pdf strucutre with meta info position](https://github.com/pavlov-o-a/dumb-pdf-meta-extractor/blob/main/pdf_meta_parcing.jpeg)

We should always start from bottom. At the end of pdf there is "startxref" tag. Right above startxref there is "trailer". Trailer keeps information about all "obj"(objects) of pdf. Meta is listed in "\Info" obj. So we take number of obj for Info in trailer and looking for obj with this nunber above "xref" tag. Above xref tag are obj's which make pdf itself: text, images and some utility obj's like Info.
