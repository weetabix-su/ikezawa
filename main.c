#include <pspkernel.h>
#include <pspdebug.h>

PSP_MODULE_INFO("Hello World", 0, 1, 0);

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
  pspDebugScreenInit();
  SetupCallbacks();
  pspDebugScreenPrintf("Hello internet!\n\nLet me be the first one to say that it's great to be back working on PSP stuff.\n\nThis port has been long overdue, and with the power of the actual SDK I hope to deliver a port that is as close to the original.\n\nThank you for your support.");
  sceKernelSleepThread();
  return 0;
}
