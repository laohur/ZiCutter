# ZiCutter

ZiCutter: cut character smaller

## background
Unicode 14.0 adds 838 characters, for a total of 144,697 characters. (https://www.unicode.org/versions/Unicode14.0.0/) About 2/3 of them are HanZi. To shrink vocab size, we cut character to smaller.

## cut name rare character
name = name of 'x'    
tokens=[name[:2],"#"+name[-1]]    
base: bigrams, [a~z][a~z],[0~9][0~9],#[a~z],#[0~9]    


    '😀' : name is 'GRINNING FACE'
    '😀' -> ["gr","#e"]


## cut ids for HanZi
base: 1719 YuanZi (minium)

    㐂	⿱七⿰七七    
    '㐂' -> ['⿰','七','七']    
    

