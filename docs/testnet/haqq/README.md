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

**live-peers** (25)
```
peers="de231cd155362b2687dca190a744bf839ce4ce63@23.88.112.123:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,7094f2c1ee04801b76159bd614eb5947ffc8c5d9@109.71.177.3:35656,26f20a2f80a4738a30a9634947a3aae67da31be3@65.108.254.227:26656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,ccff2d110a06e8a76fd1529200d96316eb077007@65.108.78.116:46656,3f11b1e4dd940582ef03f0355959676e684b0370@65.108.87.238:26656,0760b7526738dac0af14b5e3d3b62e49c63dd490@185.154.14.142:26656,1e09d40584a277c72d6023e2956ff923c9d5e062@85.10.203.117:36656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,f319bad19fea5ac3608ffec97bffeee38abae069@147.182.228.205:35656,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
