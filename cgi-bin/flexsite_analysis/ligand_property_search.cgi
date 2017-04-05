#!/usr/bin/perl -w
#used for searching by protein information.   2009.08.03
#
use CGI qw/:standard/;
use DBI;
use CGI::Carp qw(fatalsToBrowser);
$CGI::POST_MAX = 1024 * 300;

my $db1="FlexSiteDB3";
my $server1 = '172.16.1.204';
my $port1 = '3306';
my $dbuser1 = 'liweiread';
my $dbpasswd1 = 'liwei0703';
my $dbh1 = DBI -> connect("DBI:mysql:$db1:$server1:$port1",$dbuser1,$dbpasswd1,{ PrintError => 0}) || die("unable to connect to database $db1: $DBI::errstr\n");

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

$query1="";

$str_mw_1=param('mw_1');
$str_mw_2=param('mw_2');
if ($str_mw_1 ne "")
{
	$query1 .= "MW >= $str_mw_1 AND ";
}
if ($str_mw_2 ne "")
{
	$query1 .= "MW <= $str_mw_2 AND ";
}

$str_heavyatom_1=param('heavyatom_1');
$str_heavyatom_2=param('heavyatom_2');
if ($str_heavyatom_1 ne "")
{
	$query1 .= "N_heavy >= $str_heavyatom_1 AND ";
}
if ($str_heavyatom_2 ne "")
{
	$query1 .= "N_heavy <= $str_heavyatom_2 AND ";
}

$str_rotbond_1=param('rotbond_1');
$str_rotbond_2=param('rotbond_2');
if ($str_rotbond_1 ne "")
{
	$query1 .= "smalln_rot >= $str_rotbond_1 AND ";
}
if ($str_rotbond_2 ne "")
{
	$query1 .= "smalln_rot <= $str_rotbond_2 AND ";
}

if ($query1 ne "")
{
	$order=0;
	$query1=~s/AND $//;
	$sth1 = $dbh1 -> prepare ("SELECT DISTINCT LIGAND_NAME FROM interaction WHERE $query1");
	$sth1 -> execute();
	while(my @row1 = $sth1 -> fetchrow_array)
	{
		$ligname=$row1[0];
		$order ++;
		print <<HTML;
		<form action="/cgi-bin/flexsite/ligand_id_search_another.cgi" method="post" name="ligid$order" enctype="multipart/form-data" target="_blank">
		<p><input type="text" name="ligid" value="$ligname" >&nbsp;&nbsp;&nbsp;<input type="submit" name="search_id$order" value="protein" ><a href="http://ligand-expo.rcsb.org/pyapps/ldHandler.py?formid=cc-index-search&target=$ligname&operation=ccid" target="_blank">Ligand Expo</a>&nbsp;&nbsp;&nbsp;<a href="http://xray.bmc.uu.se/hicup/$ligname/" target="_blank">HIC-UP</a></p>
		</form>
HTML
	}
	if ($order == 0)
	{
		print qq(<p class="STYLE9">No structure in Flex-Site DB matchs</p>);
	}
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
