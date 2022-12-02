# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (31)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,eb5fee5e8d7d5a300db7c89a4a24a205197f85c5@185.237.97.56:656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,98a1522fc5c2c200f8363ba5885771e7ec1ab5c7@95.217.211.32:26656,96fc6a8c3eb58d43c4ac41e9e642ba8485837ad3@109.123.255.116:26656,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,0534e64a6df8a0ac7d032d3eff3587f5fd69ba37@65.108.206.118:60756,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,e8799d0034f6b99cc01916639dc424c7d2548784@185.169.252.60:36656,05fa81c618612d6730cb8b54620954ce384899af@146.190.218.191:41656,aec8ea46d0e5d0688b58df8a47c6934959fe981f@65.109.90.33:11356,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,c6dcaf5c1d59c696a5b93f53cc5a855b2399f09c@149.102.146.49:26656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,a536f71fcc2497cc7f8ef2b74b43368eaf3bf1b8@65.109.51.41:26656,eec3daeed105dcd5647d1fc24ef8f1d0f404f2fe@167.235.21.149:29656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,45de37d6340caef9bd84111ffb5163d0f3604e84@135.181.153.228:46656,fdeb051aae6f555150bb4cf685719879f21cd3e4@217.13.223.167:36656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,6a7ba7eca935a76e02b5bbb9caf149a41da9af12@144.76.27.79:46656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,f91f270980654a74c7619eff18bc068d2b86e6d8@54.90.149.14:41656,0d4c392f44c081347775643d99311bf2b36a7377@80.241.220.27:60956,d3fb1c74c2b38a220e113d450afd3000922e5eff@65.109.84.216:26656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
