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

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (27)
```
peers="23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,9af0d63f02475fc5c4cf60723070ea735895b626@185.119.59.223:26656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,de231cd155362b2687dca190a744bf839ce4ce63@23.88.112.123:26656,c2e099196ba2dcebed50c66393a79bc13b43b698@78.29.44.119:26656,88fb8b08f2184cf9390826eeb470b8b693a7e68b@185.202.223.58:26656,7094f2c1ee04801b76159bd614eb5947ffc8c5d9@109.71.177.3:35656,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,0629018cef2e53288757381ffdc0b84cbb5931cc@95.216.1.249:26656,35e1bf6fda8a37c9c4872527a30b1fe26b0a155f@45.13.59.201:26656,de8e608c13d4c215fd5012f4b347fbe2217d722f@146.190.58.63:35656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
