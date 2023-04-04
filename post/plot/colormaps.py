import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
#------------------------------------------------------------------------#
#                                                                        #
#           ARPS PYTHON PLOTTING SCRIPTS COLORMAPS COLLECTION            #
#                                                                        #
#------------------------------------------------------------------------#
#    Author:  Nate Snook (9 May 2014)                                    #
#             nsnook@ou.edu                                              #
#------------------------------------------------------------------------#
#    Modification History:                                               #
#       --> Record all modifications you make to the code HERE.          #
#           It will make your life easier -- trust me.                   #
#------------------------------------------------------------------------#

# You can get updated versions of this collection from Nate Snook (nsnook@ou.edu)

#A nice collection of matplotlib-compatible colormaps is provided below with descriptions.
#You may freely use any of these maps, edit them to your liking, or use them as templates
#to design your own.

#------------------------------------------------------------------------#
#                            Colormaps                                   #
#------------------------------------------------- ----------------------#


#------------------------------------------------------------------------#
#NOTE:  Matplotlib supports three main ways of defining colormaps:
#  1)  Accepted HTML color names -- e.g. black, red, cyan
#  2)  RGB hexidecimal color codes -- e.g. '#000000', '#FF0000', '#00F9FF'
#  3)  RGB as fractional triplets -- e.g. (0,0,0), (1,0,0), (0.,.95,1.)
#
#  When designing new colormaps, whether or not they are based on the ones provided here,
#  use one of these three standards to ensure your colormap will work with matplotlib.
#------------------------------------------------------------------------#

#Approximates the usual <<blue --> green --> yellow --> red --> pink --> white>> radar colormap
#Designed for use from 10dBZ to 70dBZ
refl_colors = ['#00FFFF', '#6495ED', '#000090', '#00FF00', '#00BB00', '#008800', '#FFFF00',
               '#FFDD00', '#DAA520', '#FF0000', '#B21111', '#990000', '#FF00FF', '#BB55DD']

#A version of the reflectivity colormap for use with plot_var_advanced.py
refl_colors_adv = ['#FFFFFF', '#00FFFF', '#6495ED', '#0000CC', '#00FF00', '#00BB00',
                   '#008800', '#FFFF00', '#FFDD00', '#DAA520', '#FF0000', '#B21111',
                   '#990000', '#FF00FF', '#BB55DD']

#--- Tim's Version of Z
refl_colors_tim = ['#ffffff','#0FBFF4','#0357E1','#097A7A','#05DD0A','#06AB0B','#7FC601',
                   '#FBE20E','#F4A506','#FA4709','#E80200','#C10606','#DA0684',
                   '#C633DA','#502C61']

#A version of the reflectivity colormap for use with plot_var_advanced.py
refl_colors_low = ['#FFFFFF', '#d9d9d9','#a6a6a6','#00FFFF', '#6495ED', '#0000CC', '#00FF00', '#00BB00',
                   '#008800', '#FFFF00', '#FFDD00', '#DAA520', '#FF0000', '#B21111',
                   '#990000', '#FF00FF', '#BB55DD']



#A correlation coeffecient (rho-hv) colormap [15 gradations]
rho_hv = ['#FFFFFF', '#000000', '#444444', '#888888', '#002090', '#0020F0', '#8888DD',
          '#60FF44', '#90CC00', '#FFFF00', '#FFC000', '#FF8800', '#FF3300', '#DD1100',
          '#990500', '#991155', '#EEAACC']


#A version of the reflectivity colormap designed for Zdr (differential reflectivity)
zdr   = ['#111111', '#444444', '#666666', '#999999', '#CCCCCC', '#FFFFFF', '#AAFFFF', '#00FFFF', 
         '#6495ED', '#0000CC', '#00FF00', '#00BB00', '#008800', '#FFFF00', '#FFDD00', '#DAA520', 
         '#FF0000', '#B21111', '#990000', '#FF00FF', '#BB55DD', '#7722A0']

# A colormap that uses muted colors so Zdr does not look like refl
altzdr = ['#111111', '#444444', '#777777', '#AAAAAA', '#DDDDDD', '#FFFFFF', '#CCCCFF', '#9999FF',
          '#6666FF', '#0000EE', '#AAFFCC', '#66FFA0', '#00CC44', '#EEDD66', '#E6CC20', '#998811',
          '#DDA0A0', '#CC6969', '#AA4040', '#DDAAFF', '#C066FF', '#8800DD']


#A colormap of 16 shades of gray, with the first 4 shades extremely light
grays = ['#ffffff', '#eeeeee', '#dddddd', '#cccccc', '#bbbbbb', '#aaaaaa', '#999999', '#888888',
         '#777777', '#666666', '#555555', '#444444', '#181818', '#111111', '#0a0a0a', '#050505']

#A colormap of 16 shades of gray, from dark to light
gray_darktolight = ['#000000', '#222222', '#444444', '#666666', '#777777', '#888888',
         '#999999', '#aaaaaa', '#bbbbbb', '#cccccc', '#dddddd', '#eaeaea', '#ffffff']
         
#A colormap designed for probability plots:  green denotes low probabilities, yellow denotes
#moderate probabilities, and red denotes high probabilities -- 9 gradations
prob_colors = ['#FFFFFF','#00FF88','#00FF00','#33FF00','#CCFF00','#FFFF00','#FFCC00','#FF3300',
               '#FF0000','#CC0000']
#Another alternate colortable, this one blue/yellow/red
alt_prob_colors3 = ['#FFFFFF', '#55DDFF', '#2C2CFF', '#FFD655', '#FFFF00', '#FF7777', '#FF2222']

#blue/yellow/red probabilities with 10 gradations (with white)
prob_colors_10grades = ['#FFFFFF', '#CCE0FF', '#88AAFF', '#4477FF', '#FFFF99', '#F0F000', '#C0C000',
                        '#FF7777', '#FF2222', '#CC0000']

#blue/yellow/red with extreme values (and white)
prob_colors_12grades = ['#FFFFFF', '#DDF0FF', '#CCE0FF', '#88AAFF', '#4477FF', '#FFFF99', '#F0F000',
                        '#C0C000', '#FF7777', '#FF2222', '#CC0000', '#AA0000']

#A colormap for probability plots in grayscale, for use in AMS Journal publications.
prob_grays =  ['#CCCCCC', '#BBBBBB', '#999999', '#888888', '#666666', '#555555', '#333333',
               '#222222', '#111111']                                  #For intervals of 0.1
#prob_grays = ['#FFFFFF', '#D2D2D2', '#BDBDBD', '#AAAAAA', '#949494', '#737373', '#525252']   #For intervals of 0.2

#A colormap to mimic "refl_grayscale.tbl" in arpsplt
refl_grayscale_tbl = [(.9,.9,.9), (.8,.8,.8), (.7,.7,.7), (.6,.6,.6), (.5,.5,.5),
                      (.4,.4,.4), (.25,.25,.25), (.1,.1,.1), (0,0,0), (0,0,0), (0,0,0)]
#A Colormap to show the updraft and downdraft
wind_colormap = ['#4d4d4d','#000000']
#wind_colormap = ['#ff0000','#ff8080','#4d4d4d','#000000']
#Red to blue through white (Blue is low, red is high, 16 gradations) -- good for temperature difference:
redwhiteblue = ['#0000CC', '#0000FF', '#3333FF', '#5555FF', '#7777FF', '#9999FF', '#BBBBFF','#DDDDFF','#FFFFFF',
                '#FFFFFF','#FFDDDD', '#FFBBBB', '#FF9999', '#FF7777', '#FF5555', '#FF3333', '#FF0000', '#CC0000']

redwhiteblue_white = ['#0000CC', '#0000FF', '#3333FF', '#5555FF', '#7777FF', '#FFFFFF', '#FFFFFF','#FFFFFF','#FFFFFF',
                '#FFFFFF','#FFFFFF', '#FFFFFF', '#FFFFFF', '#FF7777', '#FF5555', '#FF3333', '#FF0000', '#CC0000']

redgrayblue = ['#0000CC', '#0000FF', '#3333FF', '#5555FF', '#7777FF', '#9999FF', '#BBBBFF','#DDDDFF','#d9d9d9',
                '#d9d9d9','#FFDDDD', '#FFBBBB', '#FF9999', '#FF7777', '#FF5555', '#FF3333', '#FF0000', '#CC0000']

#Cyan to purple through white (Purple is low, cyan is high, 16 gradations):
cyanwhitepurple = ['#880088', '#A500A5', '#CC00CC', '#E300E3', '#FF00FF', '#FF55FF', '#FF99FF', '#FFCCFF',
                   '#BBFFFF', '#77FFFF', '#11FFFF', '#00F0F0', '#00CCCC', '#00BABA', '#00A5A5', '#008888']

#Green to brown through white (Green high, brown low, 16 gradations) -- good for moisture, dewpoint plots:
greenwhitebrown = ['#442A00', '#553300', '#775500', '#996600', '#AA8833', '#C0A066', '#D4C099', '#EEE0CC',
                   '#DDF5DD', '#AAEEAA', '#70DD70', '#33CC33', '#2AA02A', '#207920', '#114411', '#093009']

greenwhitebrown_white = ['#442A00', '#553300', '#775500', '#996600', '#AA8833', '#C0A066', '#D4C099', '#FFFFFF',
                   '#FFFFFF', '#AAEEAA', '#70DD70', '#33CC33', '#2AA02A', '#207920', '#114411', '#093009']



#Blue to yellow through white (blue low, yellow high, middle is pure white -- 15 gradations):
bluewhiteyellow = ['#00c6ff','#26d2fb','#4cdef7','#71eaf2','#96f3f2','#b9f7f7','#dcfbfb','#ffffff',
                   '#fbfcdc','#f7f7b8','#f3f394','#f3eb6f','#f7df4a','#fbd325','#ffc700']

#For plotting physical terrain (blue ocean, green for low terrain-->brown for high terrain, 16 gradations):
terrain_colors =  ['#0044FF', '#006633', '#107F35', '#28993B', '#47B247', '#7CCC6C', '#B2E599', '#E5FFCC',
                   '#C9E08F', '#BBCC5D', '#A39233', '#845B15', '#662A00', '#442200', '#CCAA99', '#FFFFFF']

#For precipitation variables and similar things (white for first value, then light blue-->dark blue in 10 gradations):
#blue_gradient =   ['#FFFFFF', '#DDEEF0', '#C6DDEE', '#99CCDD', '#69AADD', '#4490CC', '#2270BB', '#085599',
#                   '#083366', '#001844', '#000918']
blue_gradient =  ['#FFFFFF', '#DDEEF0', '#C6DDEE', '#99CCDD', '#69AADD','#5C93E6', '#4490CC', '#2270BB',
                   '#085599','#083366', '#001844', '#000918']

#Another colormap designed to show intensity (white for first value, then light purple-->dark purple in 11 gradations):
purple_gradient = ['#FFFFFF', '#FAF8FC', '#EFEEF5', '#D8D8EE', '#BBBFDD', '#A099CA', '#807ABB', '#6A50A0',
                   '#552A90', '#440080', '#22004A', '#0A0018']

#An orange intensity colormap (White for first value, then light orange-->dark orange in 10 gradations):
orange_gradient = ['#FFFFFF', '#FFF0EA', '#FFDDBB', '#FFCC99', '#FFB570', '#FFA044', '#EE9030', '#CC7730',
                   '#996020', '#664015', '#332210']

#while we're at it, how about a red gradient?  (White for first value, then light red-->dark red in 10 gradations):
red_gradient =    ['#FFFFFF', '#FFDDCC', '#FFB099', '#FF8866', '#FF6033', '#FF3300', '#CC3000', '#992000', 
                   '#661500', '#481500', '#330900']

#and a green one?  (White for first value, then light green-->dark green in 10 gradations):
green_gradient =  ['#FFFFFF', '#EEFFEE', '#BBFFCC', '#90FFA0', '#66FF80', '#20EE40', '#19CC39', '#16AA30',
                   '#117722', '#105015', '#093010']

#A gradient with both blue and red (white-->blue-->magenta-->red-->black in 16 gradations):
bluered_gradient = ['#ffffff','#bbefff','#77e0ff','#33d0ff','#11b7fe','#5583f7','#994ff0','#de1ae9',
                    '#fc00c7','#f5008a','#ee004d','#e7000f','#b80000','#7a0000','#3d0000','#000000']

#A white-->cyan-->blue-->near black gradient (16 gradations):
ice_blue =        ['#ffffff', '#c5fef9', '#89fcf2', '#4efaeb', '#20efe6', '#17cde7', '#0eaae7', '#0588e8',
                   '#0066dd', '#0047c8', '#0027b3', '#00089e', '#000081', '#000061', '#000042', '#000022']

ice_blue_reverse = ['#000022','#000042','#000061','#000081','#00089e','#0027b3','#0047c8','#0066dd',
                    '#0588e8','#0eaae7','#17cde7','#20efe6','#4efaeb','#89fcf2','#c5fef9','#ffffff']
#A white-->yellow-->orange-->blue-->dark blue gradient (16 gradations):
yelloworangeblue = ['#ffffff','#ffffe4','#fefdc1','#fcfc9e','#fbfa7b','#faee5d','#fcc24a','#fd9638','#ff6a25',
                    '#e85b2e','#b76b52','#877b75','#568b99','#3b72ac','#284cb9','#1426c7','#0000d4']

#A variant on colormap.org's "dawn" colormap.  white-->yellow-->purple-->blue-->black (16 gradations):
sunrise =         ['#ffffff','#fcffbd','#f9ff7b','#f6ff38','#efef0e','#dfab2f','#ce664f','#be2270',
                   '#a60c91','#8724b3','#683dd5','#4955f7','#3549d4','#233199','#12185f','#000024']

#A generic cool-warm colormap.  magenta-->purple-->blue-->cyan-->green-->yellow (16 gradations):
cold_hot =        ['#ff00ff','#df10ef','#bd21df','#9c31ce','#7b43c2','#585ac2','#3571c2','#1287c2',
                   '#1199b1','#32a68e','#53b36b','#75c049','#97cf33','#badf22','#ddef11','#ffff00']

#A centered cold-hot colormap (similar to redwhiteblue; blue-->cyan-->white-->yellow-->orange in 15 gradations):
cold_hot_centered = ['#003bff','#0065ff','#008fff','#00b9ff','#25d5ff','#6ee3ff','#b7f1ff','#ffffff',
                     '#fff1b7','#ffe36e','#ffd525','#ffb800','#ff8e00','#ff6400','#ff3a00']

#Precip-oriented colormap (white-->green-->blue-->purple-->black in 16 gradations):
precip =          ['#ffffff','#bbf3bb','#77e877','#33dc33','#00cd11','#00b655','#009f99','#0087de',
                   '#186bfa','#474af0','#7629e5','#a608da','#8e00ac','#5f0073','#2f0039','#000000']

#Another four color fade (white-->yellow-->green-->cyan-->dark blue in 20 gradations):
yellowgreenblue = ['#ffffff','#fff8c9','#fff094','#ffe95e','#ffe128','#f8dd02','#d9e508','#baed0f',
                   '#9bf416','#7cfc1c','#62fd37','#4bf864','#34f392','#1deec0','#06e8ee','#01c4f4',
                   '#0095ee','#0067e7','#0038e0','#0009d9']

ygb_UH = ['#ffffff','#fff8c9','#fff094','#ffe95e','#ffe128','#f8dd02','#d9e508','#baed0f',
                   '#9bf416','#7cfc1c','#62fd37','#4bf864','#34f392','#1deec0','#06e8ee','#01c4f4',
                   '#0095ee','#0067e7','#0038e0','#ffffff']


#The Reverse of yelowgreenblue
ygb_reverse = ['#0009d9','#0038e0','#0067e7','#0095ee','#01c4f4','#06e8ee','#1deec0','#34f392',
               '#4bf864','#62fd37','#7cfc1c','#9bf416','#baed0f','#d9e508','#f8dd02','#ffe128',
               '#ffe95e','#fff094','#fff8c9','#ffffff']

#Ideal for SRH, Plus showing Positive SRH values to 100
#ygb_reverse_pos = ['#0009d9','#0038e0','#0067e7','#0095ee','#01c4f4','#06e8ee','#1deec0','#34f392',
#               '#4bf864','#62fd37','#7cfc1c','#9bf416','#baed0f','#d9e508','#f8dd02','#ffe128',
#               '#ffe95e','#fff094','#fff8c9','#ffffff','#FFE6E6','#FFCCCC','#FFB2B2','#FF9999']

ygb_reverse_pos = ['#0009d9','#0038e0','#0067e7','#0095ee','#01c4f4','#06e8ee','#1deec0','#34f392',
               '#4bf864','#62fd37','#72FD4B','#81FD5F','#91FE73','#A1FE87','#B0FE9B','#C0FEAF',
               '#D0FEC3','#E0FFD7','#EFFFEB','#ffffff','#FFE6E6','#FFCCCC','#FFB2B2','#FF9999']



#Four color gradient using cool colors (white-->purple-->blue-->green in 20 gradations):
cool_gradient =   ['#ffffff','#ffe4ff','#ffc9ff','#ffaeff','#ff92ff','#f877ff','#dc5dff','#c142ff',
                   '#a528ff','#890dff','#6f0df2','#5527d8','#3b41bd','#215ba2','#077588','#14916d',
                   '#2fac52','#4ac836','#65e41b','#80ff00']

#A centered gradient with near-white in the middle (purple-->cyan-->white-->pink-->yellow, 20 gradations):
centered_grad_20 =['#aa3dff','#8666ff','#628fff','#3fb8ff','#1be0ff','#0dffff','#43ffff','#79ffff',
                   '#afffff','#e5ffff','#ffeaf1','#ffc0d6','#ff95ba','#ff6a9e','#ff3f83','#ff5568',
                   '#ff7f4e','#ffaa34','#ffd51a','#ffff00']

#A centered gradient suitable for dry vs. wet (brown-->white-->cyan, 20 gradations)
drywet_20 =       ['#650900','#761b00','#872e00','#984000','#a95200','#b9680d','#c98a43',
                   '#d9ac79','#e8cdaf','#f8efe5','#e5eff8','#afcde8','#79acd8','#438ac7',
                   '#0d68b7','#0051a3','#003d8d','#002876','#001460','#00004a']

#A centered 20-step gradient suitable for cold vs. hot (deep blue-->cyan-->white-->red-->deep red)
coldhot_20 =      ['#00003f', '#0d2568', '#194990', '#266eb9', '#3392e1', '#47b2ff', '#70c3ff', 
                   '#99d5ff', '#c2e6ff', '#ebf7ff', '#ffebeb', '#ffc3c2', '#ff9a99', '#ff7171', 
                   '#ff4848', '#e63434', '#c42727', '#a21a1a', '#800d0d', '#5e0000']

coldhot_10 =      ['#00003f', '#0d2568', '#194990', '#266eb9', '#3392e1', '#47b2ff', '#70c3ff',
                   '#99d5ff', '#c2e6ff', '#ebf7ff', '#ffffff']

#A rainbow 20-step gradient suitable for intensities (white-->green-->blue-->yellow-->red, 20 gradations):
rainbow_grad_20 = ['#ffffff','#c9ffd6','#94ffad','#5eff84','#28ff5a','#00f546','#00cc6f','#00a398',
                   '#007ac2','#0051eb','#1b52e5','#517baf','#87a479','#bccd43','#f2f60d','#ffd700',
                   '#ffa200','#ff6c00','#ff3600','#ff0000']

#Another 20-step gradient for general purpose use (white-->plum-->cyan-->yellow-->black, 20 gradations)
pcy_20 =          ['#ffffff','#e4c9d1','#c994a3','#ad5e75','#922847','#770c31','#5d3a5f','#42688d', 
                   '#2896bb','#0dc4e9','#1bdfe5','#51e7af','#87ef79','#bcf643','#f2fe0d','#d7d700', 
                   '#a2a200','#6c6c00','#363600','#323232'] 


pcy_22 =          ['#737373','#bfbfbf','#ffffff','#e4c9d1','#c994a3','#ad5e75','#922847','#770c31','#5d3a5f','#42688d',
                   '#2896bb','#0dc4e9','#1bdfe5','#51e7af','#87ef79','#bcf643','#f2fe0d','#d7d700',
                   '#a2a200','#6c6c00','#363600','#000000']



#pcy_22 =          ['#0077b3','#66ccff','#ffffff','#e4c9d1','#c994a3','#ad5e75','#922847','#770c31','#5d3a5f','#42688d',
#                   '#2896bb','#0dc4e9','#1bdfe5','#51e7af','#87ef79','#bcf643','#f2fe0d','#d7d700',
#                   '#a2a200','#6c6c00','#363600','#000000']

yellowgreen_20 =  ['#ffffff','#fffdd6','#fffaad','#fff884','#fff55a','#f6f338','#d1f22c','#acf11f', 
                   '#86f013','#61ef06','#46e000','#35c300','#25a600','#158900','#046c00','#005500', 
                   '#004000','#002b00','#001500','#000000']

precip_20 =       ['#ffffff','#e4f8c9','#c9f294','#aeeb5e','#94e528','#79db0d','#5ec643','#43b179',
                   '#289bae','#0d86e4','#066ff6','#1355e4','#203bd3','#2d21c1','#3a07af','#3d0090',
                   '#3c006d','#3c004a','#3b0026','#3b0003']

#A version of precip_20 more suitable for frozen precip (such as ice or hail)
iceprecip_20 =    ['#ffffff','#c9f0ff','#94e0ff','#5ed1ff','#28c1ff','#06acff','#2086ff','#3960ff',
                   '#5239ff','#6b13ff','#7906f2','#7a12d8','#7b1dbd','#7d29a2','#7e3587','#6f2f6c',
                   '#592351','#441736','#2e0c1b','#190000']

teal_gradient_20 = ['#ffffff','#d6f3f3','#ade7e7','#84dadb','#5bcecf','#39c1c3','#2cb2ba',
                    '#20a2b0','#1393a6','#06839c','#007596','#006794','#005a91','#004c8f',
                    '#003f8c','#003290','#002695','#001988','#000d68','#000045']

#Similar to pcy_20, but using a darker colorscheme
pby_20 =          ['#ffffff','#cfc9e0','#9f94c2','#6f5ea3','#3e2884','#190775','#132593','#0e42b2',
                   '#0860d1','#037df0','#1697e7','#41acb6','#6cc185','#97d655','#c3ec24','#b1cf14',
                   '#8ca10f','#67730a','#414505','#1c1700']

#Similar to pcy_20 and pby_20,  but with green as the first color in the fade
gby_20 =          ['#ffffff', '#c9ddd0', '#94bba1', '#5e9971', '#287742', '#035b2b', '#0e535a', 
                   '#1a4b89', '#2543b9', '#303ae8', '#4b46e6', '#7666b4', '#a08681', '#cba64e', 
                   '#f5c61b', '#e4ae0c', '#c08309', '#9b5806', '#772d03', '#520200']

#A 20-increment colormap suitable for radial velocity (Vr):
vr_20 =           ['#003d00','#005b14','#007a28','#00983d','#00b751','#0dd068','#43db8a',
                   '#79e5ac','#aff0cd','#FFFFFF','#FFFFFF','#fbe5ee','#f1afcc','#e779a9','#dc4386',
                   '#d20d63','#b9004c','#9a0039','#7b0026','#5c0013','#3d0000']

#A 20-increment map suitable for positive-negative quantities:
posneg_20 =       ['#40003f','#681b68','#913690','#b952b9','#e26de1','#ff88ff','#ffa2ff',
                   '#ffbdff','#ffd7ff','#fff2ff','#e5ffff','#afffff','#79ffff','#43ffff',
                   '#0dffff','#00e3e2','#00bcbb','#009594','#006e6d','#004746']

#A 20-increment map with a positive/negative split skewed for more positive gradations.
skew_pos_20 =     ['#0068de','#3688e5','#6ca8ec','#a2c8f3','#d7e8fa','#fffdf8','#fdf3db',
                   '#fbe9be','#f9dfa0','#f7d583','#f3c76c','#ebb45c','#e3a24c','#dc903c',
                   '#d47d2c','#c06622','#a74c19','#8e3311','#751908','#5d0000']

#A 20-increment gradient from white-->yellow-->tan-->brown-->dark brown.
sand =            ['#ffffff','#f5f8d6','#eaf0ad','#e0e985','#d5e15c','#cad63a','#bec22d',
                   '#b2ae20','#a59a13','#998606','#917300','#8e6100','#8b5000','#883e00',
                   '#852d00','#772200','#651900','#541100','#420800','#310000']

#The dreaded rainbow colormap, but with slightly muted colors.  Good for temperature.
rainbow_20 =      ['#3a006e','#3e238c','#4247ab','#466ac9','#4a8ee8','#4ca9f2','#4cabbc',
                   '#4cac86','#52ae44','#57b022','#5eb800','#82c600','#a6d400','#cae200',
                   '#eef100','#ead000','#d99f00','#c96e00','#b83d00','#a80c00']


#Early Attempt at RHV colormarp
rhv_init = ['#ffffff','#666666', '#0000CC', '#0066FF', '#00CC66', '#008800', '#669900', '#FFFF00',
         '#FF0000', '#990000', '#FF00FF' ]


#HCA Colormap

hca_colormap = ['#0000cd','#9acd32','#228b22','#ffff00','#ffa500','#ff4500','#ff0000',
                '#dda0dd','#9400d3','#800080','#eecbad']


hca_color_bio = ['#ffffff','#000000','#808080','#0000cd','#9acd32','#228b22','#ffff00','#ffa500','#ff4500','#ff0000',
                '#dda0dd','#eecbad']


hca_hailsize = ['#ffffff', '#BBBBBB', '#555555', '#001199', '#00BBBB', '#5555FF','#00AA00',
                '#004400','#FF9900','#CC2222', '#990505', '#660000', '#FF9999']


#Hail Diameter Colormap
#Shows severity 
hail_maxdiam =    ['#FFFFFF', '#20700A', '#22AA11', '#44DD22', '#88EE70', '#003D99', '#0055CC',
                   '#0066FF', '#3388FF', '#66A0FF', '#660077', '#9000B0', '#CC00FF', '#DD50FF',
                   '#EA99FF', '#990000', '#CC0000', '#FF1111', '#FF5555', '#FF8888']

hail_maxdiam_lg =    ['#FFFFFF', '#20700A', '#22AA11', '#44DD22', '#88EE70', '#003D99', '#0055CC',
                   '#0066FF', '#3388FF', '#66A0FF', '#660077', '#9000B0', '#CC00FF', '#DD50FF',
                   '#EA99FF', '#990000', '#CC0000', '#FF1111', '#FF5555', '#FF8888','#666600',
                   '#999900','#cccc00','#ffff00','#ffff80']


#HSDA_colormap = ['#FFFFFF','#44DD22','#0066FF','#CC00FF','#e6e600','#ff4000'] 
HSDA_colormap = ['#FFFFFF','#44DD22','#0066FF','#CC00FF','#ff4000','#e6e600']

maxsfc_colormap = ['#FFFFFF','#44DD22','#0066FF','#CC00FF','#ff4000','#999900','#e6e600']
            

#Similar to the hail diameter colormap, a rainfall colormap with sharp boundaries.
rainfall =        ['#FFFFFF', '#0C4405', '#20700A', '#22AA11', '#44DD22', '#88EE70', '#003D99',
                   '#0055CC', '#0066FF', '#3388FF', '#66A0FF', '#660077', '#9000B0', '#CC00FF',
                   '#DD50FF', '#EA99FF', '#990000', '#CC0000', '#FF1111', '#FF5555', '#FF8888',
                   '#FFBB00', '#FFFF44']


#---------------------------------------------------------------------------------------------------#
#                         Colormap List -- allows for dynamic import                                #
#---------------------------------------------------------------------------------------------------#

colormap_list = {
   'refl_colors': refl_colors,
   'refl_colors_adv': refl_colors_adv,
   'refl_colors2': refl_colors_adv,    #Essentially, this aliases 'refl_colors2' to 'refl_colors_adv'.
   'zdr': zdr,
   'grays': grays,
   'gray_darktolight': gray_darktolight,
   'prob_colors': prob_colors,
   'alt_prob_colors3': alt_prob_colors3,
   'prob_colors_10grades': prob_colors_10grades,
   'prob_colors_12grades': prob_colors_12grades,
   'prob_grays': prob_grays,
   'refl_grayscale_tbl': refl_grayscale_tbl,
   'redwhiteblue': redwhiteblue,
   'rwb': redwhiteblue,                         #Make rwb an alias for redwhiteblue
   'cyanwhitepurple': cyanwhitepurple,
   'cyp': cyanwhitepurple,                      #Make cwp an alias for cyanwhitepurple
   'greenwhitebrown': greenwhitebrown,
   'bluewhiteyellow': bluewhiteyellow,
   'bwy': bluewhiteyellow,                      #Make bwy an alias for bluewhiteyellow
   'terrain_colors': terrain_colors,
   'blue_gradient': blue_gradient,
   'purple_gradient': purple_gradient,
   'orange_gradient': orange_gradient,
   'red_gradient': red_gradient,
   'green_gradient': green_gradient,
   'bluered_gradient': bluered_gradient,
   'ice_blue': ice_blue,
   'yelloworangeblue': yelloworangeblue,
   'yob': yelloworangeblue,                     #Make yob an alias for yelloworangeblue
   'sunrise': sunrise,
   'cold_hot': cold_hot,
   'cold_hot_centered': cold_hot_centered,
   'precip': precip,
   'yellowgreenblue': yellowgreenblue,
   'ygb': yellowgreenblue,                      #Make ygb an alias for yellowgreenblue
   'cool_gradient': cool_gradient,
   'centered_grad_20': centered_grad_20,
   'drywet_20': drywet_20,
   'coldhot_20': coldhot_20,
   'rainbow_grad_20': rainbow_grad_20,
   'pcy_20': pcy_20,
   'yellowgreen_20': yellowgreen_20,
   'precip_20': precip_20,
   'iceprecip_20': iceprecip_20,
   'teal_gradient_20': teal_gradient_20,
   'pby_20': pby_20,
   'gby_20': gby_20,
   'vr_20': vr_20,
   'posneg_20': posneg_20,
   'skew_pos_20': skew_pos_20,
   'sand': sand,
   'rainbow_20': rainbow_20,
   'hca_hailsize': hca_hailsize,
   'hail_maxdiam': hail_maxdiam}


#---------------------------------------------------------------------------------------------------#
#                                Contours Based on Variable Data                                    #
#---------------------------------------------------------------------------------------------------#
import numpy as np

#--- Hydrometeor Contours
moist_grad_contours = np.arange(0.00,3.0,0.2)
qv_diff = np.arange(-0.0008,0.0008,0.00001)
#qv_contour=np.arange(0,0.017,0.001)
qv_contour=[0,0.00025,0.0005,0.00075,0.001,0.0015,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.010,0.012,0.014,0.016]
qr_contour= np.arange(0.00,0.00105,0.00005)
max_hail_contours = np.arange(0,100,5)
HSDA_contours = [0,5,25,50,75,100,150]
hail_contours = [0,5,10, 15, 20,25,30,35,40,45,50,55,60]

#--- Radar Variables
#eefl_contours = np.arange(5.,85.,5.)
refl_contours = np.arange(0.,75.,5.)
vel_contours =  np.arange(-20,20,2)

#vel_contours = np.arange(-50,50,5)
  
  
zdr_contours = [-2,-1.5,-1.1,-1.75,-0.5 -0.25,-0.1, 0,.25,.5,.75, 1.0,1.25, 1.5,1.75,2.0,2.5,3.0,3.5,4.0,4.5,5.0]
rhv_contours = [0.2,0.45,0.6,0.75,0.8,0.85,0.9,0.95,0.97,1.0,1.05]
hca_contours = [2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5]
hca_bio_cont = [0.0,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5]

#--- Dynamics Contours
SRH_contours = np.arange(-500,125,25)
#UH_contours = np.arange(-600,-75,25)
UH_contours = np.arange(100,625,25)
mass_contours = [0.00, 0.0001, 0.01, 0.10, 0.2, 0.4, 0.6, 0.8, 1.0, 1.25, 1.50, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0, 4.5, 5.0]
melt_contours = mass_contours
#melt_contours = [0.00,1E-5,1E-4,1E-3,1E-2,1E-1,0.2,0.3,0.6,0.8,1.0,1.25,1.50,1.75,2.0,2.25,2.5,2.75,3.0]
#mass_contours = [0.00, 0.0001, 0.05, 0.10, 0.2, 0.4, 0.6, 0.8, 1.0, 1.25, 1.50, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0, 4.5, 5.0]
w_contours_coarse = [5.0,10.0] #[-3.0,-1.0,5.0,10.0]
w_contours = np.arange(15.,65.,2.5)
u_contour = [0,.1,.2,.5,1.0,1.25,1.5,2.0,2.5,3.0]

#--- Difference Fields
wind_diff = np.arange(-9.0,10.0,1.0)
qv_diff = np.arange(-.8,.81,.1)
#qv_diff = np.arange(-0.0008,0.0008,0.00001)


#--- Perturbation Colormaps
Tpert_contours = np.arange(-8,-.5+(8-.5)/len(ice_blue),(8-.5)/len(ice_blue))
Ppert_contours = np.arange(-450,450,50)
RhoPert_contours = np.arange(-.018,.018,.002)
Buoyancy_contours = np.arange(-.18,.18,.02)

def define_contours(var):
   if var == 'buoyancy':
      contours = np.concatenate((np.array([-.2,-0.10,-0.02]),np.arange(.02,.21,.01)),axis=0)
      cb_ticks = np.concatenate((np.array([-.2,-0.10,-0.02]),np.arange(.02,.21,.01)),axis=0)
      colormap = pcy_22 #redwhiteblue
   elif var == 'bulk_shear' or var == 'high_shear':
      contours = np.arange(0,60,3.0)
      cb_ticks = np.arange(0,60,9)#[-0.16,-.12,-.08,-.04,0,.04,.08,.12,.16]
      colormap = pcy_20 #redwhiteblue
   elif var == 'low_shear':
      contours = np.arange(0,40,2.0)
      cb_ticks = np.arange(0,40,4)
      colormap = pcy_20 #redwhiteblue
   elif var in ['shs_max']:
      #contours = np.arange(100,900,50)
      #colormap = yellowgreenblue #ygb_reverse
      #cb_ticks = contours[::2] 

      #colormap = ListedColormap(newcolors, name='BlueOrangePurple')
      contours = np.arange(0,1500.,10.)
      indices = len(contours)
      colormap = plt.get_cmap("terrain", indices)
      #contours = np.arange(0,1000.,10.)
      cb_ticks = np.arange(0,1000.,100.)
   elif var in ['UH','uh','shs']:
      #contours = np.array([0,10,25,50,75,100,125,150,175,200,250,300,350,400,450,500,550,600,650,700])
      #contours = UH_contours #/10.
      #contours = np.arange(0,210,10)
      #contours = np.arange(0,315,15)
      #contours = np.arange(0,105,5)
      #contours = np.arange(0,147,7)
      #contours = np.arange(75,180,5)
      #contours = np.arange(300,1000,50)
      contours = np.arange(100,900,50)
      #print('JDL HERE')
      #contours = np.arange(0,100,5)
      #contours = np.arange(0,81,4)
      #contours = np.arange(100,1050.,50)
      #contours = np.arange(250,1250,50)
      #contours = np.arange(250,750,25)
      colormap = yellowgreenblue #ygb_reverse
      cb_ticks = contours[::2] 
      #cb_ticks=np.arange(0,210,10)
      #cb_ticks = np.arange(100,650,50)
      #cb_ticks = np.arange(-600,-75,50)
   elif var in ['zvort','svs']:
      #contours = np.array([0,1E-4,2.5E-4,5E-4,7.5E-4,1E-3,2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2,5E-2,7.5E-2,1E-1,2.5E-1,5E-1,7.5E-1,1])
      #contours = np.array([0,1E-2,2E-2,3E-2,4E-2,5E-2,6E-2,7E-2,8E-2,9E-2,1E-1,2E-1,3E-1,4E-1,5E-1])
      #contours = np.array([0,.005,.01,.015,.02,.025,.03,.035,.04,.045,.05,.055,.06,.065,.07,.075,.08,.085,.095,.1])
      #contours = np.arange(0.045,.145,0.005)
      contours = np.arange(0.,.1,0.005)
      #contours = np.arange(0,0.075,0.00375)
      #contours = np.arange(0.,0.05,0.0025)
      #contours = np.array([0.,0.02,0.06,0.08,0.1])
      #colormap = ['#ffffff','#ffe128','#baed0f','#4bf864','#0009d9']
      colormap = yellowgreenblue #ygb_reverse
      cb_ticks = contours[::2]
   elif var in ['wind','v','va']:
      #contours = np.arange(10,25,.75)
      #contours = np.arange(10,40,1.5)
      #contours = np.arange(0,22.5,1.5)
      #contours  = np.arange(0,30,1.5)
      #contours = np.arange(-30,0,1.5)
      #colormap = yellowgreenblue #ygb_reverse
      #cb_ticks = contours[::2]#np.arange(10,30,2)
      #cb_ticks = np.arange(-600,-75,50)
      #contours  = np.arange(14.0,20.1,0.1)
      #contours = np.arange(14.0,20.1,0.1)
      #contours = np.arange(5.0,20.1,0.1)
      #contours = np.arange(0.0,20.0,0.1)
      contours = np.arange(-40,0,0.5)
      indices = len(contours)
      #colormap = plt.get_cmap("plasma", indices) #yellowgreenblue #ygb_reverse
      #colormap = plt.get_cmap("gist_stern")
      colormap = plt.get_cmap("terrain", indices)
      #cb_ticks = np.arange(0.0,20.1,2.0)
      cb_ticks = np.arange(-40,0.0,1.)
      #cb_ticks = np.arange(0,3.1,0.5)
   #elif var in ['u']:
   #   #contours = np.arange(0,100.1,0.1)
   #   #contours = np.arange(0,20.1,0.1)
   #   # JDL
   #   contours = np.arange(-8,8,0.1)
   #   indices = len(contours)
   #   colormap = plt.get_cmap("gist_stern", indices) #yellowgreenblue #ygb_reverse
   #   cb_ticks = np.arange(-8,8,1.)#np.arange(0.0,20.1,4.0)
   elif var in ['wspd_var','u_var','ua_var','sws_var']:
      contours  = np.arange(0.0,3.1,0.1)
      #contours = np.arange(0.0,0.3,0.01)
      indices = len(contours)
      #colormap = plt.get_cmap("plasma", indices) #yellowgreenblue #ygb_reverse
      colormap = plt.get_cmap("YlGnBu", indices)
      #cb_ticks = np.arange(0.0,0.3,0.1)
      cb_ticks = np.arange(0,3.1,0.5)
   elif var in ['v_var']:#,'va_var','winterp_var']:
      #contours  = np.arange(0.0,5.01,0.01)
      contours = np.linspace(-1,1,100)
      contours = 10**contours
      indices = len(contours)
      #colormap = plt.get_cmap("plasma", indices) #yellowgreenblue #ygb_reverse
      #colormap = plt.get_cmap("YlGnBu", indices)
      #colormap = plt.get_cmap("inferno_r", indices)
      #colormap = plt.get_cmap("viridis", indices)
      #contours = np.arange(-40,40,2.5)
      indices = int(len(contours)/2.)
      color_B = plt.get_cmap("PuRd",indices)
      color_A = plt.get_cmap("Blues",indices)
      newcolors = np.vstack((color_A(np.linspace(0, 1, indices)),
                       color_B(np.linspace(0, 1, indices))))
      colormap = ListedColormap(newcolors, name='OrangeBlue')
      cb_ticks = [0.1,0.25,0.5,0.75,1.0,2.5,5.0,7.5,10]
      #cb_ticks = np.arange(0,5.01,0.5)
   elif var in ['w_var','wa_var']:#,'winterp_var']:
      #contours  = np.arange(0,1.55,0.05)
      contours = np.linspace(-3,0.1,100)
      contours = 10**contours
      indices = len(contours)
      colormap = plt.get_cmap("inferno_r", indices) #yellowgreenblue #ygb_reverse
      cb_ticks = contours[::10]
   elif var in ['T_var','qv_var']:
      #contours  = np.arange(0.0,0.775,0.025)
      contours = np.arange(0.0,2.,0.01)
      #contours = np.arange(0.0,0.775,0.025)
      indices = len(contours)
      colormap = plt.get_cmap("magma_r", indices) #yellowgreenblue #ygb_reverse
      #cb_ticks = np.arange(0,0.775,0.1)
      cb_ticks = np.arange(0,2.,0.25)
   elif var in ['dbz_var']:
      contours = np.arange(0.0,10.1,0.1)
      indices = len(contours)
      colormap = plt.get_cmap("magma_r", indices) #yellowgreenblue #ygb_reverse
      cb_ticks = np.arange(0,10.1,1.0)
   elif var in ['paintball']:
      #contours = np.arange(1,20)#41,1)
      contours = np.arange(1,11)
      indices = len(contours)
      colormap = plt.get_cmap("tab10",indices)
      #colormap = plt.get_cmap("tab20",indices)
      cb_ticks = contours
   elif var in ['uadiff']:
      #contours = np.array([0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.,2.5,5,7.5,10,12.5,15,17.5,20])
      contours = np.arange(0,1.01,0.01)
      indices = len(contours)
      colormap = plt.get_cmap("magma_r", indices) #yellowgreenblue #ygb_reverse
      cb_ticks = np.arange(0,20,1)
   elif var in ['vadiff']:
      contours = np.arange(-3,3.01,0.01)
      indices = len(contours)
      colormap = plt.get_cmap("PuOr", indices) #yellowgreenblue #ygb_reverse
      cb_ticks = np.arange(-3,4,1)   
   elif var in ['ua','u','U']:
      #contours = np.arange(6,12,0.3)
      #contours = np.arange(-1.5,1.5,0.15)
      #contours = np.arange(-5,5.1,0.1)
      #contours = np.arange(-6,-3.0,0.1)
      #contours  = np.arange(-10,100,.1)
      contours = np.arange(-10,40,1)
      #contours = np.arange(-0.020,0.,0.001)
      indices = len(contours)
      colormap = plt.get_cmap("magma_r", indices) #yellowgreenblue #ygb_reverse
      cb_ticks = np.arange(-10,40,5)


      #colormap = yellowgreenblue #ygb_reverse
      #cb_ticks = contours[::2]
   elif var in ['V']:
      contours = np.arange(6,12,0.3)
      colormap = yellowgreenblue #ygb_reverse
      cb_ticks = contours[::2]
   elif var in ['wspd','sws']:
      contours  = np.arange(0.0,20.25,.25)
      #contours = np.arange(0.0,50.25,.25)
      #contours = np.arange(15.0,40.0,0.5)
      #contours = np.arange(40.0,65.0,0.25)
      #contours = np.arange(0.0,30.,0.25)
      #contours = np.arange(12,40,0.5)
      #contours = np.arange(0,150)
      indices = len(contours)
      colormap = plt.get_cmap("plasma_r", indices) #yellowgreenblue #ygb_reverse
      #cb_ticks = np.arange(25,60,5)
      cb_ticks = np.arange(0,21,2.)
      #cb_ticks = np.arange(0,51,5)
      #colormap = plt.get_cmap("YlOrRd", indices)
      #cb_ticks = np.arange(0,21,5)#contours[::4]
      #cb_ticks = np.arange(0,150,25)
      #contours  = np.arange(5,50,1.0)
      #contours = np.arange(0,10,0.5)
      #colormap = yellowgreenblue #ygb_reverse
      #cb_ticks = contours[::2]#np.arange(10,30,2)
   elif var in ['pt','th','tha','theta']:
      #contours = np.arange(292,309,1.5)
      #contours = np.arange(300,350,2.5)
      #contours = np.arange(283,300,1.5)
      #contours = np.arange(280,299,1)
      #contours = np.arange(292,296,0.2)
      #contours = np.arange(292,304,0.6)
      #contours = np.arange(-1.8,2.0,0.2)
      #cb_ticks = contours[::2]
      #colormap = redwhiteblue
      #colormap = coldhot_10
      #contours  = np.arange(290.,311.,.25)
      contours = np.arange(295,315,0.5)
      indices = len(contours)
      colormap = plt.get_cmap("YlOrRd", indices)
      cb_ticks = np.arange(295,315,1.)#contours[::4]


      contours = np.arange(284,300,0.5)
      indices = len(contours)
      colormap = plt.get_cmap("bwr", indices)
      cb_ticks = contours[::4]



   elif var in ['th_var']:
      contours = np.arange(0,2.375,0.125)
      cb_ticks = contours[::2]
      colormap = redwhiteblue
      #colormap = coldhot_10
   elif var in ['Temp','temp','T']:# \
      contours = np.arange(15,30,0.5)
      cb_ticks = np.arange(15,30,1.0)
      indices = len(contours)
      colormap = plt.get_cmap("seismic", indices)



      #--- JDL Typical
      #contours = np.arange(10,25,0.25)
      #cb_ticks = np.arange(10,25,1)
      #indices = len(contours)
      #colormap = plt.get_cmap("seismic", indices)
   elif var in ['thpert']:#,'wpert']:# \
      contours = np.arange(-2.,2.2,0.2)
      cb_ticks = contours[::2]
      colormap = coldhot_20
   elif var == 'ThetaE':
      contours = np.arange(333,351,1)
      colormap = yelloworangeblue
      cb_ticks = np.arange(333,351,2)
   elif var == 'Td' or var == 'td':
      #contours = np.arange(263,296,2)-273
      #contours = np.arange(273,306,2) - 273
      contours = np.arange(0,16,1)
      colormap = greenwhitebrown
      cb_ticks = contours[::2]
      #cb_ticks = np.arange(273,306,4) - 273
      #cb_ticks = np.arange(263,296,4)-273
   elif var == 'CAPE':
      #contours = np.arange(0,1800,100)
      #colormap = yelloworangeblue
      #cb_ticks = np.arange(0,1800,200)
      contours = np.arange(250,4750,250)
      colormap = yelloworangeblue 
      cb_ticks = np.arange(500,4750,500)
   elif var == 'temp_pert':
      contours = np.arange(-8,-.5+(8-.5)/len(ice_blue),(8-.5)/len(ice_blue))
      colormap = ice_blue_reverse
      cb_ticks = [-1,-2,-3,-4,-5,-6,-7]
   elif var in ['thdiff','Tdiff']:
      contours = np.arange(-2,2,0.05)
      indices = len(contours)
      colormap = plt.get_cmap("seismic", indices)
      cb_ticks = np.arange(-3,3.5,0.5)
   elif var in ['qv_diff','qvdiff']:
      #contours = np.arange(-.8,.81,.1)
      #colormap = greenwhitebrown
      #cb_ticks = np.arange(-.8,.81,.2)
     
      contours = np.arange(-0.5,0.55,0.05)
      indices = len(contours)
      colormap = plt.get_cmap("BrBG", indices)
      cb_ticks = contours[::2]

   elif var == 'qv_var':
      contours = np.arange(0,.8,.05)
      colormap = greenwhitebrown
      cb_ticks = np.arange(0,.81,.1)
   elif var == 'qr_diff':
      #contours = np.arange(-.4,.41,.05)
      #cb_ticks = np.arange(-.4,.41,.1)
      #contours = np.arange(-.8,.81,0.1)
      contours = [-1.5,-1.0,-0.5,-0.1,-.05,-0.01,-.005,-.001,0.0,0.001,0.005,0.01,0.05,0.1,0.5,1.0,1.5]
      #contours = np.arange(-1.6,1.8,0.2)
      #contours = np.arange(-3.2,3.6,0.4)
      cb_ticks = contours[::2]
      colormap = greenwhitebrown_white
      #cb_ticks = np.arange(-.4,.41,.1)
   elif var == 'qr_var':
      #contours = np.arange(0,1,0.01)
      #cb_ticks = np.arange(0,1,0.1)
      #colormap = plt.get_cmap("Purples")


      contours_lowest = np.arange(0.001,0.01,0.0001)
      contours_low = np.arange(0.01,0.0999,0.001)
      contours_high = np.arange(0.1,1.0,0.01)
      contours_highest = np.arange(1.,10.1,0.1)

      print('contours_A = ',len(contours_lowest))
      print('contours_B = ',len(contours_low))
      print(contours_lowest[-3:])
      print(contours_low[-3:])
 
      print('contours_C = ',len(contours_high))
      print('contours_D = ',len(contours_highest))

      contours = np.concatenate((contours_low,contours_high))
      contours = np.concatenate((contours_lowest,contours))
      contours = np.concatenate((contours,contours_highest))
      indices = len(contours)
      #cb_ticks = contours[::50]
      cb_ticks = np.array([0.001,0.005,0.01,0.05,0.1,0.5,1.,5.,10.])
    
      color_C = plt.get_cmap("PuRd_r",indices)
      color_B = plt.get_cmap("Oranges",indices)
      color_AA = plt.get_cmap("Greens_r",indices)
      color_A = plt.get_cmap("Blues",indices)
      newcolors = np.vstack((color_A(np.linspace(0, 1, indices)),
                             color_AA(np.linspace(0, 1, indices)),
                             color_B(np.linspace(0, 1, indices)),
                             color_C(np.linspace(0, 1, indices))))
      
      colormap = ListedColormap(newcolors, name='BlueOrangePurple')
   

   elif var == 'qv':
      contours = np.arange(2,16,0.25)
      indices = len(contours)
      colormap = plt.get_cmap("BrBG", indices)
      cb_ticks = np.arange(2,16,1)
   elif var in ['prs','P','p']:
      contours = np.arange(90000,102000,50)
      indices = len(contours)
      colormap = plt.get_cmap("twilight", indices)
      cb_ticks = np.arange(90000,10200,1000)
   elif var in ['qvpert']:
      contours = np.arange(-.8,.9,0.1)
      cb_ticks = contours[::2]
      colormap = greenwhitebrown
   elif var == 'nx_diff':
      #contours = np.arange(-225,250,25)
      #contours = np.arange(-4.5,5.0,0.5)
      #contours = [-5E4,-1E4,-5E3,-1E3,-5E2,-1E2,-5E1,-1E1,-5,0,5,1E1,5E1,1E2,5E2,1E3,5E3,1E4,5E4]
      contours = [-25,-10,-7.5,-5,-2.5,-1.,-.75,-.5,-.25,0,.25,.5,.75,1,2.5,5,7.5,10,25]
      colormap = redwhiteblue
      cb_ticks = contours[::2]
   elif var in ['Z','refl2d','refl3d','outgridtilt_zhh','obsordr_zhh','truref','dbz']:
      contours = np.arange(5.,85.,5.) 
      contours = np.arange(0.,75.,5.)
      colormap = refl_colors_adv
      cb_ticks = [10., 20., 30., 40., 50., 60., 70.]



      #contours = np.arange(0,70,0.5)
      #contours = np.arange(-0.020,0.,0.001)
      #indices = len(contours)
      #colormap = plt.get_cmap("jet", indices) #yellowgreenblue #ygb_reverse
      #cb_ticks = np.arange(0,70,5)

      #contours = np.array([-100,-5,0,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80])
      #colormap = refl_colors_low
      #cb_ticks = [1,5,10., 20., 30., 40., 50., 60., 70.]

      #contours = np.arange(-200,-150,5)
      #cb_ticks = np.arange(-200,-150,10)
   elif var == 'radv3d' or var == 'radv2d' or var == 'outgridtilt_vr' or var =='obsordr_vr' :
      contours = vel_contours
      colormap = vr_20
      cb_ticks = np.arange(-40,40,10)#np.arange(-20,20,5) 
   elif var == 'zdr' or var == 'outgridtilt_zdr' or var == 'obsordr_zdr':
      contours =  [-3.0, -2.0, -1.5, -1.0, -0.5, -0.01, 0.01, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.50, 4.00, 4.50, 5.00]
      cb_ticks = [-3.0, -2.0, -1.0, 0, 1.0, 2.0, 3.0, 4.0, 5.0]
      colormap = altzdr
   elif var == 'rhohv' or var == 'outgridtilt_rhv':
      contours = [-0.01, 0.00, 0.20, 0.40, 0.55, 0.65, 0.75, 0.80, 0.85, 0.90, 0.925, 0.95, 0.96, 0.97, 0.98, 0.99, 1.00, 1.05]
      cb_ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 0.9, 0.95, 1.00]
      colormap = rho_hv
   elif var in ['rho_h','rho_g']:
      contours = [0,10,100,300,500,600,650,700,750,800,825,850,875,900,925]
      cb_ticks = contours[:]
      colormap = sunrise
   elif var == 'hail' or var == 'MESH' or var == 'Dmax'  or var == 'dmax' or var == 'DEPTH':
      #--- 0 - 100 mm
      #contours = max_hail_contours
      #colormap = hail_maxdiam
      #cb_ticks = max_hail_contours

      #--- Enlarged 0 -150 mm
      #contours = [0.0,5.0]
      #cb_ticks = contours
      #colormap = ['#FFFFFF','#FFFFFF']
      contours = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0,110.0,120.0,130.0,140.0,150.0]
      cb_ticks = [0.0, 25.0, 50.0, 75.0,100.0,150.0]
      colormap = hail_maxdiam_lg
   #elif var == 'DEPTH':
   #   contours = np.arange(0,10,.5)
   #   cb_ticks = contours[::2]
   #   colormap = hail_maxdiam_lg
   elif var == 'HSDA' or var == 'hsda':# or var =='maxsfc' :
      contours = HSDA_contours
      colormap = HSDA_colormap 
      cb_ticks = HSDA_contours
   elif var == 'maxsfc':
      contours = [0,5,25,50,75,100,150,200]
      colormap = maxsfc_colormap
      cb_ticks = contours[1:7]
   elif var in ['UH','uh','shs']:
      contours = SRH_contours 
      colormap = ygb_reve
      cb_ticks = np.arange(-500,125,50)
   elif var == 'SRH':
      contours = SRH_contours 
      colormap = ygb_reverse_pos
      cb_ticks = np.arange(-500,125,50)
   elif var == 'dryline':
      contours = moist_grad_contours
      colormap = greenwhitebrown
      cb_ticks = np.arange(0.00,3.0,0.2)
   elif var == 'HCA' or var == 'hca':# or var == 'outgridtilt_zhh':
      contours = hca_contours
      #colormap = hca_colormap#hca_hailsize
      colormap = hca_color_bio
      cb_ticks = hca_bio_cont #np.arange(0.00,3.0,0.2)
   elif var == 'stretching' or var == 'tilting':
      contours = np.linspace(-5,5,18)
      colormap = redwhiteblue
      cb_ticks = np.arange(-5,5,1)

   #elif var in ['w','W','wmax','WMAX','winterp','upert','wa']:
   #   contours = np.arange(0,6,0.1)
   #   colormap = plt.get_cmap("gist_stern")
   #   cb_ticks = np.arange(0,6,1)
   elif var in ['upert','vpert','wpert','vpert1']:
      #contours = np.arange(-5,5,0.5)
      #contours = np.arange(-3,3.3,0.3)
      #cb_ticks = contours[::2]
      #colormap = centered_grad_20
      contours = np.arange(-3.0,3.1,0.1)#25)
      #contours = np.arange(-40,40,2.5)
      cb_ticks = np.arange(-3.0,3.1,1.0)
      indices = int(len(contours)/2.)
      color_B = plt.get_cmap("Oranges",indices)
      color_A = plt.get_cmap("Blues_r",indices)
      newcolors = np.vstack((color_A(np.linspace(0, 1, indices)),
                       color_B(np.linspace(0, 1, indices))))
      colormap = ListedColormap(newcolors, name='OrangeBlue')
   elif var in ['va_var']:
      contours = np.arange(0,10,0.1)
      indices = len(contours)
      colormap = plt.get_cmap("jet", indices)
      cb_ticks = np.arange(0.0,11.,1.0) 
   elif var in ['w','W','wmax','WMAX','winterp','upert','wa','sus']:
      #contours = np.arange(7.5,57.5,2.5)
      #colormap = hail_maxdiam
      #cb_ticks = np.arange(10.,60.,5.0)
      #=== ORIG
      #contours = np.arange(0,40,2)
      #contours = np.arange(10,30,1)
      #contours = np.arange(-4.5,5,0.5)
      #contours = np.arange(-18,20,2)
      #contours = np.arange(-9,10,1)
      #cb_ticks = np.arange(0,40,4)
      #colormap = hail_maxdiam

      #high_contour = np.arange(0,22,2)
      #low_contour = np.arange(-5,0,0.5)
      #---
      #high_contour = np.arange(0,77,7)
      #low_contour = np.arange(-25,0,2.5)
      #contours = np.append(low_contour,high_contour)

      #contours = [0,0.5,1.,2.,2.5,3,3.5,4,5,6,7,8,9,10,11,12,13,14,15]
      #contours = np.arange(0,1.05,0.05)
      #contours = np.arange(-1,0.05,0.05)
      #colormap = centered_grad_20
      #colormap = plt.get_cmap("PuOr", 18) #RdYIGn #redwhiteblue
     
      contours = np.arange(-1.5,1.6,0.1)#25)
      contours = np.arange(-25,25,1)
      #contours = np.arange(-10,10,0.5)
      cb_ticks = contours[::2]
      indices = int(len(contours)/2.)
      color_B = plt.get_cmap("Oranges",indices)
      color_A = plt.get_cmap("Blues_r",indices)
      newcolors = np.vstack((color_A(np.linspace(0, 1, indices)),
                       color_B(np.linspace(0, 1, indices))))
      colormap = ListedColormap(newcolors, name='OrangeBlue')

       #contours = [-80.0, -60.0, -40.0, -30.0, -20.0, -15.0, -10.0, -7.5, -5.0, -2.5, 0.0, 2.5, 5.0, 7.5, 10.0, 15.0, 20.0, 30.0, 40.0, 60.0, 80.0]
       #contours = np.arange(0,95,5)
       #cb_ticks = contours[::2]
       #cb_ticks = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50]
       #colormap = yellowgreenblue
#   elif var == 'wmax':
#      contours = np.arange(10,50,2)
#      cb_ticks = contours[::2]
#      colormap = yellowgreenblue 

   elif var == 'qx_diff':
      contours = np.linspace(-.1,0.1,18)
      colormap = redgrayblue
      cb_ticks = contours[::2]
   elif var == 'NEP':
      contours = np.array([0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0])
      colormap = ['#FFFFFF', '#DDF0FF', '#CCE0FF', '#88AAFF', '#4477FF', '#FFFF99', '#F0F000',
                        '#C0C000', '#FF7777', '#FF2222', '#CC0000', '#AA0000']
      cb_ticks = np.array([0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0])
      contours = contours #/ 2.
      cb_ticks = cb_ticks #/ 2.
   elif var in ['mh','qh','qg','qhl','qs'] :
      #contours = melt_contours
      contours = [1E-4,2.5E-4,5E-4,7.5E-4,1E-3,2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2,5E-2,7.5E-2,0.1,.25,.5,.75,1.0,2.5,5.,7.5]
      #contours = np.arange(1,20,1)
      #contours = contours/2.
      colormap = iceprecip_20
      cb_ticks = contours[::2]#np.arange(0.5,5,0.5)


   elif var in ['qh_sum']:
      contours = [2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2,5E-2,7.5E-2,0.1,.25,.5,.75,1.0,2.5,5.,7.5,10,25,50,75,100]
      colormap = iceprecip_20
      cb_ticks = contours[::2]
   elif var in ['qxtsfc']:
      melt_contours = [0.1,0.25,0.5,0.75,1.0,2.5,5.0,7.5,10.,25,50,75,100,250,500,750,1000]
      contours = melt_contours
      cb_ticks = melt_contours[::2]
      colormap = iceprecip_20

   elif var in ['vh','vg']:
      #contours = [1E-4,2.5E-4,5E-4,7.5E-4,1E-3,2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2,5E-2,7.5E-2,0.1,.25,.5,.75,1.0,2.5,5.,7.5]
      contours = [1E-2,2.5E-2,5E-2,7.5E-2,0.1,.25,.5,.75,1.0,2.5,5.,7.5,10,25,50,75,100,250,500,750,1000]
      #contours = [1E-6,2.5E-6,5E-6,7.5E-6,1E-5,2.5E-5,5E-5,7.5E-5,1E-4,2.5E-4,5E-4,7.5E-4,1E-3,2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2,5E-2,7.5E-2]
      colormap = yellowgreenblue#iceprecip_20
      cb_ticks = contours[::2]#np.arange(0.5,5,0.5)
   #elif var in ['qh','qg']:
   #   contours = [0.00,1E-6,1E-5,1E-4,1E-3,1E-2,1E-1,1E0]
   #   cb_ticks = [0.00, 0.002, 0.004, 0.006, 0.008, 0.010]
   #   colormap = iceprecip_20
   elif var == 'fm':
      contours = melt_contours
      cb_ticks = melt_contours[::2]
      colormap = iceprecip_20 
   elif var == 'Null' or var == 'null':
      contours = [-100000.,-10000.]
      colormap = ['#b3b3b3','#b3b3b3'] 
      cb_ticks = [-999.]
   elif var == 'Obj':
      contours = np.arange(0,30,1)
      colormap = rainbow_grad_20
      cb_ticks = np.arange(0,30,1)  
   elif var == 'alpha' or var == 'Alpha' or var == 'alph_h' or var == 'alph_r':
      #contours = [0.0,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0]
      contours = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
      colormap = bluered_gradient 
      cb_ticks = [2.0,4.0,6.0,8.0,10.0,12.0]
   elif var == 'nthsum':
      #contours = np.arange(250000,2000000,250000)#np.arange(1000,15000,1000)
      contours = np.arange(0,5E6,2.5E5)
      cb_ticks = contours[::2]
      colormap = pcy_20
   elif var == 'nh' or var == 'ng' or var == 'nr':
      #thresholds = np.arange(0,2,.1)
      #contours = [0,0.1,0.25,0.5,0.75,1.0,2.5,5,7.5,10,25,50,75,100,250,500,750,1000]#[0,0.1,0.5,1.0,5,10,50,100,500,1000]
      #cb_ticks = [1,10,100,1000]#arange(0,2,0.2)
      #contours = [1e-4,1e-3,1e-2,1e-1,1,5,10,25,50,75,100,200,300]
      #cb_ticks = [1e-4,1e-3,1e-2,1e-1,1,5,10,50,100,300]
      contours = [1E-4,5E-4,1E-3,5E-3,1E-2,5E-2,1E-1,5E-1,1,5,10,50,100,500,1000,5000,10000]
      #contours = np.arange(1000,20000,1000)
      cb_ticks = contours[::2]
      colormap = pcy_20
   elif var == 'ntxsfc':
      contours = [0,0.075,0.1,.25,.5,.75,1,2.5,5,7.5,10,25,50,75,100,250,500,750]
      cb_ticks = contours[::2]
      colormap = pcy_20
   elif var == 'nttsfc':
      contours = [1E1,2.5E1,5E1,7.5E1,1E2,2.5E2,5E2,7.5E2,1E3,2.5E3,5E3,7.5E3,1E4,2.5E4,5E4,7.5E4,1E5]
      cb_ticks = contours[::2]
      colormap = pcy_20

   elif var == 'mmdi':
      contours = [0.0, 1.0,  2.0,  3.0,  4.0,  5.0,  6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0,24.0,26.0,28.0,30.0]
      cb_ticks = [0.0,5.0,10.0,15.0,20.0,25.0,30.0]
      colormap = hail_maxdiam
   elif var in ['mmdi_h','dmhail']:

      #contours = np.arange(0,10,0.5)
      #cb_ticks = np.arange(0,10,1)
      #colormap = pcy_20
      contours = [0,0.5,1,1.5,2.5,3,4,5,6,7,8,9,10,11,12,13,14,15]#np.arange(0,10,0.5)
      #contours = np.arange(0,5,0.25)
      #contours = np.arange(0,20,1.)
      cb_ticks = contours[::2]#np.arange(0,10,1)
      colormap = gby_20
   elif var in ['dmgrpl']:
      contours = np.arange(0,4,0.2)
      cb_ticks = contours[::2]#np.arange(0,10,1)
      colormap = gby_20
   elif var == 'mmdi_hmelt':
      contours = np.arange(0,20,1.)
      cb_ticks = np.arange(0,20,2)
      colormap = pcy_20
   elif var in ['mmdi_r','dmrain']:
      contours = np.arange(0,5,.25)
      cb_ticks = np.arange(0,5,1)
      colormap = pcy_20
   elif var in ['mmdi_rdiff']:
      #contours = np.arange(-1.125,1.25,.125)
      #cb_ticks = np.arange(-1,1,0.25)     
      contours = np.arange(-.45,.5,0.05)
      #contours = np.arange(-.045,.05,.005)
      cb_ticks = contours[::2]


      
      #contours = np.arange(-4.5,5,.5)
      #cb_ticks = np.arange(-4,5,1)
      colormap = redwhiteblue
   elif var == 'covariance':
      #contours = np.arange(-18,20,2)
      #contours = np.arange(-,5.5,0.5)
      #contours = np.arange(-5.4,6.0,0.6)     
      #contours = np.arange(-3.6,4.0,0.4)
      contours = [-1.5,-1,-5E-1,-1E-1,-5E-2,-1e-2,-5E-3,-1E-3,0,1E-3,5E-3,1E-2,5E-2,1E-1,5E-1,1,1.5]

      #contours = np.arange(-18,20,2)
      cb_ticks = contours[::2]
      colormap = redgrayblue
   elif var == 'qcovariance':
      contours = [-5,-1,-5E-1,-1E-1,-5E-2,-1e-2,-5E-3,-1E-3,0,1E-3,5E-3,1E-2,5E-2,1E-1,5E-1,1,5]
      cb_ticks = contours[::2]
      colormap = redgrayblue
   elif var == 'ncovariance':
      #contours = np.arange(-18,20,2)
      #contours = np.arange(-,5.5,0.5)
      #contours = np.arange(-5.4,6.0,0.6)
      contours = [-1E3,-5E2,-1E2,-5E1,-1E1,-5,-1,-5E-1,-1E-1,0,1E-1,5E-1,1,5,1E1,5E1,1E2,5E2,1E3]
      #contours = np.arange(-8000,9000,1000)
      #contours = np.arange(-1.8,2.0,0.2)
      cb_ticks = contours[::2]
      colormap = redwhiteblue
   elif var == 'correl':
      contours = np.array([-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,0.0,0.2,0.30,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
      #contours = np.arange(-0.9,1.0,0.1)
      #contours = np.arange(-0.50,0.55,0.05)
      #colormap = plt.get_cmap("coolwarm", 20)
      cb_ticks = contours[::2]
      colormap = redwhiteblue
   elif var == 'mmdi_hdiff':
      contours = np.arange(-1.125,1.25,.125)
      cb_ticks = np.arange(-1,1,0.25)
      colormap = redwhiteblue
   elif var == 'fm':   # water fraction
      contours = np.arange(0,0.16,0.01)
      cb_ticks = np.arange(0,0.16,0.02)
      colormap = sunrise
   elif var in ['raing','rain']:
      #contours = [0.0, 0.25, 1.0, 2.0, 3.0, 4.0, 5.0, 7.5, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 125.0, 150.0]
      #cb_ticks = [0.0, 10.0, 20.0, 50.0, 100.0, 150.0,200.0]
      #contours = np.arange(0,52,2.5)
      contours = np.arange(0,20,1)
      cb_ticks = contours[::2]
      colormap = precip_20 #rainfall
   elif var in ['raing_var']:
      contours = np.arange(0,15.5,0.75)
      cb_ticks = contours[::2]
      colormap = yellowgreenblue  #rainfall
   elif var in ['dmax_var']:
      contours = np.arange(0,31,1.5)
      cb_ticks = contours[::2]
      colormap = yellowgreenblue  #rainfall

   elif var in ['sfwind']:
      contours = np.arange(0,18,1.5)
      cb_ticks= contours[::2]
      colormap =  yelloworangeblue
   elif var == 'fw':
      contours = np.arange(0.5,0.9,0.025)
      cb_ticks = np.arange(0.5,0.9,0.05)
      colormap = sunrise
   elif var in ['Diff','zdiff']:
      #contours = np.linspace(-2.5,2,16)
      contours = np.arange(-2.25,2.5,0.25)
      #contours = np.arange(-22.5,25,2.5)
      cb_ticks = contours[::2]
      colormap = redwhiteblue
   elif var in ['ptdiff']:
      #contours = np.arange(-9,10,1.)
      contours = np.arange(-2,2.25,0.25)
      cb_ticks = contours[::2]
      colormap = redwhiteblue 
   elif var == 'z_diff':
      #--- Change in Z During Assimilation
      contours = np.arange(-18,20,2)
      cb_ticks = contours[::2]
      colormap = redwhiteblue
   elif var == 'zdiff':
      contours = np.arange(-225,250,25)
      cb_ticks = contours[::2]
      colormap = redwhiteblue
   elif var == 'hterain' or var == 'zp':
      #contours = [-10, 0, 50, 100, 150, 200, 300, 500, 750, 1000, 1300, 1700, 2200, 2800, 3200, 3500, 4000]
      contours = [-10, 0, 1500,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000]
      cb_ticks = [0, 500, 1000, 2000, 3000, 4000]
      colormap = terrain_colors
   elif var == 'radcnt':
      contours=[-1,0,1,2]
      cb_ticks=[-1,0,1,2]
      colormap=['#000000','#e6e6e6','#ffffff','#ffffff']
   elif var in ['qhfall','qgfall','nhfall','ngfall']:
      contours = np.arange(0.0,10,0.5)
      cb_ticks = contours[::2]
      colormap = precip_20
   elif var == 'p':
      contours = np.arange(93000,97000,250)
      cb_ticks= np.arange(93000,97000,500)
      colormap =  yelloworangeblue
   elif var == 'qr_max':
      contours = np.arange(0,40,2)
      cb_ticks = contours[::2]
      colormap = precip_20
   elif var == 'qrtmax':
      #contours = np.arange(0,10000,500)
      contours = np.arange(0,10,.5)
      cb_ticks = contours[::2]
      colormap = precip_20
   elif var in ['mr']:
      contours = [0.00, 0.01, 0.05, 0.10, 0.2, 0.4, 0.6, 0.8, 1.0, 1.25, 1.50, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0, 4.5, 5.0]
      cb_ticks = [0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0]
      colormap = precip_20
   elif var in ['qr','qc']:
      #thresholds = arange(0.00, 0.0105, 0.0005)
      #contours = np.arange(0.0000,0.0000105,0.0000005)
      #cb_ticks = [0.00, 0.002, 0.004, 0.006, 0.008, 0.010]
      #cb_ticks = contours
      print('JDL HERE')
      contours = [1E-4,2.5E-4,5E-4,7.5E-4,1E-3,2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2,5E-2,7.5E-2,0.1,.25,.5,.75,1.0,2.5,5.,7.5]
      #cb_ticks = contours[::2]
      #colormap = precip_20
      #contours = [1E-3,2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2,5E-2,7.5E-2,1E-1,2.E-1,5E-1,7.5E-1,1,2.5,5,7.5,10]
      #contours = np.arange(0,10.5,0.5)
      cb_ticks = contours[::2]
      colormap = precip_20
      #--- JDL ORIG
      #contours = np.arange(0.0,5.,.25)
      #cb_ticks = contours
      #colormap = precip_20
      #thresholds = np.arange(0.0000,0.0000105,0.0000005)
      #cb_ticks = thresholds
      #colormap = precip_20
   elif var in ['qc']:
      contours = [1E-4,2.5E-4,5E-4,7.5E-4,1E-3,2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2,5E-2,7.5E-2,0.1,.25,.5,.75,1.0,2.5,5.,7.5]
      cb_ticks = contours[::2]
      colormap = precip_20 
   elif var in ['qhlacr','QCLrh','QCLch','qhlacw','QSHhr','qhlshr','qhlcnh']:
      contours = np.arange(-15,0,1)
      cb_ticks = contours[::2]
      colormap = precip_20
   elif var in ['chlcnh']:
      contours = np.arange(-5,10,1)
      cb_ticks = contours[::2]
      colormap = precip_20
   elif var == 'percentage':
     contours = [-10000,-5000,-1000,-500,-100,-50,-10,-5,-1,1,5,10,50,100,500,1000,5000,10000]
     cb_ticks = contours[::2]
     colormap = redwhiteblue
   else:
      contours= colormap=cb_ticks=['NaN']

   return contours,cb_ticks,colormap


def overlayContours(var):
   if var == 'UH':
      #contours = [-50,-100]
      #contours = [25,300]
      contours = [-100,-300]
      colormap = ['#000000','#404040','#737373']
   elif var == 'w':
      contours = [2.5,5.0]
      colormap = wind_colormap
   elif var == 'temp_pert':
      contours = [-1,-3,-5]
      colormap = ['#000000','#404040','#737373']
   elif var == 'mixing_ratio':
      contours = mass_contours
      colormap = iceprecip_20
   elif var == 'CINE':
      contours = [300]
      colormap = ['#009933']
   elif var == 'HCA':
      #--- Hail Contours
      contours = [9.5]
      colormap = ['#e65c00']
   else:
      contours=colormap=['NaN']
      
   return contours,colormap

