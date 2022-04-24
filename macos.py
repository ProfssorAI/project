a=int(input())
yekan=a%10
dahgan=int(((a%100)-yekan)/10)
sadgan=a-yekan-(10*dahgan)
sadgan=int(sadgan/100)
adad_dovom=sadgan+10*dahgan+100*yekan
#hasel=adad_dovom*2
print(adad_dovom)