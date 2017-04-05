#!/usr/bin/perl -w
#used for searching by protein information.   2009.08.03
#
use CGI qw/:standard/;
use DBI;
use CGI::Carp qw(fatalsToBrowser);

use DBI;
my $db='fpdb3';
my $server='172.16.1.204';
my $port='3306';
my $dbuser='liweiread';
my $dbpasswd='liwei0703';
my $dbh = DBI -> connect ("DBI:mysql:$db:$server:$port",$dbuser,$dbpasswd,{ PrintError => 0}) || die("unable to connect to database $db:$DBI::errstr\n");
my $sth1 = $dbh -> prepare ("SELECT DISTINCT PDBID, DL_LIGAND_ID, COFACTOR FROM chain");

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

$ligand = param('ligid');
$ligand =~s/\s+//g;
$ligand =uc($ligand);
$order=0;
$sth1 -> execute();
while(my @row1 = $sth1 -> fetchrow_array)
{
	$pdbid=$row1[0];
	if (defined($row1[1]) and $row1[1] eq $ligand)
	{
		$order++;
		print <<HTML;
		<form action="/cgi-bin/flexsite/protein_search_all.cgi" method="post" name="protein_pdbid$order" enctype="multipart/form-data" target="_blank">
		<p><input type="text" name="pdbid" value="$pdbid" >&nbsp;&nbsp;&nbsp;<input type="submit" name="search_id$order" value="view" ></p>
		</form>
HTML
	}
	elsif (defined($row1[2]))
	{
		@cof=split /\s+/, $row1[2];
		for my $cofactor (@cof)
		{
			if ($cofactor eq $ligand)
			{
				$order ++;
print <<HTML;
				<form action="/cgi-bin/flexsite/protein_search_all.cgi" method="post" name="protein_pdbid$order" enctype="multipart/form-data" target="_blank">
				<p><input type="text" name="pdbid" value="$pdbid" >&nbsp;&nbsp;&nbsp;<input type="submit" name="search_id$order" value="view" ></p>
				</form>
HTML
				last;
			}
		}
	}
}
if ($order == 0)
{
	print qq(<p class="STYLE9">No structure in Flex-Site DB matchs</p>);
}
$sth1 -> finish();
$dbh -> disconnect || warn("Disconnection failed: $DBI::errstr\n");
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
