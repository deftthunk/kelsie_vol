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

