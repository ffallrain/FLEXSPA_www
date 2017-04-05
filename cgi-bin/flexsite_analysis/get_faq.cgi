#!/usr/bin/perl -w
#used for searching by interaction information.   2009.08.20
#
use CGI qw/:standard/;
use DBI;
use CGI::Carp qw(fatalsToBrowser);

my $id = $ENV{'REMOTE_ADDR'}.time().$$;
$faq=param('faq');
open RE,"> /flexsite/www/html/flexsite/faq/$id.txt";
print RE "$id\n";
print RE $faq;
close RE;
print "Content-type: text/html\n\n";
print <<HTML;
<html>
<head>
<title>FAQ</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<link rel="stylesheet" href="/flexsite/flex.css" type="text/css" >
<style type="text/css">
<!--
.STYLE1 {color: #CC9933}
.STYLE2 {
	font-family: Author;
	font-size: 36px;
	font-weight: bold;
}
.STYLE8 {
	font-size: 18px;
	font-weight: bold;
	color: #CC6600;
}
.STYLE11 {
	font-size: 12px;
	font-weight: bold;
	color: #FF3399;
}
.STYLE14 {color: #666666; font-size: 16px;}
-->
</style>
</head>
<body bgcolor="#F4FFE4">
<table width="100%" height="100%" border="0" cellspacing="0" cellpadding="0">
  <tr bgcolor="#D5EDB3">
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
    <td colspan="5" bgcolor="#99CC66" background="line.gif"><img src="/flexsite/line.gif" width="4" height="3" border="0" ></td>
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
    <td colspan="2" valign="top"><p>&nbsp;</p>
      <p align="left" class="STYLE8">FAQ:</p>
      <p align="left" class="STYLE8">1. What Can Flex-Site DB provide ?</p>
      <p class="STYLE14">Flex-Site DB provides much useful information: the summary of the protein PDB file content, multiple conformations for the same protein, the binding site and secondary structure location, binding site and secondary structure conformational change, the residue normalized B-factor, the residue solvent accessible molecular surface, the residue sidechain dihedral angle, the datasets selected for several specific analysis, descriptors of protein-ligand interaction including conventional hydrogen bond, weak hydrogen bond, halogen bond, AHPDI (Atom hydrophobicity difference), BURCP (Ligand Buried carbon percentage), Hydrophobic contact.</p> 
      &nbsp;<br >
      &nbsp;<br >
      <p align="left" class="STYLE8">2. Can I get the entire database ?</p>
      <p class="STYLE14">Yes, All of these protein and ligand structures can be downloaded. The entire database and some derived datasets can also be downloaded. We will derive more useful datasets in the future.</p>
      &nbsp;<br >
      &nbsp;<br >
      &nbsp;<br >
      &nbsp;<br >
      <p align="left" class="STYLE8"> Quetions From The Users</p>
    <form action="./get_faq.cgi" method="post" name="fq" enctype="multipart/form-data">
    <textarea name="faq" wrap="physical" rows="15" cols="60">
    Your question has been submitted, we will reply it soon...
    </textarea>
    </p><input type="submit" name="fq_sub" value="Submit" >&nbsp;&nbsp;&nbsp;&nbsp;<input value="Clear Input" type="button" onclick="this.form.faq.value=''">
    </form>
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
