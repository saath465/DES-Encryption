//This is a support dll program to the main mal1007.exe program to inject into the process.
//The dll displays the message given below in the infected process.
#include <Windows.h>

BOOL APIENTRY DllMain(HMODULE hModule, DWORD  url_to_proc, LPVOID lpReserved)
{
	if (url_to_proc == DLL_PROCESS_ATTACH)
		MessageBox(0, L"I must have called a thousand times", L"Hello From The Other Side!!!!!!", MB_ICONHAND);

	return TRUE;
}