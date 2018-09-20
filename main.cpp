#include <pspkernel.h>
#include <pspdisplay.h>
#include <pspdebug.h>
#include <psprtc.h>
#include <pspctrl.h>
#include "glib2d.h"

PSP_MODULE_INFO("ikezawa graphics test", 0, 0, 2);

int exit_callback(int arg1, int arg2, void *common)
{
  sceKernelExitGame();	
  return 0;
}

int CallbackThread(SceSize args, void *argp)
{
  int cbid;
  cbid = sceKernelCreateCallback("Exit Callback", exit_callback, NULL);
  sceKernelRegisterExitCallback(cbid);
  sceKernelSleepThreadCB();
  return 0;
}

int SetupCallbacks(void)
{
  int thid = 0;
  thid = sceKernelCreateThread("update_thread", CallbackThread, 0x11, 0xFA0, 0, 0);
  if(thid >= 0) {	
    sceKernelStartThread(thid, 0, 0);
  }
  return thid;	
}

int main()
{
  // INITIALIZE
  SetupCallbacks();
  // ADD SCENE STUFF
  g2dTexture* bg = g2dTexLoad("game/event/lilly_train/train_scenery.jpg", G2D_SWIZZLE);
  g2dTexture* pole = g2dTexLoad("game/event/lilly_train/train_scenery_fg.png", G2D_SWIZZLE);
  g2dTexture* fg = g2dTexLoad("game/event/lilly_train/lilly_trainride.png", G2D_SWIZZLE);
  float bg_x = 0, pole_x = 0;
  u64 last_tick, curr_tick;
	sceRtcGetCurrentTick(&last_tick);
	u32 tick_frequency = sceRtcGetTickResolution();
	int framecount = 0;
  float curr_fps = 0.0f, curr_ms = 1.0f;
  // LOOP
  while(1){
    curr_fps = 1.0f / curr_ms;
    g2dClear(BLACK);	// CLEAR SCREEN
    // DRAW BG
    if (bg == NULL) bg_x = 0;
    else{
      if (bg_x <= -((bg->w) - 480.0f)) bg_x = 0;
      else bg_x -= ((bg->w) - 480.0f) * (2.0f / curr_fps);
    }
    g2dBeginRects(bg);
    if (bg == NULL) g2dSetColor(BLUE);
    g2dSetCoordMode(G2D_UP_LEFT);
    g2dSetAlpha(255);
    g2dSetScaleWH(bg == NULL ? 480 : bg->w, bg == NULL ? 272 : bg->h);
    g2dSetCoordXY(bg_x, 0);
    g2dAdd();
    g2dEnd();
    g2dFlip(G2D_VSYNC);	// FLIP SCREEN
    ++framecount;
    sceRtcGetCurrentTick(&curr_tick);
		if ((curr_tick-last_tick) >= tick_frequency)
		{
			float time_span = ((int)(curr_tick-last_tick)) / (float)tick_frequency;
			curr_ms = time_span / framecount;

			framecount = 0;
			sceRtcGetCurrentTick(&last_tick);
		}
  }
  sceKernelExitGame();
  return 0;
}
