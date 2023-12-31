#-----------------------------------------------------------------------------
#
#  The pdbcal package
#  Copyright (C) PHENIX collaboration, 1999
#
#  Perl script PdbRootify.pl
#
#  Purpose: auto-generate LinkDef files
#
#  Description:
#
#  Author: Matthias Messer
#-----------------------------------------------------------------------------

#print "perl PdbRootify.pl ";
#print $ARGV[0];
#print "\n";

if ($#ARGV > -1) {
  #
  # Anybody asked for help?
  #
  if ($ARGV[0] eq "-h" || $ARGV[0] eq "--help" || $ARGV[0] eq "-?") {
    print "\n";
    print "******************* rootify, the linkdef-generator ********************** \n";
    print "--------------------------------------------------------------------------\n";
    print "arguments:                                                                \n";
    print " -1- The name of the class to be rootified, e.g. PdbADCChan,              \n";
    print "                                                                          \n";
    print " The script should be called in the make process                          \n";
    print "                                          8/1999 Matthias Messer          \n";
    print "\n";
    exit;
  }
}
if ($#ARGV == 0) {
  $className = $ARGV[0];
} else {
  print"usage PdbRootify [-h] [--help] [-?] className";
  exit;
}

if ($className =~ /LinkDef/)
{
    $linkDefName = $className;
    $className =~ s/\_LinkDef\.h//;
}
else
{
  $linkDefName = join("", $className, "_LinkDef.h");
}

#
# Write Root linkDef file
#
open (LINKDEF, ">$linkDefName") || die "cannot open linkdef file $linkDefName\n";

print LINKDEF "//-----------------------------------------------------------------------------\n";
print LINKDEF "//\n";
print LINKDEF "//  The pdbcal package\n";
print LINKDEF "//  Copyright (C) PHENIX collaboration, 1999\n";
print LINKDEF "//\n";
print LINKDEF "//  Root LinkDef file for class $className\n";
print LINKDEF "//\n";
print LINKDEF "//  Author: auto-generated by PdbRootify.pl\n";
print LINKDEF "//-----------------------------------------------------------------------------\n";
print LINKDEF "#ifdef __CINT__\n";
print LINKDEF "\n";
print LINKDEF "#pragma link C++ class $className+;\n";
print LINKDEF "\n";
print LINKDEF "#endif /* __CINT__ */\n";
