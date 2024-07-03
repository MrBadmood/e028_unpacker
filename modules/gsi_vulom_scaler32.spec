// Jan Glorius
// 15.05.2024

VME_GSI_VULOM_SCALER32(channels)
{
  MEMBER(DATA32 data[32] ZERO_SUPPRESS);

  list(0<=index<channels)
    {
      UINT32 ch_data NOENCODE
	{
	  0_31:  value;

	  ENCODE(data[index],(value=value));
	}
    }
}


