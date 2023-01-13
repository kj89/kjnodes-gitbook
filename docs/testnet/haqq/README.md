# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)


## Public endpoints

* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)

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

**live-peers** (28)
```bash
peers="d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,65bfa4b4b4b9accb9c0e0d46a1c07ae9a44a3a23@168.119.227.142:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,70c1b8334bf08fe5d56fb53d07da11f01faa560b@65.109.30.90:26656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,f1b1df46afd4c9d4f66051437078c0b85bc6b67b@65.108.206.118:61056,fed6ab9973f224f3b2334fd48fa835512d6311da@185.244.183.200:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,e576d332451c7c3c0c5c753b1bbd4e670b1ecfc7@5.161.97.83:26656,589f76a7932cf6d4ecf601a11ccc0a721b9a4ee4@65.109.85.170:29656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,0f5c320341a9134743f70f29dc99572977f97161@159.69.201.172:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,2ddd301131ac37ea58a390361cfaeb6701645ee5@114.218.165.119:35656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:21256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
