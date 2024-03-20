"""
C# Version
var parentheses = new Dictionary<string, string>()
{
    {"(", ")" },
    {"[", "]" },
    {"{", "}" },
};
    

string s = "([)]";
List<char> list = s.ToList();

for (int i = 0; i < s.Length; i++)
{
    int j = s.Length - 1;

    while (j >= 0)
    {
        if (parentheses.ContainsKey(s[i].ToString()))
        {
            if (s[j].ToString() == parentheses.GetValueOrDefault(s[i].ToString()))
            {
                list.Remove(s[i]);
                list.Remove(s[j]);
                break;
            }
        }

        j--;
    }
}

foreach (var item in list)
{
    Console.WriteLine(item);
}

Console.WriteLine(!(list.Count > 0));

"""

def test(param):
    simvols = {'{':'}', '(':')', '[':']'}
    param = list(param)
    while True:
        test2 = False
        index = 0
        while len(param) > index:
            if index != len(param)-1 and param[index+1] == simvols.get(param[index]):
                test2 = True
                param.pop(index)
                param.pop(index)
                break
            index+=1
        if not test2:
            break
        test2 = False
    return not param

a = '[[]]()'

print(test(a))
