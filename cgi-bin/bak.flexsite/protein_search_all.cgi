#!/usr/bin/perl -w
#used for searching by protein information.   2009.08.03
#modified for all proteins, both single and interface.  2010.08.13 liwei
#
use CGI qw/:standard/;
use DBI;
use CGI::Carp qw(fatalsToBrowser);

my $db1="FlexSiteDB3";
my $server1 = '172.16.1.204';
my $port1 = '3306';
my $dbuser1 = 'liwei';
my $dbpasswd1 = 'liwei0703';
my $dbh1 = DBI -> connect("DBI:mysql:$db1:$server1:$port1",$dbuser1,$dbpasswd1,{ PrintError => 0}) || die("unable to connect to database $db1: $DBI::errstr\n");
my $sth7 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, CHAIN, CHAINB, Ref_CHAIN, Ref_CHAINB, Ref_PDBID FROM all_site WHERE PDBID=?");
my $sth8 = $dbh1 -> prepare ("SELECT DISTINCT PDBID, CHAIN, CHAINB, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=?");
my $sth10 = $dbh1 -> prepare ("SELECT DISTINCT CHAIN, RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_NAME, ORI_BF_ALL, ASA_RATIO FROM single_bfasa WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=?");

my $db2="fpdb3";
my $server2 = '172.16.1.204';
my $port2 = '3306';
my $dbuser2 = 'liwei';
my $dbpasswd2 = 'liwei0703';
my $dbh2 = DBI -> connect("DBI:mysql:$db2:$server2:$port2",$dbuser2,$dbpasswd2,{ PrintError => 0}) || die("unable to connect to database $db2: $DBI::errstr\n");
my $sth1 = $dbh2 -> prepare ("SELECT DISTINCT CHAIN, MOLECULE, EC, SOURCE_ORGANISM_SCI FROM chain WHERE (MODEL_NO=0 or MODEL_NO=1) AND PDBID=?");
my $sth2 = $dbh2 -> prepare ("SELECT RESOLUTION, HEADER, FREE_R FROM general WHERE PDBID=?");

print "Content-type: text/html\n\n";
print <<HTML;
<html>
<head>
<title></title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="/flexsite/flex.css" type="text/css" />
<style type="text/css">
<!--
.STYLE1 {color: #CC9933}
.STYLE2 {
	font-family: Author;
	font-size: 36px;
	font-weight: bold;
	color: #0000FF;
}
.STYLE9 {
	color: #CC6600;
	font-size: 18px;
	font-weight: bold;
}
.STYLE10 {font-size: 16px}
.STYLE11 {
	font-size: 12px;
	font-weight: bold;
	color: #FF3399;
}
-->
</style>
</head>
<body bgcolor="#F4FFE4">
<table width="100%" height="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="3" rowspan="2" bgcolor="#FFFFCC">&nbsp;</td>
    <td height="50" colspan="2" align="center" valign="bottom" nowrap="nowrap" bgcolor="#FFFFCC" id="logo"><span class="STYLE2">Flex-Site DB </span></td>
  </tr>
  <tr bgcolor="#D5EDB3">
    <td height="51" colspan="2" align="center" valign="middle" bgcolor="#FFFFCC" id="tagline"><span class="STYLE11">When protein meets ligand... </span></td>
  </tr>

  <tr>
    <td colspan="5" bgcolor="#5C743D"><img src="/flexsite/space.gif" width="1" height="2" border="0" /></td>
  </tr>

  <tr>
    <td colspan="5" bgcolor="#99CC66" background="/flexsite/line.gif"><img src="/flexsite/line.gif" width="4" height="3" border="0" /></td>
  </tr>
  <script type="text/javascript">
  document.write("<tr bgcolor='#99CC66'>");
  document.write("<td height='20' colspan='6' bgcolor='#FFCC99' id='dateformat'>");
  document.write(Date());
  document.write("</td></tr>");
  </script>

  <tr>
    <td colspan="5" bgcolor="#99CC66" background="/flexsite/line.gif"><img src="/flexsite/line.gif" width="4" height="3" border="0" /></td>
  </tr>

  <tr>
    <td colspan="5" bgcolor="#5C743D"><img src="/flexsite/space.gif" width="1" height="2" border="0" /></td>
  </tr>

 <tr>
    <td valign="top" bgcolor="#FFFFCC">
	<table width="90%" height="200" cellpadding="0" cellspacing="0" border='0' class="navText" id="navigation">
        <tr>
          <td height="7%" bgcolor="#FFFFCC">&nbsp;<br /></td>
        </tr>
        <tr>
          <td height="7%" bgcolor="#FFFFCC"><a href="/flexsite/index.html" class="navText ">Home</a></td>
        </tr>
        <tr>
          <td height="7%"><a href="/flexsite/Introduction.html" class="navText ">Introduction</a></td>
        </tr>
        <tr>
          <td height="7%"><a href="/flexsite/Search.html" class="navText ">Search</a></td>
        </tr>
        <tr>
          <td height="7%"><a href="/flexsite/Browse.html" class="navText ">Browse</a></td>
        </tr>
        <tr>
          <td height="7%"><a href="/flexsite/Download.html" class="navText ">Download</a></td>
        </tr>
        <tr>
          <td height="7%"><a href="/flexsite/Analysis.html" class="navText ">Analysis</a></td>
        </tr>
        <tr>
          <td height="7%"><a href="/flexsite/Methods.html" class="navText ">Methods</a></td>
        </tr>
        <tr>
          <td height="7%"><a href="/flexsite/FAQ.html" class="navText ">FAQ</a></td>
        </tr>
        <tr>
          <td height="7%"><a href="/flexsite/Links.html" class="navText ">Links</a></td>
        </tr>
	<tr>
	  <td height="7%" bgcolor="#FFFFCC">&nbsp;<br /></td>
	 </tr>
	<tr>
	  <td height="7%" bgcolor="#FFFFCC">&nbsp;<br /></td>
	 </tr>
	<tr>
	  <td height="7%" bgcolor="#FFFFCC">&nbsp;<br /></td>
	 </tr>
      </table>
    </td>
    <td class="STYLE11"><p><img src="/flexsite/space.gif" height="1" border="0" /></p></td>
    <td colspan="2" valign="top"  class="STYLE10"><p>&nbsp;</p>
      <p align="left" class="STYLE9"></p>
      <p>&nbsp;</p>
HTML
$site_serial=0;
$sec_serial=0;
$pdbid = param('pdbid');

$sth2 -> execute($pdbid);
while(my $data2 = $sth2 -> fetchrow_hashref)
{
	$resolution=$data2->{RESOLUTION};
	$data2->{HEADER}=~/ (\d+\-\w{3}\-\d+) /;
	$date=$1;
	$free_r=$data2->{FREE_R};
}
print <<HTML;
      <table class="STYLE10" border="1" cellpadding="10">
      <tr>
      <td class="STYLE10">PDBID</td><td class="STYLE10">$pdbid</td>
      </tr>
      <tr>
      <td class="STYLE10">Resolution</td><td class="STYLE10">$resolution</td>
      </tr>
      <tr>
      <td class="STYLE10">Free R Value</td><td class="STYLE10">$free_r</td>
      </tr>
      <tr>
      <td class="STYLE10">Deposited Date</td><td class="STYLE10">$date</td>
      </tr>
      </table>
HTML

%molecule=();
%ec=();
%source=();
$sth1 -> execute($pdbid);
while(my $data1 = $sth1 -> fetchrow_hashref)
{
	$molecule{$data1->{CHAIN}}=$data1->{MOLECULE};
	$ec{$data1->{CHAIN}}=$data1->{EC};
	$source{$data1->{CHAIN}}=$data1->{SOURCE_ORGANISM_SCI};
}
@cluster=();
$sth9 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET FROM all_site WHERE PDBID=?");
$sth9 -> execute($pdbid);
while (my $data9 = $sth9 -> fetchrow_hashref)
{
	push @cluster,"$data9->{CLUSTER}-$data9->{SUBSET}";
}
$num_cluster=@cluster;
if ($num_cluster == 0)
{
	print qq(<p>This protein is not included in FlexSiteDB currently</p>);
}
elsif ($num_cluster == 1)
{
	print qq(<p>This protein has $num_cluster binding site</p>);
}
else
{
	print qq(<p>This protein has $num_cluster different binding sites</p>);
}
$cluster="";
$subset="";
$order=0;
$site_order=0;
$link=0;
$check_site_order=0;
$chain_order=0;
$sth7 -> execute($pdbid);
while (my $data7 = $sth7 -> fetchrow_hashref)
{
#for multiple conformations
#
	if ($cluster ne "" and ($data7->{CLUSTER} ne $cluster or $data7->{SUBSET} ne $subset))
	{
		print qq(</div>);
	}
	if ($data7->{CLUSTER} ne $cluster or $data7->{SUBSET} ne $subset)
	{
		$chain_order=0;
		$site_order ++;
		$check_site_order=$site_order;
		@chain=();
		@lig=();
		%lig=();
		$sth8 -> execute($data7->{CLUSTER}, $data7->{SUBSET});
		while (my $data8 = $sth8 -> fetchrow_hashref)
		{
			if (defined($data8->{CHAINB}))
			{
				$pdbidchain="$data8->{PDBID}$data8->{CHAIN}_$data8->{CHAINB}";
				push @chain, $pdbidchain;
			}
			else
			{
				$pdbidchain="$data8->{PDBID}$data8->{CHAIN}";
				push @chain, $pdbidchain;
			}
			if (defined($data8->{LIGAND_NAME}))
			{
				push @lig, $data8->{LIGAND_NAME};
				$lig{$pdbidchain}=$data8->{LIGAND_NAME};
			}
		}
		undef $multi_structs;
		undef $multi_comlex;
		undef $multi_ligs;
		$multi_structs=@chain;
		$multi_comlex=@lig;
		for (my $k=0;$k<$#lig;$k++)
		{
			for (my $g=$k+1;$g<=$#lig;$g++)
			{
				if ($lig[$k] eq $lig[$g])
				{
					splice (@lig,$g,1);
					$g=$g-1;
				}
			}
		}
		$multi_ligs=@lig;
print <<HTML;
		<p class="STYLE9">For Binding Site Number $site_order:&nbsp;
		<script>
		function DIFF_$site_order(element){
		return element = document.getElementById(element);
		}
		function DIFF_D_$site_order(){
		var d=DIFF_$site_order('DIF_$site_order');
		d.style.display='block';
		}
		function DIFF_D2_$site_order(){
		var d=DIFF_$site_order('DIF_$site_order');
		d.style.display='none';
		}
		function DIFF_use_$site_order(){
		var d=DIFF_$site_order('DIF_$site_order');
		if(d.style.display=='none'){
		DIFF_D_$site_order();
		}else{
		DIFF_D2_$site_order();
		}
		}
		</script>
		<input type="submit" id="DD_$site_order" class="STYLE9" onclick="DIFF_use_$site_order()" value="Open This Binding Site" />
		<div id="DIF_$site_order" style="DISPLAY: none">
		<table border="1" cellpadding="10">
		<tr><td class="STYLE10">Binding Site Multiple Structures</td><td class="STYLE10">$multi_structs</td></tr>
		<tr><td class="STYLE10">Binding Site Multiple Complexes</td><td class="STYLE10">$multi_comlex</td></tr>
		<tr><td class="STYLE10">Binding Site Multiple Complexes with Different Ligands</td><td class="STYLE10">$multi_ligs</td></tr>
		</table>
		<script>
		function MULTI_$site_order(element){
		return element = document.getElementById(element);
		}
		function MULTI_D_$site_order(){
		var d=MULTI_$site_order('MUL_$site_order');
		d.style.display='block';
		}
		function MULTI_D2_$site_order(){
		var d=MULTI_$site_order('MUL_$site_order');
		d.style.display='none';
		}
		function MULTI_use_$site_order(){
		var d=MULTI_$site_order('MUL_$site_order');
		if(d.style.display=='none'){
		MULTI_D_$site_order();
		}else{
		MULTI_D2_$site_order();
		}
		}
		</script>
		<input type="submit" id="M_$site_order" class="STYLE9" onclick="MULTI_use_$site_order()" value="Open Multiple Conformations" /><br />
		<div id="MUL_$site_order" style="DISPLAY: none">
HTML
#for represent structures
		$multi_url="";
		$multi_rmsd_url="";
		$multi_url_1="";
		$multi_rmsd_url_1="";
		$multi_url_2="";
		$multi_rmsd_url_2="";
		if (-e "/flexsite/www/html/flexsite/data/Site_NMR/RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/1.png")
		{
			$negtive="";
			$negtive=`grep '-' /flexsite/www/html/flexsite/data/Site_NMR/RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/1.dat`;
			if ($negtive eq "")
			{
				$multi_url="/flexsite/data/Site_NMR/RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/1.png";
				$multi_rmsd_url="/flexsite/data/Site_NMR/RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/str.1.dat";
			}
		}
		if (-e "/flexsite/www/html/flexsite/data/inter_Site_NMR/RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/1.png")
		{
			$negtive="";
			$negtive=`grep '-' /flexsite/www/html/flexsite/data/inter_Site_NMR/RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/1.dat`;
			if ($negtive eq "")
			{
				$multi_url_1="/flexsite/data/inter_Site_NMR/RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/1.png";
				$multi_rmsd_url_1="/flexsite/data/inter_Site_NMR/RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/str.1.dat";
			}
		}
		if (-e "/flexsite/www/html/flexsite/data/inter_Site_NMR/S_RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/1.png")
		{
			$negtive="";
			$negtive=`grep '-' /flexsite/www/html/flexsite/data/inter_Site_NMR/S_RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/1.dat`;
			if ($negtive eq "")
			{
				$multi_url_2="/flexsite/data/inter_Site_NMR/S_RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/1.png";
				$multi_rmsd_url_2="/flexsite/data/inter_Site_NMR/S_RENUM/$data7->{CLUSTER}-$data7->{SUBSET}/str.1.dat";
			}
		}
		if ($multi_url ne "")
		{
			print qq(<p>Multiple Conformations 2D RMSD :</p>);
			print qq(<IMG src='$multi_url'>);
			print qq(<br /><a href='$multi_rmsd_url'>binding site pairwise allatom RMSD VALUE</a>);
			open REP,"/flexsite/www/html/flexsite/data/Site_NMR/single.site.nomut.new.row.insec.rmsd.rep.str";
			@a=<REP>;
			close REP;
			chomp @a;
			@b=();
			for (my $i=0;$i<=$#a;$i++)
			{
			     	if($a[$i]=~/^>Cluster/)
     			     	{
        		        	push @b,$i;
     			     	}
                        }
			print qq(<table border="1" cellpadding="10">);
			for (my $i=0;$i<$#b;$i++)
			{	
				$a[$b[$i]]=~/>Cluster\s+(\d+)-(\d+)/;
				$cluster_rep=$1;
				$subset_rep=$2;
				if ($cluster_rep == $data7->{CLUSTER} and $subset_rep == $data7->{SUBSET})
				{
					for (my $j=$b[$i]+1;$j<=$b[$i+1]-1;$j++)
					{
						@rep=split /\s+/,$a[$j];
						if (defined($rep[1]))
						{
							print qq(<tr><td class="STYLE10">Represent Strucutre: $rep[0]</td><td class="STYLE10">Represented Structures: $rep[1]</td></tr>);
						}
						else
						{
							print qq(<tr><td class="STYLE10">Represent Strucutre: $rep[0]</td><td class="STYLE10">&nbsp;</td></tr>);
						}
					}
					last;
				}
			}
			print qq(</table>);
		}
		if ($multi_url_1 ne "")
		{
			print qq(<p>Multiple Conformations 2D RMSD :</p>);
			print qq(<IMG src='$multi_url_1'>);
			print qq(<br /><a href='$multi_rmsd_url_1'>binding site pairwise allatom RMSD VALUE</a>);
			open REP,"/flexsite/www/html/flexsite/data/inter_Site_NMR/inter.site.nomut.new.row.inter.insec.rmsd.rep.str";
			@a=<REP>;
			close REP;
			chomp @a;
			@b=();
			for (my $i=0;$i<=$#a;$i++)
			{
			     	if($a[$i]=~/^>Cluster/)
     			     	{
        		        	push @b,$i;
     			     	}
                        }
			print qq(<table border="1" cellpadding="10">);
			for (my $i=0;$i<$#b;$i++)
			{	
				$a[$b[$i]]=~/>Cluster\s+(\d+)-(\d+)/;
				$cluster_rep=$1;
				$subset_rep=$2;
				if ($cluster_rep == $data7->{CLUSTER} and $subset_rep == $data7->{SUBSET})
				{
					for (my $j=$b[$i]+1;$j<=$b[$i+1]-1;$j++)
					{
						@rep=split /\s+/,$a[$j];
						if (defined($rep[1]))
						{
							print qq(<tr><td class="STYLE10">Represent Strucutre: $rep[0]</td><td class="STYLE10">Represented Structures: $rep[1]</td></tr>);
						}
						else
						{
							print qq(<tr><td class="STYLE10">Represent Strucutre: $rep[0]</td><td class="STYLE10">&nbsp;</td></tr>);
						}
					}
					last;
				}
			}
			print qq(</table>);
		}
		if ($multi_url_2 ne "")
		{
			print qq(<p>Multiple Conformations 2D RMSD :</p>);
			print qq(<IMG src='$multi_url_2'>);
			print qq(<br /><a href='$multi_rmsd_url_2'>binding site pairwise allatom RMSD VALUE</a>);
			open REP,"/flexsite/www/html/flexsite/data/inter_Site_NMR/inter.site.nomut.new.row.single.insec.rmsd.rep.str";
			@a=<REP>;
			close REP;
			chomp @a;
			@b=();
			for (my $i=0;$i<=$#a;$i++)
			{
			     	if($a[$i]=~/^>Cluster/)
     			     	{
        		        	push @b,$i;
     			     	}
                        }
			print qq(<table border="1" cellpadding="10">);
			for (my $i=0;$i<$#b;$i++)
			{	
				$a[$b[$i]]=~/>Cluster\s+(\d+)-(\d+)/;
				$cluster_rep=$1;
				$subset_rep=$2;
				if ($cluster_rep == $data7->{CLUSTER} and $subset_rep == $data7->{SUBSET})
				{
					for (my $j=$b[$i]+1;$j<=$b[$i+1]-1;$j++)
					{
						@rep=split /\s+/,$a[$j];
						if (defined($rep[1]))
						{
							print qq(<tr><td class="STYLE10">Represent Strucutre: $rep[0]</td><td class="STYLE10">Represented Structures: $rep[1]</td></tr>);
						}
						else
						{
							print qq(<tr><td class="STYLE10">Represent Strucutre: $rep[0]</td><td class="STYLE10">&nbsp;</td></tr>);
						}
					}
					last;
				}
			}
			print qq(</table>);
		}
		for my $pdbidchain (@chain)
		{
			undef $str_url;
			if (-e "/flexsite/www/html/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/aligned_$pdbidchain.pdb.gz")
			{
				$str_url="/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/aligned_$pdbidchain.pdb.gz";
			}
			elsif (-e "/flexsite/www/html/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/reference_$pdbidchain.pdb.gz")
			{
				$str_url="/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/reference_$pdbidchain.pdb.gz";
			}
			elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/aligned_$pdbidchain.pdb.gz")
			{
				$str_url="/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/aligned_$pdbidchain.pdb.gz"
			}
			elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/reference_$pdbidchain.pdb.gz")
			{
				$str_url="/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/reference_$pdbidchain.pdb.gz";
			}
			elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/align_$pdbidchain.pdb.gz")
			{
				$str_url="/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/align_$pdbidchain.pdb.gz";
			}
			elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/refer_$pdbidchain.pdb.gz")
			{
				$str_url="/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/refer_$pdbidchain.pdb.gz";
			}

#for site_match
			undef $site_str_url;
			if (-e "/flexsite/www/html/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/site_align_$pdbidchain.pdb.gz")
			{
				$site_str_url="/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/site_align_$pdbidchain.pdb.gz";
			}
			elsif (-e "/flexsite/www/html/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/site_refer_$pdbidchain.pdb.gz")
			{
				$site_str_url="/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/site_refer_$pdbidchain.pdb.gz";
			}
			elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/site_align_$pdbidchain.pdb.gz")
			{
				$site_str_url="/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/site_align_$pdbidchain.pdb.gz"
			}
			elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/site_refer_$pdbidchain.pdb.gz")
			{
				$site_str_url="/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/site_refer_$pdbidchain.pdb.gz";
			}
			elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/site_align_$pdbidchain.pdb.gz")
			{
				$site_str_url="/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/site_align_$pdbidchain.pdb.gz";
			}
			elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/site_refer_$pdbidchain.pdb.gz")
			{
				$site_str_url="/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/site_refer_$pdbidchain.pdb.gz";
			}

#for ligand
			$lig_url="";
			if (-e "/flexsite/www/html/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/$pdbidchain.lig.pdb.gz")
			{
				$lig_url="/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/$pdbidchain.lig.pdb.gz";
			}
			elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/$pdbidchain.lig.pdb.gz")
			{
				$lig_url="/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/$pdbidchain.lig.pdb.gz"
			}
			elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/$pdbidchain.lig.pdb.gz")
			{
				$lig_url="/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/$pdbidchain.lig.pdb.gz";
			}

			@m_lig=();
			$order ++;
			$m_pdbid=substr($pdbidchain,0,4);
			$m_chain=substr($pdbidchain,4);
			if (defined($lig{$pdbidchain}))
			{
				@m_lig=split /~/, $lig{$pdbidchain};
			}
			print <<HTML;
			<table>
			<tr>
			<td class="STYLE10">
			<form action="/cgi-bin/flexsite/protein_search_all.cgi" method="post" name="protein_pdbid$order" enctype="multipart/form-data">
			<input type="text" name="pdbid" value="$m_pdbid" />$m_chain&nbsp;&nbsp;&nbsp;<input type="submit" name="search_id$order" value="view" />
			</form>
			</td>
			<td class="STYLE10">
			<a href='$str_url'>complex aligned structures (protein superimposed)</a>
			<a href='$site_str_url'>complex aligned structures (binding site superimposed)</a>
			</td>
HTML
			for my $m_ligname (@m_lig)
			{
				$order++;
				print <<HTML;
				<td class="STYLE10">
				<form action="/cgi-bin/flexsite/ligand_id_search_another.cgi" method="post" name="ligid$order" enctype="multipart/form-data">
				<input type="text" name="ligid" value="$m_ligname" />&nbsp;&nbsp;&nbsp;<input type="submit" name="search_id$order" value="protein" />
				</form>
				</td>
HTML
			}
			if ($lig_url ne "")
			{
				print qq(<td class="STYLE10"><a href='$lig_url'>ligand aligned structures</a></td>);
			}
			print <<HTML;
			</tr>
			</table>
HTML
		}
		print qq(</div>);
		$cluster=$data7->{CLUSTER};
		$subset=$data7->{SUBSET};
	}
	$chain_order ++;
print <<HTML;
	<script>
	function CHAIN_${site_order}_$chain_order(element){
	return element = document.getElementById(element);
	}
	function CHAIN_D_${site_order}_$chain_order(){
	var d=CHAIN_${site_order}_$chain_order('CH_${site_order}_$chain_order');
	d.style.display='block';
	}
	function CHAIN_D2_${site_order}_$chain_order(){
	var d=CHAIN_${site_order}_$chain_order('CH_${site_order}_$chain_order');
	d.style.display='none';
	}
	function CHAIN_use_${site_order}_$chain_order(){
	var d=CHAIN_${site_order}_$chain_order('CH_${site_order}_$chain_order');
	if(d.style.display=='none'){
	CHAIN_D_${site_order}_$chain_order();
	}else{
	CHAIN_D2_${site_order}_$chain_order();
	}
	}
	</script>
HTML
	if ($pdbid eq $data7->{Ref_PDBID} and $data7->{CHAIN} eq $data7->{Ref_CHAIN} and !defined($data7->{CHAINB}) and !defined($data7->{Ref_CHAINB}))
	{
		print qq(<input type="submit" id="CHA_${site_order}_$chain_order" class="STYLE9" onclick="CHAIN_use_${site_order}_$chain_order()" value="Open POCKET $site_order CHAIN $chain_order (Reference Chain)" /><br />);
	}
	elsif ($pdbid eq $data7->{Ref_PDBID} and defined($data7->{CHAINB}) and defined($data7->{Ref_CHAINB}) and $data7->{CHAIN} eq $data7->{Ref_CHAIN} and $data7->{CHAINB} eq $data7->{Ref_CHAINB})
	{
		print qq(<input type="submit" id="CHA_${site_order}_$chain_order" class="STYLE9" onclick="CHAIN_use_${site_order}_$chain_order()" value="Open POCKET $site_order CHAIN $chain_order (Reference Chain)" /><br />);
	}
	else
	{
		print qq(<input type="submit" id="CHA_${site_order}_$chain_order" class="STYLE9" onclick="CHAIN_use_${site_order}_$chain_order()" value="Open POCKET $site_order CHAIN $chain_order" /><br />);
	}
	print qq(<div id="CH_${site_order}_$chain_order" style="DISPLAY: none">);

#for common information
	print qq(<table border="1" cellpadding="10">);
	if (defined($data7->{CHAINB}))
	{
		print qq(<tr><td class="STYLE10">Moleucle CHAIN 1</td><td class="STYLE10">$molecule{$data7->{CHAIN}}</td></tr>) if defined($molecule{$data7->{CHAIN}});
		print qq(<tr><td class="STYLE10">Moleucle CHAIN 2</td><td class="STYLE10">$molecule{$data7->{CHAINB}}</td></tr>) if defined($molecule{$data7->{CHAINB}});
		print qq(<tr><td class="STYLE10">EC number CHAIN 1</td><td class="STYLE10">$ec{$data7->{CHAIN}}</td></tr>) if defined($ec{$data7->{CHAIN}});
		print qq(<tr><td class="STYLE10">EC number CHAIN 2</td><td class="STYLE10">$ec{$data7->{CHAINB}}</td></tr>) if defined($ec{$data7->{CHAINB}});
		print qq(<tr><td class="STYLE10">SOURCE ORGANISM CHAIN 1</td><td class="STYLE10">$source{$data7->{CHAIN}}</td></tr>) if defined($source{$data7->{CHAIN}});
		print qq(<tr><td class="STYLE10">SOURCE ORGANISM CHAIN 2</td><td class="STYLE10">$source{$data7->{CHAINB}}</td></tr>) if defined($source{$data7->{CHAINB}});
	}
	else
	{
		print qq(<tr><td class="STYLE10">Moleucle CHAIN 1</td><td class="STYLE10">$molecule{$data7->{CHAIN}}</td></tr>) if defined($molecule{$data7->{CHAIN}});
		print qq(<tr><td class="STYLE10">EC number CHAIN 1</td><td class="STYLE10">$ec{$data7->{CHAIN}}</td></tr>) if defined($ec{$data7->{CHAIN}});
		print qq(<tr><td class="STYLE10">SOURCE ORGANISM CHAIN 1</td><td class="STYLE10">$source{$data7->{CHAIN}}</td></tr>) if defined($source{$data7->{CHAIN}});
	}

#for binding site

#first get the sitematch results and store it.
	if (defined($data7->{CHAINB}))
	{
		$sth14 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_CHAIN, RESIDUE_NAME, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD FROM all_sitematch WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=?");
		$sth14 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN}, $data7->{CHAINB});
	}
	else
	{
		$sth14 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_CHAIN, RESIDUE_NAME, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD FROM all_sitematch WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL");
		$sth14 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN});
	}
	%sup_res_all=();
	%sup_res_bone=();
	%sup_res_side=();
	while(my $data14 = $sth14 -> fetchrow_hashref)
	{
		undef $href_residue_id;
		if (defined($data14->{RESIDUE_CHAIN}))
		{
			$href_residue_id="$data14->{RESIDUE_NUM}$data14->{RESIDUE_INSERT}_$data14->{RESIDUE_CHAIN}_$data14->{RESIDUE_NAME}";
		}
		else
		{
			$href_residue_id="$data14->{RESIDUE_NUM}$data14->{RESIDUE_INSERT}_$data7->{CHAIN}_$data14->{RESIDUE_NAME}";
		}
		if (defined($data14->{RESIDUE_ALL_RMSD}) and $data14->{RESIDUE_ALL_RMSD} >=0)
		{
			$sup_res_all{$href_residue_id}=$data14->{RESIDUE_ALL_RMSD};

		}
		if (defined($data14->{RESIDUE_BONE_RMSD}) and $data14->{RESIDUE_BONE_RMSD} >=0)
		{
			$sup_res_bone{$href_residue_id}=$data14->{RESIDUE_BONE_RMSD};
		}
		if (defined($data14->{RESIDUE_SIDE_RMSD}) and $data14->{RESIDUE_SIDE_RMSD} >=0)
		{
			$sup_res_side{$href_residue_id}=$data14->{RESIDUE_SIDE_RMSD};
		}
	}

#for binding site (protein superimposed)
#
	$header_line="";
	if (defined($data7->{CHAINB}))
	{
		$sth3 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, Type, Ref_PDBID, Ref_CHAIN, Ref_CHAINB, LIGAND_SPEC, LIGAND_NAME, LIGAND_ASA, OTHER_LIGAND, ONESITE_NUM_LIGS, POCKET_RESIDUE, POCKET_RESIDUE_NUM, POCKET_ALL_RMSD, POCKET_BONE_RMSD, POCKET_CA_RMSD, POCKET_SIDE_RMSD, RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_CHAIN, RESIDUE_NAME, Ref_RESIDUE_NUM, Ref_RESIDUE_INSERT, Ref_RESIDUE_CHAIN, Ref_RESIDUE_NAME, RESIDUE_HET, RESIDUE_SIDEMISS, RESIDUE_BONEMISS, RESIDUE_MUTATION, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD, POCKET_MUTATION, MULTI_STRUCTS, MULTI_COMX, MULTI_LIGS, STAND_POCKET_RES_NUM, CHECK_APO, CHECK_APO_LIG FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=?");
		$sth3 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN}, $data7->{CHAINB});
	}
	else
	{
		$sth3 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, Type, Ref_PDBID, Ref_CHAIN, Ref_CHAINB, LIGAND_SPEC, LIGAND_NAME, LIGAND_ASA, OTHER_LIGAND, ONESITE_NUM_LIGS, POCKET_RESIDUE, POCKET_RESIDUE_NUM, POCKET_ALL_RMSD, POCKET_BONE_RMSD, POCKET_CA_RMSD, POCKET_SIDE_RMSD, RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_CHAIN, RESIDUE_NAME, Ref_RESIDUE_NUM, Ref_RESIDUE_INSERT, Ref_RESIDUE_CHAIN, Ref_RESIDUE_NAME, RESIDUE_HET, RESIDUE_SIDEMISS, RESIDUE_BONEMISS, RESIDUE_MUTATION, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD, POCKET_MUTATION, MULTI_STRUCTS, MULTI_COMX, MULTI_LIGS, STAND_POCKET_RES_NUM, CHECK_APO, CHECK_APO_LIG FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL");
		$sth3 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN});
	}
	while(my $data3 = $sth3 -> fetchrow_hashref)
	{
		if ($header_line eq "")
		{
			$site_serial ++;
			print qq(<tr><td class="STYLE10">PDBID</td><td class="STYLE10">$pdbid</td></tr>);
			print qq(<tr><td class="STYLE10">CHAIN 1</td><td class="STYLE10">$data7->{CHAIN}</td></tr>);
			print qq(<tr><td class="STYLE10">CHAIN 2</td><td class="STYLE10">$data7->{CHAINB}</td></tr>) if defined($data7->{CHAINB});
			if ($data3->{Type} eq "nofit")
			{
				print qq(<tr><td class="STYLE10">Type</td><td class="STYLE10">SEE "Binding site holo-apo form" For Details</td></tr>);
			}
			else
			{
				print qq(<tr><td class="STYLE10">Type</td><td class="STYLE10">$data3->{Type}</td></tr>)
			}
print <<HTML;
			<tr><td class="STYLE10">Reference PDBID</td><td class="STYLE10">$data3->{Ref_PDBID}</td></tr>
			<tr><td class="STYLE10">Reference CHAIN 1</td><td class="STYLE10">$data3->{Ref_CHAIN}</td></tr>
HTML
			print qq(<tr><td class="STYLE10">Reference CHAIN 2</td><td class="STYLE10">$data3->{Ref_CHAINB}</td></tr>) if defined($data3->{Ref_CHAINB});
			print qq(<tr><td class="STYLE10">Ligand identifier</td><td class="STYLE10">$data3->{LIGAND_SPEC}</td></tr>) if defined($data3->{LIGAND_SPEC});
			print qq(<tr><td class="STYLE10">Ligand name</td><td class="STYLE10">$data3->{LIGAND_NAME}</td></tr></table>) if defined($data3->{LIGAND_NAME});
			if (defined($data3->{LIGAND_NAME}))
			{
				@ligname=split /~/,$data3->{LIGAND_NAME};
				for my $lig_name (@ligname)
				{
					$order++;
print <<HTML;
				<form action="/cgi-bin/flexsite/ligand_id_search_another.cgi" method="post" name="ligid$order" enctype="multipart/form-data">
				<input type="text" name="ligid" value="$lig_name" />&nbsp;&nbsp;&nbsp;<input type="submit" name="search_id$order" value="protein" /><a href="http://ligand-expo.rcsb.org/pyapps/ldHandler.py?formid=cc-index-search&target=$lig_name&operation=ccid" target="_blank">Ligand Expo</a>&nbsp;&nbsp;&nbsp;<a href="http://xray.bmc.uu.se/hicup/$lig_name/" target="_blank">HIC-UP</a>&nbsp;&nbsp;
				</form>
HTML
				}
			}
			undef $hhb_pdbidchain;
			undef $pic_src;
			if (defined($data7->{CHAINB}))
			{
				$hhb_pdbidchain="$pdbid$data7->{CHAIN}_$data7->{CHAINB}";
			}
			else
			{
				$hhb_pdbidchain="$pdbid$data7->{CHAIN}";
			}
			if (-e "/flexsite/www/html/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/hhb_nnb/$hhb_pdbidchain/$hhb_pdbidchain.$data7->{CLUSTER}-$data7->{SUBSET}.png")
			{
				$pic_src="/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/hhb_nnb/$hhb_pdbidchain/$hhb_pdbidchain.$data7->{CLUSTER}-$data7->{SUBSET}.png";
			}
			elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/hhb_nnb/$hhb_pdbidchain/$hhb_pdbidchain.$data7->{CLUSTER}-$data7->{SUBSET}.png")
			{
				$pic_src="/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/hhb_nnb/$hhb_pdbidchain/$hhb_pdbidchain.$data7->{CLUSTER}-$data7->{SUBSET}.png";
			}
			if (defined($pic_src))
			{
				print qq(<p>Interaction From LIGPLOT:</p>);
				print qq(<IMG src='$pic_src'><p></p>);
			}
			
			print qq(<table border="1" cellpadding="10">) if defined($data3->{LIGAND_NAME});
			print qq(<tr><td class="STYLE10">Ligand Solvent Accessibility</td><td class="STYLE10">$data3->{LIGAND_ASA}</td></tr>) if defined($data3->{LIGAND_ASA});
#			print qq(<tr><td class="STYLE10">Other molecules</td><td class="STYLE10">$data3->{OTHER_LIGAND}</td></tr>) if defined($data3->{OTHER_LIGAND});
#			print qq(<tr><td class="STYLE10">Number of molecules in the binding site</td><td class="STYLE10">$data3->{ONESITE_NUM_LIGS}</td></tr>) if defined($data3->{ONESITE_NUM_LIGS});
###
			
			if (defined($data3->{POCKET_RESIDUE}))
			{
				@site_res=();
				$site_res_line="";
				@site_res=split /:/, $data3->{POCKET_RESIDUE};
				$site_res_line .= "<a href=\"#$_\">$_</a>:" for @site_res;
				$site_res_line=~s/:$//;
				print qq(<tr><td class="STYLE10">Binding Site Residues</td><td class="STYLE10">$site_res_line</td></tr>);
			}
			print qq(<tr><td class="STYLE10">Number of Binding Site Residues</td><td class="STYLE10">$data3->{POCKET_RESIDUE_NUM}</td></tr>) if defined($data3->{POCKET_RESIDUE_NUM});
			if (defined($data3->{POCKET_ALL_RMSD}) and $data3->{POCKET_ALL_RMSD} >= 0)
			{
				print qq(<tr><td class="STYLE10">Binding Site Allatom RMSD with Reference Structure</td><td class="STYLE10">$data3->{POCKET_ALL_RMSD}</td></tr>);
			}
			if (defined($data3->{POCKET_BONE_RMSD}) and $data3->{POCKET_BONE_RMSD} >= 0)
			{
				print qq(<tr><td class="STYLE10">Binding Site Backbone RMSD with Reference Structure</td><td class="STYLE10">$data3->{POCKET_BONE_RMSD}</td></tr>);
			}
			if (defined($data3->{POCKET_CA_RMSD}) and $data3->{POCKET_CA_RMSD} >= 0)
			{
				print qq(<tr><td class="STYLE10">Binding Site CA RMSD with Reference Structure</td><td class="STYLE10">$data3->{POCKET_CA_RMSD}</td></tr>);
			}
			if (defined($data3->{POCKET_SIDE_RMSD}) and $data3->{POCKET_SIDE_RMSD} >=0)
			{
				print qq(<tr><td class="STYLE10">Binding Site Sidechain RMSD with Reference Structure</td><td class="STYLE10">$data3->{POCKET_SIDE_RMSD}</td></tr>);
			}
			if (defined($data3->{POCKET_MUTATION}) and $data3->{POCKET_MUTATION} ne "NO")
			{
				print qq(<tr><td class="STYLE10">Binding Site Mutation</td><td class="STYLE10">$data3->{POCKET_MUTATION}</td></tr>);
			}
			print qq(<tr><td class="STYLE10">Binding Site Holo-Apo Form</td><td class="STYLE10">$data3->{CHECK_APO}</td></tr>) if defined($data3->{CHECK_APO});
			print qq(</table>);

			if (defined($data3->{CHECK_APO_LIG}))
			{
				@p_lig=split /~/, $data3->{CHECK_APO_LIG};
				for my $p_lig_line (@p_lig)
				{
					$order++;
					$p_lig_line=~/>(\w+)/;
					$p_lig_name=$1;
print <<HTML;	
				<form action="/cgi-bin/flexsite/ligand_id_search_another.cgi" method="post" name="ligid$order" enctype="multipart/form-data">
				<input type="text" name="ligid" value="$p_lig_name" />&nbsp;&nbsp;&nbsp;<input type="submit" name="search_id$order" value="protein" /><a href="http://ligand-expo.rcsb.org/pyapps/ldHandler.py?formid=cc-index-search&target=$p_lig_name&operation=ccid" target="_blank">Ligand Expo</a>&nbsp;&nbsp;&nbsp;<a href="http://xray.bmc.uu.se/hicup/$p_lig_name/" target="_blank">HIC-UP</a>
				</form>
HTML
				}
			}
			print qq(</p>);
#
#Interaction Information
			if (defined($data3->{LIGAND_SPEC}) and defined($data3->{LIGAND_NAME}))
			{
print <<HTML;
	<script>
	function ACTION_${site_order}_$chain_order(element){
	return element = document.getElementById(element);
	}
	function ACTION_D_${site_order}_$chain_order(){
	var d=ACTION_${site_order}_$chain_order('act_${site_order}_$chain_order');
	d.style.display='block';
	}
	function ACTION_D2_${site_order}_$chain_order(){
	var d=ACTION_${site_order}_$chain_order('act_${site_order}_$chain_order');
	d.style.display='none';
	}
	function ACTION_use_${site_order}_$chain_order(){
	var d=ACTION_${site_order}_$chain_order('act_${site_order}_$chain_order');
	if(d.style.display=='none'){
	ACTION_D_${site_order}_$chain_order();
	}else{
	ACTION_D2_${site_order}_$chain_order();
	}
	}
	</script>
	<input type="submit" id="ACTI_${site_order}_$chain_order" class="STYLE9" onclick="ACTION_use_${site_order}_$chain_order()" value="Open Interaction Information" />
	<div id="act_${site_order}_$chain_order" style="DISPLAY: none">
HTML
				print qq(<table border="1" cellpadding="10">);
				if (defined($data7->{CHAINB}))
				{
					$sth13 = $dbh1 -> prepare ("SELECT MW, N_atom, N_heavy, N_H, N_rot, smalln_rot, RBscore, AHPDI, Contact, UnsatPo, UnsatCh, BurCP, all_action, convention_hb, other_interaction, weak_hb, halbond, pi_pi, no_pi, cdonor_pi, cdonor_no, cdonor_s, cdonor_hal, cdonor, sdonor_pi, sdonor_no, sdonor_s, sdonor_hal, sdonor, sacceptor_no, sacceptor, halacceptor_no, halacceptor, LCHPPi, LCHPS, LCHPX, LSHPPi, LSHPS, LSHPX, LXHPPi, LXHPS, LXHPX, PCHLha, PCHLPi, PCHLS, PCHLX, PCOLha, PPiLPi, PSHLha, PSHLPi, PSHLS, PSHLX, PXHLha, PXHLPi, PXHLS, PXHLX FROM interaction WHERE PDBID=? AND CHAIN=? AND CHAINB=? AND LIGAND_SPEC =? AND LIGAND_NAME =?"); 
					$sth13 -> execute($pdbid, $data7->{CHAIN}, $data7->{CHAINB}, $data3->{LIGAND_SPEC}, $data3->{LIGAND_NAME});
				}
				else
				{
					$sth13 = $dbh1 -> prepare ("SELECT MW, N_atom, N_heavy, N_H, N_rot, smalln_rot, RBscore, AHPDI, Contact, UnsatPo, UnsatCh, BurCP, all_action, convention_hb, other_interaction, weak_hb, halbond, pi_pi, no_pi, cdonor_pi, cdonor_no, cdonor_s, cdonor_hal, cdonor, sdonor_pi, sdonor_no, sdonor_s, sdonor_hal, sdonor, sacceptor_no, sacceptor, halacceptor_no, halacceptor, LCHPPi, LCHPS, LCHPX, LSHPPi, LSHPS, LSHPX, LXHPPi, LXHPS, LXHPX, PCHLha, PCHLPi, PCHLS, PCHLX, PCOLha, PPiLPi, PSHLha, PSHLPi, PSHLS, PSHLX, PXHLha, PXHLPi, PXHLS, PXHLX FROM interaction WHERE PDBID=? AND CHAIN=? AND CHAINB IS NULL AND LIGAND_SPEC =? AND LIGAND_NAME =?"); 
					$sth13 -> execute($pdbid, $data7->{CHAIN}, $data3->{LIGAND_SPEC}, $data3->{LIGAND_NAME});
				}
				while(my $data13 = $sth13 -> fetchrow_hashref)
				{
					print qq(<tr><td class="STYLE10">Ligand Molecular Weight</td><td class="STYLE10">$data13->{MW}</td></tr>);
					print qq(<tr><td class="STYLE10">Ligand Heavy Atom Number</td><td class="STYLE10">$data13->{N_heavy}</td></tr>);
					print qq(<tr><td class="STYLE10">Ligand Rotatable Bond Number</td><td class="STYLE10">$data13->{smalln_rot}</td></tr>);
					print qq(<tr><td class="STYLE10">Rotatable Bond Score &#40;RBScore&#41;</td><td class="STYLE10">$data13->{RBscore}</td></tr>);
					print qq(<tr><td class="STYLE10">Atomic Hydrophobicity Difference &#40;AHPDI&#41;</td><td class="STYLE10">$data13->{AHPDI}</td></tr>);
					print qq(<tr><td class="STYLE10">Contact</td><td class="STYLE10">$data13->{Contact}</td></tr>);
					print qq(<tr><td class="STYLE10">Unsatisfied Polar Atom Contact</td><td class="STYLE10">$data13->{UnsatPo}</td></tr>);
					print qq(<tr><td class="STYLE10">Unsatisfied Charged Atom Contact</td><td class="STYLE10">$data13->{UnsatCh}</td></tr>);
					print qq(<tr><td class="STYLE10">Buried Carbon Percentage</td><td class="STYLE10">$data13->{BurCP}</td></tr>);
					print qq(<tr><td class="STYLE10">Conventional Hydrogen Bond</td><td class="STYLE10">$data13->{convention_hb}</td></tr>);
					print qq(<tr><td class="STYLE10">Weak Hydrogen Bond</td><td class="STYLE10">$data13->{weak_hb}</td></tr>);
					print qq(<tr><td class="STYLE10">Halogen Bond</td><td class="STYLE10">$data13->{halbond}</td></tr>);
					print qq(<tr><td class="STYLE10">&#960;-&#960;</td><td class="STYLE10">$data13->{pi_pi}</td></tr>);
					print qq(<tr><td class="STYLE10">X-H&#183;&#183;&#183;&#960; \(X=N,O\)</td><td class="STYLE10">$data13->{no_pi}</td></tr>);
					print qq(<tr><td class="STYLE10">C-H&#183;&#183;&#183;&#960;</td><td class="STYLE10">$data13->{cdonor_pi}</td></tr>);
					print qq(<tr><td class="STYLE10">C-H&#183;&#183;&#183;X \(X=N,O\)</td><td class="STYLE10">$data13->{cdonor_no}</td></tr>);
					print qq(<tr><td class="STYLE10">C-H&#183;&#183;&#183;S</td><td class="STYLE10">$data13->{cdonor_s}</td></tr>);
					print qq(<tr><td class="STYLE10">C-H&#183;&#183;&#183;Halogen \(F,Cl,Br,I\)</td><td class="STYLE10">$data13->{cdonor_hal}</td></tr>);
					print qq(<tr><td class="STYLE10">C-H&#183;&#183;&#183;* \(ALL ATOM TYPES\)</td><td class="STYLE10">$data13->{cdonor}</td></tr>);
					print qq(<tr><td class="STYLE10">S-H&#183;&#183;&#183;&#960;</td><td class="STYLE10">$data13->{sdonor_pi}</td></tr>);
					print qq(<tr><td class="STYLE10">S-H&#183;&#183;&#183;X \(X=N,O\)</td><td class="STYLE10">$data13->{sdonor_no}</td></tr>);
					print qq(<tr><td class="STYLE10">S-H&#183;&#183;&#183;S</td><td class="STYLE10">$data13->{sdonor_s}</td></tr>);
					print qq(<tr><td class="STYLE10">S-H&#183;&#183;&#183;Halogen \(F,Cl,Br,I\)</td><td class="STYLE10">$data13->{sdonor_hal}</td></tr>);
					print qq(<tr><td class="STYLE10">S-H&#183;&#183;&#183;* \(ALL ATOM TYPES\)</td><td class="STYLE10">$data13->{sdonor}</td></tr>);
					print qq(<tr><td class="STYLE10">X-H&#183;&#183;&#183;S \(X=N,O\)</td><td class="STYLE10">$data13->{sacceptor_no}</td></tr>);
					print qq(<tr><td class="STYLE10">\(ALL ATOM TYPES\) *-H&#183;&#183;&#183;S</td><td class="STYLE10">$data13->{sacceptor}</td></tr>);
					print qq(<tr><td class="STYLE10">X-H&#183;&#183;&#183;Halogen \(F,Cl,Br,I\) \(X=N,O\)</td><td class="STYLE10">$data13->{halacceptor_no}</td></tr>);
					print qq(<tr><td class="STYLE10">\(ALL ATOM TYPES\) *-H&#183;&#183;&#183;Halogen \(F,Cl,Br,I\)</td><td class="STYLE10">$data13->{halacceptor}</td></tr>);
				}
				print qq(</table>);
				print qq(</div>);
			}
			
#Flexible Residue
#
			$header_line=1;
		        if (defined($data3->{POCKET_RESIDUE}))
			{
				%bfactor=();
				%asa=();
				@bf_res=();
				$bf_res_line="";
				@asa_res=();
				$asa_res_line="";
				@site_res=();
				$sth10 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN});
				while(my $data10 = $sth10 -> fetchrow_hashref)
				{
					$bfactor{"$data10->{RESIDUE_NUM}$data10->{RESIDUE_INSERT}_$data10->{CHAIN}_$data10->{RESIDUE_NAME}"}=$data10->{ORI_BF_ALL};
					$asa{"$data10->{RESIDUE_NUM}$data10->{RESIDUE_INSERT}_$data10->{CHAIN}_$data10->{RESIDUE_NAME}"}=$data10->{ASA_RATIO};
				}
				if (defined($data7->{CHAINB}))
				{
					$sth10 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAINB});
					while(my $data10 = $sth10 -> fetchrow_hashref)
					{
						$bfactor{"$data10->{RESIDUE_NUM}$data10->{RESIDUE_INSERT}_$data10->{CHAIN}_$data10->{RESIDUE_NAME}"}=$data10->{ORI_BF_ALL};
						$asa{"$data10->{RESIDUE_NUM}$data10->{RESIDUE_INSERT}_$data10->{CHAIN}_$data10->{RESIDUE_NAME}"}=$data10->{ASA_RATIO};
					}
				}
				@site_res=split /:/, $data3->{POCKET_RESIDUE};
				$bf_check=0;
				for my $xyz (@site_res)
				{
					if (! defined($bfactor{$xyz}))
					{
						$bf_check=1;
						last;
					}
				}
				if ($bf_check == 0)
				{
					@bf_res=sort {$bfactor{$b} <=> $bfactor{$a}}@site_res;
					$bf_res_line .= "<a href=\"#$_\">$_</a> > " for @bf_res;
					$bf_res_line=~s/ > $//;
				}
				$asa_check=0;
				for my $xyz (@site_res)
				{
					if (!defined($asa{$xyz}))
					{
						$asa_check=1;
						last;
					}
				}
				if ($asa_check == 0)
				{
					@asa_res=sort {$asa{$b} <=> $asa{$a}}@site_res;
					$asa_res_line .= "<a href=\"#$_\">$_</a> > " for @asa_res;
					$asa_res_line=~s/ > $//;
				}
				print qq(<table border="1" cellpadding="10">);
				if ($bf_res_line ne "")
				{
					print qq(<tr><td class="STYLE10">B-Factor Order of Binding Site Residues</td><td class="STYLE10">$bf_res_line</td></tr>);
				}
				if ($asa_res_line ne "")
				{
					print qq(<tr><td class="STYLE10">Solvent Accessibility Order of Binding Site Residues</td><td class="STYLE10">$asa_res_line</td></tr>);
				}
#for residue rmsd
				if (defined($data7->{CHAINB}))
				{
					$sth11 = $dbh1 -> prepare ("SELECT DISTINCT RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_CHAIN, RESIDUE_NAME, Ref_RESIDUE_NUM, Ref_RESIDUE_INSERT, Ref_RESIDUE_CHAIN, Ref_RESIDUE_NAME, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=?");
					$sth11 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN}, $data7->{CHAINB});
				}
				else
				{
					$sth11 = $dbh1 -> prepare ("SELECT DISTINCT RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_CHAIN, RESIDUE_NAME, Ref_RESIDUE_NUM, Ref_RESIDUE_INSERT, Ref_RESIDUE_CHAIN, Ref_RESIDUE_NAME, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL");
					$sth11 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN});
				}
				@site_all=();
				%site_all=();
				$site_all_line="";
				@site_bk=();
				%site_bk=();
				$site_bk_line="";
				@site_side=();
				%site_side=();
				$site_side_line="";
				while(my $data11 = $sth11 -> fetchrow_hashref)
				{
					if (defined($data11->{RESIDUE_CHAIN}))
					{
						if ($data11->{RESIDUE_ALL_RMSD} >=0)
						{
							$site_all{"$data11->{RESIDUE_NUM}$data11->{RESIDUE_INSERT}_$data11->{RESIDUE_CHAIN}_$data11->{RESIDUE_NAME}"}=$data11->{RESIDUE_ALL_RMSD};
						}
						if ($data11->{RESIDUE_BONE_RMSD} >=0)
						{
							$site_bk{"$data11->{RESIDUE_NUM}$data11->{RESIDUE_INSERT}_$data11->{RESIDUE_CHAIN}_$data11->{RESIDUE_NAME}"}=$data11->{RESIDUE_BONE_RMSD};
						}
						if ($data11->{RESIDUE_SIDE_RMSD} >=0)
						{
							$site_side{"$data11->{RESIDUE_NUM}$data11->{RESIDUE_INSERT}_$data11->{RESIDUE_CHAIN}_$data11->{RESIDUE_NAME}"}=$data11->{RESIDUE_SIDE_RMSD};
						}
					}
					else
					{
						if ($data11->{RESIDUE_ALL_RMSD} >=0)
						{
							$site_all{"$data11->{RESIDUE_NUM}$data11->{RESIDUE_INSERT}_$data7->{CHAIN}_$data11->{RESIDUE_NAME}"}=$data11->{RESIDUE_ALL_RMSD};
						}
						if ($data11->{RESIDUE_BONE_RMSD} >= 0)
						{
							$site_bk{"$data11->{RESIDUE_NUM}$data11->{RESIDUE_INSERT}_$data7->{CHAIN}_$data11->{RESIDUE_NAME}"}=$data11->{RESIDUE_BONE_RMSD};
						}
						if ($data11->{RESIDUE_SIDE_RMSD} >= 0)
						{
							$site_side{"$data11->{RESIDUE_NUM}$data11->{RESIDUE_INSERT}_$data7->{CHAIN}_$data11->{RESIDUE_NAME}"}=$data11->{RESIDUE_SIDE_RMSD};
						}
					}
				}
				@site_all=sort {$site_all{$b} <=> $site_all{$a}} keys %site_all;
				$site_all_line .= "<a href=\"#$_\">$_</a> > " for @site_all;
				$site_all_line=~s/ > $//;

				@site_bk=sort {$site_bk{$b} <=> $site_bk{$a}} keys %site_bk;
				$site_bk_line .= "<a href=\"#$_\">$_</a> > " for @site_bk;
				$site_bk_line=~s/ > $//;

				@site_side=sort {$site_side{$b} <=> $site_side{$a}} keys %site_side;
				$site_side_line .= "<a href=\"#$_\">$_</a> > " for @site_side;
				$site_side_line=~s/ > $//;

				print qq(<tr><td class="STYLE10">Allatom RMSD Order of Binding Site Residues</td><td class="STYLE10">$site_all_line</td></tr>);
				print qq(<tr><td class="STYLE10">Backbone RMSD Order of Binding Site Residues</td><td class="STYLE10">$site_bk_line</td></tr>);
				print qq(<tr><td class="STYLE10">Sidechain RMSD Order of Binding Site Residues</td><td class="STYLE10">$site_side_line</td></tr>);
				print qq(</table>);
				@clashfile=();
				if (-e "/flexsite/www/html/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/clash")
				{
					@clashfile=`ls /flexsite/www/html/flexsite/data/2_first_job/PDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/clash/$pdbid$data7->{CHAIN}-*`;
				}
				elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/clash")
				{
					@clashfile=`ls /flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULTS/clash/$pdbid$data7->{CHAIN}-*`;
				}
				elsif (-e "/flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/clash")
				{
					if (defined($data7->{CHAINB}))
					{
						@clashfile=`ls /flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/clash/$pdbid$data7->{CHAIN}_$data7->{CHAINB}-*`;
					}
					else
					{
						@clashfile=`ls /flexsite/www/html/flexsite/data/inter_job/interPDBFILE/cluster$data7->{CLUSTER}/cluster$data7->{CLUSTER}-$data7->{SUBSET}/RESULT/clash/$pdbid$data7->{CHAIN}-*`;
					}
				}
				print qq(<table border="1" cellpadding="10">);
				print qq(<tr><td class="STYLE10">Ligand ID</td><td class="STYLE10">Ligand NAME</td><td class="STYLE10">Ligand From</td><td class="STYLE10">Severe Order of Clashed Residue</td></tr>);
				for my $clash_file (@clashfile)
				{
					$clash_file=~/-(\w+)\.clash\.SPEC(.*)\.NAME(.*)\.gz/;
					$fromchain=$1;
					$from_ligspec=$2;
					$from_ligname=$3;
					open CLS,"zcat $clash_file |";
					@cls=<CLS>;
					close CLS;
					chomp @cls;
					%clash_count=();
					@clash_res=();
					$clash_res_line="";
					for my $cls_line (@cls)
					{
						if ($cls_line=~/^#/)
						{
							@cls_it=split /\s+/, $cls_line;
							$cls_it[6]=~s/\./_/;
							$cls_it_res=$cls_it[6]."_".$cls_it[5];
							$clash_count{$cls_it_res} ++;
						}
					}
					@clash_res=sort {$clash_count{$b} <=> $clash_count{$a}} keys %clash_count;
					for (my $x=0;$x<=$#clash_res;$x++)
					{
						$ok=0;
						for my $site_res (@site_res)
						{
							if ($clash_res[$x] eq $site_res)
							{
								$ok = 1;
								last;
							}
						}
						if ($ok == 0)
						{
							splice (@clash_res,$x,1);
							$x=$x-1;
						}
					}
					$clash_res_line .= "<a href=\"#$_\">$_</a> > " for @clash_res;
					$clash_res_line=~s/ > $// if $clash_res_line ne "";
					if ($clash_res_line ne "")
					{
						print qq(<tr><td class="STYLE10">$from_ligspec</td><td class="STYLE10">$from_ligname</td><td class="STYLE10">$fromchain</td><td class="STYLE10">$clash_res_line</td></tr>);
					}
					else
					{
						print qq(<tr><td class="STYLE10">$from_ligspec</td><td class="STYLE10">$from_ligname</td><td class="STYLE10">$fromchain</td><td class="STYLE10">No clash</td></tr>);
					}
				}
				print qq(</table>);
			}
print <<HTML;
			<script>
			function SITE_$site_serial(element){
			return element = document.getElementById(element);
			}
			function SITE_D_$site_serial(){
			var d=SITE_$site_serial('S_$site_serial');
			d.style.display='block';
			}
			function SITE_D2_$site_serial(){
			var d=SITE_$site_serial('S_$site_serial');
			d.style.display='none';
			}
			function SITE_use_$site_serial(){
			var d=SITE_$site_serial('S_$site_serial');
			if(d.style.display=='none'){
			SITE_D_$site_serial();
			}else{
			SITE_D2_$site_serial();
			}
			}
			</script>
			<input type="submit" id="A_$site_serial" class="STYLE9" onclick="SITE_use_$site_serial()" value="Open Binding Site Residues" />
			<div id="S_$site_serial" style="DISPLAY: none">
HTML
		}
		undef $residue_id;
		undef $href_residue_id;  # href link
		undef $ref_residue_id;  # reference residue
		if (defined($data3->{RESIDUE_CHAIN}))
		{
			$residue_id="$data3->{RESIDUE_NUM}$data3->{RESIDUE_INSERT}.$data3->{RESIDUE_CHAIN}";
			$href_residue_id="$data3->{RESIDUE_NUM}$data3->{RESIDUE_INSERT}_$data3->{RESIDUE_CHAIN}_$data3->{RESIDUE_NAME}";
		}
		else
		{
			$residue_id="$data3->{RESIDUE_NUM}$data3->{RESIDUE_INSERT}.$data7->{CHAIN}";
			$href_residue_id="$data3->{RESIDUE_NUM}$data3->{RESIDUE_INSERT}_$data7->{CHAIN}_$data3->{RESIDUE_NAME}";
		}
		if (defined($data3->{Ref_RESIDUE_CHAIN}))
		{
			$ref_residue_id="$data3->{Ref_RESIDUE_NUM}$data3->{Ref_RESIDUE_INSERT}.$data3->{Ref_RESIDUE_CHAIN}";
		}
		else
		{
			$ref_residue_id="$data3->{Ref_RESIDUE_NUM}$data3->{Ref_RESIDUE_INSERT}.$data3->{Ref_CHAIN}";
		}
		print qq(<table border="1" cellpadding="10">);
		print qq(<tr><td class="STYLE10">Binding Site Residue Identifier</td><td class="STYLE10"><a name="$href_residue_id">$residue_id</a></td></tr>) if defined($residue_id); #bookmark
		print qq(<tr><td class="STYLE10">Binding Site Residue Name</td><td class="STYLE10">$data3->{RESIDUE_NAME}</td></tr>) if defined($data3->{RESIDUE_NAME});
		print qq(<tr><td class="STYLE10">Binding Site Reference Residue Identifier</td><td class="STYLE10">$ref_residue_id</td></tr>) if defined($ref_residue_id);
		print qq(<tr><td class="STYLE10">Binding Site Reference Residue Name</td><td class="STYLE10">$data3->{Ref_RESIDUE_NAME}</td></tr>) if defined($data3->{Ref_RESIDUE_NAME});
		if (defined($data3->{RESIDUE_HET}) and $data3->{RESIDUE_HET} eq "Y")
		{
			print qq(<tr><td class="STYLE10">Unnatural Residue</td><td class="STYLE10">$data3->{RESIDUE_HET}</td></tr>);
		}
		if (defined($data3->{RESIDUE_SIDEMISS}) and $data3->{RESIDUE_SIDEMISS} eq "Y")
		{
			print qq(<tr><td class="STYLE10">Residue Sidechain Missing</td><td class="STYLE10">$data3->{RESIDUE_SIDEMISS}</td></tr>);
		}
		if (defined($data3->{RESIDUE_BONEMISS}) and $data3->{RESIDUE_BONEMISS} eq "Y")
		{
			print qq(<tr><td class="STYLE10">Residue Backbone Missing</td><td class="STYLE10">$data3->{RESIDUE_BONEMISS}</td></tr>);
		}
		if (defined($data3->{RESIDUE_MUTATION}) and $data3->{RESIDUE_MUTATION} eq "Y")
		{
			print qq(<tr><td class="STYLE10">Residue Mutation</td><td class="STYLE10">$data3->{RESIDUE_MUTATION}</td></tr>);
		}

		if (defined($data3->{RESIDUE_ALL_RMSD}) and $data3->{RESIDUE_ALL_RMSD} >=0)
		{
			print qq(<tr><td class="STYLE10">Binding Site Residue Allatom RMSD</td><td class="STYLE10">$data3->{RESIDUE_ALL_RMSD}</td></tr>);
			print qq(<tr><td class="STYLE10">Binding Site Residue Allatom RMSD \(Site Matched\)</td><td class="STYLE10">$sup_res_all{$href_residue_id}</td></tr>);
		}
		if (defined($data3->{RESIDUE_BONE_RMSD}) and $data3->{RESIDUE_BONE_RMSD} >=0)
		{
			print qq(<tr><td class="STYLE10">Binding Site Residue Backbone RMSD</td><td class="STYLE10">$data3->{RESIDUE_BONE_RMSD}</td></tr>);
			print qq(<tr><td class="STYLE10">Binding Site Residue Backbone RMSD \(Site Matched\)</td><td class="STYLE10">$sup_res_bone{$href_residue_id}</td></tr>);
		}
		if (defined($data3->{RESIDUE_SIDE_RMSD}) and $data3->{RESIDUE_SIDE_RMSD} >=0)
		{
			print qq(<tr><td class="STYLE10">Binding Site Residue Sidechain RMSD</td><td class="STYLE10">$data3->{RESIDUE_SIDE_RMSD}</td></tr>);
			print qq(<tr><td class="STYLE10">Binding Site Residue Sidechain RMSD \(Site Matched\)</td><td class="STYLE10">$sup_res_side{$href_residue_id}</td></tr>);
		}
		print qq(<tr><td class="STYLE10">Binding Site Residue Allatom B-Facotr</td><td class="STYLE10">$bfactor{$href_residue_id}</td></tr>) if (defined($bfactor{$href_residue_id}));
		print qq(<tr><td class="STYLE10">Binding Site Residue Allatom Solvent Accessibility</td><td class="STYLE10">$asa{$href_residue_id}</td></tr>) if (defined($asa{$href_residue_id}));
		print qq(</table>);
	}
	print qq(</div>);
#FOR secondary structures
#
	if (defined($data7->{CHAINB}))
	{
		$sth4 = $dbh1 -> prepare ("SELECT DISTINCT SEC_STR_TYPE, SEC_STR_SERIAL, SEC_STR_SERIAL_CHAIN, SEC_STR_RESIDUE, SEC_STR_RESIDUE_NUM, Ref_SEC_STR_RESIDUE, Ref_SEC_STR_RESIDUE_NUM, SEC_STR_ALL_RMSD, SEC_STR_BONE_RMSD, SEC_STR_CA_RMSD, SEC_STR_SIDE_RMSD, SEC_STR_MUTATION FROM all_2ndstr WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=? AND SITE_RELATE='Y'");
		$sth4 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN}, $data7->{CHAINB});
	}
	else
	{
		$sth4 = $dbh1 -> prepare ("SELECT DISTINCT SEC_STR_TYPE, SEC_STR_SERIAL, SEC_STR_SERIAL_CHAIN, SEC_STR_RESIDUE, SEC_STR_RESIDUE_NUM, Ref_SEC_STR_RESIDUE, Ref_SEC_STR_RESIDUE_NUM, SEC_STR_ALL_RMSD, SEC_STR_BONE_RMSD, SEC_STR_CA_RMSD, SEC_STR_SIDE_RMSD, SEC_STR_MUTATION FROM all_2ndstr WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL AND SITE_RELATE='Y'");
		$sth4 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN});
	}
	while(my $data4 = $sth4 -> fetchrow_hashref)
	{
		$sec_serial ++;
		undef $sec_str_serial_chain_self;
		if (defined($data4->{SEC_STR_SERIAL_CHAIN}))
		{
			if ($data4->{SEC_STR_SERIAL_CHAIN} eq $data7->{Ref_CHAIN})
			{
				$sec_str_serial_chain_self=$data7->{CHAIN};
			}
			else
			{
				$sec_str_serial_chain_self=$data7->{CHAINB};
			}
		}
		else
		{
			$sec_str_serial_chain_self=$data7->{CHAIN};
		}
		print qq(<p class="STYLE9">Seconary Structure Begin...</p>);
		print qq(<table border="1" cellpadding="10">);
		print qq(<tr><td class="STYLE10">Secondary Structure Type</td><td class="STYLE10">$data4->{SEC_STR_TYPE}</td></tr>) if defined($data4->{SEC_STR_TYPE});
		print qq(<tr><td class="STYLE10">Secondary Structure Serial Number</td><td class="STYLE10">$data4->{SEC_STR_SERIAL}</td></tr>) if defined($data4->{SEC_STR_SERIAL});
		print qq(<tr><td class="STYLE10">Secondary Structure Serial Chain</td><td class="STYLE10">$sec_str_serial_chain_self</td></tr>) if defined($sec_str_serial_chain_self);
		if (defined($data4->{SEC_STR_RESIDUE}))
		{
			@sec_res=();
			$sec_res_line="";
			@sec_res=split /:/,$data4->{SEC_STR_RESIDUE};
			$sec_res_line .= "<a href=\"#S$_\">$_</a>:" for @sec_res;
			$sec_res_line=~s/:$//;
			print qq(<tr><td class="STYLE10">Secondary Structure Residues</td><td class="STYLE10">$sec_res_line</td></tr>);
		}
		print qq(<tr><td class="STYLE10">Number of Residues in This Secondary Structure</td><td class="STYLE10">$data4->{SEC_STR_RESIDUE_NUM}</td></tr>) if defined($data4->{SEC_STR_RESIDUE_NUM});
		print qq(<tr><td class="STYLE10">Reference Secondary Structure Residues</td><td class="STYLE10">$data4->{Ref_SEC_STR_RESIDUE}</td></tr>) if defined($data4->{Ref_SEC_STR_RESIDUE});
		print qq(<tr><td class="STYLE10">Number of Residues in This Reference Secondary Structure</td><td class="STYLE10">$data4->{Ref_SEC_STR_RESIDUE_NUM}</td></tr>) if defined($data4->{Ref_SEC_STR_RESIDUE_NUM});
		if (defined($data4->{SEC_STR_ALL_RMSD}) and $data4->{SEC_STR_ALL_RMSD} >=0)
		{
			print qq(<tr><td class="STYLE10">Secondary Structure Allatom RMSD</td><td class="STYLE10">$data4->{SEC_STR_ALL_RMSD}</td></tr>);
		}
		if (defined($data4->{SEC_STR_BONE_RMSD}) and $data4->{SEC_STR_BONE_RMSD} >=0)
		{
			print qq(<tr><td class="STYLE10">Secondary Structure Backbone RMSD</td><td class="STYLE10">$data4->{SEC_STR_BONE_RMSD}</td></tr>);
		}
		if (defined($data4->{SEC_STR_CA_RMSD}) and $data4->{SEC_STR_CA_RMSD} >=0)
		{
			print qq(<tr><td class="STYLE10">Secondary Structure CA RMSD</td><td class="STYLE10">$data4->{SEC_STR_CA_RMSD}</td></tr>);
		}
		if (defined($data4->{SEC_STR_SIDE_RMSD}) and $data4->{SEC_STR_SIDE_RMSD} >=0)
		{
			print qq(<tr><td class="STYLE10">Secondary Structure Sidechain RMSD</td><td class="STYLE10">$data4->{SEC_STR_SIDE_RMSD}</td></tr>);
		}
		if (defined($data4->{SEC_STR_MUTATION}) and $data4->{SEC_STR_MUTATION} ne "NO" and $data4->{SEC_STR_MUTATION} ne "REF")
		{
			print qq(<tr><td class="STYLE10">Secondary Structure Mutation</td><td class="STYLE10">$data4->{SEC_STR_MUTATION}</td></tr>);
		}
		if (defined($data4->{SEC_STR_RESIDUE}))
		{
			@sec_res=();
			@bf_res=();
			@asa_res=();
			$bf_res_line="";
			$asa_res_line="";

			@sec_res=split /:/,$data4->{SEC_STR_RESIDUE};
			
			$sec_bfactor_check=0;
			for my $aaa (@sec_res)
			{
				if (! defined($bfactor{$aaa}))
				{
					$sec_bfactor_check=1;
				}
			}
			if ($sec_bfactor_check ==0)
			{
				@bf_res=sort {$bfactor{$b} <=> $bfactor{$a}}@sec_res;
				$bf_res_line .= "<a href=\"#S$_\">$_</a> > " for @bf_res;
				$bf_res_line=~s/ > $//;
				print qq(<tr><td class="STYLE10">B-Factor Order of Secondary Structure Residues</td><td class="STYLE10">$bf_res_line</td></tr>);
			}

			$sec_asa_check=0;
			for my $bbb (@sec_res)
			{
				if (!defined($asa{$bbb}))
				{
					$sec_asa_check=1;
				}
			}
			if ($sec_asa_check ==0)
			{
				@asa_res=sort {$asa{$b} <=> $asa{$a}}@sec_res;
				$asa_res_line .= "<a href=\"#S$_\">$_</a> > " for @asa_res;
				$asa_res_line=~s/ > $//;
				print qq(<tr><td class="STYLE10">Solvent Accessibility Order of Secondary Structure Residues</td><td class="STYLE10">$asa_res_line</td></tr>);
			}
		}

#for reside rmsd
		if (defined($data7->{CHAINB}))
		{
			$sth12 = $dbh1 -> prepare ("SELECT DISTINCT RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_NAME, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD FROM all_2ndstr WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=? AND SEC_STR_TYPE=? AND SEC_STR_SERIAL=? AND SEC_STR_SERIAL_CHAIN=?");
			$sth12 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN}, $data7->{CHAINB}, $data4->{SEC_STR_TYPE}, $data4->{SEC_STR_SERIAL}, $data4->{SEC_STR_SERIAL_CHAIN});
		}
		elsif (defined($data4->{SEC_STR_SERIAL_CHAIN}))
		{
			$sth12 = $dbh1 -> prepare ("SELECT DISTINCT RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_NAME, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD FROM all_2ndstr WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL AND SEC_STR_TYPE=? AND SEC_STR_SERIAL=? AND SEC_STR_SERIAL_CHAIN=?");
			$sth12 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN}, $data4->{SEC_STR_TYPE}, $data4->{SEC_STR_SERIAL}, $data4->{SEC_STR_SERIAL_CHAIN});
		}
		else
		{
			$sth12 = $dbh1 -> prepare ("SELECT DISTINCT RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_NAME, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD FROM all_2ndstr WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL AND SEC_STR_TYPE=? AND SEC_STR_SERIAL=? AND SEC_STR_SERIAL_CHAIN IS NULL");
			$sth12 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN}, $data4->{SEC_STR_TYPE}, $data4->{SEC_STR_SERIAL});
		}
		@sec_all=();
		%sec_all=();
		$sec_all_line="";
		@sec_bk=();
		%sec_bk=();
		$sec_bk_line="";
		@sec_side=();
		%sec_side=();
		$sec_side_line="";
		while(my $data12 = $sth12 -> fetchrow_hashref)
		{
			if ($data12->{RESIDUE_ALL_RMSD} >=0)
			{
				$sec_all{"$data12->{RESIDUE_NUM}$data12->{RESIDUE_INSERT}_${sec_str_serial_chain_self}_$data12->{RESIDUE_NAME}"}=$data12->{RESIDUE_ALL_RMSD};
			}
			if ($data12->{RESIDUE_BONE_RMSD} >=0)
			{
				$sec_bk{"$data12->{RESIDUE_NUM}$data12->{RESIDUE_INSERT}_${sec_str_serial_chain_self}_$data12->{RESIDUE_NAME}"}=$data12->{RESIDUE_BONE_RMSD};
			}
			if ($data12->{RESIDUE_SIDE_RMSD} >=0)
			{
				$sec_side{"$data12->{RESIDUE_NUM}$data12->{RESIDUE_INSERT}_${sec_str_serial_chain_self}_$data12->{RESIDUE_NAME}"}=$data12->{RESIDUE_SIDE_RMSD};
			}
		}
		@sec_all=sort {$sec_all{$b} <=> $sec_all{$a}} keys %sec_all;
		$sec_all_line .= "<a href=\"#S$_\">$_</a> > " for @sec_all;
		$sec_all_line=~s/ > $//;

		@sec_bk=sort {$sec_bk{$b} <=> $sec_bk{$a}} keys %sec_bk;
		$sec_bk_line .= "<a href=\"#S$_\">$_</a> > " for @sec_bk;
		$sec_bk_line=~s/ > $//;

		@sec_side=sort {$sec_side{$b} <=> $sec_side{$a}} keys %sec_side;
		$sec_side_line .= "<a href=\"#S$_\">$_</a> > " for @sec_side;
		$sec_side_line=~s/ > $//;
		print qq(<tr><td class="STYLE10">Allatom RMSD Order of Secondary Structure Residues</td><td class="STYLE10">$sec_all_line</td></tr>);
		print qq(<tr><td class="STYLE10">Backbone RMSD Order of Secondary Structure Residues</td><td class="STYLE10">$sec_bk_line</td></tr>);
		print qq(<tr><td class="STYLE10">Sidechain RMSD Order of Secondary Structure Residues</td><td class="STYLE10">$sec_side_line</td></tr>);
		print qq(</table>);
print <<HTML;
		<script>
		function SEC_2ND_$sec_serial(element){
		return element = document.getElementById(element);
		}
		function SEC_D_$sec_serial(){
		var d=SEC_2ND_$sec_serial('SEC_$sec_serial');
		d.style.display='block';
		}
		function SEC_D2_$sec_serial(){
		var d=SEC_2ND_$sec_serial('SEC_$sec_serial');
		d.style.display='none';
		}
		function SEC_use_$sec_serial(){
		var d=SEC_2ND_$sec_serial('SEC_$sec_serial');
		if(d.style.display=='none'){
		SEC_D_$sec_serial();
		}else{
		SEC_D2_$sec_serial();
		}
		}
		</script>
		<input type="submit" id="B_$sec_serial" class="STYLE9" onclick="SEC_use_$sec_serial()" value="Open Secondary Structure Residues" />
		<div id="SEC_$sec_serial" style="DISPLAY: none">
HTML
		if (defined($data7->{CHAINB}))
		{
			$sth5 = $dbh1 -> prepare ("SELECT DISTINCT RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_NAME, Ref_RESIDUE_NUM, Ref_RESIDUE_INSERT, Ref_RESIDUE_NAME, RESIDUE_HET, RESIDUE_SIDEMISS, RESIDUE_BONEMISS, RESIDUE_MUTATION, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD FROM all_2ndstr WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=? AND SEC_STR_TYPE=? AND SEC_STR_SERIAL=? AND SEC_STR_SERIAL_CHAIN=?");
			$sth5 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN}, $data7->{CHAINB}, $data4->{SEC_STR_TYPE}, $data4->{SEC_STR_SERIAL}, $data4->{SEC_STR_SERIAL_CHAIN});
		}
		elsif (defined($data4->{SEC_STR_SERIAL_CHAIN}))
		{
			$sth5 = $dbh1 -> prepare ("SELECT DISTINCT RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_NAME, Ref_RESIDUE_NUM, Ref_RESIDUE_INSERT, Ref_RESIDUE_NAME, RESIDUE_HET, RESIDUE_SIDEMISS, RESIDUE_BONEMISS, RESIDUE_MUTATION, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD FROM all_2ndstr WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL AND SEC_STR_TYPE=? AND SEC_STR_SERIAL=? AND SEC_STR_SERIAL_CHAIN=?");
			$sth5 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN}, $data4->{SEC_STR_TYPE}, $data4->{SEC_STR_SERIAL}, $data4->{SEC_STR_SERIAL_CHAIN});
		}
		else
		{
			$sth5 = $dbh1 -> prepare ("SELECT DISTINCT RESIDUE_NUM, RESIDUE_INSERT, RESIDUE_NAME, Ref_RESIDUE_NUM, Ref_RESIDUE_INSERT, Ref_RESIDUE_NAME, RESIDUE_HET, RESIDUE_SIDEMISS, RESIDUE_BONEMISS, RESIDUE_MUTATION, RESIDUE_ALL_RMSD, RESIDUE_BONE_RMSD, RESIDUE_SIDE_RMSD FROM all_2ndstr WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL AND SEC_STR_TYPE=? AND SEC_STR_SERIAL=? AND SEC_STR_SERIAL_CHAIN IS NULL");
			$sth5 -> execute($data7->{CLUSTER}, $data7->{SUBSET}, $pdbid, $data7->{CHAIN}, $data4->{SEC_STR_TYPE}, $data4->{SEC_STR_SERIAL});
		}
		while(my $data5 = $sth5 -> fetchrow_hashref)
		{
			if (defined($data4->{SEC_STR_SERIAL_CHAIN}))
			{
				$sec_str_serial_chain=$data4->{SEC_STR_SERIAL_CHAIN};
			}
			else
			{
				$sec_str_serial_chain=$data7->{Ref_CHAIN};
			}
			print qq(<table border="1" cellpadding="10">);
			print qq(<tr><td class="STYLE10">Seconary Structure Residue Identifier</td><td class="STYLE10"><a name="S$data5->{RESIDUE_NUM}$data5->{RESIDUE_INSERT}_${sec_str_serial_chain_self}_$data5->{RESIDUE_NAME}">$data5->{RESIDUE_NUM}$data5->{RESIDUE_INSERT}.$sec_str_serial_chain_self</a></td></tr>);
			print qq(<tr><td class="STYLE10">Seconary Structure Residue Name</td><td class="STYLE10">$data5->{RESIDUE_NAME}</td></tr>);
			print qq(<tr><td class="STYLE10">Seconary Structure Reference Residue Identifier</td><td class="STYLE10">$data5->{Ref_RESIDUE_NUM}$data5->{Ref_RESIDUE_INSERT}.$sec_str_serial_chain</td></tr>);
			if (defined($data5->{RESIDUE_HET}) and $data5->{RESIDUE_HET} eq "Y")
			{
				print qq(<tr><td class="STYLE10">Unnatural Residue</td><td class="STYLE10">$data5->{RESIDUE_HET}</td></tr>);
			}
			if (defined($data5->{RESIDUE_SIDEMISS}) and $data5->{RESIDUE_SIDEMISS} eq "Y")
			{
				print qq(<tr><td class="STYLE10">Residue Sidechain Missing</td><td class="STYLE10">$data5->{RESIDUE_SIDEMISS}</td></tr>);
			}
			if (defined($data5->{RESIDUE_BONEMISS}) and $data5->{RESIDUE_BONEMISS} eq "Y")
			{
				print qq(<tr><td class="STYLE10">Residue Backbone Missing</td><td class="STYLE10">$data5->{RESIDUE_BONEMISS}</td></tr>);
			}
			if (defined($data5->{RESIDUE_MUTATION}) and $data5->{RESIDUE_MUTATION} eq "Y")
			{
				print qq(<tr><td class="STYLE10">Residue Mutation</td><td class="STYLE10">$data5->{RESIDUE_MUTATION}</td></tr>);
			}
			if (defined($data5->{RESIDUE_ALL_RMSD}) and $data5->{RESIDUE_ALL_RMSD} >=0)
			{
				print qq(<tr><td class="STYLE10">Seconary Structure Residue Allatom RMSD</td><td class="STYLE10">$data5->{RESIDUE_ALL_RMSD}</td></tr>);
			}
			if (defined($data5->{RESIDUE_BONE_RMSD}) and $data5->{RESIDUE_BONE_RMSD} >=0)
			{
				print qq(<tr><td class="STYLE10">Seconary Structure Residue Backbone RMSD</td><td class="STYLE10">$data5->{RESIDUE_BONE_RMSD}</td></tr>);
			}
			if (defined($data5->{RESIDUE_SIDE_RMSD}) and $data5->{RESIDUE_SIDE_RMSD} >=0)
			{
				print qq(<tr><td class="STYLE10">Seconary Structure Residue Sidechain RMSD</td><td class="STYLE10">$data5->{RESIDUE_SIDE_RMSD}</td></tr>);
			}
			print qq(<tr><td class="STYLE10">Seconary Structure Residue Allatom B-Facotr</td><td class="STYLE10">$bfactor{"$data5->{RESIDUE_NUM}$data5->{RESIDUE_INSERT}_${sec_str_serial_chain_self}_$data5->{RESIDUE_NAME}"}</td></tr>) if (defined($bfactor{"$data5->{RESIDUE_NUM}$data5->{RESIDUE_INSERT}_${sec_str_serial_chain_self}_$data5->{RESIDUE_NAME}"}));
			print qq(<tr><td class="STYLE10">Seconary Structure Residue Allatom Solvent Accessibility</td><td class="STYLE10">$asa{"$data5->{RESIDUE_NUM}$data5->{RESIDUE_INSERT}_${sec_str_serial_chain_self}_$data5->{RESIDUE_NAME}"}</td></tr>) if (defined($asa{"$data5->{RESIDUE_NUM}$data5->{RESIDUE_INSERT}_${sec_str_serial_chain_self}_$data5->{RESIDUE_NAME}"}));
			print qq(</table>);
		}
		print qq(</div>);
		print qq(<p class="STYLE9">Seconary Structure End</p>);
	}
	$link ++;
print <<HTML;
	<script>
	function LINK_$link(element){
	return element = document.getElementById(element);
	}
	function LINK_D_$link(){
	var d=LINK_$link('lin_$link');
	d.style.display='block';
	}
	function LINK_D2_$link(){
	var d=LINK_$link('lin_$link');
	d.style.display='none';
	}
	function LINK_use_$link(){
	var d=LINK_$link('lin_$link');
	if(d.style.display=='none'){
	LINK_D_$link();
	}else{
	LINK_D2_$link();
	}
	}
	</script>
	<input type="submit" id="L_$link" class="STYLE9" onclick="LINK_use_$link()" value="Open Links" />
	<div id="lin_$link" style="DISPLAY: none">
	<p>&nbsp;</p>
	<table border="1" cellpadding="10">
	<tr><td class="STYLE10">Binding Site</td></tr>
	<tr><td class="STYLE10"><a href="http://pisite.hgc.jp/cgi-bin/view.cgi?pdbid=$pdbid&chain=$data7->{CHAIN}" target="_blank">PiSITE  $pdbid$data7->{CHAIN}</a></td></tr>
HTML
	if (defined($data7->{CHAINB}))
	{
		print qq(<tr><td class="STYLE10"><a href="http://pisite.hgc.jp/cgi-bin/view.cgi?pdbid=$pdbid&chain=$data7->{CHAINB}" target="_blank">PiSITE  $pdbid$data7->{CHAINB}</a></td></tr>);
	}
	print qq(<tr><td class="STYLE10"><a href="http://firedb.bioinfo.cnio.es/Php/FireDB.php?pdbcode=$pdbid$data7->{CHAIN}&cutoff=45" target="_blank">FireDB  $pdbid$data7->{CHAIN}</a></td></tr>);
	if (defined($data7->{CHAINB}))
	{
		print qq(<tr><td class="STYLE10"><a href="http://firedb.bioinfo.cnio.es/Php/FireDB.php?pdbcode=$pdbid$data7->{CHAINB}&cutoff=45" target="_blank">FireDB  $pdbid$data7->{CHAINB}</a></td></tr>);
	}
print <<HTML;	
	<tr><td class="STYLE10"><a href="http://www.ebi.ac.uk/pdbe-srv/view/entry/$pdbid/summary.html" target="_blank">PDBe  $pdbid</a></td></tr>
	<tr><td class="STYLE10"><a href="http://bioinf-tomcat.charite.de/supersite/resultPDB.faces?pdbid=$pdbid" target="_blank">SuperSite  $pdbid</a></td></tr>
	<tr><td class="STYLE10"><a href="http://www.bioinfo-pharma.u-strasbg.fr/scPDB/">sc-PDB</a></td></tr>
	<tr><td class="STYLE10"><a href="http://www.bigre.ulb.ac.be/Users/benoit/LigASite/>LigAsite</a></td></tr>
	<tr><td class="STYLE10"><a href="http://relibase.ccdc.cam.ac.uk/account_utilities/login_form.php" target="_blank">Relibase</a></td></tr>
	<tr><td class="STYLE10"><a href="http://srs6.bionet.nsc.ru/srs6bin/cgi-bin/wgetz?-page+query+-id+3p7W21blDMK" target="_blank">PDBSITE</a></td></tr>
	</table>
	&nbsp;<br />
	&nbsp;<br />
	<table border="1" cellpadding="10">
	<tr><td class="STYLE10">Binding Affinity</td></tr>
	<tr><td class="STYLE10"><a href="http://www.bindingdb.org/jsp/dbsearch/PrimarySearch_pdbids.jsp?pdbids=$pdbid&pdbids_submit=Search" target="_blank">Binding DB  $pdbid</a></td></tr>
	<tr><td class="STYLE10"><a href="http://pc1664.pharmazie.uni-marburg.de/affinity/viewPDB.php?pdbcode=$pdbid" target="_blank">AffinDB  $pdbid</a></td></tr>
	<tr><td class="STYLE10"><a href="http://www.pdbbind.org.cn" target="_blank">PDBbind</a></td></tr>
	<tr><td class="STYLE10"><a href="http://www.bindingmoad.org/moad/welcome.do" target="_blank">Binding MOAD</a></td></tr>
	</table>
	&nbsp;<br />
	&nbsp;<br />
	<table border="1" cellpadding="10">
	<tr><td class="STYLE10">Ligand Only</td></tr>
	<tr><td class="STYLE10"><a href="http://xray.bmc.uu.se/hicup/" target="_blank">HIC-Up</a></td></tr>
	<tr><td class="STYLE10"><a href="http://www.idrtech.com/PDB-Ligand/" target="_blank">PDB-ligand</a></td></tr>
	<tr><td class="STYLE10"><a href="http://bioinf.charite.de/superligands/" target="_blank">Super Ligands</a></td></tr>
	<tr><td class="STYLE10"><a href="http://ligand-expo.rcsb.org/ld-search.html" target="_blank">Ligand Expo</a></td></tr>
	</table>
	&nbsp;<br />
	&nbsp;<br />
	<table border="1" cellpadding="10">
	<tr><td class="STYLE10">Flexibility</td></tr>
	<tr><td class="STYLE10"><a href="http://www.molmovdb.org/cgi-bin/cath.cgi?set=auto" target="_blank">MolMovDB</a></td></tr>
	<tr><td class="STYLE10"><a href="http://fizz.cmp.uea.ac.uk/dyndom/" target="_blank">DynDom</a></td></tr>
	<tr><td class="STYLE10"><a href="http://74.54.147.134/~ezepcdb3/" target="_blank">PCDB</a></td></tr>
	<tr><td class="STYLE10"><a href="http://www.pocketome.org/" target="_blank">Pocketome</a></td></tr>
	</table>
	&nbsp;<br />
	&nbsp;<br />
	<table border="1" cellpadding="10">
	<tr><td class="STYLE10">Sequence Link</td></tr>
	<tr><td class="STYLE10"><a href="http://www.ncbi.nlm.nih.gov/sites/entrez?db=protein" target="_blank">NCBI Entrez Protein database</a></td></tr>
	</table>
	&nbsp;<br />
	&nbsp;<br />
	<table border="1" cellpadding="10">
	<tr><td class="STYLE10">Others...</td></tr>
	<tr><td class="STYLE10"><a href="http://www.rcsb.org/pdb/explore/explore.do?structureId=$pdbid" target="_blank">Protein Data Bank  $pdbid</a></td></tr>
	<tr><td class="STYLE10"><a href="http://www.ncbi.nlm.nih.gov/sites/entrez?SUBMIT=y&db=structure&orig_db=structure&term=$pdbid" target="_blank">MMDB  $pdbid</a></td></tr>
	<tr><td class="STYLE10"><a href="http://www.ebi.ac.uk/thornton-srv/databases/cgi-bin/pdbsum/GetPage.pl?pdbcode=$pdbid" target="_blank">PDBsum  $pdbid</a></td></tr>
	<tr><td class="STYLE10"><a href="http://hetpdbnavi.nagahama-i-bio.ac.jp/" target="_blank">Het-PDB</a></td></tr>
	<tr><td class="STYLE10"><a href="http://compbio.cs.toronto.edu/psmdb/" target="_blank">PSMDB</a></td></tr>
	<tr><td class="STYLE10"><a href="http://www.ebi.ac.uk/thornton-srv/databases/CSA/" target="_blank">Cathalytic Site Atlas</a></td></tr>
	</table>
	</div>
	&nbsp;<br />
	&nbsp;<br />
	&nbsp;<br />
	&nbsp;<br />
	<p class="STYLE9">~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>
HTML
	print qq(</div>);
}
print qq(</div>);
if ($num_cluster > 0)
{
	$sth1 -> finish();
	$sth2 -> finish();
	$sth3 -> finish();
	$sth4 -> finish();
	$sth5 -> finish();
	$sth7 -> finish();
	$sth8 -> finish();
	$sth9 -> finish();
	$sth10 -> finish();
	$sth11 -> finish();
	$sth12 -> finish();
	$sth14 -> finish();
}
elsif ($num_cluster == 0)
{
	$sth1 -> finish();
	$sth2 -> finish();
	$sth7 -> finish();
	$sth8 -> finish();
	$sth9 -> finish();
	$sth10 -> finish();
}
if (defined ($sth13))
{
	$sth13 -> finish();
}
$dbh1 -> disconnect || warn("Disconnection failed: $DBI::errstr\n");
$dbh2 -> disconnect || warn("Disconnection failed: $DBI::errstr\n");
print <<HTML;
    </td>
    <td class="STYLE11"><p><img src="/flexsite/space.gif" height="1" border="0" /></p></td>
  </tr>
  <tr>
    <td width="15%">&nbsp;</td>
    <td width="5%">&nbsp;</td>
    <td width="37.5%">&nbsp;</td>
    <td width="37.5%">&nbsp;</td>
    <td width="5%">&nbsp;</td>
  </tr>
</table>
</body>
</html>
HTML
