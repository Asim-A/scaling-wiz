using CommandLine;
using Core;
using org.apache.zookeeper;

IHost host = Host.CreateDefaultBuilder(args)
    .ConfigureServices(services =>
    {

        Console.WriteLine(args);
        Parser.Default.ParseArguments<Options>(args)
            .WithParsed(o =>
            {
                if (o.Verbose)
                {
                    Console.WriteLine("Verbose HELLO");
                }
                else
                {
                    Console.WriteLine("FK");
                }
            });
        services.AddHostedService<Worker>();
    })
    .Build();

await host.RunAsync();
