import colorama
from colorama import Fore,Back,Style
colorama.init()

mensajito = """
  _____   _         ____    ____     ___    _____   _____     ____    ___   _____      _    
 | ____| | |       |  _ \  |  _ \   / _ \  |  ___| | ____|   |  _ \  |_ _| |  ___|    / \   
 |  _|   | |       | |_) | | |_) | | | | | | |_    |  _|     | |_) |  | |  | |_      / _ \  
 | |___  | |___    |  __/  |  _ <  | |_| | |  _|   | |___    |  _ <   | |  |  _|    / ___ \ 
 |_____| |_____|   |_|     |_| \_\  \___/  |_|     |_____|   |_| \_\ |___| |_|     /_/   \_\

 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠟⠛⠋⠉⠉⠉⠉⠉⠙⠛⠓⠿⠿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠞⠋⢁⡀⠤⠀⠒⠀⠀⠀⠐⠒⠠⢀⠢⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⣿⠽⠛⠃⣀⠔⠉⠀⠀⠀⠀⢀⣀⣀⣤⣤⠤⠤⠄⠈⠀⠑⢀⡀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠿⠛⠿⠛⠃⠀⠀⡁⠁⠀⢀⣠⣴⣾⡿⠛⠉⠁⠀⠀⠀⠀⣀⢴⠤⢄⡀⠀⠀⠀⠀⠀⠀⠈⠻⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡿⡿⢦⠀⠀⠀⠀⠄⠀⠀⠀⠀⢀⣴⣿⣫⠤⠔⠚⠛⠒⠒⠚⠛⠯⠙⠢⡕⠈⠢⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⡇⠘⡄⠀⠀⠈⠀⠀⠀⠠⢴⡾⠛⠁⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡇⠄⠚⠦⢀⣀⣧⠤⠔⠒⠛⣉⣉⣉⣉⣉⣉⣉⡁⢻⣦⡀⠀⠀⠄⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡿⠁⢀⠤⠒⣉⡥⠴⠖⢛⡯⣍⠉⢉⠤⢤⡀⢀⠬⣍⢉⠿⢿⣦⡀⠈⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿
⡇⠠⣡⢴⡟⠓⠦⡀⣰⠃⠀⠈⠳⠁⠀⠀⠻⠃⠀⠘⠋⠀⠀⠷⠓⡀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿
⣷⣾⠣⡾⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⢀⠀⠀⠀⠀⠀⠀⠆⠘⡄⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⡀⠀⢀⠀⣀⣼⣆⠈⢧⡀⠀⠀⠀⠀⠸⠀⢹⡀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣇⠀⠀⠀⢀⣀⢠⠤⠐⠶⠂⠐⠒⠈⢹⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⢗⠀⠀⠀⠀⠀⣇⠀⢇⠀⠀⠀⠀⡷⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣷⣄⣌⠀⠀⠀⠀⠀⣀⣀⣤⣄⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⢆⠀⠀⠀⠀⢸⠀⠘⠀⠀`⠀⠀⣁⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⡿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⢾⡄⠀⠀⠘⡇⠀⠀⠀⠀⢰⣷⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠈⠇⠀⠀⠀⣧⠀⠀⠀⠀⣸⣻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣧⠀⠄⠀⠀⢠⠀⠀⢰⣠⣯⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⢻⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠃⠀⠀⠀⠉⢻⣿⠀⠀⠀⠀⢸⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣠⠴⠟⢋⡁⠾⠿⠋⠙⠻⠋⠉⠉⠉⠀⠀⠀⠀⠀⢠⣀⣀⣠⠏⠀⡸⠀⠀⢸⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢱⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡖⠤⣤⣀⣼⡷⠞⢁⣠⣾⠃⠀⠀⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣗⡇⠀⣀⠀⠀⠀⠀⠀⢀⡀⠀⠀⣤⣀⠀⣰⣡⣴⠖⠻⣕⠀⢺⠻⠊⠁⠀⣠⣾⣯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠘⢧⡴⠛⣆⣠⠖⢄⣀⣞⣉⣲⡾⠵⠚⠋⠉⠐⠈⠀⠉⠛⠓⠀⠀⠒⠒⠿⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⡉⠛⠛⠛⢛⣛⣉⣩⣥⡄⠒⠂⠀⠀⠀⠁⠉⠀⢀⣠⣌⣷⣖⣤⣄⣀⠘⠻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣭⣭⣿⣿⣻⣿⣷⣷⣷⣶⣶⣶⣶⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣆⣬⣘⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣭⣛⣿                                                                                                                             
"""

dibujito = """
  _        ___       ___    _   _   ___   _____   ____     ___      __  __   _   _    ____   _   _    ___  
 | |      / _ \     / _ \  | | | | |_ _| | ____| |  _ \   / _ \    |  \/  | | | | |  / ___| | | | |  / _ \ 
 | |     | | | |   | | | | | | | |  | |  |  _|   | |_) | | | | |   | |\/| | | | | | | |     | |_| | | | | |
 | |___  | |_| |   | |_| | | |_| |  | |  | |___  |  _ <  | |_| |   | |  | | | |_| | | |___  |  _  | | |_| |
 |_____|  \___/     \__\_\  \___/  |___| |_____| |_| \_\  \___/    |_|  |_|  \___/   \____| |_| |_|  \___/ 

⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠂🇺🇦⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠🇺🇦⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀

"""

print(f"{Fore.RED}"+mensajito)
      
print(f"{Fore.GREEN}"+dibujito)
