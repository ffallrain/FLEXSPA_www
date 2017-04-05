#!/usr/bin/perl -w
use CGI qw/:standard/;

#open AF,"0-35_0_4.5_allatom_chains_0.95_residue";
open AF,"/flexsite/www/html/flexsite/all_diff-0-35_0_4.5_allatom_chains_0.7_residue";
#open AF,"aa";
@pair=<AF>;
close AF;
open LIG,"/flexsite/www/html/flexsite/all_0-35_diff0.7_0_4.5_format";
@lig=<LIG>;
close LIG;
for my $line (@lig)
{
	$line=~/^(\d+-\d+)\s+(\w+)\s+.*LIGAND.*>(.*)>.*>.*/;
	$clut=$1;
	$chain=$2;
	$name=$3;
	$lig_name{"$clut-$chain"}=$name;
}

print  header;
print  start_html( -title => "Binding site conformational change upon binding structurally different ligands");
print  "<table border=1 cellpadding=0 cellspacing=0 width=100\%>";
printf  "<tr>";
print "<td>chain A</td><td>chain B</td><td>site allatom rmsd</td><td>largest rmsd</td><td>smallest rmsd</td><td>average rmsd</td><td>rmsd variation</td><td>het_name</td><td>ligand A</td><td>het_name</td><td>ligand B</td><td>alignment</td>";
printf  "</tr>";
for my $line (@pair)
{
	@temp=split (":",$line);
	$temp[0]=~/(\d+)-(\d+)/;
	$cluster=$1;
	$subset=$2;
	$temp[-1]=~/^([^ ]+)/;
	$sitermsd=$1;
	$pic1="";
	$pic2="";
	$het1="";
	$het2="";
	@item=split /\s+/,$line;
	if (-e "/flexsite/www/html/flexsite/ligand/original_$temp[1]_$lig_name{\"$cluster-$subset-$temp[1]\"}.png")
	{
		$pic1="/flexsite/ligand/original_$temp[1]_$lig_name{\"$cluster-$subset-$temp[1]\"}.png";
	}
	elsif (-e "/flexsite/www/html/flexsite/ligand/original_$temp[1]-$lig_name{\"$cluster-$subset-$temp[1]\"}.png")
	{
		$pic1="/flexsite/ligand/original_$temp[1]-$lig_name{\"$cluster-$subset-$temp[1]\"}.png";
	}
	chomp $pic1;
	
	if ($pic1=~/original_$temp[1]_(.*)\.png/)
	{
		$het1=$1;
	}
	elsif ($pic1=~/original_$temp[1]-(.*)\.png/)
	{
		$het1=$1;
	}

	if (-e "/flexsite/www/html/flexsite/ligand/original_$temp[2]_$lig_name{\"$cluster-$subset-$temp[2]\"}.png")
	{
		$pic2="/flexsite/ligand/original_$temp[2]_$lig_name{\"$cluster-$subset-$temp[2]\"}.png";
	}
	elsif (-e "/flexsite/www/html/flexsite/ligand/original_$temp[2]-$lig_name{\"$cluster-$subset-$temp[2]\"}.png")
	{
		$pic2="/flexsite/ligand/original_$temp[2]-$lig_name{\"$cluster-$subset-$temp[2]\"}.png";
	}
	chomp $pic2;
	
	if ($pic2=~/original_$temp[2]_(.*)\.png/)
	{
		$het2=$1;
	}
	elsif ($pic2=~/original_$temp[2]-(.*)\.png/)
	{
		$het2=$1;
	}

	$align="session.$temp[1].$temp[2].$cluster-$subset.py";
	printf  "<tr>";
	print "<td>$temp[1]</td><td>$temp[2]</td><td>$sitermsd</td><td>$item[2]</td><td>$item[3]</td><td>$item[4]</td><td>$item[5]</td>";
	print "<td>$het1</td>";
	print  "<td><IMG src='$pic1' width=300></td>";
	print "<td>$het2</td>";
	print  "<td><IMG src='$pic2' width=300></td>";
	print "<td><a href='/flexsite/session/$align'>alignment</a></td>";
	printf  "</tr>";
}
print  end_html;
