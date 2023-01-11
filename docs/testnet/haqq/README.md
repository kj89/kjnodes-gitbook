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

**live-peers** (32)
```bash
peers="6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,589f76a7932cf6d4ecf601a11ccc0a721b9a4ee4@65.109.85.170:29656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,ce0942b9676206400a68ce8fcdb1b1bb76f88226@155.133.27.197:36656,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,5f836eb8b9c600e8050bfcb025dc6234bf7d8796@65.108.9.230:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,5dea057533b7f44c0a0092d2a2b1742aa52f5449@154.26.157.224:35656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,698728df4782759869a4ef9a5f6f6236cd575f5a@65.108.62.95:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,8e394150929e74e51fc097023420515ce77f7533@135.181.150.198:26656,3f11b1e4dd940582ef03f0355959676e684b0370@65.108.87.238:26656,0629018cef2e53288757381ffdc0b84cbb5931cc@95.216.1.249:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,7f4b4501af5f744210dcad95fb9b3915283fd0e9@185.244.182.203:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
