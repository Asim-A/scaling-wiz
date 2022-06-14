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

    public class DriveInfo
    {
        public string Model { get; set; }
        public string Name { get; set; }
        public string VolumeName { get; set; }
        public string FileSystem { get; set; }
        public ulong TotalSize { get; set; }
        public ulong AvailableSpace { get; set; }

        public override string ToString()
        {
            return $"[Model: {Model}, Name: {Name}, VolumeName: {VolumeName}\n" +
                $"FileSystem: {FileSystem}\tTotalSize: {TotalSize / Math.Pow(1024, 3)}GB, AvailableSpace: {AvailableSpace / Math.Pow(1024, 3)}]";
        }
    }

    public class HostInfo
    {
        public string DeviceId { get; } = DeviceUtil.HostId();
        public ulong TotalPhysicalMemory { get; set; }
        public ulong TotalAvailableMemory { get; set; }
        public IPAddress IPv4 { get; set; }
        public int LogicalCores { get; set; }

        public IList<DriveInfo> Drives { get; set; } = new List<DriveInfo>();

        public override string ToString()
        {
            return $"Device: {DeviceId}\n" +
                $"TotalPhysicalMemory: {TotalPhysicalMemory} bytes, TotalAvailableMemory: {TotalAvailableMemory}\n" +
                $"IPv4 Address: {IPv4}\n" +
                $"CPUs (Logical): {LogicalCores}\n" +
                $"Drives:\n{string.Join("\n", Drives)}";
        }
    }

    public class DeviceUtil
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

        public static HostInfo Info()
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

            var drives = hardwareInfo.DriveList;
            foreach (var drive in drives)
            {
                foreach (var p in drive.PartitionList)
                {
                    foreach (var v in p.VolumeList)
                    {
                        var d = new DriveInfo
                        {
                            Model = drive.Model,
                            AvailableSpace = v.FreeSpace,
                            TotalSize = v.Size,
                            FileSystem = v.FileSystem,
                            Name = v.Name,
                            VolumeName = v.VolumeName,
                        };
                        info.Drives.Add(d);
                    }
                }
            }

            if (cpu != null)
            {
                info.LogicalCores = cpu.CpuCoreList.Count;
            }

            info.IPv4 = adapter.IPAddressList.First(x => x.AddressFamily == System.Net.Sockets.AddressFamily.InterNetwork);
            info.TotalAvailableMemory = hardwareInfo.MemoryStatus.AvailablePhysical;
            info.TotalPhysicalMemory = hardwareInfo.MemoryStatus.TotalPhysical;

            return info;
        }
    }
}
