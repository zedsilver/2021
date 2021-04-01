
**Examining the genetic makeup of predominant SARS-CoV-2 strains in California and Correlation with Infection and Death Rates**

	1. Downloaded genomes from NCBI for each Month with collection dates:
Jan 2020, n=7;
Feb 2020, n=9;
Mar 2020, n=1127;
April 2020, n=972;
May 2020, n=673;
June 2020, n=320;
July 2020, n=533;
Aug 2020, n=423;
Sep 2020, n=322;
Oct 2020, n=332;
Nov 2020, n=1079;
Dec 2020, n=2441;
Jan 2021, n=3600;
Feb 2021, n=2657

	2. Installed wtdbg2 to create consensus sequences for each month.
Mkdir CAL20C
Cd CAL20C
git clone https://github.com/ruanjue/wtdbg2
cd wtdbg2 && make
mkdir originals
Mkdir firstassembly
Cd firstassembly

Used FileZilla to copy fastas to originals folder

	3. Ran wtdbg2 and condenser
for FILENAME in ../originals/*.fasta; do newFILENAME=${FILENAME:0:-6}; ./../wtdbg2/wtdbg2 -i $FILENAME -fo ~/CAL20C/firstassembly/$newFILENAME; done

for FILENAME in ../originals/*.ctg.lay.gz; do fileSUFFIX=.ctg.fa; newFILENAME=${FILENAME:0:-11}; ./../wtdbg2/wtpoa-cns -i "$FILENAME" -fo ../firstassembly/$newFILENAME$fileSUFFIX; done

cp ../originals/*.ctg.fa ~/CAL20C/firstassembly/

for FILENAME in *.ctg.fa; do sampleNAME=${FILENAME:0:-7}; fileSUFFIX=_assembled.fasta; sed -i "s/ctg1/$sampleNAME/gi" $FILENAME; done

for FILENAME in *.ctg.fa; do printf '%s\n' "$(cat < "$FILENAME")"; done > assembled_samples.fasta

	4. Assembled sequences
mafft --reorder --localpair assembled_samples.fasta > aligned_samples.aln

	5. Found case and death rates

Found data available from JHU at https://github.com/CSSEGISandData/COVID-19. Wrote script to extract data from .csv to .xls. Run file "extractData.py" within the COVID-19/csse_covid_19_data/ folder.

	6. Determined mutations

Utilized tool “CodonCode Aligner” to determine mutations in each month consensus sequence.

	7. Analyzed data in excel.
	
![image](https://user-images.githubusercontent.com/60581129/113228327-9c337380-9262-11eb-8925-e427c173b619.png)



