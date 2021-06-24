using System;
using System.Collections.Generic;
using System.IO;
using System.Numerics;

namespace Проверка_совпадений_с_RedWhite
{
    class Program
    {
        static void Main(string[] args)
        {
            string path_Res = @"C:\Users\aleks\Desktop\Совпадения в RW.txt";
            List<string> RW = new List<string>();

            Console.WriteLine("Введите путь к первому txt фалу с уже наеденными совпадениями");
            string path = @Console.ReadLine();

            Console.WriteLine("Введите путь к txt фалу RedWhite");
            string path_RW = @Console.ReadLine();

            using (StreamReader Reader = new StreamReader(path_RW))
            {
                string line;
                while ((line = Reader.ReadLine()) != null)
                {
                    RW.Add(line);
                }
                Console.WriteLine("List RW успешно заполнен\n");
            }

            using (StreamReader Reader = new StreamReader(path))
            {
                string line;
                BigInteger Count = 0;
                while (true)
                {
                    line = Reader.ReadLine();
                    if (line == null) 
                    { 
                        line = Reader.ReadLine(); 
                        if(line == null) { break; }
                    }
                    if (line.Contains('@'))
                    {
                        try
                        {
                            Count++;
                            if (Count % 100 == 0) { Console.WriteLine("Проверено " + Count + " строк файла"); }
                            string result = line+"\n";

                            string[] str = line.Split(',');
                            if (!str[2].Contains('@'))
                            {
                                string[] tel = str[2].Split(':');
                                foreach (string t in tel)
                                {
                                    try
                                    {
                                        string telephon = t.Substring(t.Length - 10);
                                        foreach (string r in RW)
                                        {
                                            if (r.Contains(telephon)) { result += r + "\n"+Reader.ReadLine()+"\n";Console.WriteLine(result); File.AppendAllText(path_Res, result);
                                            }
                                        }
                                    }
                                    catch { }
                                }
                            }
                        }
                        catch { }
                    }
                }
                Console.WriteLine("\nНУ И ЧТО БЫ БЕЗ МЕНЯ ДЕЛАЛИ?)\n");
            }
        }
    }
}
