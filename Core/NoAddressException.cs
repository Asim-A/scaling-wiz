using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Core
{
    public class NoAddressException : Exception
    {
        public NoAddressException(string? message) : base(message)
        {
        }

    }
}
