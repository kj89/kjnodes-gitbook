# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.2.1 | **Wasm**: OFF

Website: [https://islamiccoin.net](https://islamiccoin.net)


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

**live-peers** (10)
```
peers="ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,5f836eb8b9c600e8050bfcb025dc6234bf7d8796@65.108.9.230:26656,6570de868d0f7a5b4dc9f5a007ba98319a7fa8b4@194.163.162.31:26656,dae56b465293b5f122d795f742f87c6b16539acc@23.88.44.170:12656,7f4b4501af5f744210dcad95fb9b3915283fd0e9@185.244.182.203:26656,35e1bf6fda8a37c9c4872527a30b1fe26b0a155f@45.13.59.201:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
