
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

![image](https://user-images.githubusercontent.com/60581129/113228405-cd13a880-9262-11eb-9617-122157a7b9d0.png)

	8. Doing it all again, but on a weekly basis.

| Week ID | Week Start | Week End   | Week                    |   |
|---------|------------|------------|-------------------------|---|
| W1      | 4/1/2020   | 4/7/2020   | 04/01/2020 - 04/07/2020 |   |
| W2      | 4/8/2020   | 4/14/2020  | 04/08/2020 - 04/14/2020 |   |
| W3      | 4/15/2020  | 4/21/2020  | 04/15/2020 - 04/21/2020 |   |
| W4      | 4/22/2020  | 4/28/2020  | 04/22/2020 - 04/28/2020 |   |
| W5      | 4/29/2020  | 5/5/2020   | 04/29/2020 - 05/05/2020 |   |
| W6      | 5/6/2020   | 5/12/2020  | 05/06/2020 - 05/12/2020 |   |
| W7      | 5/13/2020  | 5/19/2020  | 05/13/2020 - 05/19/2020 |   |
| W8      | 5/20/2020  | 5/26/2020  | 05/20/2020 - 05/26/2020 |   |
| W9      | 5/27/2020  | 6/2/2020   | 05/27/2020 - 06/02/2020 |   |
| W10     | 6/3/2020   | 6/9/2020   | 06/03/2020 - 06/09/2020 |   |
| W11     | 6/10/2020  | 6/16/2020  | 06/10/2020 - 06/16/2020 |   |
| W12     | 6/17/2020  | 6/23/2020  | 06/17/2020 - 06/23/2020 |   |
| W13     | 6/24/2020  | 6/30/2020  | 06/24/2020 - 06/30/2020 |   |
| W14     | 7/1/2020   | 7/7/2020   | 07/01/2020 - 07/07/2020 |   |
| W15     | 7/8/2020   | 7/14/2020  | 07/08/2020 - 07/14/2020 |   |
| W16     | 7/15/2020  | 7/21/2020  | 07/15/2020 - 07/21/2020 |   |
| W17     | 7/22/2020  | 7/28/2020  | 07/22/2020 - 07/28/2020 |   |
| W18     | 7/29/2020  | 8/4/2020   | 07/29/2020 - 08/04/2020 |   |
| W19     | 8/5/2020   | 8/11/2020  | 08/05/2020 - 08/11/2020 |   |
| W20     | 8/12/2020  | 8/18/2020  | 08/12/2020 - 08/18/2020 |   |
| W21     | 8/19/2020  | 8/25/2020  | 08/19/2020 - 08/25/2020 |   |
| W22     | 8/26/2020  | 9/1/2020   | 08/26/2020 - 09/01/2020 |   |
| W23     | 9/2/2020   | 9/8/2020   | 09/02/2020 - 09/08/2020 |   |
| W24     | 9/9/2020   | 9/15/2020  | 09/09/2020 - 09/15/2020 |   |
| W25     | 9/16/2020  | 9/22/2020  | 09/16/2020 - 09/22/2020 |   |
| W26     | 9/23/2020  | 9/29/2020  | 09/23/2020 - 09/29/2020 |   |
| W27     | 9/30/2020  | 10/6/2020  | 09/30/2020 - 10/06/2020 |   |
| W28     | 10/7/2020  | 10/13/2020 | 10/07/2020 - 10/13/2020 |   |
| W29     | 10/14/2020 | 10/20/2020 | 10/14/2020 - 10/20/2020 |   |
| W30     | 10/21/2020 | 10/27/2020 | 10/21/2020 - 10/27/2020 |   |
| W31     | 10/28/2020 | 11/3/2020  | 10/28/2020 - 11/03/2020 |   |
| W32     | 11/4/2020  | 11/10/2020 | 11/04/2020 - 11/10/2020 |   |
| W33     | 11/11/2020 | 11/17/2020 | 11/11/2020 - 11/17/2020 |   |
| W34     | 11/18/2020 | 11/24/2020 | 11/18/2020 - 11/24/2020 |   |
| W35     | 11/25/2020 | 12/1/2020  | 11/25/2020 - 12/01/2020 |   |
| W36     | 12/2/2020  | 12/8/2020  | 12/02/2020 - 12/08/2020 |   |
| W37     | 12/9/2020  | 12/15/2020 | 12/09/2020 - 12/15/2020 |   |
| W38     | 12/16/2020 | 12/22/2020 | 12/16/2020 - 12/22/2020 |   |
| W39     | 12/23/2020 | 12/29/2020 | 12/23/2020 - 12/29/2020 |   |
| W40     | 12/30/2020 | 1/5/2021   | 12/30/2020 - 01/05/2021 |   |
| W41     | 1/6/2021   | 1/12/2021  | 01/06/2021 - 01/12/2021 |   |
| W42     | 1/13/2021  | 1/19/2021  | 01/13/2021 - 01/19/2021 |   |
| W43     | 1/20/2021  | 1/26/2021  | 01/20/2021 - 01/26/2021 |   |
| W44     | 1/27/2021  | 2/2/2021   | 01/27/2021 - 02/02/2021 |   |
| W45     | 2/3/2021   | 2/9/2021   | 02/03/2021 - 02/09/2021 |   |
| W46     | 2/10/2021  | 2/16/2021  | 02/10/2021 - 02/16/2021 |   |
| W47     | 2/17/2021  | 2/23/2021  | 02/17/2021 - 02/23/2021 |   |
| W48     | 2/24/2021  | 3/2/2021   | 02/24/2021 - 03/02/2021 |   |
| W49     | 3/3/2021   | 3/9/2021   | 03/03/2021 - 03/09/2021 |   |
| W50     | 3/10/2021  | 3/16/2021  | 03/10/2021 - 03/16/2021 |   |
| W51     | 3/17/2021  | 3/23/2021  | 03/17/2021 - 03/23/2021 |   |
| W52     | 3/24/2021  | 3/30/2021  | 03/24/2021 - 03/30/2021 |   |


Mkdir CAL20_weekly

Cd CAL20_weekly

git clone https://github.com/ruanjue/wtdbg2

cd wtdbg2 && make

mkdir originals

Mkdir firstassembly

Cd firstassembly

	8. Ran wtdbg2 and consenser. Added argument specifying genome size (-g 29k) to correct error where some weeks would have a blank output.

for FILENAME in ../originals/*.fasta; do newFILENAME=${FILENAME:0:-6}; ./../wtdbg2/wtdbg2 -g 29k -i $FILENAME -fo $newFILENAME; done

for FILENAME in ../originals/*.ctg.lay.gz; do fileSUFFIX=.ctg.fa; newFILENAME=${FILENAME:0:-11}; ./../wtdbg2/wtpoa-cns -i "$FILENAME" -fo $newFILENAME$fileSUFFIX; done

cp ../originals/*.ctg.fa ~/CAL20C_weekly/firstassembly/

for FILENAME in *.ctg.fa; do sampleNAME=${FILENAME:0:-7}; fileSUFFIX=_assembled.fasta; sed -i "s/ctg1/$sampleNAME/gi" $FILENAME; done

for FILENAME in *.ctg.fa; do printf '%s\n' "$(cat < “$FILENAME")"; done > assembled_samples.fasta

mafft --reorder --localpair assembled_samples.fasta > aligned_samples.aln

	9. Imported data to CodonCode Aligner to find differences, and analyzed in Excel.

![image](https://user-images.githubusercontent.com/60581129/115786055-4dbf5380-a38e-11eb-9c9d-86fcce3904d2.png)

