DNS_Edit README file:

DNS_Edit is a lightweight python3 script designed to be used to edit the DNSMasq whitelist file.

Each function will have a designated sub section in this README file and explain its possible usage
and why it would be used.

defining a comment in the whitelist file:

A Hash ("#") followed by an asterix ("*") declares a comment in the config file. Below I have included
an example of why a comment would be used and how to implement one.
Note: All comments must be made under the corrosponding title

Example:

#BT
#*This section will allow traffic to access BTs website when uncommented
#server=/bt.com/8.8.8.8
#address=/bt.com/162.52.104.16

Force Function:

Certain entries can be marked as important by using a special character ("~") infront of the title.
This function is useful because there are certain rules (such as block-all) that should only be editted
if necessary.

Example:

#block-all~
#*This section will block all IP requests
address=/*/127.0.0.1
server=/*/127.0.0.1

Help Script:
The help script should be read by all new users, It explains functionality usage and purpose, Similar
to this README file.

The helpscript can be opened using the syntax:
python3 dns_edit.py -h

Commenting:

The commenting function is useful if you want to comment out a titles corrospoding server or address IPs.
This in turn will stop the DNS redirecting the host to the website.

the commenting function can be used on single entries or on all ("-a") entries in the whitelist file

when paired with the force command it will comment all functions, even if they have been marked as important.

Examples of Usage:

comment single: python3 DNS_Edit.py -c -f whitelist_file -t BT
comment single (Force): python3 DNS_Edit.py -c -f whitelist_file -t block-all -force 
comment all: python3 DNS_Edit.py -c -a -f whitelist_file
comment all (Force): python3 DNS_Edit.py -c -a -f whitelist_file -force

Example of commented file:

#itv.com
#*this is responsible for rerouting requests to itv's website
#server=/itv.com/12.12.12.12
#server=/itv.com/4.4.4.4

#spotify~
#*this is responsible for rerouting requests to spotify's website
#server=/spotify.com/8.8.8.8
#address=/spotify.fr/164.25.10.126

#youtube
#server=/youtube.com/10.10.10.10
#address=/youtube.com/12.12.12.13

#bt~
#*this is bts address
#server=/bt.com/67.7.52.2
#address=/bt.com/157.63.1.65

#block-all~
#*This section will block all IP requests
address=/*/127.0.0.1
server=/*/127.0.0.1

Uncommenting:

The Uncommenting function is useful if you want to uncomment servers or addresses under certain titles.
It will allow the DNS to redirect traffic if the URL matches

the Uncommenting function can be used on single entries or on all ("-a") entries in the whitelist file

when paired with the force command it will comment all functions, even if they have been marked as important.


Examples of Usage:

uncomment single: python3 DNS_Edit.py -u -f whitelist_file -t BT
uncomment single (Force): python3 DNS_Edit.py -u -f whitelist_file -t block-all -force 
uncomment all: python3 DNS_Edit.py -u -a -f whitelist_file
uncomment all (Force): python3 DNS_Edit.py -u -a -f whitelist_file -force

Example of an uncommented file:

#itv.com
#*this is responsible for rerouting requests to itv's website
server=/itv.com/12.12.12.12
server=/itv.com/4.4.4.4

#spotify~
#*this is responsible for rerouting requests to spotify's website
server=/spotify.com/8.8.8.8
address=/spotify.fr/164.25.10.126

#youtube
server=/youtube.com/10.10.10.10
address=/youtube.com/12.12.12.13

#bt~
#*this is BTs address
server=/bt.com/67.7.52.2
address=/bt.com/157.63.1.65

#block-all~
#*This section will block all IP requests
address=/*/127.0.0.1
server=/*/127.0.0.1

File Merging:

File Merging is a useful tool that can combine two whitelist files into a single, bigger whitelist file.
To use this function you need to provide two file paths, It is important that the first file path ("-f1") is
the main config file, as this is the file that will gain the ips from the second ("-f2") file.

Example of Usage:
python3 DNS_Edit.py -m -f1 main_whitelist_file -f2 merging_whitelist_file

Entry Adding:

Adding entries can be done using my script, via writing a command in the command line. The entry will be added at
the bottom of the config file, but above the block-all entry, as anything under the block-all entry would be redundant
as the DNS reads the file from top to bottom.
If user wants to add an entry of importance (I.E. force needed) then refer to the force section above.

Example of Usage: 
python3 DNS_Edit.py -a -f whitelist_file -t twitter -s server=/twitter.org/8.8.8.8
python3 DNS_Edit.py -a -f whitelist_file -t twitter -a address=/twitter.org/162.142.75.12

Entry Removing:

Removing entrys can be done using this function. This function allows for complete removing of an entry, or instead
remove a single ip at a time. To do so you can use the command line, with different syntax depending on the sub function
that should be used

Example of Usage:

python3 DNS_Edit.py -r -f whitelist_file -t BT
python3 DNS_Edit.py -r -f whitelist_file -ip server=/bt.com/8.8.8.8

Removing Duplicates:
The removing duplicates function is automatically called when merging two files, as merging is the most likely function to cause
redundant data. If for some reason the user wants to do a manual removing of duplicates then you can run a command that will do
this.

Example of Usage:

python3 DNS_Edit.py -rd -f whitelist_file

Restart:

DNS_Edit script does not manually restart after every command, this is because the DNS server shouldnt restart midway through a
sequence of commands. Instead, the user can run the restart command, which restarts the dnsmasq service and thus applies the 
changes.

Example of Usage:

python3 DNS_Edit.py -restart

Manual Backup:

The dns_edit script automatically makes backup whenever a function is used that makes edits to the whitelist file (I.E. adding,
removing, merging). However, a command can be used to make a manual backup, the manual backup function can be given a title to
name the backup, however this is optional, if no title is given then the time will be used instead.

Example of Usage:

python3 DNS_Edit -b -f whitelist_file
python3 DNS_Edit -b -f whitelist_file -n Name