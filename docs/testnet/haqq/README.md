# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)




## Chain explorer
[https://explorer.kjnodes.com/haqq-testnet](https://explorer.kjnodes.com/haqq-testnet)

## Public endpoints

* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)
* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* grpc: [https://haqq-testnet.grpc.kjnodes.com](https://haqq-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="fd53be6145264c86f2db22659141c925e119794c@138.201.155.226:12656,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,03f0098a22a95e12792597365ca759cb49b3f6b5@75.119.137.10:35656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,aed7038b96314fcb741168869c66029e6c6a58ef@34.90.39.222:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,8874e948e646cfb43ae1c5bdb69c1badf97285fc@149.102.128.160:26656,ce080696d69228597caf0e80920dfe1bae2dcd54@95.217.12.131:26656,54e81994c61bbb6c414f8ab0a606a7edda138a3b@95.216.154.100:26656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,b72f2156db8c87e679dc853730746ff40038120c@213.239.215.77:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
