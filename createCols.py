############################################
# Program to create fits table for WEAVE purposes.
# Optimized for SCIP columns
# Authors:  S.R. Berlanas & M. Monguio 
# Version v10 01-2025
########################################

#DO NOT MODIFY ANYTHING IN THIS FILE
#(Unless you know what you are doing)

import numpy as np
from astropy.io import fits
import os
import datetime



def  createC(filename,targsrvy,res,targid,targname,targprio,targuse,targclass,GAIA_ID,GAIA_DR,GAIA_RA,GAIA_DEC,GAIA_EPOCH,GAIA_PMRA,GAIA_PMRA_ERR,GAIA_PMDEC,GAIA_PMDEC_ERR,GAIA_PARAL,GAIA_PARAL_ERR,magg,emagg,magr,emagr,magi,emagi,gaiagmag, gaiabp,gaiarp,egaiagmag,egaiabp,egaiarp,apsflag, GAIA_GAL_LAT,GAIA_GAL_LONG,IGAPS_DR,IGAPS_ID, IGAPS_MAG_G, IGAPS_MAG_G_ERR, IGAPS_MAG_HA, IGAPS_MAG_HA_ERR, IGAPS_MAG_I, IGAPS_MAG_I_ERR, IGAPS_MAG_R_I, IGAPS_MAG_R_I_ERR, IGAPS_MAG_R_U, IGAPS_MAG_R_U_ERR, IGAPS_MAG_U, IGAPS_MAG_U_ERR, PROGTEMP,OBSTEMP,VPHAS_DR, VPHAS_ID, VPHAS_MAG_G, VPHAS_MAG_G_ERR,VPHAS_MAG_HA,VPHAS_MAG_HA_ERR,VPHAS_MAG_I,VPHAS_MAG_I_ERR, VPHAS_MAG_R, VPHAS_MAG_R_ERR, VPHAS_MAG_R2,VPHAS_MAG_R2_ERR,VPHAS_MAG_U,VPHAS_MAG_U_ERR, OPTCAT, OPTCAT_DR,OPTCAT_ID , OPTCAT_MAG_G, OPTCAT_MAG_G_ERR, OPTCAT_MAG_I, OPTCAT_MAG_I_ERR, OPTCAT_MAG_R,OPTCAT_MAG_R_ERR):

   #First we need to create the arrays that will be used as columns in the table.

   LEN=len(targid) #Length of the table

   #Create a vector of nans for empty columns
   Vnan=LEN*[np.nan]
   V0=LEN*[0]

   #FILL here you columns:
   targcat=LEN*['catname.fits']

   
### COMMON COLUMNS ###

   col1=fits.Column(name='CNAME',unit='none',null='',format='20A',array=[])
   col2=fits.Column(name='TARGSRVY',unit='none',null='',format='15A',array=LEN*targsrvy)
   col3=fits.Column(name='TARGPROG',unit='none',null='',format='40A',array=LEN*targclass) 
   col4=fits.Column(name='TARGCAT',unit='none',null='',format='30A',array=targcat)
   col5=fits.Column(name='TARGID',unit='none',null='',format='30A',array=targid)
   col6=fits.Column(name='TARGNAME',unit='none',null='',format='30A',array=targname) 
   col7=fits.Column(name='TARGPRIO',unit='none',null='',format='E',array=targprio)
   col8=fits.Column(name='TARGUSE',unit='none',null='',format='1A',array=LEN*targuse)
   col9=fits.Column(name='TARGCLASS',unit='none',null='',format='12A',array=LEN*targclass)

# Observing mode and observing constrains:
   col10=fits.Column(name='PROGTEMP',unit='none',null='',format='8A',array=PROGTEMP)
   col11=fits.Column(name='OBSTEMP',unit='none',null='',format='5A',array=OBSTEMP)


# GAIA
   col12=fits.Column(name='GAIA_ID',unit='none',null="",format='25A',array=GAIA_ID)
   col13=fits.Column(name='GAIA_DR',unit='none',null="",format='5A',array=GAIA_DR)
   col14=fits.Column(name='GAIA_RA',unit='deg',null="",format='D',array=GAIA_RA)
   col15=fits.Column(name='GAIA_DEC',unit='deg',null="",format='D',array=GAIA_DEC)
   col16=fits.Column(name='GAIA_EPOCH',unit='yr',null="",format='E',array=GAIA_EPOCH)
   col17=fits.Column(name='GAIA_PMRA',unit='mas/yr',null="",format='E',array=GAIA_PMRA)
   col18=fits.Column(name='GAIA_PMRA_ERR',unit='mas/yr',null="",format='E',array=GAIA_PMRA_ERR) 
   col19=fits.Column(name='GAIA_PMDEC',unit='mas/yr',null="",format='E',array=GAIA_PMDEC)
   col20=fits.Column(name='GAIA_PMDEC_ERR',unit='mas/yr',null="",format='E',array=GAIA_PMDEC_ERR) 
   col21=fits.Column(name='GAIA_PARAL',unit='mas',null="",format='E',array=GAIA_PARAL)
   col22=fits.Column(name='GAIA_PARAL_ERR',unit='mas',null="",format='E',array=GAIA_PARAL_ERR) 


# HEALPIX
   col23=fits.Column(name='HEALPIX',unit='none',null=-1,format='I',array=LEN*[-1]) 

# IFU
   col24=fits.Column(name='IFU_SPAXEL',unit='none',null="",format='6A',array=LEN*[''])
   col25=fits.Column(name='IFU_PA',unit='deg',null="",format='D',array=Vnan)
   col26=fits.Column(name='IFU_DITHER',unit='none',null=0,format='I',array=LEN*[0]) 

# mandatory photometry:
   col27=fits.Column(name='MAG_G',unit='mag',null="",format='E',array=magg)
   col28=fits.Column(name='MAG_G_ERR',unit='mag',null="",format='E',array=emagg)
   col29=fits.Column(name='MAG_R',unit='mag',null="",format='E',array=magr)
   col30=fits.Column(name='MAG_R_ERR',unit='mag',null="",format='E',array=emagr) 
   col31=fits.Column(name='MAG_I',unit='mag',null="",format='E',array=magi)
   col32=fits.Column(name='MAG_I_ERR',unit='mag',null="",format='E',array=emagi)

# GAIA mags
   col33=fits.Column(name='GAIA_MAG_G',unit='mag',null="",format='E',array=gaiagmag) 
   col34=fits.Column(name='GAIA_MAG_G_ERR',unit='mag',null="",format='E',array=egaiagmag) 
   col35=fits.Column(name='GAIA_MAG_BP',unit='mag',null="",format='E',array=gaiabp)
   col36=fits.Column(name='GAIA_MAG_BP_ERR',unit='mag',null="",format='E',array=egaiabp) 
   col37=fits.Column(name='GAIA_MAG_RP',unit='mag',null="",format='E',array=gaiarp)
   col38=fits.Column(name='GAIA_MAG_RP_ERR',unit='mag',null="",format='E',array=egaiarp) 


# SPA COLUMNS- APS

   col39=fits.Column(name='APS_WL_MIN',unit='Angstrom',null='',format='E',array=Vnan)
   col40=fits.Column(name='APS_WL_MAX',unit='Angstrom',null='',format='E',array=Vnan)
   col41=fits.Column(name='APS_Z',unit='none',null='',format='E',array=Vnan) 
   col42=fits.Column(name='APS_SIGMA',unit='km/s',null='',format='E',array=Vnan) 
   col43=fits.Column(name='APS_TEMPL_LIB',unit='none',null='',format='10A',array=LEN*[''])
   col44=fits.Column(name='APS_TEMPL_LIB_NORM',unit='none',null=-1,format='I',array=LEN*[-1])
   col45=fits.Column(name='APS_PPXF_WL_MIN',unit='Angstrom',null='',format='E',array=Vnan)
   col46=fits.Column(name='APS_PPXF_WL_MAX',unit='Angstrom',null='',format='E',array=Vnan)
   col47=fits.Column(name='APS_PPXF_MOM',unit='none',null=-1,format='I',array=LEN*[-1])
   col48=fits.Column(name='APS_PPXF_DEG_ADD',unit='none',null=-1,format='I',array=LEN*[-1])
   col49=fits.Column(name='APS_PPXF_DEG_MULT',unit='none',null=-1,format='I',array=LEN*[-1])
   col50=fits.Column(name='APS_PPXF_NUM_MC',unit='none',null=-1,format='I',array=LEN*[-1])
   col51=fits.Column(name='APS_GAND_MODE',unit='none',null=-1,format='I',array=LEN*[-1])
   col52=fits.Column(name='APS_GAND_ERR',unit='none',null=-1,format='I',array=LEN*[-1])
   col53=fits.Column(name='APS_GAND_RED1',unit='none',null='',format='E',array=Vnan)
   col54=fits.Column(name='APS_GAND_RED2',unit='none',null='',format='E',array=Vnan)   
   col55=fits.Column(name='APS_GAND_EBV',unit='none',null=-1,format='I',array=LEN*[-1])
   col56=fits.Column(name='APS_LS_MODE',unit='none',null=-1,format='I',array=LEN*[-1])
   col57=fits.Column(name='APS_LS_RES',unit='Angstrom',null='',format='E',array=Vnan)
   col58=fits.Column(name='APS_LS_NUM_MC',unit='none',null=-1,format='I',array=LEN*[-1])
   col59=fits.Column(name='APS_SSP_NUM_WLKR',unit='none',null=-1,format='I',array=LEN*[-1])
   col60=fits.Column(name='APS_SSP_NUM_CHAIN',unit='none',null=-1,format='I',array=LEN*[-1])
   col61=fits.Column(name='APS_IFU_MASK',unit='none',null=-1,format='I',array=LEN*[-1])
   col62=fits.Column(name='APS_IFU_TSSL_TYPE',unit='none',null='',format='10A',array=LEN*[''])
   col63=fits.Column(name='APS_IFU_TSSL_TARG_SNR',unit='none',null='',format='E',array=Vnan)
   col64=fits.Column(name='APS_IFU_TSSL_MIN_SNR',unit='none',null='',format='E',array=Vnan)
   col65=fits.Column(name='APS_IFU_TSSL_COVAR',unit='none',null=-1,format='I',array=LEN*[-1])
   col66=fits.Column(name='APS_IFU_SRC_ID',unit='none',null='',format='35A',array=LEN*[''])
   col67=fits.Column(name='APS_IFU_SRC_RA',unit='deg',null='',format='D',array=Vnan)
   col68=fits.Column(name='APS_IFU_SRC_DEC',unit='deg',null='',format='D',array=Vnan)
   col69=fits.Column(name='APS_FLAG',unit='none',null='',format='48A',array=apsflag)



### SCIP COLUMNS ###

   col70=fits.Column(name='GAIA_GAL_LAT',unit='deg',null="",format='D',array=GAIA_GAL_LAT) 
   col71=fits.Column(name='GAIA_GAL_LONG',unit='deg',null="",format='D',array=GAIA_GAL_LONG) 


# IGAPS
   col72=fits.Column(name='IGAPS_DR',unit='none',null="",format='20A',array=IGAPS_DR)
   col73=fits.Column(name='IGAPS_ID',unit='none',null="",format='30A',array=IGAPS_ID)
   col74=fits.Column(name='IGAPS_MAG_G',unit='mag',null="",format='E',array=IGAPS_MAG_G)
   col75=fits.Column(name='IGAPS_MAG_G_ERR',unit='mag',null="",format='E',array=IGAPS_MAG_G_ERR)
   col76=fits.Column(name='IGAPS_MAG_HA',unit='mag',null="",format='E',array=IGAPS_MAG_HA)
   col77=fits.Column(name='IGAPS_MAG_HA_ERR',unit='mag',null="",format='E',array=IGAPS_MAG_HA_ERR)
   col78=fits.Column(name='IGAPS_MAG_I',unit='mag',null="",format='E',array=IGAPS_MAG_I)
   col79=fits.Column(name='IGAPS_MAG_I_ERR',unit='mag',null="",format='E',array=IGAPS_MAG_I_ERR)
   col80=fits.Column(name='IGAPS_MAG_R_I',unit='mag',null="",format='E',array=IGAPS_MAG_R_I)
   col81=fits.Column(name='IGAPS_MAG_R_I_ERR',unit='mag',null="",format='E',array=IGAPS_MAG_R_I_ERR)
   col82=fits.Column(name='IGAPS_MAG_R_U',unit='mag',null="",format='E',array=IGAPS_MAG_R_U)
   col83=fits.Column(name='IGAPS_MAG_R_U_ERR',unit='mag',null="",format='E',array=IGAPS_MAG_R_U_ERR)
   col84=fits.Column(name='IGAPS_MAG_U',unit='mag',null="",format='E',array=IGAPS_MAG_U)
   col85=fits.Column(name='IGAPS_MAG_U_ERR',unit='mag',null="",format='E',array=IGAPS_MAG_U_ERR)


# OPTCAT
   col86=fits.Column(name='OPTCAT',unit='none',null="",format='60A',array=OPTCAT) 
   col87=fits.Column(name='OPTCAT_DR',unit='none',null="",format='50A',array=OPTCAT_DR)
   col88=fits.Column(name='OPTCAT_ID',unit='none',null="",format='30A',array=OPTCAT_ID)
   col89=fits.Column(name='OPTCAT_MAG_G',unit='mag',null="",format='E',array=OPTCAT_MAG_G)
   col90=fits.Column(name='OPTCAT_MAG_G_ERR',unit='mag',null="",format='E',array=OPTCAT_MAG_G_ERR)
   col91=fits.Column(name='OPTCAT_MAG_I',unit='mag',null="",format='E',array=OPTCAT_MAG_I)
   col92=fits.Column(name='OPTCAT_MAG_I_ERR',unit='mag',null="",format='E',array=OPTCAT_MAG_I_ERR)
   col93=fits.Column(name='OPTCAT_MAG_R',unit='mag',null="",format='E',array=OPTCAT_MAG_R)
   col94=fits.Column(name='OPTCAT_MAG_R_ERR',unit='mag',null="",format='E',array=OPTCAT_MAG_R_ERR)


# VPHAS
   col95=fits.Column(name='VPHAS_DR',unit='none',null="",format='20A',array=VPHAS_DR)
   col96=fits.Column(name='VPHAS_ID',unit='none',null="",format='30A',array=VPHAS_ID)
   col97=fits.Column(name='VPHAS_MAG_G',unit='mag',null="",format='E',array=VPHAS_MAG_G) 
   col98=fits.Column(name='VPHAS_MAG_G_ERR',unit='mag',null="",format='E',array=VPHAS_MAG_G_ERR) 
   col99=fits.Column(name='VPHAS_MAG_HA',unit='mag',null="",format='E',array=VPHAS_MAG_HA) 
   col100=fits.Column(name='VPHAS_MAG_HA_ERR',unit='mag',null="",format='E',array=VPHAS_MAG_HA_ERR) 
   col101=fits.Column(name='VPHAS_MAG_I',unit='mag',null="",format='E',array=VPHAS_MAG_I) 
   col102=fits.Column(name='VPHAS_MAG_I_ERR',unit='mag',null="",format='E',array=VPHAS_MAG_I_ERR) 
   col103=fits.Column(name='VPHAS_MAG_R',unit='mag',null="",format='E',array=VPHAS_MAG_R)
   col104=fits.Column(name='VPHAS_MAG_R_ERR',unit='mag',null="",format='E',array=VPHAS_MAG_R_ERR) 
   col105=fits.Column(name='VPHAS_MAG_R2',unit='mag',null="",format='E',array=VPHAS_MAG_R2) 
   col106=fits.Column(name='VPHAS_MAG_R2_ERR',unit='mag',null="",format='E',array=VPHAS_MAG_R2_ERR)
   col107=fits.Column(name='VPHAS_MAG_U',unit='mag',null="",format='E',array=VPHAS_MAG_U) 
   col108=fits.Column(name='VPHAS_MAG_U_ERR',unit='mag',null="",format='E',array=VPHAS_MAG_U_ERR) 
   









   cols=fits.ColDefs([col1,col2,col3,col4,col5,col6,col7,col8,col9,
               col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,
               col20,col21,col22,col23,col24,col25,col26,col27,col28,col29,
               col30,col31,col32,col33,col34, col35,col36,col37,col38,col39,
               col40,col41,col42,col43,col44,col45,col46,col47,col48,col49,
               col50,col51,col52,col53,col54,col55,col56,col57,col58,col59,
               col60,col61,col62,col63,col64,col65,col66,col67,col68,col69,
               col70,col71,col72,col73,col74,col75,col76,col77,col78,col79,
               col80,col81,col82,col83,col84,col85,col86,col87,col88,col89,
               col90,col91,col92,col93,col94,col95,col96,col97,col98,col99,
               col100,col101,col102,col103,col104,col105,col106,col107,col108])

   tbhdu = fits.BinTableHDU.from_columns(cols)


#  Primary header information. Modify according to you needs
   prihdr = fits.Header()

   prihdr['DATAMVER']='8.00'
   prihdr.comments['DATAMVER']='WEAVE Data Model Version'
   prihdr['TRIMESTE']=''
   prihdr.comments['TRIMESTE']='Observing Trimester'
   prihdr['MAG_G_CM']=''
   prihdr.comments['MAG_G_CM']='Survey specific mag column(s) used for MAG_G'
   prihdr['MAG_R_CM']=''
   prihdr.comments['MAG_R_CM']='Survey specific mag column(s) used for MAG_R'
   prihdr['MAG_I_CM']=''
   prihdr.comments['MAG_I_CM']='Survey specific mag column(s) used for MAG_I'
   prihdr['STL_NME1']=''
   prihdr['STL_NME2']=''
   prihdr['STL_MAIL']=''
   prihdr['CAT_NME1']=''
   prihdr['CAT_NME2']=''
   prihdr['CAT_MAIL']=''
   prihdr['CAT_CC']=''
   prihdr['DATETIME']=datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')
   prihdr.comments['DATETIME']='DateTime file created'

   prihdu = fits.PrimaryHDU(header=prihdr)

   thdulist=fits.HDUList([prihdu,tbhdu])
   thdulist.writeto(filename,overwrite=True,checksum=True)


   hdulist=fits.open(filename)
   prihdr0 = hdulist[0].header
   prihdr1 = hdulist[1].header

   hdulist[1].header.set('EXTNAME','NAME OF YOUR CATALOGUE','Extension name',after='TFIELDS')
   hdulist[1].header.set('COMMENT','APS Keyword Default Values in ICD-030. NULL means Default values','',after='EXTNAME')
   hdulist[0].header.set('COMMENT','Your Catalogue Template','',before='DATAMVER')



#comments:
   hdulist[1].header.comments['TTYPE1']='WEAVE object name from coordinates'
   hdulist[1].header.comments['TTYPE2']='The Survey where the target belongs'
   hdulist[1].header.comments['TTYPE3']='Optional description of (sub-)survey/programme'
   hdulist[1].header.comments['TTYPE4']='Catalogue filename'
   hdulist[1].header.comments['TTYPE5']='The identifier of the target assigned by survey'
   hdulist[1].header.comments['TTYPE6']='The target name'
   hdulist[1].header.comments['TTYPE7']='Target relative priority within a survey (1-10)'
   hdulist[1].header.comments['TTYPE8']='T=target, S=sky, G=guide C=calib., R=random'
   hdulist[1].header.comments['TTYPE9']='Classification of the target assigned by survey'
   hdulist[1].header.comments['TTYPE10']='Observing Program Template'
   hdulist[1].header.comments['TTYPE11']='Observing Constrains Template'

   hdulist[1].header.comments['TTYPE12']='Gaia Source Identifier'
   hdulist[1].header.comments['TTYPE13']='Gaia Data Release'
   hdulist[1].header.comments['TTYPE14']='Gaia RA of target in decimal degrees'
   hdulist[1].header.comments['TTYPE15']='Gaia Dec of target in decimal degrees'
   hdulist[1].header.comments['TTYPE16']='Gaia Epoch of target in (Julian) decimal years'
   hdulist[1].header.comments['TTYPE17']='Gaia Proper Motion of target in mas/yr in RA'
   hdulist[1].header.comments['TTYPE18']='Error on GAIA_PMRA'
   hdulist[1].header.comments['TTYPE19']='Gaia Proper Motion of target in mas/yr in Dec'
   hdulist[1].header.comments['TTYPE20']='Error on GAIA_PMDEC'
   hdulist[1].header.comments['TTYPE21']='Gaia Parallax of target in mas'
   hdulist[1].header.comments['TTYPE22']='Error on GAIA_PARAL'


   hdulist[1].header.comments['TTYPE23']='HEALpix ID for Nside=16 nested unsigned integer'
   hdulist[1].header.comments['TTYPE24']='Identifier for spaxel within IFU'
   hdulist[1].header.comments['TTYPE25']='Position Angle for IFU bundle'
   hdulist[1].header.comments['TTYPE26']='IFU dither pattern code (-1,0,-3,3,5,6) '

   hdulist[1].header.comments['TTYPE27']='Magnitude for target in SDSS-like g band (AB)'
   hdulist[1].header.comments['TTYPE28']='Error on MAG_G'
   hdulist[1].header.comments['TTYPE29']='Magnitude for target in SDSS-like r band (AB)'
   hdulist[1].header.comments['TTYPE30']='Error on MAG_R'
   hdulist[1].header.comments['TTYPE31']='Magnitude for target in SDSS-like i band (AB)'
   hdulist[1].header.comments['TTYPE32']='Error on MAG_I'

   hdulist[1].header.comments['TTYPE33']='Magnitude for target in Gaia G band (Vega)'
   hdulist[1].header.comments['TTYPE34']='Error on GAIA_MAG_G'
   hdulist[1].header.comments['TTYPE35']='Magnitude for target in Gaia BP band (Vega)'
   hdulist[1].header.comments['TTYPE36']='Error on GAIA_MAG_BP'
   hdulist[1].header.comments['TTYPE37']='Magnitude for target in Gaia RP band (Vega)'
   hdulist[1].header.comments['TTYPE38']='Error on GAIA_MAG_RP'

   hdulist[1].header.comments['TTYPE39']='Minimum rest-frame wavelength considered'
   hdulist[1].header.comments['TTYPE40']='Maximum rest-frame wavelength considered'
   hdulist[1].header.comments['TTYPE41']='Redshift of the system (heliocentric corrected)'
   hdulist[1].header.comments['TTYPE42']='Initial guess of the velocity dispersion'
   hdulist[1].header.comments['TTYPE43']='Library of spectral templates'
   hdulist[1].header.comments['TTYPE44']='Normalise the spectral template library'
   hdulist[1].header.comments['TTYPE45']='Minimum observed wavelength for use by pPXF'
   hdulist[1].header.comments['TTYPE46']='Maximum observed wavelength for use by pPXF'
   hdulist[1].header.comments['TTYPE47']='Number of kinematic moments to be extracted '
   hdulist[1].header.comments['TTYPE48']='Degree of additive Legendre polynomial'
   hdulist[1].header.comments['TTYPE49']='Degree of multiplicative Legendre polynomial'
   hdulist[1].header.comments['TTYPE50']='Number of MC simulations to extract pPXF errors'
   hdulist[1].header.comments['TTYPE51']='Run GANDALF to extract emission-line kinematics'
   hdulist[1].header.comments['TTYPE52']='Derive errors on the emission-line analysis'
   hdulist[1].header.comments['TTYPE53']='Initial estimate for reddening by dust'
   hdulist[1].header.comments['TTYPE54']='Second estimate for reddening by dust'
   hdulist[1].header.comments['TTYPE55']='De-redden the spectra for galactic extinction'
   hdulist[1].header.comments['TTYPE56']='Extract indices and convert them to SSP prop.'
   hdulist[1].header.comments['TTYPE57']='Spectral resolution (FWHM) of index measurement'
   hdulist[1].header.comments['TTYPE58']='Number of MC simulations to extract errors'
   hdulist[1].header.comments['TTYPE59']='Number of walkers for the SP MCMC algorithm'
   hdulist[1].header.comments['TTYPE60']='Number of iterations in the SP MCMC algorithm'
   hdulist[1].header.comments['TTYPE61']='Mask this fibre in the IFU analysis'
   hdulist[1].header.comments['TTYPE62']='Type of spatial binning for the data'
   hdulist[1].header.comments['TTYPE63']='Target SNR per pixel for the spatial binning'
   hdulist[1].header.comments['TTYPE64']='Minimum SNR per pixel for the spatial binning'
   hdulist[1].header.comments['TTYPE65']='Correct for spatial correlations'
   hdulist[1].header.comments['TTYPE66']='Identifier for sources within an IFU mosaic'
   hdulist[1].header.comments['TTYPE67']='RA of the centre of its IFU source'
   hdulist[1].header.comments['TTYPE68']='Dec of the centre of its IFU source'
   hdulist[1].header.comments['TTYPE69']='Bit mask activating APS-CS-CDP modules'


   hdulist[1].header.comments['TTYPE70']='Gaia galactic latitude in decimal degrees'
   hdulist[1].header.comments['TTYPE71']='Gaia galactic longitude in decimal degrees'

   hdulist[1].header.comments['TTYPE72']='IGAPS data release'
   hdulist[1].header.comments['TTYPE73']='IGAPS target identifier' 
   hdulist[1].header.comments['TTYPE74']='IGAPS g magnitude'
   hdulist[1].header.comments['TTYPE75']='Error on IGAPS_MAG_G'
   hdulist[1].header.comments['TTYPE76']='IGAPS Halpha Magnitude'
   hdulist[1].header.comments['TTYPE77']='Error on IGAPS_MAG_HA'
   hdulist[1].header.comments['TTYPE78']='IGAPS i Magnitude'
   hdulist[1].header.comments['TTYPE79']='Error on IGAPS_MAG_I'
   hdulist[1].header.comments['TTYPE80']='IGAPS r Magnitude (IPHAS)'
   hdulist[1].header.comments['TTYPE81']='Error on IGAPS_MAG_R_I'
   hdulist[1].header.comments['TTYPE82']='IGAPS r magnitude (UVEX)'
   hdulist[1].header.comments['TTYPE83']='Error on IGAPS_MAG_R_U'
   hdulist[1].header.comments['TTYPE84']='IGAPS U magnitude'
   hdulist[1].header.comments['TTYPE85']='Error on IGAPS_MAG_U'


   hdulist[1].header.comments['TTYPE86']='Source of the UBVRIugirzy (OPT) observations'
   hdulist[1].header.comments['TTYPE87']='Data release of OPTCAT_ID'
   hdulist[1].header.comments['TTYPE88']='Target identifier associated with OPTCAT'
   hdulist[1].header.comments['TTYPE89']='Magnitude in the g band for OPTCAT_ID'
   hdulist[1].header.comments['TTYPE90']='Error on OPTCAT_MAG_G '
   hdulist[1].header.comments['TTYPE91']='Magnitude in the I or i band for OPTCAT_ID '
   hdulist[1].header.comments['TTYPE92']='Error on OPTCAT_MAG_I'
   hdulist[1].header.comments['TTYPE93']='Magnitude in the R or r band for OPTCAT_ID'
   hdulist[1].header.comments['TTYPE94']='Error on OPTCAT_MAG_R'



   hdulist[1].header.comments['TTYPE95']='VPHAS data release'
   hdulist[1].header.comments['TTYPE96']='VPHAS target identifier'
   hdulist[1].header.comments['TTYPE97']='VPHAS g magnitude'
   hdulist[1].header.comments['TTYPE98']='Error on VPHAS_MAG_G'
   hdulist[1].header.comments['TTYPE99']='VPHAS Halpha magnitude'
   hdulist[1].header.comments['TTYPE100']='Error on VPHAS_MAG_HA'
   hdulist[1].header.comments['TTYPE101']='VPHAS i magnitude'
   hdulist[1].header.comments['TTYPE102']='Error on VPHAS_MAG_I'
   hdulist[1].header.comments['TTYPE103']='VPHAS magnitude in r band (red)'
   hdulist[1].header.comments['TTYPE104']='Error on VPHAS_MAG_R'
   hdulist[1].header.comments['TTYPE105']='VPHAS magnitude in r band (blue)'
   hdulist[1].header.comments['TTYPE106']='Error on VPHAS_MAG_R2'
   hdulist[1].header.comments['TTYPE107']='VPHAS magnitude in u band'
   hdulist[1].header.comments['TTYPE108']='Error on VPHAS_MAG_U'







# TFORM:

   hdulist[1].header.comments['TFORM1']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM2']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM3']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM4']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM5']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM6']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM7']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM8']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM9']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM10']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM11']='data format of field: ASCII Character'

   hdulist[1].header.comments['TFORM12']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM13']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM14']='data format of field: 8-byte DOUBLE'
   hdulist[1].header.comments['TFORM15']='data format of field: 8-byte DOUBLE'
   hdulist[1].header.comments['TFORM16']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM17']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM18']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM19']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM20']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM21']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM22']='data format of field: 4-byte REAL'

   hdulist[1].header.comments['TFORM23']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM24']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM25']='data format of field: 8-byte DOUBLE'
   hdulist[1].header.comments['TFORM26']='data format of field: 2-byte INTEGER'

   hdulist[1].header.comments['TFORM27']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM28']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM29']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM30']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM31']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM32']='data format of field: 4-byte REAL'

   hdulist[1].header.comments['TFORM33']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM34']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM35']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM36']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM37']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM38']='data format of field: 4-byte REAL'

   hdulist[1].header.comments['TFORM39']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM40']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM41']='data format of field: 4-byte REAL '
   hdulist[1].header.comments['TFORM42']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM43']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM44']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM45']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM46']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM47']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM48']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM49']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM50']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM51']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM52']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM53']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM54']='data format of field: 4-byte REAL'  
   hdulist[1].header.comments['TFORM55']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM56']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM57']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM58']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM59']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM60']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM61']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM62']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM63']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM64']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM65']='data format of field: 2-byte INTEGER'
   hdulist[1].header.comments['TFORM66']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM67']='data format of field: 8-byte DOUBLE'
   hdulist[1].header.comments['TFORM68']='data format of field: 8-byte DOUBLE'
   hdulist[1].header.comments['TFORM69']='data format of field: ASCII Character'


   hdulist[1].header.comments['TFORM70']='data format of field: 8-byte DOUBLE'
   hdulist[1].header.comments['TFORM71']='data format of field: 8-byte DOUBLE'

   hdulist[1].header.comments['TFORM72']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM73']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM74']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM75']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM76']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM77']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM78']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM79']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM80']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM81']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM82']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM83']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM84']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM85']='data format of field: 4-byte REAL'

   hdulist[1].header.comments['TFORM86']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM87']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM88']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM89']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM90']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM91']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM92']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM93']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM94']='data format of field: 4-byte REAL'



   hdulist[1].header.comments['TFORM95']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM96']='data format of field: ASCII Character'
   hdulist[1].header.comments['TFORM97']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM98']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM99']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM100']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM101']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM102']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM103']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM104']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM105']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM106']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM107']='data format of field: 4-byte REAL'
   hdulist[1].header.comments['TFORM108']='data format of field: 4-byte REAL'



# TDISP
   hdulist[1].header.set('TDISP1','A20','Display format for column',after='TFORM1')
   hdulist[1].header.set('TDISP2','A15','Display format for column',after='TFORM2')
   hdulist[1].header.set('TDISP3','A40','Display format for column',after='TFORM3')
   hdulist[1].header.set('TDISP4','A30','Display format for column',after='TFORM4')
   hdulist[1].header.set('TDISP5','A30','Display format for column',after='TFORM5')
   hdulist[1].header.set('TDISP6','A30','Display format for column',after='TFORM6')
   hdulist[1].header.set('TDISP7','F4.1','Display format for column',after='TFORM7')
   hdulist[1].header.set('TDISP8','A1','Display format for column',after='TFORM8')
   hdulist[1].header.set('TDISP9','A12','Display format for column',after='TFORM9')
   hdulist[1].header.set('TDISP10','A8','Display format for column',after='TFORM10')
   hdulist[1].header.set('TDISP11','A5','Display format for column',after='TFORM11')

   hdulist[1].header.set('TDISP12','A25','Display format for column',after='TFORM12')
   hdulist[1].header.set('TDISP13','A5','Display format for column',after='TFORM13')
   hdulist[1].header.set('TDISP14','F11.7','Display format for column',after='TFORM14')
   hdulist[1].header.set('TDISP15','F11.7','Display format for column',after='TFORM15')
   hdulist[1].header.set('TDISP16','F6.1','Display format for column',after='TFORM16')
   hdulist[1].header.set('TDISP17','F11.3','Display format for column',after='TFORM17')
   hdulist[1].header.set('TDISP18','F10.3','Display format for column',after='TFORM18')
   hdulist[1].header.set('TDISP19','F11.3','Display format for column',after='TFORM19')
   hdulist[1].header.set('TDISP20','F10.3','Display format for column',after='TFORM20')
   hdulist[1].header.set('TDISP21','F10.3','Display format for column',after='TFORM21')
   hdulist[1].header.set('TDISP22','F10.3','Display format for column',after='TFORM22')

   hdulist[1].header.set('TDISP23','I4','Display format for column',after='TFORM23')
   hdulist[1].header.set('TDISP24','A6','Display format for column',after='TFORM24')
   hdulist[1].header.set('TDISP25','F11.7','Display format for column',after='TFORM25')
   hdulist[1].header.set('TDISP26','I2','Display format for column',after='TFORM26')

   hdulist[1].header.set('TDISP27','F7.3','Display format for column',after='TFORM27')
   hdulist[1].header.set('TDISP28','F7.3','Display format for column',after='TFORM28')
   hdulist[1].header.set('TDISP29','F7.3','Display format for column',after='TFORM29')
   hdulist[1].header.set('TDISP30','F7.3','Display format for column',after='TFORM30')
   hdulist[1].header.set('TDISP31','F7.3','Display format for column',after='TFORM31')
   hdulist[1].header.set('TDISP32','F7.3','Display format for column',after='TFORM32')

   hdulist[1].header.set('TDISP33','F7.3','Display format for column',after='TFORM33')
   hdulist[1].header.set('TDISP34','F7.3','Display format for column',after='TFORM34')
   hdulist[1].header.set('TDISP35','F7.3','Display format for column',after='TFORM35')
   hdulist[1].header.set('TDISP36','F7.3','Display format for column',after='TFORM36')
   hdulist[1].header.set('TDISP37','F7.3','Display format for column',after='TFORM37')
   hdulist[1].header.set('TDISP38','F7.3','Display format for column',after='TFORM38')

   hdulist[1].header.set('TDISP39','F8.2','Display format for column',after='TFORM39')
   hdulist[1].header.set('TDISP40','F8.2','Display format for column',after='TFORM40')
   hdulist[1].header.set('TDISP41','F9.5','Display format for column',after='TFORM41')
   hdulist[1].header.set('TDISP42','F4.0','Display format for column',after='TFORM42')
   hdulist[1].header.set('TDISP43','A10','Display format for column',after='TFORM43')
   hdulist[1].header.set('TDISP44','I1','Display format for column',after='TFORM44')
   hdulist[1].header.set('TDISP45','F8.2','Display format for column',after='TFORM45')
   hdulist[1].header.set('TDISP46','F8.2','Display format for column',after='TFORM46')
   hdulist[1].header.set('TDISP47','I1','Display format for column',after='TFORM47')
   hdulist[1].header.set('TDISP48','I2','Display format for column',after='TFORM48')
   hdulist[1].header.set('TDISP49','I2','Display format for column',after='TFORM49')
   hdulist[1].header.set('TDISP50','I5','Display format for column',after='TFORM50')
   hdulist[1].header.set('TDISP51','I1','Display format for column',after='TFORM51')
   hdulist[1].header.set('TDISP52','I1','Display format for column',after='TFORM52')
   hdulist[1].header.set('TDISP53','F7.3','Display format for column',after='TFORM53')
   hdulist[1].header.set('TDISP54','F7.3','Display format for column',after='TFORM54')
   hdulist[1].header.set('TDISP55','I1','Display format for column',after='TFORM55')
   hdulist[1].header.set('TDISP56','I1','Display format for column',after='TFORM56')
   hdulist[1].header.set('TDISP57','F5.2','Display format for column',after='TFORM57')
   hdulist[1].header.set('TDISP58','I5','Display format for column',after='TFORM58')
   hdulist[1].header.set('TDISP59','I5','Display format for column',after='TFORM59')
   hdulist[1].header.set('TDISP60','I5','Display format for column',after='TFORM60')
   hdulist[1].header.set('TDISP61','I1','Display format for column',after='TFORM61')
   hdulist[1].header.set('TDISP62','A10','Display format for column',after='TFORM62')
   hdulist[1].header.set('TDISP63','F6.1','Display format for column',after='TFORM63')
   hdulist[1].header.set('TDISP64','F6.1','Display format for column',after='TFORM64')
   hdulist[1].header.set('TDISP65','I1','Display format for column',after='TFORM65')
   hdulist[1].header.set('TDISP66','A35','Display format for column',after='TFORM66')
   hdulist[1].header.set('TDISP67','F11.7','Display format for column',after='TFORM67')
   hdulist[1].header.set('TDISP68','F11.7','Display format for column',after='TFORM68')
   hdulist[1].header.set('TDISP69','A48','Display format for column',after='TFORM69')


   hdulist[1].header.set('TDISP70','F11.7','Display format for column',after='TFORM70')
   hdulist[1].header.set('TDISP71','F11.7','Display format for column',after='TFORM71')

   hdulist[1].header.set('TDISP72','A20','Display format for column',after='TFORM72')
   hdulist[1].header.set('TDISP73','A30','Display format for column',after='TFORM73')
   hdulist[1].header.set('TDISP74','F7.3','Display format for column',after='TFORM74')
   hdulist[1].header.set('TDISP75','F7.3','Display format for column',after='TFORM75')
   hdulist[1].header.set('TDISP76','F7.3','Display format for column',after='TFORM76')
   hdulist[1].header.set('TDISP77','F7.3','Display format for column',after='TFORM77')
   hdulist[1].header.set('TDISP78','F7.3','Display format for column',after='TFORM78')
   hdulist[1].header.set('TDISP79','F7.3','Display format for column',after='TFORM79')
   hdulist[1].header.set('TDISP80','F7.3','Display format for column',after='TFORM80')
   hdulist[1].header.set('TDISP81','F7.3','Display format for column',after='TFORM81')
   hdulist[1].header.set('TDISP82','F7.3','Display format for column',after='TFORM82')
   hdulist[1].header.set('TDISP83','F7.3','Display format for column',after='TFORM83')
   hdulist[1].header.set('TDISP84','F7.3','Display format for column',after='TFORM84')
   hdulist[1].header.set('TDISP85','F7.3','Display format for column',after='TFORM85')


   hdulist[1].header.set('TDISP86','A60','Display format for column',after='TFORM86')
   hdulist[1].header.set('TDISP87','A50','Display format for column',after='TFORM87')
   hdulist[1].header.set('TDISP88','A30','Display format for column',after='TFORM88')
   hdulist[1].header.set('TDISP89','F7.3','Display format for column',after='TFORM89')
   hdulist[1].header.set('TDISP90','F7.3','Display format for column',after='TFORM90')
   hdulist[1].header.set('TDISP91','F7.3','Display format for column',after='TFORM91')
   hdulist[1].header.set('TDISP92','F7.3','Display format for column',after='TFORM92')
   hdulist[1].header.set('TDISP93','F7.3','Display format for column',after='TFORM93')
   hdulist[1].header.set('TDISP94','F7.3','Display format for column',after='TFORM94')


   hdulist[1].header.set('TDISP95','A20','Display format for column',after='TFORM95')
   hdulist[1].header.set('TDISP96','A20','Display format for column',after='TFORM96')
   hdulist[1].header.set('TDISP97','F7.3','Display format for column',after='TFORM97')
   hdulist[1].header.set('TDISP98','F7.3','Display format for column',after='TFORM98')
   hdulist[1].header.set('TDISP99','F7.3','Display format for column',after='TFORM99')
   hdulist[1].header.set('TDISP100','F7.3','Display format for column',after='TFORM100')
   hdulist[1].header.set('TDISP101','F7.3','Display format for column',after='TFORM101')
   hdulist[1].header.set('TDISP102','F7.3','Display format for column',after='TFORM102')
   hdulist[1].header.set('TDISP103','F7.3','Display format for column',after='TFORM103')
   hdulist[1].header.set('TDISP104','F7.3','Display format for column',after='TFORM104')
   hdulist[1].header.set('TDISP105','F7.3','Display format for column',after='TFORM105')
   hdulist[1].header.set('TDISP106','F7.3','Display format for column',after='TFORM106')
   hdulist[1].header.set('TDISP107','F7.3','Display format for column',after='TFORM107')
   hdulist[1].header.set('TDISP108','F7.3','Display format for column',after='TFORM108')



#TUCD
   hdulist[1].header.set('TUCD1','meta.id;meta.main','UCD for column',after='TDISP1')
   hdulist[1].header.set('TUCD2','meta.id.parent','UCD for column',after='TDISP2')
   hdulist[1].header.set('TUCD3','meta.id.part','UCD for column',after='TDISP3')
   hdulist[1].header.set('TUCD4','meta.dataset','UCD for column',after='TDISP4')
   hdulist[1].header.set('TUCD5','meta.id','UCD for column',after='TDISP5')
   hdulist[1].header.set('TUCD6','meta.id','UCD for column',after='TDISP6')
   hdulist[1].header.set('TUCD7','meta.code','UCD for column',after='TDISP7')
   hdulist[1].header.set('TUCD8','meta.code.class','UCD for column',after='TDISP8')
   hdulist[1].header.set('TUCD9','src.class','UCD for column',after='TDISP9')
   hdulist[1].header.set('TUCD10','instr.setup','UCD for column',after='TDISP10')
   hdulist[1].header.set('TUCD11','obs.param','UCD for column',after='TDISP11')

   hdulist[1].header.set('TUCD12','meta.id','UCD for column',after='TDISP12')
   hdulist[1].header.set('TUCD13','time.release','UCD for column',after='TDISP13')
   hdulist[1].header.set('TUCD14','pos.eq.ra;meta.main','UCD for column',after='TDISP14')
   hdulist[1].header.set('TUCD15','pos.eq.dec;meta.main','UCD for column',after='TDISP15')
   hdulist[1].header.set('TUCD16','time.epoch','UCD for column',after='TDISP16')
   hdulist[1].header.set('TUCD17','pos.pm','UCD for column',after='TDISP17')
   hdulist[1].header.set('TUCD18','stat.error;pos.pm','UCD for column',after='TDISP18')
   hdulist[1].header.set('TUCD19','pos.pm','UCD for column',after='TDISP19')
   hdulist[1].header.set('TUCD20','stat.error;pos.pm','UCD for column',after='TDISP20')
   hdulist[1].header.set('TUCD21','pos.parallax','UCD for column',after='TDISP21')
   hdulist[1].header.set('TUCD22','stat.error;pos.parallax','UCD for column',after='TDISP22')

   hdulist[1].header.set('TUCD23','pos.healpix','UCD for column',after='TDISP23')
   hdulist[1].header.set('TUCD24','meta.id;instr','UCD for column',after='TDISP24')
   hdulist[1].header.set('TUCD25','pos.posAng','UCD for column',after='TDISP25')
   hdulist[1].header.set('TUCD26','meta.code.multip;obs.sequence','UCD for column',after='TDISP26')

   hdulist[1].header.set('TUCD27','phot.mag;em.opt','UCD for column',after='TDISP27')
   hdulist[1].header.set('TUCD28','stat.error;phot.mag;em.opt','UCD for column',after='TDISP28')
   hdulist[1].header.set('TUCD29','phot.mag;em.opt','UCD for column',after='TDISP29')
   hdulist[1].header.set('TUCD30','stat.error;phot.mag;em.opt','UCD for column',after='TDISP30')
   hdulist[1].header.set('TUCD31','phot.mag;em.opt','UCD for column',after='TDISP31')
   hdulist[1].header.set('TUCD32','stat.error;phot.mag;em.opt','UCD foNULL value for fieldr column',after='TDISP32')

   hdulist[1].header.set('TUCD33','phot.mag;em.opt','UCD for column',after='TDISP33')
   hdulist[1].header.set('TUCD34','stat.error;phot.mag;em.opt','UCD for column',after='TDISP34')
   hdulist[1].header.set('TUCD35','phot.mag;em.opt','UCD for column',after='TDISP35')
   hdulist[1].header.set('TUCD36','stat.error;phot.mag;em.opt','UCD for column',after='TDISP36')
   hdulist[1].header.set('TUCD37','phot.mag;em.opt','UCD for column',after='TDISP37')
   hdulist[1].header.set('TUCD38','stat.error;phot.mag;em.opt','UCD for column',after='TDISP38')

   hdulist[1].header.set('TUCD39','em.wl','UCD for column',after='TDISP39')
   hdulist[1].header.set('TUCD40','em.wl','UCD for column',after='TDISP40')
   hdulist[1].header.set('TUCD41','src.redshift','UCD for column',after='TDISP41')
   hdulist[1].header.set('TUCD42','phys.veloc.dispersion','UCD for column',after='TDISP42')
   hdulist[1].header.set('TUCD43','stat.fit.param','UCD for column',after='TDISP43')
   hdulist[1].header.set('TUCD44','meta.code','UCD for column',after='TDISP44')
   hdulist[1].header.set('TUCD45','em.wl','UCD for column',after='TDISP45')
   hdulist[1].header.set('TUCD46','em.wl','UCD for column',after='TDISP46')
   hdulist[1].header.set('TUCD47','stat.fit.dof','UCD for column',after='TDISP47')
   hdulist[1].header.set('TUCD48','stat.fit.dof','UCD for column',after='TDISP48')
   hdulist[1].header.set('TUCD49','stat.fit.dof','UCD for column',after='TDISP49')
   hdulist[1].header.set('TUCD50','meta.code.multip','UCD for column',after='TDISP50')
   hdulist[1].header.set('TUCD51','meta.code','UCD for column',after='TDISP51')
   hdulist[1].header.set('TUCD52','meta.code','UCD for column',after='TDISP52')
   hdulist[1].header.set('TUCD53','meta.code','UCD for column',after='TDISP53')
   hdulist[1].header.set('TUCD54','meta.code','UCD for column',after='TDISP54')
   hdulist[1].header.set('TUCD55','meta.code','UCD for column',after='TDISP55')
   hdulist[1].header.set('TUCD56','meta.code','UCD for column',after='TDISP56')
   hdulist[1].header.set('TUCD57','spect.resolution','UCD for column',after='TDISP57')
   hdulist[1].header.set('TUCD58','meta.code.multip','UCD for column',after='TDISP58')
   hdulist[1].header.set('TUCD59','meta.code.multip','UCD for column',after='TDISP59')
   hdulist[1].header.set('TUCD60','meta.code.multip','UCD for column',after='TDISP60')
   hdulist[1].header.set('TUCD61','meta.code','UCD for column',after='TDISP61')
   hdulist[1].header.set('TUCD62','meta.code','UCD for column',after='TDISP62')
   hdulist[1].header.set('TUCD63','stat.snr','UCD for column',after='TDISP63')
   hdulist[1].header.set('TUCD64','stat.snr','UCD for column',after='TDISP64')
   hdulist[1].header.set('TUCD65','meta.code','UCD for column',after='TDISP65')
   hdulist[1].header.set('TUCD66','meta.code','UCD for column',after='TDISP66')
   hdulist[1].header.set('TUCD67','pos.eq.ra','UCD for column',after='TDISP67')
   hdulist[1].header.set('TUCD68','pos.eq.dec','UCD for column',after='TDISP68')
   hdulist[1].header.set('TUCD69','meta.code','UCD for column',after='TDISP69')


   hdulist[1].header.set('TUCD70','pos.galactic.lat','UCD for column',after='TDISP70')
   hdulist[1].header.set('TUCD71','pos.galactic.lon','UCD for column',after='TDISP71')

   hdulist[1].header.set('TUCD72','time.release','UCD for column',after='TDISP72')
   hdulist[1].header.set('TUCD73','meta.id','UCD for column',after='TDISP73')
   hdulist[1].header.set('TUCD74','phot.mag;em.opt','UCD for column',after='TDISP74')
   hdulist[1].header.set('TUCD75','stat.error;phot.mag;em.opt','UCD for column',after='TDISP75')
   hdulist[1].header.set('TUCD76','phot.mag;em.opt','UCD for column',after='TDISP76')
   hdulist[1].header.set('TUCD77','stat.error;phot.mag;em.opt','UCD for column',after='TDISP77')
   hdulist[1].header.set('TUCD78','phot.mag;em.opt','UCD for column',after='TDISP78')
   hdulist[1].header.set('TUCD79','stat.error;phot.mag;em.opt','UCD for column',after='TDISP79')
   hdulist[1].header.set('TUCD80','phot.mag;em.opt','UCD for column',after='TDISP80')
   hdulist[1].header.set('TUCD81','stat.error;phot.mag;em.opt','UCD for column',after='TDISP81')
   hdulist[1].header.set('TUCD82','phot.mag;em.opt','UCD for column',after='TDISP82')
   hdulist[1].header.set('TUCD83','stat.error;phot.mag;em.opt','UCD for column',after='TDISP83')
   hdulist[1].header.set('TUCD84','phot.mag;em.opt','UCD for column',after='TDISP84')
   hdulist[1].header.set('TUCD85','stat.error;phot.mag;em.opt','UCD for column',after='TDISP85')


   hdulist[1].header.set('TUCD86','meta.dataset','UCD for column',after='TDISP86')
   hdulist[1].header.set('TUCD87','time.release','UCD for column',after='TDISP87')
   hdulist[1].header.set('TUCD88','meta.id','UCD for column',after='TDISP88')
   hdulist[1].header.set('TUCD89','phot.mag;em.opt','UCD for column',after='TDISP89')
   hdulist[1].header.set('TUCD90','stat.error;phot.mag;em.opt','UCD for column',after='TDISP90')
   hdulist[1].header.set('TUCD91','phot.mag;em.opt','UCD for column',after='TDISP91')
   hdulist[1].header.set('TUCD92','stat.error;phot.mag;em.opt','UCD for column',after='TDISP92')
   hdulist[1].header.set('TUCD93','phot.mag;em.opt','UCD for column',after='TDISP93')
   hdulist[1].header.set('TUCD94','stat.error;phot.mag;em.opt','UCD for column',after='TDISP94')
  



   hdulist[1].header.set('TUCD95','time.release','UCD for column',after='TDISP95')
   hdulist[1].header.set('TUCD96','meta.id','UCD for column',after='TDISP96')
   hdulist[1].header.set('TUCD97','phot.mag;em.opt','UCD for column',after='TDISP97')
   hdulist[1].header.set('TUCD98','stat.error;phot.mag;em.opt','UCD for column',after='TDISP98')
   hdulist[1].header.set('TUCD99','phot.mag;em.opt','UCD for column',after='TDISP99')
   hdulist[1].header.set('TUCD100','stat.error;phot.mag;em.opt','UCD for column',after='TDISP100')
   hdulist[1].header.set('TUCD101','phot.mag;em.opt','UCD for column',after='TDISP101')
   hdulist[1].header.set('TUCD102','stat.error;phot.mag;em.opt','UCD for column',after='TDISP102')
   hdulist[1].header.set('TUCD103','phot.mag;em.opt','UCD for column',after='TDISP103')
   hdulist[1].header.set('TUCD104','stat.error;phot.mag;em.opt','UCD for column',after='TDISP104')
   hdulist[1].header.set('TUCD105','phot.mag;em.opt','UCD for column',after='TDISP105')
   hdulist[1].header.set('TUCD106','stat.error;phot.mag;em.opt','UCD for column',after='TDISP106')
   hdulist[1].header.set('TUCD107','phot.mag;em.opt','UCD for column',after='TDISP107')
   hdulist[1].header.set('TUCD108','stat.error;phot.mag;em.opt','UCD for column',after='TDISP108')




#TPROP
   hdulist[1].header.set('TPROP1',0,'Public Column',after='TUCD1')
   hdulist[1].header.set('TPROP2',0,'Public Column',after='TUCD2')
   hdulist[1].header.set('TPROP3',0,'Public Column',after='TUCD3')
   hdulist[1].header.set('TPROP4',0,'Public Column',after='TUCD4')
   hdulist[1].header.set('TPROP5',0,'Public Column',after='TUCD5')
   hdulist[1].header.set('TPROP6',0,'Public Column',after='TUCD6')
   hdulist[1].header.set('TPROP7',0,'Public Column',after='TUCD7')
   hdulist[1].header.set('TPROP8',0,'Public Column',after='TUCD8')
   hdulist[1].header.set('TPROP9',0,'Public Column',after='TUCD9')
   hdulist[1].header.set('TPROP10',0,'Public Column',after='TUCD10')
   hdulist[1].header.set('TPROP11',0,'Public Column',after='TUCD11')
   hdulist[1].header.set('TPROP12',0,'Public Column',after='TUCD12')
   hdulist[1].header.set('TPROP13',0,'Public Column',after='TUCD13')
   hdulist[1].header.set('TPROP14',0,'Public Column',after='TUCD14')
   hdulist[1].header.set('TPROP15',0,'Public Column',after='TUCD15')
   hdulist[1].header.set('TPROP16',0,'Public Column',after='TUCD16')
   hdulist[1].header.set('TPROP17',0,'Public Column',after='TUCD17')
   hdulist[1].header.set('TPROP18',0,'Public Column',after='TUCD18')
   hdulist[1].header.set('TPROP19',0,'Public Column',after='TUCD19')
   hdulist[1].header.set('TPROP20',0,'Public Column',after='TUCD20')
   hdulist[1].header.set('TPROP21',0,'Public Column',after='TUCD21')
   hdulist[1].header.set('TPROP22',0,'Public Column',after='TUCD22')
   hdulist[1].header.set('TPROP23',0,'Public Column',after='TUCD23')
   hdulist[1].header.set('TPROP24',0,'Public Column',after='TUCD24')
   hdulist[1].header.set('TPROP25',0,'Public Column',after='TUCD25')
   hdulist[1].header.set('TPROP26',0,'Public Column',after='TUCD26')
   hdulist[1].header.set('TPROP27',0,'Public Column',after='TUCD27')
   hdulist[1].header.set('TPROP28',0,'Public Column',after='TUCD28')
   hdulist[1].header.set('TPROP29',0,'Public Column',after='TUCD29')
   hdulist[1].header.set('TPROP30',0,'Public Column',after='TUCD30')
   hdulist[1].header.set('TPROP31',0,'Public Column',after='TUCD31')
   hdulist[1].header.set('TPROP32',0,'Public Column',after='TUCD32')
   hdulist[1].header.set('TPROP33',0,'Public Column',after='TUCD33')
   hdulist[1].header.set('TPROP34',0,'Public Column',after='TUCD34')
   hdulist[1].header.set('TPROP35',0,'Public Column',after='TUCD35')
   hdulist[1].header.set('TPROP36',0,'Public Column',after='TUCD36')
   hdulist[1].header.set('TPROP37',0,'Public Column',after='TUCD37')
   hdulist[1].header.set('TPROP38',0,'Public Column',after='TUCD38')
   hdulist[1].header.set('TPROP39',0,'Public Column',after='TUCD39')
   hdulist[1].header.set('TPROP40',0,'Public Column',after='TUCD40')
   hdulist[1].header.set('TPROP41',0,'Public Column',after='TUCD41')
   hdulist[1].header.set('TPROP42',0,'Public Column',after='TUCD42')
   hdulist[1].header.set('TPROP43',0,'Public Column',after='TUCD43')
   hdulist[1].header.set('TPROP44',0,'Public Column',after='TUCD44')
   hdulist[1].header.set('TPROP45',0,'Public Column',after='TUCD45')
   hdulist[1].header.set('TPROP46',0,'Public Column',after='TUCD46')
   hdulist[1].header.set('TPROP47',0,'Public Column',after='TUCD47')
   hdulist[1].header.set('TPROP48',0,'Public Column',after='TUCD48')
   hdulist[1].header.set('TPROP49',0,'Public Column',after='TUCD49')
   hdulist[1].header.set('TPROP50',0,'Public Column',after='TUCD50')
   hdulist[1].header.set('TPROP51',0,'Public Column',after='TUCD51')
   hdulist[1].header.set('TPROP52',0,'Public Column',after='TUCD52')
   hdulist[1].header.set('TPROP53',0,'Public Column',after='TUCD53')
   hdulist[1].header.set('TPROP54',0,'Public Column',after='TUCD54')
   hdulist[1].header.set('TPROP55',0,'Public Column',after='TUCD55')
   hdulist[1].header.set('TPROP56',0,'Public Column',after='TUCD56')
   hdulist[1].header.set('TPROP57',0,'Public Column',after='TUCD57')
   hdulist[1].header.set('TPROP58',0,'Public Column',after='TUCD58')
   hdulist[1].header.set('TPROP59',0,'Public Column',after='TUCD59')
   hdulist[1].header.set('TPROP60',0,'Public Column',after='TUCD60')
   hdulist[1].header.set('TPROP61',0,'Public Column',after='TUCD61')
   hdulist[1].header.set('TPROP62',0,'Public Column',after='TUCD62')
   hdulist[1].header.set('TPROP63',0,'Public Column',after='TUCD63')
   hdulist[1].header.set('TPROP64',0,'Public Column',after='TUCD64')
   hdulist[1].header.set('TPROP65',0,'Public Column',after='TUCD65')
   hdulist[1].header.set('TPROP66',0,'Public Column',after='TUCD66')
   hdulist[1].header.set('TPROP67',0,'Public Column',after='TUCD67')
   hdulist[1].header.set('TPROP68',0,'Public Column',after='TUCD68')
   hdulist[1].header.set('TPROP69',0,'Public Column',after='TUCD69')
   hdulist[1].header.set('TPROP70',0,'Public Column',after='TUCD70')
   hdulist[1].header.set('TPROP71',0,'Public Column',after='TUCD71')
   hdulist[1].header.set('TPROP72',0,'Public Column',after='TUCD72')
   hdulist[1].header.set('TPROP73',0,'Public Column',after='TUCD73')
   hdulist[1].header.set('TPROP74',0,'Public Column',after='TUCD74')
   hdulist[1].header.set('TPROP75',0,'Public Column',after='TUCD75')
   hdulist[1].header.set('TPROP76',0,'Public Column',after='TUCD76')
   hdulist[1].header.set('TPROP77',0,'Public Column',after='TUCD77')
   hdulist[1].header.set('TPROP78',0,'Public Column',after='TUCD78')
   hdulist[1].header.set('TPROP79',0,'Public Column',after='TUCD79')
   hdulist[1].header.set('TPROP80',0,'Public Column',after='TUCD80')
   hdulist[1].header.set('TPROP81',0,'Public Column',after='TUCD81')
   hdulist[1].header.set('TPROP82',0,'Public Column',after='TUCD82')
   hdulist[1].header.set('TPROP83',0,'Public Column',after='TUCD83')
   hdulist[1].header.set('TPROP84',0,'Public Column',after='TUCD84')
   hdulist[1].header.set('TPROP85',0,'Public Column',after='TUCD85')
   hdulist[1].header.set('TPROP86',0,'Public Column',after='TUCD86')
   hdulist[1].header.set('TPROP87',0,'Public Column',after='TUCD87')
   hdulist[1].header.set('TPROP88',0,'Public Column',after='TUCD88')
   hdulist[1].header.set('TPROP89',0,'Public Column',after='TUCD89')
   hdulist[1].header.set('TPROP90',0,'Public Column',after='TUCD90')
   hdulist[1].header.set('TPROP91',0,'Public Column',after='TUCD91')
   hdulist[1].header.set('TPROP92',0,'Public Column',after='TUCD92')
   hdulist[1].header.set('TPROP93',0,'Public Column',after='TUCD93')
   hdulist[1].header.set('TPROP94',0,'Public Column',after='TUCD94')
   hdulist[1].header.set('TPROP95',0,'Public Column',after='TUCD95')
   hdulist[1].header.set('TPROP96',0,'Public Column',after='TUCD96')
   hdulist[1].header.set('TPROP97',0,'Public Column',after='TUCD97')
   hdulist[1].header.set('TPROP98',0,'Public Column',after='TUCD98')
   hdulist[1].header.set('TPROP99',0,'Public Column',after='TUCD99')
   hdulist[1].header.set('TPROP100',0,'Public Column',after='TUCD100')
   hdulist[1].header.set('TPROP101',0,'Public Column',after='TUCD101')
   hdulist[1].header.set('TPROP102',0,'Public Column',after='TUCD102')
   hdulist[1].header.set('TPROP103',0,'Public Column',after='TUCD103')
   hdulist[1].header.set('TPROP104',0,'Public Column',after='TUCD104')
   hdulist[1].header.set('TPROP105',0,'Public Column',after='TUCD105')
   hdulist[1].header.set('TPROP106',0,'Public Column',after='TUCD106')
   hdulist[1].header.set('TPROP107',0,'Public Column',after='TUCD107')
   hdulist[1].header.set('TPROP108',0,'Public Column',after='TUCD108')




# NULL

   hdulist[1].header.set('TNULL23',-1,'NULL value for field', after='TPROP23')
   hdulist[1].header.set('TNULL26',0,'NULL value for field', after='TPROP26')
   hdulist[1].header.set('TNULL44',-1,'NULL value for field', after='TPROP44')
   hdulist[1].header.set('TNULL47',-1,'NULL value for field', after='TPROP47')
   hdulist[1].header.set('TNULL48',-1,'NULL value for field', after='TPROP48')
   hdulist[1].header.set('TNULL49',-1,'NULL value for field', after='TPROP49')
   hdulist[1].header.set('TNULL50',-1,'NULL value for field', after='TPROP50')
   hdulist[1].header.set('TNULL51',-1,'NULL value for field', after='TPROP51')
   hdulist[1].header.set('TNULL52',-1,'NULL value for field', after='TPROP52')
   hdulist[1].header.set('TNULL55',-1,'NULL value for field', after='TPROP55')
   hdulist[1].header.set('TNULL56',-1,'NULL value for field', after='TPROP56')
   hdulist[1].header.set('TNULL58',-1,'NULL value for field', after='TPROP58')
   hdulist[1].header.set('TNULL59',-1,'NULL value for field', after='TPROP59')
   hdulist[1].header.set('TNULL60',-1,'NULL value for field', after='TPROP60')
   hdulist[1].header.set('TNULL61',-1,'NULL value for field', after='TPROP61')
   hdulist[1].header.set('TNULL65',-1,'NULL value for field', after='TPROP65')





# TUNIT
   hdulist[1].header.comments['TUNIT1']='none'
   hdulist[1].header.comments['TUNIT2']='none'
   hdulist[1].header.comments['TUNIT3']='none'
   hdulist[1].header.comments['TUNIT4']='none'
   hdulist[1].header.comments['TUNIT5']='none'
   hdulist[1].header.comments['TUNIT6']='none'
   hdulist[1].header.comments['TUNIT7']='none'
   hdulist[1].header.comments['TUNIT8']='none'
   hdulist[1].header.comments['TUNIT9']='none'
   hdulist[1].header.comments['TUNIT10']='none'
   hdulist[1].header.comments['TUNIT11']='none'

   hdulist[1].header.comments['TUNIT12']='none'
   hdulist[1].header.comments['TUNIT13']='none'
   hdulist[1].header.comments['TUNIT14']='physical unit of field'
   hdulist[1].header.comments['TUNIT15']='physical unit of field'
   hdulist[1].header.comments['TUNIT16']='physical unit of field'
   hdulist[1].header.comments['TUNIT17']='physical unit of field'
   hdulist[1].header.comments['TUNIT18']='physical unit of field'
   hdulist[1].header.comments['TUNIT19']='physical unit of field'
   hdulist[1].header.comments['TUNIT20']='physical unit of field'
   hdulist[1].header.comments['TUNIT21']='physical unit of field'
   hdulist[1].header.comments['TUNIT22']='physical unit of field'

   hdulist[1].header.comments['TUNIT23']='none'
   hdulist[1].header.comments['TUNIT24']='none'
   hdulist[1].header.comments['TUNIT25']='physical unit of field'
   hdulist[1].header.comments['TUNIT26']='none'

   hdulist[1].header.comments['TUNIT27']='physical unit of field'
   hdulist[1].header.comments['TUNIT28']='physical unit of field'
   hdulist[1].header.comments['TUNIT29']='physical unit of field'
   hdulist[1].header.comments['TUNIT30']='physical unit of field'
   hdulist[1].header.comments['TUNIT31']='physical unit of field'
   hdulist[1].header.comments['TUNIT32']='physical unit of field'

   hdulist[1].header.comments['TUNIT33']='physical unit of field'
   hdulist[1].header.comments['TUNIT34']='physical unit of field'
   hdulist[1].header.comments['TUNIT35']='physical unit of field'
   hdulist[1].header.comments['TUNIT36']='physical unit of field'
   hdulist[1].header.comments['TUNIT37']='physical unit of field'
   hdulist[1].header.comments['TUNIT38']='physical unit of field'

   hdulist[1].header.comments['TUNIT39']='physical unit of field'
   hdulist[1].header.comments['TUNIT40']='physical unit of field'
   hdulist[1].header.comments['TUNIT41']='none'
   hdulist[1].header.comments['TUNIT42']='physical unit of field'
   hdulist[1].header.comments['TUNIT43']='none'
   hdulist[1].header.comments['TUNIT44']='none'
   hdulist[1].header.comments['TUNIT45']='physical unit of field'
   hdulist[1].header.comments['TUNIT46']='physical unit of field'
   hdulist[1].header.comments['TUNIT47']='none'
   hdulist[1].header.comments['TUNIT48']='none'
   hdulist[1].header.comments['TUNIT49']='none'
   hdulist[1].header.comments['TUNIT50']='none'
   hdulist[1].header.comments['TUNIT51']='none'
   hdulist[1].header.comments['TUNIT52']='none'
   hdulist[1].header.comments['TUNIT53']='none'
   hdulist[1].header.comments['TUNIT54']='none'
   hdulist[1].header.comments['TUNIT55']='none'
   hdulist[1].header.comments['TUNIT56']='none'
   hdulist[1].header.comments['TUNIT57']='physical unit of field'
   hdulist[1].header.comments['TUNIT58']='none'
   hdulist[1].header.comments['TUNIT59']='none'
   hdulist[1].header.comments['TUNIT60']='none'
   hdulist[1].header.comments['TUNIT61']='none'
   hdulist[1].header.comments['TUNIT62']='none'
   hdulist[1].header.comments['TUNIT63']='none'
   hdulist[1].header.comments['TUNIT64']='none'
   hdulist[1].header.comments['TUNIT65']='none'
   hdulist[1].header.comments['TUNIT66']='none'
   hdulist[1].header.comments['TUNIT67']='physical unit of field'
   hdulist[1].header.comments['TUNIT68']='physical unit of field'
   hdulist[1].header.comments['TUNIT69']='none'


   hdulist[1].header.comments['TUNIT70']='physical unit of field'
   hdulist[1].header.comments['TUNIT71']='physical unit of field'

   hdulist[1].header.comments['TUNIT72']='none'
   hdulist[1].header.comments['TUNIT73']='none'
   hdulist[1].header.comments['TUNIT74']='physical unit of field'
   hdulist[1].header.comments['TUNIT75']='physical unit of field'
   hdulist[1].header.comments['TUNIT76']='physical unit of field'
   hdulist[1].header.comments['TUNIT77']='physical unit of field'
   hdulist[1].header.comments['TUNIT78']='physical unit of field'
   hdulist[1].header.comments['TUNIT79']='physical unit of field'
   hdulist[1].header.comments['TUNIT80']='physical unit of field'
   hdulist[1].header.comments['TUNIT81']='physical unit of field'
   hdulist[1].header.comments['TUNIT82']='physical unit of field'
   hdulist[1].header.comments['TUNIT83']='physical unit of field'
   hdulist[1].header.comments['TUNIT84']='physical unit of field'
   hdulist[1].header.comments['TUNIT85']='physical unit of field'

   hdulist[1].header.comments['TUNIT86']='none'
   hdulist[1].header.comments['TUNIT87']='none'
   hdulist[1].header.comments['TUNIT88']='none'
   hdulist[1].header.comments['TUNIT89']='physical unit of field'
   hdulist[1].header.comments['TUNIT90']='physical unit of field'
   hdulist[1].header.comments['TUNIT91']='physical unit of field'
   hdulist[1].header.comments['TUNIT92']='physical unit of field'
   hdulist[1].header.comments['TUNIT93']='physical unit of field'
   hdulist[1].header.comments['TUNIT94']='physical unit of field'


   hdulist[1].header.comments['TUNIT95']='none'
   hdulist[1].header.comments['TUNIT96']='none'
   hdulist[1].header.comments['TUNIT97']='physical unit of field'
   hdulist[1].header.comments['TUNIT98']='physical unit of field'
   hdulist[1].header.comments['TUNIT99']='physical unit of field'
   hdulist[1].header.comments['TUNIT100']='physical unit of field'
   hdulist[1].header.comments['TUNIT101']='physical unit of field'
   hdulist[1].header.comments['TUNIT102']='physical unit of field'
   hdulist[1].header.comments['TUNIT103']='physical unit of field'
   hdulist[1].header.comments['TUNIT104']='physical unit of field'
   hdulist[1].header.comments['TUNIT105']='physical unit of field'
   hdulist[1].header.comments['TUNIT106']='physical unit of field'
   hdulist[1].header.comments['TUNIT107']='physical unit of field'
   hdulist[1].header.comments['TUNIT108']='physical unit of field'



# TLMIN

   hdulist[1].header.set('TLMIN1','','',after='TUNIT1')
   hdulist[1].header.set('TLMIN2','','',after='TUNIT2')
   hdulist[1].header.set('TLMIN3','','',after='TUNIT3')
   hdulist[1].header.set('TLMIN4','','',after='TUNIT4')
   hdulist[1].header.set('TLMIN5','','',after='TUNIT5')
   hdulist[1].header.set('TLMIN6','','',after='TUNIT6')
   hdulist[1].header.set('TLMIN7',1.0,'Minimum value expected for field',after='TUNIT7')
   hdulist[1].header.set('TLMIN8','','',after='TUNIT8')
   hdulist[1].header.set('TLMIN9','','',after='TUNIT9')
   hdulist[1].header.set('TLMIN10','','',after='TUNIT10')
   hdulist[1].header.set('TLMIN11','','',after='TUNIT11')

   hdulist[1].header.set('TLMIN12','','',after='TUNIT12')
   hdulist[1].header.set('TLMIN13','','',after='TUNIT13')
   hdulist[1].header.set('TLMIN14',0.0,'Minimum value expected for field',after='TUNIT14')
   hdulist[1].header.set('TLMIN15',-90.0,'Minimum value expected for field',after='TUNIT15')
   hdulist[1].header.set('TLMIN16',2015.5,'Minimum value expected for field',after='TUNIT16')
   hdulist[1].header.set('TLMIN17','','',after='TUNIT17')
   hdulist[1].header.set('TLMIN18',0.0,'Minimum value expected for field',after='TUNIT18')
   hdulist[1].header.set('TLMIN19','','',after='TUNIT19')
   hdulist[1].header.set('TLMIN20',0.0,'Minimum value expected for field',after='TUNIT20')
   hdulist[1].header.set('TLMIN21','','',after='TUNIT21')
   hdulist[1].header.set('TLMIN22',0.0,'Minimum value expected for field',after='TUNIT22')

   hdulist[1].header.set('TLMIN23',1,'Minimum value expected for field',after='TUNIT23')
   hdulist[1].header.set('TLMIN24','','',after='TUNIT24')
   hdulist[1].header.set('TLMIN25',-180.0,'Minimum value expected for field',after='TUNIT25')
   hdulist[1].header.set('TLMIN26',-3,'Minimum value expected for field',after='TUNIT26')

   hdulist[1].header.set('TLMIN27','','',after='TUNIT27')
   hdulist[1].header.set('TLMIN28',0.0,'Minimum value expected for field',after='TUNIT28')
   hdulist[1].header.set('TLMIN29','','',after='TUNIT29')
   hdulist[1].header.set('TLMIN30',0.0,'Minimum value expected for field',after='TUNIT30')
   hdulist[1].header.set('TLMIN31','','',after='TUNIT31')
   hdulist[1].header.set('TLMIN32',0.0,'Minimum value expected for field',after='TUNIT32')

   hdulist[1].header.set('TLMIN33','','',after='TUNIT33')
   hdulist[1].header.set('TLMIN34',0.0,'Minimum value expected for field',after='TUNIT34')
   hdulist[1].header.set('TLMIN35','','',after='TUNIT35')
   hdulist[1].header.set('TLMIN36',0.0,'Minimum value expected for field',after='TUNIT36')
   hdulist[1].header.set('TLMIN37','','',after='TUNIT37')
   hdulist[1].header.set('TLMIN38',0.0,'Minimum value expected for field',after='TUNIT38')

   hdulist[1].header.set('TLMIN39',0.0,'Minimum value expected for field',after='TUNIT39')
   hdulist[1].header.set('TLMIN40',0.0,'Minimum value expected for field',after='TUNIT40')
   hdulist[1].header.set('TLMIN41','','',after='TUNIT41')
   hdulist[1].header.set('TLMIN42',0.0,'Minimum value expected for field',after='TUNIT42')
   hdulist[1].header.set('TLMIN43','','',after='TUNIT43')
   hdulist[1].header.set('TLMIN44',0,'Minimum value expected for field',after='TUNIT44')
   hdulist[1].header.set('TLMIN45',0.0,'Minimum value expected for field',after='TUNIT45')
   hdulist[1].header.set('TLMIN46',0.0,'Minimum value expected for field',after='TUNIT46')
   hdulist[1].header.set('TLMIN47',0,'Minimum value expected for field',after='TUNIT47')
   hdulist[1].header.set('TLMIN48',0,'Minimum value expected for field',after='TUNIT48')
   hdulist[1].header.set('TLMIN49',0,'Minimum value expected for field',after='TUNIT49')
   hdulist[1].header.set('TLMIN50',0,'Minimum value expected for field',after='TUNIT50')
   hdulist[1].header.set('TLMIN51',0,'Minimum value expected for field',after='TUNIT51')
   hdulist[1].header.set('TLMIN52',0,'Minimum value expected for field',after='TUNIT52')
   hdulist[1].header.set('TLMIN53',0.0,'Minimum value expected for field',after='TUNIT53')
   hdulist[1].header.set('TLMIN54',0.0,'Minimum value expected for field',after='TUNIT54')
   hdulist[1].header.set('TLMIN55',0,'Minimum value expected for field',after='TUNIT55')
   hdulist[1].header.set('TLMIN56',0,'Minimum value expected for field',after='TUNIT56')
   hdulist[1].header.set('TLMIN57',0.0,'Minimum value expected for field',after='TUNIT57')
   hdulist[1].header.set('TLMIN58',0,'Minimum value expected for field',after='TUNIT58')
   hdulist[1].header.set('TLMIN59',0,'Minimum value expected for field',after='TUNIT59')
   hdulist[1].header.set('TLMIN60',0,'Minimum value expected for field',after='TUNIT60')
   hdulist[1].header.set('TLMIN61',0,'Minimum value expected for field',after='TUNIT61')
   hdulist[1].header.set('TLMIN62','','',after='TUNIT62')
   hdulist[1].header.set('TLMIN63','','',after='TUNIT63')
   hdulist[1].header.set('TLMIN64','','',after='TUNIT64')
   hdulist[1].header.set('TLMIN65',0,'Minimum value expected for field',after='TUNIT65')
   hdulist[1].header.set('TLMIN66','','',after='TUNIT66')
   hdulist[1].header.set('TLMIN67',0.0,'Minimum value expected for field',after='TUNIT67')
   hdulist[1].header.set('TLMIN68',-90.0,'Minimum value expected for field',after='TUNIT68')
   hdulist[1].header.set('TLMIN69','','',after='TUNIT69')


   hdulist[1].header.set('TLMIN70',-90.0,'Minimum value expected for field',after='TUNIT70')
   hdulist[1].header.set('TLMIN71',0.0,'Minimum value expected for field',after='TUNIT71')

   hdulist[1].header.set('TLMIN72','','',after='TUNIT72')
   hdulist[1].header.set('TLMIN73','','',after='TUNIT73')
   hdulist[1].header.set('TLMIN74','','',after='TUNIT74')
   hdulist[1].header.set('TLMIN75',0.0,'Minimum value expected for field',after='TUNIT75')
   hdulist[1].header.set('TLMIN76','','',after='TUNIT76')
   hdulist[1].header.set('TLMIN77',0.0,'Minimum value expected for field',after='TUNIT77')
   hdulist[1].header.set('TLMIN78','','',after='TUNIT78')
   hdulist[1].header.set('TLMIN79',0.0,'Minimum value expected for field',after='TUNIT79')
   hdulist[1].header.set('TLMIN80','','',after='TUNIT80')
   hdulist[1].header.set('TLMIN81',0.0,'Minimum value expected for field',after='TUNIT81')
   hdulist[1].header.set('TLMIN82','','',after='TUNIT82')
   hdulist[1].header.set('TLMIN83',0.0,'Minimum value expected for field',after='TUNIT83')
   hdulist[1].header.set('TLMIN84','','',after='TUNIT84')
   hdulist[1].header.set('TLMIN85',0.0,'Minimum value expected for field',after='TUNIT85')


   hdulist[1].header.set('TLMIN86','','',after='TUNIT86')
   hdulist[1].header.set('TLMIN87','','',after='TUNIT87')
   hdulist[1].header.set('TLMIN88','','',after='TUNIT88')
   hdulist[1].header.set('TLMIN89','','',after='TUNIT89')
   hdulist[1].header.set('TLMIN90',0.0,'Minimum value expected for field',after='TUNIT90')
   hdulist[1].header.set('TLMIN91','','',after='TUNIT91')
   hdulist[1].header.set('TLMIN92',0.0,'Minimum value expected for field',after='TUNIT92')
   hdulist[1].header.set('TLMIN93','','',after='TUNIT93')
   hdulist[1].header.set('TLMIN94',0.0,'Minimum value expected for field',after='TUNIT94')
  


   hdulist[1].header.set('TLMIN95','','',after='TUNIT95')
   hdulist[1].header.set('TLMIN96','','',after='TUNIT96')
   hdulist[1].header.set('TLMIN97','','',after='TUNIT97')
   hdulist[1].header.set('TLMIN98',0.0,'Minimum value expected for field',after='TUNIT98')
   hdulist[1].header.set('TLMIN99','','',after='TUNIT99')
   hdulist[1].header.set('TLMIN100',0.0,'Minimum value expected for field',after='TUNIT100')
   hdulist[1].header.set('TLMIN101','','',after='TUNIT101')
   hdulist[1].header.set('TLMIN102',0.0,'Minimum value expected for field',after='TUNIT102')
   hdulist[1].header.set('TLMIN103','','',after='TUNIT103')
   hdulist[1].header.set('TLMIN104',0.0,'Minimum value expected for field',after='TUNIT104')
   hdulist[1].header.set('TLMIN105','','',after='TUNIT105')
   hdulist[1].header.set('TLMIN106',0.0,'Minimum value expected for field',after='TUNIT106')
   hdulist[1].header.set('TLMIN107','','',after='TUNIT107')
   hdulist[1].header.set('TLMIN108',0.0,'Minimum value expected for field',after='TUNIT108')



  

# TLMAX


   hdulist[1].header.set('TLMAX1','','',after='TLMIN1')
   hdulist[1].header.set('TLMAX2','','',after='TLMIN2')
   hdulist[1].header.set('TLMAX3','','',after='TLMIN3')
   hdulist[1].header.set('TLMAX4','','',after='TLMIN4')
   hdulist[1].header.set('TLMAX5','','',after='TLMIN5')
   hdulist[1].header.set('TLMAX6','','',after='TLMIN6')
   hdulist[1].header.set('TLMAX7',10.0,'Maximum value expected for field',after='TLMIN7')
   hdulist[1].header.set('TLMAX8','','',after='TLMIN8')
   hdulist[1].header.set('TLMAX9','','',after='TLMIN9')
   hdulist[1].header.set('TLMAX10','','',after='TLMIN10')
   hdulist[1].header.set('TLMAX11','','',after='TLMIN11')

   hdulist[1].header.set('TLMAX12','','',after='TLMIN12')
   hdulist[1].header.set('TLMAX13','','',after='TLMIN13')
   hdulist[1].header.set('TLMAX14',360.0,'Maximum value expected for field',after='TLMIN14')
   hdulist[1].header.set('TLMAX15',90.0,'Maximum value expected for field',after='TLMIN15')
   hdulist[1].header.set('TLMAX16',2016.0,'Maximum value expected for field',after='TLMIN16')
   hdulist[1].header.set('TLMAX17','','',after='TLMIN17')
   hdulist[1].header.set('TLMAX18','','',after='TLMIN18')
   hdulist[1].header.set('TLMAX19','','',after='TLMIN19')
   hdulist[1].header.set('TLMAX20','','',after='TLMIN20')
   hdulist[1].header.set('TLMAX21','','',after='TLMIN21')
   hdulist[1].header.set('TLMAX22','','',after='TLMIN22')

   hdulist[1].header.set('TLMAX23',12288,'Maximum value expected for field',after='TLMIN23')
   hdulist[1].header.set('TLMAX24','','',after='TLMIN24')
   hdulist[1].header.set('TLMAX25',180.0,'Maximum value expected for field',after='TLMIN25')
   hdulist[1].header.set('TLMAX26',6,'Maximum value expected for field',after='TLMIN26')

   hdulist[1].header.set('TLMAX27','','',after='TLMIN27')
   hdulist[1].header.set('TLMAX28','','',after='TLMIN28')
   hdulist[1].header.set('TLMAX29','','',after='TLMIN29')
   hdulist[1].header.set('TLMAX30','','',after='TLMIN30')
   hdulist[1].header.set('TLMAX31','','',after='TLMIN31')
   hdulist[1].header.set('TLMAX32','','',after='TLMIN32')

   hdulist[1].header.set('TLMAX33','','',after='TLMIN33')
   hdulist[1].header.set('TLMAX34','','',after='TLMIN34')
   hdulist[1].header.set('TLMAX35','','',after='TLMIN35')
   hdulist[1].header.set('TLMAX36','','',after='TLMIN36')
   hdulist[1].header.set('TLMAX37','','',after='TLMIN37')
   hdulist[1].header.set('TLMAX38','','',after='TLMIN38')

   hdulist[1].header.set('TLMAX39','','',after='TLMIN39')
   hdulist[1].header.set('TLMAX40','','',after='TLMIN40')
   hdulist[1].header.set('TLMAX41','','',after='TLMIN41')
   hdulist[1].header.set('TLMAX42','','',after='TLMIN42')
   hdulist[1].header.set('TLMAX43','','',after='TLMIN43')
   hdulist[1].header.set('TLMAX44',1,'Maximum value expected for field',after='TLMIN44')
   hdulist[1].header.set('TLMAX45','','',after='TLMIN45')
   hdulist[1].header.set('TLMAX46','','',after='TLMIN46')
   hdulist[1].header.set('TLMAX47','','',after='TLMIN47')
   hdulist[1].header.set('TLMAX48','','',after='TLMIN48')
   hdulist[1].header.set('TLMAX49','','',after='TLMIN49')
   hdulist[1].header.set('TLMAX50','','',after='TLMIN50')
   hdulist[1].header.set('TLMAX51',2,'Maximum value expected for field',after='TLMIN51')
   hdulist[1].header.set('TLMAX52',1,'Maximum value expected for field',after='TLMIN52')
   hdulist[1].header.set('TLMAX53',1.0,'Maximum value expected for field',after='TLMIN53')
   hdulist[1].header.set('TLMAX54',1.0,'Maximum value expected for field',after='TLMIN54')
   hdulist[1].header.set('TLMAX55',1,'Maximum value expected for field',after='TLMIN55')
   hdulist[1].header.set('TLMAX56',1,'Maximum value expected for field',after='TLMIN56')
   hdulist[1].header.set('TLMAX57',1000.0,'Maximum value expected for field',after='TLMIN57')
   hdulist[1].header.set('TLMAX58','','',after='TLMIN58')
   hdulist[1].header.set('TLMAX59','','',after='TLMIN59')
   hdulist[1].header.set('TLMAX60','','',after='TLMIN60')
   hdulist[1].header.set('TLMAX61',1,'Maximum value expected for field',after='TLMIN61')
   hdulist[1].header.set('TLMAX62','','',after='TLMIN62')
   hdulist[1].header.set('TLMAX63','','',after='TLMIN63')
   hdulist[1].header.set('TLMAX64','','',after='TLMIN64')
   hdulist[1].header.set('TLMAX65',1,'Maximum value expected for field',after='TLMIN65')
   hdulist[1].header.set('TLMAX66','','',after='TLMIN66')
   hdulist[1].header.set('TLMAX67',360.0,'Maximum value expected for field',after='TLMIN67')
   hdulist[1].header.set('TLMAX68',90.0,'Maximum value expected for field',after='TLMIN68')
   hdulist[1].header.set('TLMAX69','','',after='TLMIN69')


   hdulist[1].header.set('TLMAX70',90.0,'Maximum value expected for field',after='TLMIN70')
   hdulist[1].header.set('TLMAX71',360.0,'Maximum value expected for field',after='TLMIN71')

   hdulist[1].header.set('TLMAX72','','',after='TLMIN72')
   hdulist[1].header.set('TLMAX73','','',after='TLMIN73')
   hdulist[1].header.set('TLMAX74','','',after='TLMIN74')
   hdulist[1].header.set('TLMAX75','','',after='TLMIN75')
   hdulist[1].header.set('TLMAX76','','',after='TLMIN76')
   hdulist[1].header.set('TLMAX77','','',after='TLMIN77')
   hdulist[1].header.set('TLMAX78','','',after='TLMIN78')
   hdulist[1].header.set('TLMAX79','','',after='TLMIN79')
   hdulist[1].header.set('TLMAX80','','',after='TLMIN80')
   hdulist[1].header.set('TLMAX81','','',after='TLMIN81')
   hdulist[1].header.set('TLMAX82','','',after='TLMIN82')
   hdulist[1].header.set('TLMAX83','','',after='TLMIN83')
   hdulist[1].header.set('TLMAX84','','',after='TLMIN84')
   hdulist[1].header.set('TLMAX85','','',after='TLMIN85')

   hdulist[1].header.set('TLMAX86','','',after='TLMIN86')
   hdulist[1].header.set('TLMAX87','','',after='TLMIN87')
   hdulist[1].header.set('TLMAX88','','',after='TLMIN88')
   hdulist[1].header.set('TLMAX89','','',after='TLMIN89')
   hdulist[1].header.set('TLMAX90','','',after='TLMIN90')
   hdulist[1].header.set('TLMAX91','','',after='TLMIN91')
   hdulist[1].header.set('TLMAX92','','',after='TLMIN92')
   hdulist[1].header.set('TLMAX93','','',after='TLMIN93')
   hdulist[1].header.set('TLMAX94','','',after='TLMIN94')


   hdulist[1].header.set('TLMAX95','','',after='TLMIN95')
   hdulist[1].header.set('TLMAX96','','',after='TLMIN96')
   hdulist[1].header.set('TLMAX97','','',after='TLMIN97')
   hdulist[1].header.set('TLMAX98','','',after='TLMIN98')
   hdulist[1].header.set('TLMAX99','','',after='TLMIN99')
   hdulist[1].header.set('TLMAX100','','',after='TLMIN100')
   hdulist[1].header.set('TLMAX101','','',after='TLMIN101')
   hdulist[1].header.set('TLMAX102','','',after='TLMIN102')
   hdulist[1].header.set('TLMAX103','','',after='TLMIN103')
   hdulist[1].header.set('TLMAX104','','',after='TLMIN104')
   hdulist[1].header.set('TLMAX105','','',after='TLMIN105')
   hdulist[1].header.set('TLMAX106','','',after='TLMIN106')
   hdulist[1].header.set('TLMAX107','','',after='TLMIN107')
   hdulist[1].header.set('TLMAX108','','',after='TLMIN108')











# Header information not required

 


   del hdulist[1].header['TUNIT1']
   del hdulist[1].header['TUNIT2']
   del hdulist[1].header['TUNIT3']
   del hdulist[1].header['TUNIT4']
   del hdulist[1].header['TUNIT5']
   del hdulist[1].header['TUNIT6']
   del hdulist[1].header['TUNIT7']
   del hdulist[1].header['TUNIT8']
   del hdulist[1].header['TUNIT9']
   del hdulist[1].header['TUNIT10']
   del hdulist[1].header['TUNIT11']
   del hdulist[1].header['TUNIT12']
   del hdulist[1].header['TUNIT13']
   del hdulist[1].header['TUNIT23']
   del hdulist[1].header['TUNIT24']
   del hdulist[1].header['TUNIT26']
   del hdulist[1].header['TUNIT41']
   del hdulist[1].header['TUNIT43']
   del hdulist[1].header['TUNIT44']
   del hdulist[1].header['TUNIT47']
   del hdulist[1].header['TUNIT48']
   del hdulist[1].header['TUNIT49']
   del hdulist[1].header['TUNIT50']
   del hdulist[1].header['TUNIT51']
   del hdulist[1].header['TUNIT52']
   del hdulist[1].header['TUNIT53']
   del hdulist[1].header['TUNIT54']
   del hdulist[1].header['TUNIT55']
   del hdulist[1].header['TUNIT56']
   del hdulist[1].header['TUNIT58']
   del hdulist[1].header['TUNIT59']
   del hdulist[1].header['TUNIT60']
   del hdulist[1].header['TUNIT61']
   del hdulist[1].header['TUNIT62']
   del hdulist[1].header['TUNIT63']
   del hdulist[1].header['TUNIT64']
   del hdulist[1].header['TUNIT65']
   del hdulist[1].header['TUNIT66']
   del hdulist[1].header['TUNIT69']
   del hdulist[1].header['TUNIT72']
   del hdulist[1].header['TUNIT73']
   del hdulist[1].header['TUNIT86']
   del hdulist[1].header['TUNIT87']
   del hdulist[1].header['TUNIT88']
   del hdulist[1].header['TUNIT95']
   del hdulist[1].header['TUNIT96']


   del hdulist[1].header['TLMIN1']
   del hdulist[1].header['TLMIN2']
   del hdulist[1].header['TLMIN3']
   del hdulist[1].header['TLMIN4']
   del hdulist[1].header['TLMIN5']
   del hdulist[1].header['TLMIN6']
   del hdulist[1].header['TLMIN8']
   del hdulist[1].header['TLMIN9']
   del hdulist[1].header['TLMIN10']
   del hdulist[1].header['TLMIN11']
   del hdulist[1].header['TLMIN12']
   del hdulist[1].header['TLMIN13']
   del hdulist[1].header['TLMIN17']
   del hdulist[1].header['TLMIN19']
   del hdulist[1].header['TLMIN21']
   del hdulist[1].header['TLMIN24']
   del hdulist[1].header['TLMIN27']
   del hdulist[1].header['TLMIN29']
   del hdulist[1].header['TLMIN31']
   del hdulist[1].header['TLMIN33']
   del hdulist[1].header['TLMIN35']
   del hdulist[1].header['TLMIN37']
   del hdulist[1].header['TLMIN41']
   del hdulist[1].header['TLMIN43']
   del hdulist[1].header['TLMIN62']
   del hdulist[1].header['TLMIN63']
   del hdulist[1].header['TLMIN64']
   del hdulist[1].header['TLMIN66']
   del hdulist[1].header['TLMIN69']
   del hdulist[1].header['TLMIN72']
   del hdulist[1].header['TLMIN73']
   del hdulist[1].header['TLMIN74']
   del hdulist[1].header['TLMIN76']
   del hdulist[1].header['TLMIN78']
   del hdulist[1].header['TLMIN80']
   del hdulist[1].header['TLMIN82']
   del hdulist[1].header['TLMIN84']
   del hdulist[1].header['TLMIN86']
   del hdulist[1].header['TLMIN87']
   del hdulist[1].header['TLMIN88']
   del hdulist[1].header['TLMIN89']
   del hdulist[1].header['TLMIN91']
   del hdulist[1].header['TLMIN93']
   del hdulist[1].header['TLMIN95']
   del hdulist[1].header['TLMIN96']
   del hdulist[1].header['TLMIN97']
   del hdulist[1].header['TLMIN99']
   del hdulist[1].header['TLMIN101']
   del hdulist[1].header['TLMIN103']
   del hdulist[1].header['TLMIN105']
   del hdulist[1].header['TLMIN107']


   del hdulist[1].header['TLMAX1']
   del hdulist[1].header['TLMAX2']
   del hdulist[1].header['TLMAX3']
   del hdulist[1].header['TLMAX4']
   del hdulist[1].header['TLMAX5']
   del hdulist[1].header['TLMAX6']
   del hdulist[1].header['TLMAX8']
   del hdulist[1].header['TLMAX9']
   del hdulist[1].header['TLMAX10']
   del hdulist[1].header['TLMAX11']
   del hdulist[1].header['TLMAX12']
   del hdulist[1].header['TLMAX13']
   del hdulist[1].header['TLMAX17']
   del hdulist[1].header['TLMAX18']
   del hdulist[1].header['TLMAX19']
   del hdulist[1].header['TLMAX20']
   del hdulist[1].header['TLMAX21']
   del hdulist[1].header['TLMAX22']
   del hdulist[1].header['TLMAX24']
   del hdulist[1].header['TLMAX27']
   del hdulist[1].header['TLMAX28']
   del hdulist[1].header['TLMAX29']
   del hdulist[1].header['TLMAX30']
   del hdulist[1].header['TLMAX31']
   del hdulist[1].header['TLMAX32']
   del hdulist[1].header['TLMAX33']
   del hdulist[1].header['TLMAX34']
   del hdulist[1].header['TLMAX35']
   del hdulist[1].header['TLMAX36']
   del hdulist[1].header['TLMAX37']
   del hdulist[1].header['TLMAX38']
   del hdulist[1].header['TLMAX39']
   del hdulist[1].header['TLMAX40']
   del hdulist[1].header['TLMAX41']
   del hdulist[1].header['TLMAX42']
   del hdulist[1].header['TLMAX43']
   del hdulist[1].header['TLMAX45']
   del hdulist[1].header['TLMAX46']
   del hdulist[1].header['TLMAX47']
   del hdulist[1].header['TLMAX48']
   del hdulist[1].header['TLMAX49']
   del hdulist[1].header['TLMAX50']
   del hdulist[1].header['TLMAX58']
   del hdulist[1].header['TLMAX59']
   del hdulist[1].header['TLMAX60']
   del hdulist[1].header['TLMAX62']
   del hdulist[1].header['TLMAX63']
   del hdulist[1].header['TLMAX64']
   del hdulist[1].header['TLMAX66']
   del hdulist[1].header['TLMAX69']
   del hdulist[1].header['TLMAX72']
   del hdulist[1].header['TLMAX73']
   del hdulist[1].header['TLMAX74']
   del hdulist[1].header['TLMAX75']
   del hdulist[1].header['TLMAX76']
   del hdulist[1].header['TLMAX77']
   del hdulist[1].header['TLMAX78']
   del hdulist[1].header['TLMAX79']
   del hdulist[1].header['TLMAX80']
   del hdulist[1].header['TLMAX81']
   del hdulist[1].header['TLMAX82']
   del hdulist[1].header['TLMAX83']
   del hdulist[1].header['TLMAX84']
   del hdulist[1].header['TLMAX85']
   del hdulist[1].header['TLMAX86']
   del hdulist[1].header['TLMAX87']
   del hdulist[1].header['TLMAX88']
   del hdulist[1].header['TLMAX89']
   del hdulist[1].header['TLMAX90']
   del hdulist[1].header['TLMAX91']
   del hdulist[1].header['TLMAX92']
   del hdulist[1].header['TLMAX93']
   del hdulist[1].header['TLMAX94']
   del hdulist[1].header['TLMAX95']
   del hdulist[1].header['TLMAX96']
   del hdulist[1].header['TLMAX97']
   del hdulist[1].header['TLMAX98']
   del hdulist[1].header['TLMAX99']
   del hdulist[1].header['TLMAX100']
   del hdulist[1].header['TLMAX101']
   del hdulist[1].header['TLMAX102']
   del hdulist[1].header['TLMAX103']
   del hdulist[1].header['TLMAX104']
   del hdulist[1].header['TLMAX105']
   del hdulist[1].header['TLMAX106']
   del hdulist[1].header['TLMAX107']
   del hdulist[1].header['TLMAX108']





   hdulist.writeto(filename,overwrite=True,checksum=True)







if __name__ == '__main__':

 pass


