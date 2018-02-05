"""Generate input file for heavy-light code.

Only the top portion needs to be edited.
"""

import sys

conf_dir = "/lustre3/cd449/from_rd419/configs/l3296f211b630m0074m037m440-coul-v5/"
conf_name ="l3296f211b630m0074m037m440-coul"  # Config file name sans .{config number}
run_root="./"
prop_root = "/lustre2/dc-mcle2/BsDs/hl-2pt-exec/temp/"  # Propagator location.
out_dir = run_root + "correlators_set1_new/"  # Output directory.

hmass = 1.91  # Heavy quark mass.
nham = 4  # Stability parameter.
Lt = 96 # Temporal extent
tadd= Lt/2 # text - tsrc

mass = [ 0.0376 ]  # Light/strange quark masses.
tags = [ "Bs" ]  # Identify output.
assert len(mass) == len(tags)

theta = [ 0, 0, 0 ]

hsmear = [(1, 0.0),(2,3.425),(2,6.85)]  # Smearing (type, radius) pairs.
lsmear = [(1, 0.0)]

# Which smearing combinations. 
# For example (3, 1) means 3rd hsmear, 1st lsmear.
combos = [(1,1),(2,1),(3,1)]

def prop_name(config, tsrc):
    return "l3296f211b630m0074m037m440-coul.{0}_wallprop_m0.0376_t{1}.binary".format(config,tsrc)

def prop_dir(prop_root, mass):
    return prop_root

def src_name(prop_root,config, tsrc):
    return prop_root+"l3296f211b630m0074m037m440-coul.{0}_wallprop_m0.0376_t{1}.source.binary".format(config,tsrc)

def gen_input(config, tsrc):
    print "C torig text"
    print tsrc+1, (tsrc+(Lt/2+1))%Lt
    print "C heavy quark masses and stability parameters"
    print "{0}  {1}".format(hmass, nham)
    print "C if readpass=0 put passive mass & n"
    print "C if readpass=1 put passive file name(s)"
    print "C (make sure passive props correspond to smearings given)"
    for m in mass:
        print prop_name(config, tsrc)

    print "C ----momentum twist----"
    px,py,pz = theta
    print px,py,pz

    print "C read in a symbol for each passive mass"
    for tag in tags:
        print tag

    print "C -----smearing info-----"
    print "C active (type & radius)"
    for hsm in hsmear:
        type, rad = hsm
        print type, rad
    print "C passive (type & radius)"
    for lsm in lsmear:
        type, rad = lsm
        print type, rad
    print "C combination (active & passive)"
    for comb in combos:
        hsm_no, lsm_no = comb
        print hsm_no, lsm_no
    print "C -----momenta-----"
    print "0 0 0"  # Hard-coded.
    print "C -----io info-----"
    print "C output directory\n", out_dir
    print "C config number\n", config
    print "C config directory\n", conf_dir
    print "C config name\n", conf_name+"."
    print "C propagator directory"
    #print "C"  # ??
    print prop_dir(prop_root, mass[0])
    print "C -----random wall-----"
    print "C config number again\n", config
    print "C source time\n", tsrc+1
    print "C"
    print "blah.txt"
    print "C source name"
    print src_name(prop_root,config, tsrc)

def main(argv):
    config, tsrc = map(int, argv) 
    gen_input(config, tsrc)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
