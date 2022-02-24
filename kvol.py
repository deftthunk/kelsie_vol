from os.path import join
import os
import sys

## folder to dump stuff for plugins which need it
output_folder = "/home/user/..."
## leave as empty string if not using. otherwise, remove string and use number
target_pid = ""


'''
Python dictionary (key:value) of the plugins and their potential arguments.

Plugin name is the key, and value is an optional argument(s) for the plugin, 
such as the target_pid of interest. Arguments will be executed as formatted here.

To stop a plugin from running, just comment out its line.
'''
windows_plugin_dict = {
    "windows.bigpools.BigPools": "",
    "windows.cmdline.CmdLine": "",
#    "windows.crashinfo.Crashinfo": "",
    "windows.dlllist.DllList": "",
    "windows.driverirp.DriverIrp": "",
    "windows.driverscan.DriverScan": "",
#    "windows.dumpfiles.DumpFiles": "",
    "windows.envars.Envars": "",
    "windows.filescan.FileScan": "",
    "windows.getservicesids.GetServiceSIDs": "",
    "windows.getsids.GetSIDs": "",
    "windows.handles.Handles": "",
    "windows.info.Info": "",
    "windows.ldrmodules.LdrModules": f"--pid {target_pid}",
    "windows.malfind.Malfind": f"--pid {target_pid}",
#    "windows.memmap.Memmap": "",
    "windows.modscan.ModScan": "",
    "windows.modules.Modules": "",
    "windows.mutantscan.MutantScan": "",
#    "windows.poolscanner.PoolScanner": "",
    "windows.privileges.Privs": "",
    "windows.pslist.PsList": "",
    "windows.psscan.PsScan": "",
    "windows.pstree.PsTree": "",
    "windows.registry.certificates.Certificates": "",
    "windows.registry.hivelist.HiveList": "",
    "windows.registry.hivescan.HiveScan": "",
    "windows.registry.printkey.PrintKey": "",
    "windows.registry.userassist.UserAssist": "",
    "windows.sessions.Sessions": "",
    "windows.ssdt.SSDT": "",
#    "windows.statistics.Statistics": "",
#    "windows.strings.Strings": "",
    "windows.symlinkscan.SymlinkScan": "",
    "windows.vadinfo.VadInfo": f"--pid {target_pid}",
    "windows.virtmap.VirtMap": "",
}


def check_path():
    '''
    This function looks to see if the volatility folder location is in the linux "ENV"
    variable called "PATH", which hopefully was completed in the instructions.
    Linux programs find each other by searching for the program they want to run in 
    all the folders listed in PATH.
    '''
    success_flag = True

    print(">> checking for vol.py in PATH")
    linux_environment_vars = os.getenv("PATH")
    if linux_environment_vars.find("volatility") != -1:
        print(">> success!")
    else:
        print(">> failed to find a folder with the word 'volatility' in PATH")
        print(">> unable to continue, since idk where vol.py is")
        success_flag = False
    
    return success_flag


def main():
    if check_path() == False:
        sys.exit()
    

    




main()