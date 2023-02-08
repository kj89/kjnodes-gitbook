# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

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

**live-peers** (34)
```bash
peers="ee4db669ed2ff87cb2a47f848fa061517eb47737@161.97.151.46:26656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,077d5d9169efb4b070ce7895d680a9d2148d522c@195.201.195.40:36656,b72f2156db8c87e679dc853730746ff40038120c@213.239.215.77:26656,e57ee3b940a7962c72ee0cd0fa2007a984bdc58c@185.208.207.130:35656,03f0098a22a95e12792597365ca759cb49b3f6b5@75.119.137.10:35656,26a5bd6fb59f4dcd25f20bbc53b88860b2598f7d@65.21.91.50:35656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656,ff6df373bf7bce436d488d2d8f5f5b283c6431d4@51.79.100.160:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.18:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,88b8b733d8b96e9a518c1a8bea4dbc5bf896026e@5.161.156.183:26656,f93085d78df16bbd16a525683af7f857ce1cd983@188.40.98.169:36656,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656,b1c07038b5b9b96d6fb35e4bb417af7ed238e733@95.217.35.186:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,16f40215d018c7d657fef0bb5ce2950251d525d2@148.251.51.144:36656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@45.83.173.19:26656,9444cf6e8cc3e452f8006acce0283d87ee663b7a@185.163.125.253:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
