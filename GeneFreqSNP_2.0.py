# GeneFreqSNP
# Last updated 9-18-19

# Welcome

print('Welcome to GeneFreqSNP 2.0')
print('---')

#imports
import os
import time

# Set directory
genome_dir = input("Enter Genome file location: ") 
os.chdir(genome_dir)
print('Directory set to ' + genome_dir)
print('---')

# Setup
file_count_pssd = int(input("How many PSSD file are there? = "))
file_count = int(input("how many control files are there? = "))
results = open('results.txt','w')
cac = 0
pro = 0
lf = ""
k = []
umu = endtime = gap = 0
acc = int(input("differency limit = %"))
req = int(input("The minimum number of the people that must have searched genome (pssd) = "))
reqc = int(input("The minimum number of the people that must have searched genome (control) = "))
if req == 0:
    req = 1
if reqc == 0:
    reqc = 1

# Determine Experimental Group Frequency
def pssdFrequency(s):
    global ATpy, CCpy, CGpy, GGpy, AApy, TTpy, CTpy, AGpy, ACpy, GTpy, GCpy, TCpy, TGpy, TApy, GApy, CApy, totalp, inap
    ATp = CCp = CGp = GGp = AAp = TTp = CTp = AGp = ACp = GTp = GCp = TCp = TGp = TAp = GAp = CAp = totalp = inap = 0
    for t in range(file_count_pssd):
        pssd = open('pssd_' + str(t) + '.txt','r')
        pssd_check = pssd.readlines()
        for line in pssd_check:
            if s in line[:13]:
                totalp += 1
                if "C	C" in line[14:] or "CC" in line[14:]:
                    CCp += 1
                if "C	G" in line[14:] or "CG" in line[14:]:
                    CGp += 1
                if "G	G" in line[14:] or "GG" in line[14:]:
                    GGp += 1
                if "A	A" in line[14:] or "AA" in line[14:]:
                    AAp += 1
                if "A	T" in line[14:] or "AT" in line[14:]:
                    ATp += 1
                if "T	T" in line[14:] or "TT" in line[14:]:
                    TTp += 1
                if "C	T" in line[14:] or "CT" in line[14:]:
                    CTp += 1
                if "A	G" in line[14:] or "AG" in line[14:]:
                    AGp += 1
                if "A	C" in line[14:] or "AC" in line[14:]:
                    ACp += 1
                if "G	T" in line[14:] or "GT" in line[14:]:
                    GTp += 1
                if "G	C" in line[14:] or "GC" in line[14:]:
                    GCp += 1
                if "T	C" in line[14:] or "TC" in line[14:]:
                    TCp += 1
                if "T	G" in line[14:] or "TG" in line[14:]:
                    TGp += 1
                if "T	A" in line[14:] or "TA" in line[14:]:
                    TAp += 1
                if "C	A" in line[14:] or "CA" in line[14:]:
                    CAp += 1
                if "G	A" in line[14:] or "GA" in line[14:]:
                    GAp += 1
                break
    if totalp >= req:
           
        CCpy = (float(CCp) / float(totalp)) * 100
        CGpy = (float(CGp) / float(totalp)) * 100
        GGpy = (float(GGp) / float(totalp)) * 100
        AApy = (float(AAp) / float(totalp)) * 100
        ATpy = (float(ATp) / float(totalp)) * 100
        TTpy = (float(TTp) / float(totalp)) * 100
        CTpy = (float(CTp) / float(totalp)) * 100
        AGpy = (float(AGp) / float(totalp)) * 100
        ACpy = (float(ACp) / float(totalp)) * 100
        GCpy = (float(GCp) / float(totalp)) * 100
        TApy = (float(TAp) / float(totalp)) * 100
        TCpy = (float(TCp) / float(totalp)) * 100
        TGpy = (float(TGp) / float(totalp)) * 100
        GTpy = (float(GTp) / float(totalp)) * 100
        CApy = (float(CAp) / float(totalp)) * 100
        GApy = (float(GAp) / float(totalp)) * 100
           
    else:
           inap = 1
            

# Determine Control Group Frequency

def controlFrequency(s):
    global ATcy, CCcy, CGcy, GGcy, AAcy, TTcy, CTcy, AGcy, ACcy, GTcy, GCcy, TCcy, TGcy, TAcy, GAcy, CAcy, totalc, skip,ina
    ATc = CCc = CGc = GGc = AAc = TTc = CTc = AGc = ACc = GTc = GCc = TCc = TGc = TAc = GAc = CAc = totalc = skip = ina = 0
    for h in range(file_count):
        os.chdir(r"/Genome")
        file = open(str(h) + ".txt",'r')
        l = file.readlines()
        for line in l:
            if s in line[:13]:
                totalc += 1
                if "C	C" in line[14:] or "CC" in line[14:]:
                    CCc += 1
                if "C	G" in line[14:] or "CG" in line[14:]:
                    CGc += 1
                if "G	G" in line[14:] or "GG" in line[14:]:
                    GGc += 1
                if "A	A" in line[14:] or "AA" in line[14:]:
                    AAc += 1
                if "A	T" in line[14:] or "AT" in line[14:]:
                    ATc += 1
                if "T	T" in line[14:] or "TT" in line[14:]:
                    TTc += 1
                if "C	T" in line[14:] or "CT" in line[14:]:
                    CTc += 1
                if "A	G" in line[14:] or "AG" in line[14:]:
                    AGc += 1
                if "A	C" in line[14:] or "AC" in line[14:]:
                    ACc += 1
                if "G	T" in line[14:] or "GT" in line[14:]:
                    GTc += 1
                if "G	C" in line[14:] or "GC" in line[14:]:
                    GCc += 1
                if "T	C" in line[14:] or "TC" in line[14:]:
                    TCc += 1
                if "T	G" in line[14:] or "TG" in line[14:]:
                    TGc += 1
                if "T	A" in line[14:] or "TA" in line[14:]:
                    TAc += 1
                if "C	A" in line[14:] or "CA" in line[14:]:
                    CAc += 1
                if "G	A" in line[14:] or "GA" in line[14:]:
                    GAc += 1
                break
    if totalc >= reqc:
        CCcy = (float(CCc) / float(totalc)) * 100
        CGcy = (float(CGc) / float(totalc)) * 100
        GGcy = (float(GGc) / float(totalc)) * 100
        AAcy = (float(AAc) / float(totalc)) * 100
        ATcy = (float(ATc) / float(totalc)) * 100
        TTcy = (float(TTc) / float(totalc)) * 100
        CTcy = (float(CTc) / float(totalc)) * 100
        AGcy = (float(AGc) / float(totalc)) * 100
        ACcy = (float(ACc) / float(totalc)) * 100
        GCcy = (float(GCc) / float(totalc)) * 100
        TAcy = (float(TAc) / float(totalc)) * 100
        TCcy = (float(TCc) / float(totalc)) * 100
        TGcy = (float(TGc) / float(totalc)) * 100
        GTcy = (float(GTc) / float(totalc)) * 100
        CAcy = (float(CAc) / float(totalc)) * 100
        GAcy = (float(GAc) / float(totalc)) * 100
    else:
           ina = 1

# Logging
def logging(s):
    if skip == 0:
        if abs(CAcy - CApy) > acc or abs(GAcy - GApy) > acc or abs(TGcy - TGpy) > acc or abs(TCcy - TCpy) > acc or abs(TAcy - TApy) > acc or abs(GCcy - GCpy) > acc or abs(GTcy - GTpy) > acc or abs(ACcy - ACpy) > acc or abs(AGcy - AGpy) > acc or abs(CCcy - CCpy) > acc or abs(CGcy - CGpy) > acc or abs(GGcy - GGpy) > acc or abs(AAcy - AApy) > acc or abs(ATcy - ATpy) > acc or abs(TTcy - TTpy) > acc or abs(CTcy - CTpy) > acc or abs(AGcy - AGpy) > acc:
            results.write(" ###	" + s + "###\n")
            results.write("PSSD AA: %" + str(round(AApy,2)) + " -- CONTROL AA: %" + str(float(round(AAcy,2))) + "\n")
            results.write("PSSD AC: %" + str(round(ACpy,2)) + " -- CONTROL AC: %" + str(round(ACcy,2)) + "\n")
            results.write("PSSD AG: %" + str(round(AGpy,2)) + " -- CONTROL AG: %" + str(round(AGcy,2)) + "\n")
            results.write("PSSD AT: %" + str(round(ATpy,2)) + " -- CONTROL AT: %" + str(round(ATcy,2)) + "\n")
            results.write("PSSD CA: %" + str(round(CApy,2)) + " -- CONTROL CA: %" + str(round(CAcy,2)) + "\n")
            results.write("PSSD CC: %" + str(round(CCpy,2)) + " -- CONTROL CC: %" + str(round(CCcy,2)) + "\n")
            results.write("PSSD CG: %" + str(round(CGpy,2)) + " -- CONTROL CG: %" + str(round(CGcy,2)) + "\n")
            results.write("PSSD CT: %" + str(round(CTpy,2)) + " -- CONTROL CT: %" + str(round(CTcy,2)) + "\n")
            results.write("PSSD GA: %" + str(round(GApy,2)) + " -- CONTROL GA: %" + str(round(GAcy,2)) + "\n")
            results.write("PSSD GC: %" + str(round(GCpy,2)) + " -- CONTROL GC: %" + str(round(GCcy,2)) + "\n")
            results.write("PSSD GG: %" + str(round(GGpy,2)) + " -- CONTROL GG: %" + str(round(GGcy,2)) + "\n")
            results.write("PSSD GT: %" + str(round(GTpy,2)) + " -- CONTROL GT: %" + str(round(GTcy,2)) + "\n")
            results.write("PSSD TA: %" + str(round(TApy,2)) + " -- CONTROL TA: %" + str(round(TAcy,2)) + "\n")
            results.write("PSSD TC: %" + str(round(TCpy,2)) + " -- CONTROL TC: %" + str(round(TCcy,2)) + "\n")
            results.write("PSSD TG: %" + str(round(TGpy,2)) + " -- CONTROL TG: %" + str(round(TGcy,2)) + "\n")
            results.write("PSSD TT: %" + str(round(TTpy,2)) + " -- CONTROL TT: %" + str(round(TTcy,2)) + "\n\n\n")
            results.flush()

pssd_file = open("snp.txt","r")

for i in pssd_file:
    cac += 1
    
pssd_file.seek(0)

pointime = time.perf_counter()

for x in pssd_file:
    pssdFrequency(x[:-1] + "	")
    if inap == 0:
        controlFrequency(x[:-1] + "	")
        if ina == 0:
            logging(x[:-1] + "	")
    pro += 1
    print("Processing: %" + str((float(pro) / float(cac)) * 100))
    if umu <= 20:
        gap += time.perf_counter() - pointime
        pointime = time.perf_counter()
        umu += 1
        if umu == 20:
            print("\n\n\n ---- Estimated remaining time = " + str(round(float(gap) / float(20) * cac,2)) + " Seconds")
            print("\nWill continue after 30 seconds")
            time.sleep(30)
results.close()

# Close
print('Analysis has completed. Thank you for using GeneFREQSNP 2.0 from the PSSDLab.
