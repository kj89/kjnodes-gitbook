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

**live-peers** (29)
```bash
peers="fd53be6145264c86f2db22659141c925e119794c@138.201.155.226:12656,7e263a537071b8e18c74cf1543b28e31f04fcf60@158.101.209.61:12656,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,5a223d77d01319a8c7f648eddfc8549cafcd8ca5@34.147.118.211:26656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,18603aa0e749211298227974b7d3b7724cb9bb8d@185.16.38.136:36656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,ff6df373bf7bce436d488d2d8f5f5b283c6431d4@51.79.100.160:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,6570de868d0f7a5b4dc9f5a007ba98319a7fa8b4@194.163.162.31:26656,16f40215d018c7d657fef0bb5ce2950251d525d2@148.251.51.144:36656,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656,922d76c72392b5b69c03a4ae56b3aba544ff1139@144.126.194.175:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,f6c7d753cc4544031e8e243841f687cae3f09abe@161.97.145.34:35656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,9444cf6e8cc3e452f8006acce0283d87ee663b7a@185.163.125.253:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
