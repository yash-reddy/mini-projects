// A program to track the resources taken up by any specific video playing application. In hindsight, something along the lines of watch ps would've done the job.
// Anyways, this is a C++ program for those who might need it.

#include <windows.h>
#include <psapi.h>
#include<iostream>
#include<stdlib.h>

int main()
{
// appname is the exe file of the video player
    const char *appname ="C:\\Program Files (x86)\\GRETECH\\GOMPlayer\\GOM.exe";//"c:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe";//"C:\\Program Files (x86)\\DearMob\\5KPlayer\\5KPlayer.exe";//// "C:\\Program Files (x86)\\DivX\\DivX Player\\DivX Player.exe";//"C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe"; //
    const char *filename = "c:\\Users\\path\\to\\video.mp4"; //video file
STARTUPINFOA si;
    PROCESS_INFORMATION pi;
    memset(&si, 0, sizeof(si));
    si.cb = sizeof(si);
    memset(&pi, 0, sizeof(pi));

char buf[MAX_PATH + 300];
    wsprintfA(buf, "%s \"%s\" --play-and-exit", appname, filename);
    CreateProcessA(0, buf, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi);

PROCESS_MEMORY_COUNTERS_EX pmc;
int ctr=0;
SIZE_T virtualMemUsed,physicalMemUsed;

//set the number of measurements to be taken
while(ctr<10000)
{   Sleep(3000); //time interval between measurements
    GetProcessMemoryInfo(pi.hProcess,
    reinterpret_cast<PPROCESS_MEMORY_COUNTERS>(&pmc), sizeof(pmc));
physicalMemUsed = pmc.WorkingSetSize;
virtualMemUsed = pmc.PrivateUsage;
std::cout<<physicalMemUsed/(float)(1024*1024)<<"\t"<<virtualMemUsed/(float)(1024*1024)<<"\n";
ctr++;
}
return 0;
}
