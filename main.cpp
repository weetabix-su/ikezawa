#include <pspkernel.h>
#include <pspdisplay.h>
#include <pspdebug.h>
#include <psprtc.h>
#include <pspctrl.h>
#include <math.h>
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
  float bg_x = 0.0f, pole_x = 480.0f, fg_waveClock = 0;
  u64 last_tick, curr_tick;
	sceRtcGetCurrentTick(&last_tick);
	u32 tick_frequency = sceRtcGetTickResolution();
	int framecount = 0;
  float curr_fps = 0.0f, curr_ms = 0.0f;
  // LOOP
  while(1){
    curr_fps = 1.0f / curr_ms;
    g2dClear(WHITE);	// CLEAR SCREEN
    //DRAW BG
    if (bg == NULL) bg_x = 0;
    else{
      if (bg_x <= -725.0f) bg_x = 0;
      else bg_x -= 725.0f * (2.0f / curr_fps);
    }
    g2dBeginRects(bg);
    if (bg == NULL) g2dSetColor(BLUE);
    g2dSetCoordMode(G2D_UP_LEFT);
    g2dSetAlpha(255);
    g2dSetScaleWH(bg == NULL ? 480 : 1205, 272);
    g2dSetCoordXY(bg_x, 0);
    g2dAdd();
    g2dEnd();
    //DRAW POLE
    if (pole == NULL) pole_x = 480.0f;
    else{
      if (pole_x <= -5920) pole_x = 480.0f;
      else pole_x -= 5920 * (0.3f / curr_fps);
    }
    g2dBeginRects(pole);
    if (pole == NULL) g2dSetColor(ORANGE);
    g2dSetCoordMode(G2D_UP_LEFT);
    g2dSetAlpha(255);
    g2dSetScaleWH(55, 272);
    g2dSetCoordXY(pole_x, 0);
    g2dAdd();
    g2dEnd();
    //DRAW FG
    if (fg_waveClock >= 4.0f) fg_waveClock = 0.0f;
    else fg_waveClock += (1.0f / curr_fps);
    g2dBeginRects(fg);
    g2dSetCoordMode(G2D_UP_LEFT);
    g2dSetAlpha(fg == NULL ? 128 : 255);
    g2dSetScaleWH(fg == NULL ? 480 : fg->w, fg == NULL ? 272 : fg->h);
    g2dSetCoordXY(0, fg == NULL ? 0 : (-9) * (sin(fmod((fg_waveClock / 2.0f), 2) * M_PI) + 1.0f) / 2.0f);
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
