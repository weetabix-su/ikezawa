#include <pspkernel.h>
#include <pspdebug.h>
#include "glib2d.h"

PSP_MODULE_INFO("ikezawa graphics test", 0, 0, 1);

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
  // ADD BACON
  g2dTexture* hana = g2dTexLoad("game/sprites/hanako/hanako_basic_normal_cas.png", G2D_SWIZZLE);
  // LOOP
  while(1){
    g2dClear(WHITE);	// CLEAR SCREEN
    // DRAW
    g2dBeginRects(hana);
    if (hana == NULL) g2dSetColor(RED);
    g2dSetCoordMode(G2D_CENTER);
    g2dSetAlpha(255);
    g2dSetScaleWH(hana == NULL ? 120 : hana->w, hana == NULL ? 272 : hana->h);
    g2dSetCoordXY(G2D_SCR_W/2, G2D_SCR_H/2);
    g2dAdd();
    g2dEnd();
    g2dFlip(G2D_VSYNC);	// FLIP SCREEN
  }
  sceKernelExitGame();
  return 0;
}
