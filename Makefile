PSPPRE = $(shell psp-config --psp-prefix)
PSPDEV = $(shell psp-config --pspdev-path)
PSPSDK = $(shell psp-config --pspsdk-path)
PSPBIN = $(PSPDEV)/bin
#SDL_CONFIG = $(PSPBIN)/sdl-config

OBJS   = main.o glib2d.o

INCDIR   =
CFLAGS   = -G0 -Wall -O2 -g #-D PSP #-Wextra
CXXFLAGS = $(CFLAGS) -fno-exceptions -fno-rtti
ASFLAGS  = $(CFLAGS)

#CFLAGS += $(shell $(SDL_CONFIG) --cflags)

LIBDIR  =
LDFLAGS =
LIBS    = -lpng -ljpeg -lz -lpspgum -lpspgu -lpsprtc -lm -lpspvram 

BUILD_PRX = 1 

EXTRA_TARGETS   = EBOOT.PBP
PSP_EBOOT_TITLE = Katawa Shoujo
#PSP_FW_VERSION = 371
PSP_EBOOT_SFO = metadata/PARAM.SFO
PSP_EBOOT_ICON = metadata/ICON0.png
PSP_EBOOT_PIC1 = metadata/PIC1.png
#PSP_EBOOT_SND0= SND0.at3

include $(PSPSDK)/lib/build.mak