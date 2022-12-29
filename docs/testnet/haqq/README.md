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

**live-peers** (24)
```
peers="077d5d9169efb4b070ce7895d680a9d2148d522c@195.201.195.40:36656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,fd53be6145264c86f2db22659141c925e119794c@138.201.155.226:12656,b9d04ade732a3bb91b91e279c36c6f2c12d522d3@109.107.187.78:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,de231cd155362b2687dca190a744bf839ce4ce63@23.88.112.123:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,7094f2c1ee04801b76159bd614eb5947ffc8c5d9@109.71.177.3:35656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,26f20a2f80a4738a30a9634947a3aae67da31be3@65.108.254.227:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,0760b7526738dac0af14b5e3d3b62e49c63dd490@185.154.14.142:26656,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,2fdcd211d7457390cc7de84dc5b87750f1ece442@121.4.161.226:35656,4ce8cd1e523f3a452e57008ca87ce30e7a56ec3f@195.46.164.196:46656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
