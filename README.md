# kelsie_vol
things and stuff

## instructions
1) clone repo (or download zip) and copy to local machine or VM
2) enter project folder
3) if you have a PyPi repo available, run
   ```
   pip3 install pip_requirements.txt
   ```
   if you don't have a repo available, this should still work, but certain plugins/modules won't be available (there are workarounds)
4) make sure volatility3 is available on the machine/vm
    - download: https://github.com/volatilityfoundation/volatility3
    - download symbols for Windows: https://downloads.volatilityfoundation.org/volatility3/symbols/windows.zip and place the ZIP in volatility3 folder at "volatility3/symbols"
    - unpack zip
    - put folder somewhere/anywhere and then 'cd' into the volatility3 folder
    - make it so that you can call 'vol.py' from anywhere by exporting its folder path:
       ```
       echo "export PATH=\$PATH:$(pwd)" >> ~/.bashrc
       ```
       the above command adds a line to your shell's startup script, to tell it to make the new path accessible. Close your terminal and open it again to make the change take effect.
    - verify 'vol.py' is reachable by trying to run it without being in the folder
       ```
       vol.py --help
       ```
       if that didn't work something went wrong. tell steven it's his fault with zero explanation as to why.
5) in a terminal (one that's been created after step 4), browse to this project's folder
6) run the script with no arguments, and it'll check to see if everything looks ready
   ```
   python kvol.py
   ```

## things to try later for fun (and profit?)
- get script to execute more than one command at a time to speed it up
- store output of each command in its own named file, instead of just in the log
- format output of program to be more useful for ingestion into other programs for post-processing
- handle more volatility flags/options than just '-o' and '-f'
- fill out more plugin arguments
- check to see if anything is in the output folder, and if so, create a new folder named something different to organize work
- determine with plugins are worth running all the time
- figure out how to work with plugins like 'windows.strings.String' which require a target strings file
- make plugin dictionaries for mac and linux
