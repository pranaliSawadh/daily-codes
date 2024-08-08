
class Reverse
{
    // Complete the function
    // str: input string
   
    public static String reverseWord(String str)
    {
          String result = "";
        // Reverse the string str
        for(int i=str.length()-1;i>=0;i--){
        result += str.charAt(i);
        }
        
        return result;
    }
}
