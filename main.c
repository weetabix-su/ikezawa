#include <pspdisplay.h>
#include <pspdebug.h>
//#include <psprtc.h>
#include <pspctrl.h>
#include <math.h>
#include <unistd.h>
#include "glib2d.h"
#include "callbacks.h"

PSP_MODULE_INFO("Katawa Shoujo", 0, 1, 1);

int main(int argc, char *argv[])
{
  // INITIALIZE
  callbacks_setup();
  // ADD SCENE STUFF
  g2dTexture* bg = g2dTexLoad("game/event/lilly_train/train_scenery.jpg", G2D_SWIZZLE);
  g2dTexture* pole = g2dTexLoad("game/event/lilly_train/train_scenery_fg.png", G2D_SWIZZLE);
  g2dTexture* fg = g2dTexLoad("game/event/lilly_train/lilly_trainride.png", G2D_SWIZZLE);
  float bg_x = 0.0f, pole_x = 480.0f, fg_waveClock = 0;
  u64 last_tick, curr_tick;
	sceRtcGetCurrentTick(&last_tick);
	u32 tick_frequency = sceRtcGetTickResolution();
	int framecount = 0;
  float curr_ms = 0.0f;
  // LOOP
  while(1){
    g2dClear(WHITE);	// CLEAR SCREEN
    //DRAW BG
    if (bg == NULL) bg_x = 0;
    else{
      if (bg_x <= -725.0f) bg_x = 0;
      else bg_x -= 725.0f * (2.0f * curr_ms);
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
      else pole_x -= 5920 * (0.3f * curr_ms);
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
    else fg_waveClock += curr_ms;
    g2dBeginRects(fg);
    g2dSetCoordMode(G2D_UP_LEFT);
    g2dSetAlpha(fg == NULL ? 128 : 255);
    g2dSetScaleWH(fg == NULL ? 480 : fg->w, fg == NULL ? 272 : fg->h);
    g2dSetCoordXY(0, fg == NULL ? 0 : (-9) * (sin(fmod((fg_waveClock / 2.0f), 2) * M_PI) + 1.0f) / 2.0f);
    g2dAdd();
    g2dEnd();
    g2dFlip(G2D_VSYNC);
    // FLIP SCREEN
    ++framecount;
    sceRtcGetCurrentTick(&curr_tick);
    if ((curr_tick-last_tick) >= tick_frequency)
		{
			float time_span = ((float)(curr_tick-last_tick)) / (float)tick_frequency;
			curr_ms = time_span / framecount;

			framecount = 0;
			last_tick = curr_tick;
		}
  }
  sceKernelExitGame();
  return 0;
}
