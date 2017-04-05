#!/usr/bin/perl -w
#used for searching by interaction information.   2009.08.20
#
use CGI qw/:standard/;
use DBI;
use CGI::Carp qw(fatalsToBrowser);

my $db1="FlexSiteDB3";
my $server1 = '172.16.1.204';
my $port1 = '3306';
my $dbuser1 = 'liweiread';
my $dbpasswd1 = 'liwei0703';
my $dbh1 = DBI -> connect("DBI:mysql:$db1:$server1:$port1",$dbuser1,$dbpasswd1,{ PrintError => 0}) || die("unable to connect to database $db1: $DBI::errstr\n");

my $db2="fpdb3";
my $server2 = '172.16.1.204';
my $port2 = '3306';
my $dbuser2 = 'liweiread';
my $dbpasswd2 = 'liwei0703';
my $dbh2 = DBI -> connect("DBI:mysql:$db2:$server2:$port2",$dbuser2,$dbpasswd2,{ PrintError => 0}) || die("unable to connect to database $db2: $DBI::errstr\n");

$query4="";  #FlexSiteDB-single_site

#Binding Site Protein Information
$num_of_res_1=param('num_of_res_1');
$num_of_res_2=param('num_of_res_2');
if ($num_of_res_1 ne "")
{
	$query4 .= "STAND_POCKET_RES_NUM >= $num_of_res_1 AND ";
}
if ($num_of_res_2 ne "")
{
	$query4 .= "STAND_POCKET_RES_NUM <= $num_of_res_2 AND ";
}

$multi_structs_1=param('multi_structs_1');
$multi_structs_2=param('multi_structs_2');
if ($multi_structs_1 ne "")
{
	$query4 .= "MULTI_STRUCTS >= $multi_structs_1 AND ";
}
if ($multi_structs_2 ne "")
{
	$query4 .= "MULTI_STRUCTS <= $multi_structs_2 AND ";
}

$multi_comlex_1=param('multi_comlex_1');
$multi_comlex_2=param('multi_comlex_2');
if ($multi_comlex_1 ne "")
{
	$query4 .= "MULTI_COMX >= $multi_comlex_1 AND ";
}
if ($multi_comlex_2 ne "")
{
	$query4 .= "MULTI_COMX <= $multi_comlex_1 AND "; 
}

$multi_ligs_1=param('multi_ligs_1');
$multi_ligs_2=param('multi_ligs_2');
if ($multi_ligs_1 ne "")
{
	$query4 .= "MULTI_LIGS >= $multi_ligs_1 AND ";
}
if ($multi_ligs_2 ne "")
{
	$query4 .= "MULTI_LIGS <= $multi_ligs_2 AND ";
}

@clut=();
if ($query4 ne "")
{
	$query4=~s/AND $//;
	$sth6 = $dbh2 -> prepare ("SELECT DISTINCT MOLECULE FROM chain WHERE PDBID=? AND CHAIN=?");
	$sth4 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE $query4");
	$sth4 -> execute();
	while(my $data4 = $sth4 -> fetchrow_hashref)
	{
		push @clut,"$data4->{CLUSTER}-$data4->{SUBSET}";
		push @{"$data4->{CLUSTER}-$data4->{SUBSET}"},"$data4->{PDBID}=$data4->{CHAIN}=$data4->{CHAINB}=$data4->{LIGAND_SPEC}=$data4->{LIGAND_NAME}";
	}
}
for (my $i=0;$i<$#clut;$i++)
{
	for (my $j=$i+1;$j<=$#clut;$j++)
	{
		if ($clut[$i] eq $clut[$j])
		{
			splice (@clut,$j,1);
			$j=$j-1;
		}
	}
}
print "Content-type: text/html\n\n";
print <<HTML;
<html>
<head>
<title></title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<link rel="stylesheet" href="/flexsite/flex.css" type="text/css" >
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
    <td colspan="5" bgcolor="#5C743D"><img src="/flexsite/space.gif" width="1" height="2" border="0" ></td>
  </tr>

  <tr>
    <td colspan="5" bgcolor="#99CC66" background="/flexsite/line.gif"><img src="/flexsite/line.gif" width="4" height="3" border="0" ></td>
  </tr>
  <script type="text/javascript">
  document.write("<tr bgcolor='#99CC66'>");
  document.write("<td height='20' colspan='6' bgcolor='#FFCC99' id='dateformat'>");
  document.write(Date());
  document.write("</td></tr>");
  </script>

  <tr>
    <td colspan="5" bgcolor="#99CC66" background="/flexsite/line.gif"><img src="/flexsite/line.gif" width="4" height="3" border="0" ></td>
  </tr>

  <tr>
    <td colspan="5" bgcolor="#5C743D"><img src="/flexsite/space.gif" width="1" height="2" border="0" ></td>
  </tr>

 <tr>
    <td valign="top" bgcolor="#FFFFCC">
	<table width="90%" height="200" cellpadding="0" cellspacing="0" border='0' class="navText" id="navigation">
        <tr>
          <td height="7%" bgcolor="#FFFFCC">&nbsp;<br ></td>
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
	  <td height="7%" bgcolor="#FFFFCC">&nbsp;<br ></td>
	 </tr>
	<tr>
	  <td height="7%" bgcolor="#FFFFCC">&nbsp;<br ></td>
	 </tr>
	<tr>
	  <td height="7%" bgcolor="#FFFFCC">&nbsp;<br ></td>
	 </tr>
      </table>
    </td>
    <td class="STYLE11"><p><img src="/flexsite/space.gif" height="1" border="0" ></p></td>
    <td colspan="2" valign="top"  class="STYLE10"><p>&nbsp;</p>
      <p align="left" class="STYLE9"></p>
      <p>&nbsp;</p>
HTML

$order=0;
for my $clut_line (@clut)
{
	$molecule1="";
	$molecule2="";
	@pdb=split /=/, ${$clut_line}[0];
	$pdbid_s=$pdb[0];
	$chain_s_a=$pdb[1];
	$sth6 -> execute($pdbid_s, $chain_s_a);
	while(my $data6 = $sth6 -> fetchrow_hashref)
	{
		$molecule1 = $data6->{MOLECULE};
	}
	print <<HTML;
	&nbsp;<br >
	&nbsp;<br >
	<p>CHAIN 1: $molecule1</p>
HTML
	if (defined($pdb[2]) and $pdb[2] ne "")
	{
		$chain_s_b=$pdb[2];
		$sth6 -> execute($pdbid_s, $chain_s_b);
		while(my $data6 = $sth6 -> fetchrow_hashref)
		{
			$molecule2 = $data6->{MOLECULE};
		}
		print <<HTML;
		<p>CHAIN 2: $molecule2</p>
HTML
	}
	for my $site_line (@{$clut_line})
	{
		@lig=();
		$chain="";
		@pdb=split /=/,$site_line;
		$order++;
		$pdbid=$pdb[0];
		if (defined($pdb[2]) and $pdb[2] ne "")
		{
			$chain="$pdb[1]_$pdb[2]";
		}
		else
		{
			$chain=$pdb[1];
		}
		if (defined($pdb[4]))
		{
			$ligname_line=$pdb[4];
			@lig=split /~/, $ligname_line;
		}
		print <<HTML;
		<table>
		<tr>
		<td>
		<form action="/cgi-bin/flexsite/protein_search_all.cgi" method="post" name="protein_pdbid$order" enctype="multipart/form-data" target="_blank">
		<input type="text" name="pdbid" value="$pdbid" >$chain&nbsp;&nbsp;&nbsp;<input type="submit" name="search_id$order" value="view" >
		</form>
		</td>
HTML
		for my $ligname (@lig)
		{
			$order++;
			print <<HTML;
			<td>
			<form action="/cgi-bin/flexsite/ligand_id_search_another.cgi" method="post" name="ligid$order" enctype="multipart/form-data" target="_blank">
			<input type="text" name="ligid" value="$ligname" >&nbsp;&nbsp;&nbsp;<input type="submit" name="search_id$order" value="protein" >
			</form>
			</td>
HTML
		}
		print <<HTML;
		</tr>
		</table>
HTML
	}
}
if ($order == 0)
{
	print qq(<p class="STYLE9">No structure in Flex-Site DB matchs</p>);
}
	
if ($query4 ne "")
{
	$sth4 -> finish();
	$sth6 -> finish();
	$dbh1 -> disconnect || warn("Disconnection failed: $DBI::errstr\n");
	$dbh2 -> disconnect || warn("Disconnection failed: $DBI::errstr\n");
}
print <<HTML;
    </td>
    <td class="STYLE11"><p><img src="/flexsite/space.gif" height="1" border="0" ></p></td>
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
