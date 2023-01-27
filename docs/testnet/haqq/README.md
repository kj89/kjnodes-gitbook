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

**live-peers** (33)
```bash
peers="6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,6237a5c1f154e0e41738f038e204c0c60d7ad8e0@65.108.250.241:56656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,88b8b733d8b96e9a518c1a8bea4dbc5bf896026e@5.161.156.183:26656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,f6c7d753cc4544031e8e243841f687cae3f09abe@161.97.145.34:35656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,589f76a7932cf6d4ecf601a11ccc0a721b9a4ee4@65.109.85.170:29656,ff6df373bf7bce436d488d2d8f5f5b283c6431d4@51.79.100.160:26656,16f40215d018c7d657fef0bb5ce2950251d525d2@148.251.51.144:36656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,0629018cef2e53288757381ffdc0b84cbb5931cc@95.216.1.249:26656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,077d5d9169efb4b070ce7895d680a9d2148d522c@195.201.195.40:36656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,922d76c72392b5b69c03a4ae56b3aba544ff1139@144.126.194.175:26656,9444cf6e8cc3e452f8006acce0283d87ee663b7a@185.163.125.253:35656,022360b6d3bbae324b0cca90f80f6322576e2b42@23.88.70.109:12656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
