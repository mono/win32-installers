MODULE = poppler-lib
CANDLE_FLAGS = 
LIGHT_FLAGS = 

noinst_DATA = $(MODULE).msm

$(MODULE).msm: $(MODULE).wxs
	candle $(CANDLE_FLAGS) $(MODULE).wxs
	light $(LIGHT_FLAGS) $(MODULE).wixobj

CLEANFILES = \
	$(MODULES).wixobj \
	$(MODULES).msm
