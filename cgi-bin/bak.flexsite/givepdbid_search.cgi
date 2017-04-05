#!/usr/bin/perl -w
#used for searching by protein information.   2009.08.03
#
use CGI qw/:standard/;
use DBI;
use CGI::Carp qw(fatalsToBrowser);

my $db2="fpdb3";
my $server2 = '172.16.1.204';
my $port2 = '3306';
my $dbuser2 = 'liwei';
my $dbpasswd2 = 'liwei0703';
my $dbh2 = DBI -> connect("DBI:mysql:$db2:$server2:$port2",$dbuser2,$dbpasswd2,{ PrintError => 0}) || die("unable to connect to database $db2: $DBI::errstr\n");

$ec_num=param('ec_num');
$cath=param('cath');
$name=param('name');
$type=param('type');
$resolution1=param('resolution1');
$resolution2=param('resolution2');
$mutation=param('mutation');
$source=param('source');
$express=param('express');
$free_r1=param('free_r1');
$free_r2=param('free_r2');

my $query2="";  #fpdb-chain
my $query3="";  #fpdb-general

if ($ec_num ne "")
{
	$query2=$query2."EC LIKE '$ec_num%' AND ";
}
if ($name ne "")
{
	$name=~s/(.*)/\U$1/g;
	$query2=$query2."MOLECULE LIKE '%$name%' AND ";
}
if ($type ne "")
{
	if ($type ne "all")
	{
		$query2=$query2."TYPE = '$type' AND ";
	}
}
if ($resolution1 ne "")
{
	$query3=$query3."RESOLUTION >= $resolution1 AND ";
}
if ($resolution2 ne "")
{
	$query3=$query3."RESOLUTION <= $resolution2 AND ";
}
if ($mutation ne "")
{
	if ($mutation ne "all")
	{
		if ($mutation eq "yes")
		{
			$query2=$query2."MUTATION = 'YES' AND ";
		}
		elsif ($mutation eq "no")
		{
			$query2=$query2."MUTATION IS NULL AND ";
		}
	}
}
if ($source ne "")
{
	$source=~s/(.*)/\U$1/g;
	$query2=$query2."(SOURCE_ORGANISM_SCI LIKE '%$source%' OR SOURCE_ORGANISM_COM LIKE '%$source%') AND ";
}
if ($express ne "")
{
	$express=~s/(.*)/\U$1/g;
	$query2=$query2."SOURCE_TISSUE LIKE '%$express%' AND ";
}
if ($free_r1 ne "")
{
	$query3=$query3."FREE_R >= $free_r1 AND ";
}
if ($free_r2 ne "")
{
	$query3=$query3."FREE_R <= $free_r2 AND ";
}
@q1_pdbid=();
if ($cath ne "")
{
	@cath=split /\./,$cath;
	$cath_line="";
	for (@cath)
	{
		$cath_line .= "$_ +";
	}
	@q1_pdbid_tmp=`egrep '^[0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z] +$cath_line' /flexsite/www/html/flexsite/CathDomainList.htm`;
	for (@q1_pdbid_tmp)
	{
		$q1_pdbid=substr($_,0,4);
		push @q1_pdbid,$q1_pdbid;
	}
	for (my $k=0;$k<$#q1_pdbid;$k++)
	{
		for (my $h=$k+1;$h<=$#q1_pdbid;$h++)
		{
			if ($q1_pdbid[$k] eq $q1_pdbid[$h])
			{
				splice (@q1_pdbid,$h,1);
				$h=$h-1;
			}
		}
	}
}

@q2_pdbid=();
if ($query2 ne "")
{
	$query2=~s/AND $//;
	$sth2 = $dbh2 -> prepare ("SELECT DISTINCT PDBID FROM chain WHERE $query2");
	$sth2 -> execute();
	while(my $data2 = $sth2 -> fetchrow_hashref)
	{
		push @q2_pdbid,$data2->{PDBID};
	}
}
	
@q3_pdbid=();
if ($query3 ne "")
{
	$query3=~s/AND $//;
	$sth3 = $dbh2 -> prepare ("SELECT DISTINCT PDBID FROM general WHERE $query3");
	$sth3 -> execute(); 
	while(my $data3 = $sth3 -> fetchrow_hashref)
	{
		push @q3_pdbid, $data3->{PDBID};
	}
}

$number=3;  #the selected pdbid should appear three times in @total_pdbid.
if ($cath eq "")  #if customer did not fill the query1, then the selected pdbid should appear ($number - 1) times in @total_pdbid.
{
	$number --;
}
if ($query2 eq "")
{
	$number --;
}
if ($query3 eq "")
{
	$number --;
}

@total_pdbid=();
push @total_pdbid,@q1_pdbid;
push @total_pdbid,@q2_pdbid;
push @total_pdbid,@q3_pdbid;

%count=();
for my $pdbid (@total_pdbid)
{
	$count{$pdbid} ++;
}
for (my $i=0;$i<$#total_pdbid;$i++)
{
	for (my $j=$i+1;$j<=$#total_pdbid;$j++)
	{
		if ($total_pdbid[$i] eq $total_pdbid[$j])
		{
			splice (@total_pdbid,$j,1);
			$j = $j - 1;
		}
	}
}

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

$order=0;
for my $pdbid (@total_pdbid)
{
	if ($count{$pdbid} == $number)
	{
		$order++;
		print <<HTML;
		<form action="/cgi-bin/flexsite/protein_search_all.cgi" method="post" name="protein_pdbid$order" enctype="multipart/form-data">
		<p><input type="text" name="pdbid" value="$pdbid" />&nbsp;&nbsp;&nbsp;<input type="submit" name="search_id$order" value="view" /></p>
		</form>
HTML
	}
}
	
if ($query2 ne "")
{
	$sth2 -> finish();
}
if ($query3 ne "")
{
	$sth3 -> finish();
}
if ($query2 ne "" or $query3 ne "")
{
	$dbh2 -> disconnect || warn("Disconnection failed: $DBI::errstr\n");
}
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
