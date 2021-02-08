unit_table = [ "", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "];
 

ten_tables = [ "", "", "Twenty ", "Thirty ", "Forty ",  "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "];
 
 
def n2w(n, fd):
 
    str = "";
     
     
    if (n > 19):
        str += ten_tables[n // 10] + unit_table[n % 10];
    else:
        str += unit_table[n];
 
   
    if (n):
        str += fd;
 
    return str;
 
 
def convertToWords(n):
 
     
    out = "";
 
    out += n2w(((n // 1000) % 10), "thousand ");
 
    out += n2w(((n // 100) % 10), "hundred ");
 
    if (n > 100 and n % 100):
        out += "and ";
   
    out += n2w((n % 100), "");
 
    return out;

while True:

    user = input("Type a number you like: ")
    n = int(user[:])
    if (n > 9999):
        print("Number exceeds 9999.")
    else:
        print(convertToWords(n));
    