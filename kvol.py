import os, sys
import subprocess

#---------------------------------------------

## folder to dump stuff for plugins which need it
output_folder = "/i/need/a/path"
## leave as empty string if not using. otherwise, remove string and use number
target_pid = ""
## where to save the screen output
log_file = "/path/to/log/file"
## show live output on screen?
show_scrolling_output = True


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

#---------------------------------------------

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


def get_mem_path():
    '''
    Retrieve the command line argument the user provided, which is a path to
    the memory capture image file.

    Command line args are stored in the list "sys.argv". First argument is at 
    position one, so 'sys.argv[1]'
    '''
    if len(sys.argv) > 1:
        path = sys.argv[1]
        ## check if path is valid by looking to see if there's a file there
        if not os.path.exists(path):
            print(f">> ERROR: unable to find file at {path}")
            sys.exit()

        return path
    else:
        print("\n>> No memory image specified, exiting")
        sys.exit()


def build_commands(mem_path):
    '''
    For each uncommented module in the dictionary "windows_plugin_dict", extract the
    key (plugin name) and value (plugin arguments), and use them to build a command
    to execute.

    Each formatted command will be stored in the list "commands", and printed out
    for user verification before being excuted.
    '''
    commands = []

    for plugin, plugin_args in windows_plugin_dict.items():
        ## if no plugin_args, leave it off (acts weird later in code if we don't)
        if plugin_args != "":
            temp_cmd = f"vol.py -f {mem_path} -o {output_folder} {plugin} {plugin_args}"
        else:
            temp_cmd = f"vol.py -f {mem_path} -o {output_folder} {plugin}"
        print(temp_cmd)
        commands.append(temp_cmd)
    
    ## check to see if the commands look good
    user_input = input("Proceed? y/n: ")
    if user_input == "y":
        return commands
    elif user_input == "n":
        print(">> Exiting based on user input")
        sys.exit()
    else:
        print("Did not understand response...exiting!")
        sys.exit()


def run_commands(commands):
    '''
    Use python's "subprocess" module to execute each command in Linux. subprocess.Popen()
    expects each command to be a list, so we have to split up each command by splitting 
    on the whitespace characters first, then feeding that list to Popen().

    It will run one command at a time, and results are retrieved from the "process" object
    we get back from Popen().
    '''
    if log_file != "":
        log_handle = open("log_file", "w")
    for cmd in commands:
        formatted_cmd = cmd.split(" ")
        print("> Running...")
        process = subprocess.Popen(formatted_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ## we will hang here waiting on this to return when vol.py finishes running
        std_out, std_err = process.communicate()
        
        ## display command output to screen
        if show_scrolling_output:
            print(std_out.decode("utf-8"))

        ## write output to log file
        log_handle.write(std_out.decode("utf-8"))
    

    ## cleanup by closing file handle
    log_handle.close()



def main():
    if check_path() == False:
        sys.exit()
    
    mem_capture_path = get_mem_path()
    command_list = build_commands(mem_capture_path)
    run_commands(command_list)    



## start here
main()