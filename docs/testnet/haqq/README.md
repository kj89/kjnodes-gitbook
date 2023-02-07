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

**live-peers** (36)
```bash
peers="fd53be6145264c86f2db22659141c925e119794c@138.201.155.226:12656,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,a89b0005fed82c90e7eb941a5fbffc414aa65c01@65.108.100.49:11513,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,54e81994c61bbb6c414f8ab0a606a7edda138a3b@95.216.154.100:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,aed7038b96314fcb741168869c66029e6c6a58ef@34.90.39.222:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,585f921fe1d7101f2830e1d684797ab0f3d9591e@198.199.71.203:35656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,e57ee3b940a7962c72ee0cd0fa2007a984bdc58c@185.208.207.130:35656,077d5d9169efb4b070ce7895d680a9d2148d522c@195.201.195.40:36656,e0e50095bf450bb28150649be569331f97be9726@85.10.197.4:35656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656,03f0098a22a95e12792597365ca759cb49b3f6b5@75.119.137.10:35656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,18603aa0e749211298227974b7d3b7724cb9bb8d@185.16.38.136:36656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@45.83.173.17:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
