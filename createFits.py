############################################
# Program to create fits table for WEAVE purposes.
# Optimized for SCIP columns
# Authors: S.R. Berlanas & M. Monguio 
# Version v10 01-2025
########################################

# Instructions:
# Fill the columns using your own data as describred below. 
# Run the code as 
# python createFits.py

import numpy as np
from astropy.io import fits
import os
import datetime
import createCols as cC  # Make sure you are using the correct createCols file for your targets






if __name__ == '__main__':

#General characteristics. Modify according to you needs:

 targsrvy=['']  # Name of your survey or program

 res=['']        #Choose one between: LowRes: ['LR'] or HighRes ['HR']
		   #If you have both LR and HR targets, provide two fits files.

 targuse=['']      # Always ['T'] except for sky that should be ['S']

 targclass=['']  # Choose the target class of your sources 




# Below you need to include the information for each target. The information must be filled in columns.
# Create a vector for each of the columns. The length of the vector will be the number of stars in your table.
# NOTE THAT THE VALUES OF THE VECTORS HERE ARE JUST EXAMPLES!.
# NOTE THAT THE CODE IS OPTIMIZED FOR SCIP COLUMS. 
# You can load your data from an ascii file using, e.g.: 
# yourdata = np.loadtxt('yourfilename.dat', delimiter=" ", skiprows=1)
# You can load your data from a fits file using:
# yourdata=fits.getdata('yourfilename.fits',1)

 data=fits.getdata('data.fits',1)
 targid=data['TARGID'] #Mandatory: ID for each star. Make sure you do not repeat any id.
 LEN=len(targid)   #Do not modify this line
 Vnan=LEN*[np.nan] #Do not modify this line


 targprio=data['TARGPRIO']	  # Mandatory: If you have internal priorities between you targets.
                          # Must be integers from 1.0 (lowest priority) to 10.0 (highest priority)


 magg=data['MAG_G']            # Mandatory. g magnitude of the star in AB system. Must be the same as IGAPS_MAG_G or VPHAS_MAG_G (SCIP)
 emagg=data['MAG_G_ERR']              # Modify only of you know the error in g magnitude of the star
 magr=data['MAG_R'] 	          # Mandatory. r magnitude of the star in AB system.  Must be the same as IGAPS_MAG_R_I/U or VPHAS_MAG_R (SCIP)
 emagr=data['MAG_R_ERR']	          # Modify only of you know the error in r magnitude of the star
 magi=data['MAG_I']   	  # Mandatory. Magnitude in i of the star in AB system.  Must be the same as IGAPS_MAG_I or VPHAS_MAG_I (SCIP)
 emagi=data['MAG_I_ERR']             # Modify only of you know the error in i magnitude of the star
 
 gaiagmag=data['GAIA_MAG_G']           # Modify only of you know the gaia g magnitude of the star
 gaiabp=data['GAIA_MAG_BP']              # Modify only of you know the gaia BP colour of the star
 gaiarp=data['GAIA_MAG_RP']              # Modify only of you know the gaia RP column of the star 
 egaiagmag=data['GAIA_MAG_G_ERR']           # Modify only of you know the error in gaia g magnitude of the star
 egaiabp=data['GAIA_MAG_BP_ERR']              # Modify only of you know the error in the gaia BP colour of the star
 egaiarp= data['GAIA_MAG_RP_ERR']            # Modify only of you know the error in the gaia RP column of the star



#Gaia astrometry 

 GAIA_ID=data['GAIA_ID'] #Sequences of 19 digits
 GAIA_DR=[3]*LEN 	# Must be 3 for eDR3/DR3 
 GAIA_RA=data['GAIA_RA']		#Mandatory. Important since they are the
			# coordinates used for allocating the fibres.
 GAIA_DEC=data['GAIA_DEC']		#Mandatory. Important since they are the
			# coordinates used for allocating the fibres.
 GAIA_EPOCH=[2016.0]*LEN # Must be 2016.0 for eDR3/DR3 
 GAIA_PMRA=data['GAIA_PMRA']
 GAIA_PMRA_ERR=data['GAIA_PMRA_ERR']
 GAIA_PMDEC=data['GAIA_PMDEC']
 GAIA_PMDEC_ERR=data['GAIA_PMDEC_ERR']
 GAIA_PARAL=data['GAIA_PARAL']
 GAIA_PARAL_ERR=data['GAIA_PARAL_ERR']
 GAIA_GAL_LAT=data['GAIA_GAL_LAT']		#Mandatory. They are used to assign the SCIP target names.
 GAIA_GAL_LONG=data['GAIA_GAL_LONG']		#Mandatory. They are used to assign the SCIP target names.



#IGAPS photometry (ignore this section if you do not have igaps photometry)
#If you know it, change the Vnan for the vector with the values:

 IGAPS_ID=data['IGAPS_ID']    #'name' column from IGAPS catalogue
 IGAPS_DR=data['IGAPS_DR']      #or =LEN*[1] if you are using it
 IGAPS_MAG_G=data['IGAPS_MAG_G']	#in the AB system, i.e. gAB from IGAPS catalogue
 IGAPS_MAG_G_ERR=data['IGAPS_MAG_G_ERR']
 IGAPS_MAG_HA=data['IGAPS_MAG_HA']	#in the AB system, i.e. haAB from IGAPS catalogue
 IGAPS_MAG_HA_ERR=data['IGAPS_MAG_HA_ERR']
 IGAPS_MAG_I=data['IGAPS_MAG_I']	#in the AB system, i.e. iAB from IGAPS catalogue
 IGAPS_MAG_I_ERR=data['IGAPS_MAG_I_ERR']
 IGAPS_MAG_R_I=data['IGAPS_MAG_R_I']	#in the AB system, i.e. rAB_I from IGAPS catalogue
 IGAPS_MAG_R_I_ERR=data['IGAPS_MAG_R_I_ERR']
 IGAPS_MAG_R_U=data['IGAPS_MAG_R_U']	#in the AB system, i.e. rAB_U from IGAPS catalogue
 IGAPS_MAG_R_U_ERR=data['IGAPS_MAG_R_U_ERR']
 IGAPS_MAG_U=data['IGAPS_MAG_U']	#U_RGO from IGAPS catalogue
 IGAPS_MAG_U_ERR=data['IGAPS_MAG_U_ERR']


#OPT photometry (ONLY FOR IFU-LR)

 OPTCAT=LEN*['']        #Source of the UBVRIugirzy (OPT) observations
 OPTCAT_DR=LEN*['']     #Data release of OPTCAT_ID
 OPTCAT_ID=LEN*['']     #Target identifier associated with OPTCAT
 OPTCAT_MAG_G=Vnan      #Magnitude in the g band for OPTCAT_ID 
 OPTCAT_MAG_G_ERR=Vnan  #Error on OPTCAT_MAG_G 
 OPTCAT_MAG_I=Vnan      #Magnitude in the I or i band for OPTCAT_ID 
 OPTCAT_MAG_I_ERR=Vnan  #Error on OPTCAT_MAG_I 
 OPTCAT_MAG_R=Vnan      #Magnitude in the R or r band for OPTCAT_ID 
 OPTCAT_MAG_R_ERR=Vnan  #Error on OPTCAT_MAG_R 



#VPHAS photometry (ignore this section if you do not have vphas photometry)
#If you know it, change the Vnan for the vector with the values:

 VPHAS_ID=LEN*['']  #'VPHASDR2' column from VPHAS DR2 catalogue
 VPHAS_DR=LEN*['']  #or =LEN*[2] if you are using it
 VPHAS_MAG_G=Vnan	#in the AB system
 VPHAS_MAG_G_ERR=Vnan
 VPHAS_MAG_HA=Vnan	#in the AB system
 VPHAS_MAG_HA_ERR=Vnan
 VPHAS_MAG_I=Vnan	#in the AB system
 VPHAS_MAG_I_ERR=Vnan
 VPHAS_MAG_R=Vnan	#in the AB system
 VPHAS_MAG_R_ERR=Vnan
 VPHAS_MAG_R2=Vnan	#in the AB system
 VPHAS_MAG_R2_ERR=Vnan
 VPHAS_MAG_U=Vnan	#in the AB system
 VPHAS_MAG_U_ERR=Vnan


###########################################
# YOU DON NOT NEED TO MODIFY ANYTHING ELSE!
###########################################

#apsflag is a bitmask that will be used to specify what CDP/CS will be used.



 for i in targclass:
     if i =='NEBULA':
        apsflag=['1000000000001000000010000000']*LEN
     elif i =='SKY':
        apsflag=['1000100000001000000010000000']*LEN
     elif i =='STAR':
        apsflag=['1000111000001000000000000100']*LEN
     elif i =='STAR_CEP':
        apsflag=['1000111000001000000001000100']*LEN
     elif i =='STAR_EM':
        apsflag=['1000100000001000000000000000']*LEN
     elif i =='STAR_IB':
        apsflag=['1000000000001000000000000000']*LEN
     elif i =='STAR_MLUM':
        apsflag=['1000110000001000000000000100']*LEN
     elif i =='STAR_OB':
        apsflag=['1000111000001000000000000000']*LEN
     elif i =='STAR_BA':
        apsflag=['1000111000001000000000001000']*LEN
     elif i =='STAR_WD':
        apsflag=['1000001000001000000000000000']*LEN
     elif i =='STAR_YSO':
        apsflag=['1000111000001000000000100000']*LEN
     elif i =='STAR_VAR':
        apsflag=['1000111000001000000000000000']*LEN




#SCIP target name:
 targname=LEN*['']
 for i in range(LEN):
     targname[i]='SCIP_{:08.4f}{:+08.4f}'.format(GAIA_GAL_LONG[i],GAIA_GAL_LAT[i])


#Observing mode and observing constrains:
 for i in res:
     if i =='HR':
        PROGTEMP=['21331']*LEN
	OBSTEMP=['FBCEE']*LEN
     elif i =='LR':
        PROGTEMP=['11331']*LEN 
	OBSTEMP=['FBCEC']*LEN


# Name of the fits file to be created:
 filename='CATALOGUE.fits'.format(targsrvy[0],targclass[0])

#Call the createCols routine:

 cC.createC(filename,
 targsrvy,
 res,
 targid,
 targname,
 targprio,
 targuse,
 targclass,
 GAIA_ID,
 GAIA_DR,
 GAIA_RA,
 GAIA_DEC,
 GAIA_EPOCH,
 GAIA_PMRA,
 GAIA_PMRA_ERR,
 GAIA_PMDEC,
 GAIA_PMDEC_ERR,
 GAIA_PARAL,
 GAIA_PARAL_ERR,
 magg,
 emagg,
 magr,
 emagr,
 magi,
 emagi,
 gaiagmag,
 gaiabp,
 gaiarp,
 egaiagmag,
 egaiabp,
 egaiarp, 
 apsflag,
 GAIA_GAL_LAT,
 GAIA_GAL_LONG,
 IGAPS_DR,
 IGAPS_ID,
 IGAPS_MAG_G,
 IGAPS_MAG_G_ERR,
 IGAPS_MAG_HA,
 IGAPS_MAG_HA_ERR,
 IGAPS_MAG_I,
 IGAPS_MAG_I_ERR,
 IGAPS_MAG_R_I,
 IGAPS_MAG_R_I_ERR,
 IGAPS_MAG_R_U,
 IGAPS_MAG_R_U_ERR,
 IGAPS_MAG_U, 
 IGAPS_MAG_U_ERR,
 PROGTEMP,
 OBSTEMP,
 VPHAS_DR,
 VPHAS_ID,
 VPHAS_MAG_G,
 VPHAS_MAG_G_ERR,
 VPHAS_MAG_HA,
 VPHAS_MAG_HA_ERR,
 VPHAS_MAG_I,
 VPHAS_MAG_I_ERR,
 VPHAS_MAG_R,
 VPHAS_MAG_R_ERR,
 VPHAS_MAG_R2,
 VPHAS_MAG_R2_ERR,
 VPHAS_MAG_U,
 VPHAS_MAG_U_ERR,
 OPTCAT,
 OPTCAT_DR,
 OPTCAT_ID,
 OPTCAT_MAG_G,
 OPTCAT_MAG_G_ERR,
 OPTCAT_MAG_I,
 OPTCAT_MAG_I_ERR,
 OPTCAT_MAG_R,
 OPTCAT_MAG_R_ERR)







