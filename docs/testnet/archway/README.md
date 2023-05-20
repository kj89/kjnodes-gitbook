# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

Archway is an incentivized smart contract chain for Cosmos  ecosystem which gives developers a simple way to build  scalable cross-chain dapps. The developers automatically  receive rewards for their contributions to the network.

**Chain ID**: constantine-3 | **Latest Version Tag**: v0.5.2 | **Wasm**: ON

[Website](https://archway.io) | [Discord](https://discord.gg/archwayhq) | [Twitter](https://twitter.com/archwayhq)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/archway-testnet](https://explorer.kjnodes.com/archway-testnet)

## Public endpoints

* api: [https://archway-testnet.api.kjnodes.com](https://archway-testnet.api.kjnodes.com)
* rpc: [https://archway-testnet.rpc.kjnodes.com](https://archway-testnet.rpc.kjnodes.com)
* grpc: archway-testnet.grpc.kjnodes.com:15690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@archway-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@archway-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/archway-testnet/addrbook.json > $HOME/.archway/config/addrbook.json
```

**live-peers** (30)
```bash
peers="447644c34095606449e8f7eb34eeea2d9b7f2216@65.109.225.25:26656,6b137e1df61936010ea30a354d8abd7010598e29@35.239.130.141:26656,857515ed6ab05e8e59f74e1050cb9e653e899cac@159.223.220.1:26656,3a50537646a263ca11f8b29ab84ba556178b569c@46.4.68.113:27756,261acb73f483d1cace653cb54f7b8815f63b7e56@54.36.227.1:26656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,b6031525e988eefd03452807806f08b0e9bc3289@15.235.46.50:26656,d1334258b592ebccb85a917aa65976b74e254a60@65.109.65.248:31656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,13dc844645671d5da8ee81ab969d19166c3df11d@65.109.90.169:15656,b9ba5ae75fbdee6812d1aa53ff7154ed59938cbc@57.128.151.101:26656,7786f708c1851dd433a03f71ec3ff74d65895de7@34.31.130.235:26656,fc96980110a96ce6f60999650fef94aad673ead5@138.201.204.5:50656,8df8a64ecf0aaba1e1faee06d005aa912d578549@65.109.89.5:41656,3591dd903e95c9b25618f90c4a6bda63861ab8ec@65.109.92.79:45656,7e31ab391f5b5756a75dc18b5275b609c81a34ee@34.122.164.239:26656,f259ea40048744ccf6efcea92579a36a4b06035e@34.29.232.227:26656,35cff40de4efbb164d19e39f335d28bf7a301cff@65.109.89.18:44656,c96b16a81c780d840530c17fec6efd31b329c458@34.133.135.231:26656,eb70e2aaacbff6a3db3c63c9ff055d63df14c70b@34.228.170.40:26656,6d4f2faa284b9c9625e781309b637e92627b6afd@188.40.59.225:45656,b04ea6ef4d65ef56645e3adc6b94206a1800b553@65.108.206.74:34656,da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,3fa606cdc1ea323e19d7c09648a4f3666f0bc672@211.219.19.69:29656,6450606f42fce151ca3897d28ff81a908710f9ff@77.120.115.149:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,147c1668031ee62a85bd7293a845fdcf4f7b1857@222.211.225.0:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
