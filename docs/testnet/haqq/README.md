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

**live-peers** (41)
```bash
peers="26a5bd6fb59f4dcd25f20bbc53b88860b2598f7d@65.21.91.50:35656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,03f0098a22a95e12792597365ca759cb49b3f6b5@75.119.137.10:35656,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,0629018cef2e53288757381ffdc0b84cbb5931cc@95.216.1.249:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,ff6df373bf7bce436d488d2d8f5f5b283c6431d4@51.79.100.160:26656,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,4034efbff7c82e1a2d3908fefd2512552dea63f5@65.109.38.208:26651,e57ee3b940a7962c72ee0cd0fa2007a984bdc58c@185.208.207.130:35656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,754c8fecdf1ecc04d7f5e8399c916f6be83ec66a@167.235.195.204:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,47a269c3e30f70d8234a2afd8e9055e74129fde0@65.108.129.29:36656,b72f2156db8c87e679dc853730746ff40038120c@213.239.215.77:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@45.83.173.18:26656,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656,b1c07038b5b9b96d6fb35e4bb417af7ed238e733@95.217.35.186:26656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,51e4544568cf880451bfffc292de88adc472f0e0@34.147.126.38:26656,5fff90a628395b951d5fb34c64ae6c304b54d2e5@94.130.137.225:36656,10daa6c63b413d8944afef11952f680a486ce7ad@154.26.157.239:35656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.19:26656,e2fde948646175b1b49b3e1943063b049e442917@154.26.157.238:35656,dddce0afadf33e8b8c33a9e797493cd18a9ce5c7@154.26.157.240:35656,5b2ee53c742ce5d392b93c8f193f489a4f13f685@5.189.186.222:26656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
