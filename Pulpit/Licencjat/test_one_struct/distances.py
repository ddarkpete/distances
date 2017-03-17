from Bio.PDB import *
from Bio.PDB.Atom import Atom 
from Bio.PDB.Residue import Residue
from Bio.PDB.Chain import Chain
from Bio.PDB.Model import Model
from Bio.PDB.Structure import Structure
from Bio.PDB.PDBIO import PDBIO
from Bio.PDB import NeighborSearch

import chimera
import os

path = ""

#parser = PDBParser()
files = [f for f in os.listdir('.') if os.path.isfile(f) and '.pdb' in f]

for pdb_file in files:#os.listdir(path):
    print pdb_file + '\n'
    parser = PDBParser()
    struct = parser.get_structure('structure', pdb_file)
    chains = list(struct.get_chains())
    compares = []#storing compares that are already done
    for ch1 in range(0,len(chains)):
        for ch2 in range(ch1 + 1,len(chains)):
            checklist = [ chains[ch1].get_full_id()[2] , chains[ch2].get_full_id()[2] ]
            checklist2 =  [ chains[ch2].get_full_id()[2], chains[ch1].get_full_id()[2] ]
            if chains[ch1].get_full_id()[2] != chains[ch2].get_full_id()[2] and not checklist in compares and not checklist2 in compares:

                comparsion = [ chains[ch1].get_full_id()[2] , chains[ch2].get_full_id()[2] ]
                compares.append(comparsion)#appending comprasion to already done comprasions

                chain1_atms = list(chains[ch1].get_atoms())
                chain2_atms = list(chains[ch2].get_atoms())
                chain1_close = []#lists for atoms in given distance
                chain2_close = []

                for atm1 in chain1_atms:
                    for atm2 in chain2_atms:
                        if atm1 - atm2 <= 10.0:
                            #print atm1.get_name() + ' ' + atm2.get_name()
                            if atm1.get_serial_number() not in chain1_close:
                                chain1_close.append(atm1.get_serial_number())
                            if atm2.get_serial_number() not in chain2_close:
                                chain2_close.append(atm2.get_serial_number())
                if len(chain1_close) == 0 or len(chain2_close) == 0:
                    print ' No atoms in distance <= 10 Angstremes for ' + chains[ch1].get_full_id()[2] + ' and ' + chains[ch2].get_full_id()[2] + ' chains' + '\n'
                else:
                    #print 'Atoms in distance <= 10 Angstremes for ' + chains[ch1].get_full_id()[2] + ' and ' + chain[ch2].get_full_id()[2] + ' chains' + '\n'
                    #print chain1_close
                    for c1 in chain1_close:
                    	#print chains[ch1].get_full_id()
                    	command = 'color green ' + ':.' + chains[ch1].get_full_id()[2] + '@/serialNumber=' + str(c1)
                    	#print command
                    	chimera.runCommand(command)
                    print ''
                    #print chain2_close
                    for c2 in chain2_close:
                    	command = 'color orange ' + ':.' + chains[ch2].get_full_id()[2] + '@/serialNumber=' + str(c2)
                    	#print command
                    	chimera.runCommand(command)
                    print ''
                    break
            else:
                print '****************'

