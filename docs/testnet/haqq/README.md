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

**live-peers** (20)
```bash
peers="32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,5a223d77d01319a8c7f648eddfc8549cafcd8ca5@34.147.118.211:26656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,ff6df373bf7bce436d488d2d8f5f5b283c6431d4@51.79.100.160:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,8558de1d3062319bb877316c5c33e704f1e0a972@84.46.242.147:26656,88b8b733d8b96e9a518c1a8bea4dbc5bf896026e@5.161.156.183:26656,077d5d9169efb4b070ce7895d680a9d2148d522c@195.201.195.40:36656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,54e81994c61bbb6c414f8ab0a606a7edda138a3b@95.216.154.100:26656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,9444cf6e8cc3e452f8006acce0283d87ee663b7a@185.163.125.253:35656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
