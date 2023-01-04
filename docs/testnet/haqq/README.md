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

**live-peers** (31)
```
peers="62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,26f20a2f80a4738a30a9634947a3aae67da31be3@65.108.254.227:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656,077d5d9169efb4b070ce7895d680a9d2148d522c@195.201.195.40:36656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,2a73cde1925175ce2dcee61119baa7cbcb06e554@65.109.160.237:35656,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656,51e4544568cf880451bfffc292de88adc472f0e0@34.147.126.38:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,b09a7df87767ae782099d5ee352d679e3260247a@65.108.124.219:34656,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,bb9c3d1c6fb845602f9f595802765fc86a0f3b10@154.26.137.198:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,70c1b8334bf08fe5d56fb53d07da11f01faa560b@65.109.30.90:26656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,3ba8280c245f4d63a8f7913aea64a5071f0c76d7@65.109.18.166:54656,5b2ee53c742ce5d392b93c8f193f489a4f13f685@5.189.186.222:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
