#include "modules/modified_caen_v775.spec"
#include "modules/trloii.spec"
#include "modules/mesytec_vmmr8_mmr.spec"
#include "modules/mesytec_mdpp32.spec"
#include "modules/mesytec_madc32.spec"
#include "modules/gsi_vulom_scaler32.spec"

CUSTOM_HEADER(val)
{
	UINT32 header {
		0_31: v = MATCH(val);
	}
}

SUBEVENT(main_subev)
{
	header[0] = CUSTOM_HEADER(val=0xa0000000);
	vmmr8[0] = VME_MESYTEC_VMMR8(geom=0);
	
	header[1] = CUSTOM_HEADER(val=0xa0010000);
	vmmr8[1] = VME_MESYTEC_VMMR8(geom=1);
	
	header[2] = CUSTOM_HEADER(val=0xb0002016);
	mdpp32 = VME_MESYTEC_MDPP32(geom=0);
	
	header[3] = CUSTOM_HEADER(val=0xc0070901);
	v775 = VME_CAEN_V775(geom=0x1f, crate=0);
	
	header[4] = CUSTOM_HEADER(val=0xa1000241);
	madc32 = VME_MESYTEC_MADC32(geom=0);
	
	header[5] = CUSTOM_HEADER(val=0xc1000000);
	vscal = VME_GSI_VULOM_SCALER32(channels=32);
	
	tpat = TRLOII_TPAT(id=0xcf);
	lmu = TRLOII_LMU_SCALERS(id=0xc7);
}

EVENT
{
        main = main_subev(type=10, subtype=1, control=9);
}

#include "mapping.hh"
