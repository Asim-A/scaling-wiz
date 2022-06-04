using DeviceId;
using Hardware.Info;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Core
{

    public class HostInfo
    {
        public ulong TotalPhysicalMemory { get; set; }
        public ulong TotalAvailableMemory { get; set; }
        public IPAddress IPv4 { get; set; }
        public IPAddress IPv6 { get; set; }
        public int LogicalCores { get; set; }


    }

    public class DeviceInfo
    {

        static readonly IHardwareInfo hardwareInfo = new HardwareInfo();

        public static string HostId()
        {
            string deviceId = new DeviceIdBuilder()
            .AddMachineName()
            .AddMacAddress()
            .AddOsVersion()
            .ToString();


            return deviceId; 
        }

        public static string Info()
        {
            var info = new HostInfo();
            var deviceId = HostId();
            hardwareInfo.RefreshAll();

            var adapter = hardwareInfo
                .NetworkAdapterList
                .First(x => x.NetConnectionID.Equals("Ethernet") || x.Description.Contains("en"));
            if (adapter == null)
            {
                throw new NoAddressException("Ethernet Connection not Established.");
            }

            var cpu = hardwareInfo.CpuList[0];

            if (cpu != null)
            {
                info.LogicalCores = cpu.CpuCoreList.Count;
            }

            info.IPv4 = adapter.IPAddressList.First(x => x.AddressFamily == System.Net.Sockets.AddressFamily.InterNetwork);
            info.IPv6 = adapter.IPAddressList.First(x => x.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6);
            info.TotalAvailableMemory = hardwareInfo.MemoryStatus.AvailablePhysical;
            info.TotalPhysicalMemory = hardwareInfo.MemoryStatus.TotalPhysical;
    

            return $"HostID: {deviceId}\nmem: {info.TotalPhysicalMemory} memAv: {info.TotalAvailableMemory}\nip: {info.IPv4}\ncpus: {info.LogicalCores}";
        }
    }
}
