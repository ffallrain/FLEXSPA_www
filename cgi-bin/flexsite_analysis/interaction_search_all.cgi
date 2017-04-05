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

$query1="";  #FlexSiteDB-single_site
$query2_h="";  #FlexSiteDB-single_single_2ndstr
$query2_e="";  #FlexSiteDB-single_single_2ndstr
$query2_c="";  #FlexSiteDB-single_single_2ndstr
$query3="";  #FlexSiteDB-interaction
$query5_h="";  #FlexSiteDB-single_single_2ndstr
$query5_e="";  #FlexSiteDB-single_single_2ndstr
$query5_c="";  #FlexSiteDB-single_single_2ndstr

#Binding Site Interaction Information
$hbond_1=param('hbond_1');
$hbond_2=param('hbond_2');
if ($hbond_1 ne "")
{
	$query3 .= "convention_hb >= $hbond_1 AND ";
}
if ($hbond_2 ne "")
{
	$query3 .= "convention_hb <= $hbond_2 AND ";
}

$halbond_1=param('halbond_1');
$halbond_2=param('halbond_2');
if ($halbond_1 ne "")
{
	$query3 .= "halbond >= $halbond_1 AND ";
}
if ($halbond_2 ne "")
{
	$query3 .= "halbond <= $halbond_2 AND ";
}

$pp_1=param('pp_1');
$pp_2=param('pp_2');
if ($pp_1 ne "")
{
	$query3 .= "pi_pi >= $pp_1 AND ";
}
if ($pp_2 ne "")
{
	$query3 .= "pi_pi <= $pp_2 AND ";
}

$w_hbond_1=param('w_hbond_1');
$w_hbond_2=param('w_hbond_2');
if ($w_hbond_1 ne "")
{
	$query3 .= "weak_hb >= $w_hbond_1 AND ";
}
if ($w_hbond_2 ne "")
{
	$query3 .= "weak_hb <= $w_hbond_2 AND ";
}

$xp_1=param('xp_1');
$xp_2=param('xp_2');
if ($xp_1 ne "")
{
	$query3 .= "no_pi >= $xp_1 AND ";
}
if ($xp_2 ne "")
{
	$query3 .= "no_pi <= $xp_2 AND ";
}

$cp_1=param('cp_1');
$cp_2=param('cp_2');
if ($cp_1 ne "")
{
	$query3 .= "cdonor_pi >= $cp_1 AND ";
}
if ($cp_2 ne "")
{
	$query3 .= "cdonor_pi <= $cp_2 AND ";
}

$cx_1=param('cx_1');
$cx_2=param('cx_2');
if ($cx_1 ne "")
{
	$query3 .= "cdonor_no >= $cx_1 AND ";
}
if ($cx_2 ne "")
{
	$query3 .= "cdonor_no <= $cx_2 AND ";
}

$cs_1=param('cs_1');
$cs_2=param('cs_2');
if ($cs_1 ne "")
{
	$query3 .= "cdonor_s >= $cs_1 AND ";
}
if ($cs_2 ne "")
{
	$query3 .= "cdonor_s <= $cs_2 AND ";
}

$chal_1=param('chal_1');
$chal_2=param('chal_2');
if ($chal_1 ne "")
{
	$query3 .= "cdonor_hal >= $chal_1 AND ";
}
if ($chal_2 ne "")
{
	$query3 .= "cdonor_hal <= $chal_2 AND ";
}

$d_c_1=param('d_c_1');
$d_c_2=param('d_c_2');
if ($d_c_1 ne "")
{
	$query3 .= "cdonor >= $d_c_1 AND ";
}
if ($d_c_2 ne "")
{
	$query3 .= "cdonor <= $d_c_2 AND ";
}

$sp_1=param('sp_1');
$sp_2=param('sp_2');
if ($sp_1 ne "")
{
	$query3 .= "sdonor_pi >= $sp_1 AND ";
}
if ($sp_2 ne "")
{
	$query3 .= "sdonor_pi <= $sp_2 AND ";
}

$sx_1=param('sx_1');
$sx_2=param('sx_2');
if ($sx_1 ne "")
{
	$query3 .= "sdonor_no >= $sx_1 AND ";
}
if ($sx_2 ne "")
{
	$query3 .= "sdonor_no <= $sx_2 AND ";
}

$ss_1=param('ss_1');
$ss_2=param('ss_2');
if ($ss_1 ne "")
{
	$query3 .= "sdonor_s >= $ss_1 AND ";
}
if ($ss_2 ne "")
{
	$query3 .= "sdonor_s <= $ss_2 AND ";
}

$shal_1=param('shal_1');
$shal_2=param('shal_2');
if ($shal_1 ne "")
{
	$query3 .= "sdonor_hal >= $shal_1 AND ";
}
if ($shal_2 ne "")
{
	$query3 .= "sdonor_hal <= $shal_2 AND ";
}


$d_s_1=param('d_s_1');
$d_s_2=param('d_s_2');
if ($d_s_1 ne "")
{
	$query3 .= "sdonor >= $d_s_1 AND ";
}
if ($d_s_2 ne "")
{
	$query3 .= "sdonor <= $d_s_2 AND ";
}

$xs_1=param('xs_1');
$xs_2=param('xs_2');
if ($xs_1 ne "")
{
	$query3 .= "sacceptor_no >= $xs_1 AND ";
}
if ($xs_2 ne "")
{
	$query3 .= "sacceptor_no <= $xs_2 AND ";
}

$a_s_1=param('a_s_1');
$a_s_2=param('a_s_2');
if ($a_s_1 ne "")
{
	$query3 .= "sacceptor >= $a_s_1 AND ";
}
if ($a_s_2 ne "")
{
	$query3 .= "sacceptor <= $a_s_2 AND ";
}

$xhal_1=param('xhal_1');
$xhal_2=param('xhal_2');
if ($xhal_1 ne "")
{
	$query3 .= "halacceptor_no >= $xhal_1 AND ";
}
if ($xhal_2 ne "")
{
	$query3 .= "halacceptor_no <= $xhal_2 AND ";
}

$a_hal_1=param('a_hal_1');
$a_hal_2=param('a_hal_2');
if ($a_hal_1 ne "")
{
	$query3 .= "halacceptor >= $a_hal_1 AND ";
}
if ($a_hal_2 ne "")
{
	$query3 .= "halacceptor <= $a_hal_2 AND ";
}

$rbscore_1=param('rbscore_1');
$rbscore_2=param('rbscore_2');
if ($rbscore_1 ne "")
{
	$query3 .= "RBscore >= $rbscore_1 AND ";
}
if ($rbscore_2 ne "")
{
	$query3 .= "RBscore <= $rbscore_2 AND "; 
}

$ahpdi_1=param('ahpdi_1');
$ahpdi_2=param('ahpdi_2');
if ($ahpdi_1 ne "")
{
	$query3 .= "AHPDI >= $ahpdi_1 AND ";
}
if ($ahpdi_2 ne "")
{
	$query3 .= "AHPDI <= $ahpdi_2 AND ";
}

$contact_1=param('contact_1');
$contact_2=param('contact_2');
if ($contact_1 ne "")
{
	$query3 .= "Contact >= $contact_1 AND ";
}
if ($contact_2 ne "")
{
	$query3 .= "Contact <= $contact_2 AND ";
}

$unsatpo_1=param('unsatpo_1');
$unsatpo_2=param('unsatpo_2');
if ($unsatpo_1 ne "")
{
	$query3 .= "UnsatPo >= $unsatpo_1 AND ";
}
if ($unsatpo_2 ne "")
{
	$query3 .= "UnsatPo <= $unsatpo_2 AND ";
}

$unsatch_1=param('unsatch_1');
$unsatch_2=param('unsatch_2');
if ($unsatch_1 ne "")
{
	$query3 .= "UnsatCh >= $unsatch_1 AND ";
}
if ($unsatch_2 ne "")
{
	$query3 .= "UnsatCh <= $unsatch_2 AND ";
}

$burcp_1=param('burcp_1');
$burcp_2=param('burcp_2');
if ($burcp_1 ne "")
{
	$query3 .= "BurCP >= $burcp_1 AND ";
}
if ($burcp_2 ne "")
{
	$query3 .= "BurCP <= $burcp_2 AND ";
}

#Binding Site Conformational Change Information (Rmsd)
$allatom_1=param('allatom_1');
$allatom_2=param('allatom_2');
if ($allatom_1 ne "")
{
	$query1 .= "POCKET_ALL_RMSD >= $allatom_1 AND ";
}
if ($allatom_2 ne "")
{
	$query1 .= "POCKET_ALL_RMSD <= $allatom_2 AND ";
}

$backbone_1=param('backbone_1');
$backbone_2=param('backbone_2');
if ($backbone_1 ne "")
{
	$query1 .= "POCKET_BONE_RMSD >= $backbone_1 AND ";
}
if ($backbone_2 ne "")
{
	$query1 .= "POCKET_BONE_RMSD <= $backbone_2 AND ";
}

$sidechain_1=param('sidechain_1');
$sidechain_2=param('sidechain_2');
if ($sidechain_1 ne "")
{
	$query1 .= "POCKET_SIDE_RMSD >= $sidechain_1 AND ";
}
if ($sidechain_2 ne "")
{
	$query1 .= "POCKET_SIDE_RMSD <= $sidechain_2 AND ";
}

$res_allatom_1=param('res_allatom_1');
$res_allatom_2=param('res_allatom_2');
if ($res_allatom_1 ne "")
{
	$query1 .= "RESIDUE_ALL_RMSD >= $res_allatom_1 AND ";
}
if ($res_allatom_2 ne "")
{
	$query1 .= "RESIDUE_ALL_RMSD <= $res_allatom_2 AND ";
}

$res_backbone_1=param('res_backbone_1');
$res_backbone_2=param('res_backbone_2');
if ($res_backbone_1 ne "")
{
	$query1 .= "RESIDUE_BONE_RMSD >= $res_backbone_1 AND ";
}
if ($res_backbone_2 ne "")
{
	$query1 .= "RESIDUE_BONE_RMSD <= $res_backbone_2 AND ";
}

$res_sidechain_1=param('res_sidechain_1');
$res_sidechain_2=param('res_sidechain_2');
if ($res_sidechain_1 ne "")
{
	$query1 .= "RESIDUE_SIDE_RMSD >= $res_sidechain_1 AND ";
}
if ($res_sidechain_2 ne "")
{
	$query1 .= "RESIDUE_SIDE_RMSD <= $res_sidechain_2 AND ";
}

#Binding Site Secondary Structure Conformational Change Information (Rmsd)
$site_helix_allatom_1=param('site_helix_allatom_1');
$site_helix_allatom_2=param('site_helix_allatom_2');
if ($site_helix_allatom_1 ne "")
{
	$query5_h .= "SEC_STR_ALL_RMSD >= $site_helix_allatom_1 AND ";
}
if ($site_helix_allatom_2 ne "")
{
	$query5_h .= "SEC_STR_ALL_RMSD <= $site_helix_allatom_2 AND ";
}

$site_helix_backbone_1=param('site_helix_backbone_1');
$site_helix_backbone_2=param('site_helix_backbone_2');
if ($site_helix_backbone_1 ne "")
{
	$query5_h .= "SEC_STR_BONE_RMSD >= $site_helix_backbone_1 AND ";
}
if ($site_helix_backbone_2 ne "")
{
	$query5_h .= "SEC_STR_BONE_RMSD <= $site_helix_backbone_2 AND ";
}

$site_helix_sidechain_1=param('site_helix_sidechain_1');
$site_helix_sidechain_2=param('site_helix_sidechain_2');
if ($site_helix_sidechain_1 ne "")
{
	$query5_h .= "SEC_STR_SIDE_RMSD >= $site_helix_sidechain_1 AND "
}
if ($site_helix_sidechain_2 ne "")
{
	$query5_h .= "SEC_STR_SIDE_RMSD <= $site_helix_sidechain_2 AND ";
}

$site_sheet_allatom_1=param('site_sheet_allatom_1');
$site_sheet_allatom_2=param('site_sheet_allatom_2');
if ($site_sheet_allatom_1 ne "")
{
	$query5_e .= "SEC_STR_ALL_RMSD >= $site_sheet_allatom_1 AND ";
}
if ($site_sheet_allatom_2 ne "")
{
	$query5_e .= "SEC_STR_ALL_RMSD <= $site_sheet_allatom_2 AND ";
}

$site_sheet_backbone_1=param('site_sheet_backbone_1');
$site_sheet_backbone_2=param('site_sheet_backbone_2');
if ($site_sheet_backbone_1 ne "")
{
	$query5_e .= "SEC_STR_BONE_RMSD >= $site_sheet_backbone_1 AND ";
}
if ($site_sheet_backbone_2 ne "")
{
	$query5_e .= "SEC_STR_BONE_RMSD <= $site_sheet_backbone_2 AND ";
}

$site_sheet_sidechain_1=param('site_sheet_sidechain_1');
$site_sheet_sidechain_2=param('site_sheet_sidechain_2');
if ($site_sheet_sidechain_1 ne "")
{
	$query5_e .= "SEC_STR_SIDE_RMSD >= $site_sheet_sidechain_1 AND ";
}
if ($site_sheet_sidechain_2 ne "")
{
	$query5_e .= "SEC_STR_SIDE_RMSD <= $site_sheet_sidechain_2 AND ";
}

$site_coil_allatom_1=param('site_coil_allatom_1');
$site_coil_allatom_2=param('site_coil_allatom_2');
if ($site_coil_allatom_1 ne "")
{
	$query5_c .= "SEC_STR_ALL_RMSD >= $site_coil_allatom_1 AND ";
}
if ($site_coil_allatom_2 ne "")
{
	$query5_c .= "SEC_STR_ALL_RMSD <= $site_coil_allatom_2 AND ";
}

$site_coil_backbone_1=param('site_coil_backbone_1');
$site_coil_backbone_2=param('site_coil_backbone_2');
if ($site_coil_backbone_1 ne "")
{
	$query5_c .= "SEC_STR_BONE_RMSD >= $site_coil_backbone_1 AND ";
}
if ($site_coil_backbone_2 ne "")
{
	$query5_c .= "SEC_STR_BONE_RMSD <= $site_coil_backbone_2 AND ";
}

$site_coil_sidechain_1=param('site_coil_sidechain_1');
$site_coil_sidechain_2=param('site_coil_sidechain_2');
if ($site_coil_sidechain_1 ne "")
{
	$query5_c .= "SEC_STR_SIDE_RMSD >= $site_coil_sidechain_1 AND ";
}
if ($site_coil_sidechain_2 ne "")
{
	$query5_c .= "SEC_STR_SIDE_RMSD <= $site_coil_sidechain_2 AND ";
}

#Entire Protein Secondary Structure Conformational Change Information (RMSD)
$helix_allatom_1=param('helix_allatom_1');
$helix_allatom_2=param('helix_allatom_2');
if ($helix_allatom_1 ne "")
{
	$query2_h .= "SEC_STR_ALL_RMSD >= $helix_allatom_1 AND ";
}
if ($helix_allatom_2 ne "")
{
	$query2_h .= "SEC_STR_BONE_RMSD <= $helix_allatom_2 AND ";
}

$helix_backbone_1=param('helix_backbone_1');
$helix_backbone_2=param('helix_backbone_2');
if ($helix_backbone_1 ne "")
{
	$query2_h .= "SEC_STR_BONE_RMSD >= $helix_backbone_1 AND ";
}
if ($helix_backbone_2 ne "")
{
	$query2_h .= "SEC_STR_BONE_RMSD <= $helix_backbone_2 AND ";
}

$helix_sidechain_1=param('helix_sidechain_1');
$helix_sidechain_2=param('helix_sidechain_2');
if ($helix_sidechain_1 ne "")
{
	$query2_h .= "SEC_STR_SIDE_RMSD >= $helix_sidechain_1 AND ";
}
if ($helix_sidechain_2 ne "")
{
	$query2_h .= "SEC_STR_SIDE_RMSD <= $helix_sidechain_2 AND ";
}

$sheet_allatom_1=param('sheet_allatom_1');
$sheet_allatom_2=param('sheet_allatom_2');
if ($sheet_allatom_1 ne "")
{
	$query2_e .= "SEC_STR_ALL_RMSD >= $sheet_allatom_1 AND ";
}
if ($sheet_allatom_2 ne "")
{
	$query2_e .= "SEC_STR_ALL_RMSD <= $sheet_allatom_2 AND ";
}

$sheet_backbone_1=param('sheet_backbone_1');
$sheet_backbone_2=param('sheet_backbone_2');
if ($sheet_backbone_1 ne "")
{
	$query2_e .= "SEC_STR_BONE_RMSD >= $sheet_backbone_1 AND ";
}
if ($sheet_backbone_2 ne "")
{
	$query2_e .= "SEC_STR_BONE_RMSD <= $sheet_backbone_2 AND ";
}

$sheet_sidechain_1=param('sheet_sidechain_1');
$sheet_sidechain_2=param('sheet_sidechain_2');
if ($sheet_sidechain_1 ne "")
{
	$query2_e .= "SEC_STR_SIDE_RMSD >= $sheet_sidechain_1 AND ";
}
if ($sheet_sidechain_2 ne "")
{
	$query2_e .= "SEC_STR_SIDE_RMSD <= $sheet_sidechain_2 AND ";
}

$coil_allatom_1=param('coil_allatom_1');
$coil_allatom_2=param('coil_allatom_2');
if ($coil_allatom_1 ne "")
{
	$query2_c .= "SEC_STR_ALL_RMSD >= $coil_allatom_1 AND ";
}
if ($coil_allatom_2 ne "")
{
	$query2_c .= "SEC_STR_ALL_RMSD <= $coil_allatom_2 AND ";
}

$coil_backbone_1=param('coil_backbone_1');
$coil_backbone_2=param('coil_backbone_2');
if ($coil_backbone_1 ne "")
{
	$query2_c .= "SEC_STR_BONE_RMSD >= $coil_backbone_1 AND ";
}
if ($coil_backbone_2 ne "")
{
	$query2_c .= "SEC_STR_BONE_RMSD <= $coil_backbone_2 AND ";
}

$coil_sidechain_1=param('coil_sidechain_1');
$coil_sidechain_2=param('coil_sidechain_2');
if ($coil_sidechain_1 ne "")
{
	$query2_c .= "SEC_STR_SIDE_RMSD >= $coil_sidechain_1 AND ";
}
if ($coil_sidechain_2 ne "")
{
	$query2_c .= "SEC_STR_SIDE_RMSD <= $coil_sidechain_2 AND ";
}

#Do database searching
@q1_pdbid=();
if ($query1 ne "")
{
	$query1=~s/AND $//;
	$sth1 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE $query1");
	$sth1 -> execute();
	while(my $data1 = $sth1 -> fetchrow_hashref)
	{
		push @q1_pdbid, "$data1->{CLUSTER}=$data1->{SUBSET}=$data1->{PDBID}=$data1->{CHAIN}=$data1->{CHAINB}=$data1->{LIGAND_SPEC}=$data1->{LIGAND_NAME}";
	}
	$sth1 -> finish();
}

@q2_pdbid_h=();
if ($query2_h ne "")
{
	undef $sth2;
	undef $sth22;
	$query2_h=~s/AND $//;
	$sth2 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB FROM all_2ndstr WHERE SEC_STR_TYPE = 'H' AND $query2_h");
	$sth2 -> execute();
	while(my $data2 = $sth2 -> fetchrow_hashref)
	{
		if (defined($data2->{CHAINB}))
		{
			$sth22 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=?");	
			$sth22 -> execute($data2->{CLUSTER}, $data2->{SUBSET}, $data2->{PDBID}, $data2->{CHAIN}, $data2->{CHAINB});
		}
		else
		{
			$sth22 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL");	
			$sth22 -> execute($data2->{CLUSTER}, $data2->{SUBSET}, $data2->{PDBID}, $data2->{CHAIN});
		}
		while(my $data22 = $sth22 -> fetchrow_hashref)
		{
			push @q2_pdbid_h, "$data22->{CLUSTER}=$data22->{SUBSET}=$data22->{PDBID}=$data22->{CHAIN}=$data22->{CHAINB}=$data22->{LIGAND_SPEC}=$data22->{LIGAND_NAME}";
		}
	}
	$sth2 -> finish();
	if (defined($sth22))
	{
		$sth22 -> finish();
	}
}

@q2_pdbid_e=();
if ($query2_e ne "")
{
	undef $sth2;
	undef $sth22;
	$query2_e=~s/AND $//;
	$sth2 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB FROM all_2ndstr WHERE SEC_STR_TYPE = 'E' AND $query2_e");
	$sth2 -> execute();
	while(my $data2 = $sth2 -> fetchrow_hashref)
	{
		if (defined($data2->{CHAINB}))
		{
			$sth22 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=?");	
			$sth22 -> execute($data2->{CLUSTER}, $data2->{SUBSET}, $data2->{PDBID}, $data2->{CHAIN}, $data2->{CHAINB});
		}
		else
		{
			$sth22 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL");	
			$sth22 -> execute($data2->{CLUSTER}, $data2->{SUBSET}, $data2->{PDBID}, $data2->{CHAIN});
		}
		while(my $data22 = $sth22 -> fetchrow_hashref)
		{
			push @q2_pdbid_e, "$data22->{CLUSTER}=$data22->{SUBSET}=$data22->{PDBID}=$data22->{CHAIN}=$data22->{CHAINB}=$data22->{LIGAND_SPEC}=$data22->{LIGAND_NAME}";
		}
	}
	$sth2 -> finish();
	if (defined($sth22))
	{
		$sth22 -> finish();
	}
}

@q2_pdbid_c=();
if ($query2_c ne "")
{
	undef $sth2;
	undef $sth22;
	$query2_c=~s/AND $//;
	$sth2 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB FROM all_2ndstr WHERE SEC_STR_TYPE = 'C' AND $query2_c");
	$sth2 -> execute();
	while(my $data2 = $sth2 -> fetchrow_hashref)
	{
		if (defined($data2->{CHAINB}))
		{
			$sth22 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=?");	
			$sth22 -> execute($data2->{CLUSTER}, $data2->{SUBSET}, $data2->{PDBID}, $data2->{CHAIN}, $data2->{CHAINB});
		}
		else
		{
			$sth22 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL");	
			$sth22 -> execute($data2->{CLUSTER}, $data2->{SUBSET}, $data2->{PDBID}, $data2->{CHAIN});
		}
		while(my $data22 = $sth22 -> fetchrow_hashref)
		{
			push @q2_pdbid_c, "$data22->{CLUSTER}=$data22->{SUBSET}=$data22->{PDBID}=$data22->{CHAIN}=$data22->{CHAINB}=$data22->{LIGAND_SPEC}=$data22->{LIGAND_NAME}";
		}
	}
	$sth2 -> finish();
	if (defined($sth22))
	{
		$sth22 -> finish();
	}
}

@q5_pdbid_h=();
if ($query5_h ne "")
{
	undef $sth5;
	undef $sth55;
	$query5_h=~s/AND $//;
	$sth5 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB FROM all_2ndstr WHERE SITE_RELATE = 'Y' AND SEC_STR_TYPE = 'H' AND $query5_h");
	$sth5 -> execute();
	while(my $data5 = $sth5 -> fetchrow_hashref)
	{
		if (defined($data5->{CHAINB}))
		{
			$sth55 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=?");
			$sth55 -> execute($data5->{CLUSTER}, $data5->{SUBSET}, $data5->{PDBID}, $data5->{CHAIN}, $data5->{CHAINB});
		}
		else
		{
			$sth55 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL");
			$sth55 -> execute($data5->{CLUSTER}, $data5->{SUBSET}, $data5->{PDBID}, $data5->{CHAIN});
		}
		while (my $data55 = $sth55 -> fetchrow_hashref)
		{
			push @q5_pdbid_h, "$data55->{CLUSTER}=$data55->{SUBSET}=$data55->{PDBID}=$data55->{CHAIN}=$data55->{CHAINB}=$data55->{LIGAND_SPEC}=$data55->{LIGAND_NAME}";
		}
	}
	$sth5 -> finish();
	if (defined($sth55))
	{
		$sth55 -> finish();
	}
}

@q5_pdbid_e=();
if ($query5_e ne "")
{
	undef $sth5;
	undef $sth55;
	$query5_e=~s/AND $//;
	$sth5 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB FROM all_2ndstr WHERE SITE_RELATE = 'Y' AND SEC_STR_TYPE = 'E' AND $query5_e");
	$sth5 -> execute();
	while(my $data5 = $sth5 -> fetchrow_hashref)
	{
		if (defined($data5->{CHAINB}))
		{
			$sth55 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=?");
			$sth55 -> execute($data5->{CLUSTER}, $data5->{SUBSET}, $data5->{PDBID}, $data5->{CHAIN}, $data5->{CHAINB});
		}
		else
		{
			$sth55 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL");
			$sth55 -> execute($data5->{CLUSTER}, $data5->{SUBSET}, $data5->{PDBID}, $data5->{CHAIN});
		}
		while (my $data55 = $sth55 -> fetchrow_hashref)
		{
			push @q5_pdbid_e, "$data55->{CLUSTER}=$data55->{SUBSET}=$data55->{PDBID}=$data55->{CHAIN}=$data55->{CHAINB}=$data55->{LIGAND_SPEC}=$data55->{LIGAND_NAME}";
		}
	}
	$sth5 -> finish();
	if (defined($sth55))
	{
		$sth55 -> finish();
	}
}

@q5_pdbid_c=();
if ($query5_c ne "")
{
	undef $sth5;
	undef $sth55;
	$query5_c=~s/AND $//;
	$sth5 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB FROM all_2ndstr WHERE SITE_RELATE = 'Y' AND SEC_STR_TYPE = 'C' AND $query5_c");
	$sth5 -> execute();
	while(my $data5 = $sth5 -> fetchrow_hashref)
	{
		if (defined($data5->{CHAINB}))
		{
			$sth55 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB=?");
			$sth55 -> execute($data5->{CLUSTER}, $data5->{SUBSET}, $data5->{PDBID}, $data5->{CHAIN}, $data5->{CHAINB});
		}
		else
		{
			$sth55 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE CLUSTER=? AND SUBSET=? AND PDBID=? AND CHAIN=? AND CHAINB IS NULL");
			$sth55 -> execute($data5->{CLUSTER}, $data5->{SUBSET}, $data5->{PDBID}, $data5->{CHAIN});
		}
		while (my $data55 = $sth55 -> fetchrow_hashref)
		{
			push @q5_pdbid_c, "$data55->{CLUSTER}=$data55->{SUBSET}=$data55->{PDBID}=$data55->{CHAIN}=$data55->{CHAINB}=$data55->{LIGAND_SPEC}=$data55->{LIGAND_NAME}";
		}
	}
	$sth5 -> finish();
	if (defined($sth55))
	{
		$sth55 -> finish();
	}
}

@q3_pdbid=();
if ($query3 ne "")
{
	undef $sth3;
	undef $sth33;
	$query3=~s/AND $//;
	$sth3 = $dbh1 -> prepare ("SELECT DISTINCT PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM interaction WHERE $query3");
	$sth3 -> execute();
	while(my $data3 = $sth3 -> fetchrow_hashref)
	{
		if (defined($data3->{CHAINB}))
		{
			$sth33 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE PDBID=? AND CHAIN=? AND CHAINB=? AND LIGAND_SPEC=? AND LIGAND_NAME=?");
			$sth33 -> execute($data3->{PDBID}, $data3->{CHAIN}, $data3->{CHAINB}, $data3->{LIGAND_SPEC}, $data3->{LIGAND_NAME});
		}
		else
		{
			$sth33 = $dbh1 -> prepare ("SELECT DISTINCT CLUSTER, SUBSET, PDBID, CHAIN, CHAINB, LIGAND_SPEC, LIGAND_NAME FROM all_site WHERE PDBID=? AND CHAIN=? AND CHAINB IS NULL AND LIGAND_SPEC=? AND LIGAND_NAME=?");
			$sth33 -> execute($data3->{PDBID}, $data3->{CHAIN}, $data3->{LIGAND_SPEC}, $data3->{LIGAND_NAME});
		}
		while (my $data33 = $sth33 -> fetchrow_hashref)
		{
			push @q3_pdbid, "$data33->{CLUSTER}=$data33->{SUBSET}=$data33->{PDBID}=$data33->{CHAIN}=$data33->{CHAINB}=$data33->{LIGAND_SPEC}=$data33->{LIGAND_NAME}";
		}
	}
	$sth3 -> finish();
	if (defined($sth33))
	{
		$sth33 -> finish();
	}
}

$number=8;  #the selected pdbid should appear two times in @total_pdbid.
if ($query1 eq "")  #if customer did not fill the query1, then the selected pdbid should appear ($number - 1) times in @total_pdbid.
{
	$number --;
}
if ($query2_h eq "")
{
	$number --;
}
if ($query2_e eq "")
{
	$number --;
}
if ($query2_c eq "")
{
	$number --;
}
if ($query3 eq "")
{
	$number --;
}
if ($query5_h eq "")
{
	$number --;
}
if ($query5_e eq "")
{
	$number --;
}
if ($query5_c eq "")
{
	$number --;
}

@total_pdbid=();
push @total_pdbid, @q1_pdbid;
push @total_pdbid, @q2_pdbid_h;
push @total_pdbid, @q2_pdbid_e;
push @total_pdbid, @q2_pdbid_c;
push @total_pdbid, @q3_pdbid;
push @total_pdbid, @q5_pdbid_h;
push @total_pdbid, @q5_pdbid_e;
push @total_pdbid, @q5_pdbid_c;

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
if (@total_pdbid)
{
	for my $pdbid_line (@total_pdbid)
	{
		if ($count{$pdbid_line} == $number)
		{
			$order++;
			$chain="";
			@lig=();
			@item=split /=/,$pdbid_line;
			$pdbid=$item[2];
			if (defined($item[4]) and $item[4] ne "")
			{
				$chain="$item[3]_$item[4]";
			}
			else
			{
				$chain=$item[3];
			}

			if (defined($item[6]))
			{
				$ligname_line=$item[6];
				@lig=split /~/,$ligname_line;
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
				<input type="text" name="ligid" value="$ligname" >&nbsp;&nbsp;&nbsp;<input type="submit" name="search_id$order" value="protein" ></p>
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
}
else
{
	print qq(<p class="STYLE9">No structure in Flex-Site DB matchs</p>);
}
	
if ($query1 ne "" or $query2_h ne "" or $query2_e ne "" or $query2_c ne "" or $query3 ne "" or $query5_h ne "" or $query5_e ne "" or $query5_c ne "")
{
	$dbh1 -> disconnect || warn("Disconnection failed: $DBI::errstr\n");
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
