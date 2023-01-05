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

**live-peers** (30)
```
peers="99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,2a73cde1925175ce2dcee61119baa7cbcb06e554@65.109.160.237:35656,b09a7df87767ae782099d5ee352d679e3260247a@65.108.124.219:34656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656,077d5d9169efb4b070ce7895d680a9d2148d522c@195.201.195.40:36656,62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,26f20a2f80a4738a30a9634947a3aae67da31be3@65.108.254.227:26656,0f56d6cd1eae6fd5de684bcc6ee63622e17436af@149.102.149.117:35656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
