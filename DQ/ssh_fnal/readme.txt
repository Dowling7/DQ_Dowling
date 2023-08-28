README for connecting to spinquest server at fermilab
krb5.conf copy to /etc/
config copy to ~/.ssh/
known_hosts copy to ~/.ssh/


kinit dwong@FNAL.GOV 
klist 
ssh -KXY dwong@spinquestgpvm01.fnal.gov
