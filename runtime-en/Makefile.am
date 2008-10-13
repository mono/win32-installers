MODULE = Runtime
CANDLE_FLAGS = -ext WixUIExtension
LIGHT_FLAGS = -cultures:en-us -ext WixUIExtension

noinst_DATA = $(MODULE).msm

$(MODULE).msm: $(MODULE).wxs
	candle $(CANDLE_FLAGS) $(MODULE).wxs
	light $(LIGHT_FLAGS) $(MODULE).wixobj
