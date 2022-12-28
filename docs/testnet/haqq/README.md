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

**live-peers** (28)
```
peers="de231cd155362b2687dca190a744bf839ce4ce63@23.88.112.123:26656,b09a7df87767ae782099d5ee352d679e3260247a@65.108.124.219:34656,5c11c697aaf2dabf96e3eb7e7e621c200bd309ee@65.21.225.58:26656,fed6ab9973f224f3b2334fd48fa835512d6311da@185.244.183.200:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,26f20a2f80a4738a30a9634947a3aae67da31be3@65.108.254.227:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,beb98c92f9f96802fd1edf091003b622a52fe646@164.68.108.129:26656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,7094f2c1ee04801b76159bd614eb5947ffc8c5d9@109.71.177.3:35656,43eed16b41b5ce970af5930f94e33dc0173aa679@84.46.243.26:35656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,dddce0afadf33e8b8c33a9e797493cd18a9ce5c7@154.26.157.240:35656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,4926c0ebb29341d9078dfd6cc13e07e7b37171e9@1.116.75.97:35656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,3e982cadd9956384478798f8ab1a686632be0fd4@149.102.156.102:35656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,b9d04ade732a3bb91b91e279c36c6f2c12d522d3@109.107.187.78:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
