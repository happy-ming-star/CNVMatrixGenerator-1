# CNVMatrixGenerator
Mutational Signatures for copy number alterations

## COPY NUMBER MATRIX GENERATION

In order to generate a copy number matrix, provide the an absolute path to a multi-sample segmentation file obtained from one of the following copy number calling tools (if you have individual sample files, please combine them into one file with the first column corresponding to the sample name):

1. ASCAT
2. ASCAT_NGS
3. SEQUENZA
4. ABSOLUTE
5. BATTENBERG

In addition, provide the name of the project and the output directory for the resulting matrix. The final matrix will be placed in a folder with the name of the project in the directory specified by the output path.

An example to generate the CNV matrix is as follows:

$ python3
```
>>from CNVMatrixGenerator.scripts import CNVMatrixGenerator as scna
>>file_type = "BATTENBERG"
>>input_file = "./example_input/" #example input file for testing
>>output_path = "."
>>project = "Breast_Cancer"
>>scna.generateCNVMatrix(file_type, input_file, project, output_path)

```
