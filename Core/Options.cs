using CommandLine;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Core
{
    public class Options
    {
        [Option('v', "verbose")]
        public bool Verbose { get; set; }
    }
}
