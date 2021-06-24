using System;
using System.Collections.Generic;
using System.IO;
using System.Numerics;

namespace Поиск_совпадений
{
    class Program
    {
        static void Main(string[] args)
        {
            //‪C:\Users\aleks\Desktop\VK.txt
            //C:\Users\aleks\Desktop\Test.txt
            //‪C:\Users\aleks\Desktop\RW.txt

            string path_Res = @"C:\Users\aleks\Desktop\Совпадения в файлах.txt";
            List<string> VK = new List<string>();
            //List<string> RW = new List<string>();
            string result = "";
            BigInteger SovPadenie = 0;

            Console.WriteLine("Введите путь к первому txt фалу с почтой");
            string path_mail_1 = @Console.ReadLine();

            Console.WriteLine("Введите путь ко второму txt фалу с почтой");
            string path_mail_2 = @Console.ReadLine();

            Console.WriteLine("Введите путь к txt фалу VK");
            string path_VK = @Console.ReadLine();

            //Console.WriteLine("Введите путь к txt фалу RedWhite");
            //string path_RW = @Console.ReadLine();

            using (StreamReader Reader = new StreamReader(path_VK))
            {
                string line;
                while ((line = Reader.ReadLine()) != null)
                {
                    VK.Add(line);
                }
                Console.WriteLine("\nList VK успешно заполнен\n");
            }

            //using (StreamReader Reader = new StreamReader(path_RW))
            //{
            //    string line;
            //    while ((line = Reader.ReadLine()) != null)
            //    {
            //        RW.Add(line);
            //    }
            //    Console.WriteLine("List RW успешно заполнен\n");
            //}

            using (StreamReader Reader = new StreamReader(path_mail_1))
            {
                string line;
                BigInteger Count = 0;
                while ((line = Reader.ReadLine()) != null)
                {
                    try
                    {
                        Count++;
                        if (Count % 100000 == 0) { Console.WriteLine("Проверено " + Count + " строк первого файла"); Console.WriteLine("Совпадений " + SovPadenie + "\n"); }
                        string login = "";
                        string password = "";

                        try
                        {
                            string[] mass = line.Split(new char[] { ':' });
                            login = mass[0];
                            password = mass[1];
                        }
                        catch { }

                        foreach (string s in VK)
                        {
                            if (s.Contains(login))
                            {
                                result = s + "\n";
                                //string[] str = s.Split(',');
                                //if (!str[2].Contains('@'))
                                //{
                                //    string[] tel = str[2].Split(':');
                                //    foreach (string t in tel)
                                //    {
                                //        try
                                //        {
                                //            string telephon = t.Substring(t.Length - 10);
                                //            foreach (string r in RW)
                                //            {
                                //                if (r.Contains(telephon)) { result += r + "\n"; break; }
                                //            }
                                //        }
                                //        catch { }
                                //    }
                                //}
                                result += "Пароль " + password + "\n\n";
                                Console.WriteLine(result);
                                File.AppendAllText(path_Res, result);
                                SovPadenie++;
                                break;
                            }
                        }
                    }
                    catch { }
                }
            }

            using (StreamReader Reader = new StreamReader(path_mail_2))
            {
                string line;
                BigInteger Count = 0;
                while ((line = Reader.ReadLine()) != null)
                {
                    try
                    {
                        Count++;
                        if (Count % 100000 == 0) { Console.WriteLine("Проверено " + Count + " строк второго файла"); Console.WriteLine("Совпадений " + SovPadenie + "\n"); }
                        string login = "";
                        string password = "";

                        try
                        {
                            string[] mass = line.Split(new char[] { ':' });
                            login = mass[0];
                            password = mass[1];
                        }
                        catch { }

                        foreach (string s in VK)
                        {
                            if (s.Contains(login))
                            {
                                result = s + "\n";
                                //string[] str = s.Split(',');
                                //if (!str[2].Contains('@'))
                                //{
                                //    string[] tel = str[2].Split(':');
                                //    foreach (string t in tel)
                                //    {
                                //        try
                                //        {
                                //            string telephon = t.Substring(t.Length - 10);
                                //            foreach (string r in RW)
                                //            {
                                //                if (r.Contains(telephon)) { result += r + "\n"; break; }
                                //            }
                                //        }
                                //        catch { }
                                //    }
                                //}
                                result += "Пароль " + password + "\n\n";
                                Console.WriteLine(result);
                                File.AppendAllText(path_Res, result);
                                SovPadenie++;
                                break;
                            }
                        }
                    }
                    catch { }
                }
            }
        }
    }
}
